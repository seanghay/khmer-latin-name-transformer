from khmer_latin_name_transformer import to_khmer, to_latin

assert to_khmer("DARA VISAL") == "តារា វិសាល"
assert to_latin("តារា វិសាល") == "DARA VISAL"
assert to_khmer("linda sokha") == "លីនដា សុខា"