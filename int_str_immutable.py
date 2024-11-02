x=10
print(f"x={x}, memory location of x:{id(x)}")
x=20
print(f"x={x}, memory location of x:{id(x)}")

s="hello"
print(f"s={s}, memory location of s:{id(s)}")
#s[0]="H" immutable
new_s="H"+s[1:]
print(f"new_s={new_s}, memory location of new_s:{id(new_s)}")