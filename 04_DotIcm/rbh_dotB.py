import glob, subprocess
from pathlib import Path
res = Path.home() / 'Desktop' / 'proteins_results'
REF = 'WP_011216546.1'

def read_fasta(p):
    d, k = {}, None
    for l in open(p):
        l = l.strip()
        if l.startswith('>'):
            k = l[1:].split()[0]
            d[k] = []
        elif k:
            d[k].append(l)
    return {a: ''.join(b) for a, b in d.items()}

q = read_fasta(res / 'dot_icm_queries.faa')['dotB']
Path('dotB_q.faa').write_text('>dotB\n' + q + '\n')
fmt = '6 sseqid pident length qlen bitscore'
for f in sorted(glob.glob('*.faa')):
    if 'pneumophila' in f:
        continue
    out = subprocess.run(['blastp', '-query', 'dotB_q.faa', '-subject', f, '-max_hsps', '1',
                          '-evalue', '1e-3', '-outfmt', fmt],
                         capture_output=True, text=True).stdout.splitlines()
    if not out:
        print(f, 'no hit')
        continue
    best = max((l.split('\t') for l in out), key=lambda x: float(x[4]))
    Path('tmp_hit.faa').write_text('>hit\n' + read_fasta(f)[best[0]] + '\n')
    back = subprocess.run(['blastp', '-query', 'tmp_hit.faa', '-subject', 'Legionella_pneumophila.faa',
                           '-max_hsps', '1', '-outfmt', fmt],
                          capture_output=True, text=True).stdout.splitlines()
    top = max((l.split('\t') for l in back), key=lambda x: float(x[4]))
    cov = 100 * int(best[2]) / int(best[3])
    print(f, '| identity', best[1], '| coverage %.0f' % cov, '| best match back:', top[0],
          'RECIPROCAL' if top[0] == REF else 'NOT reciprocal')
