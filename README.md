# Validator

Package create to provide custom validation of attributes in a dataclass.   By design this is not a complete package put rather intended to show how to impliment a complicated practice simply. 

## Background

I was trying to set write an RestfulAPI and I wanted to only accept valid data. As a new python developer I started writing a lot of getters and setters with tons of validation. Thank goodness I was stopped and pointed at dataclasses.  I then dove in, but was having trouble writting validation for the atttributes without overridding all the benifits of the dataclass. I was then pointed at descriptors, which resulted that issue (eventually). 

Since I was learning pytest at the same time I wrote out all the tests verifiy all the expected behavior. 

## Overview

Provided validation of a property in a dataclass. In the example i am checkng a field called short code a four (4) char string utilized as part of a much large dataclass. All other parts of the dataclass have been removed. A stub program has been added to create the data class. 

The validation ensure that either a 4 character string is pass when and instance of the class is created. 
```python
obj = Obj("AAAA") 
```

It will also accept a zero length string or the class can be instances without a parameter being passed. 

```python
obj = Obj()   
```

Additionally,  this also verified that new value meets those requirements if changed.  
```python
obj.param = "BBBB"
obj.param = None
obj.param="" 
```
All would be accepted.  Any other entries will raise an error to the calling function.  

## Requirements

Seee requirements.txt

## Setup

1. Fork this project.
2. Clone to your local machine.
3. Create virtual environment.
```
$ cd validator
~/validator$ python -m venv venv
~/validator$ venv/scripts/activate
(venv) ~/validator$ pip install -r requirements.txt
```


