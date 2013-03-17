Dr. Book
==========
For any book authored using the Docbook XML structure (http://docbook.org/tdg51/en/html/) we will extract people, places, topics and concepts to render a webpage linking these resources to Open Data resources such as Freebase (wikipedia), OpenStreetMap, and Flickr. We will use Pandas to do text analysis on the book to produce a word cloud and answer other questions about the text.

What open data sets might you be working with?
Resources:
Base: eBook in structured Docbook XML
Linked Data: DBPedia - API,
Freebase
OpenMaps
Flickr

Possible ties to Wikipedia (or any Wikimedia related projects)?
We will use Freebase and OpenStreeMap

What are some concrete immediate first/next steps in your projects?
Finding parts of text to link to wikipedia
Resolving text to wikipedia entries

What challenges do you anticipate running into?
Learning to access APIs
Data mashups
Front-end design / structure / d3 visualization

What skills will a team need to develop to solve this problem?
Database management, visualization, statistical analysis, extensive JavaScript knowledge (backbone.js)

Application Structure:
  Back-end:
		Database - MarkLogic, BaseX
		Python Flask WebServer
		Semantic analysis - Python NLTK (Natural Language Toolkit)
	Front-end:
		Backbone.js (MVC)
		d3.js (visualization & interaction)
