set term gif animate delay 50
set output 'sort.gif'
stats "sort.dat" u 1:2 nooutput
set title "Sortowanie ShakerSort"
set xlabel "numer pozycji"
set ylabel "liczba na pozycji"
unset key
do for [i=1:int(STATS_blocks)]{
    plot "sort.dat" index (i-1) u 1:2 with points pt 5
}
quit