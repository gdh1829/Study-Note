String Interpolation 문자열 보간법
==========================

<code>
#!/bin/bash
how_many=6
echo "Can you eat ${how_many} bananas?" # Can you eat 6 bananas?

series="GameOfThrones"
echo "Have you watched $series_$season ?" # Not evaluated to "Have you watched GameOfThrones_7?"
echo "Have you watched ${series}_${season} ?" #OK

</code>
