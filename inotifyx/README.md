# Sources:

sources from inotifyx are downloaded from [here](https://launchpad.net/inotifyx/)

source of patches from [here](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=856283)

# Apply patches:

patch -ruN -p1 -d inotifyx-0.2.2 < 0001-python3-compatibility.patch\
patch -ruN -p1 -d inotifyx-0.2.2 < 0002-update-C-binding-for-python3.patch

# Install
pip3 install --user ./inotifyx-0.2.2
