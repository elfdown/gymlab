import random
import math
import numpy as np

class jackPay:

    park1 = 0
    park2 = 0

    def __init__(self):
        self.park1 = random.randint(0,20)
        self.park2 = random.randint(0,20)

    def poisson(self,E):
        a = random.random()
        k = 0
        up = 1
        down = 1
        total = up/down*math.exp(-E)
        while(total < a):
            k += 1
            up *= E
            down *= k
            total += up/down*math.exp(-E)
        return(k)

    def reset(self):
        self.park1 = random.randint(0,20)
        self.park2 = random.randint(0,20)
        return([self.park1,self.park2])

    def step(self,action):
        #zero the reward
        reward = 0
        #it is time to lend the car
        lose_car = self.poisson(3)
        if lose_car < self.park1:
            reward += lose_car*10
            self.park1 -= lose_car
        else:
            reward += self.park1*10
            self.park1 = 0
        lose_car = self.poisson(4)
        if lose_car < self.park2:
            reward += lose_car*10
            self.park2 -= lose_car
        else:
            reward += self.park2*10
            self.park2 = 0
        # it is time to get the ca
        get_car = self.poisson(3)
        if get_car + self.park1 > 20:
            self.park1 = 20
        else:
            self.park1 += get_car
        get_car = self.poisson(2)
        if get_car + self.park2 > 20:
            self.park2 = 20
        else:
            self.park2 += get_car
        #it is time to move the car
        if action > 0:
            if self.park1 - action < 0:
                action = self.park1
            if self.park2 + action > 20:
                action = 20 - self.park2
            self.park1 -= action
            self.park2 += action
            reward -= action*2
        elif action < 0:
            if self.park2 + action < 0:
                action = -self.park2
            if self.park1 - action > 20:
                action = -(20-self.park1)
            self.park2 += action
            self.park1 -= action
        else:
            pass
        return([self.park1,self.park2],False,reward)

if __name__ == "__main__":
    #the decison space
    decision = np.zeros([21,21],dtype = int)
    #the value space
    value = np.zeros([21,21],dtype  = int)

    #make env
    env = jackPay()
    observation = env.reset()
    for i in range (20):
        sum_reward = 0
        env.reset()
        for j in range(10000):
            observation,done,reward = env.step(decision[observation[0],observation[1]])
            # observation,done,reward = env.step(1)
            sum_reward += reward
            if done:
                break
        print(sum_reward)


