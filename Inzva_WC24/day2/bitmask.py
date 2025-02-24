 #! BITMASK OPERATIONS IN C
#* 1<<1 2 ile çarpmak demek. aslında 1 biti sola kaydırıp oraya ekliyoruz. böylece o bit 2 ile çarpılmış oluyor.
#!!!!!!!!!!! ÇALIŞ BU KONUYA
"""
A mask defines which bits you want to keep, and which bits you want to clear.

Masking is the act of applying a mask to a value. This is accomplished by doing:

Bitwise ANDing in order to extract a subset of the bits in the value
Bitwise ORing in order to set a subset of the bits in the value
Bitwise XORing in order to toggle a subset of the bits in the value
Below is an example of extracting a subset of the bits in the value:

Mask:   00001111b
Value:  01010101b
Applying the mask to the value means that we want to clear the first (higher) 4 bits, and keep the last (lower) 4 bits. Thus we have extracted the lower 4 bits. The result is:

Result: 00000101b
"""

"""
Bitmasking means imposing mask over bits. Here is a bitmasking with AND—

     1 1 1 0 1 1 0 1     input
(&)  0 0 1 1 1 1 0 0      mask
------------------------------
     0 0 1 0 1 1 0 0    output
So, only the middle four bits (as these bits are 1 in this mask) remain.

Lets see this with XOR—

     1 1 1 0 1 1 0 1     input
(^)  0 0 1 1 1 1 0 0      mask
------------------------------
     1 1 0 1 0 0 0 1    output
Now, the middle four bits are flipped (1 became 0, 0 became 1).
"""

"""
Mask:   10000000b
Value:  00000101b
---- OR ---------
Result: 10000101b
Or one could select a particular value from the state by using the AND operator:

Mask:   00001100b
Value:  00000101b
---- AND ---------
Result: 00000100b"""