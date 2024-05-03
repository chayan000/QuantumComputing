
from qiskit import QuantumCircuit, Aer, transpile
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import MCMT
from qiskit.circuit.library.standard_gates import ZGate
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def phase_inversion(marked_states):
    if not isinstance(marked_states, list):
        marked_states = [marked_states]
    num_qubits = len(marked_states[0])
    qc = QuantumCircuit(num_qubits)
    for target in marked_states:
        rev_target = target[::-1]
        zero_inds = [ind for ind in range(num_qubits) if rev_target.startswith("0", ind)]
        if(len(zero_inds)>0):
            qc.x(zero_inds)
        #multi-controlled Z gate (an phase_inversion) onto the quantum circuit. 
        #This gate flips the phase of the state if all control qubits are in the state |1⟩        
        qc.compose(MCMT(ZGate(), num_qubits - 1, 1), inplace=True) 
        if(len(zero_inds)>0):
            qc.x(zero_inds)
    return qc

# Define the invrsion_around_the_mean circuit
def inversion_around_the_mean():
    qc = QuantumCircuit(3)
    qc.h([0, 1, 2])
    qc.x([0, 1, 2])
    qc.h(2)
    qc.ccx(0, 1, 2)
    qc.h(2)
    qc.x([0, 1, 2])
    qc.h([0, 1, 2])
    return qc

def grover_circuit(marked_states):
    phase_inversion_var = phase_inversion(marked_states)
    inversion_around_the_mean_var = inversion_around_the_mean()
    qc = QuantumCircuit(3, 3)
    qc.h([0, 1, 2])
    qc.barrier()
    qc.compose(phase_inversion_var, qubits=[0, 1, 2], inplace=True)
    qc.barrier()
    qc.compose(inversion_around_the_mean_var, qubits=[0, 1, 2], inplace=True)
    qc.compose(phase_inversion_var, qubits=[0, 1, 2], inplace=True)
    qc.barrier()
    qc.compose(inversion_around_the_mean_var, qubits=[0, 1, 2], inplace=True)
    qc.measure([0, 1, 2], [0, 1, 2])
    return qc


marked_states = input("enter the state you want to search(eg. 000,101,111 etc)\t")


qc = grover_circuit(marked_states)
simulator = Aer.get_backend('qasm_simulator')
transpiled_qc = transpile(qc, simulator)
result = simulator.run(transpiled_qc).result()
counts = result.get_counts(qc)
print(qc.draw())
print(counts)
plot_histogram(counts)
plt.show()