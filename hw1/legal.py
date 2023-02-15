import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Tuple

def stats_analysis(data: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:

    # two stratum, 1 == men, 0 == women
    men = data[data.Gender == 1]
    total_men = len(men.Status)
    women = data[data.Gender == 0]
    total_women = len(women.Status)
    
    # accepted == 1, rejected == 0
    total_applicants = len(data.Status)
    total_accepted = len(data.Status[data.Status == 1])
    total_rejected = total_applicants - total_accepted
    men_accepted = len(men[men.Status == 1])
    men_rejected = total_men - men_accepted
    women_accepted = len(women[women.Status == 1])
    women_rejected = total_women - women_accepted

    print(f'Number of applicants: {total_applicants}')
    print(f'Percentage of applicants who are men: {(total_men / total_applicants):.2f}')
    print(f'Percentage of applicants who are women: {(total_women / total_applicants):.2f}')

    print(f'Percentage of applicants accepted: {(total_accepted / total_applicants):.2f}')
    print(f'Percentage of accepted applicants who are men: {(men_accepted / total_accepted):.2f}')
    print(f'Percentage of accepted apppliants who are women: {(women_accepted / total_accepted):.2f}')

    print(f'Relative freq. of men applicants being accepted: {(men_accepted / total_men):.2f}')
    print(f'Relative freq. of women applicants being accepted: {(women_accepted / total_women):.2f}')

    # just for visuals, we'll calculate this by hand
    contingency_tbl = pd.DataFrame({
        'gender': ['man', 'woman'],
        'accepted': [men_accepted, women_accepted],
        'rejected': [men_rejected, women_rejected],
        'totals': [total_men, total_women]
    })
    print(contingency_tbl)

    # expected freq. is given by (total of row r) * (total of col c) / N
    expected_accepted_men = (total_men * total_accepted) / total_applicants
    expected_accepted_women = (total_women * total_accepted) / total_applicants
    expected_rejected_men = (total_men * total_rejected) / total_applicants
    expected_rejected_women = (total_women * total_rejected) / total_applicants
    print(f'Expected number of accepted men: {expected_accepted_men}')
    print(f'Expected number of rejected men: {expected_rejected_men}')
    print(f'Expected number of accepted women: {expected_accepted_women}')
    print(f'Expected number of rejected women: {expected_rejected_women}')

    diff_accepted_men_sqrd = ((men_accepted - expected_accepted_men)**2 / expected_accepted_men)
    diff_rejected_men_sqrd = ((men_rejected- expected_rejected_men)**2 / expected_rejected_men)
    diff_accepted_women_sqrd = ((women_accepted - expected_accepted_women)**2 / expected_accepted_women)
    diff_rejected_women_sqrd = ((women_rejected- expected_rejected_women)**2 / expected_rejected_women)

    # the chi_square test stat is given by sum((expected - observed)^2 / expected)
    chi_square = diff_accepted_men_sqrd + diff_rejected_men_sqrd \
        + diff_accepted_women_sqrd + diff_rejected_women_sqrd

    # for the critical val we have the following:
    # deg. of freedom = (2 genders - 1) * (2 application states - 1) = 1
    # significance level = 0.5 per convention
    # Using these values with the below table: 
    # https://cdn.scribbr.com/wp-content/uploads/2022/05/chi-square-distribution-table.png
    critical_val = 3.841

    print(f'Chi Square test statistic: {chi_square}')
    print(f'Critical chi-square value: {critical_val}')

    if critical_val < chi_square:
      print('Null hypothesis rejected')
    else:
      print('Alternative hypothesis rejected')

    _, ax = plt.subplots()

    bottom = np.zeros(2)
    names = (
        f'Men\n{total_men} total app.\n{((men_accepted / total_men) * 100):.2f}% accepted', 
        f'Women\n{total_women} total app.\n{((women_accepted / total_women) * 100):.2f}% accepted')
    counts = {
        'accepted': np.array([men_accepted, women_accepted]),
        'rejected': np.array([men_rejected, women_rejected])
    }

    for bool, count in counts.items():
        _ = ax.bar(names, count, 0.5, label=bool, bottom=bottom)
        bottom += count

    ax.set_title('Acceptance totals for each gender')
    ax.set_ylabel('# of applicants')
    ax.legend(loc='upper right')

    def func(pct, allvals):
        absolute = int(np.round(pct/100.*np.sum(allvals)))
        return f"{pct:.1f}%\n({absolute:d})"

    pie_data = [men_accepted, women_accepted] 

    _, ax2 = plt.subplots()
    wedges, _, autotexts = ax2.pie(
        pie_data, 
        colors=['blue', 'pink'],
        autopct=lambda pct: func(pct, pie_data),
        textprops=dict(color='w')
    )

    ax2.set_title('Percentage of accepted applicants by gender')
    ax2.legend(wedges, ['men', 'women'], title='Gender', loc='upper right')
    plt.setp(autotexts, size=12, weight='bold')

    plt.show()

    return

if __name__ == '__main__':
  
    data = pd.read_excel('data.xlsx')

    stats_analysis(data)
    