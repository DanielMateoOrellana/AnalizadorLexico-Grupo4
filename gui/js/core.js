//Funcion para iniciar el servidor
// (function () {
//     // Get the path to the Python script.
//     var pythonScriptPath = "../../server.py";
//     // Run the Python script.
//     subprocess.run(["python", pythonScriptPath]);
// })();


// Función para agregar números de línea dinámicamente
function updateLineNumbers() {
    const textarea = document.getElementById('codeEditor');
    const lineNumbersDiv = document.querySelector('.line-numbers');
    
    // Obtener el número de líneas en el textarea
    const lines = textarea.value.split('\n').length;
    const numbers = Array.from({ length: lines }, (_, i) => i + 1);
    
    // Crear el HTML con los números de línea
    const lineNumbersHTML = numbers.map(num => `<div>${num}</div>`).join('');
    
    // Mostrar los números de línea en el div correspondiente
    lineNumbersDiv.innerHTML = lineNumbersHTML;
}

function scrollHeight(){
    const textarea = document.getElementById('codeEditor');
    textarea.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
    });
}

document.getElementById('runBtn').addEventListener('click', function() {
    const content = document.getElementById('codeEditor').value;

    fetch('http://localhost:8000', {
        method: 'POST',
        headers: {
            'Content-Type': 'text/plain'
        },
        body: content
    })
    .then(response => response.text())
    .then(data => {
        console.log('Respuesta del servidor:', data);
    })
    .catch(error => {
        console.error('Hubo un error:', error);
    });
    fetch('http://localhost:8000/execute_script', {
        method: 'POST'
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok on script exec');
        }
        return response.text();
    })
    .then(data => {
        console.log('Respuesta del servidor:', data);
    })
    .catch(error => {
        console.error('Hubo un error:', error);
    });
});

function getContent() {
    fetch('http://localhost:8000/get_content')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok on input read');
        }
        return response.text();
    })
    .then(data => {
        document.getElementById('codeEditor').value = data; // Establecer el contenido en el textarea
    })
    .catch(error => {
        console.error('Hubo un error:', error);
    });
}
function getContentOutput() {
    fetch('http://localhost:8000/get_output_content')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok on output read');
        }
        return response.text();
    })
    .then(data => {
        // const node = document.createTextNode(data);
        const sp1 = document.createElement("p");
        const br = document.createElement("br");
        sp1.id = "output_content"
        const sp1_content = document.createTextNode(data)
        sp1.appendChild(sp1_content)
        document.getElementById('console').replaceChild(sp1,sp1) // Establecer el contenido en el textarea
        document.getElementById('console').appendChild(br)
    })
    .catch(error => {
        console.error('Hubo un error:', error);
    });
}
getContent();
getContentOutput();

// Evento para actualizar los números de línea al escribir
document.getElementById('codeEditor').addEventListener('input', updateLineNumbers);

// Llamar a la función al cargar la página
updateLineNumbers();


/*
########################
Para iniciar el servidor
########################
*/

// const { spawn } = require('child_process');

// // Run a Python script and return output
// function runPythonScript(scriptPath) {

//   // Use child_process.spawn method from 
//   // child_process module and assign it to variable
//   const pyProg = spawn('python', [scriptPath]);

//   // Collect data from script and print to console
//   let data = '';
//   pyProg.stdout.on('data', (stdout) => {
//     data += stdout.toString();
//   });

//   // Print errors to console, if any
//   pyProg.stderr.on('data', (stderr) => {
//     console.log(`stderr: ${stderr}`);
//   });

//   // When script is finished, print collected data
//   pyProg.on('close', (code) => {
//     console.log(`child process exited with code ${code}`);
//     console.log(data);
//   });
// }

// // Run the Python file
// runPythonScript('../server.py');