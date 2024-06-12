import React from 'react';
import shell from 'shelljs';

class CommandExecutor extends React.Component {
  handleClick = () => {
    // Ejecutar el comando utilizando ShellJS
    const result = shell.exec('tu_comando_aqui');

    // Verificar el resultado de la ejecución del comando
    if (result.code === 0) {
      console.log('El comando se ejecutó correctamente');
      console.log('Salida estándar:', result.stdout);
    } else {
      console.error('Error al ejecutar el comando:', result.stderr);
    }
  }

  render() {
    return (
      <div>
        <h1>Script con React y ShellJS</h1>
        <button onClick={this.handleClick}>Ejecutar Comando</button>
      </div>
    );
  }
}

export default CommandExecutor;
