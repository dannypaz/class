import happybase

# connect to the Thrift server & reference a table:
connection = happybase.Connection('127.0.0.1')
table = connection.table('access-logs')

# fetch data by row and column:
print table.row('elton|jericho|201511')
print table.row('elton|jericho|201511', ['t'])
print table.row('elton|jericho|201511', ['t:1106'])

# fetch multiple rows and filter by column name:
print table.rows(['elton|jericho|201511', 'elton|jericho|201510'])
print table.rows(['elton|jericho|201511', 'elton|jericho|201510'], ['t:1106'])

# fetch multiple versions of a cell:
versionedTable = connection.table('with-custom-config')
print versionedTable.cells('rk1', 'cf1:data', 3)
print versionedTable.cells('rk1', 'cf1:data', 3, include_timestamp=True)

# reading counter columns:
counterTable = connection.table('counters')
print counterTable.row('rk1')
print counterTable.counter_get('rk1', 'c:1')

# iterating through a scanner:
access_logs = connection.table('access-logs')
scanner = access_logs.scan('elton|jericho|201510', 'elton|jericho|x')
for key, data in scanner:
    print key, data

# scanning by row prefix:
scanner = access_logs.scan(row_prefix='elton|jericho|', columns=['t:1106'])
for key, data in scanner:
    print key, data

# scanning rows and filtering columns:
access_logs = connection.table('access-logs')
scanner = access_logs.scan('elton|jericho|201510', 'elton|jericho|x', filter="ColumnPrefixFilter('11')")
for key, data in scanner:
    print key, data

# writing data:
access_logs.put('elton|jericho|201511', {'t:1309':'400', 't:1310':'200'})
print access_logs.row('elton|jericho|201511', ['t:1309', 't:1310'])

# writing data in batches:
with access_logs.batch() as batch:
    batch.put('elton|jericho|201512', {'t:0110':'200'})
    batch.put('elton|jericho|201512', {'t:0210':'120', 't:0211':'360'})
print access_logs.row('elton|jericho|201512')

# incrementing counters:
counterTable.counter_get('rk1', 'c:1')
counterTable.counter_inc('rk1', 'c:1')
counterTable.counter_inc('rk1', 'c:1', 100)
print counterTable.counter_get('rk1', 'c:1')
