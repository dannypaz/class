Designing Big Data Systems
-----------------

By now you should have at least two-weeks' worth of data from your data source. That's all well and good, but data is worthless on it's own. An S3 bucket full of logs does not a data scientist make. So we've got the data, now it's time for some engineering.

The purpose of this project is to provide a platform for data science projects. It might be helpful to think of yourself two months ago: what would you have wanted (though perhaps not known that you would have wanted) in order to do a statistical analysis or train a model based on this data?

You should come up with (at least) one simple data science application that your platform can run as a proof of concept. But keep in mind, the application itself is not the important part. Rather: the _ability_ and _ease_ with which that application can be developed is what we are going for.

What does that mean? Watch [Runaway Complexity in Big Data Systems...and a Plan to Stop it](https://www.youtube.com/watch?v=ucHjyb6jv08). This talk is already half-a-decade old but the core principles behind it remain viable today. After watching that video, consider the 8 "Desired properties of a Big Data system" outlined in Nathan Marz' [Big Data](https://manning-content.s3.amazonaws.com/download/3/4142054-00c8-4115-879e-946c643f3665/big-data-ch01.pdf)) and ask yourself how well does your architecture embody to these properties?

### Robustness and fault tolerance

> Building systems that "do the right thing" is difficult in the face of the challenges of distributed systems. Systems need to behave correctly despite machines going down randomly, the complex semantics of consistency in distributed databases, duplicated data, concurrency, and more. These challenges make it difficult even to reason about what a system is doing. Part of making a Big Data system robust is avoiding these complexities so that you can easily reason about the system.

### Low latency reads and updates

> The vast majority of applications require reads to be satisfied with very low latency, typically between a few milliseconds to a few hundred milliseconds. On the other hand, the update latency requirements vary a great deal between applications. Some applications require updates to propagate immediately, but in other applications a latency of a few hours is fine. Regardless, you need to be able to achieve low latency updates _when you need them_ in your Big Data systems. More importantly, you need to be able to achieve low latency reads and updates without compromising the robustness of the system.

### Scalability

> Scalability is the ability to maintain performance in the face of increasing data or load by adding resources to the system. [Your architecture should be] horizontally scalable across all layers of the system stack: scaling is accomplished by adding more machines.

### Generalization

> A general system can support a wide range of applications. Indeed, this book wouldn’t be very useful if it didn’t generalize to a wide range of applications! Because the Lambda Architecture is based on functions of all data, it generalizes to all applications, whether financial management systems, social media analytics, scientific applications, social networking, or anything else.

### Extensibility

> You don’t want to have to reinvent the wheel each time you add a related feature or make a change to how your system works. Extensible systems allow functionality to be added with a minimal development cost.

### Ad hoc queries

> Being able to do ad hoc queries on your data is extremely important. Nearly every large dataset has unanticipated value within it. Being able to mine a dataset arbitrarily gives opportunities for business optimization and new applications. Ultimately, you can’t discover interesting things to do with your data unless you can ask arbitrary questions of it.

### Minimal maintenance

> Maintenance is a tax on developers. Maintenance is the work required to keep a system running smoothly. This includes anticipating when to add machines to scale, keeping processes up and running, and debugging anything that goes wrong in production.
>
> An important part of minimizing maintenance is choosing components that have as little _implementation complexity_ as possible. You want to rely on components that have simple mechanisms underlying them. In particular, distributed databases tend to have very complicated internals. The more complex a system, the more likely something will go wrong, and the more you need to understand about the system to debug and tune it.

### Debuggability

> A Big Data system must provide the information necessary to debug the system when things go wrong. The key is to be able to trace, for each value in the system, exactly what caused it to have that value.
>
> "Debuggability" is accomplished in the Lambda Architecture through the functional nature of the batch layer and by preferring to use recomputation algorithms when possible.
