import 'package:flutter/material.dart';

class HelloWorld extends StatelessWidget {
  const HelloWorld({super.key});
  @override
  Widget build(BuildContext context) {
    return const Text(
      'Hello World!',
      style: TextStyle(
        fontSize: 25,
        color: Colors.blueGrey,
        fontWeight: FontWeight.w800,
      ),
    );
  }
}
