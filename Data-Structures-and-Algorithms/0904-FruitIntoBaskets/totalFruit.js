const totalFruit = function(fruits) {
    basket = {};
    left = 0;
    counter = 0;

    if (fruits.length < 2) {
        return 1
    }
    
    for (var right = 0; right < fruits.length; right ++) {

       (basket[fruits[right]]) ? (basket[fruits[right]] ++) : (basket[fruits[right]] = 1);

        while (Object.keys(basket).length > 2) {
            basket[fruits[left]] -= 1;

            if (basket[fruits[left]] == 0) {
                delete basket[fruits[left]]
            }          
            
            left ++;    
        }

        counter = Math.max(counter, right - left + 1)
    }

    return counter

};

fruits = [3,3,3,1,2,1,1,2,3,3,4]
console.log(totalFruit(fruits))

// O(n) iteration through the whole array
// O(n) dictionary needed space to save information in basket
// Longest continuous subarray with 2 distinct values

