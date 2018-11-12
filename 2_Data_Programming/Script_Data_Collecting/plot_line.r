#install.packages("ggplot2")
library("ggplot2")
library("scales")

#setwd("c:/Users/daehyeop.ko/Documents/R")
#dataset <- read.csv(file="search_service_sample.csv", header=TRUE, sep=",")
dataset <- read.csv(file="C:/Users/XNOTE/dev/Study-Note/999_samples_for_testing/search_service_sample.csv", header=TRUE, sep=",")

#change data type of 'date' column to Date 
dataset$date <- as.Date(dataset$date)

#drawing ggplot
graph <- ggplot(data=dataset, aes(x=date)) + 
  geom_line(aes(y=max, colour = "max")) + 
  geom_point(aes(y=max, colour="max"), size=3) +
  geom_line(aes(y=X90percentile, colour = "90percentile")) +
  geom_point(aes(y=X90percentile, colour="90percentile"), size=3) +

#set details of x and y scale
graph +
  scale_x_date(breaks = date_breaks("1 day"), labels = date_format("%m/%d")) +
  scale_y_continuous(breaks = seq(0, max(dataset$max)+100, 100), minor_breaks = waiver()) +

#name graph
graph + 
  ggtitle("Search Service Performance") +
  xlab("DATE") +
  ylab("Processing time(ms)") + 
  theme_bw()
  