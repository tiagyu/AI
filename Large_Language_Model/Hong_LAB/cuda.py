import torch


if torch.cuda.is_available():
    device = torch.device('cuda')
    print('cuda')
else:
    device = torch.device('cpu')
    print('cpu')

# print(torch.cuda.get_device_name(0))

print(torch.__version__)
