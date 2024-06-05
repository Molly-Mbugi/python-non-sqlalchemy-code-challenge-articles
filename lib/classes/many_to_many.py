class Author:
    def __init__(self, name):
        #check if its string 
        if isinstance(name, str) and len(name) > 0:
            self._name = name
            self._articles = []
        else:
            print ("Names must be longer than 0 characters")

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
          # Create a new article and add it to the author's list of articles
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        #  list of unique topic areas
        if not self._articles:
            return None
        topic_areas_set = set(article.magazine.category for article in self._articles)
        return list(topic_areas_set)


class Magazine:
    all_magazines = []

    def __init__(self, name, category):
         # Check if the name is a string between 2 and 16 char
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            print ("Name must be a string between 2 and 16 characters")
        if isinstance(category, str) and len(category) > 0:
            self._category = category
            self._articles = []
        else:
            print("Names must be longer than 0 characters")
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name
        else:
            print("Name must be a string between 2 and 16 characters")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        # Set a new category for the magazine
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category
        else:
            print("Category must be a non-empty string")

    def articles(self):
        return self._articles

    def contributors(self):
        contributors_set = set(article.author for article in self._articles)
        return list(contributors_set) if contributors_set else None

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
         # list of authors who have written more than 2 articles for the magazine
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
        # Check instance 
        if not isinstance(author, Author):
            print("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            print("Magazine must be an instance of Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            print("Title must be a string between 5 and 50 characters")
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
        # Set a new author for the article
        if isinstance(new_author, Author):
            if self in self._author.articles():
                self._author.articles().remove(self)
            self._author = new_author
            new_author.articles().append(self)
        else:
            print("Author must be an instance of Author")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
         # Set a new magazine
        if isinstance(new_magazine, Magazine):
            if self in self._magazine.articles():
                self._magazine.articles().remove(self)
            self._magazine = new_magazine
            new_magazine.articles().append(self)
        else:
            print("Magazine must be an instance of Magazine")









