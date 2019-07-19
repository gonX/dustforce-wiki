#!/bin/bash -x

. config # should contain TARGET_DIR

if [ ! -d "$TARGET_DIR" ]; then
    echo "no such dir '${TARGET_DIR}'"
    exit 1
fi

if [ ! -f "$TARGET_DIR"/index.html ]; then
    echo "no index.html, ^C to abort or wait to continue..."
    sleep 5
fi

(
    cd ../../website
    [ -d "_pushdir" ] && rm -r "_pushdir"
    mkdir "_pushdir" || exit 3
    rm -rI "$TARGET_DIR"/* || exit 4
    bundle exec jekyll build -d "_pushdir" || exit 5
    cp -r -t "$TARGET_DIR" _pushdir/* || exit 6
    rm -r "_pushdir"
)
