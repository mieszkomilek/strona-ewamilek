"""Report known usage separately from missing values; never infer billing."""
import json
from pathlib import Path
from collections import defaultdict


def report(data):
    groups = defaultdict(list)
    ids = [d['id'] for d in data['deployments']]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate deployment ID')
    fields = ('input_tokens', 'cached_input_tokens', 'output_tokens',
              'actual_usd', 'estimated_api_usd')
    for deployment in data['deployments']:
        for usage in deployment['usage']:
            for field in fields:
                value = usage.get(field)
                if value is not None and (isinstance(value, bool) or
                                          not isinstance(value, (int, float)) or value < 0):
                    raise ValueError(f'Invalid {field}')
            inp, cached = usage.get('input_tokens'), usage.get('cached_input_tokens')
            if inp is not None and cached is not None and cached > inp:
                raise ValueError('Cached tokens exceed input tokens')
            groups[usage['model']].append(usage)
    print('Wdrożenia w rejestrze:', len(ids))
    print('Sumy dotyczą wpisanego zakresu pracy; brak danych nie oznacza zera.')
    for model, rows in groups.items():
        print('\nModel:', model)
        for field in fields:
            known = [r[field] for r in rows if r.get(field) is not None]
            amount = f'{sum(known):g}' if known else 'brak danych'
            print(f'  {field}: {amount}; braki: {len(rows) - len(known)}/{len(rows)}')


if __name__ == '__main__':
    report(json.loads((Path(__file__).resolve().parents[1] /
                       'tracking/deployments.json').read_text(encoding='utf-8')))
