
##A
~~~

s2 = 0
s3 = s0

while s3 != 0:
    s2 += s1
    s3 -= 1

~~~

##B
This code effectively multiplies s1 and s0 and stores this in s2. It does through adding s1 to s2 in a loop repeated s0 times.

##C
~~~

s2 = 0
s1 = 1

while s0 != 0:
    s2 = 0
    s3 = s0

    while s3 != 0:
        s2 += s1
        s3 -= 1

    s1 = s2
    s0 -= 1

~~~
##D

The code multiplies s1 by s3 stores it in s2, then takes away 1 from s3 and multiplies s3 and s1 again adding the result to s2. It repeats this process 
a total of s3 times.

##E
~~~

	addi $s0, $zero, 10
	addi $s1, $zero, 1

loop:	mult $s1, $s1, $s0
	addi $s0, $s0, -1
	bne $s0, $zero, loop

~~~

