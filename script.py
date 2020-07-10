import cancers

age = int(input("年齢を入力してください:"))
gender = input("性別を入力してください(m or f):")
pregnancy = input("(女性の場合)現在妊娠していますか？(1:はい、2：いいえ)")
smoking = input("これまでタバコを吸ったことがありますか？(1:はい、2：いいえ、３：以前吸っていたが禁煙した)：")
number_of_smoking = int(input("1日何本吸っています(した)か？:"))
years_of_smoking = int(input("何年間吸っています(した)か？:"))

smoking_hx = number_of_smoking * years_of_smoking

print("本患者には以下の項目がヘルスメンテナンスとして推奨されます")

if age >= 50 and age < 75:
    cancers.colon_ca()

if age > 50:
    cancers.gastric_ca()

if age >= 40 and age < 75 and gender == "f":
    cancers.breast_ca()

if age >= 21 and age < 65:
    cancers.cervical_ca()

if age >= 55 and age < 80 and smoking_hx >= 30
    cancers.lung_ca()

if age >= 50 and age < 70 and gender == "m":
    cancers.prostate_ca()
