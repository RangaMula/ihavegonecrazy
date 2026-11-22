#!/usr/bin/env python3
"""Qur'an authentication check (owner's islamic-source-verifier protocol, Qur'an section).

For every verse used in the edition:
  1. reference exists (surah 1-114, ayah <= verse count of the surah, from Tanzil chapters metadata)
  2. Arabic from source #1 quran.com API v4 (text_uthmani)
  3. cross-check against source #2 Tanzil via risan/quran-json 3.1.2 (npm, pinned): letters must match after
     normalisation (NFC, no tatweel, no pause/annotation marks, unified alif forms)
  4. named translations: Saheeh International (quran.com id 20), Bangla Taisirul (161) for the bank,
     and for the books the commercially usable QuranEnc translations (bengali_zakaria, japanese_saeedsato)
  5. every Qur'anic phrase quoted inside a narration is checked to be a substring of the verified verse

Raw responses are kept in sources/quran/ (a pinned local copy counts as the same source).
    python3 tools/verify_quran.py      -> data/verification/quran.json
"""
import io, json, os, re, sys, tarfile, unicodedata, urllib.request
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "sources", "quran")
OUT = os.path.join(ROOT, "data", "verification", "quran.json")

# verse key -> (surah name, phrases quoted in the edition that must belong to the verse, where used)
VERSES = {
    "20:14": ("Ta-Ha", ["أَقِمِ الصَّلاَةَ لِذِكْرِي"], "Book 1, entry 25 (the Prophet quotes it)"),
    "7:205": ("Al-A'raf", ["وَلاَ تَكُنْ مِنَ الْغَافِلِينَ"], "Book 1, entry 8 (wording of 'Umar's letter; note)"),
    "17:78": ("Al-Isra'", ["دُلُوكُ الشَّمْسِ", "غَسَقُ اللَّيْلِ"], "Book 1, entries 19-20 (Ibn 'Umar and Ibn 'Abbas explain these words; notes)"),
    "83:1": ("Al-Mutaffifin", ["لِلْمُطَفِّفِينَ"], "Book 1, entry 22 (note on the word taffafta)"),
}
QURANCOM = "https://api.quran.com/api/v4/verses/by_key/{k}?fields=text_uthmani&translations=20,161,213"
QURANENC_AYA = "https://quranenc.com/api/v1/translation/aya/{key}/{s}/{a}"
QURANENC_KEYS = {"bn": "bengali_zakaria", "ja": "japanese_saeedsato", "en": "english_saheeh"}
TANZIL_NPM = "https://registry.npmjs.org/quran-json/-/quran-json-3.1.2.tgz"


def get(url, cache):
    os.makedirs(os.path.dirname(cache), exist_ok=True)
    if not os.path.exists(cache):
        req = urllib.request.Request(url, headers={"User-Agent": "muwatta-verifier"})
        with urllib.request.urlopen(req, timeout=60) as r, open(cache, "wb") as f:
            f.write(r.read())
    with open(cache, "rb") as f:
        return f.read()


QURANIC_MARKS = re.compile(r"[ؐ-ًؚ-ٟۖ-ۭـ]")


def letters(s):
    """Letter skeleton for comparing Uthmani and standard spellings."""
    s = unicodedata.normalize("NFC", s)
    s = s.replace("وٰ", "ا")            # Uthmani waw-with-dagger for long a (الصلوٰة = الصلاة)
    s = s.replace("ٰ", "ا")        # dagger alif = alif
    s = s.replace("ـٰ", "ا")
    s = QURANIC_MARKS.sub("", s)
    s = re.sub("[ٱأإآ]", "ا", s).replace("ى", "ي").replace("ة", "ه").replace("ۥ", "").replace("ۦ", "")
    s = re.sub("[ؤئ]", "ء", s)
    s = re.sub(r"[^ء-ي ]", "", s)
    s = s.replace("اا", "ا").replace("لل", "ل")   # Uthmani ٱلَّيْل = standard الليل
    return re.sub(r"\s+", " ", s).strip()


def main():
    tgz = get(TANZIL_NPM, os.path.join(SRC, "quran-json-3.1.2.tgz"))
    tf = tarfile.open(fileobj=io.BytesIO(tgz))
    versions = {}
    for lang in ("bengali", "japanese", "english"):
        pass
    # QuranEnc translation metadata (version numbers) for the keys we use
    meta_all = json.loads(get("https://quranenc.com/api/v1/translations/list", os.path.join(SRC, "quranenc-translations-list.json")))
    for t in meta_all.get("translations", []):
        if t.get("key") in QURANENC_KEYS.values():
            versions[t["key"]] = {"version": t.get("version"), "title": t.get("title"), "last_update": t.get("last_update")}
    results = {}
    for key, (surah_name, phrases, used) in VERSES.items():
        s, a = map(int, key.split(":"))
        qc = json.loads(get(QURANCOM.format(k=key), os.path.join(SRC, f"qurancom_{s}_{a}.json")))["verse"]
        chap = json.load(tf.extractfile(f"package/dist/chapters/{s}.json"))
        tz_verses = chap["verses"] if isinstance(chap, dict) else chap
        exists = a <= len(tz_verses)
        tz = next((v for v in tz_verses if int(v.get("id", 0)) == a), None)
        tz_text = tz["text"] if tz else ""
        q_text = qc["text_uthmani"]
        match = letters(q_text) == letters(tz_text)
        tr = {}
        for lang, k in QURANENC_KEYS.items():
            j = json.loads(get(QURANENC_AYA.format(key=k, s=s, a=a), os.path.join(SRC, f"quranenc_{k}_{s}_{a}.json")))["result"]
            tr[lang] = {"key": k, "text": j.get("translation", "").strip(), "footnotes": (j.get("footnotes") or "").strip(),
                        "arabic_matches_qurancom": letters(j.get("arabic_text", "")) == letters(q_text), **versions.get(k, {})}
        qc_tr = {t["resource_id"]: re.sub(r"<[^>]+>", "", t["text"]).strip() for t in qc.get("translations", [])}
        # the Bengali QuranEnc text must equal quran.com's copy of the same translator (resource 213)
        tr["bn"]["matches_qurancom_213"] = re.sub(r"\s+|\[.*?\]", "", qc_tr.get(213, "")) == re.sub(r"\s+|\[.*?\]", "", tr["bn"]["text"])
        phrase_checks = [{"phrase": p, "in_verse": letters(p) in letters(q_text)} for p in phrases]
        status = "VERIFIED" if exists and match and all(c["in_verse"] for c in phrase_checks) else "FAILED"
        results[key] = {
            "surah": surah_name, "reference_exists": exists, "arabic_uthmani": q_text,
            "source": "quran.com API v4 text_uthmani", "cross_check": "Tanzil via risan/quran-json 3.1.2 (npm), letter-skeleton",
            "cross_check_match": match, "phrase_checks": phrase_checks, "used_in": used,
            "en_saheeh_international": qc_tr.get(20), "bn_taisirul": qc_tr.get(161), "quranenc": tr,
            "status": status, "verified_on": date.today().isoformat(),
        }
        print(f"{key:6} {status:9} tanzil={'✓' if match else '✗'} phrases={[c['in_verse'] for c in phrase_checks]}")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump({"versions": versions, "verses": results}, f, ensure_ascii=False, indent=1)
    print("versions:", versions)
    print("->", os.path.relpath(OUT, ROOT))
    if any(v["status"] != "VERIFIED" for v in results.values()):
        sys.exit(1)


if __name__ == "__main__":
    main()
