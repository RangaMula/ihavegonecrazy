One file per language (or agent): `engine/pics/<code>.py`.

```python
from illos import P, C, E, R, L, poly, star, star_pts, crescent, cloud, leaf, ground  # helpers, viewBox 0 0 200 200

def baobab():          # every closed shape gets a colour role class a-e; open lines get "n" (and "t" for thin)
    return R(90, 90, 20, 90, "b") + cloud(40, 100, 1.2, "c") + ground(186)

PICS = {"sw_baobab": baobab}   # ALWAYS prefix new keys with your language code
```
Objects, plants and nature only — no people, no animals, no faces.
