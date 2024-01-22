import textstat

#The Flesch Reading Ease gives a text a score between 1 and 100, with 100 being the highest readability score
f_reading_ease = lambda text:  textstat.flesch_reading_ease(text)

#The Gunning Fog formula generates a grade level between 0 and 20. It estimates the education level required to understand the text.
g_fog = lambda text : textstat.gunning_fog(text)