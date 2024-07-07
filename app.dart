class Llama{

  Future<String> getResponse(String prompt) async {
    final url = Uri.parse('http://192.168.1.2:5000/api');  // Replace with your machine's IP address
    final headers = {'Content-Type': 'application/json'};
    final body = jsonEncode({
      "prompt": prompt
    });

    print("Send Data");

    try {
      final response = await http.post(url, headers: headers, body: body);
      print("Processing");
      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        print(data);
        return data;
      } else {
        return 'Failed to load prediction';
      }
    } catch (e) {
      print('Error: $e');
      return e.toString();
    }
  }
}
