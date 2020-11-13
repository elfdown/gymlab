import throwCoin_env
import numpy as np
import random

#初始化
value = np.zeros([101])
decision = np.zeros([101],dtype = int)
value[100]  =  1
standard = 0.0001
ph = 0.4
scale = 1

#策略评估
for i in range(1000):
        max_var = 0
        old_value = value.copy()
        for situation in range(1,100):
                most_value = 0
                for action in range(min(situation,100-situation)+1):
                        one_value = (1-ph)*scale*value[situation-action]\
                                +ph*scale*value[situation+action]
                        most_value = max(one_value,most_value)
                value[situation] = most_value
        for situation in range(1,100):
                var = abs(old_value[situation]-value[situation])
                max_var = max(max_var,var)
        if max_var < standard:
                break
#策略改进
for situation in range(101):
        most_value = 0
        for action in range(min(situation,100-situation)+1):
                one_value = (1-ph)*scale*value[situation-action]\
                                +ph*scale*value[situation+action]
                if one_value > most_value:
                        decision[situation] = action
print(decision)
#测试策略
env = throwCoin_env.throwCoin()
win_time = 0
total_time = 10000
for i in range (total_time):
        observation = env.reset()
        for j in range(10000):
                observation,done,reward = env.step(random.randint(0,min(observation,100-observation)))
                observation,done,reward = env.step(decision[observation])
                if done:
                        if reward == 1:
                                win_time += 1
                        break
print(win_time/total_time)