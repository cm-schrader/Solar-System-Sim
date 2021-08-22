import numpy as np
from numpy import longdouble as ld
from enum import Enum
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from collections import defaultdict

G = ld(6.67408e-11) # Gravitational Coefficient in Nm^2/kg^2

class BodyType(Enum):
    Star = 0
    Planet = 1
    DwarfPlanet = 2
    Moon = 3
    Asteroid = 4

"""
Simulates a single astronomical body.
"""
class Body:
    """
    Initializes a body object using the following parameters.
    m       Mass in kg
    a       Semi Major Axis in m
    i       self.ilination in deg
    e       Ecentricity
    theta   True anomaly in deg
    raan    Righ ascension of the ascending node in deg
    w       Argument of perigee in deg
    """
    def __init__(self, name, parent, body_type, radius,  m, a, i, e, theta, raan, w, color) -> None:
        self.name = name
        self.parent = parent
        self.body_type = body_type
        self.radius = radius
        self.m = m
        self.a = a
        self.i = np.radians(i)
        self.e = e
        self.initialTrueAnomaly = np.radians(theta)
        self.raan = np.radians(raan)
        self.w = np.radians(w)
        self.color = color
        self.children = []
        self._orbit = None
        self._orbitRes = None
        if parent is not None:
            parent.children.append(self)

    # Gravitattional Constant
    @property
    def mu(self):
        if self.parent is None:
            parent_mass = ld(0)
        else:
            parent_mass = self.parent.m
        return G * parent_mass

    # Specific Angular Momentum
    @property
    def h(self):
         return np.sqrt(self.mu * self.a * (ld(1) - np.power(self.e, ld(2))))
     
    # Orbital Period
    @property
    def T(self):
        return ld(2) * np.pi * np.sqrt(np.power(self.a, ld(3)) / self.mu)

    # Sphere of Influence
    @property
    def SOI(self):
        if self.parent is not None:
            rsoi = self.a * np.power(self.m / self.parent.m, ld(2) / ld(5))
        else:
            rsoi = ld(9e+29)
        return rsoi

    """
    Computes the rotation matrix from the perifocal to the geocentric reference frame
    Returns a 3 x 3 rotation matrix.
    """
    def QxX(self):
        return np.array([
            [-np.sin(self.raan)*np.cos(self.i)*np.sin(self.w)+np.cos(self.raan)*np.cos(self.w), -np.sin(self.raan)*np.cos(self.i)*np.cos(self.w)-np.cos(self.raan)*np.sin(self.w), np.sin(self.raan)*np.sin(self.i)],
            [np.cos(self.raan)*np.cos(self.i)*np.sin(self.w)+np.sin(self.raan)*np.cos(self.w), np.cos(self.raan)*np.cos(self.i)*np.cos(self.w)-np.sin(self.raan)*np.sin(self.w), -np.cos(self.raan)*np.sin(self.i)],
            [np.sin(self.i)*np.sin(self.w), np.sin(self.i)*np.cos(self.w), np.cos(self.i)]
        ])

    """
    Recursivley finds the offset of the orbit based off of the parent's offset.
    This ensures that orbit's can be displayed as centered around the correct parent.
    """
    def getOffset(self, resolution):
        if self.parent is not None:
            parentOffset = np.squeeze(np.transpose(np.array([self.parent.generateOrbit(resolution)[:,0],]*resolution)))
            parentOffset = parentOffset + self.parent.getOffset(resolution)
        else:
            parentOffset = np.zeros([3, resolution])
        return parentOffset

    """
    Computes the time since perigee based off of initial orbit parameters.
    """
    def timeAtStart(self):
        eccAnom = ld(2) * np.arctan(np.sqrt(ld(1) - self.e)/np.sqrt(ld(1) + self.e) * ( np.tan(self.initialTrueAnomaly/ld(2))))
        meanAnom = eccAnom - self.e * np.sin(eccAnom)
        startTime = self.T / (ld(2) * np.pi) * meanAnom 
        if startTime < 0:
            startTime += self.T
        return startTime

    """
    Propagates the entire orbit.
    """
    def generateOrbit(self, resolution):
        # If the orbit was already propagated, don't do it again
        if self._orbit is not None and self._orbitRes == resolution:
            return self._orbit
        # If this is the central body of the system, don't calculate and orbit.
        if self.parent is None:
            return np.zeros([3, 1])
            
        timeSincePeriapsis = self.timeAtStart()

        # Generate time spaced true anomaly
        time = np.linspace(timeSincePeriapsis, self.T + timeSincePeriapsis, resolution)
        if self.e == ld(0):
            tanom = np.pi * ld(2) / self.T * time
        else:
            meanAnom = time * ld(2) * np.pi / self.T
            eccAnomEqn = lambda eccAnom: eccAnom - (eccAnom - self.e * np.sin(eccAnom) - meanAnom) / (ld(1) - self.e * np.cos(eccAnom))
            eccAnom = fsolve(eccAnomEqn, meanAnom)
            tanom = ld(2) * np.arctan(np.sqrt(ld(1) + self.e) / np.sqrt(ld(1) - self.e) * np.tan(eccAnom/ld(2)))

        # Compute radius at each time
        rxcoef = np.power(self.h, ld(2)) / self.mu / (ld(1) + self.e * np.cos(tanom))
        rx = rxcoef * np.array([[np.cos(tanom)], [np.sin(tanom)], [np.transpose(np.zeros(resolution))]])
        rx = np.squeeze(rx)

        # Convert from perifocal to geocentric frame.
        r = rx
        for i in range(resolution):
            r[:,i] = self.QxX().dot(rx[:,i])
        self._orbit = r
        self._orbitRes = resolution
        return r
            
