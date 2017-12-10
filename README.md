# Redis Keys Analysis

This repository contains all the scripts necessary to keep track of the keys that Internet-accessible Redis servers are using. This can reveal whether anybody's currently compromising Redis databases across the Internet.

## Requirements

The project is managed using [pipenv](https://docs.pipenv.org/) and if you have it installed you can simply run the following from the project directory:

    pipenv install

The only requirement at the moment though is the **shodan** Python package so you may also install it using pip/ easy_install:

    easy_install shodan

The **shodan** Python package also includes the [Shodan CLI](https://cli.shodan.io) which is what the **grab-data.sh** script uses for downloading all public Redis servers. Make sure you've initialized the Shodan CLI before running **grab-data.sh**. You can find your API key from the [Shodan accounts page](https://account.shodan.io) or the [Developer dashboard](https://developer.shodan.io/dashboard):

    shodan init YOUR_API_KEY

## Usage

The **grab-data.sh** script downloads a list of public Redis servers and stores the data in a file called **redis.json.gz**. This Shodan data file is then processed using the **keys.py** script which will print a list of the top 20 most common Redis keys.

1. ./grab-data.sh
2. python keys.py redis.json.gz

Here is a sample output of the script:

    Top 20 Redis Keys

    #1	crackit                       	5639
    #2	1                             	375
    #3	xemvlk                        	94
    #4	processes                     	77
    #5	stat:failed                   	77
    #6	zrfdyh                        	76
    #7	stat:processed                	74
    #8	qwe                           	66
    #9	name                          	52
    #10	godkey                        	49
    #11	unacked_mutex                 	45
    #12	queues                        	44
    #13	abc                           	43
    #14	_kombu.binding.celery         	43
    #15	test                          	41
    #16	converter_units               	41
    #17	xcvcbre                       	37
    #18	asdfasfoqwerq33               	36
    #19	foo                           	34
    #20	_kombu.binding.celeryev       	34

This shows that the most common key name in Redis databases is **crackit** which is an indication that those instances have been compromised.