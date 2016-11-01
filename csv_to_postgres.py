"""
Usage:
    python csv_to_postgres.py <csv file name> <schema_name.table_name> | psql <database url>
"""

import sys
import re


def format_column_name(col_name):
    col_name = re.sub(r'([a-z])([A-Z])', r'\1_\2', col_name)
    col_name = col_name.replace(' ', '_')
    col_name = col_name.lower()
    return col_name


if __name__ == '__main__':
    file_name = sys.argv[1]
    table_name = sys.argv[2]

    first_line = open(file_name).readline()[:-1]
    column_names = first_line.split(',')
    column_names = map(format_column_name, column_names)

    column_definitions_str = '\n  ' + ',\n  '.join(['\"%s\" varchar' % col for col in column_names])
    drop_table_command = 'DROP TABLE IF EXISTS %s;' % table_name
    create_table_command = 'CREATE TABLE %s (%s\n);' % (table_name, column_definitions_str)
    copy_file_command = "\\copy %s FROM \'%s\' DELIMITER ',' CSV HEADER;" % (table_name, file_name)

    print(drop_table_command)
    print()
    print(create_table_command)
    print()
    print(copy_file_command)
