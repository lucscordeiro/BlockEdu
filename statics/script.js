document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('addBlockForm');
    const blockchainElement = document.getElementById('blockchain');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const blockData = document.getElementById('blockData').value;

        fetch(`/add_block/${encodeURIComponent(blockData)}`)
            .then(response => response.json())
            .then(data => {
                console.log('Block added:', data);
                updateBlockchain();
            })
            .catch(error => console.error('Error:', error));
    });

    function updateBlockchain() {
        fetch('/chain')
            .then(response => response.json())
            .then(data => {
                blockchainElement.textContent = JSON.stringify(data, null, 2);
            })
            .catch(error => console.error('Error:', error));
    }

    // Initial load
    updateBlockchain();
});
