class KijijiAd():

    def __init__(self, ad):
        self.title = ad.find('a', {"class": "cta"}).text.strip()
        self.id = ad['data-id']
        self.ad = ad
        self.info = {}

        self.__locate_info()
        self.__parse_info()

    def __locate_info(self):
        # Locate ad information
        self.info["Title"] = self.ad.find('a', {"class": "cta"})
        self.info["Image"] = str(self.ad.find('img').get("src"))
        self.info["Url"] = self.ad.find('a').get("href")
        self.info["Details"] = self.ad.find(
            'div', {"class": "details"})
        self.info["Description"] = self.ad.find(
            'p', {"class": "description"})
        self.info["Date"] = self.ad.find(
            'p', {"class": "timestamp"})
        self.info["Location"] = self.ad.find('p', {"class": "locale"})
        self.info["Price"] = self.ad.find('h4', {"class": "price"})

    def __parse_info(self):
        # Parse Details and Date information
        self.info["Details"] = self.info["Details"].text.strip() \
            if self.info["Details"] is not None else ""
        self.info["Date"] = self.info["Date"].text.strip() \
            if self.info["Date"] is not None else ""

        # Parse remaining ad information
        for key, value in self.info.items():
            if value:
                if key == "Url":
                    self.info[key] = value

                elif key == "Description":
                    self.info[key] = value.text.strip() \
                        .replace(self.info["Details"], '')

                elif key == "Location":
                    self.info[key] = value.text.strip() \
                        .replace(self.info["Date"], '')

                elif key not in ["Image", "Details", "Date"]:
                    self.info[key] = value.text.strip()
