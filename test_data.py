import testdata
import datetime
class Usage(testdata.DictFactory):
    id = testdata.CountingFactory(10)
    deviceId = testdata.CountingFactory(10)
    studentId = testdata.CountingFactory(10)
    #time = testdata.RelativeToDatetimeField("start_time", datetime.timedelta(minutes=20))
    packageName = testdata.RandomSelection(['Literacy', 'Game', 'Speech'])
    literacySkill = testdata.RandomLengthStringFactory()
    numeracySkill = testdata.RandomLengthStringFactory()
    letter = testdata.RandomLengthStringFactory()
    number = testdata.RandomLengthStringFactory()
    word = testdata.RandomLengthStringFactory()



#xpected format: id:1|deviceId:4113947bec18b7ad|time:1481916197273|packageName:org.literacyapp|literacySkill:LETTER_IDENTIFICATION|numeracySkill:null|letter:a|number:null|word:null



for usage in Usage().generate(10): # let say we only want 10 users
    print usage
    #{'numeracySkill': 'PwBiXKjwddG', 'studentId': 17, 'word': 'XctugWiHPobIvHNGEbYlgyOUuuqCSKgoTFAhJSQzUUleDEkygyZOWBnGYiLBXbywpwxAsisToqDDWGPHQqbOOlmGVVa', 'packageName': 'Literacy', 'number': 'IrtJUAxnFVOQyvvqlpIsmkaWnRvADBzWBiCYUPvfSwvdHS', 'literacySkill': 'hSQSRXUevpdYMGAs', 'deviceId': 17, 'letter': 'JYuWfonIdptbdpFhBNhLIkLoyhuUgRUvdiUWBcfReeezORAtXhJvNuLZASFeRCAvxvPgOeTZ', 'id': 17}
    #{'numeracySkill': 'ozTpqAwdLstMzeijgJBGYMLantLSMESfYEBMQQxkjILBgNXohBjMbwqrhGsnjoSlcsCGOnTsdgMICQfB', 'studentId': 18, 'word': 'CnhxwMonHnMlEtxcpGowQymEeZtxvlUBDaKHEKRC', 'packageName': 'Literacy', 'number': 'xkerlJLhlyOgsTxHqMPffjPLOqbjgZqtggGzxPTkOleoZtEaDiYnpKxrouCcgRPjdtf', 'literacySkill': 'VlEeAOKKOIgweFTxBeNiOWmoztGPWSqhsIxTr', 'deviceId': 18, 'letter': 'NwJUuHLOkaJHsIvlSQeggfT', 'id': 18}
    #{'numeracySkill': 'uaUQunGtHwrFTuRlVrhwEUisIWlcrZXUZKIlILoPoCgnVWHwrrRaHhxQJVnECUtSvppzQDtpiqUSds', 'studentId': 19, 'word': 'vOTlRRgSXwgmXAthOYnQTTtPJyGxGbbMOj', 'packageName': 'Game', 'number': 'bDmhALNhnmazlonmBIjvwWzXgQfPQQekWJErEvJjWWHrufxuINyHuNiLPvFWynVwdNTaTGIgvvGCAqFRZ', 'literacySkill': 'BpfiZyRAzovNbEhtznPSaqsaZhRkFHlWNpmbzBXKCmBJPnuYiQyEToMaOkVJOVZKNCCAyGpZSpGhfseBMfGaFvltHaJyfcdota', 'deviceId': 19, 'letter': 'nvwanqC', 'id': 19}
