import numpy as np
from projectile import Projectile
class Dog:

    def __init__(self,p,e,r,r_hat):
        self.p = p
        self.e = e
        self.r = r
        self.r_hat = r_hat

    def get_p_hat_y(self,t):
        return self.p.get_y(t-self.r)+self.r_hat*((self.p.get_y(t-self.r)-self.p.get_y(t-self.r*2)))/self.r

    def get_p_hat_x(self,t):
        return self.p.get_x(t-self.r)+self.r_hat*((self.p.get_x(t-self.r)-self.p.get_x(t-self.r*2)))/self.r

    def get_positions(self,N,T):
        x = []
        y = []

        for t in np.linspace(0,T,N):
            x.append(self.get_p_hat_x(t))
            y.append(self.get_p_hat_y(t))

        return (x,y)

    def get_angles(self,N,T):
        thetas = []

        for t in np.linspace(0,T,N):
            # In degrees
            thetas.append(np.arctan(self.get_p_hat_y(t)/self.get_p_hat_x(t))*180/np.pi+self.e*t)

        return thetas
