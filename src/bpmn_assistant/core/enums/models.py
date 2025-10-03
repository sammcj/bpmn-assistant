from enum import Enum


class OpenAIModels(Enum):
    GPT_5 = "gpt-5"
    GPT_5_MINI = "gpt-5-mini"
    GPT_4_1 = "gpt-4.1"

class AnthropicModels(Enum):
    SONNET_4_5 = "claude-sonnet-4-5-20250929"
    OPUS_4_1 = "claude-opus-4-1-20250805"


class GoogleModels(Enum):
    GEMINI_2_5_FLASH = "gemini/gemini-2.5-flash"
    GEMINI_2_5_PRO = "gemini/gemini-2.5-pro"


class FireworksAIModels(Enum):
    LLAMA_4_MAVERICK = (
        "fireworks_ai/accounts/fireworks/models/llama4-maverick-instruct-basic"
    )
    QWEN_3_235B = "fireworks_ai/accounts/fireworks/models/qwen3-235b-a22b"
    DEEPSEEK_V3_1 = "fireworks_ai/accounts/fireworks/models/deepseek-v3p1-terminus"
    DEEPSEEK_R1 = "fireworks_ai/accounts/fireworks/models/deepseek-r1"
