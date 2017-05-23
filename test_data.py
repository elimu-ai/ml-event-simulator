import testdata
import datetime
class Usage(testdata.DictFactory):
    id = testdata.CountingFactory(10)
    deviceId = testdata.CountingFactory(10)
    studentId = testdata.CountingFactory(10)
    time = testdata.RandomDateFactory(datetime.datetime(2013, 10, 1, 1, 1, 0, 0), datetime.datetime.now())
    packageName = testdata.RandomSelection(['Literacy', 'Game', 'Speech'])
    literacySkill = testdata.RandomLengthStringFactory(1,5)
    numeracySkill = testdata.RandomLengthStringFactory(1,5)
    letter = testdata.RandomLengthStringFactory(1,1)
    number = testdata.RandomInteger(1,9999)
    word = testdata.RandomLengthStringFactory(1,10)
    score = testdata.RandomInteger(20, 100) 



#xpected format: id:1|deviceId:4113947bec18b7ad|time:1481916197273|packageName:org.literacyapp|literacySkill:LETTER_IDENTIFICATION|numeracySkill:null|letter:a|number:null|word:null


out = open("usage.txt", 'w')
for usage in Usage().generate(10000): 
    #print usage
    out.write(str(usage))
    out.write("\n")
    #{'numeracySkill': 'PwBiXKjwddG', 'studentId': 17, 'word': 'XctugWiHPobIvHNGEbYlgyOUuuqCSKgoTFAhJSQzUUleDEkygyZOWBnGYiLBXbywpwxAsisToqDDWGPHQqbOOlmGVVa', 'packageName': 'Literacy', 'number': 'IrtJUAxnFVOQyvvqlpIsmkaWnRvADBzWBiCYUPvfSwvdHS', 'literacySkill': 'hSQSRXUevpdYMGAs', 'deviceId': 17, 'letter': 'JYuWfonIdptbdpFhBNhLIkLoyhuUgRUvdiUWBcfReeezORAtXhJvNuLZASFeRCAvxvPgOeTZ', 'id': 17}
    #{'numeracySkill': 'ozTpqAwdLstMzeijgJBGYMLantLSMESfYEBMQQxkjILBgNXohBjMbwqrhGsnjoSlcsCGOnTsdgMICQfB', 'studentId': 18, 'word': 'CnhxwMonHnMlEtxcpGowQymEeZtxvlUBDaKHEKRC', 'packageName': 'Literacy', 'number': 'xkerlJLhlyOgsTxHqMPffjPLOqbjgZqtggGzxPTkOleoZtEaDiYnpKxrouCcgRPjdtf', 'literacySkill': 'VlEeAOKKOIgweFTxBeNiOWmoztGPWSqhsIxTr', 'deviceId': 18, 'letter': 'NwJUuHLOkaJHsIvlSQeggfT', 'id': 18}
    #{'numeracySkill': 'uaUQunGtHwrFTuRlVrhwEUisIWlcrZXUZKIlILoPoCgnVWHwrrRaHhxQJVnECUtSvppzQDtpiqUSds', 'studentId': 19, 'word': 'vOTlRRgSXwgmXAthOYnQTTtPJyGxGbbMOj', 'packageName': 'Game', 'number': 'bDmhALNhnmazlonmBIjvwWzXgQfPQQekWJErEvJjWWHrufxuINyHuNiLPvFWynVwdNTaTGIgvvGCAqFRZ', 'literacySkill': 'BpfiZyRAzovNbEhtznPSaqsaZhRkFHlWNpmbzBXKCmBJPnuYiQyEToMaOkVJOVZKNCCAyGpZSpGhfseBMfGaFvltHaJyfcdota', 'deviceId': 19, 'letter': 'nvwanqC', 'id': 19}
out.close()
