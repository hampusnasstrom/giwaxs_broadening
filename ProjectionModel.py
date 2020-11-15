import numpy as np


class ProjectionModel:

    def __init__(self, chi, x_det, two_theta, beam_diameter, radial_divergence):
        self.chi = chi * np.pi / 180
        self.x_d = x_det
        self.two_theta = two_theta * np.pi / 180
        self.w_0 = beam_diameter
        self.delta = radial_divergence * 1E-3
        self.broadening = np.zeros((len(self.chi),
                                    len(self.x_d),
                                    len(self.two_theta),
                                    len(self.w_0),
                                    len(self.delta)))
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
        self.broadening = np.arctan(zh / self.x_d) - np.arctan(zl / self.x_d)


if __name__ == "__main__":
    test = ProjectionModel(np.array([2]),
                           np.array([300]),
                           np.array([45]),
                           np.array([0.1]),
                           np.array([1]))
    print(test.broadening*180/np.pi)
