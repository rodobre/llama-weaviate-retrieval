## What is this ?

A modified version of [llama-retrieval-plugin]([llama-retrieval-plugin](https://github.com/lastmile-ai/llama-retrieval-plugin/tree/main)) based on Facebook's LLaMA which uses Weaviate and [HuggingFace's Sentence Transformers](https://huggingface.co/sentence-transformers) to perform vectorized semantic search.

## Required environment variables

```
export BEARER_TOKEN=$(openssl rand -hex 32)
export WEAVIATE_HOST=http://127.0.0.1
export WEAVIATE_PORT=8080
export WEAVIATE_INDEX=CustomDocument
```

## Contributors & License

- [OpenAI](https://github.com/openai)
- [Weaviate](https://weaviate.io/developers/weaviate/client-libraries/python)
- Original contributors from [llama-retrieval-plugin](https://github.com/lastmile-ai/llama-retrieval-plugin) and [chatgpt-retrieval-plugin](https://github.com/openai/chatgpt-retrieval-plugin)