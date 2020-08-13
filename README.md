# Pascal Traingle
<p>Counts Pascal Traingle to the given number of rows and saves it in a list.</p>

<p>Example of a Pascal Traingle with 10 rows (printed by this script):</p>
<p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;3&nbsp;&nbsp;&nbsp;3&nbsp;&nbsp;&nbsp;1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;4&nbsp;&nbsp;&nbsp;6&nbsp;&nbsp;&nbsp;4&nbsp;&nbsp;&nbsp;1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;5&nbsp;&nbsp;10&nbsp;&nbsp;10&nbsp;&nbsp;&nbsp;5&nbsp;&nbsp;&nbsp;1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;6&nbsp;&nbsp;15&nbsp;&nbsp;20&nbsp;&nbsp;15&nbsp;&nbsp;&nbsp;6&nbsp;&nbsp;&nbsp;1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;7&nbsp;&nbsp;21&nbsp;&nbsp;35&nbsp;&nbsp;35&nbsp;&nbsp;21&nbsp;&nbsp;&nbsp;7&nbsp;&nbsp;&nbsp;1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;8&nbsp;&nbsp;28&nbsp;&nbsp;56&nbsp;&nbsp;70&nbsp;&nbsp;56&nbsp;&nbsp;28&nbsp;&nbsp;&nbsp;8&nbsp;&nbsp;&nbsp;1<br>
&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;9&nbsp;&nbsp;36&nbsp;&nbsp;84&nbsp;&nbsp;126&nbsp;126&nbsp;84&nbsp;&nbsp;36&nbsp;&nbsp;&nbsp;9&nbsp;&nbsp;&nbsp;1<br>
&nbsp;1&nbsp;&nbsp;10&nbsp;&nbsp;45&nbsp;&nbsp;120&nbsp;210&nbsp;252&nbsp;210&nbsp;120&nbsp;45&nbsp;&nbsp;10&nbsp;&nbsp;&nbsp;1<br>
</p>



<p>First row is always set to single element that is equal to 1.</p>

<p>All next rows are counted using following algorithm:</p>

<p>Step 1: add leading and ending zeroes to current row.</p>
<p>Row:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1]</p>
<p>Modified:&nbsp;&nbsp;&nbsp;[0 , 1, 0]</p>

<p>Step 2: count elements of row as sum of two neighbour elements for the above row.</p>
<p>Row:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0, 1, 0]</p>
<p>Next row:&nbsp;&nbsp;&nbsp;[0 + 1, 1 + 0] -> [1, 1]</p>

<p>A few more rows generation:</p>
<p>Row:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1, 1]</p>
<p>Modified:&nbsp;&nbsp;&nbsp;[0, 1, 1, 0]</p>
<p>Next row:&nbsp;&nbsp;&nbsp;[0 + 1, 1 + 1, 1 + 0] -> [1, 2, 1]</p>

<p>Row:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1, 2, 1]</p>
<p>Modified:&nbsp;&nbsp;&nbsp;[0, 1, 2, 1, 0]</p>
<p>Next row:&nbsp;&nbsp;&nbsp;[0 + 1, 1 + 2, 2 + 1, 1 + 0] -> [1, 3, 3, 1]</p>

<p>And so on...</p>



<p><b>pascal_traingle(n: int) -> list:</b><br>
    Takes number of rows into the n variable.<br>
    Counts Pascal Traingle to the given number of rows.<br>
    Returns a list of rows with Pascal Traingle numbers.<br>
    Example of returned value:<br>
    [[1],<br>
     [1, 1],<br>
     [1, 2, 1],<br>
     [1, 3, 3, 1]]<br>
</p>

