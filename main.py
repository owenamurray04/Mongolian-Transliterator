from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
from pathlib import Path

app = FastAPI(title="Bichig")

# Mongolian Cyrillic -> Latin.
MAPPING = {
    "а": "a",
    "б": "b",
    "в": "w",
    "г": "g",
    "д": "d",
    "е": "ye",
    "ё": "yo",
    "ж": "j",
    "з": "z",
    "и": "i",
    "й": "i",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "ө": "u",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ү": "v",
    "ф": "f",
    "х": "kh",
    "ц": "ts",
    "ч": "ch",
    "ш": "sh",
    "щ": "sh",
    "ъ": "i",
    "ы": "y",
    "ь": "i",
    "э": "e",
    "ю": "yu",
    "я": "ya",
}


def transliterate(text: str) -> str:
    out = []
    for ch in text:
        low = ch.lower()
        if low in MAPPING:
            latin = MAPPING[low]
            if ch.isupper():
                latin = latin.capitalize()
            out.append(latin)
        else:
            out.append(ch)  # spaces, digits, punctuation pass through
    return "".join(out)


@app.get("/transliterate")
def transliterate_get(text: str):
    return {"latin": transliterate(text), "system": "MNS 5217:2012"}


class Payload(BaseModel):
    text: str


@app.post("/transliterate")
def transliterate_post(payload: Payload):
    return {"latin": transliterate(payload.text), "system": "MNS 5217:2012"}


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {
        "service": "Mongolian Transliterator",
        "instructions": "/skill.md",
        "example": "/transliterate?text=Сайн байна уу",
    }

@app.get("/skill.md", response_class=PlainTextResponse)
def skill_md():
    return (Path(__file__).parent / "SKILL.md").read_text(encoding="utf-8")