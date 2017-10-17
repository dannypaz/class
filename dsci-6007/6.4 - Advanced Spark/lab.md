Structuring Your Data
---------------------

Recall that the 3rd characteristic in the [Project Proposal](../6.1 - Proposals/lab.md#final-project-proposal) requirements is **Structure**: Separate storage for structured data in 3NF. By now you have seen how to do that for the Twitter data we've been using so far in this course.

This assignment (due Monday) is to provide code to do the same thing (normalize and store) to your own data. You may either serialize it in [Parquet](https://parquet.apache.org/) (for use with Spark SQL) or save it as a CSV (to `copy` it into RDS). (_N.B._ If you do the latter make sure not to include a header.) Later, you may decide to insert the data into RDS directly from your Spark cluster (if so, do _not_ try to do this using a `map`, you will be essentially issuing a DDoS attack on your database), but for now, use S3 as a staging area.

Make the bucket where you store these data publicly accessible so that we can check your results.

This assignment has two deliverables:

1. URL of S3 datasets
    - 1 for each source (unstructured)
    - 1 for each data frame (structured, normalized)
2. Code in your repo (in this folder)

Also, if you have not already provided a schema, or if you've revised it, make sure to submit that as well.
