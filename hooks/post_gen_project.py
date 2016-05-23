#!/usr/bin/env python

import os


main_dir = os.path.join(os.getcwd(), 'src', 'main', 'java')
test_dir = os.path.join(os.getcwd(), 'src', 'test', 'java')
org_package = '{{ cookiecutter.org_package }}'

dirs = org_package.split('.')

temp_main_dir = main_dir
temp_test_dir = test_dir
for d in dirs:
    temp_main_dir = os.path.join(temp_main_dir, d)
    if not os.path.exists(temp_main_dir):
        os.makedirs(temp_main_dir)
    temp_test_dir = os.path.join(temp_test_dir, d)
    if not os.path.exists(temp_test_dir):
        os.makedirs(temp_test_dir)
