#!/usr/bin/env python3
"""Reproduce the counts in research/02-translation-mapping.md.

    python3 tools/compare.py            # feature counts
    python3 tools/compare.py 3 30 39    # show entries side by side (ar / en / ur / bn)

Downloads the fawazahmed0/hadith-api editions into .cache/ (research use only; these third-party
translations are copyrighted and are never copied into this edition).
"""
import json, os, re, sys, unicodedata, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, ".cache")
URL = "https://raw.githubusercontent.com/fawazahmed0/hadith-api/1/editions/{}-malik.json"
LANGS = ["ara", "eng", "urd", "ben"]

CHECKS = {
    "eng": {"chain kept ('related to me from Malik')": r"related to me from Malik",
            "eulogy translated in full": r"may Allah bless him and grant him peace",
            "parentheses": r"\(", "'wudu'": r"\bwudu\b", "'ghusl'": r"\bghusl\b", "'zakat'": r"\bzakat\b",
            "'sunna'": r"\bsunna\b", "'salat'": r"\bsalat\b", "'Allah'": r"\bAllah\b", "'God'": r"\bGod\b"},
    "urd": {"opens '... سے روایت ہے'": r"سے روایت ہے", "keeps Yahya/Malik chain": r"یحیی|یحییٰ.*مالک",
            "eulogy صلی اللہ علیہ وسلم": r"صلی اللہ علیہ وسلم", "added رضی اللہ": r"رضی اللہ", "added حضرت": r"حضرت",
            "parentheses": r"\(", "یعنی": r"یعنی", "نماز": r"نماز", "کہا مالک نے": r"کہا مالک",
            "ہمارے نزدیک": r"ہمارے نزدیک"},
    "ben": {"opens 'রেওয়ায়ত n'": r"^রেওয়ায়ত", "sadhu 'হইতে বর্ণিত'": r"হইতে বর্ণিত",
            "eulogy সাল্লাল্লাহু": r"সাল্লাল্লাহু", "added (রাঃ)": r"রাঃ", "added (রহঃ)": r"রহঃ", "parentheses": r"\(",
            "অর্থাৎ": r"অর্থাৎ", "নামায": r"নামায", "সালাত": r"সালাত", "মালিক (রহঃ) বলেন": r"মালিক \(রহঃ\) বলেন"},
    "ara": {"eulogy": r"صلى الله عليه وسلم", "qala Malik": r"قَالَ مَالِكٌ",
            "al-amr indana": r"الأَمْرُ (الْمُجْتَمَعُ عَلَيْهِ )?عِنْدَنَا"},
}


def load(lang):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, lang + "-malik.json")
    if not os.path.exists(path):
        with urllib.request.urlopen(URL.format(lang), timeout=180) as r, open(path, "wb") as f:
            f.write(r.read())
    data = json.load(open(path, encoding="utf-8"))
    return {h["hadithnumber"]: unicodedata.normalize("NFC", h["text"]) for h in data["hadiths"]}


def main(argv):
    T = {l: load(l) for l in LANGS}
    if argv:
        for n in map(int, argv):
            print("\n#####", n)
            for l in LANGS:
                print(f"[{l}]", T[l].get(n, ""))
        return
    nums = [n for n, t in T["ara"].items() if t.strip()]
    print("non-empty entries:", {l: sum(1 for n in nums if T[l].get(n, "").strip()) for l in LANGS})
    for l, checks in CHECKS.items():
        print("\n==", l)
        for name, pat in checks.items():
            r = re.compile(pat)
            print(f"  {name}: {sum(1 for n in nums if r.search(T[l].get(n, '')))}")


if __name__ == "__main__":
    main(sys.argv[1:])
