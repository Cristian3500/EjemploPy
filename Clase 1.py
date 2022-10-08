# Online Python Compiler
# Run Python code without any setup
import numpy as np

print ('--------------------  ESCALAR  ----------------')
# Escalar
e = 5
print (e)

print ('--------------------  VECTOR  ----------------')
# Vector
v = np.array([2,8,-4])
print (v)

print ('--------------------  MATRIZ  ----------------')
# Matrices
m = np.array([[1,0,-9], [3,-6,7]])
print (m)


print ('--------------------  TIPOS DE DATOS DE MATRICES  ----------------')
# Declaración de Array
array = np.array([5])
print (type(array))
#Tipos de datos
print(type(e))
print(type(v))
print(type(m))

print ('--------------------  DIMENSIÓN DE MATRICES  ----------------')
# Dimensión o forma de una matriz
print (m.shape)
print (array.shape)

print ('--------------------  REESCRIBIR DIMENSIÓN DE MATRICES  ----------------')
# Reescribir matriz. v = np.array([2,8,-4])
print (v.reshape(1,3))
print (v.reshape(3,1))


# Suma de Matrices
print ('--------------------  SUMA DE MATRICES  ----------------')
m1 = np.array([[5,12,6],[-3,0,14]])
m2 = np.array([[9,8,7], [1,3,-5]])

print (m1 + m2)

# Resta de Matrices
print ('--------------------  RESTA DE MATRICES  ----------------')
m1 = np.array([[5,12,6],[-3,0,14]])
m2 = np.array([[9,8,7], [1,3,-5]])
print (m1 - m2)

# Solo es posible en numpy pero no en algebra lineal
print ('--------------------  SUMA DE UN ESCALAR Y UNA MATRIZ  ----------------')
m3 = np.array([[9,8,7], [1,3,-5]])
print (m3 + 2)

#Transpuesta de una matriz
print ('--------------------  TRANSPUESTA DE UNA MATRIZ ----------------')
m4 = np.array([[5,12,6],[-3,0,14]])
print ('Matriz: ')
print (m4)
print ('Matriz Transpuesta: ')
print (m4.T)

#Transpuesta de un Vector
print ('--------------------  TRANSPUESTA DE UN VECTOR ----------------')
v1 = np.array([2,8,-4])
print ('Vector: ')
print (v1)
print ('Transpuesta de un Vector')
print ((v1.reshape(1,3)).T)
