import numpy as np

class CalculrationModule:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        return self.number1 + self.number2

    def create_array(self, dim, item_count):
        return np.zeros(tuple([item_count for i in range(dim)]))

    def create_araray_eye(self, count):
        return np.eye(count) # 대각 행렬 생성

    def create_array_arange(self, start, count, dept = 1):
        return np.arange(start, count, dept) # 1차원 배열 생성
    
    def create_array_reshape(self, count, row_count, col_count):
        return np.array(range(count)).reshape(row_count, col_count) #결과 뒤에 [0:2, 0:2]를 붙여서 슬라이싱이 가능하다. ex) create_array_reshape(20,4,5)[0:2, 0:2]

    def metrix_cross_product(self, source: np.array, target: np.array):
        return source @ target
    
    def metrix_dot_product(self, soruce: np.array, target: np.array):
        return soruce.dot(target)

    def get_random(self, seed_num, item_count, normal = False, suffle_flag = False):
        np.random.seed(seed_num)
        if(normal):
            return np.random.shuffle(np.random.randn(item_count)) if suffle_flag else np.random.randn(item_count)
        else:
            return np.random.shuffle(np.random.rand(item_count)) if suffle_flag else np.random.rand(item_count)