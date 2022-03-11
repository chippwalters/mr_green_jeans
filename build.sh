#!/bin/sh

overwrite=0
while getopts o flag
do
    case "${flag}" in
        o) overwrite=1;
    esac
done

version_extracted=`sed -n '/\"version\"/p' mr_green_jeans/__init__.py`
version_tmp=${version_extracted#*(}
version_final=${version_tmp%\)*} 
replace='.'
version=`echo $version_final | sed -e "s/, /${replace}/g"`


if [ -z "$version" ]
then
    echo 'Cannot get version from __init__.py.'
    exit 0
fi

echo 'Building version '$version'...'

if [ "$overwrite" -eq 1 ]
then
    echo 'Removing 'builds/v$version' directory.'
    rm -rf builds/v$version
fi

if [ -d builds/v$version ]
then
    echo 'Directory for v'$version' already exists, exiting.'
    exit 0
fi

mkdir builds/v$version
zip -FSr builds/v$version/mr_green_jeans.v$version.install.me.zip mr_green_jeans -x "*/__pycache__/*" "*/.DS_Store" "*/.vscode"

echo '...version '$version' built.'
