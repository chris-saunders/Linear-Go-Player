RESULTDIR1=~/496/496-stuff/output/test1
RESULTDIR2=~/496/496-stuff/output/test2
RESULTDIR3=~/496/496-stuff/output/test3
RESULTDIR4=~/496/496-stuff/output/test4
RESULTDIR5=~/496/496-stuff/output/ourOwnTest
# Modify paths to your programs below as needed
NOGO4=~/496/496-stuff/Go4/Go4.py
NOGO4AC=~/496/496-stuff/Go4AC/Go4AC.py
NOGO3=~/496/496-stuff/Go3/Go3.py
NOGO4ACAD=~/496/496-stuff/Go4ACAD/Go4ACAD.py
TWOGTP=gogui-twogtp
run(){
echo Match with $NUGAMES games on board size $BOARDSIZE.
mkdir -p $RESULTDIR1
mkdir -p $RESULTDIR2
mkdir -p $RESULTDIR3
mkdir -p $RESULTDIR4
mkdir -p $RESULTDIR5
echo Playing $NOGO4 vs $NOGO4ACAD
$TWOGTP -black "$NOGO4" -white "$NOGO4ACAD" -auto  -komi 6.5 -threads 8 -size $BOARDSIZE -games $NUGAMES -sgffile $RESULTDIR4/test4
$TWOGTP -analyze $RESULTDIR4/test4.dat -force
#
echo Playing $NOGO4AC vs $NOGO4ACAD
$TWOGTP -black "$NOGO4AC" -white "$NOGO4ACAD" -auto  -komi 6.5 -threads 8 -size $BOARDSIZE -games $NUGAMES -sgffile $RESULTDIR5/test5
$TWOGTP -analyze $RESULTDIR5/test5.dat -force
}
NUGAMES=100
BOARDSIZE=5
run
