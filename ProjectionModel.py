import numpy as np


def _validate(variable) -> np.ndarray:
    if isinstance(variable, int) or isinstance(variable, float):
        return np.array([variable])
    elif isinstance(chi, list):
        return np.array(variable)
    elif isinstance(variable, np.ndarray):
        if len(variable.shape) > 1:
            raise TypeError
        else:
            return variable
    else:
        raise TypeError


class ProjectionModel:

    def __init__(self, chi, x_det, two_theta, beam_diameter, radial_divergence):
        """

        :param chi: Incidence angle of beam on to sample in degrees
        :param x_det: Distance from sample to detector along the beam in mm
        :param two_theta: Diffraction angle in degrees
        :param beam_diameter: Beam diameter at the sample position in mm
        :param radial_divergence: Radial divergence of the beam in mrad, positive converging, negative diverging
        """
        self.chi = _validate(chi).reshape((-1, 1, 1, 1, 1)) * np.pi / 180
        self.x_d = _validate(x_det).reshape((1, -1, 1, 1, 1))
        self.two_theta = _validate(two_theta).reshape((1, 1, -1, 1, 1)) * np.pi / 180
        self.w_0 = _validate(beam_diameter).reshape((1, 1, 1, -1, 1))
        self.delta = _validate(radial_divergence).reshape((1, 1, 1, 1, -1)) * 1e-3

        self.zh = None
        self.zl = None
        self.broadening = None

        self.calculate()

    def calculate(self):
        a = self.w_0 * np.cos(self.delta) / (2 * np.sin(self.chi - self.delta))
        b = self.w_0 * np.cos(self.delta) / (2 * np.sin(self.chi + self.delta))
        zpp = a * np.sin(self.chi)
        xpp = a * np.cos(self.chi)
        zpm = b * np.sin(self.chi)
        xpm = b * np.cos(self.chi)
        zh = np.tan(self.two_theta + self.delta) * (self.x_d + xpp) - zpp
        zl = np.tan(self.two_theta - self.delta) * (self.x_d - xpm) + zpm
        self.broadening = (np.arctan(zh / self.x_d) - np.arctan(zl / self.x_d)) * 180 / np.pi


if __name__ == "__main__":
    # import matplotlib.pyplot as plt
    divergence = [1.1, 2.2]
    distance = [320, 500]
    two_thetas = [15, 45]
    w0 = [0.1, 2]
    chi = [2, 5]
    test = ProjectionModel(chi,
                           distance,
                           two_thetas,
                           w0,
                           divergence)
    print(test.broadening)
    # divergence = np.linspace(0.0, 10, 1000)
    # divergence = np.array([1.1])
    # # distance = np.linspace(200, 2000, 1000)
    # distance = np.array([500])
    # two_thetas = np.linspace(5, 70, 1000)
    # w0 = np.array([0.5])
    # chi = np.array([5.])
    # test = ProjectionModel(chi,
    #                        distance,
    #                        two_thetas,
    #                        w0,
    #                        divergence)
    # plt.plot(two_thetas, test.broadening * 180 / np.pi)
