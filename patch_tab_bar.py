import re

def update_file(filename, old_str, new_str):
    with open(filename, 'r') as f:
        content = f.read()
    
    if old_str in content:
        content = content.replace(old_str, new_str)
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"String not found in {filename}")

old_tab_home = '''    <!-- Bottom Navigation -->
    <div class="fixed bottom-0 left-0 right-0 bg-[#211F26] border-t border-[#36343B] px-4 py-1.5 max-w-md mx-auto z-30">
        <div class="flex items-center justify-around">
            <button onclick="switchTab('home')" id="nav-home" class="flex flex-col items-center gap-0.5 px-4 py-1.5 rounded-full transition-colors bg-[#4A4458]">
                <i data-lucide="home" class="w-5 h-5 fill-[#D0BCFF] text-[#D0BCFF]"></i>
                <span class="text-[10px] text-[#D0BCFF]">Home</span>
            </button>
            <button onclick="goToMenu()" id="nav-menu" class="flex flex-col items-center gap-0.5 px-4 py-1.5 rounded-full transition-colors">
                <i data-lucide="file-text" class="w-5 h-5 text-[#CAC4D0]"></i>
                <span class="text-[10px] text-[#CAC4D0]">Menu</span>
            </button>
            <button onclick="switchTab('cart')" id="nav-cart" class="relative flex flex-col items-center gap-0.5 px-4 py-1.5 rounded-full transition-colors">
                <i data-lucide="shopping-bag" class="w-5 h-5 text-[#CAC4D0]"></i>
                <div id="cart-badge" class="hidden absolute top-0.5 right-2 w-4 h-4 bg-[#F2B8B5] rounded-full flex items-center justify-center">
                    <span id="cart-count" class="text-[9px] text-[#601410] font-bold">0</span>
                </div>
                <span class="text-[10px] text-[#CAC4D0]">Cart</span>
            </button>
            <button onclick="switchTab('profile')" id="nav-profile" class="flex flex-col items-center gap-0.5 px-4 py-1.5 rounded-full transition-colors">
                <i data-lucide="user" class="w-5 h-5 text-[#CAC4D0]"></i>
                <span class="text-[10px] text-[#CAC4D0]">Profile</span>
            </button>
        </div>
    </div>'''

new_tab_home = '''    <!-- Bottom Navigation -->
    <div class="fixed bottom-0 left-0 right-0 bg-[#211F26] border-t border-[#36343B] px-2 pt-1 pb-[14px] max-w-md mx-auto z-30">
        <div class="flex items-center justify-around">
            <button onclick="switchTab('home')" id="nav-home" class="flex flex-col items-center justify-center h-11 w-16 rounded-xl transition-colors bg-[#4A4458]">
                <i data-lucide="home" class="w-5 h-5 fill-[#D0BCFF] text-[#D0BCFF]"></i>
                <span class="text-[10px] leading-none mt-0.5 text-[#D0BCFF]">Home</span>
            </button>
            <button onclick="goToMenu()" id="nav-menu" class="flex flex-col items-center justify-center h-11 w-16 rounded-xl transition-colors">
                <i data-lucide="file-text" class="w-5 h-5 text-[#CAC4D0]"></i>
                <span class="text-[10px] leading-none mt-0.5 text-[#CAC4D0]">Menu</span>
            </button>
            <button onclick="switchTab('cart')" id="nav-cart" class="relative flex flex-col items-center justify-center h-11 w-16 rounded-xl transition-colors">
                <i data-lucide="shopping-bag" class="w-5 h-5 text-[#CAC4D0]"></i>
                <div id="cart-badge" class="hidden absolute top-0 right-2 w-3.5 h-3.5 bg-[#F2B8B5] rounded-full flex items-center justify-center">
                    <span id="cart-count" class="text-[8px] text-[#601410] font-bold">0</span>
                </div>
                <span class="text-[10px] leading-none mt-0.5 text-[#CAC4D0]">Cart</span>
            </button>
            <button onclick="switchTab('profile')" id="nav-profile" class="flex flex-col items-center justify-center h-11 w-16 rounded-xl transition-colors">
                <i data-lucide="user" class="w-5 h-5 text-[#CAC4D0]"></i>
                <span class="text-[10px] leading-none mt-0.5 text-[#CAC4D0]">Profile</span>
            </button>
        </div>
    </div>'''

