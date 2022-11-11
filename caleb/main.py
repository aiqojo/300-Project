import pandas as pd


def main():
    # reading in data\
    lap_times = pd.read_csv('../data/lap_times.csv')
    print(lap_times[:5])
    print(max(lap_times['raceId']))
    print(len(lap_times))

    qualifying = pd.read_csv('../data/qualifying.csv')
    print(qualifying[:5])

main()