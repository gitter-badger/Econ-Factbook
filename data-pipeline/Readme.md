# Data Pipeline

Add Pipelines to get the most recent data from the Worldbank API.

Use a Makefile to get the data from the API, transform the resulting json with `jq` and convert the json from `jq` to csv using `csvkit`

The Makefile makes it easier to repeat the process and to only get the most recent data.

## Installation

You need to install a few packages before you can use this pipeline.
#### CSVKit

Run `pip install -r requirements.txt` to install the python packages. ( Yes you need to have python installed. )

### jq

`brew install jq` if you are on a Mac and have homebrew

`apt-get install jq` if you are on Ubuntu

Otherwise check https://stedolan.github.io/jq/download/

## Pipelines

### Population

Get the population data from the worldbank api
