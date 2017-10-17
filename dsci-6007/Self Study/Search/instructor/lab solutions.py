# Elastic Lab solutions

# Refactor curl to use requests
term = 'dilbert'
r = requests.get('http://localhost:9200/blog/post/_search?q=user:{0}&pretty=true'.format(term))
pprint(r.json())

# Test results set
results = r.json()
assert (results['_shards']['successful'] == results['_shards']['total'] ) and (results['time_out'] is False)