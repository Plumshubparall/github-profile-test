 nova impot cirq hibrido
# crear un circuito cuántico 
q0 = cirq.GridQubit(0,0)
q1 = cirq.GridQubit(1,0)
qc = cirq.Circuit() 
# Agregar una puerta de Hadamard al primer qubit
qc.append(cirq.H(q0))
# Agregar una puerta de entrelazamiento entre los cubit 
qc.append(cirq.CNOT(q0,q1))
# Agregar una puertaderotación al primer qubit
qc.append(cirq.rx(0.5)(q0))
# Optimizar el circuito cuántico 
optimized_qc=cirq.merge_k_qubit_unitaries(qc,k=2)
#imprimir el circuito cuántico original y optimizado 
primt("Circuito cuántico original :")
print(qc)
print("Circuito cuántico optimizado.")
print(optimized_qc)

## Resultados esperados 
-----------------
Al aplicar la puerta de Hadamard a un cubit en el estado |0,se espera obtener una super posición de los estados|0y|].

###Resultados teóricos
*Estado inicial:|0
*Estado final:(|0+|1)/**1/2

### Resultado de la simulacion 
*[insertar imagen o tabla con resultados de la simulación]

###Código para obtener resultados
´python
#Código para simular la puera de Hadamardy obtener resultados

import numpy as np

#Define la puerta de Hadamard 
H=1/np.sqrt(2)*np.array([[1,1],[1,-1]])

#Define el estado inicial |0
estado_inicial=np.array([1,0])

#Aplica la puerta de Hadamard al estado inicial
estado_final=np.dot(H,estado_inicial)
print("Estado final.",estado_final)


import numpyas np

#Define la puerta de Hadamard 

H=1/2**0.5*np.array([[1,1],[1,-1]])
#Define el estado inicial |0
estado_inicial=np,array([1,0])

#Aplica la puerta de Hadamard al estado inicial
estado_final=np.dot(H,estado_inicial)

print("Estado final.",estado_final)


import matplotlib.pyplot as plt
import numpy as np

#Define la puerta de Hadamard
H=1/2**05.*np.array([[1,1],[1,-1]])

#Define el estado inicial |0 
estado_inicial=np.array([1,0])

#Aplica la puerta de Hadamard al estado inicial
estado_final=np.dot(H,estado_inicial)

#Crea un gráfico simple
plt.bar([0,1],np.abs(estado_final)**2)
plt.xlabel(´Estado´)
plt.ylabel(´Probabilidad´)
plt.title(Éstado final´) 
plt.show()

#Guarda el grafico como imagen 
plt.savefig(éstado_final.png´)   
https://www.nova.io
