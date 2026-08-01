const http = require('http');
const net = require('net');
const { WebSocketServer } = require('ws');

const UUID = (process.env.UUID || 'ce6d9073-7085-4cb1-a64d-382489a2af94').replace(/-/g, '');
const PORT = process.env.PORT || 3000;

// 1. خادم HTTP مموه لإرضاء المنصة
const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  res.end(`
    <!DOCTYPE html>
    <html>
      <head><title>Server Status</title></head>
      <body style="font-family: sans-serif; text-align: center; padding-top: 50px; background-color: #121212; color: #fff;">
        <h1>Server Status: Active</h1>
        <p>WebSocket VLESS Tunnel is active and running continuously.</p>
      </body>
    </html>
  `);
});

// 2. خادم WebSocket لمعالجة بروتوكول VLESS
const wss = new WebSocketServer({ server });

wss.on('connection', (ws) => {
  let remoteSocket = null;

  ws.on('message', (chunk) => {
    if (remoteSocket) {
      remoteSocket.write(chunk);
      return;
    }

    // التحقق من الحد الأدنى لطول حزمة VLESS
    if (chunk.length < 24) return;

    // استخراج الـ UUID القادم من التطبيق
    const clientUUID = chunk.slice(1, 17).toString('hex');
    if (clientUUID !== UUID) {
      ws.close();
      return;
    }

    // استخراج معلومات العنوان والمنفذ الهدف
    const optLength = chunk[17];
    const command = chunk[18 + optLength]; // 1 = TCP
    if (command !== 1) {
      ws.close();
      return;
    }

    const portIndex = 19 + optLength;
    const port = chunk.readUInt16BE(portIndex);
    const addressType = chunk[portIndex + 2];
    let address = '';
    let addressEndIndex = portIndex + 3;

    if (addressType === 1) { // IPv4
      address = chunk.slice(addressEndIndex, addressEndIndex + 4).join('.');
      addressEndIndex += 4;
    } else if (addressType === 2) { // Domain Name
      const domainLen = chunk[addressEndIndex];
      addressEndIndex += 1;
      address = chunk.slice(addressEndIndex, addressEndIndex + domainLen).toString('binary');
      addressEndIndex += domainLen;
    } else if (addressType === 3) { // IPv6
      address = chunk.slice(addressEndIndex, addressEndIndex + 16).toString('hex');
      addressEndIndex += 16;
    }

    const rawData = chunk.slice(addressEndIndex);

    // إنشاء اتصال TCP مباشر نحو الهدف
    remoteSocket = net.connect(port, address, () => {
      // إرسال استجابة VLESS Header للعميل للتأكيد
      ws.send(Buffer.from([chunk[0], 0]));
      if (rawData.length > 0) remoteSocket.write(rawData);
    });

    remoteSocket.on('data', (data) => {
      if (ws.readyState === ws.OPEN) ws.send(data);
    });

    remoteSocket.on('error', () => ws.close());
    remoteSocket.on('close', () => ws.close());
  });

  ws.on('close', () => {
    if (remoteSocket) remoteSocket.destroy();
  });

  ws.on('error', () => {
    if (remoteSocket) remoteSocket.destroy();
  });
});

server.listen(PORT, () => {
  console.log(`VLESS WebSocket Server running on port ${PORT}`);
});
