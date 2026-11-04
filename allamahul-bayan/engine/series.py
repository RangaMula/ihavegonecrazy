# -*- coding: utf-8 -*-
"""Things shared by every book of the Allamahul Bayan Series."""

SERIES = {
    "name": "Allamahul Bayan Series",
    "ar": "عَلَّمَهُ الْبَيَانَ",
    "author": "Hafez Abdullah Muhammad Minhaz Reza",
    "author_short": "Minhaz Reza",
    "publisher": "Maktabatu Kunujul Akhirah",
    "publisher_ar": "مكتبة كنوز الآخرة",
    "publisher_note": "An imprint of the Kunujul Akhirah Charitable Trust",
    "contact": "minhaz.reza87@gmail.com",
    "year": "2026",
    "ages": "Ages 3–7",
}

# Qur'an quotations (simple Arabic script with full harakat). ¹ = Quran.com on the References page.
# MUST be checked by a qualified scholar / hafiz before publication.
AYAH_RAHMAN = dict(
    ref="Surah Ar-Raḥmān 55:1–4",
    ar="الرَّحْمَٰنُ ﴿١﴾ عَلَّمَ الْقُرْآنَ ﴿٢﴾ خَلَقَ الْإِنسَانَ ﴿٣﴾ عَلَّمَهُ الْبَيَانَ ﴿٤﴾",
    tr="Ar-Raḥmān. ʿAllamal-Qurʾān. Khalaqal-insān. ʿAllamahul-bayān.",
    en="The Most Merciful. He taught the Qur’an. He created the human being. He taught him clear expression (al-bayān).",
)
AYAH_RUM = dict(
    ref="Surah Ar-Rūm 30:22",
    ar="وَمِنْ آيَاتِهِ خَلْقُ السَّمَاوَاتِ وَالْأَرْضِ وَاخْتِلَافُ أَلْسِنَتِكُمْ وَأَلْوَانِكُمْ ۚ إِنَّ فِي ذَٰلِكَ لَآيَاتٍ لِّلْعَالِمِينَ ﴿٢٢﴾",
    tr="Wa min āyātihī khalqus-samāwāti wal-arḍi wakh-tilāfu alsinatikum wa alwānikum. Inna fī dhālika la-āyātil-lil-ʿālimīn.",
    en="And among His signs is the creation of the heavens and the earth, and the variety of your languages and your colours. Surely in that are signs for those who know.",
)
AYAH_HUJURAT = dict(
    ref="Surah Al-Ḥujurāt 49:13 (part)",
    ar="وَجَعَلْنَاكُمْ شُعُوبًا وَقَبَائِلَ لِتَعَارَفُوا",
    tr="Wa jaʿalnākum shuʿūban wa qabāʾila li-taʿārafū.",
    en="…and We made you into peoples and tribes so that you may get to know one another.",
)

# Helpers for Brahmi-family (Indic) scripts ------------------------------------------------------
def indic_consonant(letter, virama, inherent, inherent_tr="o"):
    return f'<div class="nt" style="font-size:19pt">{letter}{virama} + {inherent} = {letter}</div>'

def indic_vowel(sign, sign_name, example, example_tr, base):
    if not sign:
        return None
    return (f'<div class="nt" style="font-size:17pt">◌{sign} <span class="small" style="font-family:Nunito">'
            f'({sign_name})</span></div>'
            f'<div class="nt" style="font-size:17pt">{base} + ◌{sign} = {example} '
            f'<span class="tr" style="font-family:Nunito;font-size:12pt">({example_tr})</span></div>')
