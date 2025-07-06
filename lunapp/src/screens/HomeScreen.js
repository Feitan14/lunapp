import AsyncStorage from '@react-native-async-storage/async-storage';
import { useEffect, useState } from 'react';
import { Button, Text, View } from 'react-native';

export default function HomeScreen({ navigation }) {
  const [token, setToken] = useState(null);

  useEffect(() => {
    const getToken = async () => {
      try {
        const storedToken = await AsyncStorage.getItem('access_token');
        if (storedToken) {
          setToken(storedToken);
        }
      } catch (error) {
        console.error('Error al leer token:', error);
      }
    };
    getToken();
  }, []);

  const handleLogout = async () => {
    await AsyncStorage.removeItem('access_token');
    navigation.navigate('Login');
  };

  return (
    <View style={{ padding: 20 }}>
      <Text style={{ fontSize: 18 }}>Bienvenido a HomeScreen</Text>
      <Text style={{ marginVertical: 10 }}>Token: {token ? token.substring(0, 20) + '...' : 'No hay token'}</Text>
      <Button title="Cerrar sesión" onPress={handleLogout} />
    </View>
  );
}

