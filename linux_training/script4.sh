read -p "put a number: " number
p=$((number%2))
n=0
echo "p=$p"
if [ "$p"=="$n" ]; then
echo $number is pair
else
echo $number is impair
fi

passwdir=/etc/passwd
checkdir(){
if [ -e $passwdir ]; then
echo "le fichier $passwdir existe"
else
echo "le fichier $passwdir n'existe pas"
fi
}
checkdir
exit


