function openPayment(name, price) {
    const modal = document.getElementById('paymentModal');
    if (modal) {
        modal.style.display = 'flex';
        document.getElementById('tour-name-display').innerText = name;
        document.getElementById('tour-price-display').innerText = price.toLocaleString();
    }
}

function closePayment() {
    const modal = document.getElementById('paymentModal');
    if (modal) {
        modal.style.display = 'none';
    }
}

// Модалдык терезенин сыртын басканда жабылышы
window.onclick = function(event) {
    let modal = document.getElementById('paymentModal');
    if (event.target == modal) {
        closePayment();
    }
}

// Төлөм формасын иштетүү
const checkoutForm = document.getElementById('checkout-form');
if (checkoutForm) {
    checkoutForm.onsubmit = function(e) {
        e.preventDefault();
        const btn = e.target.querySelector('.btn-pay-submit');
        const originalText = btn.innerText;

        btn.innerText = "Төлөм аткарылууда...";
        btn.style.opacity = "0.7";

        setTimeout(() => {
            alert("Төлөм ийгиликтүү өттү! Сиздин брондооңуз тастыкталды.");
            closePayment();
            btn.innerText = originalText;
            btn.style.opacity = "1";
        }, 2000);
    }
}