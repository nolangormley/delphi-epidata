---
title: FluView Clinical
parent: Other Endpoints (COVID-19 and Other Diseases)
---

# FluView Clinical

This is the API documentation for accessing the FluView Clinical
(`fluview_clinical`) endpoint of [Delphi](https://delphi.cmu.edu/)'s
epidemiological data.

General topics not specific to any particular endpoint are discussed in the
[API overview](README.md). Such topics include:
[contributing](README.md#contributing), [citing](README.md#citing), and
[data licensing](README.md#data-licensing).

## FluView Clinical Data

... <!-- TODO -->

# The API

The base URL is: https://delphi.cmu.edu/epidata/fluview_clinical/

See [this documentation](README.md) for details on specifying epiweeks, dates, and lists.

## Parameters

### Required

| Parameter | Description | Type |
| --- | --- | --- |
| `epiweeks` | epiweeks | `list` of epiweeks |
| `regions` | regions | `list` of [region](https://github.com/cmu-delphi/delphi-epidata/blob/main/labels/regions.txt) labels |

### Optional

| Parameter | Description | Type |
| --- | --- | --- |
| `issues` | issues | `list` of epiweeks |
| `lag` | # weeks between each epiweek and its issue | integer |

Notes:
- If both `issues` and `lag` are specified, only `issues` is used.
If neither is specified, the current issues are used.

## Response

| Field | Description | Type |
| --- | --- | --- |
| `result` | result code: 1 = success, 2 = too many results, -2 = no results | integer |
| `epidata` | list of results | array of objects |
| `epidata[].release_date` | | string |
| `epidata[].region` | | string |
| `epidata[].issue` | | integer |
| `epidata[].epiweek` | | integer |
| `epidata[].lag` | | integer |
| `epidata[].total_specimens` | | integer |
| `epidata[].total_a` | | integer |
| `epidata[].total_b` | | integer |
| `epidata[].percent_positive` | | float |
| `epidata[].percent_a` | | float |
| `epidata[].percent_b` | | float |
| `message` | `success` or error message | string |

# Example URLs

### FluView Clinical on 2020w01 (national)
https://delphi.cmu.edu/epidata/fluview_clinical/?regions=nat&epiweeks=202001

```json
{
  "result": 1,
  "epidata": [
    {
      "release_date": "2020-04-10",
      "region": "nat",
      "issue": 202014,
      "epiweek": 202001,
      "lag": 13,
      "total_specimens": 64980,
      "total_a": 5651,
      "total_b": 9647,
      "percent_positive": 23.5426,
      "percent_a": 8.69652,
      "percent_b": 14.8461
    },
    ...
  ],
  "message": "success"
}
```


# Code Samples

Libraries are available for [JavaScript](https://github.com/cmu-delphi/delphi-epidata/blob/main/src/client/delphi_epidata.js), [Python](https://pypi.org/project/delphi-epidata/), and [R](https://github.com/cmu-delphi/delphi-epidata/blob/dev/src/client/delphi_epidata.R).
The following samples show how to import the library and fetch national FluView Clinical data for epiweeks `201940` and `202001-202010` (11 weeks total).

### JavaScript (in a web browser)

````html
<!-- Imports -->
<script src="delphi_epidata.js"></script>
<!-- Fetch data -->
<script>
  EpidataAsync.fluview_clinical('nat', [201940, EpidataAsync.range(202001, 202010)]).then((res) => {
    console.log(res.result, res.message, res.epidata != null ? res.epidata.length : 0);
  });
</script>
````

### Python

Optionally install the package using pip(env):
````bash
pip install delphi-epidata
````

Otherwise, place `delphi_epidata.py` from this repo next to your python script.

````python
# Import
from delphi_epidata import Epidata
# Fetch data
res = Epidata.fluview_clinical(['nat'], [201940, Epidata.range(202001, 202010)])
print(res['result'], res['message'], len(res['epidata']))
````

### R

````R
# Import
source('delphi_epidata.R')
# Fetch data
res <- Epidata$fluview_clinical(list('nat'), list(201940, Epidata$range(202001, 202010)))
cat(paste(res$result, res$message, length(res$epidata), "\n"))
````
