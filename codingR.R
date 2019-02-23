input_ints <- c(4,1,1,1,1,2,2,2,3,3,3,3,3,3)

findTopTwo <- function(input_ints){
  unique_ints <- unique(input_ints)
  result <- data.frame(cbind(unique_ints,Count=as.numeric(0)))
  
  for (input_int in input_ints) {
    for (unique_int in unique_ints){
      if (input_int == unique_int){
        result$Count[result$unique_ints==input_int]=result$Count[result$unique_ints==input_int]+1
      }
    }
  }
  
  head(result[order(-result$Count),]$unique_ints,2)
}

findTopTwo(input_ints)
