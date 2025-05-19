# viewer.py
from cube import Cube

def show(c: Cube) -> None:
    """Print a simple net of the cube in ASCII."""
    f = c.faces
    def row(face, r): return " ".join(f[face][3*r + i] for i in range(3))
    # Up
    print("      ", row('W', 0))
    print("      ", row('W', 1))
    print("      ", row('W', 2))
    # Middle: Left Front Right Back
    for r in range(3):
        print(row('O', r), row('B', r), row('R', r), row('G', r))
    # Down
    print("      ", row('Y', 0))
    print("      ", row('Y', 1))
    print("      ", row('Y', 2))

if __name__ == "__main__":
    cube = Cube()
    show(cube)
