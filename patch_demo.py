import re

def update_file(filename, replacements):
    with open(filename, 'r') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(filename, 'w') as f:
        f.write(content)

# 1. Update home.html
home_reps = [
    (
        '<!-- Bottom Navigation -->\n    <div class="fixed bottom-0 left-0 right-0 bg-[#211F26] border-t border-[#36343B] px-4 py-2 max-w-md mx-auto z-30">\n        <div class="flex items-center justify-around">\n            <button onclick="switchTab(\'home\')" id="nav-home" class="flex flex-col items-center gap-1 px-4 py-2 rounded-full transition-colors bg-[#4A4458]">\n                <i data-lucide="home" class="w-6 h-6 fill-[#D0BCFF] text-[#D0BCFF]"></i>\n                <span class="text-xs text-[#D0BCFF]">Home</span>\n            </button>\n            <button onclick="goToMenu()" id="nav-menu" class="flex flex-col items-center gap-1 px-4 py-2 rounded-full transition-colors">\n                <i data-lucide="file-text" class="w-6 h-6 text-[#CAC4D0]"></i>\n                <span class="text-xs text-[#CAC4D0]">Menu</span>\n            </button>\n            <button onclick="switchTab(\'cart\')" id="nav-cart" class="relative flex flex-col items-center gap-1 px-4 py-2 rounded-full transition-colors">\n                <i data-lucide="shopping-bag" class="w-6 h-6 text-[#CAC4D0]"></i>\n                <div id="cart-badge" class="hidden absolute top-1 right-2 w-5 h-5 bg-[#F2B8B5] rounded-full flex items-center justify-center">\n                    <span id="cart-count" class="text-xs text-[#601410] font-bold">0</span>\n                </div>\n                <span class="text-xs text-[#CAC4D0]">Cart</span>\n            </button>\n            <button onclick="switchTab(\'profile\')" id="nav-profile" class="flex flex-col items-center gap-1 px-4 py-2 rounded-full transition-colors">\n                <i data-lucide="user" class="w-6 h-6 text-[#CAC4D0]"></i>\n                <span class="text-xs text-[#CAC4D0]">Profile</span>\n            </button>\n        </div>\n    </div>',
        '<!-- Bottom Navigation -->\n    <div class="fixed bottom-0 left-0 right-0 bg-[#211F26] border-t border-[#36343B] px-4 py-1.5 max-w-md mx-auto z-30">\n        <div class="flex items-center justify-around">\n            <button onclick="switchTab(\'home\')" id="nav-home" class="flex flex-col items-center gap-0.5 px-4 py-1.5 rounded-full transition-colors bg-[#4A4458]">\n                <i data-lucide="home" class="w-5 h-5 fill-[#D0BCFF] text-[#D0BCFF]"></i>\n                <span class="text-[10px] text-[#D0BCFF]">Home</span>\n            </button>\n            <button onclick="goToMenu()" id="nav-menu" class="flex flex-col items-center gap-0.5 px-4 py-1.5 rounded-full transition-colors">\n                <i data-lucide="file-text" class="w-5 h-5 text-[#CAC4D0]"></i>\n                <span class="text-[10px] text-[#CAC4D0]">Menu</span>\n            </button>\n            <button onclick="switchTab(\'cart\')" id="nav-cart" class="relative flex flex-col items-center gap-0.5 px-4 py-1.5 rounded-full transition-colors">\n                <i data-lucide="shopping-bag" class="w-5 h-5 text-[#CAC4D0]"></i>\n                <div id="cart-badge" class="hidden absolute top-0.5 right-2 w-4 h-4 bg-[#F2B8B5] rounded-full flex items-center justify-center">\n                    <span id="cart-count" class="text-[9px] text-[#601410] font-bold">0</span>\n                </div>\n                <span class="text-[10px] text-[#CAC4D0]">Cart</span>\n            </button>\n            <button onclick="switchTab(\'profile\')" id="nav-profile" class="flex flex-col items-center gap-0.5 px-4 py-1.5 rounded-full transition-colors">\n                <i data-lucide="user" class="w-5 h-5 text-[#CAC4D0]"></i>\n                <span class="text-[10px] text-[#CAC4D0]">Profile</span>\n            </button>\n        </div>\n    </div>'
    ),
    (
        'cartItemsContainer.innerHTML = `<p class="text-[#CAC4D0] text-sm">Your cart is empty.</p>`;',
        'cartItemsContainer.innerHTML = `\n                    <div class="flex flex-col items-center justify-center py-8 text-center">\n                        <i data-lucide="shopping-bag" class="w-16 h-16 text-[#4A4458] mb-4"></i>\n                        <p class="text-[#E6E1E5] font-medium mb-1">Your cart is empty</p>\n                        <p class="text-[#CAC4D0] text-sm mb-4">Looks like you haven\'t added anything yet.</p>\n                        <button onclick="goToMenu()" class="px-6 py-2 bg-[#4A4458] text-[#D0BCFF] rounded-full text-sm font-medium hover:bg-[#36343B] transition-colors">Browse Menu</button>\n                    </div>\n                `;'
    ),
    (
        '<button onclick="placeOrder()" id="btn-place-order" disabled class="w-full bg-[#D0BCFF] text-[#381E72] font-semibold py-4 rounded-full hover:bg-[#E8DEF8] transition-colors disabled:opacity-50 disabled:cursor-not-allowed">\n                Place Order - RM 0.00\n            </button>',
        '<button onclick="placeOrder()" id="btn-place-order" disabled class="w-full flex items-center justify-center gap-2 bg-[#D0BCFF] text-[#381E72] font-semibold py-4 rounded-full hover:bg-[#E8DEF8] transition-colors disabled:opacity-50 disabled:cursor-not-allowed">\n                <i id="place-order-spinner" data-lucide="loader-2" class="w-5 h-5 animate-spin hidden"></i>\n                <span id="place-order-text">Place Order - RM 0.00</span>\n            </button>'
    ),
    (
        'function placeOrder() {\n            const cart = JSON.parse(localStorage.getItem(\'cart\') || \'[]\');\n            if (cart.length === 0) return;',
        'function placeOrder() {\n            const cart = JSON.parse(localStorage.getItem(\'cart\') || \'[]\');\n            if (cart.length === 0) return;\n\n            const btn = document.getElementById(\'btn-place-order\');\n            const spinner = document.getElementById(\'place-order-spinner\');\n            const text = document.getElementById(\'place-order-text\');\n            btn.disabled = true;\n            spinner.classList.remove(\'hidden\');\n            text.textContent = \'Processing Payment...\';\n\n            setTimeout(() => {'
    ),
    (
        'localStorage.setItem(\'activeOrder\', JSON.stringify(order));\n            localStorage.setItem(\'cart\', \'[]\');\n            navigateTo(\'tracking.html\');\n        }',
        'localStorage.setItem(\'activeOrder\', JSON.stringify(order));\n                localStorage.setItem(\'cart\', \'[]\');\n                navigateTo(\'tracking.html\');\n            }, 1500);\n        }'
    ),
    (
        'const btn = document.getElementById(\'btn-place-order\');\n                btn.disabled = true;\n                btn.textContent = `Place Order - RM 0.00`;',
        'const btn = document.getElementById(\'btn-place-order\');\n                btn.disabled = true;\n                const text = document.getElementById(\'place-order-text\');\n                if (text) text.textContent = `Place Order - RM 0.00`;\n                else btn.textContent = `Place Order - RM 0.00`;'
    ),
    (
        'const btn = document.getElementById(\'btn-place-order\');\n                btn.disabled = false;\n                btn.textContent = `Place Order - RM ${total.toFixed(2)}`;',
        'const btn = document.getElementById(\'btn-place-order\');\n                btn.disabled = false;\n                const text = document.getElementById(\'place-order-text\');\n                if (text) text.textContent = `Place Order - RM ${total.toFixed(2)}`;\n                else btn.textContent = `Place Order - RM ${total.toFixed(2)}`;'
    )
]
update_file('home.html', home_reps)


