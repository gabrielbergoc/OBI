#!/usr/bin/bash

# usage:
# bash test.sh <problem>.py
#
# where <problem>.py is at ./<problem>/<problem>.py
# and test cases are in ./<problem>/<i>/<i>.in
# and expected answers are in ./<problem>/<i>/<i>.sol
# i = 1, 2, ..., N

red='\033[0;31m'
green='\033[0;32m'
yellow='\033[0;33m'
reset='\033[0m'

# source=$1
# out=$((${1%.*}))

# g++ $source -o $out -O2 -std=c++17 -lm

problem=${1%.*}

cd $problem

total_tests=0
passed=0

for dir in */ ; do
    dir_n=${dir:0:1};

    for fin in $dir/*.in ; do
        ((++total_tests))
        tmp=${fin#*\/\/};
        test_n=${tmp%.*};
        test_case="${dir_n}/${test_n}";
        
        input=$(<"${test_case}.in");
        # output=$((./${out} << ${input}));
        output=$(echo "$input" | python $1);
        expected=$(<"${test_case}.sol");

        echo -n "case ${test_case}: "
        if [[ $output -eq $expected ]]; then
            ((++passed))
            echo -e "${green}PASSED${reset}";
        else
            echo -e "${red}FAILED${reset}";
            echo -e " - expected: ${expected}";
            echo -e " - output: ${output}";
        fi
    done
done

echo "passed ${passed} of ${total_tests}"

cd ..
