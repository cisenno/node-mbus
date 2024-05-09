{
	'targets': [
		{
			'target_name': 'mbus',
			'cflags': [
                '-w'
			],
			'include_dirs': [
				'./libmbus/mbus',
				"<!(node -e \"require('nan')\")"
			],
			'sources': [
				'./src/main.cc',
				'./src/mbus-master.cc',
				'./src/util.cc'
			],
            'conditions': [
                ['OS=="mac"', {
                    'xcode_settings': {
                        'OTHER_CFLAGS': [
                            '-w'
                        ],
                    }

                }],
                ['OS=="win"', {
			        'defines': [
                        # Stop <windows.h> from defining macros that conflict with
                        # std::min() and std::max().  We don't use <windows.h> (much)
                        # but we still inherit it from uv.h.
                        'NOMINMAX',
                    ]
                }]
            ],
            'dependencies': [
                'libmbus'
            ]
		},
		{
			'target_name': 'libmbus',
            'type': 'static_library',
			'cflags': [
                '-w'
			],
			'include_dirs': [
				'./libmbus/mbus',
			],
			'sources': [
				'./libmbus/mbus/mbus-protocol-aux.c',
				'./libmbus/mbus/mbus-protocol.c',
				'./libmbus/mbus/mbus-serial.c',
				'./libmbus/mbus/mbus-tcp.c',
				'./libmbus/mbus/mbus.c'
			],
            'conditions': [
                ['OS=="mac"', {
                    'xcode_settings': {
                        'OTHER_CFLAGS': [
                            '-w'
                        ],
                    }
                }],
                ['OS=="win"', {
			        'sources': [
                        './libmbus/win/termiWin.c'
                    ]
                }]
            ]
		}
	]
}
