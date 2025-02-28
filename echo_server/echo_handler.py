from typing import Iterator, AsyncIterator
from litellm.types.utils import GenericStreamingChunk, ModelResponse  # type: ignore
from litellm import CustomLLM, completion, acompletion  # type: ignore


class EchoModel(CustomLLM):
    def completion(self, messages, *args, **kwargs) -> ModelResponse:
        # Extract the content from the last message
        content = messages[-1]["content"]

        return completion(
            model="echo-provider/model",
            mock_response=content,  # type: ignore
        )  # type: ignore

    async def acompletion(self, messages, *args, **kwargs) -> ModelResponse:
        # Extract the content from the last message
        content = messages[-1]["content"]

        return await acompletion(
            model="echo-provider/model",
            mock_response=content,
        )  # type: ignore

    def streaming(self, messages, *args, **kwargs) -> Iterator[GenericStreamingChunk]:
        # Extract the content from the last message
        content = messages[-1]["content"]

        generic_streaming_chunk: GenericStreamingChunk = {
            "finish_reason": "stop",
            "index": 0,
            "is_finished": True,
            "text": content,
            "tool_use": None,
            "usage": {"completion_tokens": 0, "prompt_tokens": 0, "total_tokens": 0},
        }
        yield generic_streaming_chunk  # type: ignore

    async def astreaming(
        self, messages, *args, **kwargs
    ) -> AsyncIterator[GenericStreamingChunk]:
        # Extract the content from the last message
        content = messages[-1]["content"]

        generic_streaming_chunk: GenericStreamingChunk = {
            "finish_reason": "stop",
            "index": 0,
            "is_finished": True,
            "text": content,
            "tool_use": None,
            "usage": {"completion_tokens": 0, "prompt_tokens": 0, "total_tokens": 0},
        }
        yield generic_streaming_chunk  # type: ignore


echo_model = EchoModel()
