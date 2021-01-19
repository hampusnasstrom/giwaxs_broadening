import numpy as np


class Detector:

    def __init__(self, detector: str, x_pos=300, y_pos=0, z_pos=0):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.z_pos = z_pos
        if detector == 'pilatus_1m':
            self.mask = np.ones((1043, 981))
            self.mask[:, 487:487+7] = 0
            for i in range(4):
                self.mask[195+i*(195+17):195+i*(195+17)+17, :] = 0
            self.y_size = 172
            self.z_size = 172
        else:
            raise NotImplementedError

    def get_two_theta(self):
        z_low = self.z_pos
        z_high = self.z_pos + self.mask.shape[0] * self.z_size * 1e-3
        two_theta_low = np.arctan(z_low / self.x_pos) * 180 / np.pi
        two_theta_high = np.arctan(z_high / self.x_pos) * 180 / np.pi
        return two_theta_low, two_theta_high

    def set_x_pos(self, x_pos):
        self.x_pos = x_pos

    def set_y_pos(self, y_pos):
        self.y_pos = y_pos

    def set_z_pos(self, z_pos):
        self.z_pos = z_pos

    def get_y_z(self):
        y = np.arange(self.mask.shape[1]) * self.y_size
        z = np.arange(self.mask.shape[0]) * self.z_size
        return np.meshgrid(y, z)
