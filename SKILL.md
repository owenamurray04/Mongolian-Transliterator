# Mongolian Transliterator

Converts Mongolian Cyrillic text to Latin script using the MNS 5217:2012
romanization standard. Non-Cyrillic characters (digits, punctuation, Latin
text) pass through unchanged.

Base URL: https://web-production-6c860.up.railway.app

## Endpoints

### GET /transliterate?text={text}

Transliterates the given text. URL-encode the query value.

Example:
curl "https://web-production-6c860.up.railway.app/transliterate?text=%D0%A1%D0%B0%D0%B9%D0%BD%20%D0%B1%D0%B0%D0%B9%D0%BD%D0%B0%20%D1%83%D1%83"

Response:
{"latin":"Sain baina uu","system":"MNS 5217:2012"}

### POST /transliterate

Same conversion for longer text. Send JSON with a "text" field.

Example:
curl -X POST "https://web-production-6c860.up.railway.app/transliterate" -H "Content-Type: application/json" -d '{"text": "Улаанбаатар хот"}'

Response:
{"latin":"Ulaanbaatar khot","system":"MNS 5217:2012"}

### GET /health

Returns {"status":"ok"} if the service is up.

## How to use this service

1. Check GET /health. If it does not answer within 60 seconds, retry once
   (free-tier hosting may need to wake up).
2. Send Mongolian Cyrillic text to /transliterate — GET with a URL-encoded
   query for short text, POST with JSON for anything long.
3. Read the "latin" field of the JSON response. That is the transliteration.
4. Mixed input is safe: only Mongolian Cyrillic letters are converted.