# Log

One entry for each recipe, selection or Track B model you train, newest at
the bottom. The numbers come from `experiments.csv`. "Why" and "what it means"
are in your own words: your agent asks you for them and does not make them up.
End the log with your plan for what to try next.

<!-- The form of an entry:

## <date> <tag> (Track A or B)
- changed: what is different from the run before
- why: your reason
- validation: 0.000 (before: 0.000)
- what it means: what you think the result says
-->

## 2026-11-09 What tells the cities apart (before any training)
Written by the student, after looking at the first-look sheets (`look_<city>_NN`):

High Geo value images tell cities apart, stuff like: roads, street scenes,
building facades, road signs, storefronts, trains or buses, skyline views,
traditional architectural buildings, driving side, reflective markers on the
street, utility poles and plates, font styles, web adresses on trucks, buses,
phone numbers with area codes, license plates, sun position (north or south
hemisphere), particular types of flora and fauna, taxi colors, unique designs
from different utilities like electric boxes, scooter boxes, flags, etc. like
GeoGuessr experts.

## 2026-11-09 What the baseline's mistakes have in common
Written by the student, after looking at the sheets `mistakes_baseline_seed0_<city>_00`:

I see a lot of cars without plates, and cities between same countries get
confused with each other when there is any writing or alphabets because its the
same, for example seoul or busan, so intra country regional confusion cause it
shares infrastructure or cultural elements. Buddhist temples are similar
between countries with lower resolution and a smaller image it could probably
not identify them correctly. big commercial places or markets can be confusing
too. generic asphalt is not as specific, food and indoor or close up shots,
panoramic or 360vies confuse the model too.

## 2026-11-09 baseline (Track A, seeds 0 and 1)
- changed: nothing. The starter recipe as it came, trained twice; only the seed differs.
- why (student): to differentiate if it was progress or a lucky guess. models
  take the data randomly, and the seed changes that. so it will help see if the
  model actually learns or its just the randomness at work.
- validation: 0.4891 (seed 0), 0.495 (seed 1)
- what it means (student): the randomness did not affect it much. so basically
  it learned the same thing or close to the same thing. so now we know
  randomness wont affect it much. this will also give us a base on see what
  number to look at when we change stuff. if it is lower than this number then
  the change we did, did not work. this way we can look for stuff that makes
  the model better (actually better)
