# https://www.codewars.com/kata/easy-wallpaper/train/r
# My solution
numbers_0_20 = c("zero","one","two","three","four","five",
                  "six","seven","eight","nine","ten",
                  "eleven","twelve","thirteen","fourteen","fifteen",
                  "sixteen","seventeen","eighteen","nineteen","twenty")

more_15_percent <- function (value) {
    return(value + value * 0.15)
}

wallpaper <- function (length, width, height) {
    wall_in_square_meters = height * length * 2 + height * width * 2
    wall_in_square_meters = more_15_percent(wall_in_square_meters)
    rolls = wall_in_square_meters/5.2 + 1
    return(numbers_0_20[ceiling(rolls)])
}

# ...
wallpaper <- function (l, w, h) {
    switch(ceiling(2.3*h*(l + w) / 5.2) + 1,
        "zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
        "twenty")
}

# ...
wallpaper <- function (l, w, h) {
  numbers<-c("one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
  numbers[trunc(2*(l+w)*h/.52*1.15/10)+1]
}