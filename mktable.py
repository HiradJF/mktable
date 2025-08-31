#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 13:33:24 2025

@author: Hirad Jahangirfard (@HiradJF)
"""

class Table():
    """
    mktable.Table is a class of a table as expected
    Make an instance by : table = mktable.Table(["Row","1"])
    Made by : Hirad jahangirfard
    Documentaition : ./README.MD
    



        

    """
    def __init__(self, header:list, *rows:list):
        '''The __init__ constructor of the table'''
        self.rows = []
        self.h_sep_char = '-'
        self.v_sep_char = '|'
        self.connection_point = '+'
        self.rows.append(header)
        for row in rows :
            self.rows.append(row)
   
    def add_row(self, *new_rows:list):
        
        for nr in new_rows:
            self.rows.append(nr)

    def get_columns (self) -> list:
        columns = []
        for i in range(len(self.rows[0])):
            column = [row[i] for row in self.rows]
            columns.append(column)
        return columns
    
    def remove_row(self, *index):
        for i in len(self.rows):
            self.rows.pop(index[i])
    
    def render(self):
        """
        Renders out the table and returns it in a list.
        To get the printable string do this: str(my_table)
        This upper function casts the table list to str which I added this ability by __str__(self) function and returns it
        To print this: print(m) # No need to cast it to string with str(my_table) when printing it.
        """
        rows = self.rows
        h_sep_char = self.h_sep_char
        v_sep_char = self.v_sep_char
        connection_point = self.connection_point
        
        max_column_widths = self.get_max_column_widths()
        
        def fill_rows_len_gaps(rows):
            pass
        def format_row(row:list) -> list:
            """formats the row and returns it so that it's spacing and seperators are fixed"""
            formatted_row = []
            for i in range(len(row)):
                #getting the diffrence between the needed width and the actual width
                diff = max_column_widths[i] - len(row[i])
                #formatting the cell {0} is the vertical sep {1} is the unformatted cell from rows
                #{2} is the needed spacing
                # so it should look like this |cell   | the space replicates spacing
                formatted_cell = f"{v_sep_char} {row[i]}{' '*diff} "              
                formatted_row.append(formatted_cell)
            
            return ("".join(formatted_row)) + v_sep_char
        
        
        f_rows = list(map(format_row, rows))
        border_len = len(f_rows[0]) - 2
        horizontal_separator = connection_point + (h_sep_char * border_len) + connection_point

        
        f_rows.insert(0, horizontal_separator)
        f_rows.insert(2, horizontal_separator)
        f_rows.append(horizontal_separator)
        #finaly returns the rendered in list ! of string !
        return f_rows
        
        
    def __str__(self):
        rows = self.render()
        n_rows = list(map(lambda row: row + "\n", rows))
        return "".join(n_rows)        
    
    def get_max_column_widths(self) -> list:
        #for getting the printable(max) width of each column :
        max_column_widths = []
        for column in self.get_columns():
            column_widths = []
            for i in column:
                #gets the column widths (width of each row in column)
                column_widths.append(len(i))
            #gets the max width for this column
            max_column_widths.append(max(column_widths))
        # and this loop ^ gets all the columns max widths
        #why? we need max widths for spacing and the table being inline
        return max_column_widths
    
    def get_row_lengths(self):
        length = []
        rows = self.rows
        for i in range(len(rows)):
            length.append(len(rows[i]))
        return length
        
        
    
t = Table(["First Name","Last Name"], ["Hirad", "Jahangirfard"], ["qwen", "--"])
t.add_row(["Behrad"])
print(t)