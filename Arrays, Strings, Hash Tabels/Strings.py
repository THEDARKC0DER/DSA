# Far from being simple sequences of characters, strings offer a rich landscape for
#  developers to explore concepts like data encoding, pattern matching, 
# and efficient memory management.

# At its core, a string is an immutable sequence of characters.

# Key Characteristics
# Sequential Data: 
# Encoding:  UTF-8 is the most common modern standard

# Immutability means that once a string object is created, its value cannot be changed. 
# Any operation that appears to modify a string, such as concatenation or 
# character replacement, actually results in the creation of an entirely new string object 
# in memory. The original string remains untouched.


# How Strings are Stored
# Heap Memory: 
# String Constant Pool/Interning: (IMP) Article on medium by me
a = "hello"
b = "hello"

print(a is b)  # Often True
# True because of string constant pool...

# Why Immutability Matters:
# Thread Safety:
# Performance and Optimization: 
# Security





Compile Time vs Runtime — The Theory
1️⃣ Compile Time

Compile time is the phase where:

Your source code is converted into bytecode (in Java).

The compiler checks syntax errors.

Certain optimizations are performed.

Some expressions are evaluated early.

In Java, this is handled by the Java compiler (javac).

If something can be determined before the program runs, it happens at compile time.

2️⃣ Runtime

Runtime is when:

The program is actually executed by the JVM.

Memory is allocated.

Objects are created.

Variables get real values.

If something depends on a value that is only known when the program runs, it happens at runtime.