# Research Questions
## How Have Terrorist Attacks Changed Over the Years?
> Authors: Kezhao Jiang, Vitaliy Kaparchuk


#### Research Questions
---
1. Are there any points in time from which the number of terrorist attacks dramatically increase? If there are, we want to find out exactly what was going on at this specific point in time to cause the large change, such as the beginning of a war or a period of poor national relations, or some other event. This question would look at longer intervals, such as years, unlike the intra-year trends of Question 4.
	- **Answer**: There were two years where the number of attacks drastically increased. These years were 2004 and 2011. Although the number increased following these two years, the increase was much more pronounced in 2011.

2. How have the types of attacks (bombings, assassinations, hijacking, etc.) changed over time? With different conflicts and different periods in time, there seem to be types of attacks that are more common than others. We might even be able to see if a new kind of terrorist attack is beginning to happen more frequently.
	- **Answer**: Although bombings and armed assaults have always been the most common attacks, in the past decade and half they have both increased to many times their previous values.

3. What is the relationship between different regions and the number of attacks that happen there? We know that regions like the Middle East tend to have a high number of terrorist attacks, but there could be other regions that have a lot of incidents that we generally don’t hear about, or regions that have seen a rise in attacks in recent years.
	- **Answer**: The year is a large factor in the relationship between the locations of attacks. Over the years, the locations of concentrated attacks has moved all over the world.

4. Does the time of year have an effect on the number or type of attacks? It would be very interesting if there appeared to be a correlation between this. Instead of the attacks being completely random, there might be times of the year where they happen more often.
	- **Answer**: Looking at each individual year there is no pattern. In the total counts, however, we see that more attacks happen in the Northern Hemisphere spring and decrease in the Northern Hemisphere winter.

#### Motivation and Background
---

These questions and the accompanying visualizations will allow us to observe what variables or events have an influence on the amount and kind of terrorist attacks that happen. We might be able to narrow down to specific types of events that increase the amount of attacks, to see what kinds of events or variables we need to watch out for in the present day. Knowing how these variables affect the amount and types of attacks can help us be better prepared, or at at least anticipate what can happen, if similar events happen again.

#### Dataset
---

The dataset that we are using is the Global Terrorism Database. It is provided by the University of Maryland. The data for the events goes back from 1970 to the end of 2017, with 181,692 total events. Each row is a single event that contains information about each event such as the time (year, month, day), the place (region, country, state, city, specific location), the latitude and longitude, a summary of the event, the attack type, and the targets. It also has the organization or group that the attacker(s) belonged to, their motives, the weapons used, damage caused, and the outcome, along with other information about the event. The dataset has all the information we would need for our research questions, and plenty of other data if we decide or need to change a question. The dataset also comes with a codebook that contains information on each individual column in the table. It also comes with a geodatabase folder which contains all the shape files necessary for creating a map for the dataset.

URL: https://www.start.umd.edu/gtd/contact/

#### Methodology
---

Make one or several plots for each question:

    1. Plot the total number of attacks over the years and find any times where they drastically increased. We can then see what major events happened around that time that may have had a direct influence on the number of attacks.
    2. Separate the attacks into several major types and make a plot that contains a line for each different kind of attack. We can then try to see things like if any kind of attack is “disappearing”, if a certain kind of attack is increasing in number, or how the overall amount of different types compare to each other.
    3. Use geographical data to visualize the number of attacks using a heat map, possibly in different years as well, and see what places tend to have more attacks, or places that have a lot of attacks that we don’t hear about.
    4. Plot data where the timeframe of the plot is a single year, possibly plotting several years on the same graph and observing whether certain times of the year can have an influence on attacks. It doesn’t seem like something that could have an effect but it would be very interesting if we did see a pattern.

We are planning on adding interactivity for the plots as well, where the variables in the plots can be changed by a user so that the relationship between two chosen variables can be observed.

#### Results

1. From 1970 to 2017, there were two years where the number of attacks drastically increased from their previous levels. These two years were 2004 and 2011. After 2004, the total number of attacks quadrupled in just four years, going from about 1200 to 4800 total attacks in 2008. We looked at the major news headlines and events from 2004 and surrounding years saw that this coincided with the fact that the Iraq War had begun the year before and then American troops were withdrawn in 2009, which was the span of years where the attacks quadrupled. The other major year was 2011, where attacks tripled from about 5000 to almost 17000 in just three years. Looking at the major events in 2011, we saw that this was the year that the civil war began in Syria. This contributed to a huge rise in the number of attacks, especially when this conflict began overflowing into other neighboring countries like Iraq, making the situation much worse. Although we didn’t focus on times where the number of attacks declined, since the end of 2014 the number of attacks has been sharply decreasing (up to 2017, which is where our dataset ends).


