def factoriel(n):
  #n*(n-1)*...1
  #n*(factoriel(n-1))
  if n>1:
    result= n*factoriel(n-1)
    return result
  else:
    return 1


factoriel(5)