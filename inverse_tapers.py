import numpy as np
import matplotlib.pyplot as plt
# propagation in is x-axis
#   x,y = [0,0]  - center
#   z - height of the taper
#   input in micrometers [um]
#
# [1]G. Ren, S. Chen, Y. Cheng, and Y. Zhai, “Study on inverse taper based mode transformer for low loss coupling between silicon wire waveguide and lensed fiber,” Optics Communications, vol. 284, no. 19, pp. 4782–4788, Sep. 2011, doi: https://doi.org/10.1016/j.optcom.2011.05.072.
# [2] https://optics.ansys.com/hc/en-us/articles/360042799713-Curved-waveguide-taper-varFDTD-and-FDTD
# [3] M. R. Karim, N. A. Kayed, R. Rafi, and A. Rahman, “Design and analysis of inverse tapered silicon nitride waveguide for flat and highly coherent supercontinuum generation in the mid-infrared,” Optical and Quantum Electronics, vol. 56, no. 1, Dec. 2023, doi: https://doi.org/10.1007/s11082-023-05636-5.


# =============================================================================
#  IF YOU WANT NORMAL TAPER ROTATE IT AND CHANGE x,y 
# solver.set("first axis","y");
# solver.set("rotation 1",180);
# solver.set("x",x)
# solver.set("y",y) // if y = 0 not needed
# =============================================================================


# from [1]   
def exponencial(solver_object, material, w_start, w_end, length, x, y, z_min, z_max, num_of_points = 1000):

    w_start = w_start/2 # only half 
    w_end = w_end/2

    v = np.empty((0, 2)) # init empty matrix
    
    x_points = np.linspace(0, length, num_of_points)
    
    norm = x_points / length # normalization        
    
    function = (np.exp(norm) - 1) / (np.exp(1) - 1) # function that defines the taper
    
    # this normalizes the input and output widths
    w = w_start + (w_end - w_start) * function
    
    # fill the empty matrix
    v_bottom = np.array([[x_points[i]*1e-6, -w[i]*1e-6] for i in range(len(x_points))])
    v_top = np.array([[x_points[i]*1e-6, w[i]*1e-6] for i in reversed(range(len(x_points)))])
    v = np.vstack([v_bottom, v_top])
    
    solver_object.addpoly()
    solver_object.set("name", "taper_costum")
    solver_object.set("vertices", v)
    solver_object.set("x", x*1e-6)
    solver_object.set("y", y*1e-6)
    solver_object.set("z min", z_min*1e-6)
    solver_object.set("z max", z_max*1e-6)
    solver_object.set("color opacity", 1)
    solver_object.set("material",material)
    
    plt.plot(v[:,0], v[:,1])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis("equal")
    plt.title(label="Created taper - exponencial")
    plt.show()
    

# from [1]   
def quadratic(solver_object, material, w_start, w_end, length, x, y, z_min, z_max, num_of_points = 1000):

    w_start = w_start/2 # only half 
    w_end = w_end/2

    v = np.empty((0, 2)) # init empty matrix
    
    x_points = np.linspace(0, length, num_of_points)
    
    norm = x_points / length # normalization        
    
    function = norm ** 2 # function that defines the taper
    
    # this normalizes the input and output widths
    w = w_start + (w_end - w_start) * function
    
    # fill the empty matrix
    v_bottom = np.array([[x_points[i]*1e-6, -w[i]*1e-6] for i in range(len(x_points))])
    v_top = np.array([[x_points[i]*1e-6, w[i]*1e-6] for i in reversed(range(len(x_points)))])
    v = np.vstack([v_bottom, v_top])
    
    solver_object.addpoly()
    solver_object.set("name", "taper_costum")
    solver_object.set("vertices", v)
    solver_object.set("x", x*1e-6)
    solver_object.set("y", y*1e-6)
    solver_object.set("z min", z_min*1e-6)
    solver_object.set("z max", z_max*1e-6)
    solver_object.set("color opacity", 1)
    solver_object.set("material",material)
    
    plt.plot(v[:,0], v[:,1])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis("equal")
    plt.title(label="Created taper - quadratic")
    plt.show()
    
def cubic(solver_object, material, w_start, w_end, length, x, y, z_min, z_max, num_of_points = 1000):

    w_start = w_start/2 # only half 
    w_end = w_end/2

    v = np.empty((0, 2)) # init empty matrix
    
    x_points = np.linspace(0, length, num_of_points)
    
    norm = x_points / length # normalization        
    
    function = norm ** 3 # function that defines the taper
    
    # this normalizes the input and output widths
    w = w_start + (w_end - w_start) * function
    
    # fill the empty matrix
    v_bottom = np.array([[x_points[i]*1e-6, -w[i]*1e-6] for i in range(len(x_points))])
    v_top = np.array([[x_points[i]*1e-6, w[i]*1e-6] for i in reversed(range(len(x_points)))])
    v = np.vstack([v_bottom, v_top])
    
    solver_object.addpoly()
    solver_object.set("name", "taper_costum")
    solver_object.set("vertices", v)
    solver_object.set("x", x*1e-6)
    solver_object.set("y", y*1e-6)
    solver_object.set("z min", z_min*1e-6)
    solver_object.set("z max", z_max*1e-6)
    solver_object.set("color opacity", 1)
    solver_object.set("material",material)
    
    plt.plot(v[:,0], v[:,1])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis("equal")
    plt.title(label="Created taper - cubic")
    plt.show()
    
