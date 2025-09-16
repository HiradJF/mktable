import unittest
from mktable.mktable import Table

# reigon random data for tests

# simple data

simple_data = (
    (
        ["ID", "Name", "Age"],
        [1, "Alice", 23],
        [2, "Bob", 30],
        [3, "Charlie", 18],
    ),
    """+----+---------+-----+
| ID | Name    | Age |
+----+---------+-----+
| 1  | Alice   | 23  |
| 2  | Bob     | 30  |
| 3  | Charlie | 18  |
+----+---------+-----+
""",
)

# Table with different data types

mixed_data = (
    (
        ["Product", "Price", "InStock", "Tags"],
        ["Laptop", 999.99, True, ["electronics", "work"]],
        ["Phone", 499.49, False, ["electronics"]],
        ["Book", 12.5, True, ["education", "fun"]],
    ),
    """+---------+--------+---------+-------------------------+
| Product | Price  | InStock | Tags                    |
+---------+--------+---------+-------------------------+
| Laptop  | 999.99 | True    | ["electronics", "work"] |
| Phone   | 499.49 | False   | ["electronics"]         |
| Book    | 12.5   | True    | ["education", "fun"]    |
+---------+--------+---------+-------------------------+
 """,
)

# Table with missing values
missing_data = (
    (
        ["ID", "Name", "Score"],
        [1, "Alice", 95],
        [2, None, 88],
        [3, "Charlie", None],
    ),
    """+----+---------+-------+
| ID | Name    | Score |
+----+---------+-------+
| 1  | Alice   | 95    |
| 2  |         | 88    |
| 3  | Charlie |       |
+----+---------+-------+
""",
)

# Larger numeric dataset (for sorting/filtering tests)
numeric_data = (
    (
        ["ID", "Value"],
        [1, 10],
        [2, 50],
        [3, 30],
        [4, 70],
        [5, 20],
    ),
    """+----+-------+
| ID | Value |
+----+-------+
| 1  | 10    |
| 2  | 50    |
| 3  | 30    |
| 4  | 70    |
| 5  | 20    |
+----+-------+
""",
)

# Edge cases (empty, duplicates)
edge_case_data = [
    (
        ["Key", "Value"],
        [1, "A"],
        [1, "B"],  # duplicate key
        [None, "C"],  # null key
    ),
    """+-----+-------+
| Key | Value |
+-----+-------+
| 1   | A     |
| 1   | B     |
|     | C     |
+-----+-------+
""",
]


class TestTable(unittest.TestCase):
    def test_output(self):
        t = Table(*simple_data[0])
        out = str(t)
        self.assertEqual(out.strip(), simple_data[1].strip())

    def test_render(self):
        t = Table(*simple_data[0])
        rendered = list(t.render())
        out = "\n".join(rendered)
        self.assertEqual(out.strip(), simple_data[1].strip())

    def test_add_rows(self):
        t = Table(*simple_data[0])
        new_rows = [["4", "Alex", "20"], ["5", "Jack", "30"]]
        t.add_row(*new_rows)

        # Convert the original simple_data rows to strings
        expected = [
            [str(cell) if cell is not None else "" for cell in row]
            for row in simple_data[0]
        ] + new_rows

        self.assertEqual(list(t.get_rows()), expected)


    def test_remove_rows(self):
        t = Table(*simple_data[0])
        t.remove_row(0, 2)
        self.assertEqual(t.rows, [["1", "Alice", "23"], ["3", "Charlie", "18"]])

    def test_move_rows(self):
        t = Table(*simple_data[0])

    def get_columns_test(self):
        pass

    def column_widths_test(self):
        pass

    def simple_gap_test(self):
        pass

    def mixed_data_test(self):
        pass

    def advanced_gap_test(self):
        pass


if __name__ == "__main__":
    unittest.main()
