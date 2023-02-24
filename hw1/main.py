import legal
import epidemiology
import industrial
import defense
import pandas as pd

def main() -> None:
    legal_data = pd.read_excel('data.xlsx', 'Legal')
    epi_data = pd.read_excel('data.xlsx', 'Epidemiology')
    industry_data = pd.read_excel('data.xlsx', 'Industrial Engineering')
    defense_data = pd.read_excel('data.xlsx', 'Defense Contracting')

    print('---- Legal ----')
    legal.stats_analysis(legal_data)
    print('---- Legal ----')

    print('---- Epidemiology ----')
    epidemiology.stats_analysis(epi_data)
    print('---- Epidemiology ----')

    print('---- Industrial Engineering ----')
    industrial.stats_analysis(industry_data)
    print('---- Industrial Engineering ----')

    print("---- Defense Contracting ----")
    defense.stats_analysis(defense_data)
    print("---- Defense Contracting ----")

    return

if __name__ == '__main__':
    main()
