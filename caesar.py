alph = "abcdefghijklmnopqrstuvwxyz"

def oldcaesar(word,shift):
  c = [alph[(alph.index(l)+shift)%26] for l in word.lower()]
  return "".join(c)

scrablets = "aeilnorstudgbcmpfhvwykjxqz 1234567890"
scrabscrs = "111111111122333344444588xx00000000000"

def sn(st):
  if st.lower()=="x":
    return 10
  else: 
    return int(st)


def scrabscr(word):
  return sum([sn(scrabscrs[scrablets.index(l)]) for l in word.lower()])

def score_counts(score,mylist):
  return [[i,len([x for x in mylist if score(x)==i])] for i in xrange(max([score(x) for x in mylist])+1) if len([x for x in mylist if score(x)==i])!=0]





def alph_offset(alph,l):
  alphl = alph.lower()
  ll = l.lower()
  return alphl.find(ll)

def caesar(string,key,decrypt=True):
  alph = "abcdefghijklmnopqrstuvwxyz"
  ciph_offset = alph_offset(alph,key)
  if decrypt:
    output = "".join([alph[(alph_offset(alph,l)-ciph_offset)%26] for l in string])
  else:
    output = "".join([alph[(alph_offset(alph,l)+ciph_offset)%26] for l in string])
  return output


def vigenere(string, key, decrypt=True):
  output = ""
  for i in xrange(len(string)):
    keyl = key[i%len(key)]
    output = output + caesar(string[i],keyl,decrypt)
  return output

import subprocess

greekalphnames = "alpha,beta,gamma,delta,epsilon,zeta,eta,theta,iota,kappa,lambda,mu,nu,xi,omicron,pi,rho,sigma,tau,upsilon,phi,chi,psi,omega".split(",")

phonenums = "22233344455566677778889999"
def phone_l2n(word):
  pd = {}
  for [l,k] in zip(alph,phonenums):
    phonedict[l]=k
  return "".join([phonedict[l] for l in word.lower()])

def dict_lookup(w,prefix=True,suffix=True,
                dct="/usr/share/dict/words"):
  if prefix:
    w = "^"+w
  if suffix:
    w = w+"$"
  pro = subprocess.Popen(["grep","-i",w,dct],stdout=subprocess.PIPE)
  res = pro.communicate()[0].split("\n")
  return res[:-1]

def parse12(x,maxn=26):
  if len(x)==0:
    return []
  if len(x)<=2:
    ret = []
    if int(x)<=maxn:
      ret = ret + [[int(x)]]
    if len(x)==2:
      ret = ret + [[int(x[k]) for k in [0,1] if int(x[k])<maxn]]
    return ret
  x0 = int(x[0])
  x01 = int(x[:2])
  a = []
  if x0<maxn:
    a = [[x0]+y for y in parse12(x[1:],maxn)]
  b = []
  if x01<maxn:
    b = [[x01]+y for y in parse12(x[2:],maxn)]
  return a+b

def onetwo_revalph(x):
  parses = parse12(x,26)
  rets = []
  for p in parses:
    s = [alph[26-i-1] for i in p]
    t = "".join(s)
    rets.append(t)
  return rets

def dict_revalph(x):
  possws = onetwo_revalph(x)
  return [w for w in possws if dict_lookup(w)]

pss = [1,2,3,4,5,8,10]

def parse12_fromlist(x,fromlist=pss):
  if len(x)==0:
    return []
  if len(x)<=2:
    ret = []
    if int(x[0])!=0 and int(x) in fromlist:
      ret = ret + [[int(x)]]
    if len(x)==2 and int(x[0]) in fromlist and int(x[1]) in fromlist:
      ret = ret + [[int(x[0]),int(x[1])]]
    return ret
  x0 = int(x[0])
  x01 = int(x[:2])
  a = []
  if x0 in fromlist:
    a = [[x0]+y for y in parse12_fromlist(x[1:],fromlist)]
  b = []
  if x0!=0 and x01 in fromlist:
    b = [[x01]+y for y in parse12_fromlist(x[2:],fromlist)]
  return a+b

def make_all_trans_from_list(l,d):
  x = d.get(l[0],"")
  if len(l)<=1:
    return [dd for dd in x]
  y = make_all_trans_from_list(l[1:],d)
  rets = []
  for dd in x:
    rets += [dd + yy for yy in y]
  return rets

