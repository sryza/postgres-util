import sys

if __name__ == '__main__':
    file_name = sys.argv[1]
    table_name = sys.argv[2]

    first_line = open(file_name).readline()[:-1]
    column_names = first_line.split(',')

    column_definitions_str = ', '.join(['\"%s\" varchar' % col for col in column_names])
    create_table_command = 'CREATE TABLE %s (%s);' % (table_name, column_definitions_str)
    copy_file_command = "\\copy %s FROM \'%s\' DELIMITER ',' CSV HEADER;" % (table_name, file_name)

    print(create_table_command)
    print()
    print(copy_file_command)
