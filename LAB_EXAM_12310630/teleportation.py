from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute
from qiskit.visualization import circuit_drawer
from qiskit.visualization import plot_histogram
import math
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)



M_simulator = Aer.get_backend('qasm_simulator')
S_simulator = Aer.get_backend('statevector_simulator')

q = QuantumRegister(3)
c = ClassicalRegister(1)
qc = QuantumCircuit(q, c)

#creating the state alpha|0> + beta|1> such that alpha^2 + beta^2 =1
print("Alice's qubit 0.6|0>+0.8|1>\n")
qc.initialize([0.6,0.8], 0)
qc.barrier()

#creating entangled pair 
print("new entangle pair |01>+|10>")
qc.h(q[1])
qc.x(q[2])
qc.cx(q[1],q[2])
qc.barrier()

#at Alice's side
qc.cx(0,1)
qc.h(0)

qc.barrier()

#at Bob's side
qc.x(q[2])  #this is the change bob need to do 
qc.cx(q[1],q[2])
qc.cz(q[0],q[2])

qc.measure(q[2],c[0])
job = execute(qc, M_simulator, shots=1024)
result = job.result()
counts = result.get_counts(qc)
print(counts)
print(qc.draw())
print("probabilities of states at Bob's side:\n ")
total_shots = sum(counts.values())
percentages = {outcome: count / total_shots * 100 for outcome, count in counts.items()}
print(percentages)
# Extract the amplitudes for states |0> and |1>
print("Bob's qubit:\n")
prob_0 = math.sqrt(percentages.get('0', 0))/10
prob_1 = math.sqrt(percentages.get('1', 0))/10
output = f"{prob_0:.1f}|0⟩ + {prob_1:.1f}|1⟩"
print(output)

print("clearly it is the qubit Alice teleported")