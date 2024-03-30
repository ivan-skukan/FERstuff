proba="Ovo je proba"
echo $proba #provjeri

#lista_datoteka=($(find -type f))
lista_datoteka=(*)
echo "${lista_datoteka[@]}"

proba3=""
for i in 1 2 3
do
  proba3+="$proba. "
done
echo "$proba3"

a=4
b=3
c=7
d=$((($a+4)*$b%$c))
echo "$a $b $c $d"

broj_rijeci=$(wc -w *.txt)
echo "$broj_rijeci"

ls ~
