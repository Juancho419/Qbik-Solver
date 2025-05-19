# Qbik-Solver: Development Roadmap

A desktop application that teaches users how to solve a physical 3x3 Rubik's Cube through an interactive visual assistant. This roadmap outlines the planned development milestones and features.

You can copy this file into your project as `ROADMAP.md` and commit it to your GitHub repo.

---

## Phase 1: Core Functionality (✅ Current Focus)

### Goal:

Build the base cube engine and connect it to a graphical interface.

### Tasks:

* [x] Implement Cube logic (`cube.py`) with all 18 standard moves
* [x] Implement scramble generation and move execution (`scramble.py`)
* [x] Terminal-based cube viewer for testing (`viewer.py`)
* [ ] Build basic GUI using `tkinter`

  * [ ] Display cube net as colored grid
  * [ ] Buttons for: U, D, L, R, F, B (including ', 2 versions)
  * [ ] Buttons for Scramble and Reset

---

## Phase 2: Solving Assistant

### Goal:

Guide the user step-by-step through solving a real Rubik's Cube

### Tasks:

* [ ] Implement solving steps (white cross, corners, etc.)
* [ ] Add "Next Step" button to show and apply the next move
* [ ] Display current solving phase and instruction text
* [ ] Highlight affected facelets in the UI

---

## Phase 3: Polish and Release

### Goal:

Make the app usable, shareable, and ready for real users

### Tasks:

* [ ] Add colored theme and modern fonts
* [ ] Add installer (via `pyinstaller`)
* [ ] Error handling and edge cases
* [ ] Optional: Save/load scramble state
* [ ] Optional: Add sound or animation for moves

---

## Stretch Goals (Future Ideas)

* [ ] Add 3D cube visualization (e.g., using OpenGL or Pygame)
* [ ] Export solution steps as PDF
* [ ] Add support for 2x2 or 4x4 cubes
* [ ] Web version using Flask or React
* [ ] Mobile app with touch controls

---

## How to Contribute

1. Fork the repo
2. Clone your fork
3. Create a new branch
4. Commit your changes
5. Open a Pull Request

Let's build a cube-solving coach together! 🎉
