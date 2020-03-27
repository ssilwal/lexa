import torch
import os
import io

class WGADataset(torch.utils.data.Dataset):
  def __init__(self, dirname,transform=None):
    self.data_dir = dirname
    self.images = os.listdir(dirname)
    self.transform = transform

  def __getitem__(self, index):
  	if torch.is_tensor(index):
  		index = index.tolist()
  	img_file = os.path.join(self.data_dir, self.images[index])
  	image = io.imread(img_file)
  	if self.transform:
  		sample = self.transform({'image':self.images[index]})
    return sample

  def __len__():
    return len(self.images)

  def transform(self, sample):
  	return {'image':self.transform(sample['image'])}