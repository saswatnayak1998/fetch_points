import math
from datetime import datetime

def count_alphanumeric(string):
  count = 0
  for char in string:
    if char.isalnum():
      count += 1
  return count

def calculate_points(receipt):
    points = 0
    
    points += count_alphanumeric(receipt['retailer'])
    
    total = float(receipt['total'])
    if total.is_integer():
        points += 50
    
    if total % 0.25 == 0:
        points += 25
    
    points += (len(receipt['items']) // 2) * 5
    
    # Points for item descriptions
    for item in receipt['items']:
        description = item['shortDescription'].strip()
        if len(description) % 3 == 0:
            points += math.ceil(float(item['price']) * 0.2)
    
    purchase_date = datetime.strptime(receipt['purchaseDate'], '%Y-%m-%d')
    if purchase_date.day % 2 == 1:  # Odd day
        points += 6
    
    purchase_time = datetime.strptime(receipt['purchaseTime'], '%H:%M')
    afternoon_start = datetime.strptime('14:00', '%H:%M')
    afternoon_end = datetime.strptime('16:00', '%H:%M')
    if afternoon_start.time() <= purchase_time.time() < afternoon_end.time():
        points += 10

    response = {"points": points}
    
    return response
    
