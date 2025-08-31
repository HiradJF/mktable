1.You need to make an instance by doing it like this
       '''
       your_table_name = mktable.Table(["first", "row"], ["Other", "Rows(Optional)"])
       '''
    2. Each rows column count must be the same or the output might look ugly or don't work at all:
       > To prevent this pass empty sells like this "" or this "--"
    3.How to add rows? 
        '''
        your_table.add_row(["ABC","DEF"], ["Your", "Content"]) 
        '''
        just include any row you want how many you want
    4.How to render and Use? 
        use the render function
        like '''table_list = your_table.render()''' 
        or you can add arguements such as custom separators like this
        '''render(self, h_sep_char = '-',v_sep_char ='|', connection_point = '+')'''
        
        and btw it returns a list you can '''str(your_table)'' 
        to get the printable str
        or if you want to print it just do '''print(your_table)''' 
        it automaticaly casts it to str.

        Argurments:
            connection point : the point where separators connect.
                default: table.connection_point = "+"
            v_sep_char : vertical separator character
                default: table.v_sep_char = "|"
            h_sep_char : vertical separator character
                default: table.h_sep_char = "-"
    5.How to remove rows?
        call the function '''table.remove_row(*index)'''
        like '''table.remove_row(1, 5, 10)''
        make sure you have that amount of rows or you will get index out of range error
    