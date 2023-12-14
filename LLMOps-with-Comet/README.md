# 1. LLMOps vs MLOps



# 2. LLMOps Lifecycle



# 3. Prompt Engineering
Some best practices in prompt engineering:
- be specific and clear
- add delimiter to help structure instructions
- specify output format to explicitly stated the desired results
- think step by step to allows the model provide the detail reasoning before goes to the final answer
- role playing to mimic the behavior you want to expect from the model 

Prompt techniques:
| Prompting Technique | When to use? |
|:-------- |:-------- |
| Zero-shot prompting | Effective on basic tasks but not effective for advanced tasks |
| Few-shot in-context learning | Add high-quality demonstrations for more improved response |
| Chain of thought (CoT) | Applies chain of thoughts so that models use reasoning steps before responding |
| ReAct | enable models to leverage external tools and knowledge to improve performance and reduce  hallucination |
| Prompt Chaining | Chains several prompts to achieve complex tasks that involve different subtasks |
| Tree of Thoughts | Encourage exploration over thoughts that serve as intermediate steps for general problem solving with language models |
| Retrieval Augmented Generation (RAG) | Helps to leverage external knowledge to optimize prompt context and improve output quality and reliability |


# Reference
- [LLMOps course from Comet](https://apps.courses.comet.com/learning/course/course-v1:Comet+101+1/home)