update_file('home.html', old_tab_home, new_tab_home)

old_tab_menu = '''    <!-- Bottom Navigation -->
    <div class="fixed bottom-0 left-0 right-0 bg-[#211F26] border-t border-[#36343B] px-4 py-1.5 max-w-md mx-auto z-[60]">
        <div class="flex items-center justify-around">
            <button onclick="navigateTo('home.html?tab=home')" class="flex flex-col items-center gap-0.5 px-4 py-1.5 rounded-full transition-colors">
                <i data-lucide="home" class="w-5 h-5 text-[#CAC4D0]"></i>
                <span class="text-[10px] text-[#CAC4D0]">Home</span>
            </button>
            <button onclick="navigateTo('home.html?tab=menu')" class="flex flex-col items-center gap-0.5 px-4 py-1.5 rounded-full transition-colors bg-[#4A4458]">
                <i data-lucide="file-text" class="w-5 h-5 text-[#D0BCFF] fill-[#D0BCFF]"></i>
                <span class="text-[10px] text-[#D0BCFF]">Menu</span>
            </button>
            <button onclick="navigateTo('home.html?tab=cart')" class="relative flex flex-col items-center gap-0.5 px-4 py-1.5 rounded-full transition-colors">
                <i data-lucide="shopping-bag" class="w-5 h-5 text-[#CAC4D0]"></i>
                <div id="cart-badge" class="hidden absolute top-0.5 right-2 w-4 h-4 bg-[#F2B8B5] rounded-full flex items-center justify-center">
                    <span id="cart-count" class="text-[9px] text-[#601410] font-bold">0</span>
                </div>
                <span class="text-[10px] text-[#CAC4D0]">Cart</span>
            </button>
            <button onclick="navigateTo('home.html?tab=profile')" class="flex flex-col items-center gap-0.5 px-4 py-1.5 rounded-full transition-colors">
                <i data-lucide="user" class="w-5 h-5 text-[#CAC4D0]"></i>
                <span class="text-[10px] text-[#CAC4D0]">Profile</span>
            </button>
        </div>
    </div>'''

new_tab_menu = '''    <!-- Bottom Navigation -->
    <div class="fixed bottom-0 left-0 right-0 bg-[#211F26] border-t border-[#36343B] px-2 pt-1 pb-[14px] max-w-md mx-auto z-[60]">
        <div class="flex items-center justify-around">
            <button onclick="navigateTo('home.html?tab=home')" class="flex flex-col items-center justify-center h-11 w-16 rounded-xl transition-colors">
                <i data-lucide="home" class="w-5 h-5 text-[#CAC4D0]"></i>
                <span class="text-[10px] leading-none mt-0.5 text-[#CAC4D0]">Home</span>
            </button>
            <button onclick="navigateTo('home.html?tab=menu')" class="flex flex-col items-center justify-center h-11 w-16 rounded-xl transition-colors bg-[#4A4458]">
                <i data-lucide="file-text" class="w-5 h-5 text-[#D0BCFF] fill-[#D0BCFF]"></i>
                <span class="text-[10px] leading-none mt-0.5 text-[#D0BCFF]">Menu</span>
            </button>
            <button onclick="navigateTo('home.html?tab=cart')" class="relative flex flex-col items-center justify-center h-11 w-16 rounded-xl transition-colors">
                <i data-lucide="shopping-bag" class="w-5 h-5 text-[#CAC4D0]"></i>
                <div id="cart-badge" class="hidden absolute top-0 right-2 w-3.5 h-3.5 bg-[#F2B8B5] rounded-full flex items-center justify-center">
                    <span id="cart-count" class="text-[8px] text-[#601410] font-bold">0</span>
                </div>
                <span class="text-[10px] leading-none mt-0.5 text-[#CAC4D0]">Cart</span>
            </button>
            <button onclick="navigateTo('home.html?tab=profile')" class="flex flex-col items-center justify-center h-11 w-16 rounded-xl transition-colors">
                <i data-lucide="user" class="w-5 h-5 text-[#CAC4D0]"></i>
                <span class="text-[10px] leading-none mt-0.5 text-[#CAC4D0]">Profile</span>
            </button>
        </div>
    </div>'''

update_file('menu.html', old_tab_menu, new_tab_menu)

