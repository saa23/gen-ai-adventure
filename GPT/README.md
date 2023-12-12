# OpenAI ChatCompletion API
Parameters in `chat.completions.create()`:
1. **`model`** (string)

The model to use.

Here is [available models reference](https://platform.openai.com/docs/models/model-endpoint-compatibility).

2. **`temperature`** (float)

Range from 0 - 2.

0 means focused/ deterministic response.

More than or equal to 1 means random response or we can say provide more creative response.

It is usually set the value between 0 to 1.

3. **`messages`** (array)

array that containing:
- content (required)
- role (required)
- name (optional)

4. **`max_tokens`** (int)

The maximum number of tokens to generate in the completion.

ChaGPT use a Byte Pair Encoding (BPE) tokenizer.

[Here is how tokenizer in openAI API (tiktoken) works](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken)

5. **`top_p`**

It is also called *Nucleus sampling* which controlling response quality.

The higher value means allow more tokens, leading to broader response possibilities.

The lower value means provide more focused and contrained response.

6. **`n`**

Generating multiple response

7. **`stop`**

To define stop condition. 

8. **`frequency_penalty`**

Number between -2 to 2.

It is controlling repetitive responses.

The higher value means encourage the model to explore more diverse and novel response.

The lower value means the model likely to repeat information.

9. **`presence_penalty`**

Number between -2 to 2.

It is controlling avoidance of certain topics mentioned in prompt.

The higher value means make the model to avoid mentioning topics.

The lower value means the model less concern about preventing mentioning topics.

## Reference
- Good explanation of OpenAI API: https://medium.com/nerd-for-tech/model-parameters-in-openai-api-161a5b1f8129
- chat.completions.create doc: https://platform.openai.com/docs/api-reference/chat/create
- simulation of tokenizer in openAI: https://platform.openai.com/tokenizer
- frequency and presence penalty: https://platform.openai.com/docs/guides/text-generation/parameter-details 
