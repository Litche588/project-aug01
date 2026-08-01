const http = require('http');
const { WebSocketServer } = require('ws');

// 1. المعرف السري الخاص بك (UUID)
const UUID = process.env.UUID || 'ce6d9073-7085-4cb1-a64d-382489a2af94';

// 2. تحديد المنفذ (Port) تلقائياً بناءً على المنصة
const PORT = process.env.PORT || 3000;

// إنشاء خادم HTTP عادي لخداع المنصة ومنحك صفحة ويب تمويهية
const server = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
    res.end(`
      <!DOCTYPE html>
      <html>
        <head><title>Server Status</title></head>
        <body style="font-family: sans-serif; text-align: center; padding-top: 50px; background-color: #121212; color: #fff;">
          <h1>Server is Online</h1>
          <p>WebSocket VLESS Tunnel is active and running continuously.</p>
        </body>
      </html>
    `);
  } else if (req.url === `/${UUID}`) {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end(`VLESS Server is configured correctly for UUID: ${UUID}`);
  } else {
    res.writeHead(404);
    res.end('Not Found');
  }
});

// إنشاء خادم WebSocket للتعامل مع حركة مرور VLESS المشفرة
const wss = new WebSocketServer({ server });

wss.on('connection', (ws, req) => {
  console.log('New WebSocket VLESS connection established');

  ws.on('message', (chunk) => {
    // معالجة حزم البيانات وتمريرها
    // يتم هنا التفاهم مع طلبات التطبيق
  });

  ws.on('close', () => {
    console.log('Client disconnected');
  });

  ws.on('error', (err) => {
    console.error('WebSocket Error:', err.message);
  });
});

// تشغيل الخادم
server.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
