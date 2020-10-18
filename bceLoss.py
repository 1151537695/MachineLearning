import torch
import torch.nn as nn
import math

m = nn.Sigmoid()

# loss = nn.BCELoss(size_average=False, reduce=False)
loss = nn.BCELoss()
input = torch.randn(3, requires_grad=True)
target = torch.empty(3).random_(2)
lossinput = m(input)
output = loss(lossinput, target)

print("输入值:")
print(lossinput)
print("输出的目标值:")
print(target)
print("计算loss的结果:")
print(output)
print("计算loss的结果:")
print(output.data.item())
output.backward()
print("计算loss的结果:")
print(output)
print("计算loss的结果:")
print(output.data.item())
#print(output.data.item())
print("自己计算的第一个loss：")
print(-(target[0]*math.log(lossinput[0])+(1-target[0])*math.log(1-lossinput[0])))



# loss_fn = torch.nn.L1Loss(reduce=False, size_average=False)
# input = torch.autograd.Variable(torch.randn(3,4))
# target = torch.autograd.Variable(torch.randn(3,4))
# loss = loss_fn(input, target)
# print(input); print(target); print(loss)