from smartphone import Smartphone


catalog = [
    Smartphone("Nokia", "3310", "+790134442211"),
    Smartphone("Sony Ericsson", "310", "+790134442222"),
    Smartphone("Xiaomi", "Mi6", "+790134442233"),
    Smartphone("Xiaomi", "Mi12", "+790134442244"),
    Smartphone("Huawei", "Honor", "+790134442255")
]


for smartphone in catalog:
    print(f"Smartphone: {smartphone.brand_name} - {smartphone.model_name}. "
          f"{smartphone.phone_number}.")
