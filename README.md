# Khmer Latin Name Transformer

Transform **Khmer Personal Name** into Latin and vice-versa.

[[Google Colab]](https://colab.research.google.com/drive/17r-9ubY_oGWfQMaaH2xFPPS8DKe1fsvi?usp=sharing)

**Important!**

Make sure you have `pynini` installed on your current environment before install this library. To install `pynini`, use this

```shell
conda install -c conda-forge pynini
```

Install khmer_latin_name_transformer from PyPI

```shell
pip install khmer-latin-name-transformer
```

## Usage

```python
from khmer_latin_name_transformer import (
  to_khmer,
  to_khmer_pronounce,
  to_latin
)

to_khmer("DARA VISAL")
# => "តារា វិសាល"

to_khmer("linda sokha")
# => "លីនដា សុខា"

to_latin("តារា វិសាល")
# => "DARA VISAL"

to_khmer_pronounce("ភក្ត្រា")
# => ភ័ក-ត្រា

to_khmer_pronounce("និន្ទ្រា")
# => និន-ទ្រា
```

## License

`Apache 2.0`
