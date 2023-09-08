from khmer_latin_name_transformer import to_khmer, to_latin, to_khmer_pronounce

assert to_khmer("DARA VISAL") == "តារា វិសាល"
assert to_latin("តារា វិសាល") == "DARA VISAL"
assert to_khmer("linda sokha") == "លីនដា សុខា"
assert to_khmer_pronounce("ភក្ត្រា") == 'ភ័ក-ត្រា'
assert to_khmer_pronounce("ណាចក្រ") == "ណា-ចាក់"
assert to_khmer_pronounce("និន្ទ្រា") == 'និន-ទ្រា'