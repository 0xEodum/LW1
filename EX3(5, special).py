def search_date(data):
    dates = []
    days = [str(i).zfill(2) for i in range(1, 32)]
    months = ["января", "февраля", "марта", "апреля", "мая", "июня",
              "июля", "августа", "сентября", "октября", "ноября", "декабря"]

    for i in range(len(data)):
        month = ""
        if data[i:i + 2] in days and data[i + 2:i + 3] == " ":
            for j in range(i + 3, len(data)):
                month += data[j]
                if month in months and data[j+1] == " ":
                    date = data[i:j + 6]
                    dates.append(date)
                    continue
    return dates

if __name__ == '__main__':
    text = """13 апреля 2024 ivgt 25 ноября 2000еупы 98 декабря 2000 12 декабря 2004"""
    print(search_date(text))