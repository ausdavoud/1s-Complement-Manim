#!/bin/zsh
manim-slides render scene/001_intro.py
manim-slides render scene/002_example.py
manim-slides render scene/003_complement.py
manim-slides render scene/004_add_carry.py
manim-slides render scene/005_graph.py
manim-slides render scene/006_when.py
manim-slides render scene/007_x_plus_y_graph.py
manim-slides render scene/008_x_plus_y_proof.py
manim-slides render scene/009_x_minus_y_graph.py
manim-slides render scene/010_x_minus_y_proof_when.py
manim-slides render scene/011_x_minus_y_proof_why.py
manim-slides render scene/012_minus_x_minus_y_graph.py
manim-slides render scene/013_minus_x_minus_y_proof.py

manim-slides convert Intro Example Complement Carry Graph When XPlusYGraph XPlusYProof XMinusYGraph XMinusYProofWhen XMinusYProofWhy MinusXMinusYGraph MinusXMinusYProof 
