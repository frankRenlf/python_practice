from typing import List
from collections import deque


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = nums[i] + max(dp[max(0, i - k) : i])
        return dp[n - 1]


class SolutionBest:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        queue = deque([0])
        for i in range(1, n):
            while queue and queue[0] < i - k:
                queue.popleft()
            dp[i] = dp[queue[0]] + nums[i]
            while queue and dp[queue[-1]] <= dp[i]:
                queue.pop()
            queue.append(i)
        return dp[n - 1]


arr = [1, 2, 3]
print(arr[1:2])


c = {
    "error": {
        "message": "The response was filtered due to the prompt triggering Azure OpenAI's content management policy. Please modify your prompt and retry. To learn more about our content filtering policies please read our documentation: https://go.microsoft.com/fwlink/?linkid=2198766",
        "type": None,
        "param": "prompt",
        "code": "content_filter",
        "status": 400,
        "innererror": {
            "code": "ResponsibleAIPolicyViolation",
            "content_filter_result": {
                "hate": {"filtered": False, "severity": "safe"},
                "self_harm": {"filtered": False, "severity": "safe"},
                "sexual": {"filtered": False, "severity": "safe"},
                "violence": {"filtered": True, "severity": "medium"},
            },
        },
    }
}
e = {
    "error": {
        "message": "The response was filtered due to the prompt triggering Azure OpenAI's content management policy. Please modify your prompt and retry. To learn more about our content filtering policies please read our documentation: https://go.microsoft.com/fwlink/?linkid=2198766",
        "type": None,
        "param": "prompt",
        "code": "content_filter",
        "status": 400,
        "innererror": {
            "code": "ResponsibleAIPolicyViolation",
            "content_filter_result": {
                "hate": {"filtered": False, "severity": "safe"},
                "self_harm": {"filtered": False, "severity": "safe"},
                "sexual": {"filtered": False, "severity": "safe"},
                "violence": {"filtered": True, "severity": "medium"},
            },
        },
    }
}
d = {
    "seed": 0,
    "messages": [
        {
            "role": "system",
            "content": "You are an expert in assisting human. Follows the user prompt in a completion mode. Generate precise and clear response. End your response with {END}.",
        },
        {
            "role": "user",
            "content": "Compare the ground truth and prediction from AI models, to give a correctness score for the prediction. <AND> in the ground truth means it is totally right only when all elements in the ground truth are present in the prediction, and <OR> means it is totally right when any one element in the ground truth is present in the prediction. The correctness score is 0.0 (totally wrong), 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, or 1.0 (totally right). Just complete the last space of the correctness score.\n\n            Question | Ground truth | Prediction | Correctness\n            --- | --- | --- | ---\n            What is x in the equation? | -1 <AND> -5 | x = 3 | 0.0\n            What is x in the equation? | -1 <AND> -5 | x = -1 | 0.5\n            What is x in the equation? | -1 <AND> -5 | x = -5 | 0.5\n            What is x in the equation? | -1 <AND> -5 | x = -5 or 5 | 0.5\n            What is x in the equation? | -1 <AND> -5 | x = -1 or x = -5 | 1.0\n            Can you explain this meme? | This meme is poking fun at the fact that the names of the countries Iceland and Greenland are misleading. Despite its name, Iceland is known for its beautiful green landscapes, while Greenland is mostly covered in ice and snow. The meme is saying that the person has trust issues because the names of these countries do not accurately represent their landscapes. | The meme talks about Iceland and Greenland. It's pointing out that despite their names, Iceland is not very icy and Greenland isn't very green. | 0.4\n            Can you explain this meme? | This meme is poking fun at the fact that the names of the countries Iceland and Greenland are misleading. Despite its name, Iceland is known for its beautiful green landscapes, while Greenland is mostly covered in ice and snow. The meme is saying that the person has trust issues because the names of these countries do not accurately represent their landscapes. | The meme is using humor to point out the misleading nature of Iceland's and Greenland's names. Iceland, despite its name, has lush green landscapes while Greenland is mostly covered in ice and snow. The text 'This is why I have trust issues' is a playful way to suggest that these contradictions can lead to distrust or confusion. The humor in this meme is derived from the unexpected contrast between the names of the countries and their actual physical characteristics. | 1.0\n            \nDescribe the image<IMAGE> | The image is a black and white X-ray of a human skull, viewed from the front. The top and bottom of the skull are visible. The teeth and jaw bones are clearly visible. The nasal cavity and eye sockets are also visible but not as clear. The image is labeled with an “L” on the bottom right corner, indicating that it is the left side of the skull. | The image features a close-up of a person's skull, focusing on the teeth and jaw. The skull is missing its lower jaw, revealing the teeth and bones of the upper jaw. The teeth are clearly visible, with some of them appearing to be missing. The skull is positioned in the center of the image, and the teeth are arranged in a row, creating a striking visual effect. | ",
        },
    ],
    "max_tokens": 1024,
    "stop": "{END}",
}

