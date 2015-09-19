#! /usr/bin/env python
import random as r
merge=lambda m:(filter(int,reduce(lambda x,y:x+[y]*(y>0)if x[-1]-y else x[:-1]+[y*2,0],m,[0]))+[0]*9)[:len(m)]
def e(g):g[:]=[r[::-1]for r in g]
def t(g):g[:]=map(list,zip(*g))
class TwentyFortyEight:
 def __init__(s,h,w):s.h=h;s.w=w;s.z=s.new_tile;s.reset()
 def reset(s):s.g=[s.w*[0]for _ in range(s.h)];s.z();s.z()
 def get_grid_height(s):return s.h
 def get_grid_width(s):return s.w
 def move(s,d):
  if d==3:
   g=s.g;s.g=map(merge,s.g)
   if g!=s.g:s.z()
  elif d>3:e(s.g);s.move(3);e(s.g)
  else:t(s.g);s.move(2+d);t(s.g)
 def new_tile(s):s.set_tile(*r.choice([(i,j)for i,l in enumerate(s.g)for j in range(len(l))if l[j]==0]),v=2+2*(r.random()<.1))
 def set_tile(s,r,c,v):s.g[r][c]=v
 def get_tile(s,r,c):return s.g[r][c]
