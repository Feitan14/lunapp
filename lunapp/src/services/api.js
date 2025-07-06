const BASE_URL = 'http://10.0.2.2:8000'; // Cambia esto según tu backend

// Registro de usuario
export const register = async (email, password) => {
  try {
    const response = await fetch(`${BASE_URL}/register`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email, password })
    });

    // Devuelve JSON siempre para que puedas ver el resultado
    return await response.json();
  } catch (error) {
    console.error('Error en register:', error);
    throw error;
  }
};

// Login de usuario
export const login = async (email, password) => {
  try {
    const response = await fetch(`${BASE_URL}/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email, password })
    });

    return await response.json();
  } catch (error) {
    console.error('Error en login:', error);
    throw error;
  }
};

// 📝 Aquí puedes agregar más funciones, por ejemplo:

// Obtener lista de transacciones
export const getTransactions = async (token) => {
  try {
    const response = await fetch(`${BASE_URL}/transactions`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });
    return await response.json();
  } catch (error) {
    console.error('Error al obtener transacciones:', error);
    throw error;
  }
};

// Crear una nueva transacción
export const createTransaction = async (token, data) => {
  try {
    const response = await fetch(`${BASE_URL}/transactions`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(data)
    });
    return await response.json();
  } catch (error) {
    console.error('Error al crear transacción:', error);
    throw error;
  }
};
