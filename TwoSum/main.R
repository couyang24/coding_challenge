nums <- c(2, 7, 11, 15) 
target <-  9

for(inputIndex1 in 1:length(nums)){
  for(inputIndex2 in 1:(length(nums)-inputIndex1+1)){
    if((nums[inputIndex1]+nums[inputIndex2+inputIndex1-1]) == target){
      print(c(inputIndex1, inputIndex2+inputIndex1-1))
    }
  }
}
