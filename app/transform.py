def transform_data(data):
    transformed = []

    for item in data:
        transformed.append(
            (item['id'], item['title'].upper())
        )

    print("Data transformed successfully!")
    print("Number of records:", len(transformed))

    return transformed

