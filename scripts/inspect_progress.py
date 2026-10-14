import sys
import os
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

for name in ['gen_item_bank_g1_g2.py', 'gen_item_bank_g3_g4.py']:
    path = os.path.join('courseware', 'scripts', name)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        exp_matches = re.findall(r"build_expository_slot\s*\(\s*grade_num=(\d+),\s*subskill_code=['\"]([^'\"]+)['\"]", content)
        com_matches = re.findall(r"build_common_slot\s*\(\s*grade_num=(\d+),\s*com_code_suffix=['\"]([^'\"]+)['\"]", content)
        print(f"[{name}]")
        print(f"  Expository slots ({len(exp_matches)}): {exp_matches}")
        print(f"  Common slots ({len(com_matches)}): {com_matches}")
