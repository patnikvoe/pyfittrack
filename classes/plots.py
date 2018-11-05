from pyfittrack import *

def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)

#
#
#   CHECK !!!
def plot_goal_actuall(tracks, goals):
    aktuellerMonat = last_day_of_month(datetime.date.today())
    pastgoals=goals[:aktuellerMonat.strftime("%Y-%m-%d")]

    distance = tracks["Strecke"].resample("M").sum()
    distance = distance.to_frame(name="Distanz gelaufen")
    distance = distance.assign(Zieldistanz=pastgoals["Zieldistanz"])

    pace = tracks["Pace"].resample("M").mean()
    pace = pace.to_frame(name="Mittlere Pace")
    pace = pace.assign(Zielpace=pastgoals["Zielpace"])

    speed = tracks["Speed"].resample("M").mean()
    speed = speed.to_frame(name="Mittlerer Speed")
    speed = speed.assign(Zielspeed=pastgoals["Zielspeed"])

    fig, axes =plt.subplots(nrows=3,ncols=1)

    distanceplot = distance.plot(style=["k-","r-"], ax=axes[0], label="Strecke",sharex=True)
    distanceplot.set_ylabel("Distanz in km")
    #distanceplot.set_title("Gelaufene Distanz vs. Ziel")

    paceplot = pace.plot(style=["k-","r-"], ax=axes[1],sharex=True)
    paceplot.set_ylabel("Pace in min/km")
    #paceplot.set_title("Mittlere Pace vs. Ziel")

    speedplot = speed.plot(style=["k-","r-"], ax=axes[2],sharex=True)
    speedplot.set_ylabel("Geschwindigkeit in km/h")
    speedplot.set_xlabel("Monat")
    #speedplot.set_title("Mittlere Geschwindigkeit vs. Ziel")

    plt.show()
