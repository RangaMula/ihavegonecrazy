#!/usr/bin/env python3
"""Build data/languages.csv: every target language of the multilingual Muwatta edition.

The language list is the series master list (festive-goodall branch: series-standard/languages/master_languages.csv,
143 languages, vendored as data/master_languages.csv) plus Bengali, the series' home language.
For each language this assigns the pronunciation scheme (engine/scripts.py) and records the production status.

    python3 tools/build_registry.py
"""
import csv, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "engine"))
from scripts import SCHEMES  # noqa: E402

CODES = {
    "Hindi": "hi", "Urdu": "ur", "Nepali": "ne", "Assamese": "as", "Odia": "or", "Punjabi (Gurmukhi)": "pa",
    "Punjabi (Shahmukhi)": "pnb", "Marathi": "mr", "Gujarati": "gu", "Tamil": "ta", "Telugu": "te", "Kannada": "kn",
    "Malayalam": "ml", "Sinhala": "si", "Sanskrit": "sa", "Pashto": "ps", "Sindhi": "sd", "Maithili": "mai",
    "Dhivehi": "dv", "Kashmiri": "ks", "Konkani": "kok", "Santali": "sat", "Meitei (Manipuri)": "mni", "Tibetan": "bo",
    "Dzongkha": "dz", "Arabic (Modern Standard)": "ar", "Gulf Arabic (Khaleeji)": "afb", "Egyptian Arabic": "arz",
    "Levantine Arabic": "apc", "Persian (Farsi/Dari)": "fa", "Turkish": "tr", "Azerbaijani": "az",
    "Kurdish (Kurmanji / Sorani)": "ku", "Hebrew": "he", "Yiddish": "yi", "Armenian": "hy", "Georgian": "ka",
    "Uzbek": "uz", "Kazakh": "kk", "Kyrgyz": "ky", "Tajik": "tg", "Turkmen": "tk", "Uyghur": "ug", "Mongolian": "mn",
    "Mandarin Chinese (Simplified)": "zh-Hans", "Chinese (Traditional) / Cantonese": "zh-Hant", "Japanese": "ja",
    "Korean": "ko", "Malay": "ms", "Indonesian": "id", "Thai": "th", "Vietnamese": "vi", "Filipino (Tagalog)": "fil",
    "Cebuano": "ceb", "Khmer": "km", "Burmese": "my", "Lao": "lo", "Javanese": "jv", "Sundanese": "su", "Tetum": "tet",
    "English": "en", "French": "fr", "Spanish": "es", "Portuguese": "pt", "German": "de", "Italian": "it",
    "Russian": "ru", "Dutch": "nl", "Polish": "pl", "Romanian": "ro", "Greek": "el", "Ukrainian": "uk", "Latin": "la",
    "Esperanto": "eo", "Czech": "cs", "Slovak": "sk", "Hungarian": "hu", "Croatian": "hr", "Serbian": "sr",
    "Bosnian": "bs", "Albanian": "sq", "Slovenian": "sl", "Bulgarian": "bg", "Macedonian": "mk", "Belarusian": "be",
    "Lithuanian": "lt", "Latvian": "lv", "Estonian": "et", "Swedish": "sv", "Norwegian": "no", "Danish": "da",
    "Finnish": "fi", "Icelandic": "is", "Faroese": "fo", "Catalan": "ca", "Galician": "gl", "Basque": "eu",
    "Maltese": "mt", "Irish": "ga", "Welsh": "cy", "Luxembourgish": "lb", "Scottish Gaelic": "gd", "Breton": "br",
    "West Frisian": "fy", "Corsican": "co", "Occitan / Provençal": "oc", "Romansh": "rm", "Alsatian": "gsw",
    "Scots": "sco", "Manx": "gv", "Cornish": "kw", "Swahili": "sw", "Afrikaans": "af", "Amharic": "am", "Somali": "so",
    "Hausa": "ha", "Yoruba": "yo", "Igbo": "ig", "Zulu": "zu", "Xhosa": "xh", "Berber / Tamazight": "zgh",
    "Oromo": "om", "Tigrinya": "ti", "Fula (Fulfulde / Pular)": "ff", "Wolof": "wo", "Malagasy": "mg",
    "Lingala": "ln", "Shona": "sn", "Kinyarwanda": "rw", "Kirundi": "rn", "Luganda": "lg", "Chichewa": "ny",
    "Sesotho": "st", "Setswana": "tn", "Akan (Twi)": "ak", "Haitian Creole": "ht", "Quechua": "qu", "Guarani": "gn",
    "Māori": "mi", "Samoan": "sm", "Fijian": "fj", "Tok Pisin": "tpi", "Hawaiian": "haw",
}

ARABIC_DIALECTS = {"ar", "afb", "arz", "apc"}


def scheme_for(code, script):
    """-> (scheme, status, note)"""
    s = script.lower()
    if code in ARABIC_DIALECTS:
        return ("-", "special", "Arabic readers: vowelled text + Arabic explanation (sharh-lite) instead of a translation")
    if s.startswith("arabic") or code in ("ur", "pnb", "ps", "sd", "ks", "ug", "fa"):
        return ("ar-vowelled", "ready", "reads Arabic script: the fully vowelled Arabic is the pronunciation guide")
    if code == "bn":
        return ("bn", "ready", "books/ar/STYLE.md notation")
    if code == "ja":
        return ("ja", "ready", "katakana, Japanese Islamic-literature conventions")
    if s.startswith("devanagari"):
        return ("hi", "ready" if code == "hi" else "base",
                "Hindi scheme; check local conventions" if code != "hi" else "Hindi-Urdu nukta conventions")
    if s.startswith("latin") or s.startswith("cyrillic / latin"):
        return ("latn", "base", "ALA-LC base; a per-language orthographic profile is recommended")
    if s.startswith("bengali-assamese"):
        return ("as", "todo", "derive from bn: ৰ for r, ৱ for w")
    return (script.split()[0].lower().replace("'", ""), "todo", "renderer to write: " + script)


def main():
    src = os.path.join(ROOT, "data", "master_languages.csv")
    rows = list(csv.DictReader(open(src, encoding="utf-8")))
    out = [{"no": 0, "code": "bn", "en": "Bengali", "bn": "বাংলা", "script": "Bengali", "tier": "A",
            "region": "South Asia", "pron_scheme": "bn", "pron_status": "ready", "pron_note": "books/ar/STYLE.md notation",
            "meaning_status": "pilot: Book 1"}]
    for i, r in enumerate(rows, 1):
        code = CODES[r["en"]]
        sch, st, note = scheme_for(code, r["script"])
        if sch not in SCHEMES and sch not in ("-", "ar-vowelled") and st in ("ready", "base"):
            st = "todo"
        out.append({"no": i, "code": code, "en": r["en"], "bn": r["bn"], "script": r["script"], "tier": r["tier"],
                    "region": r["region"], "pron_scheme": sch, "pron_status": st, "pron_note": note,
                    "meaning_status": "pilot: Book 1" if code == "ja" else "not started"})
    dst = os.path.join(ROOT, "data", "languages.csv")
    with open(dst, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)
    from collections import Counter
    print(len(out), "languages ->", os.path.relpath(dst, ROOT))
    print("pronunciation status:", dict(Counter(o["pron_status"] for o in out)))


if __name__ == "__main__":
    main()
