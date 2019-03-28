


#!/usr/bin/env python

# In our movies data columns are separated by ::
# In loading data via Pig Storage this may cause some difficulties
# By means of this mapper we replace the delimiter :: by :
# ın this MapReduce process we do not need any reducer

import sys

for line in sys.stdin:
    print(line.strip().replace("::",":"))

