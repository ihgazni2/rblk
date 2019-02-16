pip3 uninstall rblk
git rm -r dist
git rm -r build
git rm -r rblk.egg-info
rm -r dist
rm -r build
rm -r rblk.egg-info
git add .
git commit -m "remove old build"
