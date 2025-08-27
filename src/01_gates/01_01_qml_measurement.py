import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt

# Device: 1 qubit simulator with samples
dev = qml.device("default.qubit", wires=1, shots=102400)

# Define the circuit
@qml.qnode(dev)
def hadamard_measure():
    qml.Hadamard(wires=0)
    return qml.sample(qml.PauliZ(0))  # computational basis measurement

# Run circuit
samples = hadamard_measure()

# Convert samples (±1 from PauliZ) into bits (0/1)
bits = (1 - samples) // 2

# Count results
unique, counts = np.unique(bits, return_counts=True)
result_counts = dict(zip(unique.astype(str), counts))
print(result_counts)

# --- Draw the circuit ---
qml.draw_mpl(hadamard_measure)()
plt.show()

# --- Plot histogram ---
plt.bar(result_counts.keys(), result_counts.values(), color="skyblue", edgecolor="black")
plt.xlabel("Measurement outcome")
plt.ylabel("Counts")
plt.title("Hadamard on |0> → measurement results")
plt.show()
