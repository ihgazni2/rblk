#printf "please input the projname:"
#read projname

#printf "please input the git_username:"
#read git_username

#printf "please input the description:"
#read description

#printf "please input the author_email:"
#read author_email

#printf "please input the author:"
#read author



#必须变成双引号
#printf "replace check.py"
#sed -i "s/@projname@/${projname}/g" check.py
#printf "replace ./INIT/init.sh"
#sed -i "s/@projname@/${projname}/g" ./INIT/init.sh
#sed -i "s/@git_username@/${git_username}/g" ./INIT/init.sh
#printf "replace README.md"
#sed -i "s/@projname@/${projname}/g" README.md
#sed -i "s/@description@/${description}/g" README.md
#printf "replace setup.py"
#sed -i "s/@projname@/${projname}/g" setup.py
#sed -i "s/@git_username@/${git_username}/g" setup.py
#sed -i "s/@author_email@/${author_email}/g" setup.py
#sed -i "s/@description@/${description}/g" setup.py
#sed -i "s/@author@/${author}/g" setup.py
#printf "replace uninstall.sh"
#sed -i "s/@projname@/${projname}/g" uninstall.sh
#printf "replace updateversion.sh"
#sed -i "s/@projname@/${projname}/g" updateversion.sh


chmod 777 ./INIT/init.sh
./INIT/init.sh
