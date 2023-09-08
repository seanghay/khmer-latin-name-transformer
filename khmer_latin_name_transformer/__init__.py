import os
import pynini
import re

from pynini.lib import rewrite

current_dir = os.path.dirname(__file__)
km_latin_names_fst = pynini.Fst.read(os.path.join(current_dir, "km_latin_names.fst"))
latin_km_names_fst = pynini.Fst.read(os.path.join(current_dir, "latin_km_names.fst"))
km_pronounce_fst = pynini.Fst.read(os.path.join(current_dir, "km_pronounce.fst"))

NON_KHMER_REPLACER = re.compile(r"[^\u1780-\u17ff ]+")
NON_LATIN_REPLACER = re.compile(r"[^A-Z ]+")

def to_khmer_pronounce(text):
    return rewrite.top_rewrite(
        NON_KHMER_REPLACER.sub("", text).strip(),
        rule=km_pronounce_fst,
        input_token_type="utf8",
        output_token_type="utf8",
    )


def to_khmer(text):
    return rewrite.top_rewrite(
        NON_LATIN_REPLACER.sub("", text.upper()).strip(),
        rule=latin_km_names_fst,
        input_token_type="utf8",
        output_token_type="utf8",
    )


def to_latin(text):
    return rewrite.top_rewrite(
        NON_KHMER_REPLACER.sub("", text).strip(),
        rule=km_latin_names_fst,
        input_token_type="utf8",
        output_token_type="utf8",
    )
