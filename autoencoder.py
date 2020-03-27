import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import matplotlib.pyplot as plt
from torchvision import datasets, transforms

from wga_dataset import WGADataset

#taken from https://www.cs.toronto.edu/~lczhang/360/lec/w05/autoencoder.html
# class Autoencodeer & train function
class Autoencoder(nn.Module):
  def __init__(self):
    super(Autoencoder, self).__init__()
    self.encoder = nn.Sequential( # like the Composition layer you built
      nn.Conv2d(1, 16, 3, stride=2, padding=1),
      nn.ReLU(),
      nn.Conv2d(16, 32, 3, stride=2, padding=1),
      nn.ReLU(),
      nn.Conv2d(32, 64, 7)
    )
    self.decoder = nn.Sequential(
      nn.ConvTranspose2d(64, 32, 7),
      nn.ReLU(),
      nn.ConvTranspose2d(32, 16, 3, stride=2, padding=1, output_padding=1),
      nn.ReLU(),
      nn.ConvTranspose2d(16, 1, 3, stride=2, padding=1, output_padding=1),
      nn.Sigmoid()
    )
  def forward(self, x):
    x = self.encoder(x)
    x = self.decoder(x)
    return x

def train(model, training_data, num_epochs=5, batch_size=64, learning_rate=1e-3):
  print ('autoencoder')
  torch.manual_seed(42)
  criterion = nn.MSELoss() 
  optimizer = torch.optim.Adam(model.parameters(),
                               lr=learning_rate,
                               weight_decay=1e-5)
  train_loader = torch.utils.data.DataLoader(training_data,
                                             batch_size=batch_size,
                                             shuffle=True)
  outputs = []
  for epoch in range(num_epochs):
    for data in train_loader:
      img, _ = data #TODO check that this returns a good value
      recon = model(img)
      loss = criterion(recon, img)
      loss.backward()
      optimizer.step()
      optimizer.zero_grad()
    print('Epoch:{}, Loss:{:.4f}'.format(epoch+1, float(loss)))
        outputs.append((epoch, img, recon),)
  return outputs

def main():
  wga_dataset = WGADataset('./img_lib',transform=transforms.ToTensor())
  model = Autoencoder()
  outputs = train(model, wga_dataset)


if __name__ == "__main__":
  main()