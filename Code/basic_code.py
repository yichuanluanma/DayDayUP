import numpy as np
#生成坐标矩阵，w0，表示生成的第0维的结果，w1是第一维的结果,输出的维度是N * M
w0,w1=np.meshgrid(np.linspace(-1,1,3),np.linspace(-1,1,2))
#print(w0)
'''
[[-1.  0.  1.]
 [-1.  0.  1.]]
'''
#print(w1)
'''
[[-1. -1. -1.]
 [ 1.  1.  1.]]
'''

s0,s1,s2=np.meshgrid(np.linspace(-1,1,2),np.linspace(-1,1,3),np.linspace(-1,1,4))
#输入为 M， N，P==》输出为 N*M*P ,输出的维度只跟输入的维度有关。
#print(s0.shape)
'''
[[[-1. -1. -1. -1.]
  [ 1.  1.  1.  1.]]

 [[-1. -1. -1. -1.]
  [ 1.  1.  1.  1.]]

 [[-1. -1. -1. -1.]
  [ 1.  1.  1.  1.]]]
'''
#print(help(np.meshgrid))
'''
'''

#w0,w1 ==>2*3,列表连接，转换成ndarray  、、 内存存储的方式，按行，或者按列？
w=np.array([w0,w1])
print(w.shape) # 2*2*3

#转换成 2*3*2,,即将最外层的结果转换到最内层。 ，如果设置转换的参数u？
w=w.transpose(1,2,0)
print(w.shape)
print(help(np.ndarray.transpose))
t=np.array([[1,2,3],[4,5,6]])
print(t)
print(t.transpose(1,0))
#transpose 按顺序排列维度，，其中（0,1,2）表示转换之前的维度，（0,1,2）排列的顺序如（1,2,0）表示之前的第1维在最先，
#第2维在第二，第0维在最后。只是重新排列维度，，坐标轴的重新排列。
