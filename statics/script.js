document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('addBlockForm');
    const blockchainElement = document.getElementById('blockchain');
    const transactionForm = document.getElementById('transactionForm');
    const pendingTransactionsElement = document.getElementById('pendingTransactions');

    // Add block
    if (form) {
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
    }

    // Add transaction
    if (transactionForm) {
        transactionForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const sender = document.getElementById('sender').value;
            const receiver = document.getElementById('receiver').value;
            const amount = document.getElementById('amount').value;

            const transaction = {
                sender: sender,
                receiver: receiver,
                amount: amount
            };

            fetch('/add_transaction', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(transaction)
            })
                .then(response => response.json())
                .then(data => {
                    console.log('Transaction added:', data);
                    updatePendingTransactions();
                })
                .catch(error => console.error('Error:', error));
        });
    }

    // Update blockchain
    function updateBlockchain() {
        fetch('/chain')
            .then(response => response.json())
            .then(data => {
                blockchainElement.textContent = JSON.stringify(data, null, 2);
            })
            .catch(error => console.error('Error:', error));
    }

    // Update pending transactions
    function updatePendingTransactions() {
        fetch('/pending_transactions')
            .then(response => response.json())
            .then(data => {
                pendingTransactionsElement.textContent = JSON.stringify(data, null, 2);
            })
            .catch(error => console.error('Error:', error));
    }

    // Initial load
    updateBlockchain();
    updatePendingTransactions();
});