# 2. Update menu.html
menu_reps = [
    (
        '<!-- Bottom Navigation -->\n    <div class="fixed bottom-0 left-0 right-0 bg-[#211F26] border-t border-[#36343B] px-4 py-2 max-w-md mx-auto z-[60]">\n        <div class="flex items-center justify-around">\n            <button onclick="navigateTo(\'home.html?tab=home\')" class="flex flex-col items-center gap-1 px-4 py-2 rounded-full transition-colors">\n                <i data-lucide="home" class="w-6 h-6 text-[#CAC4D0]"></i>\n                <span class="text-xs text-[#CAC4D0]">Home</span>\n            </button>\n            <button onclick="navigateTo(\'home.html?tab=menu\')" class="flex flex-col items-center gap-1 px-4 py-2 rounded-full transition-colors bg-[#4A4458]">\n                <i data-lucide="file-text" class="w-6 h-6 text-[#D0BCFF] fill-[#D0BCFF]"></i>\n                <span class="text-xs text-[#D0BCFF]">Menu</span>\n            </button>\n            <button onclick="navigateTo(\'home.html?tab=cart\')" class="relative flex flex-col items-center gap-1 px-4 py-2 rounded-full transition-colors">\n                <i data-lucide="shopping-bag" class="w-6 h-6 text-[#CAC4D0]"></i>\n                <div id="cart-badge" class="hidden absolute top-1 right-2 w-5 h-5 bg-[#F2B8B5] rounded-full flex items-center justify-center">\n                    <span id="cart-count" class="text-xs text-[#601410] font-bold">0</span>\n                </div>\n                <span class="text-xs text-[#CAC4D0]">Cart</span>\n            </button>\n            <button onclick="navigateTo(\'home.html?tab=profile\')" class="flex flex-col items-center gap-1 px-4 py-2 rounded-full transition-colors">\n                <i data-lucide="user" class="w-6 h-6 text-[#CAC4D0]"></i>\n                <span class="text-xs text-[#CAC4D0]">Profile</span>\n            </button>\n        </div>\n    </div>',
        '<!-- Bottom Navigation -->\n    <div class="fixed bottom-0 left-0 right-0 bg-[#211F26] border-t border-[#36343B] px-4 py-1.5 max-w-md mx-auto z-[60]">\n        <div class="flex items-center justify-around">\n            <button onclick="navigateTo(\'home.html?tab=home\')" class="flex flex-col items-center gap-0.5 px-4 py-1.5 rounded-full transition-colors">\n                <i data-lucide="home" class="w-5 h-5 text-[#CAC4D0]"></i>\n                <span class="text-[10px] text-[#CAC4D0]">Home</span>\n            </button>\n            <button onclick="navigateTo(\'home.html?tab=menu\')" class="flex flex-col items-center gap-0.5 px-4 py-1.5 rounded-full transition-colors bg-[#4A4458]">\n                <i data-lucide="file-text" class="w-5 h-5 text-[#D0BCFF] fill-[#D0BCFF]"></i>\n                <span class="text-[10px] text-[#D0BCFF]">Menu</span>\n            </button>\n            <button onclick="navigateTo(\'home.html?tab=cart\')" class="relative flex flex-col items-center gap-0.5 px-4 py-1.5 rounded-full transition-colors">\n                <i data-lucide="shopping-bag" class="w-5 h-5 text-[#CAC4D0]"></i>\n                <div id="cart-badge" class="hidden absolute top-0.5 right-2 w-4 h-4 bg-[#F2B8B5] rounded-full flex items-center justify-center">\n                    <span id="cart-count" class="text-[9px] text-[#601410] font-bold">0</span>\n                </div>\n                <span class="text-[10px] text-[#CAC4D0]">Cart</span>\n            </button>\n            <button onclick="navigateTo(\'home.html?tab=profile\')" class="flex flex-col items-center gap-0.5 px-4 py-1.5 rounded-full transition-colors">\n                <i data-lucide="user" class="w-5 h-5 text-[#CAC4D0]"></i>\n                <span class="text-[10px] text-[#CAC4D0]">Profile</span>\n            </button>\n        </div>\n    </div>'
    ),
    ('pb-[72px]', 'pb-[56px]'),
    ('bottom-[72px]', 'bottom-[56px]'),
    (
        'document.getElementById(\'btn-add-to-cart\').textContent = `Add to Cart - RM ${calculateTotal().toFixed(2)}`;',
        'const btn = document.getElementById(\'btn-add-to-cart\');\n            btn.textContent = `Add to Cart - RM ${calculateTotal().toFixed(2)}`;\n            \n            // Animation pulse\n            btn.classList.add(\'scale-[1.02]\', \'bg-[#E8DEF8]\');\n            setTimeout(() => {\n                btn.classList.remove(\'scale-[1.02]\', \'bg-[#E8DEF8]\');\n            }, 150);'
    )
]
update_file('menu.html', menu_reps)


