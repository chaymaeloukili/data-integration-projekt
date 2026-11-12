# Google Trends ("Kino" vs. "Netflix")

Status: **checked, currently not used in the project** (as of 08.11.2026)

## Fact sheet

|Field|Content|
|-|-|
|ID|Z1|
|Provider|Google|
|Link|https://trends.google.de|
|Type|quantitative, time series|
|Period|from 2004 to today|
|Format|CSV export via the download icon in the chart|
|Content|Relative search interest (index 0 to 100) over time, plus a breakdown by sub-region (federal state) and related search queries|
|Acquisition|manual export, no automated queries|
|Research relevance|F1: search interest in "Kino" compared to "Netflix" as an indication of interest in cinema and streaming|

## Query (reproducibility)

|Parameter|Value|
|-|-|
|Search terms|"Kino" + "Netflix"|
|Region|Germany|
|Period|2004 to today|
|Category|All categories|
|Search type|Web search|
|Date retrieved|08.11.2026|
|Screenshot|see below|

<img width="600" alt="Google Trends: Kino and Netflix" src="https://github.com/user-attachments/assets/b5fec7eb-adea-40ad-8d54-09ebbc775692" />

<img width="350" alt="Google Trends: breakdown by sub-region for Kino and Netflix" src="https://github.com/user-attachments/assets/13d96674-1f3a-4e58-94ff-dc970b1f5a1d" />

No CSV export was placed in the repository because the data is currently not used.

## Licence and use

* No open licence (e.g. Creative Commons).
* The Google help page "Export, embed and cite Trends data" allows the CSV export and states that information from Google Trends may be used "in accordance with the Google Terms of Service". When reusing it, it should be clearly visible that the data comes from Google. The help page gives "Data source: Google Trends" with a link to google.com/trends as an example. (Help page checked on 08.11.2026: https://support.google.com/trends/answer/4365538?hl=de)
* The Google Terms of Service themselves were not read word for word.
* No automated queries (e.g. unofficial libraries such as pytrends), manual export only.

**Source citation:** "Data source: Google Trends (https://www.google.com/trends), query of 08.11.2026, search terms 'Kino' and 'Netflix', Germany, 2004 to today."

## Completeness and quality

* The values are a relative index from 0 to 100, not an absolute search volume. 100 is the highest value in the selected period and for all compared terms together.
* When queried together, the series "Kino" and "Netflix" are directly comparable. If you change parameters such as the period or the terms, the scaling and the values change.
* The values can differ slightly between retrievals. Therefore: record the retrieval date and parameters and save the exported CSV unchanged.
* The chart shows lines at individual points in time that are meant to represent a note. They point to changes at Google and can explain breaks in the series. The exact wording was not checked and would have to be read up on before use.
* Observation from the screenshot: "Kino" shows seasonal fluctuations over the whole period and a sharp drop around 2020. "Netflix" is close to zero until about 2013 and rises afterwards. Exact values come from the CSV, not from the screenshot.

## Limits of interpretation

* Search interest does not mean use or attendance. A person interested in searching will not necessarily also visit a cinema. In addition, "Kino" includes searches for programmes, individual cinemas and films, so it can be interpreted in more than one way.
* Two time series that rise or fall together do not prove a causal relationship (-> spurious correlation). A displacement effect between Netflix and cinema cannot be shown this way.
* The series is based on samples of Google search queries. Details of the methodology were not checked.

## Decision

Not used as a data source because the project already contains enough sources. The check stays in the repository for documentation. If the source is used later after all:

1. Define two to three search terms (e.g. "Kino", "Netflix").
2. Export the CSV for each query.
3. Add the parameters to this file and read up on the notes in the chart.

