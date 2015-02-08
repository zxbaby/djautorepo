#!/usr/bin/python 

#coding:utf8


import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')

def main():
    from learn.models import Blog
    f = open('/tmp/testblog.txt')
    for line in f:
	title,content = line.split('****')
	Blog.objects.create(title=title,content=content)
    f.close()

if __name__ == '__main__':
    main()
    print 'Done'
