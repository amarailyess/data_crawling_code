echo "nom du script: $0"
echo "premier parametre: $1"
echo "second parametre: $2"
echo "pid du shell $$"
echo "code de retour: $?"
echo "Give us your name: "
read response
read -p "give your country: " country
echo "Hello ${response}"
echo "you are fom ${country}"
echo "personal directory /home/${response}"
exit
