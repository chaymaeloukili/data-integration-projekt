# Notes: What happens after Clean?

Flow: Explore → Clean → Integrate → Check → Analyse → Visualise

## 1. What do we do after Clean?

After cleaning, every source has a clean, uniform format (for Q6: `year` and `population`).

Next step: merge the sources into one common table.

In our project this is `notebooks/combined/`, followed by `03_analysis` and `04_visualisation`. Then we check whether the result is correct (row count, no unexpected gaps), and only after that we analyse.

## 2. What do we join it with?

With the other sources, using the key `year`. For us, the population is mainly a reference value: with visitors or tickets per year (FFA) we can calculate visits per capita. This makes the years comparable, even when the population grows or jumps (2011) because of the census. The Letterboxd data is at film level and has to be aggregated to years first (`groupby`) before it can be joined.

## 3. How does it work?

Technically it is a join on the common key, in pandas for example:

```python
combined = tickets.merge(population, on="year", how="left", validate="one_to_one")
```

Three things matter:

- The key must have the same name, the same type and the same granularity in all tables (here: one row per year, as a number).
- `how`: `inner` keeps only the years both tables have, `left` keeps all years of the left table and fills gaps with NaN, `outer` keeps everything.
- `validate="one_to_one"` stops with an error if a year appears twice. Otherwise rows would multiply without anyone noticing.

Granularity means how finely the data is resolved, that is, what a single row represents.

In our project:

- Destatis population: one row per year
- FFA tickets: one row per year (if we use yearly values)
- Letterboxd: one row per film. The granularity is finer.

Population and FFA have the same granularity, so we can join them directly on `year`. Letterboxd cannot be attached directly. Otherwise every film would get the population of its year, and a year with 300 films would appear 300 times in the table. That is why Letterboxd is first aggregated with `groupby("year")`, for example as the number of films or the average rating per year. Only then do the granularities match.

Rule of thumb: before a join, both tables must have the same granularity, otherwise rows multiply. This is exactly what `validate="one_to_one"` catches: if a year appears twice in one table, there is an error.

## 4. Which methods exist?

These terms may come up in the course:

- **Schema matching / mapping:** Which columns mean the same? (Aligning column names)
- **Entity resolution / record linkage:** Recognising the same things across different sources, even when the spelling differs (for example film titles, with exact or fuzzy comparisons).
- **Data fusion:** When two sources contradict each other, deciding which value counts.
- **Aggregation and harmonisation:** Aligning units, time periods and granularity.
- **ETL (Extract, Transform, Load):** the usual flow as a pipeline.

For us, a key join on `year` is probably enough. Entity resolution would only be needed if we link individual films between FFA and Letterboxd.

## 5. What to watch out for, especially regarding reusability

- **Data quality after the join:** gaps (NaN), duplicate rows, different time periods (Destatis 1950–2025, Q7 from 1970, our focus 2001–2025).
- **Breaks in the series:** The census break in 2011 stays a break in the combined table as well. It should be stated in the documentation.
- **Reproducibility:** Never change raw data, do everything with scripts instead of by hand, use relative paths, no fixed paths like `C:\Users\...`. This is exactly why the scripts sit next to the notebooks.
- **Documentation:** What does each column mean, which unit, which source, which date? A short data dictionary helps.
- **Licences:** Derived data inherits the terms of the sources. For us: Destatis (dl-de/by-2-0, attribution), Kaggle (CC BY 4.0 or CC BY-NC-SA 4.0, non-commercial, share-alike) and the FFA (permission). This also applies to the combined table.
- **Conventions:** Consistent column names, types and file names, as in our README. In addition, automatic checks such as `assert` lines (Q6), so that errors show up early.
- **FAIR principles:** Findable, Accessible, Interoperable, Reusable. The "R" is exactly the question: data is reusable when its origin, licence and meaning are clearly documented.

NaN = Not a Number
