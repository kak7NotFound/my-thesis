fetch('http://127.0.0.1:5000/tests')
    .then(response => response.text()) // Преобразуем ответ в текст
    .then(html => {
        // Вставляем полученный HTML-код в элемент с id "content"
        console.log(html)
        document.getElementById("test_list").innerHTML = html;
    })
    .catch(error => {
        console.log('Ошибка при выполнении запроса:', error);
    });