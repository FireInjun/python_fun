#!/usr/bin/env sh
# -*- coding: utf-8 -*-


"""
set_vars(){
    DIR=$1
    TEST="test_${1}.py"
    CODE="$1.py"
    INIT="__init__.py"
}

build_files()
{
    mkdir  $1 #Create Project Folder
    pushd "$1" #Go into Project Folder
    touch "$TEST"
    touch "$CODE"
    touch "$INIT" #Create new files
    popd #Go back to last stored spot
}

main()
{
set_vars
build_files
}

main
"""
