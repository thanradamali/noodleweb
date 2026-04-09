<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>เรือใบสั่ง - Noodle Pro System</title>
    <link href="https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        :root { --primary: #8b0000; --success: #28a745; --light: #f8f9fa; }
        body { font-family: 'Kanit', sans-serif; margin: 0; background: #fff; color: #333; }
        
        /* Header & Navigation */
        header { background: var(--primary); color: white; padding: 15px; text-align: center; position: sticky; top: 0; z-index: 1000; }
        .tabs { display: flex; overflow-x: auto; background: white; border-bottom: 1px solid #ddd; position: sticky; top: 61px; z-index: 999; }
        .tab-btn { padding: 15px 20px; border: none; background: none; white-space: nowrap; font-weight: 600; cursor: pointer; color: #666; font-family: 'Kanit'; }
        .tab-btn.active { color: var(--primary); border-bottom: 3px solid var(--primary); }

        /* Menu Display */
        .container { max-width: 1000px; margin: auto; padding: 15px; padding-bottom: 120px; }
        .menu-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 15px; }
        .card { border: 1px solid #eee; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.05); cursor: pointer; transition: 0.2s; }
        .card:hover { transform: scale(1.02); }
        .card img { width: 100%; height: 120px; object-fit: cover; background: #eee; }
        .card-body { padding: 10px; }
        .card-name { font-size: 14px; font-weight: 600; height: 38px; overflow: hidden; }
        .card-price { color: var(--primary); font-weight: bold; margin-top: 5px; }

        /* Modal / Drawer */
        .overlay { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.7); z-index: 2000; align-items: flex-end; justify-content: center; }
        .drawer { background: white; width: 100%; max-width: 500px; border-radius: 20px 20px 0 0; padding: 25px; box-sizing: border-box; max-height: 85vh; overflow-y: auto; }
        
        .option-box { margin-bottom: 20px; border-bottom: 1px solid #eee; padding-bottom: 15px; }
        .option-box h4 { margin: 0 0 10px 0; color: var(--primary); }
        .opt-label { display: flex; align-items: center; justify-content: space-between; background: #f4f4f4; padding: 12px; margin-bottom: 8px; border-radius: 10px; cursor: pointer; }
        .opt-label input { width: 18px; height: 18px; accent-color: var(--primary); }

        /* Bottom Bar */
        .bottom-bar { position: fixed; bottom: 0; left: 0; width: 100%; background: white; padding: 15px 25px; box-sizing: border-box; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 -5px 15px rgba(0,0,0,0.1); z-index: 1500; }
        .btn-order { background: var(--success); color: white; border: none; padding: 12px 30px; border-radius: 30px; font-weight: bold; font-size: 16px; cursor: pointer; font-family: 'Kanit'; }

        /* Review List */
        .review-item { display: flex; justify-content: space-between; border-bottom: 1px solid #eee; padding: 12px 0; }
        .detail-text { font-size: 12px; color: #777; display: block; }
        
        @media (max-width: 480px) { .menu-grid { grid-template-columns: 1fr 1fr; } }
    </style>
</head>
<body>

<header><h1>เรือใบสั่ง Noodle Bar</h1></header>

<div class="tabs">
    <button class="tab-btn active" onclick="filterMenu('ทั้งหมด', this)">ทั้งหมด</button>
    <button class="tab-btn" onclick="filterMenu('ก๋วยเตี๋ยว', this)">ก๋วยเตี๋ยว</button>
    <button class="tab-btn" onclick="filterMenu('เครื่องเคียง', this)">เครื่องเคียง</button>
    <button class="tab-btn" onclick="filterMenu('น้ำดื่ม', this)">น้ำดื่ม</button>
</div>

<div class="container">
    <div class="menu-grid" id="menuDisplay"></div>
</div>

<div class="overlay" id="optionOverlay">
    <div class="drawer">
        <h3 id="optTitle" style="margin-top:0;"></h3>
        <div class="option-box">
            <h4>ขนาด</h4>
            <label class="opt-label"><input type="radio" name="size" value="ธรรมดา" data-price="0" checked> ธรรมดา <span>+0฿</span></label>
            <label class="opt-label"><input type="radio" name="size" value="พิเศษ" data-price="25"> พิเศษ <span>+25฿</span></label>
        </div>
        <div class="option-box">
            <h4>เลือกเส้น</h4>
            <label class="opt-label"><input type="radio" name="noodle" value="เส้นเล็ก" checked> เส้นเล็ก</label>
            <label class="opt-label"><input type="radio" name="noodle" value="มาม่า"> มาม่า</label>
            <label class="opt-label"><input type="radio" name="noodle" value="วุ้นเส้น"> วุ้นเส้น</label>
            <label class="opt-label"><input type="radio" name="noodle" value="บะหมี่"> บะหมี่เหลือง</label>
            <label class="opt-label"><input type="radio" name="noodle" value="หมี่ขาว"> หมี่ขาว</label>
        </div>
        <div class="option-box">
            <h4>ตัวเลือกผัก</h4>
            <label class="opt-label"><input type="radio" name="veggie" value="ใส่ผักปกติ" checked> ใส่ผัก</label>
            <label class="opt-label"><input type="radio" name="veggie" value="ไม่ใส่ผัก"> ไม่ใส่ผัก</label>
        </div>
        <button class="btn-order" style="width:100%" onclick="addToCart()">เพิ่มลงใบสั่ง</button>
        <button onclick="closeDrawers()" style="width:100%; background:none; border:none; margin-top:10px; color:#999; cursor:pointer;">ยกเลิก</button>
    </div>
</div>

<div class="overlay" id="reviewOverlay">
    <div class="drawer">
        <h3>ใบสั่งอาหาร</h3>
        <div id="reviewList"></div>
        <div style="display:flex; justify-content:space-between; font-size:20px; font-weight:bold; margin-top:20px; border-top:2px solid #eee; padding-top:10px;">
            <span>ยอดรวม:</span> <span id="reviewTotal">0 ฿</span>
        </div>
        <button class="btn-order" style="width:100%; margin-top:20px;" onclick="confirmKitchen()">ยืนยันส่งเข้าครัว</button>
        <button onclick="closeDrawers()" style="width:100%; background:none; border:none; margin-top:10px; color:#999; cursor:pointer;">สั่งเพิ่ม</button>
    </div>
</div>

<div class="bottom-bar">
    <div>
        <div style="font-size:13px; color:#888;">สั่งแล้ว <span id="cartQty">0</span> จาน</div>
        <div style="font-size:20px; font-weight:bold; color:var(--primary);"><span id="cartTotal">0</span> ฿</div>
    </div>
    <button class="btn-order" onclick="openReview()">เช็ครายการ</button>
</div>

<script>
    const menus = [
        { id: '1', name: 'ก๋วยเตี๋ยวเรือเนื้อน้ำตก', cat: 'ก๋วยเตี๋ยว', price: 20, opt: true, img: 'https://via.placeholder.com/300/800000/FFFFFF?text=Beef' },
        { id: '2', name: 'ก๋วยเตี๋ยวเรือหมูน้ำตก', cat: 'ก๋วยเตี๋ยว', price: 20, opt: true, img: 'https://via.placeholder.com/300/8B4513/FFFFFF?text=Pork' },
        { id: '3', name: 'ก๋วยเตี๋ยวต้มยำหมู', cat: 'ก๋วยเตี๋ยว', price: 25, opt: true, img: 'https://via.placeholder.com/300/FF4500/FFFFFF?text=TomYum' },
        { id: '4', name: 'กากหมูเจียว', cat: 'เครื่องเคียง', price: 20, opt: false, img: 'https://via.placeholder.com/300?text=Lard' },
        { id: '5', name: 'แคบหมู', cat: 'เครื่องเคียง', price: 12, opt: false, img: 'https://via.placeholder.com/300?text=PorkRind' },
        { id: '6', name: 'เกี๊ยวทอด', cat: 'เครื่องเคียง', price: 12, opt: false, img: 'https://via.placeholder.com/300?text=Wonton' },
        { id: '7', name: 'แป๊ปซี่', cat: 'น้ำดื่ม', price: 15, opt: false, img: 'https://via.placeholder.com/300?text=Pepsi' },
        { id: '8', name: 'สไปรท์', cat: 'น้ำดื่ม', price: 15, opt: false, img: 'https://via.placeholder.com/300?text=Sprite' },
        { id: '9', name: 'แฟนตาส้ม', cat: 'น้ำดื่ม', price: 15, opt: false, img: 'https://via.placeholder.com/300?text=Orange' },
        { id: '10', name: 'แฟนตาเขียว', cat: 'น้ำดื่ม', price: 15, opt: false, img: 'https://via.placeholder.com/300?text=Green' },
        { id: '11', name: 'น้ำเปล่า', cat: 'น้ำดื่ม', price: 10, opt: false, img: 'https://via.placeholder.com/300?text=Water' },
        { id: '12', name: 'น้ำแข็ง (แก้ว)', cat: 'น้ำดื่ม', price: 2, opt: false, img: 'https://via.placeholder.com/300?text=Ice' }
    ];

    let cart = [];
    let activeItem = null;

    function renderMenu(items) {
        const display = document.getElementById('menuDisplay');
        display.innerHTML = items.map(item => `
            <div class="card" onclick="openOption('${item.id}')">
                <img src="${item.img}">
                <div class="card-body">
                    <div class="card-name">${item.name}</div>
                    <div class="card-price">${item.price} ฿</div>
                </div>
            </div>
        `).join('');
    }

    function openOption(id) {
        activeItem = menus.find(m => m.id === id);
        if(activeItem.opt) {
            document.getElementById('optTitle').innerText = activeItem.name;
            document.getElementById('optionOverlay').style.display = 'flex';
        } else {
            cart.push({ name: activeItem.name, price: activeItem.price, detail: 'ปกติ' });
            updateUI();
        }
    }

    function addToCart() {
        const sizeInput = document.querySelector('input[name="size"]:checked');
        const size = sizeInput.value;
        const addPrice = parseInt(sizeInput.getAttribute('data-price'));
        const noodle = document.querySelector('input[name="noodle"]:checked').value;
        const veggie = document.querySelector('input[name="veggie"]:checked').value;

        cart.push({
            name: `${activeItem.name} (${size})`,
            price: activeItem.price + addPrice,
            detail: `เส้น${noodle} / ${veggie}`
        });
        closeDrawers();
        updateUI();
    }

    function openReview() {
        if(cart.length === 0) return alert('กรุณาเลือกเมนูก่อนครับ');
        const list = document.getElementById('reviewList');
        list.innerHTML = cart.map((item, index) => `
            <div class="review-item">
                <div><strong>${item.name}</strong><small class="detail-text">${item.detail}</small></div>
                <div>${item.price} ฿ <button onclick="removeItem(${index})" style="color:red; border:none; background:none; cursor:pointer;">ลบ</button></div>
            </div>
        `).join('');
        document.getElementById('reviewTotal').innerText = cart.reduce((s,i)=>s+i.price,0) + " ฿";
        document.getElementById('reviewOverlay').style.display = 'flex';
    }

    function removeItem(index) {
        cart.splice(index, 1);
        if(cart.length === 0) closeDrawers(); else openReview();
        updateUI();
    }

    function updateUI() {
        document.getElementById('cartQty').innerText = cart.length;
        document.getElementById('cartTotal').innerText = cart.reduce((s,i)=>s+i.price,0);
    }

    function filterMenu(cat, btn) {
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        if(cat === 'ทั้งหมด') renderMenu(menus); else renderMenu(menus.filter(m => m.cat === cat));
    }

    function confirmKitchen() {
        alert('ส่งออเดอร์เข้าครัวเรียบร้อย!');
        cart = []; updateUI(); closeDrawers();
    }

    function closeDrawers() { document.querySelectorAll('.overlay').forEach(o => o.style.display = 'none'); }

    renderMenu(menus);
</script>
</body>
</html>
