for num in 0 1 2 3 4 5; do
#touch fichier$num.tar.gz;
echo ficher$num.tar.gz
done

for i in {1..9}; do
echo number $i;
done


for x in ./*.tar.gz; do
if [ -e $file ]; then
echo "$x -> $x.old"
mv "$x" "$x.old"
else
echo $x "not exist"
fi
done


for file in ./*.tar.gz; do
if [ -e $file ]; then
rm $file;
echo $file "removed successfully";
else
echo "not exist"
fi
done

for ((i=0;i<5;i=i+1)); do
 echo $i
 done

exit
