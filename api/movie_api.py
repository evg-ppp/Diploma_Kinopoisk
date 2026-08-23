import requests

from config.config import API_KEY, API_URL


class MovieAPI:
    """Класс для работы с API Кинопоиска."""

    def __init__(self) -> None:
        self.headers = {
            "X-API-KEY": API_KEY
        }

    def _get(
            self,
            endpoint: str,
            params: dict | None = None
    ) -> requests.Response:
        """Выполнить GET-запрос к API."""

        return requests.get(
            f"{API_URL}{endpoint}",
            headers=self.headers,
            params=params
        )

    def get_movie(self, movie_id: int) -> requests.Response:
        """Получить информацию о фильме по ID."""

        return self._get(
            f"/v1.4/movie/{movie_id}"
        )

    def search_movie(
            self,
            name: str,
            page: int | None = None,
            limit: int | None = None
    ) -> requests.Response:
        """Поиск фильма по названию."""

        params = {
            "query": name
        }

        if page is not None:
            params["page"] = page

        if limit is not None:
            params["limit"] = limit

        return self._get(
            "/v1.4/movie/search",
            params=params
        )
