worker = 'modermodemet'
wallet = '1ChM1MDWwH2F58F923oq3e8bVKpFtTVS3L'
maxIdleTime = 50
stdOutBufferRows = 50

## hash template
#    '' : {
#      'host' : '',
#      'port' : '',
#      'username' : '',
#      'password' : ''
#    },

pools = {
  'nicehash' : {
    'daggerhashimoto' : {
      'host' : 'daggerhashimoto.eu.nicehash.com',
      'port' : '3353',
      'username' : '###wallet###.###worker###',
      'password' : 'x'
    },
    'lyra2rev2' : {
      'host' : 'lyra2rev2.eu.nicehash.com',
      'port' : '3347',
      'username' : '###wallet###.###worker###',
      'password' : 'x'
    },
   'equihash' : {
     'host' : 'equihash.eu.nicehash.com',
     'port' : '3357',
     'username' : '###wallet###.###worker###',
     'password' : 'x'
   },
   'sia' : {
     'host' : 'sia.eu.nicehash.com',
     'port' : '3360',
     'username' : '###wallet###.###worker###',
     'password' : 'x'
   }
  }
}

miners = {
  'excavator' : {
    'binaryPath' : 'miner\\excavator\\excavator.exe',
    'hashSupport' : ['equihash', 'sia', 'lbry', 'daggerhashimoto', 'pascal', 'blake2s', 'decred']
  },
  'ethminer' : {
    'binaryPath' : 'miner\\ethminer\\ethminer.exe',
    'hashSupport' : ['daggerhashimoto']
  },
  'ccminer' : {
    'binaryPath' : 'miner\\ccminer_tpruvot\\ccminer.exe',
    'hashSupport' : ['blake', 'blake2s', 'blakecoin', 'bmw', 'c11/flax', 'decred', 'deep', 'dmd-gr', 'fresh', 'fugue256', 'groestl', 'heavy', 'jackpot', 'keccak', 'lbry', 'luffa', 'lyra2', 'lyra2v2', 'mjollnir', 'myr-gr', 'neoscrypt', 'nist5', 'penta', 'quark', 'qubit', 'sia', 'sib', 'scrypt', 'scrypt-jane', 'skein', 'skein2', 's3', 'vanilla', 'veltor', 'whirlcoin', 'whirlpool', 'x11evo', 'x11', 'x13', 'x14', 'x15', 'x17', 'zr5']
  }
}

## old pool configuration
# pools = {
#   'nicehash-daggerhashimoto' : {
#     'host' : 'daggerhashimoto.eu.nicehash.com',
#     'port' : '3353',
#     'password' : 'x',
#     'arguments' : '--cuda -S ###host###:###port### -O ###wallet###.###worker###:###password### --api-port 4001 --cuda-devices 0 --dag-load-mode singlekeep 0',
#     'binaryPath' : 'miner\\ethminer\\ethminer.exe',
#     'minerName' : 'Ethminer'
#   },
#   'nicehash-equihash1' : {
#     'host' : 'equihash.eu.nicehash.com',
#     'port' : '3355',
#     'password' : 'x',
#     'arguments' : '-a equihash -s ###host###:###port### -u ###wallet###.###worker###:###password### -ca -ca',
#     'binaryPath' : 'miner\\excavator\\excavator.exe',
#     'minerName' : 'Ethminer'
#   },
#   'nicehash-lyra2rev2' : {
#     'host' : 'lyra2rev2.eu.nicehash.com',
#     'port' : '3347',
#     'password' : 'x',
#     'arguments' : '-a lyra2v2 -o stratum+tcp://###host###:###port### -b 4003 -O ###wallet###.###worker###:###password### -x socks://127.0.0.1:8123',
#     'binaryPath' : 'miner\\ccminer_tpruvot\\ccminer.exe',
#     'minerName' : 'ccminer_tpruvot'
#   },
#   'nicehash-equihash2' : {
#     'host' : 'equihash.eu.nicehash.com',
#     'port' : '3357',
#     'password' : 'x',
#     'arguments' : '-l ###host###:###port### -u ###wallet###.###worker### -cd 0',
#     'binaryPath' : 'miner\\nheqminer_v0.4b\\nheqminer.exe',
#     'minerName' : 'nheqminer_v0.4b'
#   },
#   'nicehash-cryptonight' : {
#     'host' : 'cryptonight.eu.nicehash.com',
#     'port' : '3355',
#     'password' : 'x',
#     'arguments' : '-a cryptonight -o stratum+tcp://###host###:###port### -b 4002 -O ###wallet###.###worker###:###password### -x socks://127.0.0.1:8123',
#     'binaryPath' : 'miner\\cpuminer-multi\\cpuminer-gw64-core2.exe',
#     'minerName' : 'cpuminerMulti'
#   },
#   'minergate-cryptonight' : {
#     'host' : 'bcn.pool.minergate.com',
#     'port' : '45550',
#     'password' : 'x',
#     'arguments' : '-a cryptonight -o stratum+tcp://###host###:###port### -b 4002 -O ###wallet###.###worker###:###password###',
#     'binaryPath' : 'miner\\cpuminer-multi\\cpuminer-gw64-core2.exe',
#     'minerName' : 'cpuminerMulti'
#   }
# }