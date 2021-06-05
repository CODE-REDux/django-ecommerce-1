var updateBtns = document.getElementsByClassName('update-cart')

// add an event handler to each button
for (var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId: ', productId, 'action: ', action)

        // this user variable is available as we are inheriting it from main.html
        console.log('USER', user)
        if (user == 'AnonymousUser') {
            console.log('User is not authenticated')
        }
        else {
            console.log('User is authenticated, sending data...')
        }
    })


}