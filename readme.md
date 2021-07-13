## Top N search from huge list


> Given a file with two columns, uuid and a value (assuming valuees to be integers).
> 
> Print uuid with top N values to stdout


#### Data Generator
To generate the file to play with, use

`python data_generator.py --file_path <OUTPUT_FILE_PATH> --count <#ROWS>`

(50000000 rows => 2 GB)


#### Get Top N 
To get the uuids with top N values, use

`python main.py --file_path <INPUT_FILE_PATH> --n <N int>`

---

#### Sample

![img.png](img.png)