#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Parse and clean text sources"""

import re


def extract_citation_info(citation_text: str) -> str:
    """Extract citation information from the document name."""

    citation_pattern = r"(.*?)(\d{4})(.*)"  # split at first occurrence of year
    authors, year, title = re.findall(citation_pattern, citation_text)[0]
    authors = authors.replace("et al ", "")
    title = title.replace(" - ", "")

    return authors, year, title
