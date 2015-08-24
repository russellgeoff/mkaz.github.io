



# grab data from Yahoo
etfc <- read.csv(paste("http://ichart.finance.yahoo.com/table.csv?", "s=ETFC", "&g=m", sep=""))

# save to file
#save(etfc, "etfc.RData")


# now can read in from file
#etfc <- load("etfc.RData")

# verify, show first 5 rows
etfc[1:5,]

# simple plot
plot(etfc$Date, etfc$Close)


# better plotting
library("ggplot2")

qplot(as.Date(Date, "%Y-%m-%d"), Close, data=etfc, geom="line", xlab="", ylab="", colour = I("steelblue4"),fill = I("steelblue4"))


