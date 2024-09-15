import torch
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader
import torch.nn as nn
import torch.optim as optim

# 1. 데이터 전처리 설정
data_transforms = {
    'train': transforms.Compose([
        transforms.Resize((224, 224)),  # 이미지 크기 조정
        transforms.RandomHorizontalFlip(),  # 데이터 증강
        transforms.ToTensor(),  # 텐서로 변환
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])  # 정규화
    ]),
    'val': transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
    'test': transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
}

# 2. 데이터 로드
data_dir = r'C:\Users\조갱\OneDrive\바탕 화면\사용할거'
image_datasets = {x: datasets.ImageFolder(root=f'{data_dir}/{x}', transform=data_transforms[x])
                  for x in ['train', 'val', 'test']}
dataloaders = {x: DataLoader(image_datasets[x], batch_size=32, shuffle=True, num_workers=4)
               for x in ['train', 'val', 'test']}

# 3. 모델 정의 (ResNet18 사용)
model = models.resnet18(pretrained=True)
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 10)  # 10개의 클래스로 분류

# 4. 손실 함수와 옵티마이저 설정
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

# 5. 학습 루프
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = model.to(device)

for epoch in range(10):  # 에포크 수
    print(f'Epoch {epoch+1}/10')

    for phase in ['train', 'val']:
        if phase == 'train':
            model.train()  # 학습 모드
        else:
            model.eval()   # 평가 모드

        running_loss = 0.0
        running_corrects = 0

        # 데이터 반복
        for inputs, labels in dataloaders[phase]:
            inputs, labels = inputs.to(device), labels.to(device)

            optimizer.zero_grad()

            with torch.set_grad_enabled(phase == 'train'):
                outputs = model(inputs)
                loss = criterion(outputs, labels)
                _, preds = torch.max(outputs, 1)

                if phase == 'train':
                    loss.backward()
                    optimizer.step()

            running_loss += loss.item() * inputs.size(0)
            running_corrects += torch.sum(preds == labels.data)

        epoch_loss = running_loss / len(image_datasets[phase])
        epoch_acc = running_corrects.double() / len(image_datasets[phase])

        print(f'{phase} Loss: {epoch_loss:.4f} Acc: {epoch_acc:.4f}')

# 6. 테스트 데이터로 평가
model.eval()
test_acc = 0.0
for inputs, labels in dataloaders['test']:
    inputs, labels = inputs.to(device), labels.to(device)
    outputs = model(inputs)
    _, preds = torch.max(outputs, 1)
    test_acc += torch.sum(preds == labels.data)

test_acc = test_acc.double() / len(image_datasets['test'])
print(f'Test Acc: {test_acc:.4f}')


torch.save(model, "./Models/Base_model.pth")