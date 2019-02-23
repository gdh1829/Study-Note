Difference between assignment operations in R
===
※ Retyped to remember and understand this subject from the following article
Reference [Difference between assignment operations in R article](https://renkun.me/2014/01/28/difference-between-assignment-operators-in-r/)

## __Google's R Style Guide says "Use <-, not =, for assignment."__
```R
    #GOOD 
    x <- 5
    #BAD:
    x = 5
```

## But WHY?
First, let's take a look at an example.
```R
x <- rnorm(100)
x
y <- 2*x + rnorm(100)
y

?lm
lm(formula = y~x)

```
The above code uses both <- and = symbols, but the work they do are different. <- in the first two lines are used as __assignment operator__ while = in the third line does not serves as assignment operator but an operator that specifies a named parameter `formula` for `lm` function.  

In other words, <- evaluates the expression on its right side `(rnorm(100))` and assign the evaluated value to the symbol (variable) on the left side `(x)` in the current environment. = evaluates the expression on its right side `(y~x)` and set the evaluated value to the parameter of the name specified on the left side `(formular)` for a certain function.  

We know that `<-` and `=` are perfectly equivalent when they are used as assignment operators.  

Therefore, the above code is equivalent to the following code:  
```R
x = rnorm(100)
y = 2*x + rnorm(100)
lm(formula=y~x)
```
Here, we only use = but for two different purposes: in the first and second lines we use = as assignment operator and in the third line we use = as a specifier of named parameter.  

Now, let's see what happens if we change all = symbols to <-.  
```R
x <- rnorm(100)
y <- 2*x + rnorm(100)
lm(formula <- y~x)
```
If you run this code, you will find that the output are similar. But if you inspect the environment, you will observe the difference: a new variable `formular` is defined in the environment whose value is `y~x`. So what happens?  

Actually, in the third line, two things happened: First, we introduce a new symbol (variable) `formular` to the environment and assign it a formular-typed value `y~x`. Then, teh value of `formular` is provided to the __first parameter__ of function `lm` rather than, accurately speaking, to the __parameter named `formular`__, although this time they mean the identical parameter of the function.  

To test it, we conduct an experiment. This time we first prepare the data.  
```R
x <- rnorm(100)
y <- 2*x+rnorm(100)
z <- 3*x+rnorm(100)
data <- data.frame(z,x,y)
rm(x,y,z)
```
Basically, we just did similar things as before except that we store all vectors in a data frame and clear those numeric vectors from the environment. We know taht `lm` function accepts a data frame as the data source when a formular is specified.  

Standard usage:
```R
lm(formular=z~x+y, data=data)
```
Working alternative where two named parameters are reordered:
```R
lm(data=data, formular=z~x+y)
```
Working alternative with side effects that two new variable are defined:
```R
lm(formular<-z~x+y, data<-data)
```
Nonworking example:
```R
lm(data<-data, formular<-z~x+y)
```
The reason is exactly what I mentioned previously. We reassign `data` to `data` and give its value to the first argument `(formular)` of `lm` which only accepts a formular-typed value. We also try to assign `z~x+y` to a new variable `formular` and give it to the second argument `(data)` of `lm` which only accepts a data frame-typed value. Both types of the parameter we provide to `lm` are wrong, so we receive the message:  
>Error in as.data.frame.default(data) :  
    cannot coerce class ""formula"" to a data.frame  
From the above examples and experiments, the bottom line gets clear: to reduce ambiguity, we should use either <- or = as assignment operator, and only use = as named-paramter specifier for functions.  

In conlusion, for better readability of R code, it is suggested that we only use <- for assignment and = for specifying named parameters.