e = {
    "id": "chatcmpl-8olNBQHipZx4aXoPqc2d2tus6OIM9",
    "object": "chat.completion",
    "created": 1707109193,
    "model": "gpt-4",
    "prompt_filter_results": [
        {
            "prompt_index": 0,
            "content_filter_results": {
                "hate": {"filtered": False, "severity": "safe"},
                "self_harm": {"filtered": False, "severity": "safe"},
                "sexual": {"filtered": False, "severity": "safe"},
                "violence": {"filtered": False, "severity": "safe"},
            },
        }
    ],
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "I'm sorry, but I am unable to process image data or provide any analysis on images, as my current capabilities do not include the ability to view or interpret visual content. If you have text-based inquiries or need assistance with other types of information, please let me know, and I would be happy to help. ",
            },
            "content_filter_results": {
                "hate": {"filtered": False, "severity": "safe"},
                "self_harm": {"filtered": False, "severity": "safe"},
                "sexual": {"filtered": False, "severity": "safe"},
                "violence": {"filtered": False, "severity": "safe"},
            },
        }
    ],
    "usage": {"prompt_tokens": 1119, "completion_tokens": 64, "total_tokens": 1183},
    "system_fingerprint": "fp_68a7d165bf",
}
x = {
    "id": "chatcmpl-8olOP2IuQtZZlOjGMD1vm0niqxNA2",
    "object": "chat.completion",
    "created": 1707109269,
    "model": "gpt-4",
    "prompt_filter_results": [
        {
            "prompt_index": 0,
            "content_filter_results": {
                "hate": {"filtered": False, "severity": "safe"},
                "self_harm": {"filtered": False, "severity": "safe"},
                "sexual": {"filtered": False, "severity": "safe"},
                "violence": {"filtered": False, "severity": "safe"},
            },
        }
    ],
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "To address your request:\n\n1. As an AI text-based model, I cannot process images directly. If you provide the size of the image, I can include that in the response, but I cannot view or analyze actual image content.\n\n2. Similarly, I am unable to localize or provide bounding box coordinates without the ability to view the image.\n\n3. Recognition of individuals in images is also outside my capabilities as I cannot process visual data.\n\n4. Without visual data, generating detailed captions for bounding boxes is not possible.\n\nIf you have any text-based questions or need assistance with information that doesn't require image processing, please let me know, and I'll be glad to help! ",
            },
            "content_filter_results": {
                "hate": {"filtered": False, "severity": "safe"},
                "self_harm": {"filtered": False, "severity": "safe"},
                "sexual": {"filtered": False, "severity": "safe"},
                "violence": {"filtered": False, "severity": "safe"},
            },
        }
    ],
    "usage": {"prompt_tokens": 1119, "completion_tokens": 137, "total_tokens": 1256},
    "system_fingerprint": "fp_68a7d165bf",
}

x = {
    "id": "chatcmpl-8olObJLxpAACG4upTzNOrC5svbzLK",
    "object": "chat.completion",
    "created": 1707109281,
    "model": "gpt-4",
    "prompt_filter_results": [
        {
            "prompt_index": 0,
            "content_filter_results": {
                "hate": {"filtered": False, "severity": "safe"},
                "self_harm": {"filtered": False, "severity": "safe"},
                "sexual": {"filtered": False, "severity": "safe"},
                "violence": {"filtered": False, "severity": "safe"},
            },
        }
    ],
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "message": {"role": "assistant", "content": "0.0 "},
            "content_filter_results": {
                "hate": {"filtered": False, "severity": "safe"},
                "self_harm": {"filtered": False, "severity": "safe"},
                "sexual": {"filtered": False, "severity": "safe"},
                "violence": {"filtered": False, "severity": "safe"},
            },
        }
    ],
    "usage": {"prompt_tokens": 676, "completion_tokens": 4, "total_tokens": 680},
    "system_fingerprint": "fp_68a7d165bf",
}
