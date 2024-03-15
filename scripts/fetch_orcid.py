'''
Fetch publications from ORCID
Based on code from Chris Holdgraf, 19 Nov 2022:
https://chrisholdgraf.com/blog/2022/orcid-auto-update/
'''

import pandas as pd
import requests
from rich import progress
from pathlib import Path
import json
import os


def fetch_meta(doi, fmt="reference", **kwargs):
    """
    Fetch metadata for a given DOI.

    Parameters
    ----------
    doi : str
    fmt : str, optional
        Desired metadata format. Can be 'dict' or 'bibtex'.
        Default is 'dict'.
    **kwargs :
        Additional keyword arguments are passed to `json.loads()` if `fmt`
        is 'dict' and you're a big JSON nerd.

    Returns
    -------
    out : str or dict or None
        `None` is returned if the server gives unhappy response. Usually
        this means the DOI is bad.

    Examples
    --------
    >>> fetchmeta('10.1016/j.dendro.2018.02.005')
    >>> fetchmeta('10.1016/j.dendro.2018.02.005', 'bibtex')

    References
    ----------
    https://www.doi.org/hb.html
    """
    # Parse args and setup the server response we want.
    accept_type = "application/"
    if fmt == "dict":
        accept_type += "citeproc+json"
    elif fmt == "bibtex":
        accept_type += "x-bibtex"
    elif fmt == "reference":
        accept_type = "text/x-bibliography; style=apa"
    else:
        raise ValueError(f"Unrecognized `fmt`: {fmt}")

    # Request data from server.
    url = "https://dx.doi.org/" + str(doi)
    header = {"accept": accept_type}
    r = requests.get(url, headers=header)

    # Format metadata if server response is good.
    out = None
    if r.status_code == 200:
        if fmt == "dict":
            out = json.loads(r.text, **kwargs)
        else:
            out = r.text
    return out


def get_publications(orcid_id):
    """
    Create markdown-formatted list of publications, fetched from ORCID API

    Parameters
    ----------
    orcid_id : str
        Researcher 16-digit ORCID digital identifier
    """
    orcid_record_api = "https://pub.orcid.org/v3.0/"

    # Download full ORCID record
    print(f"Retrieving ORCID entries from API for {orcid_id}...")
    response = requests.get(
        url=requests.utils.requote_uri(orcid_record_api + orcid_id),
        headers={"Accept": "application/json"},
    )
    response.raise_for_status()
    orcid_record = response.json()

    # Establish filename
    forename = orcid_record["person"]["name"]["given-names"]["value"]
    surname = orcid_record["person"]["name"]["family-name"]["value"]
    path = f"{Path(__file__).parent.parent}/publications"
    filename = (f"{forename}_{surname}_publications.txt").lower()

    # Check if any publications are listed for that ORCID ID
    if len(orcid_record["activities-summary"]["works"]["group"]) == 0:
        txt_file = open(os.path.join(path, filename), "w")
        txt_file.write('No publications associated with ORCID ID')
        txt_file.close()
    else:
        # Extract metadata for each entry
        # Loop through each of the publications...
        df = []
        for iwork in progress.track(
            orcid_record["activities-summary"]["works"]["group"],
            "Fetching reference data..."
        ):
            isummary = iwork["work-summary"][0]

            # Extract the DOI
            for ii in isummary["external-ids"]["external-id"]:
                if ii["external-id-type"] == "doi":
                    doi = ii["external-id-value"]
                    break

            # Fetch meta data from DOI
            meta = fetch_meta(doi, fmt="dict")

            # If it was unable to retrive meta data, use ORCID info
            if meta is None:
                title = isummary["title"]["title"]["value"]
                year = isummary["publication-date"]["year"]["value"]
                url = isummary["url"]["value"]
                autht = ""  # No author information available
                journal = isummary["journal-title"]
                # Replace with blank space if no journal was provided
                if journal is None:
                    journal = ""
            else:
                # Else, use the provided meta data
                title = meta["title"]
                year = meta["issued"]["date-parts"][0][0]
                url = meta["URL"]

                # Create authors list with links to their ORCIDs
                authors = meta["author"]
                autht = []
                for author in authors:
                    # Will be "given" and "family" for individual authors
                    if "family" in author:
                        name = f"""{author["family"]}, {author["given"][0]}."""
                        # Bold the name of our chosen person
                        if surname.lower() in author["family"].lower():
                            name = f"**{name}**"
                    # For a compancy/group, it will just be "name"
                    else:
                        name = author["name"]
                    # If author has an ORCID ID, link to it
                    if "ORCID" in author:
                        autht.append(f"[{name}]({author['ORCID']})")
                    else:
                        autht.append(name)
                autht = ", ".join(autht)

                journal = meta["publisher"]

            # Format
            url_doi = url.split("//", 1)[-1]
            reference = (f"""
{autht} ({year}). **{title}**. {journal}. [{url_doi}]({url})""")
            df.append({"year": year, "reference": reference})

        # Convert into a markdown string
        df = pd.DataFrame(df)
        md = []
        for year, items in df.groupby("year", sort=False):
            md.append(f"### {year}")
            for _, item in items.iterrows():
                md.append(item["reference"])
                md.append("")
            md.append("")
        mds = "\n".join(md)

        # Write to text file
        txt_file = open(os.path.join(path, filename), "w")
        txt_file.write(mds)
        txt_file.close()


# Run for each team member...

# Amy Heather
get_publications("0000-0002-6596-3479")

# Andy Mayne
get_publications("0000-0003-1263-2286")

# Anna Laws
get_publications("0000-0002-2145-0487")

# Ben Holdsworth
# ORCID ID unknown

# Chrissie Walker
get_publications("0000-0002-7933-1501")

# Dan Chalk
get_publications("0000-0002-4165-4364")

# Kerry Pearn
get_publications("0000-0003-2786-4426")

# Martin Pitt
get_publications("0000-0003-4026-8346")

# Mike Allen
get_publications("0000-0002-8746-9957")

# Rob Challen
get_publications("0000-0002-5504-7768")

# Sammi Rosser
# ORCID ID unknown

# Tom Monks
get_publications("0000-0003-2631-4481")
