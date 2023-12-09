# gen-ai-adventure
# 1. Introduction to Generative AI
## 1.1. What generative  AI is?
In general, AI is a discipline of creating of intelligent machines that can perform tasks that require human intelligent.
As a discipline, it is has some subfields:
- Machine Learning (ML)
- Deep Learning (DL)
    - Generative AI

Deep Learning model types:
- Discriminative Models

Typically trained on a dataset of labeled data.
It learns the relationship between the features of the data points and the labels to classify or predict the results.

Example: We have a cat image as an input. The Model is able to classify the image as a cat image.

- Generative Models

It generates new data that is similar to data it was trained on. It used to predict the next word in a sequence.

Example: We have a cat image as an input. The Model is able to generate new cat image that resemblance with the input image.


Generative AI is the sub-field of Deep Learning.
The foundation model of Generative AI is a large AI model pretrained on a vast quantity of data that was "designed to be adapted” (or fine-tuned) to a wide range of downstream tasks, such as sentiment analysis, image captioning, and object recognition.

### 1.1.1. Hallucination
Hallucination is non-sensical or grammatically incorrect response from generative AI.

Some of the causes:
1. The model is not trained on enough data
2. The model is trained on noisy data
3. The model is not given enough context.
4. The model is not given enough constraint. 

### 1.1.2. Prompt Design
Prompt Design is instructions that used as a guidance for generative model in producing the desired responses.

Prompt Engineering = practice of developing and optimizing prompts to efficiently use language models for a variety of applications.

### 1.1.3. Model Types Based on the Task 
- Text to text
    
    The models are trained on a large set of text datasets.
    - text generation
    - text classification
    - text summarization
    - text translation
    - text extraction
    - text clustering

- Text to image
    
    The models are trained on a large set of images captioned with a short text description.
    - image generation
    - image editing

- Text to video or 3D object
    
    The models aim to generate a video or 3D object representation from text input.
    - video generation
    - video editing
    - game assets

- Text to task
    
    The models are trained on specific task or action based on text input.
    - software agents
    - virtual assistants
    - automation

## 1.2. When to fine-tune the models?
Pre-trained generative models are already trained on a large dataset. But they still have tendency for hallucination. Therefore for specific context, better to fine-tune (post training) the models on specific context dataset for more accurate and intended response.

## 1.3. What differs it from traditional ML Development?
In terms of its model development.

| Gen AI (Pre-trained API) | Tradition ML|
|:-------- |:-------- |
|No ML Expertise needed | ML Expertise needed|
|No training examples | training examples needed |
|No need to train a model | need to train a model |
| Thinks about prompt design | compute time + hardware needed|
|  | Thinks about minimizing a loss function |

# 2. Introduction to Large Language Models (LLM)
## 2.1. What is LLM?
LLM is a subset of Deep Learning.

Type of AI model that produce new content, whether text, image, video, or synthetic data.

LLM is general-purpose language models that can be pre-trained and then fine-tuned (adapt) for specific purposes.

Some tasks that commonly solved using LLM:
- text classification
- question answering
- document summarization
- text generation

The pre-trained LLM can adapt to more specific task or context by fine-tuning process (post-training).


Types of LLM:
1. Generic (Raw) Language Model

Predict the next word based on the training data

2. Instruction Tuned

Predict a response to the instruction given in the input

3. Dialog Tuned

Predict the next response to the given dialog of user

### 2.1.1. LLM general characteristics
1. Large Size Dataset

It is trained on very vast size dataset (usually at least in petabyte scale)

2. Large number of parameters

Hyperparameter is parameter set during training process. Number of parameter reflects to the model size.

3. General Purpose

LLM is able to solve common problems.

4. Pre-trained and fine-tuned

LLM is pre-trained to solve general problems then fine-tuned to solve more specific problems.


### 2.1.2. Benefit using LLM
1. Single model LLM can be used for different tasks
2. Fine-tune process require minimal field data (usually decent enough  result on few-shot or even zero-shot training)
3. Performance is growing with more data and parameters

## 2.2. Prompt Tuning
Prompt Design is instructions that used as a guidance for generative model in producing the desired responses.

Prompt Engineering = practice of developing and optimizing prompts to efficiently use language models for a variety of applications.

Prompt design is a more general concepts while prompt engineering is  a more specialized concept.

## 2.3. LLMs examples
1. PaLM (Pathways Language Model)

In April 2022, Google released PaLM. It is a decoder-based transformers model and has 540B parameters.

While traditional language models process text sequentially, PaLM employs a multi-path approach thus able to comprehend text paralelly.
These paths can represent different linguistic features, syntactic structure, or semantic context.

Strengh:
- improved comprehension of context
- efficient parallelism
- enhanced performance-resource tradeoff
- scalability to larger models
- broader applicability

2. LaMDA (Language Model for Dialogue Applications)
LLM that designed for dialog purpose created by Google in May 2021. The model size from 2B to 137B parameters. It is initially trained to predict the next token in a text corpus. LaMDA models is able to performs in both classification and text generation tasks.

# 3. Introduction to Responsible AI
- The need for a responsible AI practice within an organization
- Organizations can design AI to fit their own business needs and values

Nowadays AI can see, understand, and interact with the world. The advancement happened in remarkable pace.

Developing responsible AI means we need to understand of the **possible issues**, **limitations**, and **unintended consequences**.

For now, there is no a universal definition of responsible AI. Instead, organizations are developing their own definitions that suitable for them.

But generally the principle of responsible AI consist of following:
- transparency
- fairness
- accountability
- privacy


# 4. Generative AI Fundamentals


# Reference
- [Introduction to Generative AI Learning Path by Google](https://www.cloudskillsboost.google/paths/118)
- [Introduction to Generative AI](https://www.cloudskillsboost.google/course_templates/536)
- [Introduction to LLM](https://www.cloudskillsboost.google/course_sessions/4021096/video/379143)
- [Introduction to Responsible AI](https://www.cloudskillsboost.google/paths/118/course_templates/554)
- [Generative AI Fundamentals](https://www.cloudskillsboost.google/paths/118/course_templates/556)
- PaLM: https://medium.com/mlearning-ai/googles-pathways-to-language-model-palm-scaling-to-new-heights-in-ai-understanding-c900b0e87c22
- LaMBDA: https://medium.com/aiguys/lamda-language-models-for-dialog-applications-b76d24eb1f15
