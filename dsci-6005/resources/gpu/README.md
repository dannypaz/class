Graphics Processing Unit (GPUs)
----

Preparation Material
---------

| Source | Title | Notes | Priority |
| ------ | ----- | ----- | -------- |
| [Bitcoin Wiki](https://en.bitcoin.it/wiki/Main_Page) | [Why a GPU Mines Faster Than a CPU](https://en.bitcoin.it/wiki/Why_a_GPU_mines_faster_than_a_CPU) | replace "mines" with "matrix multiplies" | Introductory
| [Quora](https://www.quora.com/) | [Why Are GPUs More Powerful Than CPUs?](https://www.quora.com/Why-are-GPUs-more-powerful-than-CPUs) | | Introductory
| [Wikipedia](https://en.wikipedia.org/wiki/Main_Page) | [Embarrassingly Parallel](https://en.wikipedia.org/wiki/Embarrassingly_parallel) | | Introductory
| [Wikipedia](https://en.wikipedia.org/wiki/Main_Page) | [Graphics Processing Unit](https://en.wikipedia.org/wiki/Graphics_processing_unit) | | Introductory
| [Wikipedia](https://en.wikipedia.org/wiki/Main_Page) | [Parallel Algorithm](https://en.wikipedia.org/wiki/Parallel_algorithm) | | Introductory
| [Quant Start](https://www.quantstart.com/) | [Matrix-Matrix Multiplication on the GPU with Nvidia-CUDA](https://www.quantstart.com/articles/Matrix-Matrix-Multiplication-on-the-GPU-with-Nvidia-CUDA) | | Introductory
| [cs231n](http://cs231n.stanford.edu/index.html) | [ConvNets in Practice](https://www.youtube.com/watch?v=ue4RJdI8yRA&index=11&list=PLlJy-eBtNFt6EuMxFYRiNRS07MCWN5UIA) | start at 49:43 | **Required** |
| [The Economist](http://www.econmist.com/) | [The Rise of Artificial Intelligence is Creating New Variety in the Chip Market, and Trouble for Intel](http://www.economist.com/news/business/21717430-success-nvidia-and-its-new-computing-chip-signals-rapid-change-it-architecture) | | **Required**
| [Quora](https://www.quora.com/) | [Why are GPUs Well-Suited to Deep Learning?](https://www.quora.com/Why-are-GPUs-well-suited-to-deep-learning) | read Tim Dettmer's answer | **Required**
| [Tim Dettmers](http://timdettmers.com/) | [Which is the Best GPU for Deep Learning?](http://timdettmers.com/2014/08/14/which-gpu-for-deep-learning/) | | Optional
| [Tim Dettmers](http://timdettmers.com/) | [A Full Hardware Guide to Deep Learning](http://timdettmers.com/2015/03/09/deep-learning-hardware-guide/) | | Optional
| | [Guide to setting up GPUs on Mac laptop](https://gist.github.com/Mistobaan/dd32287eeb6859c6668d) | | Optional |
| fast.ai | [Another guide to setting up GPUs on AWS](http://course.fast.ai/lessons/aws.html) | | Optional |
| | [| fast.ai |](https://medium.com/@mateuszsieniawski/keras-with-gpu-on-amazon-ec2-a-step-by-step-instruction-4f90364e49ac#.jescztubp)  | | Optional |
| keras blog | [Yet Another guide to setting up GPUs on AWS](https://blog.keras.io/running-jupyter-notebooks-on-gpu-on-aws-a-starter-guide.html) | | Optional |

------
Configuring EC2 Instance for GPU Usage
------

1. Visit Amazon [EC2 Dashboard](https://us-west-1.console.aws.amazon.com/ec2/v2/home?region=us-west-1)
2. Click `Launch Instance`
3. Select `Community AMIs`
4. Type *deep learning* in the search box and hit enter
5. `Select` the **vict0rsch-1.0 - ami-10762170** AMI
6. Select the **g2.2xlarge** instance type then click `Review and Launch`
7. Click `Launch`
8. Create a new key pair if you don't already have a key. Otherwise select an existing key pair and click `Launch Instances`
9. Click `View Instances`
9. Log into your newly created instance (with the user `ubuntu`)

Configuring Tensorflow
------

1. Clone this repo
2. Create a new anaconda environment with `resources/environment.yml`
3. Start up an `ipython` session and execute

 ```python
In [1]: import tensorflow as tf
I tensorflow/stream_executor/dso_loader.cc:128] successfully opened CUDA library libcublas.so locally
I tensorflow/stream_executor/dso_loader.cc:128] successfully opened CUDA library libcudnn.so locally
I tensorflow/stream_executor/dso_loader.cc:128] successfully opened CUDA library libcufft.so locally
I tensorflow/stream_executor/dso_loader.cc:128] successfully opened CUDA library libcuda.so.1 locally
I tensorflow/stream_executor/dso_loader.cc:128] successfully opened CUDA library libcurand.so locally

In [2]: sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:936] successful NUMA node read from SysFS had negative value (-1), but there m
ust be at least one NUMA node, so returning NUMA node zero
I tensorflow/core/common_runtime/gpu/gpu_device.cc:885] Found device 0 with properties:
name: GRID K520
major: 3 minor: 0 memoryClockRate (GHz) 0.797
pciBusID 0000:00:03.0
Total memory: 3.94GiB
Free memory: 3.91GiB
I tensorflow/core/common_runtime/gpu/gpu_device.cc:906] DMA: 0
I tensorflow/core/common_runtime/gpu/gpu_device.cc:916] 0:   Y
I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GRID K520, pci bus i
d: 0000:00:03.0)
Device mapping:
/job:localhost/replica:0/task:0/gpu:0 -> device: 0, name: GRID K520, pci bus id: 0000:00:03.0
I tensorflow/core/common_runtime/direct_session.cc:255] Device mapping:
/job:localhost/replica:0/task:0/gpu:0 -> device: 0, name: GRID K520, pci bus id: 0000:00:03.0
```

 If your output looks like this, congratulations! Tensorflow will now be able to use the gpu for very fast computations. Let's have tensorflow train an MLP to classify MNIST digits to make sure everything is copacetic.

4. Download `mnist_mlp.py` by executing

 ```shell
(py36) ubuntu@ip-172-31-13-217:~$ wget https://raw.githubusercontent.com/fchollet/keras/master/examples/mnist_mlp.py
--2017-03-05 03:38:47--  https://raw.githubusercontent.com/fchollet/keras/master/examples/mnist_mlp.py
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 151.101.40.133
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|151.101.40.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1727 (1.7K) [text/plain]
Saving to: ‘mnist_mlp.py’

mnist_mlp.py                      100%[==========================================================>]   1.69K  --.-KB/s    in 0s

2017-03-05 03:38:47 (384 MB/s) - ‘mnist_mlp.py’ saved [1727/1727]
```

5. Finally, run `mnist_mlp.py` with

```shell
(py36) ubuntu@ip-172-31-13-217:~$ python mnist_mlp.py
Using TensorFlow backend.
60000 train samples
10000 test samples
____________________________________________________________________________________________________
Layer (type)                     Output Shape          Param #     Connected to
====================================================================================================
dense_1 (Dense)                  (None, 512)           401920      dense_input_1[0][0]
____________________________________________________________________________________________________
activation_1 (Activation)        (None, 512)           0           dense_1[0][0]
____________________________________________________________________________________________________
dropout_1 (Dropout)              (None, 512)           0           activation_1[0][0]
____________________________________________________________________________________________________
dense_2 (Dense)                  (None, 512)           262656      dropout_1[0][0]
____________________________________________________________________________________________________
activation_2 (Activation)        (None, 512)           0           dense_2[0][0]
____________________________________________________________________________________________________
dropout_2 (Dropout)              (None, 512)           0           activation_2[0][0]
____________________________________________________________________________________________________
dense_3 (Dense)                  (None, 10)            5130        dropout_2[0][0]
____________________________________________________________________________________________________
activation_3 (Activation)        (None, 10)            0           dense_3[0][0]
====================================================================================================
Total params: 669,706
Trainable params: 669,706
Non-trainable params: 0
____________________________________________________________________________________________________
Train on 60000 samples, validate on 10000 samples
Epoch 1/20
W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE3 instructions, but these are available on your machine and could speed up CPU computations.
W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.1 instructions, but these areavailable on your machine and could speed up CPU computations.
W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these areavailable on your machine and could speed up CPU computations.
W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX instructions, but these are available on your machine and could speed up CPU computations.
60000/60000 [==============================] - 7s - loss: 0.2442 - acc: 0.9244 - val_loss: 0.1189 - val_acc: 0.9630
Epoch 2/20
60000/60000 [==============================] - 7s - loss: 0.1006 - acc: 0.9695 - val_loss: 0.0771 - val_acc: 0.9767
Epoch 3/20
60000/60000 [==============================] - 7s - loss: 0.0748 - acc: 0.9776 - val_loss: 0.0775 - val_acc: 0.9769
Epoch 4/20
60000/60000 [==============================] - 7s - loss: 0.0598 - acc: 0.9822 - val_loss: 0.0761 - val_acc: 0.9793
Epoch 5/20
60000/60000 [==============================] - 7s - loss: 0.0515 - acc: 0.9848 - val_loss: 0.0953 - val_acc: 0.9781
Epoch 6/20
60000/60000 [==============================] - 7s - loss: 0.0430 - acc: 0.9873 - val_loss: 0.0933 - val_acc: 0.9781
Epoch 7/20
60000/60000 [==============================] - 8s - loss: 0.0395 - acc: 0.9885 - val_loss: 0.0828 - val_acc: 0.9814
Epoch 8/20
60000/60000 [==============================] - 8s - loss: 0.0338 - acc: 0.9900 - val_loss: 0.0933 - val_acc: 0.9811
Epoch 9/20
60000/60000 [==============================] - 8s - loss: 0.0318 - acc: 0.9905 - val_loss: 0.0916 - val_acc: 0.9820
Epoch 10/20
60000/60000 [==============================] - 8s - loss: 0.0296 - acc: 0.9916 - val_loss: 0.0951 - val_acc: 0.9797
Epoch 11/20
60000/60000 [==============================] - 8s - loss: 0.0273 - acc: 0.9923 - val_loss: 0.0901 - val_acc: 0.9825
Epoch 12/20
60000/60000 [==============================] - 8s - loss: 0.0252 - acc: 0.9929 - val_loss: 0.0864 - val_acc: 0.9840
Epoch 13/20
60000/60000 [==============================] - 8s - loss: 0.0239 - acc: 0.9935 - val_loss: 0.0885 - val_acc: 0.9839
Epoch 14/20
60000/60000 [==============================] - 8s - loss: 0.0242 - acc: 0.9937 - val_loss: 0.0969 - val_acc: 0.9826
Epoch 15/20
60000/60000 [==============================] - 8s - loss: 0.0204 - acc: 0.9939 - val_loss: 0.0970 - val_acc: 0.9829
Epoch 16/20
60000/60000 [==============================] - 8s - loss: 0.0202 - acc: 0.9947 - val_loss: 0.0977 - val_acc: 0.9837
Epoch 17/20
60000/60000 [==============================] - 8s - loss: 0.0188 - acc: 0.9951 - val_loss: 0.1115 - val_acc: 0.9824
Epoch 18/20
60000/60000 [==============================] - 8s - loss: 0.0189 - acc: 0.9950 - val_loss: 0.0959 - val_acc: 0.9842
Epoch 19/20
60000/60000 [==============================] - 8s - loss: 0.0178 - acc: 0.9953 - val_loss: 0.1076 - val_acc: 0.9823
Epoch 20/20
60000/60000 [==============================] - 8s - loss: 0.0183 - acc: 0.9952 - val_loss: 0.0979 - val_acc: 0.9851
Test score: 0.0979186110775
Test accuracy: 0.9851
```

Each epoch should only take about 8 seconds and you should get a test accuracy of about 98.5%.
