import multiprocessing as mp
from pathlib import Path
from argparse import ArgumentParser
from khmer_latin_name_transformer import to_khmer, to_khmer_pronounce, to_latin

if __name__ == "__main__":
    parser = ArgumentParser("transform.py", description="Transform Text to Text")
    parser.add_argument(
        "files", nargs="+", type=Path, default=[], help="Path to input file"
    )
    parser.add_argument("-t", "--to", choices=["khmer", "latin", "pro"], required=True)
    parser.add_argument(
        "-j", "--job", type=int, default=mp.cpu_count(), help="Number of processors"
    )
    
    args = parser.parse_args()
    transformers = {
      "khmer": to_khmer,
      "latin": to_latin,
      "pro": to_khmer_pronounce,  
    }  
    with mp.Pool(args.job) as pool:
        for file in args.files:
            with open(file) as infile:
                items = [line.strip() for line in infile]
                for item in pool.imap(transformers[args.to], items):
                    print(item)
