impot cirq hibrido
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

