# jambase_api

Python API wrapper for the [Jambase Concert API](https://www.jambase.com/concert-api)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install jambase_api.

```bash
pip install jambase_api
```

## API Keys
To get an API key, go to [Jambase](https://www.jambase.com/concert-api) and click Access API Docs in the upper right corner. As of this writing, their typical rate limit is a generous 3600 API calls per hour, which can be extended for an additional cost.

## Usage

```python
import jambase_api.jambase import Jambase

# initialize jambase object with your api key
jambase = Jambase(apikey='YOUR_API_KEY_HERE')

# returns list of states
states = jambase.get_states()

# search artists
artists = jambase.search_by_artist_by_name('goose')

# search events by venue
events = jambase.search_events_by_artist_name('taylor swift')
```

## Development setup

Clone this repo and install packages listed in requirements.txt
```python
pip3 install -r requirements.txt
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please add or update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