# just for test
def nth_power(solver_object, material, w_start, w_end, length, x, y, z_min, z_max, n, num_of_points = 1000):

    w_start = w_start/2 # only half 
    w_end = w_end/2

    v = np.empty((0, 2)) # init empty matrix
    
    x_points = np.linspace(0, length, num_of_points)
    
    norm = x_points / length # normalization        
    
    function = norm ** n # function that defines the taper
    
    # this normalizes the input and output widths
    w = w_start + (w_end - w_start) * function
    
    # fill the empty matrix
    v_bottom = np.array([[x_points[i]*1e-6, -w[i]*1e-6] for i in range(len(x_points))])
    v_top = np.array([[x_points[i]*1e-6, w[i]*1e-6] for i in reversed(range(len(x_points)))])
    v = np.vstack([v_bottom, v_top])
    
    solver_object.addpoly()
    solver_object.set("name", "taper_costum")
    solver_object.set("vertices", v)
    solver_object.set("x", x*1e-6)
    solver_object.set("y", y*1e-6)
    solver_object.set("z min", z_min*1e-6)
    solver_object.set("z max", z_max*1e-6)
    solver_object.set("color opacity", 1)
    solver_object.set("material",material)
    
    plt.plot(v[:,0], v[:,1])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis("equal")
    plt.title(label=f"Created taper - n^{n}")
    plt.show()

def lumerical(solver_object, material, w_start, w_end, length, x, y, z_min, z_max, m, num_of_points = 1000):

    w_start = w_start/2 # only half 
    w_end = w_end/2

    v = np.empty((0, 2)) # init empty matrix
    
    x_points = np.linspace(0, length, num_of_points)
    
    # equation from lumerical [2]
    
    alfa = (w_start - w_end) / length ** m
    
    w = alfa * (length - x_points) ** m + w_end
    
    
    # fill the empty matrix
    v_bottom = np.array([[x_points[i]*1e-6, -w[i]*1e-6] for i in range(len(x_points))])
    v_top = np.array([[x_points[i]*1e-6, w[i]*1e-6] for i in reversed(range(len(x_points)))])
    v = np.vstack([v_bottom, v_top])
    
    solver_object.addpoly()
    solver_object.set("name", "taper_costum")
    solver_object.set("vertices", v)
    solver_object.set("x", x*1e-6)
    solver_object.set("y", y*1e-6)
    solver_object.set("z min", z_min*1e-6)
    solver_object.set("z max", z_max*1e-6)
    solver_object.set("color opacity", 1)
    solver_object.set("material",material)
    
    plt.plot(v[:,0], v[:,1])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis("equal")
    plt.title(label=f"Created taper - lumerical m={m}")
    plt.show()

    
# [3]

# this is the same as lumerical how ever it is normal taper not inverse
def M_R_Karim(solver_object, material, w_start, w_end, length, x, y, z_min, z_max, a, num_of_points = 1000):

    w_start = w_start/2 # only half 
    w_end = w_end/2

    v = np.empty((0, 2)) # init empty matrix
    
    x_points = np.linspace(0, length, num_of_points)
    
    # equation from lumerical [2]
    
    
    w = w_end  - (w_end - w_start) * (x_points / length) ** a
    
    
    # fill the empty matrix
    v_bottom = np.array([[x_points[i]*1e-6, -w[i]*1e-6] for i in range(len(x_points))])
    v_top = np.array([[x_points[i]*1e-6, w[i]*1e-6] for i in reversed(range(len(x_points)))])
    v = np.vstack([v_bottom, v_top])
    
    solver_object.addpoly()
    solver_object.set("name", "taper_costum")
    solver_object.set("vertices", v)
    solver_object.set("x", x*1e-6)
    solver_object.set("y", y*1e-6)
    solver_object.set("z min", z_min*1e-6)
    solver_object.set("z max", z_max*1e-6)
    solver_object.set("color opacity", 1)
    solver_object.set("material",material)
    solver_object.set("rotation 1", 180)
    
    plt.plot(v[:,0], v[:,1])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis("equal")
    plt.gca().invert_xaxis()
    plt.title(label=f"Created taper - M_R_Karim a={a}")
    plt.show()
 
    
    
    