2. We had data for nine different types of attacks, including bombings, armed assault, hostage taking, infrastructure attacks, and others. Basically all of the types of attacks followed the global trend in rises and falls discussed in the results to the first question, although to very different degrees. Interesting points in time include several years in the 1970s where assassinations were the most common type of attack in the world, surpassing armed assaults and even bombings. Assassinations now rank 5th in the most common types of attacks. Hostage taking went from 5th most common to 3rd most common, seeing a large rise in the past decade. However, there are two types of attacks that have easily surpassed all others. In the past two decades, we have seen a very large separation in the number of bombings and armed assaults compared to all the other types of attacks. These two types of attacks have gone up by over 10 times their previous amounts less than two decades ago, and now easily make up the majority of all attacks, comprising about 75% of all recorded events in 2014.

3. We see that throughout the years, the locations of concentrated attacks change quite a bit. Attacks happen in almost every country, although some countries and regions definitely see more attacks than others. What was interesting was the locations of concentrated attacks seems to change continents just about every decade, as different regions experience different periods of violence and instability. In the 1970s, the location of the majority of all attacks happened in Europe and the United States, mostly events on the local level with political, social, and racial groups coming into conflict with each other. For most of the 1980s, the location of concentrated attacks moved almost exclusively to South America, with attacks appearing in South Asia towards the end of the 1980s and continuing into the 1990s. The 1990s saw terrorism events appear all over the world with no specific locations, and this continued into the early 2000s. For the last decade and a half, the locations of almost all attacks now take place in Iraq and the areas surrounding Pakistan and India.

4. When we looked at the trend of attacks per month in every year, there wasn’t a pattern or trend that particularly stood out. We didn’t really expect there to be much correlation with the number of attacks and the time of year, but when we graphed the total number of attacks per month there was an interesting trend that we saw. There appear to be more total attacks that have happened in the Northern Hemisphere spring, and less attacks in the Northern Hemisphere winter. When we look at the counts, we can see that 25% more attacks have occured in May compared to December, the high and low points of the graph (16,875 attacks compared 13,496). We have found no reason for this trend to be significant, and it is entirely possible that this is due to chance, or there may have been a few years with a very large number of events in one month that caused this “trend” to appear. Even so, it was quite interesting to see this.

#### Reproducing Results

We used the Bokeh interactive visualization library to create tabs with interactive plots that can be placed on a page that is hosted on your local server. The project was done with GitHub so the client can clone the repository and host the webpage on their own machine to interact with the plots.
    - Steps:
        1. __Client needs to be using Python version 3.7.3 and install pandas, geopandas, and pandas_bokeh using the following commands in their terminal__:
            - conda install bokeh
            - conda install pandas
            - conda install geopandas
            - pip install pandas_bokeh (pandas_bokeh library can only be installed by pip)
        2. __Clone the repository__:
	        - git clone https://github.com/kz9/cse163-project.git
        3. __Go into the bokeh_app directory and unzip the data.zip file into a folder called database__:
	        - cd cse163-project/bokeh_app/
	        - mkdir database
	        - unzip data.zip -d database/
        4. __Change directory to outside of bokeh_app folder__
	        - cd ..
        5. __Create the local website at the port 5006(localhost:5006/bokeh_app)__
	        - bokeh serve --show bokeh_app
        6. __The webpage will open on your default browser. Please wait for all resources to load__.


#### Work Plan & Evaluation

1. Make the necessary plots for each problem and separate the work through the github issue function.
2. Write a markdown file for each plot and separate the work through github issue function as well.
3. We will use the dash module to organize the plots and markdown files into an interactive website in order to present the data and separate the work through the github as well.
4. Use the video option to create a presentation.

We did not include any estimated times for our work plan, but we can confidently say that any estimates we would have included would have been underestimations, especially for creating the interactivity for the plots. We also changed some things, like changing from the dash library to the bokeh library.

#### Testing

For testing our code, we found that the best way was to plot the data that we have and see whether it corresponds to actual data and events. For example, we know from our research that most of the attacks happening right now are concentrated in Iraq and India/Pakistan, and we plotted to see whether our code was correct and gave us the correct visualization. The interactivity of the page and the animation of the yearly attacks also gave us insight into whether our data manipulation was done correctly, with us being able to change and view different years, and then researching years of interest to see if that’s what was really going on at that time.

#### Presentation Option

We are going to be doing the video option for the final presentation.

#### Collaboration

**Authors**: Vitaliy Kaparchuk, Kezhao Jiang
No other people helped with this project.
