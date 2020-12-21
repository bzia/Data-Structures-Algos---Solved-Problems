/**
 * @param {number[]} nums
 * @return {number}
 */

 var numIdenticalPairs = function(nums) {
    let obj = {};
    let count = 0;

    for (val of nums) {
      if (obj[val]) {
        count += obj[val];
        obj[val]++;
      } else {
        obj[val] = 1;
      }
    }
    console.log(obj);
    return count;
};

// Time Complexity: O(n)
// Space Complexity: O(n)

