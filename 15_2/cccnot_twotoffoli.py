from qiskit import QuantumRegister,QuantumCircuit,Aer,execute
from qiskit import ClassicalRegister
from qiskit.tools.visualization import circuit_drawer
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
M_simulator = Aer.backends(name='qasm_simulator')[0]
S_simulator = Aer.backends(name='statevector_simulator')[0]

q=QuantumRegister(5)
c=ClassicalRegister(5)


for msg in ["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]:
    qc=QuantumCircuit(q,c)
    print("input: "+msg+"--->"+"\t")
    if(msg[0]=="1" ):
            qc.x(q[0]) 
    if(msg[1]=="1" ):
            qc.x(q[1])   
    if(msg[2]=="1" ):
            qc.x(q[3]) 
    if(msg[3]=="1" ):
            qc.x(q[4])        
    qc.ccx(q[0],q[1],q[2])
    qc.ccx(q[2],q[3],q[4])
    #qc.ccx(q[0],q[1],q[2]) #removing the third toffoli
    qc.barrier()
    
    qc.measure(q,c)
    M=execute(qc,M_simulator,shots=100).result().get_counts(qc)
#print("after ccnot")
    print("output: "+list(M.keys())[0])
    print("\n")
    if(msg=="1101"):
        print(qc.draw())
print("after deleting the last qubit we also get x^y at index2\n")    
    