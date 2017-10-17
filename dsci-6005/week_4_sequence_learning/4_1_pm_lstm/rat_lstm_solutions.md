RAT: RNN & LSTM
----

1) Recurrent Neural Network takes in __sequential__ data, maintains the __context__ of the data, and learns __temporal patterns__.

2) Label this LSTM cell / node:

![](lstm_node_labelded.png)

3) List 1 specific applications for RNN/LSTM, not discussed in class

Recognize patterns in sequences of data:
- text
- genomes
- handwriting
- the spoken word
- music
- video
- language modeling
- translation
- numerical times series data emanating from sensors
- image captioning (w/ CNN)

----
Challenge Questions
-----

1) At every time step, the stored information (state) is multiplied by a matrix to generate the next state.

If the matrix is not absolutely optimal (and nothing is absolutely optimal in machine learning), it will slowly decay what's stored in the state. After a few hundred iterations, the original information is probably not recoverable anymore.

2) 
LSTMs are better because the connections essentially makes remembering information the "default action" at each timestep, and the network needs to learn to change the content of the cells.

[Source](https://www.quora.com/Why-is-it-difficult-for-recurrent-neural-networks-to-store-information-for-very-long)

----
Extra questions

2. In general, why do RNN require more data than CNN?
A more complex model.