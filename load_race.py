import fastf1
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

fastf1.Cache.enable_cache('cache')  #caching to speed up data retrieval

#loading monza race session
session =fastf1.get_session(2024, "Monza", "R")
session.load()  

laps = session.laps

#filtering out all slow laps (ex. starting lap where there is more congestion)
quick_laps = laps.pick_quicklaps()

#filter for Fernando Alonso
alonso_laps = quick_laps[quick_laps["Driver"] == "ALO"].copy()

#converting lap times to seconds
alonso_laps["LapTimeSeconds"] = alonso_laps["LapTime"].dt.total_seconds()

#remove rows with missing values
alonso_laps = alonso_laps.dropna(
    subset=["LapTimeSeconds", "LapNumber", "Compound"]
)

#plot lap times by tire compound
for compound, group in alonso_laps.groupby("Compound"):
    plt.scatter(
        group["LapNumber"],
        group["LapTimeSeconds"],
        label=compound
    )

#labelling plot axes 
plt.xlabel("Lap Number")
plt.ylabel("Lap Time (seconds)")
plt.title("Fernando Alonso Lap Times At 2024 Monza GP")
plt.legend()

plt.savefig("lap_times.png")
plt.show()

#this time shows how many laps the tire set completed
# instead of measuring lap time against total of numbers completed
#in the race, here I am measuring it against the wear of a single set of tires

for compound, group in alonso_laps.groupby("Compound"): #separating his laps by tire compound
    plt.scatter(
        group["TyreLife"],
        group["LapTimeSeconds"],
        label = compound
    )

model = smf.ols(
    "LapTimeSeconds ~ LapNumber + TyreLife + C(Compound)",
    data=alonso_laps
).fit()

print(model.summary())

plt.xlabel("Tyre Life (laps)")
plt.ylabel("Lap Time (seconds)")
plt.title("Fernando Alonso Lap Times vs Tire Life At 2024 Monza GP")
plt.legend()

plt.savefig("lap_times_vs_tire_life.png")
plt.show()

#plot shows 3 stints, medium, medium and hard, with medium having the overall fastest lap times
