---
name: packaging-svg-inventory
description: Inspect SVG physical dimension attributes, layers, live text, embedded or linked images and path inventory with installed Inkscape inkex. Use for read-only packaging SVG preparation checks, not geometric dieline certification or automatic path repair.
---

Inspect SVG attributes and objects without editing the input. Open paths may be intentional. Confirm physical dimensions and dieline geometry separately.

Requires Python with inkex available. Run: python svg_audit.py --source demo.svg --out inventory.json

