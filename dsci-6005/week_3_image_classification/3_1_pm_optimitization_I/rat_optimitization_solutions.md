RAT: Optimitization I
----

1. "all" vs "some" Batch gradient descent uses the entire dataset. Mini-batch Stochastic gradient  is estimated only with respect to a small sample.

2. SGD is a first order optimization method. It only use 1st deveriate, no other curvative information, and can get stuck in a local mimum.

3. It is hard to build "n-dimensional" wall. As dimensions increase, there are more opportunities (i.e., axises) to escape and continue to descend.

------

1. It is 2^7. GPU optimitization. Fewer cache misses.
> By ensuring the texture dimensions are a power of two, the graphics pipeline can take advantage of optimizations related to efficiencies in working with powers of two. For example, it can be (and absolutely was several years back before we had dedicated GPUs and extremely clever optimizing compilers) faster to divide and multiply by powers of two. Working in powers of two also simplified operations within the pipeline, such as computation and usage of mipmaps (a number that is a power of two will always divide evenly in half, which means you don't have to deal with scenarios where you must round your mipmap dimensions up or down).
http://gamedev.stackexchange.com/questions/26187/why-are-textures-always-square-powers-of-two-what-if-they-arent

It's true you "waste" some space this way, but the extra space is usually worth it for the tradeoff in render performance. Additionally there are techniques, such as compression or packing multiple images into a single texture space that can alleviate some of the storage waste.

2) new_parameters = old_parameters + (momentum * velocity) - (learning_rate*gradient_new_location)

3) Nesterov Accelerated Gradient (NAG) takes the "gamble -> correction" approach. It calculates the parameter updates based on standard momentum then finds the gradient from that location. It makes an actual move to that paramater location.
