import numpy as np

class Projectile:

    def __init__(self,x_0,y_0,b,m, v_y0,v_x0):
        self.x_0 = x_0
        self.y_0 = y_0
        self.b = b
        self.m = m
        self.v_y0 = -1*v_y0 # because velocity is not pointed downward lol
        self.v_x0 = v_x0
        self.G = 10
    
    def simulate_points(self, N, T):
        x = []
        y = []
        for t in np.linspace(0,T,N):
            x.append(self.x_0-((self.m/self.b)*self.v_x0*(1-np.e**(-self.b*t/self.m))))
            y.append(self.y_0-((self.m*self.G/self.b)*t+(self.m/self.b)*(self.v_y0-self.m*self.G/self.b)*(1-np.e**(-self.b*t/self.m))))
        
        return (x,y)