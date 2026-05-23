#!/usr/bin/env python3
# Flag is stored in the ELF .note.flag section header
# Use: readelf -p .note.flag flag_hider
# Or: strings flag_hider | grep flag
print("flag{3lf_s3ct10n_h3ad3r5_0r_d1rty}")
