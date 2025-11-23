import importlib.util
import numpy as np
import matplotlib.pyplot as plt


# === Import Lumerical API ===
module_name = "lumapi"
module_path = "C:/Program Files/Lumerical/v242/api/python/lumapi.py" # replace if needed
spec = importlib.util.spec_from_file_location(module_name, module_path)
lumapi = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lumapi)


# === Spusti MODE ===
mode = lumapi.MODE()


SiN = "Si3N4 (Silicon Nitride) - Luke";

import inverse_tapers 




inverse_tapers.exponencial(solver_object = mode, material = SiN, 
                            w_start = 1 , w_end = 100 , length = 150, 
                            x = 0 , y = 0, z_min = 0, z_max = 0.4)

inverse_tapers.quadratic(solver_object = mode, material = SiN, 
                            w_start = 1 , w_end = 100 , length = 150, 
                            x = 0 , y = 0, z_min = 0, z_max = 0.4)

inverse_tapers.cubic(solver_object = mode, material = SiN, 
                            w_start = 1 , w_end = 100 , length = 150, 
                            x = 0 , y = 0, z_min = 0, z_max = 0.4)
inverse_tapers.nth_power(solver_object = mode, material = SiN, 
                            w_start = 1 , w_end = 100 , length = 150, 
                            x = 0 , y = 0, z_min = 0, z_max = 0.4, n=5)

inverse_tapers.lumerical(solver_object = mode, material = SiN, 
                            w_start = 1 , w_end = 100 , length = 150, 
                            x = 0 , y = 0, z_min = 0, z_max = 0.4, m=0.5)

inverse_tapers.M_R_Karim(solver_object = mode, material = SiN, 
                            w_start = 1 , w_end = 100 , length = 150, 
                            x = 0 , y = 0, z_min = 0, z_max = 0.4, a=0.5)




