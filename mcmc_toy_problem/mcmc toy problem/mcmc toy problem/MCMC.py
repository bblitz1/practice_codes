import numpy as np

class MCMCModel:
    def __init__(self, t, data_generator):
        self.t = t
        self.data_generator = data_generator
    
    def polynomial(self, v=-1, a=1, b=0):
        """
        Computes the polynomial function.
        """
        return 4 + v * self.t + (0.5 * a * self.t**2) + b * (self.t**3)

    def generate_data(self, x, A=0):
        """
        Generates noisy data by adding random noise.

        Args:
        - x: numpy array of true values
        - A: amplitude of noise

        Returns:
        - numpy array of noisy data
        """
        noise = A * np.random.random(len(x))
        return x + noise

    def compute_rms(self, observed, predicted):
        diff = observed - predicted
        return np.sqrt(np.mean(diff**2))

    def fit_with_noise(self, a_low, a_high, v_low, v_high, N, noise_amplitude, b=0):
        """
        Fits the data with noise for a given amplitude and returns the best-fit parameters and likelihood.

        Args:
        - a_low, a_high: bounds for acceleration
        - v_low, v_high: bounds for velocity
        - N: number of grid points
        - noise_amplitude: amplitude of the noise
        - b: coefficient of cubic term (default: 0)

        Returns:
        - best_a: best-fit acceleration
        - best_v: best-fit velocity
        - likelihood: likelihood of the best fit
        """
        true_vals = self.polynomial(v=-1, a=1, b=b)
        noisy_vals = self.generate_data(true_vals, noise_amplitude)

        a_values = np.linspace(a_low, a_high, N)
        v_values = np.linspace(v_low, v_high, N)
        rms_errors = []

        for v_val in v_values:
            for a_val in a_values:
                trial_vals = self.polynomial(v=v_val, a=a_val, b=b)
                rms_error = self.compute_rms(noisy_vals, trial_vals)
                rms_errors.append(rms_error)

        rms_errors = np.array(rms_errors)
        best_index = np.argmin(rms_errors)
        best_a = a_values[best_index % N]
        best_v = v_values[best_index // N]

        best_rms = rms_errors[best_index]
        likelihood = 1 / best_rms if best_rms != 0 else np.inf

        return best_a, best_v, likelihood

    def likelihood(self, noisy_vals, a, v, b=0):
        trial_vals = self.polynomial(v=v, a=a, b=b)
        rms_error = self.compute_rms(noisy_vals, trial_vals)
        likelihood = 1 / rms_error if rms_error != 0 else np.inf
        return likelihood

    def metropolis_hastings(self, a_range, v_range, num_iterations, noise_amplitude, b=0):
        a_low, a_high = a_range
        v_low, v_high = v_range

        true_vals = self.polynomial(v=-1, a=1, b=b)
        noisy_vals = self.generate_data(true_vals, noise_amplitude)

        current_a = np.random.uniform(a_low, a_high)
        current_v = np.random.uniform(v_low, v_high)
        current_likelihood = self.likelihood(noisy_vals, current_a, current_v, b)

        samples = [(current_a, current_v)]

        for _ in range(num_iterations):
            proposed_a = np.random.uniform(a_low, a_high)
            proposed_v = np.random.uniform(v_low, v_high)
            proposed_likelihood = self.likelihood(noisy_vals, proposed_a, proposed_v, b)

            acceptance_ratio = proposed_likelihood / current_likelihood
            if acceptance_ratio > np.random.uniform(0, 1):
                current_a, current_v, current_likelihood = proposed_a, proposed_v, proposed_likelihood

            samples.append((current_a, current_v))

        return samples