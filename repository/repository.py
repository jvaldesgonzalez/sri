from typing import List

class Language:
    def __init__(self, name) -> None:
        self.name = name
        self.extensions = [name]

class Auth:
    def __init__(self, username, fullname, biography, avatar, github_url, isVerified) -> None:
        self.username = username
        self.fullname = fullname
        self.github_url = github_url
        self.biography = biography
        self.avatar = avatar
        self.isVerified = isVerified

class Section:
    def __init__(self, header, content) -> None:
        self.header = header
        self.content: str or Section = content
        pass

class Documentation:
    def __init__(self, sections: List[Section] ) -> None:
        self.sections: List[Section] = sections,
        pass

class WikiPage:
    def __init__(self, title, content) -> None:
        self.title = title
        self.content = content

class Wiki:
    def __init__(self, pages) -> None:
        self.pages: List[WikiPage] = pages

class Repository:
    def __init__(self, languages, name, description, createdAt, lic, auth, github_url, documentation: Documentation, wiki: Wiki) -> None:
        self.name = name
        self.github_url = github_url
        self.description =  description
        self.createdAt =  createdAt
        self.lic = lic
        self.auth = auth
        self.languages: List[Language] = languages
        self.documentation = documentation
        self.wiki = wiki
        pass