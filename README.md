# psypy #

## a collection of ciphers as Python functions ##

Spending sometime with the topic of cryptography, and writing what I'm learning in Python. Feel free to fork and contribute more!

## ciphers ##

example,

    from psypy.ciphers.caesar import encrypt
  
    print encrypt("hello there!")
  
## layout ##

Right now as I read about any ciphers, they'll be added to the ciphers folder. Some misc scripts can be found in the tools folder.

## resources ##

### predicate encryption ###

Ben Agre's "[Cool New Crypto][1]" talk from Shmoocon 2012 (video)

[PyPEBEL][2] 

[1]:http://www.shmoocon.org/2012/videos/Agre-CoolNewCrypto.m4v
[2]:https://github.com/jfdm/pyPEBEL