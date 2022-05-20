# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Recurrent Neural Networks

## Materials We Provide

| Topic | Description | Link |
| --- | --- | --- |
| Intro to RNNs | Slide Deck | [Link](./rnn.pdf)
| Coding Example | RNN walkthrough | [Link](./starter-code.ipynb)|

## Learning Objectives

*After this lesson, students will be able to:*

1. Preprocess sequence data for RNN modeling
2. Design, train and evaluate an RNN model
3. Create a model that predicts the price of Apple's (AAPL) stock

## Lesson Outline

> **Total Time: 90 mins**

I. **Intro to RNNs** (30 minutes total)
- What types of datasets are ideal for RNN models
- How `TimeseriesGenerator` prepares your sequence data for modeling
- Overview of RNN architecture
- The shortcomings of early RNN models
- How LSTM/GRU networks solve the problem of vanishing gradients

II. **RNN walkthrough** (60 minutes total)
- Load in stock price data
- Train/test split for time series data
- Use `TimeseriesGenerator` to prep our data for modeling
- Design a basic RNN network using GRU layers

## OPTIONAL: Resources for Practice and Learning

*For supplemental reading material on this topic, check out the following resources:*
- Andrew Ng's Coursera course on [Sequence Models](https://www.coursera.org/learn/nlp-sequence-models)
- Ava Soleimany's [video on RNNs](https://www.youtube.com/watch?v=SEnXr6v2ifU)
- [*The Unreasonable Effectiveness of Recurrent Neural Networks*](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)
- A good [explanation of RNNs](https://explained.ai/rnn/index.html)
- Blog on the [Vanishing Gradient Problem](https://towardsdatascience.com/the-vanishing-gradient-problem-69bf08b15484)
- How LSTMs solve the [vanishing gradient problem](https://medium.com/datadriveninvestor/how-do-lstm-networks-solve-the-problem-of-vanishing-gradients-a6784971a577)
- A blog on the [basics of RNNs](https://medium.com/towards-artificial-intelligence/whirlwind-tour-of-rnns-a11effb7808f)
- [An Illustrated Guide to RNNs](https://towardsdatascience.com/illustrated-guide-to-recurrent-neural-networks-79e5eb8049c9) with some helpful graphics for gaining some intuition about how RNNs work.

#### **Additional Resources (on specific topics discussed in the lesson)**

- Some resources on the use of `TimeSeriesGenerator` to preprocess data for time series modeling:
    - https://medium.com/swlh/timeseriesgenerator-a-deep-down-with-example-in-python-dfe32dcb2a24
    - https://machinelearningmastery.com/how-to-use-the-timeseriesgenerator-for-time-series-forecasting-in-keras/
    - https://www.dlology.com/blog/how-to-use-keras-timeseriesgenerator-for-time-series-data/
    - [This one](https://stanford.edu/~shervine/blog/keras-how-to-generate-data-on-the-fly) is more generally on how to use DataGenerators in Keras

- A few links on the difference between `GRU` and `LSTM` layers:
    - https://medium.com/mindboard/lstm-vs-gru-experimental-comparison-955820c21e8b
    - https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21
    - https://www.pluralsight.com/guides/lstm-versus-gru-units-in-rnn
    - https://datascience.stackexchange.com/questions/14581/when-to-use-gru-over-lstm
    - [Here's another comparison](https://theaisummer.com/gru/) that uses another Python Deep Learning framework called `PyTorch`

- A few links on the use of different batch sizes when training and predicting with RNNs:
    - https://machinelearningmastery.com/difference-between-a-batch-and-an-epoch/
    - https://machinelearningmastery.com/use-different-batch-sizes-training-predicting-python-keras/
    - https://stackoverflow.com/a/61823888
    - More generally, batch_size is a hyperparameter of gradient descent that controls the number of training samples to work through before the model’s internal parameters (weights & biases) are updated. [(From this useful and relatively comprehensive resource)](https://python-data-science.readthedocs.io/en/latest/sl-deeplearning.html#gradient-descent)
