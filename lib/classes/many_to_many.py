class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
            self._articles = []
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        magazines_list = []
        for article in self._articles:
            if article.magazine not in magazines_list:
                magazines_list.append(article.magazine)
        return magazines_list if magazines_list else None

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        if not self._articles:
            return None
        topic_areas_set = set()
        for article in self._articles:
            topic_areas_set.add(article.magazine.category)
        return list(topic_areas_set)


class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError("Name must be a string between 2 and 16 characters")
        if isinstance(category, str) and len(category) > 0:
            self._category = category
            self._articles = []
        else:
            raise ValueError("Category must be a non-empty string")
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        return self._articles

    def contributors(self):
        contributors_set = set()
        for article in self._articles:
            contributors_set.add(article.author)
        return list(contributors_set) if contributors_set else None

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        if not self._articles:
            return None
        
        authors_dict = {}
        for article in self._articles:
            if article.author in authors_dict:
                authors_dict[article.author] += 1
            else:
                authors_dict[article.author] = 1
        
        result = [author for author, count in authors_dict.items() if count > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not cls.all_magazines:
            return None
        top_magazine = max(cls.all_magazines, key=lambda mag: len(mag.articles()))
        return top_magazine


class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        author.articles().append(self)
        magazine.articles().append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            if self in self._author.articles():
                self._author.articles().remove(self)
            self._author = new_author
            new_author.articles().append(self)
        else:
            raise ValueError("Author must be of type Author")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            if self in self._magazine.articles():
                self._magazine.articles().remove(self)
            self._magazine = new_magazine
            new_magazine.articles().append(self)
        else:
            raise ValueError("Magazine must be of type Magazine")

