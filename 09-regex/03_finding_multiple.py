import re
silly_string = "the cat in the hat"
pattern = "the"
print (re.findall(pattern, silly_string))

# Finding multiple matches using findite()
silly_string = "the cat in the hat"
pattern = "the"

for match in re.finditer(pattern, silly_string):
    s = "Found '{group}' at {begin}:{end}".format(
        group=match.group(), begin=match.start(),
        end=match.end())
    print(s)