import gym
import random

env = gym.make("CartPole-v0")
observation = env.reset()
print(env.observation_space.low)
print(env.observation_space.high)
for i in range(10):
    observation = env.reset()
    print("defualt:{}".format(observation))
    sum_reward = 0
    for j in range(1000):
        env.render()
        if observation[3]>0:
            observation,reward,done,info = env.step(1)
        else :
            observation,reward,done,info = env.step(0)
        sum_reward += reward
        if done:
            print("now:{}".format(observation))
            print(sum_reward)
            break
env.close()