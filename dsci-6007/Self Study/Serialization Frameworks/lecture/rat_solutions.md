RAT - Serialization Framework
----

1) Match the terms to all the concepts that apply? (Hint: Many-to-many relationships) <br>

Protocol Buffers 

- Optimized for serializing structured data  
- Works well with complex nested data structures

JSON

- Design for humans to easily read and write
- Works well with complex nested data structures

Parquet

- Optimized for serializing structured data  
- Geometric mosaic of wood pieces used for decorative effect 
- Works well with complex nested data structures

Avro

- Optimized for serializing structured data   
- Uses JSON for defining data types and protocols, and serializes data in a compact binary format
- Works well with complex nested data structures (arguable)

Thrift 

- Optimized for serializing structured data
- Works well with complex nested data structures (arguable)


2) Which of the following is the most compact representation. Why? <br>
&nbsp;&nbsp;&nbsp;&nbsp; - CSV <br>
&nbsp;&nbsp;&nbsp;&nbsp; - TSV <br>
&nbsp;&nbsp;&nbsp;&nbsp; - JSON <br>
&nbsp;&nbsp;&nbsp;&nbsp; - __Parquet__ <br>
&nbsp;&nbsp;&nbsp;&nbsp; - [Roman Numerals](http://imgs.xkcd.com/comics/iso_8601.png) <br>

<br>

3) Which data format is the best for storing data on HDFS. Why? <br>
&nbsp;&nbsp;&nbsp;&nbsp; - Protocol buffers <br>
&nbsp;&nbsp;&nbsp;&nbsp; - __Avro__ <br>
&nbsp;&nbsp;&nbsp;&nbsp; - FLAC <br>
&nbsp;&nbsp;&nbsp;&nbsp; - Cuneiform <br>

4) Which one is optimized for columnar storage? Why? <br>
&nbsp;&nbsp;&nbsp;&nbsp; - __Parquet__ <br>
&nbsp;&nbsp;&nbsp;&nbsp; - Protocol buffers <br>
&nbsp;&nbsp;&nbsp;&nbsp; - Doric <br>
&nbsp;&nbsp;&nbsp;&nbsp; - Corinthian <br>

5) What makes columnar storage a good fit for read-centric, analytic loads?

bytes are disk are sequenctial for columns, thus minizing random access reads
predicate push-down