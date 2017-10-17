RAT: Review
----

1. ![](https://keon.io/images/deep-q-learning/rl.png)
2. It is a RNN (Recurrent neural networks ). The loop represents past information.
3. LSTMs are Long Short Term Memory networks. They are a special kind of Recurrent neural network (RNN), capable of learning __long-term__ dependencies.
4.
5. 
![](https://oshearesearch.com/wp-content/uploads/2016/07/mnist_gan.png)

GANs have not been applied to NLP because GANs are only defined for real-valued data.

GANs work by training a generator network that outputs synthetic data, then running a discriminator network on the synthetic data. The gradient of the output of the discriminator network with respect to the synthetic data tells you how to slightly change the synthetic data to make it more realistic.

You can make slight changes to the synthetic data only if it is based on continuous numbers. If it is based on discrete numbers, there is no way to make a slight change.

For example, if you output an image with a pixel value of 1.0, you can change that pixel value to 1.0001 on the next step.

If you output the word "penguin", you can't change that to "penguin + .001" on the next step, because there is no such word as "penguin + .001". You have to go all the way from "penguin" to "ostrich".

Since all NLP is based on discrete values like words, characters, or bytes, no one really knows how to apply GANs to NLP yet.
https://www.reddit.com/r/MachineLearning/comments/40ldq6/generative_adversarial_networks_for_text/