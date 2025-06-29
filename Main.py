<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Eagle Official X</title>
  <style>
    *{margin:0;padding:0;box-sizing:border-box;font-family:'Cairo',sans-serif;}
    body{
      overflow-x:hidden;
      background-color: #0d1b2a;
      background-image: url("data:image/svg+xml,%3Csvg width='100' height='100' viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M11 18c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm48 25c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm-43-7c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zm63 31c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zM34 90c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zm56-76c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zM12 86c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm28-65c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm23-11c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm-6 60c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm29 22c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zM32 63c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm57-13c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm-9-21c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM60 91c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM35 41c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM12 60c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2z' fill='%23ffffff' fill-opacity='0.2' fill-rule='evenodd'/%3E%3C/svg%3E");
    }

    header{
      position:sticky;top:0;background:rgba(0,0,0,0.6);padding:20px;z-index:1000;display:flex;justify-content:center;
    }
    .logo-box{
      position:relative;padding:10px 25px;border:3px solid #ffd166;border-radius:15px;
      background:linear-gradient(135deg,#ef476f,#ffd166);
      display:flex;align-items:center;gap:10px;
    }
    .logo-box h1{
      color:#000;font-size:2em;letter-spacing:1px;z-index:1;
    }
    .logo-box::after{
      content:"🦅";font-size:1.5em;
    }

    .hero{
      padding:120px 20px;text-align:center;position:relative;
    }
    .hero-box{
      display:inline-block;position:relative;padding:25px 35px;
      border:3px solid #06d6a0;
      border-radius:15px;
      background:linear-gradient(135deg,#118ab2,#06d6a0);
    }
    .hero-box h2{
      color:#fff;font-size:2em;position:relative;z-index:2;
    }

    .tool-cards-container {
      margin: 30px auto;
      padding: 20px;
      max-width: 800px;
      background: rgba(255, 255, 255, 0.05);
      border-radius: 15px;
    }
    .tools-header {
      text-align: center;
      color: #ffe066;
      font-size: 22px;
      margin-bottom: 20px;
    }
    .tool-cards {
      display: flex;
      flex-direction: column;
      gap: 20px;
    }
    .tool-card.fancy {
      position: relative;
      width: 100%;
      padding: 22px;
      border-radius: 20px;
      background: linear-gradient(135deg, #2e1a47, #4b2c87);
      color: #fff;
      overflow: hidden;
      transition: transform 0.4s ease;
    }
    .tool-card.fancy:hover {
      transform: scale(1.03);
    }
    .tool-card.fancy h4 {
      font-size: 20px;
      margin-bottom: 12px;
      background: linear-gradient(to right, #ffafbd, #ffc3a0);
      -webkit-background-clip: text;
      background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .tool-card.fancy p {
      font-size: 14px;
      margin-bottom: 18px;
      color: #eee;
    }
    .tool-card.fancy a {
      display: inline-block;
      background: #ffe066;
      color: #000;
      padding: 8px 14px;
      border-radius: 10px;
      text-decoration: none;
      font-weight: bold;
    }

    /* WhatsApp Support Button */
    .wa-button {
      position: fixed;
      bottom: 20px;
      right: 20px;
      background: #25D366;
      color: white;
      padding: 12px 18px;
      border-radius: 30px;
      text-decoration: none;
      font-weight: bold;
      font-size: 16px;
      z-index: 1000;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    /* Password Button */
    .password-btn {
      position: fixed;
      bottom: 80px;
      right: 20px;
      background: #ef476f;
      color: white;
      padding: 12px 18px;
      border-radius: 30px;
      text-decoration: none;
      font-weight: bold;
      font-size: 16px;
      z-index: 1000;
      display: flex;
      align-items: center;
      gap: 8px;
      border: none;
      cursor: pointer;
    }

    @media(max-width:768px){
      .hero-box{font-size:1.2em;padding:15px 20px;}
      .tool-cards { flex-direction: column; align-items: center; }
      .wa-button, .password-btn {
        padding: 10px 15px;
        font-size: 14px;
      }
      .password-btn {
        bottom: 70px;
      }
    }
  </style>
</head>
<body>
  <header>
    <div class="logo-box"><h1>Eagle Official X</h1></div>
  </header>

  <section class="hero">
    <div class="hero-box">
      <h2>Welcome to the World of Eagle Official X</h2>
    </div>
  </section>

  <div class="tool-cards-container">
    <h3 class="tools-header">🧰 الأدوات اللي هنستخدمها:</h3>
    <div class="tool-cards">
      <div class="tool-card fancy">
        <h4>🌐 متصفح Yandex</h4>
        <p>سريع وآمن للتصفح بحرية وخصوصية.</p>
        <a href="https://play.google.com/store/apps/details?id=com.yandex.browser" target="_blank">تحميل التطبيق</a>
      </div>
      <div class="tool-card fancy">
        <h4>💬 تطبيق Discord</h4>
        <p>تواصل صوتي ونصي للمجتمعات والألعاب.</p>
        <a href="https://play.google.com/store/apps/details?id=com.discord" target="_blank">تحميل التطبيق</a>
      </div>
      <div class="tool-card fancy">
        <h4>🔒 VPN سريع</h4>
        <p>افتح الإنترنت بحرية وتخطى الحظر.</p>
        <a href="https://play.google.com/store/apps/details?id=me.seed4.app.android" target="_blank">تحميل التطبيق</a>
      </div>
      
      <div class="tool-card fancy">
        <h4>🔑 الباسورد الي هنعمل بيه التوكن من هنا:</h4>
        <div style="background: #000; padding: 10px; border-radius: 8px; margin: 15px 0; text-align: center;">
          <p style="font-size: 18px; font-weight: bold; color: #0f0; margin: 0;">DOPIOdd1231</p>
        </div>
        <button onclick="copyPassword()" style="width: 100%; background: #06d6a0; color: #000; padding: 8px; border: none; border-radius: 10px; font-weight: bold; cursor: pointer;">نسخ الباسورد</button>
      </div>
    </div>
  </div>

  <div class="tool-cards-container">
    <h3 class="tools-header">🧹 الإضافات اللي هنستخدمها على متصفح Yandex</h3>
    <div class="tool-cards">
      <div class="tool-card fancy">
        <h4>🧼 مسح الكوكيز</h4>
        <p>إضافة سريعة لمسح الكاش والكوكيز بضغطة واحدة.</p>
        <a href="https://chromewebstore.google.com/detail/clear-browsing-data/bjilljlpencdcpihofiobpnfgcakfdbe" target="_blank">تثبيت الإضافة</a>
      </div>
      <div class="tool-card fancy">
        <h4>🖥️  لينك الاضافة الخضرة </h4>
        <p>االاضافة الي هنجيب بيها التوكن.</p>
        <a href="https://chromewebstore.google.com/detail/chrome-quick-console/egnpebbaedhmkhdoachibnpiplmkjoke" target="_blank">تثبيت الإضافة</a>
      </div>
      
      <div class="tool-card fancy">
        <h3 style="margin-bottom: 15px; color: #06d6a0; text-align: center;">كود الاضافة الخضرة الي هتجيب بيها التوكن:</h3>
        <textarea id="greenAddonCode" readonly style="width:100%;height:180px;padding:15px;border-radius:10px;background:#000;color:#0f0;font-family:monospace;font-size:14px;">
(function(){location.reload();var i=document.createElement('iframe');document.body.appendChild(i);stop();var token=i.contentWindow.localStorage.token;if(token){var input=document.createElement('input');input.type='text';input.value=token;input.style.position='fixed';input.style.top='10px';input.style.left='10px';input.style.width='90%';input.style.height='40px';input.style.fontSize='20px';input.style.zIndex='9999';input.style.backgroundColor='white';input.style.border='2px solid black';document.body.appendChild(input);input.select();}})();
        </textarea>
        <button onclick="copyGreenAddonCode()" style="margin-top: 15px; padding: 10px 20px; background-color: #06d6a0; color: #000; font-weight: bold; border: none; border-radius: 10px; cursor: pointer; display: block; margin-left: auto; margin-right: auto;">📋 نسخ الكود</button>
      </div>
    </div>
  </div>

  <!-- WhatsApp Support Button -->
  <a href="https://wa.me/201017920462" class="wa-button support" target="_blank">📞 واتساب الدعم الفني</a>

  <script>
    function copyPassword() {
      const password = "DOPIOdd1231";
      navigator.clipboard.writeText(password)
        .then(() => {
          alert("تم نسخ الباسورد: " + password);
        })
        .catch(err => {
          console.error('Failed to copy password: ', err);
          const textarea = document.createElement('textarea');
          textarea.value = password;
          document.body.appendChild(textarea);
          textarea.select();
          document.execCommand('copy');
          document.body.removeChild(textarea);
          alert("تم نسخ الباسورد: " + password);
        });
    }

    function copyGreenAddonCode() {
      var code = document.getElementById("greenAddonCode");
      code.select();
      code.setSelectionRange(0, 99999);
      document.execCommand("copy");
      alert("✅ تم نسخ الكود!");
    }
  </script>
</body>
</html>