# softwareArt-project-1

# Make History - Don't Trust What You Read Online 👀
---

## What is it?

My project is a **fake history** textbook generator that is presented on the web. 

Using three different Python algorithms, I have completed a rough timeline of the history of K*zakh-stan (real country names are excluded :D). The text output is a narrative that describes different events based on the real or generated events happening in random parts of the planet during the given time period.

The concept behind this project is to demonstrate how (relatively) easy it is to generate fake history and news and present them online to the public. What I want to say with my work is that **we should not blindly trust what we read online** -- especially during the pandemic, when the rise of fake news is so high.

## How it's made?

The algorithms used for the text-generator are made (1) utilizing the `random` library, (2) HTML parsing of open-source websites with the `BeatifulSoup` and `requests` libraries, and (3) regular expression and string manipulation in Python. Here is the explanatin of each underlying algorithm: 

  (1). I have created multiple string lists and sentences. When I print the sentence, the program randomly chooses one of the strings from the lists to complete the text.

  (2). I have used several websites with history books on the Gutenberg Project, song lyrics, and travel blogs to scrape the necessary information for the text output.

  (3). After scraping some of the information from the web, I have used regular expression and string manipulation to modify the text and generate new output.

## Why it's made?

  One of the most noticeable traits is that the text output might look like a real history timeline to people unfamiliar with the country, and this is the effect I was trying to achieve. The website, however, serves to warn the reader that the information might be misleading, prompting the reader to stop and reflect.

In the age when so many resources are available to us online, I believe it is a crucial step to be able to stop for a moment and critically analyze the information consumed.
