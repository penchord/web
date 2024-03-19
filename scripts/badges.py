"""
Create badges for profile and save to text file
"""
from pathlib import Path
import os


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
    return badge


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
    return badge


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
    return badge


def create_badges(orcid_id, full_name, linkedin_link, github_username):
    """
    Generate markdown to produce ORCID, LinkedIn and GitHub badges

    Parameters
    ----------
    orcid_id: str
        Researcher 16-digit ORCID digital identifier, eg. "0000-0000-0000-0000"
    full_name : str
        Full name
    linkedin_link: str
        Link to LinkedIn profile
    github_username : str
        GitHub username
    """
    path = f"{Path(__file__).parent.parent}/badges"
    name_lower = full_name.lower().replace(" ", "_")
    txt_file = open(os.path.join(path, f"{name_lower}_badges.txt"), "w")
    txt_file.write(str(
        orcid(orcid_id) + "   " +
        linkedin(full_name, linkedin_link) + "   " +
        github(github_username)))
    txt_file.close()


create_badges(
    "0000-0002-6596-3479",
    "Amy Heather",
    "https://www.linkedin.com/in/amyheather/",
    "amyheather")
