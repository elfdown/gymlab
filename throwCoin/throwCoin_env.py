import random
class throwCoin:

    observation = 0
    ph = 0.4

    def __init__(self):
        self.observation = random.randint(1,99)

    def reset(self):
        self.observation = random.randint(1,99)
        return self.observation
    
    def step(self,action):

        win = True
        done = False
        reward = 0

        pwin = random.random()
        if pwin < self.ph :
            win = True
        else :
            win = False

        if win:
            self.observation += action
            if self.observation == 100:
                done = True
                reward = 1
            return([self.observation,done,reward])
        else:
            self.observation -= action
            if self.observation == 0:
                done = True
                reward = 0
            return([self.observation,done,reward])

if __name__ == "__main__":
    env = throwCoin()
    for i in range (20):
        observation = env.reset()
        for j in range(10000):
            print(observation)
            money = random.randint(0,min(observation,100-observation))
            observation,done,reward = env.step(money)
            # observation,done,reward = env.step(1)
            if done:
                print(observation)
                print("after {} times it erns {}".format(j,reward))
                break