"""
Plots an orbit for a body using MATPLOTLIB
"""
def plotOrbit(ax, body, resolution=300):
    if body.body_type == BodyType.Planet:
        marker = "o"
        size = 10
    elif body.body_type == BodyType.Moon:
        marker = "o"
        size = 3
    elif body.body_type == BodyType.Star:
        marker = "o"
        size = 20
    elif body.body_type == BodyType.Asteroid:
        marker = "D"
        size = 3
    elif body.body_type == BodyType.DwarfPlanet:
        marker = "o"
        size = 8
    else:
        raise
    orbit = body.getOffset(resolution) + body.generateOrbit(resolution)
    ax.plot(orbit[0,0], orbit[1,0], orbit[2,0], c=body.color, marker=marker, markersize=size)
    ax.plot(np.ndarray.flatten(orbit[0,:]), np.ndarray.flatten(orbit[1,:]), np.ndarray.flatten(orbit[2,:]), body.color)
    return np.squeeze(np.amax(np.abs(orbit), 1))

"""
Recursivley plots an entire system given the central body.
"""
def plotSystem(body, resolution=300, ax=None):
    if ax is None:
        ax = plt.axes(projection='3d')
        body.parent = None
    orbitmax = plotOrbit(ax, body, resolution=resolution)
    bounds = np.zeros(3)
    for child in body.children:
        bounds = plotSystem(child, resolution=resolution, ax=ax)
    if ax is not None:
        orbitmax = np.squeeze(np.amax(np.abs(body.getOffset(resolution)), 1))
    bounds = np.amax(np.stack([orbitmax, bounds], 1),1)

    if body.parent is None:
        X = np.array([-bounds[0], bounds[0]])
        Y = np.array([-bounds[1], bounds[1]])
        Z = np.array([-bounds[2], bounds[2]])

        max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max()
        Xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(X.max()+X.min())
        Yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(Y.max()+Y.min())
        Zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(Z.max()+Z.min())

        for xb, yb, zb in zip(Xb, Yb, Zb):
            ax.plot([xb], [yb], [zb], 'w')

        ax.set_title(f"{body.name} System")
        plt.show()
    return bounds

def countBodies(body, top=True):
    def mergeCount(dict1, dict2):
        dict3 = defaultdict(lambda: 0)
        keys = list(dict1.keys()) + list(dict2.keys())
        keys = list(set(keys))
        for key in keys:
            dict3[key] = dict1[key] + dict2[key]
        return dict3
    count = defaultdict(lambda: 0)
    count[body.body_type.name] += 1
    for child in body.children:
        count = mergeCount(count, countBodies(child, top=False))    
    if top:
        print(f"\n=== {body.name} System ===")
        sum = 0
        for key in count.keys():
            sum += count[key]
            print(f"{key}: {count[key]}")
        print(f"\nTotal Bodies: {sum}\n")
    return count

