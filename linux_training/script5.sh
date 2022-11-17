target=$1
usage(){
echo "usage: $0 <fichier>"
echo "compte les lignes d'un fichier"
exit
}

main(){
echo $target
ls -l $target
echo "nombre de lignes: $(wc -l $target)"
stat $target
exit
}

if [ $# -lt 1 ]; then
usage
elif [ $# -eq 1 ]; then
main
else
usage
fi
exit
