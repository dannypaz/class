#! usr/bin/env python
import requests
from lxml import etree
from StringIO import StringIO
import pandas as pd
import datetime
import pytz
import time
from collections import defaultdict
import yaml
import os
import argparse
from bart_station_list import bart_stations_dict
import time
import datetime
import boto3
import numpy as np
__author__ = 'Jonathan Hilgart'


def bart_xml_parser():
    """Parse the xml for the bart api. Return one pandas dataframes. This
    dateframe will be split per train direction for every car and time.
    If there are not three time projections for a given train a
    default estimate of 90 minutes is given."""
    # http://www.blog.pythonlibrary.org/2010/11/20/python-parsing-xml-with-lxml/
    credentials = yaml.load(open(os.path.expanduser(
        '~/data_engineering_final_credentials.yml')))
    # add in the terminal arguments to the payload for the bart api
    client = boto3.client('firehose', region_name='us-east-1')
    direction_options = ['n', 's']
    for name, station_abr in bart_stations_dict.iteritems():  # every station
        for direction in direction_options:
            bart_key = credentials['bart'].get('key')
            payload = {'cmd': 'etd', 'orig': station_abr,
                       'dir': direction, 'key': bart_key}
            # http://api.bart.gov/api/etd.aspx?cmd=etd&orig=12th&key=MW9S-E7SL-26DU-VV8V
            r = requests.get('http://api.bart.gov/api/etd.aspx',
                params = payload)
            content = r.content

            # parse the XML returned by the BART api
            tree = etree.parse(StringIO(content))
            context = etree.iterparse(StringIO(content))
            destination_station = ''
            destination_minutes = defaultdict(list)
            destination_train_size = defaultdict(list)
            train_size = defaultdict(list)
            minutes = defaultdict(list)
            direction = defaultdict(list)
            destination = defaultdict(list)
            bike_flag = defaultdict(list)
            color = defaultdict(list)
            bart_origination_station = defaultdict(list)
            origin_station = ''
            current_destination = ''
            current_time = ''
            current_date = ''
            date = defaultdict(list)
            time_current = defaultdict(list)
            unix_time = defaultdict(list)
            timestamp_unix = int(time.time())
            for action, elem in context:  # go through the xml returned
                if not elem.text:
                    text = "None"
                else:
                    text = elem.text
                if elem.tag == 'name':
                    origin_station = text
                elif elem.tag == 'destination':
                    current_destination= text
                    destination_minutes[destination_station] = []
                    destination_train_size[destination_station] = []
                elif elem.tag == 'minutes':
                    if text == 'Leaving':  # This train is leaving now!
                        destination_minutes[destination_station].append(0)
                        minutes['minutes'].append(0)
                    else:
                        destination_minutes[destination_station].append(
                            int(text))
                        minutes['minutes'].append(int(text))
                elif elem.tag == 'length':
                    destination_train_size[destination_station].append(
                        int(text))
                    train_size['train_size'].append(int(text))
                    destination['destination'].append(current_destination)
                    date['date'].append(current_date)
                    time_current['time'].append(current_time)
                    unix_time['unix_time'].append(timestamp_unix)
                    bart_origination_station['origin_station'].append(
                        origin_station)
                elif elem.tag == 'direction':
                    direction['direction'].append(text)
                elif elem.tag == 'destination':
                    current_destination = text
                elif elem.tag == 'bikeflag':
                    bike_flag['bike_flag'].append(text)
                elif elem.tag == 'color':
                    color['color'].append(text)
                elif elem.tag =='date':
                    current_date = text
                elif elem.tag == 'time':
                    current_time = text
            for k, v in destination_minutes.iteritems():
                # check if there are not the same number of trains coming
                if len(v) < 3:
                    [destination_minutes[k].append(90)
                     for _ in range(3-len(v))]
            for k, v in destination_train_size.iteritems():
                # check if there are not the same number of trains coming
                if len(v) < 3:
                    [destination_train_size[k].append(v[0]) for _ in range(3-len(v))]
            destination_minutes_df = pd.DataFrame(destination_minutes)
            destination_train_size_df = pd.DataFrame(destination_train_size)
            origin_location_df = pd.DataFrame(bart_origination_station)
            train_size_df = pd.DataFrame(train_size)
            minutes_df = pd.DataFrame(minutes)
            direction_df = pd.DataFrame(direction)
            destination_df = pd.DataFrame(destination)
            bike_df = pd.DataFrame(bike_flag)
            color_df = pd.DataFrame(color)
            time_df = pd.DataFrame(time_current)
            date_df = pd.DataFrame(date)
            unix_time_df = pd.DataFrame(unix_time)
            final_df = pd.concat([train_size_df, minutes_df, direction_df,
                             destination_df,bike_df, color_df, time_df, date_df,
                             unix_time_df, origin_location_df],
                            join='outer',axis=1)
            # calculate number of people and time or arrival
            final_df['arrival_time'] = np.nan
            # assume each bart train can hold 200 people
            # http://www.bart.gov/about/history/cars
            final_df['capacity'] = np.nan
            final_df['minutes_til_arrival'] = np.nan
            try:
                final_df['minutes_til_arrival'] =  \
                    final_df['minutes'].apply(lambda x:
                                                  pd.Timedelta(x,unit='m'))
            except KeyError:  ## there is not train arriving
                continue
            # Find when bart will arrive in SF time
            arrival_data_bart_one = []
            for idx, row in enumerate(final_df['time']):
                arrival_data_bart_one.append(
                    row+final_df['minutes_til_arrival'][idx])
            final_df['arrival_time'] = arrival_data_bart_one
            # calculate capacity
            final_df['capacity'] = final_df['train_size']*200
            # push to kinesis
            client.put_record(
                         DeliveryStreamName='bart-data-collection',
                                Record={'Data': final_df.to_json() + "\n"})

if __name__ == "__main__":
    bart_xml_parser()
