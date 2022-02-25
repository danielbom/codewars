# https://www.codewars.com/kata/find-the-smallest-integer-in-the-array/train/r
# My solution
findSmallestInt <- function(arr){
    return(min(arr))
}

# ...
findSmallestInt <- function(arr){
    arr[arr==min(arr)]
}

# ...
findSmallestInt <- function(arr) {
    min <- arr[1]

    for (x in arr) {
        if (x < min) {
            min = x
        }
    }
    
    return(min)
}

# ...
findSmallestInt <- function(arr){
    return = min(arr) 
}

# ...
findSmallestInt <- function(arr){
    x <- sort(arr, decreasing = FALSE)
    return(x[1])
}

# ...
findSmallestInt <- function(arr){
    min(arr)# assumes array is numeric, and all values are integers. 
}

# ...
findSmallestInt <- function(arr){
    arr[which(arr == min(arr))]
}

# ...
findSmallestInt <- function(arr){
    arr[which.min(arr)]
}