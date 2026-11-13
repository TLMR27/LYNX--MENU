"""Χτίζει το wine/index.html από το data/wines.json (πηγή των τιμών)."""
import json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((root/'data/wines.json').read_text(encoding='utf-8'))
tpl = (root/'tools/wine_template.html').read_text(encoding='utf-8')
(root/'wine/index.html').write_text(tpl.replace('__DATA__', json.dumps(data, ensure_ascii=False)), encoding='utf-8')
print(f'OK: {len(data)} κρασιά')
