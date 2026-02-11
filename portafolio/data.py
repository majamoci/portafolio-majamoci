import json
from dataclasses import dataclass, field


@dataclass
class Media:
    email: str
    cv: str
    github: str
    likedin: str


@dataclass
class Technology:
    icon: str
    name: str


@dataclass
class Info:
    icon: str
    title: str
    subtitle: str
    description: str
    date: str = ""
    certificate: str = ""
    technologies: list = field(default_factory=list)
    image: str = ""
    url: str = ""
    github: str = ""
    
    def __post_init__(self):
        self.technologies = [
            Technology(**tech) if isinstance(tech, dict) else tech
            for tech in self.technologies
        ]


@dataclass
class Extra:
    image: str
    title: str
    description: str
    url: str


@dataclass
class Data:
    title: str
    description: str
    image: str
    avatar: str
    name: str
    skill: str
    location: str
    media: Media
    about: str
    technologies: list = field(default_factory=list)
    experience: list = field(default_factory=list)
    projects: list = field(default_factory=list)
    training: list = field(default_factory=list)
    extras: list = field(default_factory=list)
    
    def __post_init__(self):
        self.media = Media(**self.media) if isinstance(self.media, dict) else self.media
        self.technologies = [
            Technology(**tech) if isinstance(tech, dict) else tech
            for tech in self.technologies
        ]
        self.experience = [
            Info(**info) if isinstance(info, dict) else info
            for info in self.experience
        ]
        self.projects = [
            Info(**info) if isinstance(info, dict) else info
            for info in self.projects
        ]
        self.training = [
            Info(**info) if isinstance(info, dict) else info
            for info in self.training
        ]
        self.extras = [
            Extra(**info) if isinstance(info, dict) else info
            for info in self.extras
        ]


with open("assets/data/data.json") as file:
    json_data = json.load(file)

data = Data(**json_data)
