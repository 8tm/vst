#!/usr/bin/env bash
# shellcheck disable=SC2181

MAIN_FOLDER="src/mts tests"
BASH_FILES_TO_CHECK=$(find . -name \*.sh  -not -path "./.venv/*" | tr '\012' ' ')

declare -A COMMANDS=(
    [pylint]="pylint --rcfile=.pylintrcfile ${MAIN_FOLDER}"                                                                       \
    [flake8]="flake8 ${MAIN_FOLDER}"                                                                                              \
    [mypy]="mypy --disallow-untyped-defs --disallow-incomplete-defs --check-untyped-defs --disallow-untyped-calls ${MAIN_FOLDER}" \
    [shellcheck]="shellcheck ${BASH_FILES_TO_CHECK}"                                                                              \
)

check_status() {
    local command="${1}"
    local show_output="${2}"
    local status="\\033[31m ERROR \\033[0m"

    if [ "${show_output}" != "true" ]; then
        { ${command} > /dev/null; } 2>&1
    else
        ${command}
    fi

    if [ $? -eq 0 ]; then
        status="\\033[32m  O K  \\033[0m"
    fi

    echo -e "$(printf "[%-7s] %-70s\\n" "${status}" "${command}")"
}

show_help() {
    echo -e "\\n Usage:
    ${0}                 Run all applications without output
    ${0} [application]   Run application and show output

    \\rArguments:
    -h, --help           This help

    \\r Currently available applications and used commands:"

    for COMMAND in "${!COMMANDS[@]}";
    do
        printf "* %-10s  [ %-70s ]\\n" "${COMMAND}" "${COMMANDS[${COMMAND}]}"
    done
    echo
}

main() {
    if [ $# -gt 0 ]; then
        if [ "${1}" == "--help" ] || [ "${1}" == "-h" ] || [ "${COMMANDS[${1}]}" == "" ]; then
            show_help
            exit 1
        fi
        command="${COMMANDS[${1}]}"
        show_output=true
        check_status "${command}" ${show_output}
    else
        for COMMAND in "${!COMMANDS[@]}";
        do
            check_status "${COMMANDS[${COMMAND}]}"
        done
    fi
}

main "$@"
