
from torch import nn
import torch.nn.functional as F

class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        # 卷積層
        self.conv1 = nn.Conv2d(3, 10, 3, 1, 1)
        self.conv2 = nn.Conv2d(10, 20, 3, 1, 1)
        self.conv3 = nn.Conv2d(20, 40, 3, 1, 1)
        
        # 最大池化層
        self.pool = nn.MaxPool2d(2, 2)
        
        # 全連接層
        self.linear1 = nn.Linear(40 * 4 * 4, 100)
        self.linear2 = nn.Linear(100, 10)
        
        # Dropout層
        self.dropout1 = nn.Dropout(0.3)  # 在第一個全連接層前
        self.dropout2 = nn.Dropout(0.5)  # 在第二個全連接層前

    def forward(self, x):
        # 卷積 + 池化 + 激活
        x = self.pool(F.relu(self.conv1(x)))  # 10 * 16 * 16
        x = self.pool(F.relu(self.conv2(x)))  # 20 * 8 * 8
        x = self.pool(F.relu(self.conv3(x)))  # 40 * 4 * 4

        # 展平
        x = x.view(-1, 40 * 4 * 4)

        # 全連接層 + Dropout
        x = self.dropout1(F.relu(self.linear1(x)))  # 第一層加入 Dropout
        x = self.dropout2(x)  # 第二層加入 Dropout
        
        # 輸出層
        x = F.log_softmax(self.linear2(x), dim=1)
        return x
