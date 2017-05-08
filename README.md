# DataGeneratorSimulator
It will generate usage and performance data from user.

## Tutorial
*[Building a Data-Driven Education System](http://www2.datainnovation.org/2016-data-driven-education.pdf)

*[Enhancing Teaching and Learning Through Educational Data Mining and Learning Analytics](https://tech.ed.gov/wp-content/uploads/2014/03/edm-la-brief.pdf)


# Focus two major areas:
## Content Analytics

Are teachers using the best possible content? This level of data analysis takes a deeper dive to better inform the design of new course content and understand its impact (or lack thereof) on students.

## Learning Analytics

Game-based learning and adaptive learning systems are growing in use. This technology is designed to build statistical models of student knowledge, tracking their progress in order to personalize the learning experience.

## Requirement

    pip install python-testdata


## Examples
We integrate the awsome fake-factory package to generate data using FakeData,
this allows us to usage data event:
    * id 
    * deviceId
    * studentId
    * packageName
    * literacySkill
    * and much much more

lets create a very simple factory that generates Users:

```python

import testdata
import datetime

class Usage(testdata.DictFactory):
    id = testdata.CountingFactory(10)
    deviceId = testdata.CountingFactory(10)
    studentId = testdata.CountingFactory(10)
    packageName = testdata.RandomSelection(['Literacy', 'Game', 'Speech'])
    literacySkill = testdata.RandomLengthStringFactory()
    numeracySkill = testdata.RandomLengthStringFactory()
    letter = testdata.RandomLengthStringFactory()
    number = testdata.RandomLengthStringFactory()
    word = testdata.RandomLengthStringFactory()


for usage in Usage().generate(10): # let say we only want 10 users
    print usage
    #{'numeracySkill': 'PwBiXKjwddG', 'studentId': 17, 'word': 'XctugWiHPobIvHNGEbYlgyOUuuqCSKgoTFAhJSQzUUleDEkygyZOWBnGYiLBXbywpwxAsisToqDDWGPHQqbOOlmGVVa', 'packageName': 'Literacy', 'number': 'IrtJUAxnFVOQyvvqlpIsmkaWnRvADBzWBiCYUPvfSwvdHS', 'literacySkill': 'hSQSRXUevpdYMGAs', 'deviceId': 17, 'letter': 'JYuWfonIdptbdpFhBNhLIkLoyhuUgRUvdiUWBcfReeezORAtXhJvNuLZASFeRCAvxvPgOeTZ', 'id': 17}
    #{'numeracySkill': 'ozTpqAwdLstMzeijgJBGYMLantLSMESfYEBMQQxkjILBgNXohBjMbwqrhGsnjoSlcsCGOnTsdgMICQfB', 'studentId': 18, 'word': 'CnhxwMonHnMlEtxcpGowQymEeZtxvlUBDaKHEKRC', 'packageName': 'Literacy', 'number': 'xkerlJLhlyOgsTxHqMPffjPLOqbjgZqtggGzxPTkOleoZtEaDiYnpKxrouCcgRPjdtf', 'literacySkill': 'VlEeAOKKOIgweFTxBeNiOWmoztGPWSqhsIxTr', 'deviceId': 18, 'letter': 'NwJUuHLOkaJHsIvlSQeggfT', 'id': 18}
    #{'numeracySkill': 'uaUQunGtHwrFTuRlVrhwEUisIWlcrZXUZKIlILoPoCgnVWHwrrRaHhxQJVnECUtSvppzQDtpiqUSds', 'studentId': 19, 'word': 'vOTlRRgSXwgmXAthOYnQTTtPJyGxGbbMOj', 'packageName': 'Game', 'number': 'bDmhALNhnmazlonmBIjvwWzXgQfPQQekWJErEvJjWWHrufxuINyHuNiLPvFWynVwdNTaTGIgvvGCAqFRZ', 'literacySkill': 'BpfiZyRAzovNbEhtznPSaqsaZhRkFHlWNpmbzBXKCmBJPnuYiQyEToMaOkVJOVZKNCCAyGpZSpGhfseBMfGaFvltHaJyfcdota', 'deviceId': 19, 'letter': 'nvwanqC', 'id': 19}
