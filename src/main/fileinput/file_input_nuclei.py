import os
import sys
from src.main.objects import Nuclei


class FileInputNuclei:

    def __init__(self, file_input_mol):
        self.file_input_mol = os.path.join(sys.path[1], 'molfiles\\' + file_input_mol)

    def create_nuclei_array_and_electron_count(self):
        nuclei_array = []
        total_nuclei_charge = 0
        with open(self.file_input_mol, 'r') as file:
            lines = file.readlines()
            molecular_charge = int(lines[0].split()[0])
            multiplicity = int(lines[0].split()[1])
            for a in range(1, len(lines)):
                line = lines[a]
                array = line.split()
                total_nuclei_charge += int(array[1])
                coordinates = (float(array[3]), float(array[4]), float(array[5]))
                nuclei = Nuclei(array[0], float(array[1]), float(array[2]), coordinates)
                nuclei_array.append(nuclei)
        file.close()
        electron_count = total_nuclei_charge - molecular_charge
        return nuclei_array, electron_count, multiplicity