<p><b>print_pascal_traingle(traingle):</b><br>
    Prints formatted array with Pascal Traingle numbers to the standart output.<br>
    Example of output:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;3&nbsp;&nbsp;&nbsp;&nbsp;3&nbsp;&nbsp;&nbsp;&nbsp;1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;4&nbsp;&nbsp;&nbsp;&nbsp;6&nbsp;&nbsp;&nbsp;&nbsp;4&nbsp;&nbsp;&nbsp;&nbsp;1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;5&nbsp;&nbsp;&nbsp;&nbsp;10&nbsp;&nbsp;&nbsp;10&nbsp;&nbsp;&nbsp;5&nbsp;&nbsp;&nbsp;&nbsp;1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;6&nbsp;&nbsp;&nbsp;&nbsp;15&nbsp;&nbsp;&nbsp;20&nbsp;&nbsp;&nbsp;15&nbsp;&nbsp;&nbsp;6&nbsp;&nbsp;&nbsp;&nbsp;1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;7&nbsp;&nbsp;&nbsp;&nbsp;21&nbsp;&nbsp;&nbsp;35&nbsp;&nbsp;&nbsp;35&nbsp;&nbsp;&nbsp;21&nbsp;&nbsp;&nbsp;7&nbsp;&nbsp;&nbsp;&nbsp;1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;8&nbsp;&nbsp;&nbsp;&nbsp;28&nbsp;&nbsp;&nbsp;56&nbsp;&nbsp;&nbsp;70&nbsp;&nbsp;&nbsp;56&nbsp;&nbsp;&nbsp;28&nbsp;&nbsp;&nbsp;8&nbsp;&nbsp;&nbsp;&nbsp;1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;9&nbsp;&nbsp;&nbsp;&nbsp;36&nbsp;&nbsp;&nbsp;84&nbsp;&nbsp;126&nbsp;&nbsp;126&nbsp;&nbsp;&nbsp;84&nbsp;&nbsp;&nbsp;36&nbsp;&nbsp;&nbsp;9&nbsp;&nbsp;&nbsp;&nbsp;1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;10&nbsp;&nbsp;&nbsp;45&nbsp;&nbsp;120&nbsp;&nbsp;210&nbsp;&nbsp;252&nbsp;&nbsp;210&nbsp;&nbsp;120&nbsp;&nbsp;&nbsp;45&nbsp;&nbsp;&nbsp;10&nbsp;&nbsp;&nbsp;1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;11&nbsp;&nbsp;&nbsp;55&nbsp;&nbsp;165&nbsp;&nbsp;330&nbsp;&nbsp;462&nbsp;&nbsp;462&nbsp;&nbsp;330&nbsp;&nbsp;165&nbsp;&nbsp;&nbsp;55&nbsp;&nbsp;&nbsp;11&nbsp;&nbsp;&nbsp;1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;12&nbsp;&nbsp;&nbsp;66&nbsp;&nbsp;220&nbsp;&nbsp;495&nbsp;&nbsp;792&nbsp;&nbsp;924&nbsp;&nbsp;792&nbsp;&nbsp;495&nbsp;&nbsp;220&nbsp;&nbsp;&nbsp;66&nbsp;&nbsp;&nbsp;12&nbsp;&nbsp;&nbsp;1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;13&nbsp;&nbsp;&nbsp;78&nbsp;&nbsp;286&nbsp;&nbsp;715&nbsp;&nbsp;1287&nbsp;1716&nbsp;1716&nbsp;1287&nbsp;715&nbsp;&nbsp;286&nbsp;&nbsp;&nbsp;78&nbsp;&nbsp;&nbsp;13&nbsp;&nbsp;&nbsp;1<br>
&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;14&nbsp;&nbsp;&nbsp;91&nbsp;&nbsp;364&nbsp;&nbsp;1001&nbsp;2002&nbsp;3003&nbsp;3432&nbsp;3003&nbsp;2002&nbsp;1001&nbsp;364&nbsp;&nbsp;&nbsp;91&nbsp;&nbsp;&nbsp;14&nbsp;&nbsp;&nbsp;1<br>
&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;15&nbsp;&nbsp;105&nbsp;&nbsp;455&nbsp;&nbsp;1365&nbsp;3003&nbsp;5005&nbsp;6435&nbsp;6435&nbsp;5005&nbsp;3003&nbsp;1365&nbsp;455&nbsp;&nbsp;105&nbsp;&nbsp;&nbsp;15&nbsp;&nbsp;&nbsp;1<br>
 </p>
