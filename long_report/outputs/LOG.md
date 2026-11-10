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

## 2026-11-10 balanced (Track A)
- changed: `sample_weights` in `track_a/recipe.py` gives every photo the weight 1 / (number of photos of its city), so every city is drawn about 20% of the time. Nothing else is different from the baseline.
- why (student): because i remember in class the professor talked about the
  difference on the data each had, and because we cannot change the budget i
  thought about just having them equally.
- validation: 0.5093 (before: 0.4891 and 0.495, the baseline with seeds 0 and 1)
- what it means (student): that the more data you have the better, so the
  better option would be to have more busan and osaka pictures instead of
  reducing and having them all equally but for now in track A, not possible.

## 2026-11-10 no_flip (Track A)
- changed: `T.RandomHorizontalFlip()` removed from `train_transform` in `track_a/recipe.py`. Nothing else is different from `balanced`, which has every city drawn equally often.
- why (student): i wanted to remove the flip because of text orientation and
  layour. i thought if the alphabets were backwards, the model wouldnt get
  them, cause many pictures had clear busan or tokyo texts so i found it weird.
  same with the driving sides and country specific stuff. flipping it would
  change it.
- validation: 0.4995 (before: 0.5093, balanced)
- what it means (student): probly not reading or not having legible hangul or
  kanji to identify places. because of the 224 by 224 resolution.

## 2026-11-10 no_panorama (Track A)
- changed: the 670 training photos with width at least 2.0 times their height are left out of `track_a/selection.csv` (43,587 photos remain; made by `scripts/make_selection.py`, listed in `track_a/dropped.csv`). The recipe is the same as `balanced`. The 120 photos from the earlier "no information" cleaning stay in.
- why (student): i say various of them on the suspicion sheets, thought it could
  be a way of cleaning data.
- validation: 0.5025 (before: 0.5093, balanced)
- what it means (student): maybe it didn't work because the images were only
  like around 600? so the change wasnt very big.

## 2026-11-10 b2 (Track B)
- changed: the model and the image size. ResNet18 at 224 pixels (`b1`) became MobileNetV3-Large at 512 pixels (4.20 million parameters, 1.11 billion multiply-adds), 4 epochs as before. Two things changed at once, because of the time I had on Colab.
- why (student): when doing track A i found that letters were probably not taken
  into account for now because of how small it is. the 224 x 224. because we
  cannot change for track A i wondered if we could for Track B and because it
  was possible I did it. so there could be more info to use and to find unique
  features from the similar cities.
- validation: 0.5566 (before: 0.4865, b1)
- what it means (student): The model did well, but still is better on the main
  cities, seoul and tokyo.

## 2026-11-10 ema (Track A)
- changed: `on_step` keeps a running average of the weights (decay 0.999, over roughly the last 1,000 of the 3,906 steps) and `final_model` hands in the average. Nothing else is different from `balanced`.
- why (student): i did it to make sure that the last runs didnt change the
  results of the overall model.
- validation: 0.509 (before: 0.5093, balanced)
- what it means (student): but didnt change much.

## 2026-11-10 b3 (Track B)
- changed: `--balance` added, so every city is drawn equally often. Everything else is the same as `b2` (MobileNetV3-Large at 512 pixels, 4 epochs).
- why (student): it worked really well for track A so i wanted to see if it
  would also help on track b.
- validation: 0.5656 (before: 0.5566, b2). On the leaderboard page read at 18:43 KST it scored 0.417, against 0.432 for b2, so b2 was released again as `track-b-4` and stays my final Track B.
- what it means (student): but it didn't make much of a difference. probably the
  different pictures.
