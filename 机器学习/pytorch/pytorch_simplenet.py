import torch
import torch.nn.functional as F
from torchvision.datasets import mnist
from torch.utils.data import DataLoader
import torchvision.transforms as transforms
import torch.optim as optim
from torch import nn

# 定义一些超参数
train_batch_size = 64
test_batch_size = 128
learning_rate = 0.01
num_epoches = 20
# data preprocessing
transforms = transforms.Compose([transforms.ToTensor(),
                                 transforms.Normalize([0.5], [0.5])])
# define dataset
train_data = mnist.MNIST('./data', train=True, transform=transforms, download=True)
test_data = mnist.MNIST('./data', train=False, transform=transforms, download=True)
# transform to a data loader which is a generator basically
train_loader = DataLoader(dataset=train_data, batch_size=train_batch_size, shuffle=True,
                          num_workers=-1, drop_last=True)
test_loader = DataLoader(dataset=test_data, batch_size=test_batch_size,
                         num_workers=-1, shuffle=False)

examples = enumerate(test_loader)