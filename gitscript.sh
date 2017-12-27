cd $4/../JekLog/$1/$2
git init
git add .
git config user.email "ranvir@gmail.com"
git config user.name "Ranvir"
git commit -m "inital commit"
git branch gh-pages
git checkout gh-pages
git remote add origin https://github.com/$1/$2
git config remote.origin.url https://$1:$3@github.com/$1/$2.git
git push origin gh-pages
