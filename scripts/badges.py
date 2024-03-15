"""
Create badges for profile and save to text file
"""
from IPython.display import Markdown


def orcid(orcid_id):
    """
    Create ORCID profile badge

    Parameters
    ----------
    orcid_id: str
        Researcher 16-digit ORCID digital identifier, eg. "0000-0000-0000-0000"

    Returns
    -------
    badge : str
        String of markdown that will produce the ORCID badge
    """
    # Add extra dashes to ID, for creating the badge image
    id_dash = orcid_id.replace("-", "--")
    badge = (f"[![ORCID](https://img.shields.io/badge/ORCID-{id_dash}-" +
             f"brightgreen)](https://orcid.org/{orcid_id})")
    return Markdown(badge)


def linkedin(name, link):
    """
    Create LinkedIn profile badge

    Parameters
    ----------
    name : str
        Full name
    link: str
        Link to LinkedIn profile

    Returns
    -------
    badge : str
        String of markdown that will produce the LinkedIn badge
    """
    name = name.replace(" ", "_")
    badge = ("[![LinkedIn](https://img.shields.io/badge/LinkedIn-" +
             f"{name}-0A66C2)]({link})")
    return Markdown(badge)


def github(username):
    """
    Create GitHub profile badge

    Parameters
    ----------
    username : str
        GitHub username

    Returns
    -------
    badge : str
        String of markdown that will produce the GitHub badge
    """
    badge = (f"[![GitHub](https://img.shields.io/badge/GitHub-{username}" +
             f"-DCD0FF)](https://github.com/{username})")
    return Markdown(badge)


orcid("0000-0002-6596-3479")
linkedin("Amy Heather", "https://www.linkedin.com/in/amyheather/")
github("amyheather")
