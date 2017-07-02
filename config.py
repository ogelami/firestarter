worker = 'modermodemet'
wallet = '1ChM1MDWwH2F58F923oq3e8bVKpFtTVS3L'
maxIdleTime = 50
stdOutBufferRows = 50

pools = {
  'nicehash-daggerhashimoto' : {
    'host' : 'daggerhashimoto.eu.nicehash.com',
    'port' : '3353',
    'password' : 'x',
    'arguments' : '--cuda -S ###host###:###port### -O ###wallet###.###worker###:###password### --api-port 4001 --cuda-devices 0 --dag-load-mode singlekeep 0',
    'binaryPath' : 'miner\\ethminer\\ethminer.exe',
    'minerName' : 'Ethminer'
  },
  'ob-test' : {
    'host' : '-',
    'port' : '-',
    'password' : '-',
    'arguments' : '-u miner\\ob-test\\ob.py',
    'binaryPath' : 'python',
    'minerName' : 'obTest'
  },
  'nicehash-lyra2rev2' : {
    'host' : 'lyra2rev2.eu.nicehash.com',
    'port' : '3347',
    'password' : 'x',
    'arguments' : '-a lyra2v2 -o stratum+tcp://###host###:###port### -b 4003 -O ###wallet###.###worker###:###password### -x socks://127.0.0.1:8123',
    'binaryPath' : 'miner\\ccminer_tpruvot\\ccminer.exe',
    'minerName' : 'ccminer_tpruvot'
  },
  'nicehash-cryptonight' : {
    'host' : '37.58.117.214',
    'port' : '3355',
    'password' : 'x',
    'arguments' : '-a cryptonight -o stratum+tcp://###host###:###port### -b 4002 -O ###wallet###.###worker###:###password### -x socks://127.0.0.1:8123',
    'binaryPath' : 'miner\\cpuminer-multi\\cpuminer-gw64-core2.exe',
    'minerName' : 'cpuminerMulti'
  },
  'minergate-cryptonight' : {
    'host' : 'bcn.pool.minergate.com',
    'port' : '45550',
    'password' : 'x',
    'arguments' : '-a cryptonight -o stratum+tcp://###host###:###port### -b 4002 -O ###wallet###.###worker###:###password###',
    'binaryPath' : 'miner\\cpuminer-multi\\cpuminer-gw64-core2.exe',
    'minerName' : 'cpuminerMulti'
  }
}