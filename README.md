# Onset of the Rainy Season (ORS) in West Africa

This repository provides the code for the Fuzzy-ORS definition used in Rauch et al. (2019) as follows:
1. The ORS is defined as the first day of the year in which the following three conditions occur simultaneously:
2. The accumulated sum of precipitation in five consecutive days is at least 25 mm.
3. Within this pentad, at least two more days must exceed a precipitation amount of 1 mm.
There is no period of consecutive 7 dry days or longer within the next 30 days (false start criterion). A dry day is defined as a day with less than 1 mm precipitation.

A shortcoming of the approach this is its binary logic. An accumulated precipitation sum of 24.9 mm is not identified as the onset of the rainy season although only 0.1 mm is missing to fulfill the criteria. Since many other ORS approaches rely on binary logics, Laux et al. (2008) introduced fuzzy rules for a more smoothed transition of the applied conditions. The membership functions of the fuzzy rules used in this study are shown in Figure 5 in Rauch et al. (2019)

Fo  example, for condition 1, accumulated precipitation amounts of less than 18 mm receives a membership value of 0, and above 25 mm a 1. In the range between 18 and 25 mm, normalized values between 0 and 1 are assigned by linear interpolation. Thus, the probabilities of being interpreted as ORS are increasing with precipitation rates larger than 18 mm. A similar membership function is applied to condition 2, which is supposed to exclude single rainfall events to be misinterpreted as ORS. It must be noted that the membership functions were optimized for the Volta Basin of West Africa. It is necessary to fit the parameters for the target region!

In the script "example.py", an example for one time series is shown.
