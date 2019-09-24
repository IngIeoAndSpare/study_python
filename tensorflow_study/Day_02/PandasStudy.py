import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class FileReadModule:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = None

    def change_file_path(self, file_path):
        self.file_path = file_path

    def file_reader_csv(self):
        self.file = pd.read_csv(self.file_path)

    def get_colum_item(self, col_name):
        return self.file[col_name]

    def show_data(self):
        plt.plot(data = self.file)
        plt.show()

