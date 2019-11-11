# geek comics

Spider to download geek comics and fun programmer pictures.

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

## turnoff.us

You will be able to get all the comic from turnoff.us at download folder, I download it via scrapy.∂

## copyright

The site owners and authors have the full copyright of the comics, this repo is just for fun, no commercial use allowed.