import sqlite3
import pandas as pd
from tabulate import tabulate
from IPython.display import display

def save_to_df(db_path, table_name, columns='ALL'):
    conn = sqlite3.connect(db_path)
    if isinstance(columns, str):
        return pd.read_sql_query(f"SELECT * FROM {table_name}",conn)
    else:
        print("Not supported yet")

"""
Following the plan in our interim report

‘charge_degree’ (from ‘casearrest’ table) which is a categorical variable describing how serious is their sentencing.
‘Name’ (from ‘prisonhistory’ table) which is a categorical variable describing which prison(s) the individual stayed at.
‘In_custody’ (from ‘prisonhistory’ table) which gives the starting time of the individual going to the prison.
‘Legal_status’ (from ‘summary’ table)
‘Marital_status’ (from ‘compas’ table)
‘Case_type’ (from ‘compas’ table)
‘Race’ (from ‘summary’ table)
‘Sex’ (from ‘summary’ table)
‘Age’ (from ‘summary’ table)
‘Num_days_in_jail’ (from ‘summary’ table)
‘Filing_type’ (from ‘summary’ table)
‘Filling_agency’ (from ‘summary’ table)
‘juv_fel_count’ (from ‘people’ table)
‘juv_misd_count’ (from ‘people’ table)
‘juv_other_count’ (from ‘people’ table)

"""

def merge_as_planned(db_path):
    conn = sqlite3.connect(db_path)

    query = f"""
            SELECT
                casearrest.charge_degree,
                people.id AS person_id, 
                people.violent_recid,
                people.is_recid,
                people.juv_fel_count,
                people.juv_misd_count,
                people.juv_other_count,
                prisonhistory.name,
                prisonhistory.in_custody,
                prisonhistory.out_custody,
                compas.legal_status,
                compas.marital_status,
                people.race,
                people.sex,
                people.age,
                summary.num_days_in_jail,
                summary.recidivist,
                charge.case_type,
                charge.filing_type,
                charge.filing_agency,
                charge.case_number
            FROM 
                casearrest
            LEFT JOIN people ON casearrest.person_id = people.id
            INNER JOIN prisonhistory ON casearrest.person_id = prisonhistory.person_id
            LEFT JOIN compas ON casearrest.person_id = compas.person_id
            LEFT JOIN summary ON casearrest.person_id = summary.person_id
            LEFT JOIN charge ON casearrest.case_number = charge.case_number
            GROUP BY
                people.id,
                charge.case_number
            """
    df = pd.read_sql_query(query, conn)
    return df




if __name__ == "__main__":
    path = "compas-analysis-master/compas.db"
    df = save_to_df(path, 'people')
    display(df.head())
    display(df.tail())
    print(df.shape) 


    df = merge_as_planned(path)
    #df.dropna(inplace=True)
    print(tabulate(df.head(10), headers='keys',tablefmt='html'))
    print(tabulate(df.tail(10), headers='keys',tablefmt='html'))
    print(df.shape) 