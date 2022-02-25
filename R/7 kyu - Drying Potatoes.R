# https://www.codewars.com/kata/drying-potatoes/train/r
# My solution
potatoes <- function (initial_percentage, weight, final_percentage) {
    initial_percentage_of_dry_matter = (100-initial_percentage)/100
    final_percentage_of_dry_matter = (100-final_percentage)/100
    dry_matter = initial_percentage_of_dry_matter * weight
    # percentage_of_dry_matter * weight = x
    final_weight = dry_matter / final_percentage_of_dry_matter
    # to avoid float storage errors, a small constant is added
    return(trunc(final_weight + 0.00003)) # trunc() or as.integer()
}

# ...
potatoes <- function (p0, w0, p1) {
    floor(w0 * (100 - p0) / (100 - p1))
}

# ...
# @param
# p0 - initial humidity percent
# w0 - initial weight
# p1 - final humidity percent

potatoes <- function (p0, w0, p1){
 
 ####################################################################
 # THERE IS MISTAKE IN TESTS!!! p0 AND p1 SHOULD BE A PERCENTAGE!!! #
 ####################################################################
 
  if(any(c(p0,p1) < 0) || any(c(p0,p1) > 1)){
    warning(paste0("bad parameters p0 or p1. It should be a percentage.
      Sent: p0=",p0," w0=",w0," p1=",p1))
  }
  
  if(w0 < 0){
    warning(paste0("bad parameter w0. It should be +integer.
      Sent: p0=",p0," w0=",w0," p1=",p1))
  }
  
  
  
  materyWeightPercentage0 <- 100 - p0
  materyWeightPercentage1 <- 100 - p1
  materyWeight <- w0 * materyWeightPercentage0 / 100 #final
  
  as.integer(100 / materyWeightPercentage1 * materyWeight)
}