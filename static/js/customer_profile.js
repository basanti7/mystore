console.log('hello customer')

function findProfiles(){
    const searchValue = document.getElementById('customer_search').value.toLowerCase();
    const elements = document.getElementsByClassName('card');
    for (let elem of elements) {
        let element_nest = elem.querySelector('.card-title');
        // console.log(element_nest.innerHTML);
        if(!element_nest.innerHTML.toLowerCase().includes(searchValue)){
            elem.style.display = 'none';
        }else elem.style.display = '';
    }
}

function calculateTotalDue(){
    let due_elems = document.getElementsByClassName('due_count');
    let total = 0;
    let current_due = 0;
    for (let due_elem of due_elems){
        current_due = parseFloat(due_elem.innerHTML)
        total+=current_due
    }
    document.getElementById('due_display').innerHTML = total;
    // console.log(document.getElementById('due_display'))
}
calculateTotalDue();