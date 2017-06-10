#These are the directories for the finished games to go, change them as needed
#RESULTDIR1=~/496/496-stuff/output/test1
# RESULTDIR2=~/496/496-stuff/output/test2
# RESULTDIR3=~/496/496-stuff/output/test3
# RESULTDIR4=~/496/496-stuff/output/test4
# RESULTDIR5=~/496/496-stuff/output/ourOwnTest

RESULTDIR1=test1 #Creates a directory where you run the command
RESULTDIR2=test2
RESULTDIR3=test3
RESULTDIR4=test4
# Modify paths to your programs below as needed
LGO1=Go4-current\\Go4.py
LGORANDOM=lgoRandom\\lgoRandom.py
GO6=Go6\\Go6.py


#####################
#These are old paths for reference, written on linux
# NOGO4=~/496/496-stuff/Go4/Go4.py
# NOGO4AC=~/496/496-stuff/Go4AC/Go4AC.py
# NOGO3=~/496/496-stuff/Go3/Go3.py
# NOGO4ACAD=~/496/496-stuff/Go4ACAD/Go4ACAD.py
######################
TWOGTP=gogui-twogtp
run(){
echo Match with $NUGAMES games on board size $BOARDSIZE.
mkdir -p $RESULTDIR1
mkdir -p $RESULTDIR2


echo Playing $LGO1 vs $GO6
$TWOGTP -black "python $LGO1" -white "python $GO6"  -auto -komi 0 -threads 2 -size $BOARDSIZE -games $NUGAMES -sgffile $RESULTDIR1/test1
$TWOGTP -analyze $RESULTDIR1/test1.dat -force

echo Playing $GO6 vs $LGO1
$TWOGTP -white "python $LGO1" -black "python $GO6" -auto -komi 0 -threads 2 -size $BOARDSIZE -games $NUGAMES -sgffile $RESULTDIR2/test1
$TWOGTP -analyze $RESULTDIR2/test1.dat -force





#Feel free to change the threads to however many you want to use. Do not use more than your computer has, can crash shit or actually slow you down

#The rest of the commented lines were for an assignment, left here as reference
#Feel free to create as many tests as you want

# $TWOGTP -black "$NOGO3" -white "$NOGO4AC" -auto  -komi 6.5 -threads 8 -size $BOARDSIZE -games $NUGAMES -sgffile $RESULTDIR1/test1
# $TWOGTP -analyze $RESULTDIR1/test1.dat -force
# #
# echo Playing $NOGO3 vs $NOGO4ACAD
# $TWOGTP -black "$NOGO3" -white "$NOGO4ACAD" -auto  -komi 6.5 -threads 8 -size $BOARDSIZE -games $NUGAMES -sgffile $RESULTDIR2/test2
# $TWOGTP -analyze $RESULTDIR2/test2.dat -force
# #
# echo Playing $NOGO4 vs $NOGO4AC
# $TWOGTP -black "$NOGO4" -white "$NOGO4AC" -auto  -komi 6.5 -threads 8 -size $BOARDSIZE -games $NUGAMES -sgffile $RESULTDIR3/test3
# $TWOGTP -analyze $RESULTDIR3/test3.dat -force
#
}
NUGAMES=60
BOARDSIZE=10
run
