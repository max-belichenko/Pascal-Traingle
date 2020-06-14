def pascal_traingle(n: int) -> list:
    """
    Counts Pascal Traingle to given number of rows.

    Returns list of rows with counted numbers.
    """
    traingle = [[1]] # Pascal Traingle starts with a row of a single number 1. 
  
    for _ in range(n):
        base = [0]  # Extend row with leading and ending zeroes.
        base.extend(traingle[-1])
        base.append(0)
        
        row = [base[i] + base[i+1] for i in range(len(base)-1)] # Count new elements as a sum of two neighbour elements of a current row.

        traingle.append(row)
        
    return traingle


def print_pascal_traingle(traingle):
    """ Pretty print for a Pascal Traingle. """

    # Get max length of text string needed to represent a longest row.
    
    max_element = max(traingle[-1])
    element_width = len(str(max_element))
    max_elements_count = len(traingle[-1])
    number_of_spaces = max_elements_count - 1
    text_width = element_width * len(traingle[-1]) + number_of_spaces
        
    for row in traingle:
        text = ''
        for i in range(len(row)):
            element_text = f'{str(row[i]):^{element_width}}'
            text += element_text
            if i < len(row) - 1:
                text += ' '

        print(f'{text:^{text_width}}')
    

if __name__ == '__main__':
    n = int(input('Enter number of rows for Pascal Traingle:'))

    traingle = pascal_traingle(n)

    print_pascal_traingle(traingle)
