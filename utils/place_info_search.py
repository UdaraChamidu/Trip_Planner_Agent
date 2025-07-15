import os
import json
from langchain_tavily import TavilySearch
from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper 
import requests

# class GooglePlaceSearchTool:
#     def __init__(self, api_key: str):
#         self.places_wrapper = GooglePlacesAPIWrapper(gplaces_api_key=api_key)
#         self.places_tool = GooglePlacesTool(api_wrapper=self.places_wrapper)
    
#     def google_search_attractions(self, place: str) -> dict:
#         """
#         Searches for attractions in the specified place using GooglePlaces API.
#         """
#         return self.places_tool.run(f"top attractive places in and around {place}")
    
#     def google_search_restaurants(self, place: str) -> dict:
#         """
#         Searches for available restaurants in the specified place using GooglePlaces API.
#         """
#         return self.places_tool.run(f"what are the top 10 restaurants and eateries in and around {place}?")
    
#     def google_search_activity(self, place: str) -> dict:
#         """
#         Searches for popular activities in the specified place using GooglePlaces API.
#         """
#         return self.places_tool.run(f"Activities in and around {place}")

#     def google_search_transportation(self, place: str) -> dict:
#         """
#         Searches for available modes of transportation in the specified place using GooglePlaces API.
#         """
#         return self.places_tool.run(f"What are the different modes of transportations available in {place}")

class TavilyPlaceSearchTool:
    def __init__(self):
        pass

    def tavily_search_attractions(self, place: str) -> dict:
        """
        Searches for attractions in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"top attractive places in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_restaurants(self, place: str) -> dict:
        """
        Searches for available restaurants in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"what are the top 10 restaurants and eateries in and around {place}."})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_activity(self, place: str) -> dict:
        """
        Searches for popular activities in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"activities in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

    def tavily_search_transportation(self, place: str) -> dict:
        """
        Searches for available modes of transportation in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"What are the different modes of transportations available in {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    
class HerePlaceSearchTool:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://discover.search.hereapi.com/v1/discover"

    def search_places(self, place: str, query: str, limit=10):
        params = {
            "q": query,
            "at": "0,0",  # Optional: You can try geocoding `place` to get lat,lng
            "limit": limit,
            "apiKey": self.api_key
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            results = [item["title"] for item in data.get("items", [])]
            return results if results else f"No results found for {query} in {place}"
        else:
            return f"HERE API error: {response.status_code}"

    def here_search_attractions(self, place: str):
        return self.search_places(place, f"tourist attractions in {place}")

    def here_search_restaurants(self, place: str):
        return self.search_places(place, f"restaurants in {place}")

    def here_search_activity(self, place: str):
        return self.search_places(place, f"things to do in {place}")

    def here_search_transportation(self, place: str):
        return self.search_places(place, f"public transportation in {place}")