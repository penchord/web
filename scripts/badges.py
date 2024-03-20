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
    # For the badge, will need to replace any '-' with '--' else error
    badge_name = username.replace("-", "--")
    badge = (f"[![GitHub](https://img.shields.io/badge/GitHub-{badge_name}" +
             f"-DCD0FF)](https://github.com/{username})")
    return badge


def create_badges(full_name, orcid_id=None, linkedin_link=None,
                  github_username=None):
    """
    Generate markdown to produce ORCID, LinkedIn and GitHub badges

    Parameters
    ----------
    full_name : str
        Full name
    orcid_id: str
        Researcher 16-digit ORCID digital identifier, eg. "0000-0000-0000-0000"
    linkedin_link: str
        Link to LinkedIn profile
    github_username : str
        GitHub username
    """
    # Get badges (depending on information provided)
    content = ""
    if orcid_id is not None:
        content += str(orcid(orcid_id) + "   ")
    if linkedin_link is not None:
        content += str(linkedin(full_name, linkedin_link) + "   ")
    if github_username is not None:
        content += str(github(github_username))

    # Get path and name for text file produced
    path = f"{Path(__file__).parent.parent}/badges"
    name_lower = full_name.lower().replace(" ", "_")

    # Write badges to text file
    txt_file = open(os.path.join(path, f"{name_lower}_badges.txt"), "w")
    txt_file.write(content)
    txt_file.close()


create_badges(
    full_name="Amy Heather",
    orcid_id="0000-0002-6596-3479",
    linkedin_link="https://www.linkedin.com/in/amyheather/",
    github_username="amyheather")

create_badges(
    orcid_id="0000-0002-2145-0487",
    full_name="Anna Laws",
    github_username="aselaws")

create_badges(
    orcid_id="0000-0002-7933-1501",
    full_name="Chrissie Walker",
    linkedin_link="https://www.linkedin.com/in/chrisssiewalker/")

create_badges(
    orcid_id="0000-0002-4165-4364",
    full_name="Dan Chalk",
    github_username="hsma-chief-elf")

create_badges(
    orcid_id="0000-0003-2786-4426",
    full_name="Kerry Pearn",
    github_username="KerryPearn")

create_badges(
    orcid_id="0000-0003-4026-8346",
    full_name="Martin Pitt",
    linkedin_link="https://www.linkedin.com/in/martin-pitt-735625a/")

create_badges(
    orcid_id="0000-0002-8746-9957",
    full_name="Mike Allen",
    github_username="MichaelAllen1966")

create_badges(
    orcid_id="0000-0002-9552-8988",
    full_name="Sammi Rosser",
    linkedin_link="https://www.linkedin.com/in/sammijaderosser/",
    github_username="Bergam0t")

create_badges(
    orcid_id="0000-0003-2631-4481",
    full_name="Tom Monks",
    linkedin_link="https://www.linkedin.com/in/thomas-monks-a24aa22/",
    github_username="TomMonks")
