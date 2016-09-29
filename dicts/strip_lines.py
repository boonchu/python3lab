muls = """// this is a comment
{ // another comment
   true, "foo", // 3rd comment
   "http://www.ariba.com" // comment after URL
}"""

buffers=list()
begin_to_strip_it = False
reserved_word = False
count = 0
for c in muls:
    if '"' in c:
        if not reserved_word:
            reserved_word = True
        else:
            reserved_word = False
            count = 0
        buffers += str(c)
    elif '/' in c:
        count += 1
        if count == 2 and not reserved_word:
            begin_to_strip_it = True
        elif count > 2:
            count = 0
        if reserved_word:
            buffers += str(c)
        next
    elif '\n' in c: 
        begin_to_strip_it = False
        reserved_word = False
        buffers += str(c)
        count = 0
        next
    else:
        if not begin_to_strip_it:
            buffers += str(c)

print ''.join(buffers)
