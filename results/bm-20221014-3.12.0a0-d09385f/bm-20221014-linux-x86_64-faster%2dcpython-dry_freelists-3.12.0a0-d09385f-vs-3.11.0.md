
# Results vs. 3.11.0

- fork: faster-cpython
- ref: dry_freelists
- machine: linux-x86_64
- commit hash: d09385f
- commit date: 2022-10-14
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 248 ms: 1.04x faster                                                     |
| chameleon      | 6.41 ms                                                | 6.46 ms: 1.01x slower                                                    |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                   |
| html5lib       | 63.2 ms                                                | 59.6 ms: 1.06x faster                                                    |
| tornado_http   | 96.6 ms                                                | 92.8 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.1 ms: 1.06x faster                                                    |
| pidigits       | 199 ms                                                 | 206 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.07x faster                                                     |
| regex_effbot   | 3.36 ms                                                | 3.43 ms: 1.02x slower                                                    |
| regex_dna      | 203 ms                                                 | 218 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.30 ms: 1.36x faster                                                    |
| json_loads           | 26.2 us                                                | 23.4 us: 1.12x faster                                                    |
| unpickle_pure_python | 225 us                                                 | 203 us: 1.11x faster                                                     |
| pickle_pure_python   | 304 us                                                 | 287 us: 1.06x faster                                                     |
| pickle_list          | 4.17 us                                                | 4.10 us: 1.02x faster                                                    |
| pickle_dict          | 31.4 us                                                | 31.1 us: 1.01x faster                                                    |
| xml_etree_generate   | 76.2 ms                                                | 75.6 ms: 1.01x faster                                                    |
| xml_etree_iterparse  | 103 ms                                                 | 102 ms: 1.01x faster                                                     |
| pickle               | 9.79 us                                                | 10.3 us: 1.05x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                             |

