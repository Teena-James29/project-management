document.addEventListener("DOMContentLoaded", function () {
    const ctx = document.getElementById('clientChart');

    if (ctx) {
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['Jan','Feb','Mar','Apr','May','Jun'],
                datasets: [
                    {
                        label: 'US',
                        data: [12, 19, 10, 25, 18, 30],
                        borderColor: '#5f3bff',
                        tension: 0.4
                    },
                    {
                        label: 'UK',
                        data: [8, 12, 6, 18, 15, 22],
                        borderColor: '#ff6b6b',
                        tension: 0.4
                    }
                ]
            }
        });
    }
});