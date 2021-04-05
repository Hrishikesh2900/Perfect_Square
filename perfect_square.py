def isPerfectSquare(x):
     
    left = 1
    right = x
     
    while (left <= right):
       
        mid = (left + right) >> 1
         
        # Check if mid is perfect square
        if ((mid * mid) == x):
            return True
         
        if (mid * mid < x):
            left = mid + 1
           
        else:
            right = mid - 1
    return False
if __name__ == "__main__":
   
  x = int(input("Please enter a number to check: "))
   
  # Function Call
  if (isPerfectSquare(x)):
      print("Yes")
  else:
      print("No")