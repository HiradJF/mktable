#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 13:33:24 2025

@author: Hirad Jahangirfard (@HiradJF)

mktable:

a simple, efficient, super customizable table class
that's easy to use and does most of things you need
in showing a working yet sleek CLI table.
"""


class Table: 
    """
    mktable.Table is the class of mktable table as expected
    Make an instance by : table = mktable.Table(["Row","1"])
    Made by : Hirad jahangirfard
    Documentaition : ../../README.MD
    """

    def __init__(self, *rows: list):
        """
        The __init__ constructor of the table
        """
        self.rows = [row for row in rows]  # adds rows to self.rows
        self.h_sep_char = "-"
        self.v_sep_char = "|"
        self.connection_point = "+"
        self.empty = ""

    def add_row(self, *new_rows: list):
        """
        adds given rows from the *new_rows arguement
        """
        for nr in new_rows:
            self.rows.append(nr)

    def get_columns(self) -> list:
        """
        Transforms the rows and returnes the column (with filled gaps)
        """
        #columns = []
        rows = self.fill_rows_gaps()
        for i in range(len(rows[0])):
            column = [row[i] for row in rows]
            yield column
            #columns.append(column)
        #return columns
    
    def get_raw_columns(self) -> list:
        """
        Transforms the rows and returnes the raw column without filling the gaps
        """
        #columns = []
        rows = self.get_rows()
        for i in range(len(rows[0])):
            column = [row[i] for row in rows]
            yield column
            #columns.append(column)
        #return columns

    def remove_row(self, *index, **kwargs):
        """
        Removes the row with the given index(s) : *index
        Or by the content with *kwargs
        Use like rm1 = ["Hi", "this row", "must be deleted"]
        """
        for i in range(len(self.rows)):
            try :
                self.rows.pop(index[i])
            except IndexError:
                raise IndexError(f"[Error] mktable: there isn't a row on the given index therefore removing row [{i}] was not possible (IndexError)")


    def move_row(self, old_index, new_index):
        """Moves the row in old_index to new_index"""
        try :
            self.rows.insert(new_index, self.rows.pop(old_index))
        except IndexError:
            raise IndexError("[Error] mktable: there is no row on old_index or new_index ," \
            " therefore moving the row from index {old_index} to {new_index} was not possible (IndexError)")

    def render(self) -> list:
        """
        Renders out the table and returns it in a list.
        To get the printable string do this: str(my_table)
        This upper function casts the table list to str which I added this ability by __str__(self) function and returns it
        To print this: print(m) # No need to cast it to string with str(my_table) when printing it.
        """
        rows = self.fill_rows_gaps()
        h_sep_char = self.h_sep_char
        v_sep_char = self.v_sep_char
        connection_point = self.connection_point
        column_widths = self.get_columns_widths()
        max_column_widths = [max(col_width) for col_width in column_widths]
        
        horizontal_separator = ''

        def format_row(row: list) -> list:
            """formats the row and returns it so that it's spacing and seperators are fixed"""
            formatted_row = []

            for i, cell in enumerate(row):
                # getting the diffrence between the needed width and the actual width
                diff = max_column_widths[i] - len(cell)
                # formatting the cell {0} is the vertical sep {1} is the unformatted cell from rows
                # {2} is the needed spacing
                # so it should look like this |cell   | the space replicates spacing
                formatted_cell = f"{v_sep_char} {cell}{' '*diff} "
                formatted_row.append(formatted_cell)
                
                
            
            return ("".join(formatted_row)) + v_sep_char

        f_rows = list(map(format_row, rows))
        
        horizontal_separator = ''.join((connection_point if char == v_sep_char else h_sep_char 
                                        for char in f_rows[0]))

        f_rows.insert(0, horizontal_separator)
        f_rows.insert(2, horizontal_separator)
        f_rows.append(horizontal_separator)
        #finaly returns the rendered list in a iter of string
        return iter(f_rows)

    def __str__(self):
        rows = self.render()
        n_rows = list(map(lambda row: row + "\n", rows))
        return "".join(n_rows)

    def get_columns_widths(self) -> list:
        """
        You can get every columns width in a list with this method.
        """
        # for getting the printable(max) width of each column :
        max_column_widths = []
        columns = self.get_columns()
        for column in columns:
            column_widths = []
            for cell in column:
                # gets the column widths (width of each row in column)
                column_widths.append(len(cell))
            # gets the max width for this column
            max_column_widths.append(column_widths)
        # and this loop ^ gets all the columns max widths
        # why? we need max widths for spacing and the table being inline
        return max_column_widths

    def get_rows_lengths(self, rows=None):
        if rows is None:
            rows = self.rows
        return [len(row) for row in rows]

    def insert_row(self, index:int, row:list[str]):
        '''inserts a row in given index'''
        self.rows.insert(index, row)

    def get_rows(self) -> list:
        """
        Returns a copy of all rows.
        Users can modify the returned list safely without affecting the table.
        """
        return [row.copy() for row in self.rows]  # shallow copy of each row


    def fill_rows_gaps(self) -> list:
        """
        This method gets an copy of rows, fills it's empty gaps with self.empty and returns it.
        This makes it efficient to print and is used internally.
        """
        # initializing variables
        rows = self.get_rows()
        rows_lengths = self.get_rows_lengths()
        #error handling
        try:
            max_rows_len = max(rows_lengths)
        except ValueError: 
            raise ValueError("[Error] mktable: the rows are empty (ValueError)")

        for i in range(len(rows)):
            diff = max_rows_len - rows_lengths[i] # getting the error
            rows[i] += [self.empty] * diff
        return rows
    
    def export_dict(self):
        table_dict = {}
        columns = list(self.get_columns())  # materialize generator
        headers = columns[0]  # first row = header
        for i, header in enumerate(headers):
            table_dict[header] = [row[i] for row in self.rows[1:]]  # skip header row
        return table_dict

    
    def import_dict(self, dictionary : dict, method:str , index:int = 0):
        """
        Imports the given dictionary by the given method
        -------------------------------------------------
        :param dictionary (dict): this is the arguement for the dictionary you want to import.
            keys = header      values = other rows
        :param method (str): this is the method that your dictionary is imported
            available methods : 'append', 'insert', 'overwrite'
        """
        method = method.strip().lower() #making it non case-sensetive and non whitespace sensetive
        columns = []
        header = list(dictionary.keys())
        rows = [header] + [list(r) for r in zip(*dictionary.values())]
        del header

        if method == 'append':
            self.add_row(*rows)
        elif method == 'insert':
            for i in range(index, len(rows)):
                self.insert_row(i, rows[i])
        elif method == 'overwrite':
            self.rows = rows
        else :
            raise NotImplementedError(f"Currently there is no method named '{method}'." +
                                      "\nAvailable methodes : 'append', 'overwrite', 'insert'")


            

if __name__ == '__main__':
    rows = []
    t = Table()

    print("Enter table rows. Use ';' to separate cells.")
    print("Use '@e' for an empty cell, and '@x' to finish input.\n")

    while True:
        raw_input = input("Enter row: ").strip()
        if raw_input == "":
            continue  # skip empty input lines
        cells = raw_input.split(";")

        if "@x" in cells:
            break  # exit input loop

        # replace '@e' with the table's empty placeholder
        row = [t.empty if cell == "@e" else cell for cell in cells]
        rows.append(row)

    # assign the collected rows to the table
    t.rows = rows

    # print the table
    print(t)

