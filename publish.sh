#!/usr/bin/env bash
# Renders the slides, builds the site and publishes it to the gh-pages branch,
# which GitHub Pages serves at https://ausdavoud.github.io/1s-Complement-Manim/
#
#   uv run ./publish.sh            # render, build, publish
#   SKIP_RENDER=1 uv run ./publish.sh   # publish what's already in site/
#
# Rendered files are named after their content, so unchanged scenes produce identical
# files and only what actually changed gets uploaded.
set -euo pipefail
cd "$(dirname "$0")"

if [[ -z "${SKIP_RENDER:-}" ]]; then
  ./render.sh site/slides.html
  python web/build_site.py
fi

branch=gh-pages
dir=.gh-pages
git worktree remove --force "$dir" 2>/dev/null || true
rm -rf "$dir"

if git fetch -q origin "$branch" 2>/dev/null; then
  git worktree add -q -B "$branch" "$dir" "origin/$branch"
else
  git worktree add -q --orphan -b "$branch" "$dir"
fi

rsync -a --delete --exclude .git site/ "$dir/"
git -C "$dir" add -A
if git -C "$dir" diff --cached --quiet; then
  echo "Nothing changed, nothing to publish."
else
  git -C "$dir" commit -q -m "Publish slides from $(git rev-parse --short HEAD)"
  git -C "$dir" push -q origin "$branch"
  echo "Published. GitHub Pages updates in a minute or two."
fi
git worktree remove "$dir"
