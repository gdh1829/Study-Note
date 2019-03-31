Boxing and Unboxing
===

This is Java terms  

`Boxing` means to change a primitive type value into a Wrapper class and `Unboxing` is the opposite concept.  
Boxed values are stored in heap memory because it is an instance.  

int => boxing => Integer  
int <= unboxing <= Integer  

There are also `auto-boxing/unboxing` that Java automatically offers.  
For example,  
Auto-boxing  
```java
int sample = 7;
Integer boxedSample = sample; //auto-boxing
```

Auto-unboxing  
```java
Integer boxedSample = new Integer(7);
int autoUnboxedSum = boxedSample + 13; //auto-unboxing
```

**Why do we need Wrapper classes and boxing?**  
In many places like Generic, data structure, arguments or sth, they don't require primitive types but reference types. Also Wrapper classes have various convenient methods unlike the primitves and can be used in various ways.  