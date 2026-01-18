cities = {
    "Ambala": {
        "Country": "India",
        "Population": "About 2.9 lakh",
        "Fact": "Ambala is a major trade and transport hub, known for its grain, cotton and sugar markets and strong roadrail connectivity between Delhi and Amritsar.",
    },
    "Ahmedabad": {
        "Country": "India",
        "Population": "About 92.7 lakh",
        "Fact": "Ahmedabad is a major industrial and cultural center, historically called the “Manchester of India” for its textile industry and home to Mahatma Gandhi's Sabarmati Ashram.",
    },
    "Mumbai": {
        "Country": "India",
        "Population": "About 1.84 crore",
        "Fact": "Mumbai is the financial capital of India and the heart of the Hindi film industry, popularly known as Bollywood, and was officially renamed from Bombay in 1995.",
    },
}

for city, city_info in cities.items():
    print(f"\n{city}")
    for cat, value in city_info.items():
        print(f"\t{cat}: {value}")