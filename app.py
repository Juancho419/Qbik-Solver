import tkinter as tk
from cube import Cube
from scramble import generate_scramble, apply_algorithm

FACE_COLORS = {
    'W': 'white',
    'Y': 'yellow',
    'R': 'red',
    'O': 'orange',
    'B': 'blue',
    'G': 'green'
}

MOVE_KEYS = ["U", "U'", "U2", "D", "D'", "D2", "L", "L'", "L2",
             "R", "R'", "R2", "F", "F'", "F2", "B", "B'", "B2"]

class CubeApp:
    def __init__(self, root):
        print("CubeApp constructor entered")
        self.root = root
        self.root.title("Qbik Solver")
        self.cube = Cube()

        self.canvas = tk.Canvas(root, width=400, height=300, bg='gray20')
        self.canvas.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        self.buttons = {}
        row, col = 1, 0
        for move in MOVE_KEYS:
            self.buttons[move] = tk.Button(root, text=move, width=4, command=lambda m=move: self.apply_move(m))
            self.buttons[move].grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col >= 6:
                row += 1
                col = 0

        tk.Button(root, text="Scramble", command=self.scramble).grid(row=row+1, column=0, columnspan=3, sticky="we", pady=5)
        tk.Button(root, text="Reset", command=self.reset).grid(row=row+1, column=3, columnspan=3, sticky="we", pady=5)
        tk.Button(root, text="Next Step", command=self.solve_step).grid(row=row+2, column=0, columnspan=6, sticky="we", pady=5)

        
        self.draw_cube()
        self.solve_steps = [
            ["F"],                  # Step 1
            ["U", "R"],             # Step 2
            ["F'", "D"],            # Step 3
            ["L2"],                 # Step 4
            ["B", "B'"],            # Step 5 (demo only)
        ]
        self.step_index = 0

        print("CubeApp constructor finished")
    
    def solve_step(self):
        if self.cube.is_white_cross_solved():
            print("✅ White cross is complete!")
            return

        moves = self.cube.solve_white_cross_step()
        if moves:
            print(f"Applied moves: {moves}")
            self.draw_cube()
        else:
            print("No white edge to fix right now.")


    def apply_move(self, move):
    # Convert move like "U'" to "move_U_prime"
        if "'" in move:
            method_name = f"move_{move[0]}_prime"
        else:
            method_name = f"move_{move}"
        getattr(self.cube, method_name)()
        self.draw_cube()

    def scramble(self):
        alg = generate_scramble()
        apply_algorithm(self.cube, alg)
        self.draw_cube()

    def reset(self):
        self.cube = Cube()
        self.draw_cube()

    def draw_cube(self):
        self.canvas.delete("all")
        size = 30
        faces = self.cube.faces

        def draw_face(face, offset_x, offset_y):
            for i in range(3):
                for j in range(3):
                    color = FACE_COLORS[faces[face][i*3 + j]]
                    x1 = offset_x + j * size
                    y1 = offset_y + i * size
                    x2 = x1 + size
                    y2 = y1 + size
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

        draw_face('W', 3*size, 0)        # Up
        draw_face('O', 0, 3*size)        # Left
        draw_face('B', 3*size, 3*size)   # Front
        draw_face('R', 6*size, 3*size)   # Right
        draw_face('G', 9*size, 3*size)   # Back
        draw_face('Y', 3*size, 6*size)   # Down
        
            # Face labels for user orientation
        self.canvas.create_text(3*size + size * 1.5, size * 0.3,
                                text="Up", fill="black", font=("Arial", 10, "bold"))
        self.canvas.create_text(size * 1.5, 3*size + size * 1.5,
                                text="Left", fill="white", font=("Arial", 10, "bold"))
        self.canvas.create_text(3*size + size * 1.5, 3*size + size * 1.5,
                                text="Front", fill="white", font=("Arial", 10, "bold"))
        self.canvas.create_text(6*size + size * 1.5, 3*size + size * 1.5,
                                text="Right", fill="white", font=("Arial", 10, "bold"))
        self.canvas.create_text(9*size + size * 1.5, 3*size + size * 1.5,
                                text="Back", fill="white", font=("Arial", 10, "bold"))
        self.canvas.create_text(3*size + size * 1.5, 6*size + size * 1.5,
                                text="Down", fill="black", font=("Arial", 10, "bold"))



if __name__ == "__main__":
    print("App starting...")
    root = tk.Tk()
    app = CubeApp(root)
    root.mainloop()