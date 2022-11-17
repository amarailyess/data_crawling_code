target=$1
execverif(){
if [ -x $target ]; then
echo $target " est executable."
else
echo $target " n est pas executable."
fi
}
dir=$2
dirverif(){
if [ -d $dir ]; then
rm -rf $dir
echo "le dossier de travail $dir et il est effacé"
else
mkdir $dir
echo "le dossier de travail $dir a été creer"
fi
}
execverif
dirverif
exit
