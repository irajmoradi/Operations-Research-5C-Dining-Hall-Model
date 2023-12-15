# Ops_Research_project



This is a repository containing a python program as well as AMPL files for use in utilizing a linear programming model to help optimize the perfect dining hall schedule for students of the Claremont Colleges. This model was created as part of a group project between Simi, Iraj, and Eli, all students of the Claremont Colleges, for their Math 187 class. 


1. Run the python file in this repo and input your information/preferences regarding dining hall schedule.
2. Open AMPLIDE and open the mod file in the repo as well as the .dat file produced in step one.
3. Run the following commands (You may have to use a open source solver)
```
#Run Program:
reset;
option solver gurobi;
model DiningHallSchedule.mod;
data FileNameHere.dat;
solve;

#To find your optimal schedule:
display whereToGo;

#To find how your schedule scores on a variety of metrics:
#Overall Score
display diningHallScheduleEnjoyment;
#Food Score
display sum{d in Days, h in Halls, m in Meals} (whereToGo[d,h,m] * choicesScore[h,m] * qualityScore[h,m]);
#Time Crunch
display sum{d in Days, h in Halls, m in Meals} (whereToGo[d,h,m] * timeCrunch[d,h,m]);
#Variety Score
display sum{d in Days, h in Halls} ((sum{m in Meals} (whereToGo[d,h,m])) / (1 + sum{m in Meals} (whereToGo[d,h,m]))) + sum{m in Meals, h in Halls} ((sum{d in Days} (whereToGo[d,h,m])) / (1 + sum{d in Days} (whereToGo[d,h,m])));
```
4. Enjoy having a better dining hall schedule.
