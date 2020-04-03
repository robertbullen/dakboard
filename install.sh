#!/usr/bin/env bash

# libgraphviz-dev installs everything necessary for pygraphviz to be built at installation.
# graphviz installs the actual binaries invoked by pygraphviz at runtime.
apt-get install -y libgraphviz-dev graphviz || exit $?

# Install all the Python packages.
pip3 install -r requirements.txt || exit $?
