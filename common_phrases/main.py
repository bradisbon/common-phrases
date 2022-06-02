import re
from collections import Counter
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel


api = FastAPI()


class Text(BaseModel):
    text: str


class MostCommon(BaseModel):
    most_common: List[str]


def clean(text: str) -> List[str]:
    """Replace newlines with spaces, remove punctuation, and convert to lowercase"""

    no_newlines = text.replace('\n', ' ')
    no_punc = re.sub(r"[^a-z ]+", '', no_newlines, flags=re.I)
    lower = no_punc.lower()

    return [word for word in lower.split(' ') if re.match(r'[a-z]',word)]


@api.post('/find_common', response_model=MostCommon)
async def find_common(text: Text):
    clean_text = clean(text.text)
    counts = Counter((' '.join(clean_text[i:i+3]) for i,_ in enumerate(clean_text[:-2])))

    return {'most_common': (p[0] for p in counts.most_common(100))}
