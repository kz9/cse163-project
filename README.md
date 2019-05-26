# Research Questions

1. Are there any points in time from which the number of terrorist attacks dramatically increase?
    - If there are, we want to find out exactly what was going on at this specific point in time to
      cause the large change, such as the beginning of a war or a period of poor national relations,
      or some other event. This question would look at longer intervals, such as years, unlike the
      intra-year trends of Question 4.
2. How have the types of attacks (bombings, assassinations, hijacking, etc.) changed over time?
    - With different conflicts and different periods in time, there seem to be types of attacks that
      are more common than others. We might even be able to see if a new kind of terrorist attack is
      beginning to happen more frequently.
3. What is the relationship between different regions and the number of attacks that happen there?
    - We know that regions like the Middle East tend to have a high number of terrorist attacks, but
      there could be other regions that have a lot of incidents that we generally don’t hear about, or
      regions that have seen a rise in attacks in recent years.
4. Does the time of year have an effect on the number or type of attacks?
    - It would be very interesting if there appeared to be a correlation between this. Instead of
      the attacks being completely random, there might be times of the year where they happen more
      often.

## Motivation and Background

It allows people to observe what variables increase and decrease the terrorist attacks so that
people can narrow several variables in order to decrease the terrorist attacks. This report will
make world a better please(something like this?)

## Dataset

The dataset that we are using is the Global Terrorism Database. It is provided by the University
of Maryland. The data for the events goes back from 1970 to the end of 2017, with 181,692 total
events. Each row is a single event that contains information about each event such as the time
(year, month, day), the place (region, country, state, city, specific location), the latitude and
longitude, a summary of the event, the attack type, and the targets. It also has the organization
or group that the attacker(s) belonged to, their motives, the weapons used, damage caused, and
the outcome, along with other information about the event. The dataset has all the information
we would need for our research questions, and plenty of other data if we decide or need to change
a question. The dataset also comes with a codebook that contains information on each individual
column in the table. It also comes with a geodatabase folder which contains all the shape files
necessary for creating a map for the dataset.

URL: https://www.start.umd.edu/gtd/contact/

## Motivation and Background

These questions and the accompanying visualizations will allow us to observe what variables or events have an influence on the amount and kind of terrorist attacks that happen. We might be able to narrow down to specific types of events that increase the amount of attacks, to see what kinds of events or variables we need to watch out for in the present day. Knowing how these variables affect the amount and types of attacks can help us be better prepared, or at at least anticipate what can happen, if similar events happen again.


## Methodology

**Make one or several plots for each question**:
1. Plot the total number of attacks over the years and find any times where they drastically increased. We can then see what major events happened around that time that may have had a direct influence on the number of attacks.
2. Separate the attacks into several major types and make a plot that contains a line for each different kind of attack. We can then try to see things like if any kind of attack is “disappearing”, if a certain kind of attack is increasing in number, or how the overall amount of different types compare to each other.
3. Use geographical data to visualize the number of attacks using a heat map, possibly in different years as well, and see what places tend to have more attacks, or places that have a lot of attacks that we don’t hear about.
4. Plot data where the timeframe of the plot is a single year, possibly plotting several years on the same graph and observing whether certain times of the year can have an influence on attacks. It doesn’t seem like something that could have an effect but it would be very interesting if we did see a pattern.

We are planning on adding interactivity for the plots as well, where the variables in the plots can be changed by a user so that the relationship between two chosen variables can be observed.

## Work Plan

1. Make the necessary plots for each problem and separate the work through the github issue function.
2. Write a markdown file for each plot and separate the work through github issue function as well.
3. We will use the dash module to organize the plots and markdown files into an interactive website in order to present the data and separate the work through the github as well.
4. Use the video option to create a presentation.

