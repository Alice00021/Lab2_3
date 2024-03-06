import numpy as np
def get_matrix_from_input():
    try:
        rows = int(input("Введите количество строк матрицы: "))
        cols = int(input("Введите количество столбцов матрицы: "))
        print("Введите элементы матрицы построчно (разделите элементы пробелами):")
        matrix = []
        for i in range(rows):
            row = list(map(float, input().split()))
            if len(row) != cols:
                print("Ошибка: количество элементов в строке не соответствует количеству столбцов")
                return None
            matrix.append(row)
        return matrix
    except ValueError:
        print("Ошибка: введите корректные числа")
        return None

def main():
    matrix = get_matrix_from_input()
    if matrix:
        try:
            det = np.linalg.det(matrix)
            print("Определитель матрицы равен:", det)
        except np.linalg.LinAlgError:
            print("Ошибка: матрица вырожденная, определитель не может быть вычислен")

if __name__ == "__main__":
    main()