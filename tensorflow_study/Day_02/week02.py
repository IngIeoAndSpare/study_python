from Calculration import CalculrationModule
from PandasStudy import FileReadModule

# mod1.py 
def add(a, b = 1): 
    return a+b, a-b

if __name__ == "__main__":
    #b = CalculrationModule(1,2).create_array_reshape(20,4,5)
    #print(b)
    #print(b[0:2, 0:2])

    c = FileReadModule('C:\\DevelopeToo\\tensorflow_study\\Day_02\\iris.csv')
    c.file_reader_csv()

    #print(c.file.describe()) # 그 외에도 values, columns, tail, head 등 여러 메소드가 있다.
    #print(c.get_colum_item('sepal.length'))

    c.show_data()
