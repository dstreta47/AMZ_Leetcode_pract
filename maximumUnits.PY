  def maximumUnits(self, boxTypes, truckSize):
    boxTypes.sort(key=lambda a:-a[1])
    max_units = 0
    for box in boxTypes:
      if truckSize < 0 : break
        max_units += min(truckSize, box[0]) * box[1]
        truckSize -= box[0]
      return max_units
