worker = 'modermodemet'
wallet = '1ChM1MDWwH2F58F923oq3e8bVKpFtTVS3L'
maxIdleTime = 5
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
    'cryptonight' : {
      'host' : 'cryptonight.eu.nicehash.com',
      'port' : '3355',
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

miner = {
  'docker_cpuminer_opt' : {
    'binaryPath' : 'docker',
    'algorithmSupport' : [
      'argon2',
      'axiom',
      'bastion',
      'blake',
      'blakecoin',
      'blake2s',
      'bmw',
      'c11',
      'cryptolight',
      'cryptonight',
      'decred',
      'deep',
      'dmd-gr',
      'drop',
      'fresh',
      'groestl',
      'heavy',
      'hmq1725',
      'hodl',
      'jha',
      'keccak',
      'lbry',
      'luffa',
      'lyra2re',
      'lyra2rev2',
      'lyra2z',
      'lyra2z330',
      'm7m',
      'myr-gr',
      'neoscrypt',
      'nist5',
      'pluck',
      'pentablake',
      'quark',
      'qubit',
      'scrypt',
      'scrypt:N',
      'scryptjane:nf',
      'sha256d',
      'sha256t',
      'shavite3',
      'skein',
      'skein2',
      'timetravel',
      'timetravel10',
      'tribus',
      'vanilla',
      'veltor',
      'whirlpool',
      'whirlpoolx',
      'x11',
      'x11evo',
      'x11gost',
      'x13',
      'x14',
      'x15',
      'x17',
      'xevan',
      'yescrypt',
      'zr5'
    ],
    'hardwareSupport' : ['cpu']
  },
  'excavator' : {
    'binaryPath' : 'miner/excavator/excavator.exe',
    'algorithmSupport' : [
      'equihash',
      'sia',
      'lbry',
      'daggerhashimoto',
      'pascal',
      'blake2s',
      'decred'
    ],
    'hardwareSupport' : []
  },
  'ethminer' : {
    'binaryPath' : 'miner/ethminer/ethminer.exe',
    'algorithmSupport' : ['daggerhashimoto'],
    'hardwareSupport' : ['CUDA', 'OpenCL']
  },
  'ccminer' : {
    'binaryPath' : 'miner/ccminer_tpruvot/ccminer.exe',
    'algorithmSupport' : [
      'blake',
      'blake2s',
      'blakecoin',
      'bmw',
      'c11/flax',
      'decred',
      'deep',
      'dmd-gr',
      'fresh',
      'fugue256',
      'groestl',
      'heavy',
      'jackpot',
      'keccak',
      'lbry',
      'luffa',
      'lyra2',
      'lyra2v2',
      'mjollnir',
      'myr-gr',
      'neoscrypt',
      'nist5',
      'penta',
      'quark',
      'qubit',
      'sia',
      'sib',
      'scrypt',
      'scrypt-jane',
      'skein',
      'skein2',
      's3',
      'vanilla',
      'veltor',
      'whirlcoin',
      'whirlpool',
      'x11evo',
      'x11',
      'x13',
      'x14',
      'x15',
      'x17',
      'zr5'
    ],
    'hardwareSupport' : ['CUDA']
  }
}
