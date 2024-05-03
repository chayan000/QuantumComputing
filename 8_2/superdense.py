from qiskit import QuantumRegister, QuantumCircuit, Aer, execute
from qiskit import ClassicalRegister
from qiskit.tools.visualization import circuit_drawer

M_simulator = Aer.get_backend('qasm_simulator')
S_simulator = Aer.get_backend('statevector_simulator')

q = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)

# Iterate over all possible messages and perform superdense coding
for msg in ["00", "01", "10", "11"]:
    print("Encoding message:", msg)
    qc = QuantumCircuit(q, c)  
    # maximally entangled state
    qc.h(q[0])
    qc.cx(q[0], q[1])

    #Encode the message
    if msg == "00":
        pass    
    elif msg == "10":
        qc.x(0) 
    elif msg == "01":
        qc.z(0) 
    elif msg == "11":
        qc.z(0) 
        qc.x(0) 
    else:
        print("Invalid Message")
    qc.cx(q[1], q[0])  
    qc.h(q[1])  
    qc.measure(q, c)
    job = execute(qc, M_simulator, shots=1000)
    result = job.result()
    counts = result.get_counts(qc)
    print("result:", counts)
    print(qc.draw())

