from torch import nn
import torch.nn.functional as F

class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        # 卷積層
        self.conv1 = nn.Conv2d(3, 10, 3, 1, 1)
        self.bn1 = nn.BatchNorm2d(10)  # Batch Normalization for Conv1
        self.conv2 = nn.Conv2d(10, 20, 3, 1, 1)
        self.bn2 = nn.BatchNorm2d(20)  # Batch Normalization for Conv2
        self.conv3 = nn.Conv2d(20, 40, 3, 1, 1)
        self.bn3 = nn.BatchNorm2d(40)  # Batch Normalization for Conv3

        # 池化層
        self.pool = nn.MaxPool2d(2, 2)

        # 全連接層
        self.linear1 = nn.Linear(40 * 4 * 4, 100)
        self.linear2 = nn.Linear(100, 10)

        # Dropout層
        self.dropout1 = nn.Dropout(0.3)  # Dropout before Linear1
        self.dropout2 = nn.Dropout(0.5)  # Dropout before Linear2

    def forward(self, x):
        # 卷積層 + Batch Normalization + 激活函數 + 池化層
        x = self.pool(F.relu(self.bn1(self.conv1(x))))  # Conv1 + BN1 + Pool
        x = self.pool(F.relu(self.bn2(self.conv2(x))))  # Conv2 + BN2 + Pool
        x = self.pool(F.relu(self.bn3(self.conv3(x))))  # Conv3 + BN3 + Pool

        # 展平特徵圖
        x = x.view(-1, 40 * 4 * 4)  # Flatten feature maps

        # 全連接層 + Dropout
        x = self.dropout1(F.relu(self.linear1(x)))  # Linear1 + Dropout1
        x = self.dropout2(x)  # Dropout2 before output
        x = F.log_softmax(self.linear2(x), dim=1)  # Linear2 + LogSoftmax
        return x