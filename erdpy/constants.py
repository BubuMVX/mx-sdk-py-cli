VM_TYPE_SYSTEM = "0001"
VM_TYPE_WASM_VM = "0500"
SC_HEX_PUBKEY_PREFIX = "0" * 16
SC_HEX_PUBKEY_PREFIX_SYSTEM = SC_HEX_PUBKEY_PREFIX + VM_TYPE_SYSTEM + "0" * 30
SC_HEX_PUBKEY_PREFIX_WASM_VM = SC_HEX_PUBKEY_PREFIX + VM_TYPE_WASM_VM
