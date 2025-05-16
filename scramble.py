# scramble.py
import random
from cube import Cube

# Map notation to the corresponding Cube method
MOVE_FUNCS = {
    "R":  Cube.move_R,
    "R'": Cube.move_R_prime,
    "R2": Cube.move_R2,
    "U":  Cube.move_U,
    "U'": Cube.move_U_prime,
    "U2": Cube.move_U2,
}

def apply_algorithm(cube: Cube, alg: str) -> None:
# aplly a space separated move sequence to the cube
    for move in alg.split():
        MOVE_FUNCS[move](cube)
        
def generate_scramble(length: int = 20) -> str:
    # Return a random scramble using the available moves
    return " ".join(random.choice(list(MOVE_FUNCS)) for _ in range(length))

if __name__ == "__main__":
    scramble = generate_scramble()
    print("Scramble:", scramble)
    
    c = Cube()
    apply_algorithm(c, scramble)
    print("Cube scrambled! (visual check by printing faces);")
    print(c.faces)

    