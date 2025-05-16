# quick_test.py
from cube import Cube

c = Cube()

# four right turns should restore the cube after another four
for _ in range(4):
    c.move_R()
assert c.faces == Cube().faces, "R rotation failed"

# four up turns should do the same
for _ in range(4):
    c.move_U()
assert c.faces == Cube().faces, "U rotation failed"

print("All basic tests passed!")
