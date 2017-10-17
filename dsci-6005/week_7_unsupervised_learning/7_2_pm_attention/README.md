GalvanizeU-University of New Haven <br> Master of Science in Data Science <br> DSCI6005: Deep Learning
----

![](resources/images/dl_tweet.png)

Table of Contents:
----
- [Logistics](#logistic)
- [Course Description](#course-description)
- [Class Structure](#class-structure)
- [Grades](#grades)
- [Course Policies](#course-policies)
- [Course Schedule](#course-schedule)

------
Logistics
------

__Instructor:__ Dr. Brian Spiering brian.spiering@galvanize.com
__Office Hours:__ Wednesday 11a-12n & By Appointment  

__Assistant Faculty:__ Edward Banner edward.banner@galvanize.com  
__Office Hours:__ By Appointment  

__Class Location:__ 44 Tehama St, ~~309~~ 311 classroom, San Francisco, CA   
__Lecture Times/Days:__ 11a-1p & 3-5p, Monday & Tuesday  
__Lab Times/Days:__ 1p-2p & 5-6p, Monday & Tuesday  

__Communication:__ [`#gu4_sf_dl`](https://gstudent.slack.com/archives/gu4_sf_dl)

----
Course Description
----

This course provides a broad overview of Deep Learning, aka artificial neural networks. We will cover the mathematics and programming required to understand the fundamentals of Deep Learning and design contemporary architectures. Students will apply these techniques to real-world problems, for example image classification.  

### By the end of this course, you should be able to:

- Apply Deep Learning to solve real world problems
- Build a 3-layer artificial neural network from scratch
- Explain and implement backpropagation algorithm
- Build the following architectures:
    - Convolutional Neural Networks (CNN)
    - Recurrent Neural Network (RNN) and Long Short Term Memory (LSTM)
    - Generative Adversarial Nets (GANs)
    - Reinforcement Learning (RL)

### Out of Scope

- All other kinds of machine learning (We are only covering Deep Learning)
- All other Deep Learning frameworks (We are only covering Keras and TensorFlow)
   - Theano, Caffe, CNTK, DSSTNE, PaddlePaddle, …
   - OpenAI Gym/Universe & DeepMind Lab
   - High Performance Computing (HPC)
   - Distributed systems
- ALL other hardware implementations (We are only covering CPU and GPUs)
    - ASIC
    - Mobile
- Deep Learning research (We are only covering applied Deep Learning)
    - Memory Networks
    - Neural Turing Machines
    - Energy–Based Models

### Prerequisites

Successful completion of:  

- DSCI-6001: Mathematics for Data Scientists   
- DSCI-6002: Data Exploration, Feature Engineering, and Statistics for Data Scientists  
- DSCI-6003: Machine Learning

### Required Resources 

#### Books
- _Fundamentals of Deep Learning_
- [Deep Learning](http://www.deeplearningbook.org/)

#### MOOCs
- [CS231n: Convolutional Neural Networks for Visual Recognition](http://cs231n.stanford.edu/)
- [fast.ai](http://course.fast.ai/)
- [Udacity's Deep Learning](https://www.udacity.com/course/deep-learning--ud730)

### Optional Resources
- [Awesome Deep Learning](https://github.com/ChristosChristofidis/awesome-deep-learning)

----
Class Structure
----

This course is an "active" learning environment. You'll learn through doing. The focus will be on explaining concepts in your words and applying concepts through programming.

Before class you will complete preparation materials (e.g., watch videos and read book chapters / blogs). All preparation materials should be covered __prior__ to the start of each class session. They are __always required__ unless explicitly labeled as optional. These materials will be the source of factual knowledge. You are expected to be familiar with the basic concepts and technical jargon before the start of class.

In-class time is precious - We'll reserve it for discussion, presenting complex material, answering questions, and working on exercises.  

Typical class structure:

1. On Your Own (OYO) activity
1. RAT (Readiness Assessment Test)
1. Lecture
1. Lab

### Complete On Your Own (OYO) activity

OYO activity is a creative activity to help you to integrate and apply the the preparation materials.

### RATs

The Readiness Assessment Tests (RATs) are intended to test your understanding of the materials presented thus far in the course. This includes material from previous classes. There are 3 parts: individual, small-group, and class.

1. Each student will answer all the questions on the RAT individually.
2. Then the class will split into teams of 3-4. Each team will answer the same questions again, the goal is to reach consensus. This is an opportunity for peer-to-peer instruction which is often more effective than lectures!
3. Finally, the answers to the questions will be gone over by the class, hopefully resolving any misunderstandings before proceeding.

### Labs

The RATs are meant to assess the first three levels of [Bloom's Taxonomy](http://en.wikipedia.org/wiki/Bloom's_taxonomy#Cognitive): knowledge, comprehension, and analysis. The lab work is meant to develop the latter three levels: analysis, synthesis, and evaluation. Students will separate into two (or threes) for "pair programming". These exercises may involve a series of short questions, single day projects, or multi-day projects.

----
Grades
----

| Item | Weight  |  
|:-------:|:------:|
| Mastery Tracker | 10% |  
| Participation | 20% | 
| Lab | 30% |
| Final Project | 40% |

The expected grade is B+. Getting an A- or above requires completion of the Mastery Tracker, high level participation, and a stellar final project.

### Mastery Tracking

Mastery Tracking is a tool to provide feedback student learning. Standards are the core-competencies of MSDS graduates - the knowledge, skills, and habits every student should possess by time they graduate. Standards are measurable, student-focused outcomes that state what students are expected to be able to do by the end of the course. Students who are below ‘mastery’ on a standard are expected to continue practicing said standard (with the instructor's guidance) until they reach mastery. What matters is that students eventually learn the material, not how many attempts it takes to get there. The Instructor and Data Scientist in Residence are available to offer feedback and help guide everyone on their mastery journey.

Mastery Tracking uses a 4-point scale. Every student is expected to achieve 3 or above (Mastery) across all Standards by the end of the course. 1s and 2s indicate areas where students need further practice and/or interventions to reach mastery.

4 pt Scale:

0 = Has not been covered  
1 = Falling far below mastery - Meeting none of the success criteria or has egregious errors  
2 = Approaching mastery - Meeting some of the success criteria  
3 = Mastery - Meeting all of the success criteria  
4 = Exceeding mastery - Truly exceeding expectations and demonstrating proficiency at a higher level of rigor  

We will be using Galvanize's Learning Management System (LMS) which can be found at [learn.galvanize.com](https://learn.galvanize.com).

### Participation

You must also show up prepared. Each person is important to the dynamic of the class, and therefore students are required to participate in class activities. Expect to be "cold called". I call on students at random, not to put you on the spot but, to keep you engaged in the material at all times.

Attendance is __mandatory__. It is the responsibility of each student to attend all classes. If you have to miss class, due to any circumstances, please notify Brian by Slack ASAP. Supporting documents (e.g., doctor’s notes) should accompany absences due to sickness. Each excused absences beyond 2 or _each_ unexcused absences will result in lowering your __overall course grade by ⅓ of a letter grade__ (A->A-, A->B+, …). It is at the instructor’s discretion to deny any absences or to allow students to make-up course work resulting from any absences.

### Final Project

Details will be covered in a future class (mostly likely tomorrow).

----
Course Schedule
-----

1. Neural Network Fundamentals
    1. Welcome 
    2. Fundamentals
    3. Backpropagation I
    4. Backpropagation II 
2. Neural Network Training 
    1. Keras
    2. Training Neural Networks I
    3. Images and Convolution
    4. Convolutional Neural Networks (CNNs)  
3. Image Classification
    1. Image Classification I
    2. Optimization I 
    3. Image Classification II
    4. Review / Project Check-in
4. Sequence Learning (aka, Natural Language Processing)
    1. Recurrent Neural Networks (RNNs) 
    2. Long Short Term Memory (LSTM) Networks 
    3. Sequence-to-Sequence Learning
    4. Natural Language Processing (NLP)  
5. Reinforcement Learning (RL) 
    1. TensorFlow I 
    2. Reinforcement Learning (RL) I
    3. Reinforcement Learning (RL) II 
    4. Training Neural Networks II
6. Generative Adversarial Nets (GANs)
    1. Optimization II
    2. Generative Adversarial Nets (GANs) I 
    3. Generative Adversarial Nets (GANs) II
    4. Review / Project Check-in
7. Unsupervised learning
    1. TensorFlow II
    2. Unsupervised Learning I
    3. Attention-Based Models
    4. Unsupervised Learning II
8. Final Project
    1. Review
    2. Final Project Worksession
    3. Presentations
    4. Presentations
