Real-Time Bart Arrival, Capacity, and forecast

- Below is an overview of the architecture for my final project


# Robustness and fault tolerance
- The system can create backup ec2 instances in case one goes down.
# Low latency reads and updates
- Spark has very low latency


# Scalability
- Checks such as
autoscaling (http://docs.aws.amazon.com/autoscaling/latest/userguide/WhatIsAutoScaling.html)
can ensure that the website hosting the EC2 instance does not go down. Or, when
additional traffic comes to the website, additional servers can spin up
to handle the load.

# Generalization
- Although this system will be used for predicting percent capacity, the data
stored in s3 can be used for additional data science questions.

# Extensibility
- This system can be used across any Ec2 instance. In addition, a vagrant file
can be used to keep the configuration ready to spin up another server.

# Ad hoc queries
- With all of the data being stored in Postgres, a user can write custom queries
to ask different questions of historical data than is being asked currently

# Minimal Maintenance
- With airflow, emails can be sent in case of errors in completing tasks.

# Debuggability
- data structures will be immutable in this system. Therefore, it will be easier
to debug what things go wrong.
- Also, the try except blocks will help catch errors in the system.
