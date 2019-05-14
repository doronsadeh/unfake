import dpath


class Cfg:
    config = {
        'sources': {
            'twitter': {
                'api': {
                    'consumer_key': 'yourkeyhere',
                    'consumer_secret': 'yourkeyhere',
                    'access_token': 'yourkeyhere',
                    'access_token_secret': 'yourkeyhere'
                }
            }
        }
    }

    def get(self, key):
        return dpath.get(key, separator='.')
