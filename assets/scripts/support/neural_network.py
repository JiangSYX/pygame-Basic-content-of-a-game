""" 包含丧尸移动目标寻找的3层神经网络, 用于寻找和跟踪目标(逻辑关系用于躲避子弹的避障) """
import numpy

from assets.scripts.support.settings import settings # 设置


# 神经网络
class NeuralNetwork:

    # 初始化神经网络
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # 初始化神经层
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        # 初始化权值
        try:
            self.wih = numpy.loadtxt(settings('weight_input_to_hidden'))
            self.who = numpy.loadtxt(settings('weight_hidden_to_output'))
        except OSError:
            self.wih = numpy.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
            self.who = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))

        # 初始化学习率
        self.lr = learningrate

        # 初始化S型激活函数
        self.activation_function = lambda x: 1 / (numpy.exp(-x) + 1)

        pass

    # 训练神经网络
    def train(self, inputs_list, targets_list):
        # 输入数据数组和目标数据数组
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        # 输入层到隐藏层的权值计算
        hidden_inputs = numpy.dot(self.wih, inputs)
        # 隐藏层激活函数激活
        hidden_outputs = self.activation_function(hidden_inputs)

        # 隐藏层到输出层的权值计算
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # 输出层激活函数激活
        final_outputs = self.activation_function(final_inputs)

        # 输出层误差
        output_errors = targets - final_outputs
        # 隐藏层误差
        hidden_errors = numpy.dot(self.who.T, output_errors)

        # 根据误差更新隐藏层到输出层的权值
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)),
                                        numpy.transpose(hidden_outputs))

        # 根据误差更新输出层到隐藏层的权值
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),
                                        numpy.transpose(inputs))

        # 实时保存权值
        with open(settings('weight_input_to_hidden'), 'w') as wih_object:
            numpy.savetxt(wih_object, self.wih)
             
        with open(settings('weight_hidden_to_output'), 'w') as who_object:
            numpy.savetxt(who_object, self.who)

        pass

    # 查询神经网络
    def query(self, inputs_list):
        # 输入数据数组
        inputs = numpy.array(inputs_list, ndmin=2).T

        # 输入层到隐藏层的权值计算
        hidden_inputs = numpy.dot(self.wih, inputs)
        # 隐藏层激活函数激活
        hidden_outputs = self.activation_function(hidden_inputs)

        # 隐藏层到输出层的权值计算
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # 输出层激活函数激活
        final_outputs = self.activation_function(final_inputs)

        return final_outputs