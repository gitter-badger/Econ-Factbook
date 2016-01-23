# Data Pipeline

Add Pipelines to get the most recent data from the Worldbank API.

Use a Makefile to get the data from the API, transform the resulting json with `jq` and convert the json from `jq` to csv using `csvkit`

The Makefile makes it easier to repeat the process and to only get the most recent data.


## Pipelines

### Population

Get the population data from the worldbank api
