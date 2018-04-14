'''
Python中如何将int在十进制和二、八、十六进制之间互相转换
'''
#第一种 这样转换会有一个前缀0b、0o、0x
a = 100

print(bin(a))#2进制
print(oct(a))#8进制
print(hex(a))#16进制
print()
#第二种 如果不想要前缀只想要数值的话，可以使用format

print(format(a,'b'))
print(format(a,'o'))
print(format(a,'x'))
print()

#二、八、十六进制向十进制转换
#直接使用int()即可，因为int()的原型是int(x, base=10)，所以我们只需要指定base就行了
print(int('1100100',base=2),int('144',base=8),int('64',base=16))
print()

#如果只是需要在源码中将二、八、十六进制转十进制，实际上只需要写上前缀就可以了，不需要进行转换，数值会自动转换为十进制

print(0b1100100,0o144,0x64)