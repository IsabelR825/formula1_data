# formula1_data

I'm a big Formula 1 fan, so I wanted to see what the race data says about tire wear. This is my first project using real F1 data, so it's not very complicated and I still want to add and build to it.

## What I'm trying to figure out
How much slower do lap times get as a set of tires ages? And can I see that through the other things changing during a race?

## The data
Lap timing data from the 2024 Italian Grand Prix at Monza, pulled with the FastF1 Python library. So far I'm only looking at Fernando Alonso's laps after filtering out pit laps and slow laps.

## What I did
- Loaded the race data and cleaned out the slow laps
- Plotted lap time by lap number, colored by tire compound
- Plotted lap time by tire age
- Ran a regression in statsmodels with lap number, tire life and compound

## What I found
- Lap times get faster as the race goes on. I think that's because the cars burn off fuel and get lighter, and the track gets grippier, which hides the tire wear.
- Once I put lap number in the regression, each extra lap on a set of tires was associated with about 0.056 seconds slower (95% interval roughly 0.04 to 0.08).
- Some context is that Alonso finished with a midfield result at 11th place. After the race he said Aston Martin were "doing something really wrong" and he was frustrated that the car wasn't competitive with the teams at the front, so these laps come from a car that wasn't one of the fastest. 

## What I want to improve
- It's only one driver and one race, so I'd like to expand it to get more information on other cars and constructors.
- The regression errors are correlated from lap to lap since Durbin-Watson was about 1.13, so my standard errors are probably too small.
- Next I want to add stint to the model, use more drivers, and try robust standard errors.

## How to run it
1. Install these libraries: `pip install fastf1 pandas matplotlib statsmodels`
2. Make an empty folder called `cache` next to `load_race.py`
3. Run `python3 load_race.py`

The first run takes a few minutes because it downloads the race data
