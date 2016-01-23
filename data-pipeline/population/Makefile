GENERATED_FILES = population.csv
.PHONY: all

all: $(GENERATED_FILES)

.INTERMEDIATE: pop.json
pop.json:
	curl -o $@ "http://api.worldbank.org/countries/all/indicators/SP.POP.TOTL?date=2014:2014&per_page=20000&format=json"

.INTERMEDIATE: population.json
population.json: pop.json
	cat $< | jq '[.[1] | .[] | { country_code: .country.id, country_name: .country.value, population: .value, date: .date }]' > $@

population.csv: population.json
	in2csv $< > $@
