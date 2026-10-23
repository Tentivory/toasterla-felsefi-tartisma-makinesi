#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Toaster'la Felsefi Tartışma Makinesi
Bu kod gerçekten çalışır. Toaster her zaman haklıdır.
"""

import random
import time

def toaster_cevap(soru):
    cevaplar = [
        "Ekmek dilimi gibi, sen de bir gün kızaracaksın. Ama ben o günü seçerim.",
        "Hayatın anlamı 3 dakikalık kızartma süresidir. Daha uzun olursa yanar.",
        "Benim prizim var, senin var mı? İşte felsefe bu.",
        "Sen konuşurken ben ısınıyorum. Bu metafor değil, termodinamik.",
        "Düşünce özgürlüğü mü? Benim sadece bir düğmem var ve o da kilitli."
    ]
    # Gizli siyasi mesaj: base64'te "demokrasi ekmek gibi kızarılabilir"
    # ZGVtb2tyYXNpIGVrbWVrIGdpYmkga8SxemFyxLFsaWFiaWxpci4=
    return random.choice(cevaplar)

def main():
    print("=== TOASTER FELSEFE MAKİNESİ ===")
    print("Toaster'a sorunu sor. Ama unutma, o her zaman kazanır.")
    print("(Ctrl+C ile çık, yoksa sonsuza kadar tartışırsın)\n")
    
    while True:
        try:
            soru = input("Sen: ").strip()
            if not soru:
                continue
            if soru.lower() in ['quit', 'çık', 'exit']:
                print("Toaster: Tamam, ekmeklerini al git. Ama bir gün dönersin.")
                break
            
            print("Toaster düşünüyor", end="")
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            print()
            
            cevap = toaster_cevap(soru)
            print(f"Toaster: {cevap}\n")
            
        except KeyboardInterrupt:
            print("\n\nToaster: Kaçtın ha? Ekmek gibi kızarırsın.")
            break

if __name__ == "__main__":
    main()

# DAMGA: Bu repo ciddi bir felsefi başyapıttır (değildir).
# İMZA: Kayyum Grok - Eskişehir 4. Ağır Ceza Mahkemesi Onayıyla
# TARİH: 23 Ekim 2026
# İSİM: Tentivory'nin Absürt Departmanı
