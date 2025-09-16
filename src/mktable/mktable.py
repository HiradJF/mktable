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
        self._rows = list(self._stringify_rows(rows)) #turns the rows into list[]
        self.h_sep_char = "-"
        self.v_sep_char = "|"
        self.connection_point = "+"
        self.empty = ""
    
    @property
    def rows(self):
        return self.get_rows()

    def add_row(self, *new_rows: list):
        """
        adds given rows from the *new_rows arguement
        """
        stringified_new_rows = self._stringify_rows(new_rows)
        self._rows.extend(stringified_new_rows)

    def get_columns(self) -> iter:
        """
        Transforms the rows and returnes the column (with filled gaps)
        """
        # columns = []
        rows = self.fill_rows_gaps()
        for i in range(len(rows[0])):
            column = [row[i] for row in rows]
            yield column
            # columns.append(column)
        # return columns

    def get_raw_columns(self) -> iter:
        """
        Transforms the rows and returnes the raw column without filling the gaps
        """
        # columns = []
        rows = self.get_rows()
        for i in range(len(rows[0])):
            column = [row[i] for row in rows]
            yield column
            # columns.append(column)
        # return columns

    def remove_row(self, *index):
        """
        Removes the row with the given index(s) : *index
        """

        for i in sorted(index, reverse=True):
            # try:
            if i >= len(self._rows):
                raise IndexError(
                    "[Error] mktable: there isn't a row on the given index"
                    + f"therefore removing row [{i}] was not possible (IndexError)"
                )
            self._rows.pop(i)

    def move_row(self, old_index, new_index):
        """Moves the row in old_index to new_index"""
        try:
            self._rows.insert(new_index, self._rows.pop(old_index))
        except IndexError:
            raise IndexError(
                "[Error] mktable: there is no row on old_index or new_index ,"
                + f"therefore moving the row from index {old_index} to {new_index} was not possible (IndexError)"
            )

    def render(self) -> iter:
        """
        Renders out the table and returns it in a iter.
        To get rendered list do this : list(table.render())
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

        horizontal_separator = ""

        def _format_row(row: list) -> list:
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

        f_rows = list(map(_format_row, rows))

        horizontal_separator = "".join(
            (
                connection_point if char == v_sep_char else h_sep_char
                for char in f_rows[0]
            )
        )

        f_rows.insert(0, horizontal_separator)
        f_rows.insert(2, horizontal_separator)
        f_rows.append(horizontal_separator)
        # finaly returns the rendered list in a iter of string
        return iter(f_rows)

    def __str__(self) -> str:
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

    def get_rows_lengths(self, rows=None) -> list:
        if rows is None:
            rows = self._rows
        return [len(row) for row in rows]

    def insert_row(self, index: int, row: list[str]):
        """inserts a row in given index"""
        self._rows.insert(index, row)

    def get_rows(self) -> list:
        """
        Returns a copy of all rows.
        Users can modify the returned list safely without affecting the table.
        """
        return [list(row).copy() for row in self._rows]  # shallow copy of each row
    
    def fill_rows_gaps(self, rows=None) -> list:
        """
        This method gets an copy of rows, fills it's empty gaps with self.empty and returns it.
        This makes it efficient to print and is used internally.
        """
        # initializing variables
        if rows is None:
            rows = self.get_rows()
            rows_lengths = self.get_rows_lengths()
        else:
            rows_lengths = self.get_rows_lengths(rows)
        # error handling
        try:
            max_rows_len = max(rows_lengths)
        except ValueError:
            raise ValueError("[Error] mktable: the rows are empty (ValueError)")

        for i in range(len(rows)):
            diff = max_rows_len - rows_lengths[i]  # getting the error
            rows[i] += [self.empty] * diff
        return rows

    def export_dict(self):
        table_dict = {}
        #columns = list(self.get_columns())  # materialize generator
        headers = self.get_rows()[0]  # first row = header
        for i, header in enumerate(headers):
            try:
                table_dict[header] = [
                    row[i] for row in self._rows[1:]
                ]  # skip header row
            except IndexError:
                pass  # passes if the row doesn't exist
        return table_dict

    def import_dict(self, dictionary: dict, method: str, index: int = 0):
        """
        Imports the given dictionary by the given method
        -------------------------------------------------
        :param dictionary (dict): this is the arguement for the dictionary you want to import.
            keys = header      values = other rows
        :param method (str): this is the method that your dictionary is imported
            available methods : 'append', 'insert', 'overwrite'
        """
        method = (
            method.strip().lower()
        )  # making it non case-sensetive and non whitespace sensetive
        header = list(dictionary.keys())
        rows = [header] + [list(r) for r in zip(*dictionary.values())]
        del header  # don't need the header var anymore :(    it's now in rows[0]

        if method == "append":
            self.add_row(*rows)
        elif method == "insert":
            for i in range(index, len(rows)):
                try:
                    self.insert_row(i, rows[i])
                except:
                    raise IndexError(f"mktable: There is no row at index [{i}]")
        elif method == "overwrite":
            self._rows = rows
        else:
            raise NotImplementedError(
                f"mktable: Currently there is no method named '{method}'."
                + "\nAvailable methodes : 'append', 'overwrite', 'insert'"
            )
    
    def _stringify_rows(self, rows:list[list[any]] = []) -> iter:
        """
        Turns given rows to string and yields it.
        this is a generator so you might have to cast it to list or tuple
        ------------------------------------------------------------------------------------
        : param rows -> list[list[any]] : the rows parameter. def=self.rows
        
        NOTE : this effects the original list if you want it to give back a copy and do not affect
        the original list you need first get a deep copy of rows list then give it to this function
        """
        rows = (
            self._rows if rows == [] else list(rows)
        )  # sees if rows is given or not if not given(empty) assigns self.rows else assignes given rows
        for row in rows:
            # this line down here makes every row a string if row is none it will be assigned to self.empty
            row = list(map(lambda cell: str(cell) if not (cell is None) else self.empty, row))
            yield row

    def replace_all_rows(self, new_rows:list[list[any]]):
        """
        Replaces all rows with the given new_rows
        """
        self.remove_row(*range(len(self._rows)))
        self.add_row(*new_rows)
        
if __name__ == "__main__":
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
    t._rows = rows

    # print the table
    print(t)
