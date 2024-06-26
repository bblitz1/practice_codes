import numpy as np

class Polynomial:
    def __init__(self, t):
        """
        METHOD: this function outputs 4-t+0.5t^2 for an array of supplied t values
    
        INPUT: 
        ------
        t: values of time (numpy array)
        a: acceleration value (float)
        b: coefficient of cubic term (default is 0)
        v: initial velocity (float)
        
        OUTPUT: 
        -------
        returns the value of the polynomial
        """
        
        self.t = t
        
    def create(self, a=1, v=-1, b=0):
      
        return 4 + v * self.t + (0.5* a* self.t**2) + b*(self.t**3)


    def fitting(self, a_low, a_hi, v_low, v_hi, N, b=0):
        """
        METHOD: This function accepts the bounds of the `a` and `v` and the total number of grid points,
        constructs a grid on both the variables, and computes the fit of the polynomial function.
    
        INPUT:
        ------
        a_low: lowest range of acceleration value
        a_hi: highest range of acceleration value
        v_low: lowest range of velocity value
        v_hi: highest range of velocity value
        N: number of grid points
        x_vals_true: true values of x (numpy array)
        b: coefficient of the cubic term (default: 0)
    
        OUTPUT:
        Returns the fitted parameters, the RMS error array, and the grid points.
        """
        x_vals_true = self.create()
        a = np.linspace(a_low, a_hi, N)
        v = np.linspace(v_low, v_hi, N)
        rms = []
        grid_points = []
        for v_val in v:
            for a_val in a:
                x_trial = self.create(v=v_val, a=a_val, b=b)  # Pass b to the modified polynomial function
                diff = x_vals_true - x_trial
                rms.append(np.sqrt(np.mean(diff**2)))
                grid_points.append((a_val, v_val))
        rms = np.array(rms)
        best_index = np.argmin(rms)
        a_fit, v_fit = grid_points[best_index]  
        return a_fit, v_fit, rms, a, v


