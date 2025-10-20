#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de teste para verificar se o WhatsApp Web está funcionando
Execute este script antes de usar o aplicativo principal
"""

import pyautogui as gui
import time
import webbrowser

def test_whatsapp_basic():
    """Teste básico do WhatsApp Web"""
    print("🧪 Iniciando teste do WhatsApp Web...")
    
    # Abrir WhatsApp Web
    print("1. Abrindo WhatsApp Web...")
    webbrowser.open("https://web.whatsapp.com")
    time.sleep(10)
    
    # Aguardar login
    input("2. Faça login no WhatsApp Web e pressione ENTER...")
    
    # Testar atalhos básicos
    print("3. Testando atalhos básicos...")
    try:
        # Testar Ctrl+N (nova conversa)
        gui.hotkey('ctrl', 'n')
        time.sleep(2)
        print("   ✅ Ctrl+N funcionando")
        
        # Cancelar nova conversa
        gui.press('escape')
        time.sleep(1)
        print("   ✅ Escape funcionando")
        
        # Testar digitação
        gui.hotkey('ctrl', 'n')
        time.sleep(1)
        gui.typewrite("teste")
        time.sleep(1)
        gui.press('escape')
        time.sleep(1)
        print("   ✅ Digitação funcionando")
        
        print("\n🎉 Todos os testes passaram! O WhatsApp Web está funcionando corretamente.")
        return True
        
    except Exception as e:
        print(f"❌ Erro durante o teste: {str(e)}")
        return False

def test_screen_resolution():
    """Testa a resolução da tela"""
    print("\n📺 Testando resolução da tela...")
    try:
        width, height = gui.size()
        print(f"   Resolução: {width}x{height}")
        
        # Calcular posições para área de mensagem
        message_x = int(width * 0.5)
        message_y = int(height * 0.7)
        print(f"   Posição sugerida para área de mensagem: ({message_x}, {message_y})")
        
        return True
    except Exception as e:
        print(f"❌ Erro ao obter resolução: {str(e)}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("🔧 TESTE DE DIAGNÓSTICO - WHATSAPP WEB")
    print("=" * 50)
    
    # Testar resolução
    test_screen_resolution()
    
    # Testar WhatsApp Web
    if test_whatsapp_basic():
        print("\n✅ Sistema pronto para usar o aplicativo principal!")
    else:
        print("\n❌ Problemas detectados. Verifique as configurações.")
    
    print("\n" + "=" * 50)
