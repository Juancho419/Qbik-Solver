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
    
        # Front (F) 
    def move_F(self) -> None:
        """Front face, 90° clockwise (F)."""
        self._rotate_face('B')  # 'B' = blue = Front
        u, r, d, l = self.faces['W'], self.faces['R'], self.faces['Y'], self.faces['O']
        (u[6], u[7], u[8],
         r[0], r[3], r[6],
         d[2], d[1], d[0],
         l[8], l[5], l[2]) = (l[8], l[5], l[2],
                              u[6], u[7], u[8],
                              r[0], r[3], r[6],
                              d[2], d[1], d[0])

    def move_F_prime(self) -> None:
        """Front face, 90° counter-clockwise (F')."""
        for _ in range(3):
            self.move_F()

    def move_F2(self) -> None:
        """Front face, 180° (F2)."""
        for _ in range(2):
            self.move_F()
            
        # ---------- Back (B) ----------
    def move_B(self) -> None:
        """Back face, 90° clockwise (B)."""
        self._rotate_face('G')  # 'G' = green = Back
        r, f, l, b = self.faces['R'], self.faces['B'], self.faces['O'], self.faces['G']
        (r[2], r[5], r[8],
         f[0], f[1], f[2],
         l[0], l[3], l[6],
         b[8], b[7], b[6]) = (l[0], l[3], l[6],
                              r[2], r[5], r[8],
                              b[8], b[7], b[6],
                              f[0], f[1], f[2])

    def move_B_prime(self) -> None:
        """Back face, 90° counter-clockwise (B')."""
        for _ in range(3):
            self.move_B()

    def move_B2(self) -> None:
        """Back face, 180° (B2)."""
        for _ in range(2):
            self.move_B()

    # ---------- Left (L) ----------
    def move_L(self) -> None:
        """Left face, 90° clockwise (L)."""
        self._rotate_face('O')  # 'O' = orange = Left
        u, f, d, b = self.faces['W'], self.faces['B'], self.faces['Y'], self.faces['G']
        (u[0], u[3], u[6],
         f[0], f[3], f[6],
         d[0], d[3], d[6],
         b[8], b[5], b[2]) = (b[8], b[5], b[2],
                              u[0], u[3], u[6],
                              f[0], f[3], f[6],
                              d[0], d[3], d[6])

    def move_L_prime(self) -> None:
        """Left face, 90° counter-clockwise (L')."""
        for _ in range(3):
            self.move_L()

    def move_L2(self) -> None:
        """Left face, 180° (L2)."""
        for _ in range(2):
            self.move_L()
            
        # ---------- Down (D) ----------
    def move_D(self) -> None:
        """Down face, 90° clockwise (D)."""
        self._rotate_face('Y')  # 'Y' = yellow = Down
        r, f, l, b = self.faces['R'], self.faces['B'], self.faces['O'], self.faces['G']
        (r[6], r[7], r[8],
         f[6], f[7], f[8],
         l[6], l[7], l[8],
         b[6], b[7], b[8]) = (b[6], b[7], b[8],
                              r[6], r[7], r[8],
                              f[6], f[7], f[8],
                              l[6], l[7], l[8])

    def move_D_prime(self) -> None:
        """Down face, 90° counter-clockwise (D')."""
        for _ in range(3):
            self.move_D()

    def move_D2(self) -> None:
        """Down face, 180° (D2)."""
        for _ in range(2):
            self.move_D()

            
            
