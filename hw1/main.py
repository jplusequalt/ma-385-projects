import legal
import epidemiology
import pandas as pd

def main() -> None:
    legal_data = pd.read_excel('data.xlsx', 'Legal')
    epi_data = pd.read_excel('data.xlsx', 'Epidemiology')

    print('---- Legal ----')
    legal.stats_analysis(legal_data)
    print('---- Legal ----')

    print('---- Epidemiology ----')
    epidemiology.stats_analysis(epi_data)
    print('---- Epidemiology ----')

    return

if __name__ == '__main__':
    main()
