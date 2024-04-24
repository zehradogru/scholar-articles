import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox, QCheckBox
from serpapi import GoogleSearch

class ScholarArticlesApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scholar Articles App")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.author_combo = QComboBox()
        self.populate_authors()
        self.author_combo.setPlaceholderText("Akademisyen seçin")

        self.all_authors_checkbox = QCheckBox("Tüm Akademisyenleri Seç")
        self.all_authors_checkbox.stateChanged.connect(self.toggle_author_combo)

        self.keyword_input = QLineEdit()
        self.keyword_input.setPlaceholderText("Anahtar kelimeyi girin")

        self.year_start_input = QLineEdit()
        self.year_start_input.setPlaceholderText("Başlangıç yılını girin")

        self.year_end_input = QLineEdit()
        self.year_end_input.setPlaceholderText("Bitiş yılını girin")

        self.search_button = QPushButton("Ara")
        self.search_button.clicked.connect(self.search_articles)

        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)

        layout.addWidget(self.author_combo)
        layout.addWidget(self.all_authors_checkbox)
        layout.addWidget(QLabel("Anahtar Kelime:"))
        layout.addWidget(self.keyword_input)
        layout.addWidget(QLabel("Başlangıç Yılı:"))
        layout.addWidget(self.year_start_input)
        layout.addWidget(QLabel("Bitiş Yılı:"))
        layout.addWidget(self.year_end_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.result_display)

        self.setLayout(layout)

    def populate_authors(self):
        authors = [
            "Mehmet Kemal GÜLLÜ",
            "Mehmet SAĞBAŞ",
            "Faruk UGRANLI",
            "Ahmet AYDOĞAN",
            "Bayram KÖSE"
        ]
        self.author_combo.addItems(authors)

    def toggle_author_combo(self, state):
        if state == 2:  # Qt.Checked
            self.author_combo.setEnabled(False)
        else:
            self.author_combo.setEnabled(True)

    def search_articles(self):
        if self.all_authors_checkbox.isChecked():
            authors = ["Mehmet Kemal GÜLLÜ", "Mehmet SAĞBAŞ", "Faruk UGRANLI", "Ahmet AYDOĞAN", "Bayram KÖSE"]
        else:
            authors = [self.author_combo.currentText()]

        keyword = self.keyword_input.text()
        year_start = self.year_start_input.text()
        year_end = self.year_end_input.text()

        articles = []
        for author in authors:
            author_id = self.get_author_id(author)
            if author_id:
                articles.extend(self.get_author_articles(author_id, keyword, year_start, year_end))

        if articles:
            self.display_articles(articles)
        else:
            self.result_display.setText("Makale bulunamadı.")

    def get_author_id(self, author):
        authors = {
            "Mehmet Kemal GÜLLÜ": "nQzwWRQAAAAJ",
            "Mehmet SAĞBAŞ": "Xnvw2B8AAAAJ",
            "Faruk UGRANLI": "lTVGokwAAAAJ",
            "Ahmet AYDOĞAN": "G6_h4LAAAAAJ",
            "Bayram KÖSE": "IMm58HcAAAAJ"
        }
        return authors.get(author)

    def get_author_articles(self, author_id, keyword, year_start, year_end):
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

    def display_articles(self, articles):
        self.result_display.clear()
        for article in articles:
            title = article.get("title", "")
            url = article.get("link", "")
            publication = article.get("publication", "")
            year = article.get("year", "")
            self.result_display.append(f"Title: {title}\nPublication: {publication}\nYear: {year}\nURL: {url}\n\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScholarArticlesApp()
    window.show()
    sys.exit(app.exec_())
