python3 -m virtualenv env
source env/bin/activate 

source /Users/mac/Documents/DjangoOrm/env/bin/activate
mac@macs-MacBook-Pro DjangoOrm % source /Users/mac/Documents/DjangoOrm/env/bin/activate
(env) mac@macs-MacBook-Pro DjangoOrm % python manage.py shell
Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> >>> from DjangoORM.models import Blog
Traceback (most recent call last):
  File "<console>", line 1, in <module>
ModuleNotFoundError: No module named 'postDjangoORM'
>>> from DjangoORM.models import Blog
>>> b = Blog(name='Food', tagline='This is the nices food blog')
>>> b.save()
Blog.objects.all(
Blog.objects.filter(tagline__startswith='This')
Blog.objects.filter(tagline__endswith='This')
Blog.objects.filter(name = 'Food')
Blog.objects.filter(tagline__iexact='This is the nices food BLOG')
Blog.objects.filter(tagline__contains='blog')


###333#####################################################


or create a new repository on the command line
echo "# Django2" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Markermav/Django2.git
git push -u origin main
…or push an existing repository from the command line
git remote add origin https://github.com/Markermav/Django2.git
git branch -M main
git push -u origin main
…or import code from another repository
You can initialize this repository with code from a Subversion, Mercurial, or TFS project.

