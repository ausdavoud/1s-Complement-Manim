#!/usr/bin/env bash
# Renders every scene with Manim Slides, then builds the reveal.js deck.
#
#   ./render.sh                    # -> slides.html (+ slides_assets/)
#   ./render.sh site/slides.html   # what the GitHub Pages build uses
#
# Extra Manim flags can go in MANIM_FLAGS, e.g. MANIM_FLAGS=-ql for a quick low-quality pass.
set -euo pipefail
cd "$(dirname "$0")"

out="${1:-slides.html}"

scenes=(
  001_intro:Intro
  002_example:Example
  003_complement:Complement
  004_add_carry:Carry
  005_graph:Graph
  006_when:When
  007_x_plus_y_graph:XPlusYGraph
  008_x_plus_y_proof:XPlusYProof
  009_x_minus_y_graph:XMinusYGraph
  010_x_minus_y_proof_when:XMinusYProofWhen
  011_x_minus_y_proof_why:XMinusYProofWhy
  012_minus_x_minus_y_graph:MinusXMinusYGraph
  013_minus_x_minus_y_proof:MinusXMinusYProof
)

classes=()
for entry in "${scenes[@]}"; do
  file="${entry%%:*}"
  cls="${entry##*:}"
  # shellcheck disable=SC2086
  manim-slides render ${MANIM_FLAGS:-} "scene/$file.py" "$cls"
  classes+=("$cls")
done

mkdir -p "$(dirname "$out")"
manim-slides convert "${classes[@]}" "$out" \
  -c "title=1's Complement" -ccontrols=true -cprogress=true -chash=true
