age = 18
if age > 18:
    print('your eligible for vote')
elif age == 18:
    print('you van vote')
else:
    print('wait')
# Nested if
# Syntax
if True:
    print('outer if')
    if True:
        print("inner if")
    else:
        print('inner else')
else:
    print('outer else')
