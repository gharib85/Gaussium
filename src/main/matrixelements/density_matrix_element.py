class DensityMatrix:

    def __init__(self, orbital_coefficient_matrix, electrons):
        self.orbital_coefficient_matrix = orbital_coefficient_matrix
        self.electrons = electrons


class DensityMatrixRestricted(DensityMatrix):

    def calculate(self, i, j):
        p_ij = 0
        c = self.orbital_coefficient_matrix
        for a in range(int((1/2) * self.electrons)):
            p_ij += 2 * c.item(i, a) * c.item(j, a)
        return p_ij


class DensityMatrixUnrestricted(DensityMatrix):

    def calculate(self, i, j):
        p_ij = 0
        c = self.orbital_coefficient_matrix
        for a in range(self.electrons):
            p_ij += c.item(i, a) * c.item(j, a)
        return p_ij
