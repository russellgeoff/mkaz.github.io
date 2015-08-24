
library(RMySQL)
library(ggplot2)

 teams = c("BAL","BOS","CHW","CLE","DET","KCR","ANA","MIN","NYY","OAK","SEA","TBD","TEX","TOR",
    "ARI","ATL","CHC","CIN","COL","FLA","HOU","LAD","MIL","NYM","PHI", "PIT", "SDP", "SFG", "STL", "WSN")  

#-- y-axis formatter
y_formatter <- function(x) {
  lab <- paste(x/1000000, "M")
}


con <- dbConnect(dbDriver('MySQL'), 
  user='demo', 
  password = 'demo',
  host = 'localhost',
  dbname = 'baseball')

## ATTENDANCE
for (team in teams) {
  resultSet <- dbSendQuery(con, paste(
    "SELECT W,Attendance,yearID,name
     FROM teams
    WHERE (yearID between 1990 and 2010)
      AND franchID = '", team, "'", sep = ""))


  stats <- fetch(resultSet, n=-1)
  p <- ggplot(stats, aes(x=W, y=Attendance, label=yearID))
  p + geom_point() + geom_text(hjust=0.2, vjust=-0.5, size=2.6) + xlab("Wins") + ylab("Annual Attendance") + opts(title=stats$name) + scale_y_continuous(formatter="y_formatter")
  ggsave(file=paste(team,".png", sep=""))
}


## BATTING AVERAGE from Baseball Hacks by Joseph Adler
library(lattice)

#Build the data set
res<-dbSendQuery(con,
  "select * from batting where yearID=2010 and AB > 250");
batting<-fetch(res, n=-1);
attach(batting);

#Compute batting averages
AVG<-H/AB;

#Plot the charts
histogram(~ AVG | teamID), nint=10
densityplot(~ AVG | teamID), plot.points=FALSE


