#!/bin/sh
IFS=$'\n'
dir=$1
declare -a files=($(find $dir -maxdepth 1 -type f | sort))
numfiles=${#files[@]}
if [ $numfiles -lt 2 ]
then
    exit 0
fi
declare -a islinked

for((i=0;i<$numfiles;i++)); do
    islinked[$i]=0
done


for((i=0;i<$numfiles;i++)); do
    file1=${files[i]}
    
    if [ -r $file1 ]
    then
	:
    else
	echo "files[$i] is not readable or doesnt exist"
    fi

    if [ "${islinked[$i]}" = "0" ]
    then
	name1="${file1##*/}"
	s1="${name1:0:1}"
	if [ "$s1" == '.' ]
	then
	    for((j=0;j<$numfiles;j++)); do
		file2=${files[$j]}
		if [ "$j" != "$i" ]
		then 
		    if [ "${islinked[$j]}" = 0 ]
		    then
			if [ -r $file2 ]
			then
			    cmp -s "$file1" "$file2"
			    res=$?
			    if [ $res -eq 0 ]
			    then
				rm "$file2"
				ln "$file1" "$file2"
				islinked[$i]=1
				islinked[$j]=1
			    fi
			else
			    echo "file2 was not readable or doesnt exist \n"
			fi
		    fi
		else
		    :
		fi
	    done
	fi
    fi
done

for((i=0;i<$numfiles;i++)); do
    file1=${files[i]}
    
    if [ -r $file1 ]
    then
	:
    else
	echo "files[$i] is not readable or doesnt exist"
    fi

    if [ "${islinked[$i]}" = "0" ]
    then
	name1="${file1##*/}"
	s1="${name1:0:1}"
	if [ "$s1" != '.' ]
	then
	    for((j=0;j<$numfiles;j++)); do
		file2=${files[$j]}
		if [ "$j" != "$i" ]
		then 
		    if [ "${islinked[$j]}" = 0 ]
		    then
			if [ -r $file2 ]
			then
			    cmp -s "$file1" "$file2"
			    res=$?
			    if [ $res -eq 0 ]
			    then
				rm "$file2"
				ln "$file1" "$file2"
				islinked[$i]=1
				islinked[$j]=1
			
			    fi
			else
			    echo "file2 was not readable or doesnt exist \n"
			fi
		    fi
		else
		    :
		fi
	    done
	fi
    fi
done













































































































