"""Read-only SVG dimensions, layer, text, image and open-path inventory."""
import argparse
import json
from pathlib import Path
import inkex


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source', required=True)
    p.add_argument('--out', required=True)
    a = p.parse_args()
    out = Path(a.out)
    if out.exists():
        p.error('Report already exists')
    root = inkex.load_svg(a.source).getroot()
    tags = lambda name: root.xpath('//svg:' + name)
    images = tags('image')
    def href(e):
        return e.get('href') or e.get(inkex.addNS('href', 'xlink')) or ''
    layers = root.xpath('//svg:g[@inkscape:groupmode="layer"]')
    paths = tags('path')
    report = dict(source=str(Path(a.source).resolve()), width=root.get('width'), height=root.get('height'), viewBox=root.get('viewBox'), layers=[dict(id=e.get('id'), label=e.get(inkex.addNS('label', 'inkscape')), style=e.get('style')) for e in layers], text_count=len(tags('text')), image_count=len(images), external_images=[e.get('id') for e in images if not href(e).startswith('data:')], path_count=len(paths), paths_with_no_close_command=[e.get('id') for e in paths if 'z' not in (e.get('d') or '').lower()], status='INVENTORY_ONLY_NOT_DIELINE_OR_PREPRESS_CERTIFICATION')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(report, ensure_ascii=True))


if __name__ == '__main__':
    main()


