"""Generate review SVG and PNG barcodes from CSV using pinned Zint."""
import argparse
import csv
import json
import re
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

EXE = 'zint'


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--csv', required=True, help='UTF-8 CSV columns: name,type,data')
    p.add_argument('--out', required=True)
    p.add_argument('--module-mm', type=float, required=True)
    a = p.parse_args()
    out = Path(a.out)
    if out.exists():
        p.error('Output directory exists')
    if not .1 <= a.module_mm <= 2:
        p.error('Module width must be 0.1-2 mm; choose to match job specification')
    rows = list(csv.DictReader(open(a.csv, encoding='utf-8-sig', newline='')))
    if not rows or not {'name', 'type', 'data'} <= rows[0].keys():
        p.error('CSV requires name,type,data and at least one row')
    allowed = {'EAN13': 'EAN13', 'CODE128': 'CODE128', 'QR': 'QRCODE', 'DATAMATRIX': 'DATAMATRIX', 'GS1-128': 'GS1_128'}
    used = set()
    for r in rows:
        name, kind, data = r['name'], r['type'].upper(), r['data']
        if not re.fullmatch(r'[A-Za-z0-9_-]{1,80}', name) or name.lower() in used:
            p.error('Use distinct safe ASCII names')
        used.add(name.lower())
        if kind not in allowed or not data or '\n' in data or '\r' in data:
            p.error('Unsupported type or empty/multiline data')
        if kind == 'EAN13':
            if not re.fullmatch(r'[0-9]{13}', data):
                p.error('EAN13 requires all 13 digits including its verified check digit')
            check = (10 - sum(int(n) * (1 if i % 2 == 0 else 3) for i, n in enumerate(data[:12])) % 10) % 10
            if int(data[-1]) != check:
                p.error('Invalid EAN13 check digit')
    out.mkdir(parents=True)
    results = []
    for r in rows:
        args = [str(EXE), '--barcode=' + allowed[r['type'].upper()], '--data=' + r['data'], '--quietzones', '--compliantheight', '--werror', f'--scalexdimdp={a.module_mm}mm']
        if r['type'].upper() == 'GS1-128':
            args += ['--gs1']
        for suffix in ['svg', 'png']:
            dest = out / (r['name'] + '.' + suffix)
            proc = subprocess.run(args + (['--embedfont'] if suffix == 'svg' else []) + ['--output=' + str(dest)], capture_output=True)
            if proc.returncode or not dest.exists():
                raise RuntimeError(f'Zint failed; partial outputs retained: {r["name"]}: {proc.stderr.decode("utf-8", "replace")}')
            if suffix == 'svg':
                # Zint scales to 12 dots/mm but writes unitless SVG dimensions.
                # Explicit mm + viewBox preserve its geometry at the requested X dimension.
                tree = ET.parse(dest)
                root = tree.getroot()
                width, height = float(root.get('width')), float(root.get('height'))
                root.set('viewBox', f'0 0 {width:g} {height:g}')
                root.set('width', f'{width / 12:.8f}mm')
                root.set('height', f'{height / 12:.8f}mm')
                ET.register_namespace('', 'http://www.w3.org/2000/svg')
                tree.write(dest, encoding='utf-8', xml_declaration=True)
        results.append(dict(r, module_mm=a.module_mm, status='GENERATED_NOT_PHYSICALLY_GRADED'))
    (out / 'manifest.json').write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding='utf-8')
    print(json.dumps(results, ensure_ascii=True))


if __name__ == '__main__':
    main()


