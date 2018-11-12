data <- c(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,24,26,28,30,32,34,36,38,40)
quantile(data)
min(data)

setwd("c:/Users/daehyeop.ko/Documents/R")
dataset <- read.csv(file="search_service_sample.csv", header=TRUE, sep=",")

dataset$date
mean(dataset$median)
dataset[2]

xrange <- seq(dataset$date[1], dataset$date[nrow(dataset)])
yrange <- seq(min(dataset$median), max(dataset$median))

plot(dataset$date, dataset$median, type="line")
# convert factor to numeric for convenience 
Orange$Tree <- as.numeric(Orange$Tree) 
ntrees <- max(Orange$Tree)

# get the range for the x and y axis 
xrange <- range(dataset$date) 
yrange <- range(dataset$median) 

# set up the plot 
plot(xrange, yrange, type="n", xlab="Age (days)",
     ylab="Circumference (mm)" ) 
colors <- rainbow(ntrees) 
linetype <- c(1:ntrees) 
plotchar <- seq(18,18+ntrees,1)

# add lines 
for (i in 1:ntrees) { 
  tree <- subset(Orange, Tree==i) 
  lines(tree$age, tree$circumference, type="b", lwd=1.5,
        lty=linetype[i], col=colors[i], pch=plotchar[i]) 
} 

# add a title and subtitle 
title("Tree Growth", "example of line plot")

# add a legend 
legend(xrange[1], yrange[2], 1:ntrees, cex=0.8, col=colors,
       pch=plotchar, lty=linetype, title="Tree")