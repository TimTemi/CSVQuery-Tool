import csv

class MySelectQuery:
    def __init__(self, csv_content):
        self.rows = []
        for row_str in csv_content.strip().split('\n'):
            self.rows.append(row_str.strip().split(','))
        self.columns = self.rows[0]
        self.rows = self.rows[1:]

    def where(self, column_name, criteria):
        result = []
        for row in self.rows:
            if row[self.columns.index(column_name)] == criteria:
                result.append(','.join(row))
        return result