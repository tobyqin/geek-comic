# geek-comics

Spider to download geek comics and funny programmer pictures.

## project structure

I will struct this project as:

```
root
 |- @download  # comics already downloaded, group by source
 |- geek_downloader # the spider or downloader application
 |_ requirements.txt # project dependencies 

```

## usage

```shell script
pip install -r requirements.txt

# start a scrapy project
scrapy startproject geek_downloader

cd geek_downloader

# create a spider
scrapy genspider turnoffus http://turnoff.us/

# run a spider
scrapy crawl turnoffus

# download the pictures, check the json data and downloader.py ahead
python downloder.py
```

## download source 

- turnoff.us: one of my favourite geek comics site, easy to download.
- geek-and-poke.com: another very good website for geek comics.

## copyright

The site owners and comic authors have the full copyright of the comics, this repo is just for fun, no commercial use allowed.