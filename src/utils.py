# standard library
import requests
import urllib


def calc_recall(tps_no: int, fns_no: int):
    return tps_no / (tps_no + fns_no)


def calc_precision(tps_no: int, fps_no: int):
    return tps_no / (tps_no + fps_no)


def calc_f1(recall: int, precision: int):
    return 2 * (precision * recall) / (precision + recall)


class Gazetteer:
    def __init__(self, gazetteer_source: str = "nominatm"):
        self.gazetteer_source = gazetteer_source
        self.base_url = "https://nominatim.openstreetmap.org/"
        self.session = requests.Session()
        self.cache = {}

    def nominatim_query(self, location: str) -> dict:
        # build url
        location = urllib.parse.quote(location)
        url_metainfo = self.base_url + f"search?q={location}&format=geocodejson"
        url_metainfo += (
            "&polygon_geojson=1&addressdetails=1&namedetails=1&accept-language=en"
        )

        # API call
        r_metainfo = self.session.get(
            url_metainfo, timeout=20, headers={"User-agent": None}
        )

        # Example: check if the API request was successful
        assert (
            r_metainfo.status_code == 200
        ), f"Unexpected status code: {r_metainfo.status_code}"

        r_metainfo_json = r_metainfo.json()
        self.cache.update({"query": r_metainfo_json})

        return r_metainfo_json
