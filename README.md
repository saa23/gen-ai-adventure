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
Prompt Design is design/ construction of prompting that used as contraint for generative model. It guides the model in producing the intended responses.

The quality of the input determines the quality of the output.

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


# 2. Introduction to Large Language Models



# 3. Introduction to Responsible AI


# 4. Generative AI Fundamentals


# Reference
[Introduction to Generative AI Learning Path by Google](https://www.cloudskillsboost.google/paths/118)
