from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit, Aer, execute
from qiskit.tools.visualization import circuit_drawer
import numpy as np
q = QuantumRegister(3)
c = ClassicalRegister(3)
qc = QuantumCircuit(q,c)

# Define the coefficients
coefficient_000 = 1
coefficient_001 = 2
coefficient_010 = 3
coefficient_011 = 4
coefficient_100 = 5
coefficient_101 = 6
coefficient_110 = 7
coefficient_111 = 8

# Calculate the normalization factor
norm_factor = (coefficient_000**2 + coefficient_001**2 + coefficient_010**2 +
               coefficient_011**2 + coefficient_100**2 + coefficient_101**2 +
               coefficient_110**2 + coefficient_111**2)**0.5

# Normalize the coefficients
alpha_000 = coefficient_000 / norm_factor
alpha_001 = coefficient_001 / norm_factor
alpha_010 = coefficient_010 / norm_factor
alpha_011 = coefficient_011 / norm_factor
alpha_100 = coefficient_100 / norm_factor
alpha_101 = coefficient_101 / norm_factor
alpha_110 = coefficient_110 / norm_factor
alpha_111 = coefficient_111 / norm_factor

# Apply gates with the normalized coefficients
qc.initialize([alpha_000, alpha_001, alpha_010, alpha_011, alpha_100, alpha_101, alpha_110, alpha_111])
print("for doing from 1 2 3 4 5 6 7 8 to 5 6 7 8 1 2 3 4 applying NOT2")
qc.x(q[2])
qc.measure(q,c)
#S_simulator = Aer.backends(name='statevector_simulator')[0]
#job=execute(qc,S_simulator)
#result=job.result()
#print(result.get_statevector())
M_simulator = Aer.backends(name='qasm_simulator')[0]
M=execute(qc,M_simulator,shots=100).result().get_counts(qc)
print(M)


# Write your code here


print(qc.draw())