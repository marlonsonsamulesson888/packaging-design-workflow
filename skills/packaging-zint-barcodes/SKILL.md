---
name: packaging-zint-barcodes
description: Generate batch packaging barcode SVGs with explicit millimetre dimensions using installed Zint, including EAN13, Code128, QR, Data Matrix and GS1-128. Use for multi-SKU barcode assets; not GTIN allocation or printed barcode grading.
---

Create SVG and review PNG files from UTF-8 CSV. Use verified product data for production. Test artwork digitally and verify printed barcodes independently.

Requires Python and Zint 2.16.0 on PATH. Run: python zint_batch.py --csv demo.csv --module-mm 0.33 --out demo-output