scrabnums = [1]*10 + [2]*2 + [3]*4 + [4]*5 + [5]+ [8]*2 + [10]*2
scrablets = "aeilnorstudgbcmpfhvwykjxqz"

def onetwo_scrabscores(x):
  parses = parse12_fromlist(x,pss)
  scrabdict = {}
  for i in xrange(11):
    scrabdict[i] = ""
  for [k,l] in zip(scrabnums,scrablets):
    scrabdict[k]+=l
  posswords = []
  for p in parses:
    posswords += make_all_trans_from_list(p,scrabdict)
  posswords = sorted(list(set(posswords)))
  return posswords

def dict_scrabscores(x):
  possws = onetwo_scrabscores(x)
  return [p for p in possws if dict_lookup(p)]


keycols = ['p','qaz','wsx','edc','rfv','tgb','yhn','ujm','ik','ol']
kcd = {}
for i in xrange(10):
  kcd[i] = keycols[i]

def dict_keycols(x,lookup=True):
  parses = parse12_fromlist(x,range(10))
  pws = []
  for p in parses:
    pw += make_all_trans_from_list(p,kcd)
  pws = sorted(list(set(pws)))
  if lookup:
    return [p for p in pws if dict_lookup(p)]
  return pws

qwerty_alph = "qwertyuiopasdfghjklzxcvbnm"
qd = {}
for i in xrange(26):
  qd[i+1]=qwerty_alph[i]

def dict_qwerty(x,lookup=True):
  parses = parse12(x,26)
  pws = []
  for p in parses:
    pws += make_all_trans_from_list(p,qd)
  pws = sorted(list(set(pws)))
  if lookup:
    return [p for p in pws if dict_lookup(p)]
  return pws

def make_check_trans_from_list(l,d):
  x = d.get(l[-1],"")
  if len(l)<=1:
    return [dd for dd in x if dict_lookup(dd,suffix=False)]
  y = make_check_trans_from_list(l[:-1],d)
  rets = []
  for dd in x:
    rets += [yy+dd for yy in y if dict_lookup(yy+dd,suffix=False)]
  return rets

sd = {}
for i in pss:
  sd[i]=""
for [k,l] in zip(scrabnums,scrablets):
  sd[k]+=l
print(sd)


def dict_build_scrabscores(x,look=True):
  parses = parse12_fromlist(x,pss)
  pws = []
  for p in parses:
    pws += make_check_trans_from_list(p,sd)
  pws = sorted(list(set(pws)))
  if look:
    return [p for p in pws if dict_lookup(p)]
  return pws

def dict_build_anyscores(x,d,look=True):
  parses = parse12_fromlist(x,d.keys())
  pws = []
  for p in parses:
    pws += make_check_trans_from_list(p,d)
  pws = sorted(list(set(pws)))
  if look:
    return [p for p in pws if dict_lookup(p)]
  return pws

pl = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
pd = {}
for i in range(2,10):
  pd[i]=pl[i-2]

def make_re(x,d):
  re = ""
  for y in x:
    z = d.get(y,"")
    if z:
      re += "["+z+"]"
    else:
      return ""
  return re

def dict_grep_anyscores(x,d,dct):
  parses = parse12_fromlist(x,d.keys())
  pws = []
  for p in parses:
    gs = make_re(p,d)
    pws += dict_lookup(gs,dct=dct)
  pws = sorted(list(set(pws)))
  return pws


def sortby(s,b):
  return [s[b.index(x)] for x in sorted(b)]

def rev_each(l):
  return [x[-1::-1] for x in l]


def parse_fromlist(x,fromlist=pss):
  if len(x)==0:
    return []
  if int(x[0])==0:
    return []
  ret = []
  if int(x) in fromlist:
    ret = ret + [[int(x)]]
  if len(x)==1:
    return ret
  print x
  for i in xrange(2,len(x)+1):
    p = x[:i]
    s = x[i:]
    if int(p) in fromlist:
      ret = ret + [[int(p)]+y for y in parse_fromlist(s)]
  return ret

nato = ['ALPHA','BRAVO','CHARLIE','DELTA','ECHO','FOXTROT','GOLF',
        'HOTEL','INDIA','JULIET','KILO','LIMA','MIKE','NOVEMBER',
        'OSCAR','PAPA','QUEBEC','ROMEO','SIERRA','TANGO',
        'UNIFORM','VICTOR','WHISKEY','XRAY','YANKEE','ZULU']
