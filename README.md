# Pascal Traingle
 Counts Pascal Traingle to the given number of rows and saves it in a list.

Example of a Pascal Traingle with 10 rows (printed by this script):
                     1
                   1   1
                 1   2   1
               1   3   3   1
             1   4   6   4   1
           1   5  10  10   5   1
         1   6  15  20  15   6   1
       1   7  21  35  35  21   7   1
     1   8  28  56  70  56  28   8   1
   1   9  36  84  126 126 84  36   9   1
 1  10  45  120 210 252 210 120 45  10   1



First row is always set to single element that is equal to 1.

All next rows are counted using following algorithm:

Step 1: add leading and ending zeroes to current row.
Row:        [1]
Modified:   [0 , 1, 0]

Step 2: count elements of row as sum of two neighbour elements for the above row.
Row:        [0, 1, 0]
Next row:   [0 + 1, 1 + 0] -> [1, 1]

A few more rows generation:
Row:        [1, 1]
Modified:   [0, 1, 1, 0]
Next row:   [0 + 1, 1 + 1, 1 + 0] -> [1, 2, 1]

Row:        [1, 2, 1]
Modified:   [0, 1, 2, 1, 0]
Next row:   [0 + 1, 1 + 2, 2 + 1, 1 + 0] -> [1, 3, 3, 1]

And so on.



pascal_traingle(n: int) -> list:
    Takes number of rows into the n variable.
    Counts Pascal Traingle to the given number of rows.
    Returns a list of rows with Pascal Traingle numbers.
    Example of returned value:
    [[1],
     [1, 1],
     [1, 2, 1],
     [1, 3, 3, 1]]


print_pascal_traingle(traingle):
    Prints formatted array with Pascal Traingle numbers to the standart output.
    Example of output:
                                      1
                                    1    1
                                 1    2    1
                               1    3    3    1
                            1    4    6    4    1
                          1    5    10   10   5    1
                       1    6    15   20   15   6    1
                     1    7    21   35   35   21   7    1
                  1    8    28   56   70   56   28   8    1
                1    9    36   84  126  126   84   36   9    1
             1    10   45  120  210  252  210  120   45   10   1
           1    11   55  165  330  462  462  330  165   55   11   1
        1    12   66  220  495  792  924  792  495  220   66   12   1
      1    13   78  286  715  1287 1716 1716 1287 715  286   78   13   1
   1    14   91  364  1001 2002 3003 3432 3003 2002 1001 364   91   14   1
 1    15  105  455  1365 3003 5005 6435 6435 5005 3003 1365 455  105   15   1