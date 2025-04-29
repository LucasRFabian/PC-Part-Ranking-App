function setupAutocomplete(id, options) {
    const input = document.getElementById(id);
    input.addEventListener('input', function() {
        const value = this.value;
        closeAllLists();
        if (!value) return false;
        const list = document.createElement("div");
        list.setAttribute("id", this.id + "autocomplete-list");
        list.setAttribute("class", "autocomplete-items list-group");
        this.parentNode.appendChild(list);

        let i = 0;

        options.forEach(option => {
            if (option.toUpperCase().includes(value.toUpperCase())) {
                if (i >= 5) return; // Limits Query to 5 Items

                const item = document.createElement("div");
                // Highlight
                const index = option.toUpperCase().indexOf(value.toUpperCase());
                item.innerHTML = option.substr(0, index) +
                                "<strong>" + option.substr(index, value.length) + "</strong>" +
                                option.substr(index + value.length);
                                
                item.classList.add("list-group-item", "list-group-item-action");

                item.addEventListener("click", function() {
                    input.value = option;
                    closeAllLists();
                });

                list.appendChild(item);

                i++;
            }
        });
    });

    function closeAllLists(elmnt) {
        const items = document.getElementsByClassName("autocomplete-items");
        for (let i = 0; i < items.length; i++) {
            if (elmnt != items[i] && elmnt != input) {
                items[i].parentNode.removeChild(items[i]);
            }
        }
    }

    document.addEventListener("click", function (e) {
        closeAllLists(e.target);
    });
}