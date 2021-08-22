from matplotlib import markers
import numpy as np
import matplotlib.pyplot as plt
from body import *


if __name__ == "__main__":
    # ARGUMENTS: name, parent, type, r, m, a, i, e, theta, raan, w, color
    
    # Cellestial Bodies
    Sol = Body("Sol", None, BodyType.Star, 696000e+3, 1.9891e+30, 0, 0, 0, 0, 0, 0, "yellow")
    
    Mercury = Body("Mercury", Sol, BodyType.Planet, 2439.7e+3, 3.3011e+23, 57909050e+3, 6.35, 0.205, 210, 48.331, 29.124, "sienna")

    Venus = Body("Venus", Sol, BodyType.Planet, 6051.8e+3, 4.8675e+24, 108.209e+9, 3.395, 0.0067, 270, 54, 54, "darkorange")
    
    Earth = Body("Earth", Sol, BodyType.Planet, 6371e+3, 5.9724e+24, 149.6e+9, 1.578690, 0.0167086, 10, 174.873, 288.1, "royalblue")
    Luna = Body("Luna", Earth, BodyType.Moon, 1737.1e+3, 0.07346e+24, .3844e+9, 5.145, 0, 0, 0, 0, "grey")
    
    Mars = Body("Mars", Sol, BodyType.Planet, 3389.5e+3, 6.39e+23, 227.923e+9, 1.851, .0935, 80, 5, 6, "firebrick")
    Phobos = Body("Phobos", Mars, BodyType.Moon, 11.267e+3, 10.6e+15, 9375e+3, 1.1, 0.015, 70, 280, 44, "tan")
    Deimos = Body("Deimos", Mars, BodyType.Moon, 6.2e+3, 1.5e+15, 23458e+3, 1.8, 0, 300, 180, 200, "wheat")
    
    Vesta = Body("Vesta", Sol, BodyType.Asteroid, 262.7e+3, 2.589e+20, 353.319e+9, 5.58, .08874, 144, 103.85, 151.198, "slategrey")
    Ceres = Body("Ceres", Sol, BodyType.DwarfPlanet, 473e+3, 9.3835e+20, 414261e+6, 9.2, 0.079009, 210, 80.305, 73.597, "darkcyan")
    Pallas = Body("Pallas", Sol, BodyType.Asteroid, 272.5e+3, 2.04e+20, 414960772.18583e+3, 34.43, .2299, 180.1, 173.024, 310.202, "aquamarine")
    Hygiea = Body("Hygiea", Sol, BodyType.Asteroid, 222e+3, 8.32e+19, 469961711e+3, 3.8316, .1125, 200, 283.2, 312.32, "peru")
    # Intermania
    # Europa (The asteroid)
    # Davida
    # Sylvia
    # Hektor
    # Juno
    # Fortuna 
    # Iris
    # Aurora
    # Bennu
    # Itokawa
    # Ryugu
    # Lutetia
    # Ida
    # Mathilde
    # Nike
    # Eros
    # Gaspra
    # Annefrank
    # Steins
    # Toutatis
    # Psyche


    Jupiter = Body("Jupiter", Sol, BodyType.Planet, 69911e+3, 1.8982e+27, 778567158e+3, .32, 0.04, 77, 100.464, 273.867, "orange")
    # Ganymede
    # Callisto
    # Io
    # Europa
    # Himalia
    # Amalthea
    # Elara
    # Thebe
    # Pasiphae
    # Carme
    # Sinope
    # Lysithea
    # Metis
    # Ananke
    # Leda

    Saturn = Body("Saturn", Sol, BodyType.Planet, 58232e+3, 5.6834e+26, 1.433537e+12, 0.93, 0.0565, 190, 113.665, 339.392, "navajowhite")
    # Titan
    # Rhea
    # Lapetus
    # Dione
    # Tethys
    # Enceladus
    # Mimas
    # Phoebe
    # Hyperion
    # Janus
    # Epimetheus
    # Prometheus
    # Pandora
    # Siarnaq
    # Helene
    # Albiorix
    # Telesto
    # Atlas
    # Calypso

    Uranus = Body("Uranus", Sol, BodyType.Planet, 25362e+3, 8.6810e+25, 2875046678e+3, 0.99, 0.046, 235, 74.006, 96.998, "lightsteelblue")
    # Oberon
    # Ariel
    # Umbriel
    # Miranda
    # Puck
    # Sycorax
    # Portia
    # Juliet
    # Belinda
    # Cressida
    # Desdomona
    # Dianca

    Neptune = Body("Neptune", Sol, BodyType.Planet, 24622e+3, 1.02413e+26, 4.49841e+12, 0.74, 0, 300, 131.784, 276.336, "blue")
    # Triton
    # Proteus
    # Nereid
    # Larissa
    # Despina
    # Galatea
    # Thalassa
    # Naiad
    # Halimede
    # Neso
    # Sao
    # Laomedeia
    # Psamathe
    # Hippocamp

    Pluto = Body("Pluto", Sol, BodyType.DwarfPlanet, 1188.3e+3, 1.309e+22, 5.906423e+12, 17.16, 0.2488, 163, 110.299, 113.834, "cadetblue")
    Charon = Body("Charon", Pluto, BodyType.Moon, 606e+3, 1.586e+21, 19591.4e+3, 112.783, 0, 64, 223.046, 0, "mediumorchid")
    Nix = Body("Nix", Pluto, BodyType.Moon, 49.8e+3, 4.5e+16, 48694e+3, 115.783, 0, 64,  223, 11, "lightgreen")
    Hydra = Body("Hydra", Pluto, BodyType.Moon, 50.9e+3, 4.8e+16, 64738e+6, 110, 0, 224, 224, 8, "seagreen")
    Styx = Body("Styx", Pluto, BodyType.Moon, 16e+3, 7.5e+15, 42656e+3, 112, 0, 33, 222, 359, "black")


    # Haumea (dwarf planet)
    # Hi'iaka
    # Namaka
    
    # Arrokoth

    # Makemake (dwarf planet)
    # S/2015 

    Sedna = Body("Sedna", Sol, BodyType.DwarfPlanet, 998e+3, 8.32e+21, 7.57e+13, 11.9307, 0.8496, 170, 144.248, 311.352, "pink")
    
    Eris = Body("Eris", Sol, BodyType.DwarfPlanet, 1163e+3, 1.6466e+22, 1.015231e+13, 44.040, 0.43607, 200, 35.951, 151.639, "indianred")
    Dysnomia = Body("Dysnomia", Eris, BodyType.Moon, 350e+3, 3.6e+20, 37273e+3, 78.29, 0, 80, 126.17, 89, "yellowgreen")

    Biden = Body("Biden", Sol, BodyType.DwarfPlanet, 597e+3, 1.782e+21, 6.5246064e+13, 24.110, 0.68876, 200, 90.680, 293.62, "dodgerblue")

    Leleakuhonua = Body("Leleakuhonua", Sol, BodyType.DwarfPlanet, 100e+3, 8.38e+18, 1.6231e+14, 11.654, 0.9399, 190, 300.78, 117.778, "teal")

    # Quaoar (dwarf planet)
    # Weywot

    Orcus = Body("Orcus", Sol, BodyType.DwarfPlanet, 910e+3, 6.348e+20, 5.860347e+12, 20.592, 0.22701, 85, 268.799, 72.310, "maroon")
    Vanth = Body("Vanth", Orcus, BodyType.Moon, 442.5e+3, 4.2e+19, 8999.8e+3, 105.03, 0, 2, 0, 0, "green")

    # Gonggong (dwarf planet)
    # Xiangliu

    # Commets
    # Halley's Commet
    # Donati's Comet
    # Coggia's Comet
    # Ceasar's Commet
    # Comet Mrkos
    # Comet Kohoutek
    # Comet West
    # Comet Hyakutake
    # Comet McNaught
    # Commet Bennet
    # Catalina
    # Borrelly
    # Wild 2
    # Tempel 1
    # Hartley 2
  
    countBodies(Sol)
    plotSystem(Sol)     
