"""Prepare non-Gutenberg sources as pre-split 'books' that build.py can use.

- Internet Archive OCR books (public domain): split with ocr_split, credits entered by hand (with death years).
- African Storybook (CC BY 4.0) traditional tales: grouped by country of origin.
Writes meta/<repo>.json (with "presplit") and books/<repo>.tales.json.  Prints the catalog keys created.
"""
import json, os, re, glob, collections
from ocr_split import split_ocr

HERE = os.path.dirname(os.path.abspath(__file__))
META, BOOKS = os.path.join(HERE, "meta"), os.path.join(HERE, "books")

# key: (IA identifier, language of text, title, [(role, name, death)], extra split kwargs)
IA = {
    "ia-tremearne": ("hausasuperstitio00tremuoft", "en", "Hausa Superstitions and Customs (1913)", [("author", "Tremearne, A. J. N.", 1915)], {}),
    "ia-dennett": ("notesonfolkloreo00dennuoft", "en", "Notes on the Folklore of the Fjort (French Congo) (1898)", [("author", "Dennett, R. E.", 1921)], {}),
    "ia-chatelain": ("folktalesofangol00chat", "en", "Folk-Tales of Angola (1894)", [("author", "Chatelain, Héli", 1908)], {}),
    "ia-jacottet": ("treasuryofbasuto01jaco", "en", "The Treasury of Ba-Suto Lore (1908)", [("editor", "Jacottet, Édouard", 1920)], {}),
    "ia-junod": ("leschantsetlesco00juno", "fr", "Les chants et les contes des Ba-Ronga (1897)", [("author", "Junod, Henri-Alexandre", 1934)], {}),
    "ia-basset": ("nouveauxcontesb00bassgoog", "fr", "Nouveaux contes berbères (1897)", [("author", "Basset, René", 1924)], {}),
    "ia-spitta": ("contesarabesmode00spit", "fr", "Contes arabes modernes (1883)", [("translator", "Spitta, Wilhelm", 1883)], {}),
    "ia-ferrand": ("contespopulaires00ferr", "fr", "Contes populaires malgaches (1893)", [("translator", "Ferrand, Gabriel", 1935)], {}),
    "ia-riviere": ("recueildecontes00rivigoog", "fr", "Recueil de contes populaires de la Kabylie du Djurdjura (1882)", [("translator", "Rivière, Joseph", 1883)], {}),
    "ia-schleicher": ("somalitexte00schlgoog", "de", "Somali-Texte (1900)", [("author", "Schleicher, A. W.", 1894), ("editor", "Reinisch, Leo", 1919)], {}),
    "ia-frobenius1": ("atlantisvolksm01frobuoft", "de", "Atlantis, Bd. I: Volksmärchen der Kabylen (1921)", [("author", "Frobenius, Leo", 1938)], {}),
    "ia-frobenius3": ("atlantisvolksm03frobuoft", "de", "Atlantis, Bd. III: Volksmärchen der Kabylen (1921)", [("author", "Frobenius, Leo", 1938)], {}),
    "ia-frobenius6": ("atlantisvolksm06frob", "de", "Atlantis, Bd. VI: Spielmannsgeschichten der Sahel (1921)", [("author", "Frobenius, Leo", 1938)], {}),
    "ia-frobenius8": ("atlantisvolksm08frobuoft", "de", "Atlantis, Bd. VIII: Erzählungen aus dem West-Sudan (1922)", [("author", "Frobenius, Leo", 1938)], {}),
}

DEMONYM = {"mozambic": "Mozambique", "ghana": "Ghana", "kenya": "Kenya", "ugand": "Uganda", "nigeria": "Nigeria",
           "south africa": "South Africa", "southern africa": "Southern Africa (regional)", "ethiopia": "Ethiopia",
           "zambia": "Zambia", "tanzania": "Tanzania", "lesotho": "Lesotho", "malawi": "Malawi", "rwanda": "Rwanda",
           "cameroon": "Cameroon", "somali": "Somalia", "senegal": "Senegal", "zimbabwe": "Zimbabwe", "namibia": "Namibia",
           "botswana": "Botswana", "congo": "DR Congo", "west africa": "West Africa (regional)",
           "east africa": "East Africa (regional)", "benin": "Benin", "sudan": "South Sudan", "angola": "Angola",
           "swazi": "Eswatini", "liberia": "Liberia", "sierra leone": "Sierra Leone", "mali": "Mali", "burundi": "Burundi"}
