import redis



db = redis.Redis(host='redis', port=6379, db=0)