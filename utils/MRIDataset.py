from monai.data import Dataset as monaiDataset, DataLoader as monaiDataLoader


class MRIDataset(monaiDataset):

    def __init__(self, image_files, labels, transforms):
        self.data = [{"image":image_files[i]} for i in range(len(image_files))]
        self.labels = labels
        self.transforms = transforms

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.transforms(self.data[index]), self.labels[index]