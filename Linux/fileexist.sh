#!/bin/bash
                                        # #checking the file exist with the name
# echo enter the file name
# read File
# if [ -e $File ]
# then echo 'file exist'
# else echo 'file does not exist'
# fi


                                       # checking that file exist with path and file name

echo enter the path or file name
read file
read path
LOC="$path // $file"
if [ -d $path ]
then
  LOC="$path/$file"
  if [ -e $LOC ]
  then
    echo "file exist"
  else
    echo "file does not exist"
  fi
else
  echo "path does not exist"
fi

                                            #arrays shell scripting

# fruits=( orange mango apple )
# fruits[0]=orange
# fruits[1]=mango
# fruits[2]=apple

# echo ${fruits[0]}
# echo ${fruits[1]}
# echo ${fruits[2]}