LANG_COUNTRY = {"Kiswahili": "East Africa (regional)", "isiXhosa": "South Africa", "isiZulu": "South Africa",
                "Afrikaans": "South Africa", "Setswana": "Botswana", "Sesotho (South Africa)": "South Africa",
                "Sepedi": "South Africa", "isiNdebele": "South Africa", "Xitsonga": "South Africa", "Siswati": "Eswatini",
                "Luganda": "Uganda", "Lunyole": "Uganda", "Lumasaaba": "Uganda", "Lugbarati (Official)": "Uganda",
                "Lusoga": "Uganda", "Rutooro": "Uganda", "Oluwanga": "Kenya", "Maa": "Kenya", "Kikamba": "Kenya",
                "Ekegusii": "Kenya", "Amharic": "Ethiopia", "Anii": "Benin", "Xitswa": "Mozambique",
                "Hausa (Nigeria)": "Nigeria", "Kinyarwanda": "Rwanda", "Fulfulde Mbororoore": "Cameroon",
                "Somali": "Somalia", "Tiv": "Nigeria", "Twi": "Ghana", "Asante Twi": "Ghana", "ChiChewa": "Malawi",
                "CiNyanja": "Zambia", "IciBemba": "Zambia", "ChiTonga": "Zambia", "Portuguese": "Mozambique"}


def write(repo, meta, tales):
    meta["presplit"] = True
    json.dump(meta, open(os.path.join(META, repo + ".json"), "w"), ensure_ascii=False)
    json.dump(tales, open(os.path.join(BOOKS, repo + ".tales.json"), "w"), ensure_ascii=False)


def prep_ia():
    out = {}
    for key, (ident, lang, title, people, kw) in IA.items():
        tales = split_ocr(os.path.join(HERE, "ia", ident + ".txt"), lang, **kw)
        creator, contrib = {}, {}
        for role, name, death in people:
            (creator if role == "author" else contrib).setdefault(role, []).append({"agent_name": name, "deathdate": death})
        meta = {"title": title, "language": lang, "creator": creator, "contributor": contrib,
                "source_line": f"Internet Archive item `{ident}` — https://archive.org/details/{ident} (OCR text, lightly cleaned)"}
        for t in tales:
            t["note"] = "Digitised by OCR; minor recognition errors may remain."
        write(f"IA-{ident}_{key}", meta, tales)
        out[key] = len(tales)
    return out


def fix_mojibake(s):
    if not re.search(r"[ÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑâ][\x80-\xbf\u0152-\u2122\u02c6\u02dc]|â€", s):
        return s
    for enc in ("cp1252", "latin-1"):
        try:
            return s.encode(enc).decode("utf-8")
        except Exception:
            continue
    # mixed: fix piecewise
    return re.sub(r"(?:[ÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑâ][\x80-\xbf\u0152-\u2122\u02c6\u02dc]{1,2})+", lambda m: _fx(m.group(0)), s)


def _fx(x):
    for enc in ("cp1252", "latin-1"):
        try:
            return x.encode(enc).decode("utf-8")
        except Exception:
            pass
    return x


def prep_asb():
    groups = collections.defaultdict(list)
    for f in sorted(glob.glob(os.path.join(HERE, "asb", "*.json"))):
        s = json.load(open(f))
        if not s["pages"] or "Non Commercial" in s["license"] or "NonCommercial" in s["license"]:
            continue
        import html as H
        lang = fix_mojibake(H.unescape(s["language"]))
        people = s["people"]
        country = None
        for k, v in DEMONYM.items():
            if re.search(k, people + " " + s["summary"], re.I):
                country = v
                break
        country = country or LANG_COUNTRY.get(lang, "Africa (regional, origin not stated)")
        body = "\n\n".join(fix_mojibake(p.replace("\\'", "'")) for p in s["pages"])
        title = fix_mojibake(s["title"].replace("\\'", "'"))
        credit = fix_mojibake(re.sub(r"\s{2,}", "; ", people.replace("\\'", "'").strip()))
        groups[country].append({
            "title": title, "text": body,
            "credit": f"{credit} (story, illustration and translation credits as listed by African Storybook)",
            "language": lang,
            "source": f"African Storybook story #{s['id']} — https://www.africanstorybook.org/ (search the title)",
            "license_text": "Creative Commons Attribution 4.0 (CC BY 4.0). Free to copy, translate and adapt for any purpose, "
                            "including commercial, as long as you credit the original author(s), illustrator(s) and African Storybook "
                            "and link to the licence: https://creativecommons.org/licenses/by/4.0/",
            "status": "ccby",
        })
    out = {}
    for country, tales in groups.items():
        key = "asb-" + re.sub(r"[^a-z]+", "-", country.lower()).strip("-")
        meta = {"title": "African Storybook — traditional tales retold (CC BY 4.0)", "language": "various",
                "creator": {}, "contributor": {}, "license": "ccby",
                "source_line": "African Storybook (Saide), https://www.africanstorybook.org/"}
        write(f"ASB-{key}_{key}", meta, tales)
        out[key] = (country, len(tales))
    return out


if __name__ == "__main__":
    print(json.dumps(prep_ia(), indent=1))
    print(json.dumps(prep_asb(), indent=1, ensure_ascii=False))
