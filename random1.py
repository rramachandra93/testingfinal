a = [['###','# #','# #','# #','###'],['#','#','#','#','#'],['###','  #',"###",'#  ','###'],['###','  #','###','  #','###'],['# #','# #','###','  #','  #'],['###','#  ','###','  #','###'],['###','#  ','###','# #','###'],['###','  #','  #','  #','  #'],['###','# #','###','# #','###'],['###','# #','###','  #','###']]
s = input('enter one digit Number')
for k in range(5):
    print()
    for i in s:
       print(a[int(i)][k],end='  ')