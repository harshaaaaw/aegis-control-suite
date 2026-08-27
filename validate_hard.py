from kw import KEYWORDS
import re, unicodedata

spec = open(r"C:\Users\Harsh\job-hunt-2026\TEN_PRODUCTS.md", encoding="utf-8").read()
spec_l = spec.lower()

def covered(kw):
    # normalize: strip parenthetical qualifiers for fuzzy match, but keep core
    k = kw.lower()
    # direct substring
    if k in spec_l:
        return True
    # try core token (text before '(' )
    core = re.split(r"[\(/]", k)[0].strip()
    if core and core in spec_l:
        return True
    # try key token for multiword
    toks = re.findall(r"[a-z0-9]+", k)
    # require most distinctive token present
    if "mlflow" in toks and "mlflow" in spec_l: return True
    return False

miss = [k for k in KEYWORDS if not covered(k)]
hit = [k for k in KEYWORDS if covered(k)]
print(f"TOTAL keywords: {len(KEYWORDS)}")
print(f"COVERED: {len(hit)}  ({100*len(hit)/len(KEYWORDS):.1f}%)")
print(f"UNCOVERED: {len(miss)}  ({100*len(miss)/len(KEYWORDS):.1f}%)")
print("\n--- UNCOVERED (not in any bucket spec text) ---")
for m in miss:
    print(" -", m)
