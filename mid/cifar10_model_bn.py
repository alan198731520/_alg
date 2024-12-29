from torch import nn
import torch.nn.functional as F

class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        # 卷積層
        self.conv1 = nn.Conv2d(3, 10, 3, 1, 1)  # 第一層卷積
        self.bn1 = nn.BatchNorm2d(10)          # 第一層 Batch Normalization
        self.conv2 = nn.Conv2d(10, 20, 3, 1, 1) # 第二層卷積
        self.bn2 = nn.BatchNorm2d(20)          # 第二層 Batch Normalization
        self.conv3 = nn.Conv2d(20, 40, 3, 1, 1) # 第三層卷積
        self.bn3 = nn.BatchNorm2d(40)          # 第三層 Batch Normalization
        
        # 最大池化層
        self.pool = nn.MaxPool2d(2, 2)         # 池化層
        
        # 全連接層
        self.linear1 = nn.Linear(40 * 4 * 4, 100) # 第一個全連接層
        self.linear2 = nn.Linear(100, 10)        # 第二個全連接層
        
        # Dropout層
        self.dropout = nn.Dropout(0.2)          # Dropout層，防止過擬合

    def forward(self, x):
        # 卷積層 + Batch Normalization + 激活函數 + 池化層
        x = self.pool(F.relu(self.bn1(self.conv1(x))))  # 第一層
        x = self.pool(F.relu(self.bn2(self.conv2(x))))  # 第二層
        x = self.pool(F.relu(self.bn3(self.conv3(x))))  # 第三層
        
        # 展平特徵圖
        x = x.view(-1, 40 * 4 * 4)  # 展平特徵
        
        # 全連接層 + Dropout
        x = self.dropout(F.relu(self.linear1(x)))  # 第一個全連接層
        x = F.log_softmax(self.linear2(x), dim=1)  # 第二個全連接層（輸出層）
        return x