from serpapi import GoogleSearch

class ScholarArticlesDatabase:
    @staticmethod
    def get_author_id(author):
        authors = {
            "Mehmet Kemal GÜLLÜ": "nQzwWRQAAAAJ",
            "Mehmet SAĞBAŞ": "Xnvw2B8AAAAJ",
            "Faruk UGRANLI": "lTVGokwAAAAJ",
            "Ahmet AYDOĞAN": "G6_h4LAAAAAJ",
            "Bayram KÖSE": "IMm58HcAAAAJ"
        }
        return authors.get(author)

    @staticmethod
    def get_author_articles(author_id, keyword, year_start, year_end):
        params = {
            "engine": "google_scholar_author",
            "author_id": author_id,
            "api_key": "your_api_key_here",
            "timeframe": "custom",
            "as_ylo": year_start,
            "as_yhi": year_end,
            "q": keyword
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        return results.get("articles", [])
