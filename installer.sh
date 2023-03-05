#!/bin/bash

RED="\e[31m"
YELLOW="\e[1;33m"
ENDCOLOR="\e[0m"
BOLD="\e[1m;"
ITALIC="\e[3m;"

clear
echo -e "@-----------------------------------------------------@"
echo -e "| I will install all requirements for this project.   |"
echo -e "|                                                     |"
echo -e "| author: blcklptn                                    |"
echo -e "@-----------------------------------------------------@"



unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     machine=Linux;;
    Darwin*)    machine=Mac;;
    CYGWIN*)    machine=Cygwin;;
    MINGW*)     machine=MinGw;;
    *)          machine="UNKNOWN:${unameOut}"
esac

install_requirements() {
  echo "Installing requirements from pyproject.toml"
  poetry install
}

install_requirements