# 3. Update login.html
login_reps = [
    (
        '<div id="error-msg" class="hidden bg-[#601410] text-[#F2B8B5] px-4 py-3 rounded-xl text-sm"></div>',
        ''
    ),
    (
        '<button onclick="handleLogin()" class="w-full bg-[#D0BCFF] text-[#381E72] py-4 rounded-full font-semibold hover:bg-[#E8DEF8] transition-colors mb-4">\n            Sign In\n        </button>',
        '<button id="btn-login" onclick="handleLogin()" class="w-full flex items-center justify-center gap-2 bg-[#D0BCFF] text-[#381E72] py-4 rounded-full font-semibold hover:bg-[#E8DEF8] transition-colors mb-4">\n            <i id="login-spinner" data-lucide="loader-2" class="w-5 h-5 animate-spin hidden"></i>\n            <span id="login-text">Sign In</span>\n        </button>\n\n        <div id="toast" class="fixed bottom-10 left-1/2 -translate-x-1/2 bg-[#4A4458] text-[#EADDFF] px-6 py-3 rounded-full text-sm font-medium opacity-0 transition-opacity pointer-events-none z-50 whitespace-nowrap"></div>'
    ),
    (
        '        function handleLogin() {\n            const id = document.getElementById(\'identifier\').value;\n            const pwd = document.getElementById(\'password\').value;\n            const errorMsg = document.getElementById(\'error-msg\');\n\n            if (!id || !pwd) {\n                errorMsg.textContent = \'Please enter both fields.\';\n                errorMsg.classList.remove(\'hidden\');\n                return;\n            }\n\n            // Dummy login logic\n            if (id === \'staff\') {',
        '        function showToast(msg) {\n            const t = document.getElementById(\'toast\');\n            t.textContent = msg;\n            t.classList.replace(\'opacity-0\', \'opacity-100\');\n            setTimeout(() => t.classList.replace(\'opacity-100\', \'opacity-0\'), 2000);\n        }\n\n        function handleLogin() {\n            const id = document.getElementById(\'identifier\').value;\n            const pwd = document.getElementById(\'password\').value;\n            const btn = document.getElementById(\'btn-login\');\n            const spinner = document.getElementById(\'login-spinner\');\n            const text = document.getElementById(\'login-text\');\n\n            if (!id || !pwd) {\n                showToast(\'Please enter your credentials.\');\n                return;\n            }\n\n            btn.disabled = true;\n            spinner.classList.remove(\'hidden\');\n            text.textContent = \'Signing in...\';\n\n            setTimeout(() => {\n            // Dummy login logic\n            if (id === \'staff\') {'
    ),
    (
        '                localStorage.setItem(\'currentUser\', JSON.stringify({ role: \'customer\', name: \'Ahmad\', email: \'student@iium.edu.my\' }));\n                navigateTo(\'location.html\');\n            }\n        }',
        '                localStorage.setItem(\'currentUser\', JSON.stringify({ role: \'customer\', name: \'Ahmad\', email: \'student@iium.edu.my\' }));\n                navigateTo(\'location.html\');\n            }\n            }, 1000);\n        }'
    )
]
update_file('login.html', login_reps)


# 4. Update scanner.html
scanner_reps = [
    (
        '<!-- Camera View Simulation -->\n            <div class="w-full max-w-sm aspect-square bg-[#2B2930] rounded-3xl relative mb-6 overflow-hidden">',
        '<!-- Camera View Simulation -->\n            <div class="w-full max-w-sm aspect-square bg-[#2B2930] rounded-3xl relative mb-6 overflow-hidden">\n                <div id="flash-overlay" class="absolute inset-0 bg-white opacity-0 pointer-events-none transition-opacity duration-300 z-10"></div>'
    ),
    (
        '        function simulateScan() {\n            showSuccess();\n        }',
        '        function simulateScan() {\n            const flash = document.getElementById(\'flash-overlay\');\n            flash.classList.replace(\'opacity-0\', \'opacity-100\');\n            setTimeout(() => {\n                flash.classList.replace(\'opacity-100\', \'opacity-0\');\n                showSuccess();\n            }, 300);\n        }'
    )
]
update_file('scanner.html', scanner_reps)

print("Patch applied successfully.")
