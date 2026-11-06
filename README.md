# DES coursework: ECB and CBC

Undergraduate Cryptography and Information Security coursework by Qiaoyu Wan and Yiwen Wei, as credited in the original report. Individual contributions and the provenance of the custom ECB implementation still need confirmation; this repository does not claim sole authorship or a wholly original implementation.

## Contents

- `src/des_ecb.py`: archived Python DES implementation with key scheduling, permutations, S-boxes, 16 Feistel rounds, encryption and decryption. Uses zero padding.
- `src/des_cbc.py`: a CBC encryption/decryption demonstration built on **pyDes**, with PKCS#5 padding and hexadecimal output. CBC and DES internals here are provided by the library.
- `tests/test_ecb.py`: validation added during repository preparation, not part of the original coursework.

## Run

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 src/des_ecb.py
python3 src/des_cbc.py
python3 -m unittest discover -s tests -v
```

The ECB script and its tests use only the standard library. CBC requires pyDes.

## Limitations and report corrections

This is a historical learning project, **not production cryptography**. The demonstration uses fixed, public example keys and IVs. It provides no authentication. ECB reveals repeated blocks. Zero padding cannot distinguish original trailing zeros from padding; the ECB code also pads/truncates keys rather than validating their lengths. `generateK` is an unimplemented placeholder.

DES has a 64-bit block size and a 56-bit effective key, not 48-bit ciphertext blocks as mistakenly stated in the original report. CBC is deterministic for identical plaintext, key, IV and padding. The archived CBC comparison used different IVs and compared different encodings, so differing output alone is not evidence of greater security. ECB zero padding and PKCS#5 padding also produce different output lengths.

## Archival preparation and attribution

Original source files are preserved separately on the owner's computer. This upload copy removes the unused MySQL integration (including hard-coded local credentials and SQL string interpolation), normalizes filenames and corrects two CBC comments. No database service is needed.

The original folder contains separately labelled reference examples and downloaded `DES-C-master` / `SCU_DES-master` projects. Those are excluded from this upload, as are videos, binaries, ZIP files and reports containing student IDs. The CBC reference README names Futuresea713; the precise upstream URL and licensing remain unconfirmed. No blanket open-source license is asserted for historical source code whose provenance is unresolved.
