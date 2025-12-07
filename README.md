# Quantum-Swarm: Hybrid VQC Control System

![Language](https://img.shields.io/badge/language-Python%20%7C%20C%2B%2B-blue.svg) ![Quantum Backend](https://img.shields.io/badge/backend-Qiskit-purple.svg) ![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📖 Abstract
**Quantum-Swarm** is a hybrid quantum-classical robotics controller that utilizes **Variational Quantum Circuits (VQC)** to pilot autonomous drone swarms. 

Unlike deterministic PID controllers, this system leverages quantum entanglement to simulate "hive-mind" consensus. By encoding physical drone coordinates into a high-dimensional Hilbert space, the swarm utilizes quantum measurement collapse to escape local minima and avoid deadlocks in complex pathfinding scenarios.

---

## 🔬 The "Swarm Ansatz" (Visual Proof)
The core logic is not a random number generator; it is a **Ring-Entangled Variational Circuit**.

![Quantum Circuit Topology](circuit_topology.png)
*Figure 1: Generated circuit topology from the Quantum-Swarm codebase.*

### Topology Breakdown
* **Initialization ($H$):** Hadamard gates place the control qubits into superposition, allowing the drone to evaluate multiple flight vectors simultaneously.
* **Angle Encoding ($R_y, R_z$):** Real-time telemetry (velocity/position) is mapped to rotation angles $\theta$ on the Bloch sphere.
* **Ring Entanglement (CNOT):** A cyclic entanglement strategy ($q_0 \to q_1 \to q_2 \to q_3 \to q_0$) forces neighbor-consensus. The state of the last qubit physically affects the probability amplitude of the first, mimicking a biological swarm neural network.

---

## 🚀 Key Technical Differentiators

### 1. Hybrid Architecture (Python + C++)
To solve the "Quantum Latency" problem, the system is split into two layers:
* **The Physics Engine (C++):** Handles Newtonian mechanics, gravity, and collision detection at high speed.
* **The Quantum Brain (Python):** Interfaces with the QPU/Simulator to perform the decision-making inference step.

### 2. Stochastic Optimization
Classical swarms often get stuck in deadlock loops (A waits for B, B waits for A). The probabilistic nature of the quantum measurement introduces **controlled stochasticity** (noise). This acts as a natural annealing process, allowing the swarm to "jitter" out of mathematical deadlocks.

---

## 🛠️ Installation & Usage

### Prerequisites
* Python 3.10+
* C++ Compiler (GCC/Clang)
* Qiskit & Matplotlib

### Setup
1.  **Clone the repository**
    ```bash
    git clone [https://github.com/samfrazerdutton/Quantum-Swarm.git](https://github.com/samfrazerdutton/Quantum-Swarm.git)
    cd Quantum-Swarm
    ```

2.  **Install Python Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Simulation**
    ```bash
    python swarm.py
    ```

4.  **Verify Circuit Topology**
    To generate the visual proof of the quantum logic yourself:
    ```bash
    python generate_proof.py
    ```

---

## 🤝 Contributing
This project is open-source. I am particularly interested in PRs that explore:
* Different entanglement topologies (e.g., Linear vs. Full).
* Integration with real hardware (IBM Quantum Experience).

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

## 📧 Contact
**Sam Frazer-Dutton** [GitHub Profile](https://github.com/samfrazerdutton)
