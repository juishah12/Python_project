def table_print(n):
 for count in range(1,21):
     ans = count*n
     print(n, "X", count, "=", ans)
     if(ans%2 == 0):
         print("even number",ans)
     else:
         print("odd number", ans)




table_print(3)