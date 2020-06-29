mand() {
    if [[ $1 = "list" ]]; then
        python $(dirname "$BASH_SOURCE")/mand.py list
    elif [[ $1 = "map" ]]; then
        source .shellmands
    else
        echo "Usage: mand {list|map}"
    fi
}
