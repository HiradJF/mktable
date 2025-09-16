1.You need to make an instance by doing it like this:
    ```python
    your_table_name = mktable.Table()
    ```
    and you can have arguements like :
    ```python
    your_table_name = mktable.Table(["first", "row"], ["Other", "Rows(Optional)"])
    ```

2.How to add rows? 
    ```python
    your_table.add_row(["ABC","DEF"], ["Your", "Content"]) 
    ```
    just include any row you want how many you want.
3.How to render and Use? 
    use the render function
    like 
    ```python
    table_list = your_table.render()
    ```
    or you can add arguements such as custom separators like this
    ```python
    render(self, h_sep_char = '-',v_sep_char ='|', connection_point = '+')
    ```
    and btw it returns a list you can `str(your_table)` 
    to get the printable str
    or if you want to print it just do `print(your_table)` 
    it automaticaly casts it to str.
    
        Argurments:
        connection point : the point where separators connect.
            default: table.connection_point = "+"
        v_sep_char : vertical separator character
            default: table.v_sep_char = "|"
        h_sep_char : vertical separator character
            default: table.h_sep_char = "-"

    
           
4.How to remove rows?
    call the function 
    ```python
    table.remove_row(*index)
    ```
    like
    ```python
    table.remove_row(1, 5, 10)
    ```
    make sure you have that amount of rows or you will get index out of range error
    
    
5.How to use dictionaries?
    for importing from dict:
        ```python
        my_table.import_dict(my_dict, 'insert', index)  
        #replace my_table with your table and my dict with your dictionary and replace index with an index(int)
        #index in default is 0 and only matters in 'index' method
        ```
        method can be either 'insert', 'append' or 'overwrite'.method must be string.
        and the method string is not case-sensetive
            methods:
                overwrite: overwrites all the rows in the table
                insert: inserts the dict from given index (0 if non given)
                append: appends the dict to the end of the table

    for exporting to a dict:
        use this method:
        ```python
        my_table.export_dict() #returns a dict
        ```
        for assigning it to a new dict (if the variable already exists it will be overwritten):
        ```python
        my_dict = my_table.export_dict()
        ```
        and for adding it to a dict:
            ```python
            my_dict += my_table.export_dict()
            ```
            