import random as r
import pprint


raw_data = [r.randint(1, 10000) for _ in range(10000)]
bucket_per_count = 1000

def fill_bucket(datas: list, bucket_counts: int) -> dict:
    buckets = {}

    for item in datas:
        bucket_index = item//bucket_counts
        if bucket_index not in buckets:
            buckets[bucket_index] = [item]
        buckets[bucket_index].append(item)

    return buckets

pprint.pprint(fill_bucket(raw_data, bucket_per_count))