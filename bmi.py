w = input('請輸入體重(公斤):')
h = input('請輸入身高(公分):')
w = float(w)
h = float(h)
h = h/100
b = w/h/h
if b < 18.5:
    print('您的BMI值為:', b, '您的體重過輕')
elif b < 24:
    print('您的BMI值為:', b, '您的體重正常')
elif b < 27:
    print('您的BMI值為:', b, '您為輕度肥胖')
elif b < 30:
    print('您的BMI值為:', b, '您為中度肥胖')
else:
    print('您的BMI值為:', b, '您為重度肥胖')
bbbbb