#!/usr/bin/env bash
echo "le contenu du repertoire courant va etre affiché."
affiche(){
read -p "souhaitez-vous afficher aussi les fichiers cachés (oui/non): " rep
case $rep in
	oui)
		clear
		ls -a;;
	non)
		ls;;
	*)	
		echo "veuillez repondre par oui ou non."
		affiche;;
esac
}
affiche
exit
