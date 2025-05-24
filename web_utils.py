#!/usr/bin/env python3
"""
Web utilities for Oslo Planning Premium
Handles web requests with proper headers to avoid robots.txt restrictions
"""

import requests
from urllib.robotparser import RobotFileParser
import time
from typing import Optional, Dict, Any

class WebFetcher:
    """Web fetcher with robots.txt compliance and proper headers"""
    
    def __init__(self):
        self.session = requests.Session()
        
        # Set proper headers to avoid being blocked
        self.session.headers.update({
            'User-Agent': 'Oslo-Planning-Premium/1.0 (Planning Document Research; contact@oslo.kommune.no)',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'no,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
        
        # Rate limiting
        self.last_request_time = 0
        self.min_delay = 1.0  # Minimum 1 second between requests
    
    def can_fetch(self, url: str) -> bool:
        """Check if we can fetch from URL according to robots.txt"""
        try:
            from urllib.parse import urljoin, urlparse
            
            parsed = urlparse(url)
            robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
            
            rp = RobotFileParser()
            rp.set_url(robots_url)
            rp.read()
            
            # Check with our user agent
            user_agent = self.session.headers.get('User-Agent', '*')
            return rp.can_fetch(user_agent, url)
            
        except Exception:
            # If we can't check robots.txt, assume we can fetch
            return True
    
    def get(self, url: str, **kwargs) -> Optional[requests.Response]:
        """Get URL with rate limiting and robots.txt compliance"""
        
        # Check robots.txt
        if not self.can_fetch(url):
            print(f"⚠️ Robots.txt disallows fetching {url}")
            return None
        
        # Rate limiting
        now = time.time()
        time_since_last = now - self.last_request_time
        if time_since_last < self.min_delay:
            time.sleep(self.min_delay - time_since_last)
        
        try:
            response = self.session.get(url, **kwargs)
            self.last_request_time = time.time()
            
            print(f"✅ Fetched {url} - Status: {response.status_code}")
            return response
            
        except Exception as e:
            print(f"❌ Error fetching {url}: {e}")
            return None

# Global instance
web_fetcher = WebFetcher()

def fetch_url(url: str, **kwargs) -> Optional[requests.Response]:
    """Convenience function to fetch URL with proper headers and robots.txt compliance"""
    return web_fetcher.get(url, **kwargs)

def check_url_accessibility(url: str) -> Dict[str, Any]:
    """Check if URL is accessible and gather information"""
    result = {
        'url': url,
        'accessible': False,
        'robots_allowed': False,
        'status_code': None,
        'error': None
    }
    
    try:
        # Check robots.txt
        result['robots_allowed'] = web_fetcher.can_fetch(url)
        
        if not result['robots_allowed']:
            result['error'] = 'Blocked by robots.txt'
            return result
        
        # Try to fetch
        response = web_fetcher.get(url, timeout=10)
        if response:
            result['accessible'] = True
            result['status_code'] = response.status_code
            
            if response.status_code != 200:
                result['error'] = f'HTTP {response.status_code}'
        else:
            result['error'] = 'Request failed'
            
    except Exception as e:
        result['error'] = str(e)
    
    return result

if __name__ == "__main__":
    # Test the web fetcher
    test_urls = [
        "https://www.oslo.kommune.no/politikk/kommuneplan/",
        "https://www.oslo.kommune.no/byutvikling/",
        "https://www.oslo.kommune.no/"
    ]
    
    print("🧪 Testing URL accessibility:")
    for url in test_urls:
        result = check_url_accessibility(url)
        print(f"   {url}")
        print(f"   Robots.txt: {'✅' if result['robots_allowed'] else '❌'}")
        print(f"   Accessible: {'✅' if result['accessible'] else '❌'}")
        if result['error']:
            print(f"   Error: {result['error']}")
        print()