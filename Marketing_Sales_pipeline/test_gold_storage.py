from gold.storage.gold_storage import GoldStorage

storage = GoldStorage()

google = storage.read_latest_silver("google_ads")

print("\nGoogle Ads Data:")
print(google.head())

print("\nColumns:")
print(google.columns.tolist())

print("\nRows:", len(google))