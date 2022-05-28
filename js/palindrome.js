exports.palindrome = function(word) {
    if(isNaN(word)){
        let newWord = word.toLowerCase()
        let testWord = newWord.split('').reverse('').join('')
        return (newWord == testWord)? true: false     
    }else{
        let numWord = word.toString()
        let testNumWord = numWord.split('').reverse('').join('')
        return (numWord == testNumWord)? true : false
    } 
}
