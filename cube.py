class Cube:
    """Representa el cubo de 3x3x3 en estado y movimientos básicos"""
    def __init__(self):
    # Faces: U, R, F, D, L, B : up, right, front, down, left, back
        colors = ['W', 'R', 'B', 'Y', 'O', 'G']
    # Face by list of 9 stickers
        self.faces = {c: [c] * 9 for c in colors} 
                
    # Face int rotation 90°
    def _rotate_face(self, face: str, clockwise: bool = True) -> None:
        idx = [6,3,0,7,4,1,8,5,2] if clockwise else [2,5,8,1,4,7,0,3,6]
        self.faces[face] = [self.faces[face][i] for i in idx]
        
    #  hourly rotation
    def move_R(self) -> None:
        self._rotate_face('R')
        u, f, d, b =self.faces['W'], self.faces['B'], self.faces['Y'], self.faces['G']
        (u[2], u[5], u[8],
         f[2], f[5], f[8],
         d[2], d[5], d[8],
         b[2], b[5], b[8]) = (f[2], f[5], f[8],
                              d[2], d[5], d[8], 
                              b[2], b[5], b[8], 
                              u[2], u[5], u[8])
        
    def move_R_prime(self) -> None:
        for _ in range(3):
            self.move_R()
    
    def move_R2(self) -> None:
    # Right face, 180° (R2)
        for _ in range(2):
            self.move_R()

    # Up (U) face, 90° clockwise (U)
    def move_U(self) ->None:
        self._rotate_face('W') # white
        r, f, l, b = self.faces['R'], self.faces['B'], self.faces['O'], self.faces['G']
        (r[0], r[1], r[2],
         f[0], f[1], f[2],
         l[0], l[1], l[2],
         b[0], b[1], b[2]) = (f[0], f[1], f[2],
                              l[0], l[1], l[2],
                              b[0], b[1], b[2],
                              r[0], r[1], r[2])
         
    def move_U_prime(self) -> None:
        # Up face, 90° counter-clockwise ('U')
        for _ in range(3):
            self.move_U()
            
    def move_U2(self) -> None:
        #  Up dace, 180° (U2)
        for _ in range(2):
            self.move_U()
            
            
