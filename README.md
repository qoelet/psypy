# psypy #

## a collection of ciphers as Python functions ##

Spending sometime with the topic of cryptography, and writing what I'm learning in Python. Feel free to fork and contribute more! These are purely recreational and BROKEN - definitely not to be used in real life applications.

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

### salsa20 ###

[PureSalsa20][3] - an implementation in Python 2.5

[1]:http://www.shmoocon.org/2012/videos/Agre-CoolNewCrypto.m4v
[2]:https://github.com/jfdm/pyPEBEL
[3]:http://www.tiac.net/~sw/2010/02/PureSalsa20/pureSalsa20.py