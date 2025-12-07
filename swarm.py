import tkinter as tk
import pennylane as qml
import numpy as np
import math
import time
import random

# --- CONFIGURATION ---
NUM_DRONES = 4       # Qubits
SPEED = 3.0          # Movement speed
ENTANGLEMENT = 1.0   # Hive Mind strength
TARGET_SENSITIVITY = 1.5

# --- 1. THE QUANTUM BRAIN ---
dev = qml.device("default.qubit", wires=NUM_DRONES)

@qml.qnode(dev)
def swarm_brain(inputs, weights):
    # Encoding
    for i in range(NUM_DRONES):
        qml.RY(inputs[i], wires=i)
        qml.RZ(inputs[i], wires=i)
    
    # Entanglement (Ring Topology)
    for i in range(NUM_DRONES):
        qml.CNOT(wires=[i, (i + 1) % NUM_DRONES])
        qml.RX(weights[i], wires=i) 

    # Measurement
    return [qml.expval(qml.PauliZ(i)) for i in range(NUM_DRONES)], \
           [qml.expval(qml.PauliY(i)) for i in range(NUM_DRONES)]

# --- 2. DRONE CLASS ---
class Drone:
    def __init__(self, canvas, idx, color):
        self.canvas = canvas
        self.idx = idx
        self.x = np.random.randint(100, 700)
        self.y = np.random.randint(100, 500)
        self.color = color
        self.id = canvas.create_oval(self.x-6, self.y-6, self.x+6, self.y+6, fill=color, outline="white", width=2)
        self.text = canvas.create_text(self.x, self.y-15, text=f"Q{idx}", fill="white", font=("Courier", 8))
        self.trail = []

    def update(self, dx, dy):
        self.x += dx * SPEED
        self.y += dy * SPEED
        self.canvas.coords(self.id, self.x-6, self.y-6, self.x+6, self.y+6)
        self.canvas.coords(self.text, self.x, self.y-15)
        
        self.trail.append(self.canvas.create_oval(self.x, self.y, self.x+1, self.y+1, fill=self.color, outline=""))
        if len(self.trail) > 20:
            self.canvas.delete(self.trail.pop(0))

# --- 3. THE HUD APPLICATION ---
class SwarmOps:
    def __init__(self, root):
        self.root = root
        self.root.title("QUANTUM SWARM COMMANDER")
        self.root.geometry("1000x700")
        self.root.configure(bg="black")
        
        self.frame_top = tk.Frame(root, bg="#111", height=50)
        self.frame_top.pack(fill="x")
        
        self.lbl_status = tk.Label(self.frame_top, text="SYSTEM: ONLINE  |  ENTANGLEMENT: ACTIVE  |  MODE: TARGET ACQUISITION", 
                                   fg="#00ffcc", bg="#111", font=("Consolas", 10))
        self.lbl_status.pack(pady=15)

        self.canvas = tk.Canvas(root, bg="#050505", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.draw_grid()

        self.target_x = 500
        self.target_y = 350
        self.target_id = self.canvas.create_oval(490, 340, 510, 360, outline="#ff0055", width=2)
        self.canvas.bind("<Motion>", self.update_target)

        colors = ["#00ccff", "#00ff99", "#ffcc00", "#ff0055", "#cc00ff"]
        self.drones = [Drone(self.canvas, i, colors[i % len(colors)]) for i in range(NUM_DRONES)]
        self.q_weights = np.random.uniform(0, np.pi, NUM_DRONES)

        self.animate()

    def draw_grid(self):
        w, h = 1000, 700
        for i in range(0, w, 50): self.canvas.create_line(i, 0, i, h, fill="#111")
        for i in range(0, h, 50): self.canvas.create_line(0, i, w, i, fill="#111")

    def update_target(self, event):
        self.target_x = event.x
        self.target_y = event.y
        self.canvas.coords(self.target_id, event.x-10, event.y-10, event.x+10, event.y+10)

    def animate(self):
        angles = []
        for d in self.drones:
            dx = self.target_x - d.x
            dy = self.target_y - d.y
            dist = math.sqrt(dx*dx + dy*dy)
            if dist == 0: dist = 0.001
            angles.append(math.atan2(dy, dx))

        move_x, move_y = swarm_brain(np.array(angles), self.q_weights)

        for i, d in enumerate(self.drones):
            q_dx = move_x[i]
            q_dy = move_y[i]
            c_dx = (self.target_x - d.x) / 100
            c_dy = (self.target_y - d.y) / 100
            
            final_dx = (q_dx * ENTANGLEMENT) + (c_dx * TARGET_SENSITIVITY)
            final_dy = (q_dy * ENTANGLEMENT) + (c_dy * TARGET_SENSITIVITY)
            d.update(final_dx, final_dy)

        self.root.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    app = SwarmOps(root)
    root.mainloop()
