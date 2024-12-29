# %%
import numpy as np
import matplotlib.pyplot as plt

class RadioactiveDecay:
    def __init__(self, decay_constant):
        """
        Initialize the RadioactiveDecay object with a decay constant.
        :param decay_constant: Decay constant (lambda) for the isotope.
        """
        self.decay_constant = decay_constant

    def calculate_remaining(self, initial_amount, time):
        """
        Calculate the remaining amount of isotope over time.
        :param initial_amount: Initial quantity of the isotope.
        :param time: Array of time points.
        :return: Array of remaining isotope quantities at each time point.
        """
        return initial_amount * np.exp(-self.decay_constant * time)

    def calculate_half_life(self):
        """
        Calculate the half-life of the isotope.
        :return: Half-life of the isotope.
        """
        return np.log(2) / self.decay_constant


class TracerModel:
    def __init__(self, decay_constant, dilution_rate):
        """
        Initialize the TracerModel object with decay and dilution constants.
        :param decay_constant: Decay constant (lambda) for the tracer.
        :param dilution_rate: Dilution rate of the tracer in the system.
        """
        self.decay_constant = decay_constant
        self.dilution_rate = dilution_rate

    def concentration_over_time(self, initial_concentration, time):
        """
        Simulate tracer concentration over time considering decay and dilution.
        :param initial_concentration: Initial concentration of the tracer.
        :param time: Array of time points.
        :return: Array of tracer concentrations at each time point.
        """
        effective_decay = self.decay_constant + self.dilution_rate
        return initial_concentration * np.exp(-effective_decay * time)


class Plotter:
    @staticmethod
    def plot_concentration(time, concentrations, title):
        """
        Plot concentration changes over time.
        :param time: Array of time points.
        :param concentrations: Array of concentrations.
        :param title: Title of the plot.
        """
        plt.figure(figsize=(8, 6))
        plt.plot(time, concentrations, label='Concentration')
        plt.xlabel('Time (units)')
        plt.ylabel('Concentration (units)')
        plt.title(title)
        plt.grid(True)
        plt.legend()
        plt.show()


# %%
