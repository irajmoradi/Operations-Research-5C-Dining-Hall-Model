set Days;
set Halls;
set Restrictions;
set Meals;
set Locations;

#Research Inputted:
param waitTime{Meals, Halls} >= 0;
param options{Meals, Restrictions, Halls} >= 0;
param quality{Meals, Restrictions, Halls} >= 0;
param proximity{Halls, Locations} >= 0;
param mealExists{Days, Meals} >= 0;

#Student Inputted:
param preMealLocation{Days, Meals, Locations} >= 0;
param postMealLocation{Days, Meals, Locations} >= 0;
param rushFactor{Days, Meals} >= 0;
param varietyFactor{Meals} >= 0;
param dailyVarietyFactor >= 0;
param restrictionActual{Restrictions} >= 0;
param mealImportance{Meals} >= 0;

#Main Decision Variable:
var whereToGo{Days, Halls, Meals} >= 0;

#Supplementary Fixed Variables:
var qualityScore{Halls, Meals} >= 0;
var choicesScore{Halls, Meals} >= 0;
var walkTime{Days, Halls, Meals} >= 0;
var timeCrunch{Days, Halls, Meals};
var overallMealQuality{Days, Halls, Meals};

#Note: Only looking at times within our timeframe, so no incentive for imaginary job starts at negative times.
maximize diningHallScheduleEnjoyment:
sum{d in Days, h in Halls, m in Meals} (whereToGo[d,h,m] * overallMealQuality[d,h,m]);

subject to qualityScoreCalculation{h in Halls, m in Meals}:
qualityScore[h,m] = sum{r in Restrictions} quality[m,r,h] * restrictionActual[r] * mealImportance[m];

subject to choicesScoreCalculation{h in Halls, m in Meals}:
choicesScore[h,m] = (sum{r in Restrictions} (options[m,r,h] * restrictionActual[r])) / (1 + sum{r in Restrictions} (options[m,r,h] * restrictionActual[r]));

subject to walkTimeCalculation{d in Days, h in Halls, m in Meals}:
walkTime[d,h,m] = sum{l in Locations} (proximity[h,l] * (preMealLocation[d,m,l] + postMealLocation[d,m,l]));

subject to timeCrunchCalculation{d in Days, h in Halls, m in Meals}:
(1 - timeCrunch[d,h,m]) * rushFactor[d,m] = (walkTime[d,h,m] + waitTime[m,h]);

subject to overallMealTimeQualityCalculation{d in Days, h in Halls, m in Meals}:
overallMealQuality[d,h,m] = (timeCrunch[d,h,m] * choicesScore[h,m] * qualityScore[h,m]);

subject to mealAssignmentRestriction{d in Days, m in Meals}:
sum{h in Halls} whereToGo[d,h,m] = mealExists[d,m];

subject to varietyRestriction{h in Halls, m in Meals}:
sum{d in Days} whereToGo[d,h,m] <= 1.2 + (((sum{d in Days} mealExists[d,m])-1) * (10 - varietyFactor[m]) / 10);

subject to daysVarietyRestriction{h in Halls, d in Days}:
sum{m in Meals} whereToGo[d,h,m] <= 1 + (((sum{m in Meals} mealExists[d,m])-1) * (10 - dailyVarietyFactor) / 10);