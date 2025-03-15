import 'package:flutter/material.dart';

class ParkingMap extends StatelessWidget {
  const ParkingMap({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        decoration: const BoxDecoration(
          image: DecorationImage(
            image: AssetImage('assets/parking_lot.jpg'),
            fit: BoxFit.cover,
          ),
        ),
      ),
    );
  }
}