Benchmark hidden because not significant (4): unpickle, xml_etree_parse, unpickle_list, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 5.96 ms                                                | 5.94 ms: 1.00x faster                                                    |
| python_startup         | 8.36 ms                                                | 8.41 ms: 1.01x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 22.1 ms                                                | 20.8 ms: 1.06x faster                                                    |
| genshi_xml     | 52.1 ms                                                | 49.1 ms: 1.06x faster                                                    |
| mako           | 9.85 ms                                                | 9.89 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.30 ms: 1.36x faster                                                    |
| json_loads              | 26.2 us                                                | 23.4 us: 1.12x faster                                                    |
| deltablue               | 3.64 ms                                                | 3.27 ms: 1.12x faster                                                    |
| unpickle_pure_python    | 225 us                                                 | 203 us: 1.11x faster                                                     |
| json                    | 4.95 ms                                                | 4.48 ms: 1.11x faster                                                    |
| go                      | 143 ms                                                 | 131 ms: 1.10x faster                                                     |
| richards                | 46.2 ms                                                | 42.3 ms: 1.09x faster                                                    |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.05 ms: 1.09x faster                                                    |
| nqueens                 | 85.0 ms                                                | 78.9 ms: 1.08x faster                                                    |
| sqlalchemy_imperative   | 18.0 ms                                                | 16.7 ms: 1.08x faster                                                    |
| regex_compile           | 136 ms                                                 | 127 ms: 1.07x faster                                                     |
| scimark_sor             | 115 ms                                                 | 108 ms: 1.07x faster                                                     |
| logging_silent          | 98.5 ns                                                | 92.5 ns: 1.07x faster                                                    |
| coroutines              | 26.1 ms                                                | 24.5 ms: 1.06x faster                                                    |
| genshi_text             | 22.1 ms                                                | 20.8 ms: 1.06x faster                                                    |
| genshi_xml              | 52.1 ms                                                | 49.1 ms: 1.06x faster                                                    |
| html5lib                | 63.2 ms                                                | 59.6 ms: 1.06x faster                                                    |
| fannkuch                | 388 ms                                                 | 366 ms: 1.06x faster                                                     |
| pickle_pure_python      | 304 us                                                 | 287 us: 1.06x faster                                                     |
| float                   | 76.3 ms                                                | 72.1 ms: 1.06x faster                                                    |
| aiohttp                 | 1.05 ms                                                | 991 us: 1.06x faster                                                     |
| pycparser               | 1.17 sec                                               | 1.11 sec: 1.05x faster                                                   |
| logging_simple          | 6.06 us                                                | 5.76 us: 1.05x faster                                                    |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                                    |
| deepcopy_memo           | 36.4 us                                                | 34.7 us: 1.05x faster                                                    |
| mypy                    | 669 ms                                                 | 639 ms: 1.05x faster                                                     |
| pprint_pformat          | 1.44 sec                                               | 1.38 sec: 1.05x faster                                                   |
| sqlalchemy_declarative  | 139 ms                                                 | 133 ms: 1.05x faster                                                     |
| scimark_fft             | 329 ms                                                 | 315 ms: 1.05x faster                                                     |
| hexiom                  | 6.35 ms                                                | 6.08 ms: 1.04x faster                                                    |
| pyflate                 | 417 ms                                                 | 400 ms: 1.04x faster                                                     |
| sympy_expand            | 472 ms                                                 | 453 ms: 1.04x faster                                                     |
| deepcopy                | 344 us                                                 | 330 us: 1.04x faster                                                     |
| tornado_http            | 96.6 ms                                                | 92.8 ms: 1.04x faster                                                    |
| logging_format          | 6.62 us                                                | 6.37 us: 1.04x faster                                                    |
| async_tree_cpu_io_mixed | 752 ms                                                 | 724 ms: 1.04x faster                                                     |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                   |
| 2to3                    | 257 ms                                                 | 248 ms: 1.04x faster                                                     |
| scimark_monte_carlo     | 68.3 ms                                                | 65.9 ms: 1.04x faster                                                    |
| chaos                   | 68.6 ms                                                | 66.2 ms: 1.04x faster                                                    |
| bench_thread_pool       | 810 us                                                 | 782 us: 1.04x faster                                                     |
| pprint_safe_repr        | 691 ms                                                 | 670 ms: 1.03x faster                                                     |
| async_tree_none         | 529 ms                                                 | 514 ms: 1.03x faster                                                     |
| async_generators        | 359 ms                                                 | 349 ms: 1.03x faster                                                     |
| sqlglot_optimize        | 53.0 ms                                                | 51.5 ms: 1.03x faster                                                    |
| sympy_integrate         | 20.9 ms                                                | 20.3 ms: 1.03x faster                                                    |
| sympy_str               | 287 ms                                                 | 280 ms: 1.03x faster                                                     |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                     |
| coverage                | 101 ms                                                 | 98.3 ms: 1.02x faster                                                    |
| sympy_sum               | 166 ms                                                 | 162 ms: 1.02x faster                                                     |
| sqlglot_parse           | 1.37 ms                                                | 1.34 ms: 1.02x faster                                                    |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                                    |
| dulwich_log             | 63.9 ms                                                | 62.8 ms: 1.02x faster                                                    |
| pickle_list             | 4.17 us                                                | 4.10 us: 1.02x faster                                                    |
| deepcopy_reduce         | 2.97 us                                                | 2.92 us: 1.02x faster                                                    |
| sqlglot_transpile       | 1.66 ms                                                | 1.63 ms: 1.02x faster                                                    |
| thrift                  | 752 us                                                 | 742 us: 1.01x faster                                                     |
| mdp                     | 2.62 sec                                               | 2.59 sec: 1.01x faster                                                   |
| pickle_dict             | 31.4 us                                                | 31.1 us: 1.01x faster                                                    |
| xml_etree_generate      | 76.2 ms                                                | 75.6 ms: 1.01x faster                                                    |
| xml_etree_iterparse     | 103 ms                                                 | 102 ms: 1.01x faster                                                     |
| python_startup_no_site  | 5.96 ms                                                | 5.94 ms: 1.00x faster                                                    |
| mako                    | 9.85 ms                                                | 9.89 ms: 1.00x slower                                                    |
| async_tree_io           | 1.31 sec                                               | 1.31 sec: 1.01x slower                                                   |
| python_startup          | 8.36 ms                                                | 8.41 ms: 1.01x slower                                                    |
| chameleon               | 6.41 ms                                                | 6.46 ms: 1.01x slower                                                    |
| unpack_sequence         | 43.4 ns                                                | 44.0 ns: 1.01x slower                                                    |
| async_tree_memoization  | 625 ms                                                 | 636 ms: 1.02x slower                                                     |
| spectral_norm           | 99.9 ms                                                | 102 ms: 1.02x slower                                                     |
| scimark_lu              | 107 ms                                                 | 110 ms: 1.02x slower                                                     |
| regex_effbot            | 3.36 ms                                                | 3.43 ms: 1.02x slower                                                    |
| crypto_pyaes            | 73.9 ms                                                | 75.9 ms: 1.03x slower                                                    |
| sqlite_synth            | 2.49 us                                                | 2.56 us: 1.03x slower                                                    |
| pidigits                | 199 ms                                                 | 206 ms: 1.03x slower                                                     |
| generators              | 72.2 ms                                                | 75.4 ms: 1.04x slower                                                    |
| pickle                  | 9.79 us                                                | 10.3 us: 1.05x slower                                                    |
| regex_dna               | 203 ms                                                 | 218 ms: 1.07x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (12): pylint, unpickle, telco, xml_etree_parse, raytrace, regex_v8, bench_mp_pool, meteor_contest, unpickle_list, django_template, nbody, xml_etree_process
Ignored benchmarks (1) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20221014-3.12.0a0-d09385f/bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
