# Generates the table for sitelen pona input.
# Sources from the AHK script on the SP UCSUR guide.

from pathlib import Path
import urllib.request as url
import re
import io

SOURCE_URL = r"https://raw.githubusercontent.com/neroist/sitelen-pona-ucsur-guide/refs/heads/main/sitelen-pona-input.ahk"
OUTPUT_FILE = Path(__file__).parent / "src" / "sitelen-pona.txt"
AHK_ROW_RE = re.compile(r"::(.+?)::\{(.+?)\}")

AHK_ESCAPE_RE = re.compile(r"`(.)")
AHK_ESCAPE_TABLE = {
    "n": "\n",
    "r": "\r",
    "b": "\b",
    "t": "\t",
    "v": "\v",
    "a": "\a",
    "f": "\f",
}

def process_escape(m: re.Match):
    c = m.group(1)
    x = AHK_ESCAPE_TABLE.get(c, c)
    return x

key_code = set()
max_len = 0
data_lines = []

with io.TextIOWrapper(url.urlopen(SOURCE_URL), encoding="utf-8") as dfile:
    for item_raw in dfile:
        item = item_raw[:-2].rsplit(";", 1)[0].strip()
        if not item or item[0] != ":":
            continue
        word, codepoint = AHK_ROW_RE.fullmatch(item).groups()
        word = re.sub(AHK_ESCAPE_RE, process_escape, word)
        key_code.update(word)
        max_len = max(len(word), max_len)



        char = chr(int(codepoint[2:], 16))
        print(f"nimi {word} li {char}")
        data_lines.append(f"{word} {char}\n")

print(f"mi kama jo e ijo {len(data_lines)}")

with open(OUTPUT_FILE, "w") as ofile:
    kc_list = list(key_code)
    kc_list.sort()
    kc_str = "".join(kc_list)

    ofile.write(f"""\
KeyCode={kc_str}
Length={max_len}
[Data]
""")
    for line in data_lines:
        ofile.write(line)
    ofile.flush()

print("lipu li lon!")