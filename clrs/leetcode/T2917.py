import math
from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(31):
            cnt = sum(1 for num in nums if ((num >> i) & 1) > 0)
            if cnt >= k:
                ans |= 1 << i
        return ans


import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms


# 定义模型结构
class SimpleDalle(nn.Module):
    def __init__(self, vocab_size, image_size):
        super(SimpleDalle, self).__init__()
        self.embedding = nn.Embedding(vocab_size, 32)
        self.transformer = nn.Transformer(
            d_model=32, nhead=4, num_encoder_layers=6, num_decoder_layers=6
        )
        self.decoder = nn.Linear(32, image_size * image_size)
        self.image_size = image_size

    def forward(self, text, image):
        text_emb = self.embedding(text)  # [batch_size, seq_len, 32]
        image_emb = self.embedding(image)  # [batch_size, seq_len, 32]
        text_encoded = self.transformer(text_emb)  # [batch_size, seq_len, 32]
        image_encoded = self.transformer(image_emb)  # [batch_size, seq_len, 32]
        prediction = self.decoder(text_encoded)  # [batch_size, image_size * image_size]
        return prediction.view(
            prediction.size(0), self.image_size, self.image_size
        )  # [batch_size, image_size, image_size]
