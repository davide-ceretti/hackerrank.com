from collections import Counter
input_string = raw_input()
is_odd = len(input_string) % 2

if is_odd:
    counter = Counter(input_string)
    values = [each % 2 for each in counter.itervalues()]
    if values.count(1) != 1:
        print 'NO'
    else:
        print 'YES'
else:
    counter = Counter(input_string)
    values = [each % 2 for each in counter.itervalues()]
    if values.count(1) > 0:
        print 'NO'
    else:
        print 'YES'
