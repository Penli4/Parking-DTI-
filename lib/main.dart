import 'package:flutter/material.dart';
import 'login_screen.dart';
import 'parking_map.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      initialRoute: '/',
      routes: {
        '/': (context) => const LoginScreen(),
        '/parking_lot': (context) => const ParkingMap(),
      },
    );
  }
}