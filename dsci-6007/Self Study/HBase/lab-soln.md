Lab
===

Step 1: Install HBase
---------------------

Install HBase on your machine.

Bring it up in *standalone* mode.

Bring up the HBase shell.

Type `puts "hello world"` and see that it works.

Follow the steps in the lecture notes.

Step 2: Download Data
---------------------

Download stock data for these companies: AAPL, AMZN, GOOG, MSFT

Here is how to get the stock for AAPL, for example:

<http://real-chart.finance.yahoo.com/table.csv?s=AAPL&g=d&ignore=.csv>

```bash
# Download CSV files for all companies.
for SYMBOL in AAPL AMZN GOOG MSFT; do
  echo "${SYMBOL}: Writing ${SYMBOL}.csv"
  URL="http://real-chart.finance.yahoo.com/table.csv?s=${SYMBOL}&g=d&ignore=.csv"
  curl -L ${URL} > ${SYMBOL}.csv
done
```

Step 3: Design Row Key
----------------------

Design a row key schema for storing this data in HBase. 

Your goal is to calculate the minimum/maximum/average prices for each
company over the period covered in the data.

- The columns in the data are: `Date,Open,High,Low,Close,Volume,Adj Close`.

- The row key for this query should be: `stock:date`.

- This will allow us to scan for date ranges for a specific stock.

Step 4: Upload Data
-------------------

Using the lecture notes as a guide create a HBase shell script to
upload the CSV data into HBase.

```ruby
# Create sales table.
create 'prices', 'd'

# Import CSV.
require 'csv'

# Insert data using loop.
stocks = ['AAPL','AMZN','GOOG','MSFT']
for stock in stocks
  puts "--> Inserting #{stock}"
  path = ENV['HOME'] + '/tmp/hbase/' + stock + '.csv'
  CSV.foreach(path) do |date,open,high,low,close,volume,adj| 
    if date.start_with? 'Date' then 
      next
    end
    key = stock + ":" + date
    put 'prices', key, 'd:date',date
    put 'prices', key, 'd:open',open
    put 'prices', key, 'd:high',high
    put 'prices', key, 'd:low',low
    put 'prices', key, 'd:close',close
    put 'prices', key, 'd:volume',volume
    put 'prices', key, 'd:adj',adj
  end
end

# Use count to see how many rows are there inserted.
count 'prices'

# Scan individual stocks.
scan 'prices', {STARTROW=>'AAPL:',STOPROW=>'AAPL;'}
scan 'prices', {STARTROW=>'AMZN:',STOPROW=>'AMZN;'}
scan 'prices', {STARTROW=>'GOOG:',STOPROW=>'GOOG;'}
scan 'prices', {STARTROW=>'MSFT:',STOPROW=>'MSFT;'}
```

Step 5: Calculate Statistics
----------------------------

Use `scan` (or the `range` function in `hbase-jruby`) to go through
the data for each company and calculate the minimum, maximum, and
average prices for each company across all time.

```ruby
# Load library.
$LOAD_PATH << ENV['HOME'] + '/hbase-jruby/lib'
require 'hbase-jruby'

# Get table.
hbase = HBase.new
prices = hbase.table('prices')

# Find stats for each stock.
stocks = ['AAPL','AMZN','GOOG','MSFT']
for stock in stocks
  min = + Float::MAX
  max = - Float::MIN
  count = 0
  total = 0.0

  # Scan prices.
  prices.range(stock+':' .. stock+';').each do 
    |row| 

    # Extract fields.
    date   = row.string('d:date')
    adj    = row.string('d:adj').to_f

    # Calculate min, max, total.
    min = [adj,min].min
    max = [adj,max].max
    total += adj
    count += 1
  end

  # Compute stats.
  avg = total/count
  puts "#{stock} Avg = #{avg}"
  puts "#{stock} Min = #{min}"
  puts "#{stock} Max = #{max}"

end
```

Step 6: Row Key Redesign 
------------------------

Suppose the hedge fund you work for, HedgeBase, now wants to create an
index fund based on the stocks of these companies. Each share of the index
fund is made up of exactly one share of the constituent companies.

They want to use HBase to calculate the minimum/maximum/average price
of this index fund.

What row key should they use? 

Design the system that would calculate the minimum, maximum, and
average price of the index fund per month.

- The row key in this case must be `date:stock`
