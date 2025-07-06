import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import HomeScreen from './src/screens/HomeScreen';
import LoginScreen from './src/screens/LoginScreen';
import RegisterScreen from './src/screens/RegisterScreen';

const Stack = createNativeStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator
        initialRouteName="Login"
        screenOptions={{
          headerShown: false, // Oculta el header por defecto
          animation: 'slide_from_right', // Animación suave entre pantallas (opcional)
        }}
      >
        <Stack.Screen
          name="Login"
          component={LoginScreen}
          // headerShown false ya está aplicado por defecto
        />
        <Stack.Screen
          name="Register"
          component={RegisterScreen}
          options={{
            headerShown: true,    // Muestra header solo en Register
            title: 'Registro',
            headerBackTitle: 'Volver' // Texto del botón "Back"
          }}
        />
        <Stack.Screen
          name="Home"
          component={HomeScreen}
          options={{
            headerShown: true,    // Muestra header en Home
            title: 'Inicio',
            headerBackVisible: false // Oculta botón "Back" para que no regresen al login
          }}
        />
        {/* Aquí podrías añadir ForgotPassword, Settings, etc */}
      </Stack.Navigator>
    </NavigationContainer>
  );
}
