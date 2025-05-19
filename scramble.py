# scramble.py
import random
from cube import Cube
import viewer

# Map notation to the corresponding Cube method
MOVE_FUNCS = {
    "R":  Cube.move_R,
    "R'": Cube.move_R_prime,
    "R2": Cube.move_R2,
    "U":  Cube.move_U,
    "U'": Cube.move_U_prime,
    "U2": Cube.move_U2,
    "F":  Cube.move_F,
    "F'": Cube.move_F_prime,
    "F2": Cube.move_F2,
    "L":  Cube.move_L,
    "L'": Cube.move_L_prime,
    "L2": Cube.move_L2,
    "B":  Cube.move_B,          
    "B'": Cube.move_B_prime,   
    "B2": Cube.move_B2,
}

def apply_algorithm(cube: Cube, alg: str) -> None:
# apply a space separated move sequence to the cube
    for move in alg.split():
        MOVE_FUNCS[move](cube)
        
def generate_scramble(length: int = 20) -> str:
    # Return a random scramble using the available moves
    return " ".join(random.choice(list(MOVE_FUNCS)) for _ in range(length))

if __name__ == "__main__":
    scramble = generate_scramble()
    print("Scramble:", scramble)
    
    c = Cube()
    print("Solved satate:")
    viewer.show(c)
    print()
    
    apply_algorithm(c, scramble)
    print("After scramble: ")
    viewer.show(c)
    print("\nCube scrambled! (visual check by printing faces):")
    print(c.faces)

    