# Results vs. 3.13.0

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-x86_64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.02x faster
- HPT reliability: 95.19%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 288 ms: 1.01x faster                                                                  |
| docutils       | 2.81 sec                                                     | 3.01 sec: 1.07x slower                                                                |
| html5lib       | 71.9 ms                                                      | 74.1 ms: 1.03x slower                                                                 |
| tornado_http   | 120 ms                                                       | 118 ms: 1.02x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 388 ms: 1.19x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                       | 304 ms: 1.12x faster                                                                  |
| async_tree_none            | 372 ms                                                       | 336 ms: 1.11x faster                                                                  |
| async_tree_memoization     | 452 ms                                                       | 409 ms: 1.10x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 546 ms: 1.05x faster                                                                  |
| async_tree_io_tg           | 819 ms                                                       | 781 ms: 1.05x faster                                                                  |
| async_tree_io              | 847 ms                                                       | 818 ms: 1.03x faster                                                                  |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 582 ms: 1.03x faster                                                                  |
| asyncio_tcp                | 380 ms                                                       | 375 ms: 1.01x faster                                                                  |
| coroutines                 | 21.6 ms                                                      | 21.5 ms: 1.01x faster                                                                 |
| async_generators           | 359 ms                                                       | 365 ms: 1.01x slower                                                                  |
| asyncio_websockets         | 382 ms                                                       | 389 ms: 1.02x slower                                                                  |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                          |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 85.6 ms: 1.03x faster                                                                 |
| float          | 81.9 ms                                                      | 80.2 ms: 1.02x faster                                                                 |
| pidigits       | 253 ms                                                       | 254 ms: 1.01x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 236 ms: 1.03x faster                                                                  |
| regex_v8       | 26.2 ms                                                      | 25.6 ms: 1.02x faster                                                                 |
| regex_compile  | 144 ms                                                       | 143 ms: 1.01x faster                                                                  |
| regex_effbot   | 3.37 ms                                                      | 3.56 ms: 1.06x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.21 sec: 1.09x faster                                                                |
| xml_etree_process    | 60.9 ms                                                      | 59.2 ms: 1.03x faster                                                                 |
| unpickle_pure_python | 214 us                                                       | 210 us: 1.02x faster                                                                  |
| json_dumps           | 11.0 ms                                                      | 10.8 ms: 1.02x faster                                                                 |
| pickle_pure_python   | 318 us                                                       | 321 us: 1.01x slower                                                                  |
| xml_etree_iterparse  | 100 ms                                                       | 104 ms: 1.04x slower                                                                  |
| json_loads           | 24.0 us                                                      | 25.8 us: 1.08x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                          |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                                 |
| python_startup_no_site | 8.94 ms                                                      | 9.08 ms: 1.02x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 54.7 ms: 1.05x faster                                                                 |
| mako            | 10.4 ms                                                      | 10.6 ms: 1.01x slower                                                                 |
| genshi_text     | 26.6 ms                                                      | 27.1 ms: 1.02x slower                                                                 |
| django_template | 38.9 ms                                                      | 40.7 ms: 1.05x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 290 us: 1.37x faster                                                                  |
| deepcopy_memo              | 39.5 us                                                      | 30.5 us: 1.30x faster                                                                 |
| deepcopy_reduce            | 3.54 us                                                      | 2.95 us: 1.20x faster                                                                 |
| async_tree_memoization_tg  | 461 ms                                                       | 388 ms: 1.19x faster                                                                  |
| generators                 | 33.5 ms                                                      | 28.7 ms: 1.17x faster                                                                 |
| async_tree_none_tg         | 340 ms                                                       | 304 ms: 1.12x faster                                                                  |
| async_tree_none            | 372 ms                                                       | 336 ms: 1.11x faster                                                                  |
| async_tree_memoization     | 452 ms                                                       | 409 ms: 1.10x faster                                                                  |
| scimark_sor                | 126 ms                                                       | 115 ms: 1.09x faster                                                                  |
| tomli_loads                | 2.41 sec                                                     | 2.21 sec: 1.09x faster                                                                |
| raytrace                   | 289 ms                                                       | 266 ms: 1.09x faster                                                                  |
| pathlib                    | 17.4 ms                                                      | 16.2 ms: 1.08x faster                                                                 |
| telco                      | 8.58 ms                                                      | 8.09 ms: 1.06x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 546 ms: 1.05x faster                                                                  |
| async_tree_io_tg           | 819 ms                                                       | 781 ms: 1.05x faster                                                                  |
| genshi_xml                 | 57.3 ms                                                      | 54.7 ms: 1.05x faster                                                                 |
| richards_super             | 59.8 ms                                                      | 57.3 ms: 1.04x faster                                                                 |
| bpe_tokeniser              | 5.10 sec                                                     | 4.90 sec: 1.04x faster                                                                |
| async_tree_io              | 847 ms                                                       | 818 ms: 1.03x faster                                                                  |
| richards                   | 52.7 ms                                                      | 51.0 ms: 1.03x faster                                                                 |
| regex_dna                  | 244 ms                                                       | 236 ms: 1.03x faster                                                                  |
| bench_thread_pool          | 901 us                                                       | 874 us: 1.03x faster                                                                  |
| coverage                   | 81.1 ms                                                      | 78.8 ms: 1.03x faster                                                                 |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 582 ms: 1.03x faster                                                                  |
| xml_etree_process          | 60.9 ms                                                      | 59.2 ms: 1.03x faster                                                                 |
| nbody                      | 88.0 ms                                                      | 85.6 ms: 1.03x faster                                                                 |
| crypto_pyaes               | 72.8 ms                                                      | 71.0 ms: 1.02x faster                                                                 |
| regex_v8                   | 26.2 ms                                                      | 25.6 ms: 1.02x faster                                                                 |
| logging_format             | 7.07 us                                                      | 6.91 us: 1.02x faster                                                                 |
| logging_simple             | 6.40 us                                                      | 6.25 us: 1.02x faster                                                                 |
| unpickle_pure_python       | 214 us                                                       | 210 us: 1.02x faster                                                                  |
| float                      | 81.9 ms                                                      | 80.2 ms: 1.02x faster                                                                 |
| json_dumps                 | 11.0 ms                                                      | 10.8 ms: 1.02x faster                                                                 |
| tornado_http               | 120 ms                                                       | 118 ms: 1.02x faster                                                                  |
| deltablue                  | 3.41 ms                                                      | 3.36 ms: 1.02x faster                                                                 |
| scimark_fft                | 314 ms                                                       | 310 ms: 1.01x faster                                                                  |
| fannkuch                   | 365 ms                                                       | 360 ms: 1.01x faster                                                                  |
| spectral_norm              | 97.4 ms                                                      | 96.1 ms: 1.01x faster                                                                 |
| asyncio_tcp                | 380 ms                                                       | 375 ms: 1.01x faster                                                                  |
| 2to3                       | 291 ms                                                       | 288 ms: 1.01x faster                                                                  |
| regex_compile              | 144 ms                                                       | 143 ms: 1.01x faster                                                                  |
| mdp                        | 2.52 sec                                                     | 2.50 sec: 1.01x faster                                                                |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.01x faster                                                                  |
| sqlglot_optimize           | 59.7 ms                                                      | 59.3 ms: 1.01x faster                                                                 |
| coroutines                 | 21.6 ms                                                      | 21.5 ms: 1.01x faster                                                                 |
| go                         | 160 ms                                                       | 160 ms: 1.00x faster                                                                  |
| pidigits                   | 253 ms                                                       | 254 ms: 1.01x slower                                                                  |
| pickle_pure_python         | 318 us                                                       | 321 us: 1.01x slower                                                                  |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                                 |
| sympy_integrate            | 23.3 ms                                                      | 23.5 ms: 1.01x slower                                                                 |
| hexiom                     | 6.33 ms                                                      | 6.39 ms: 1.01x slower                                                                 |
| sympy_str                  | 296 ms                                                       | 299 ms: 1.01x slower                                                                  |
| sqlglot_normalize          | 118 ms                                                       | 120 ms: 1.01x slower                                                                  |
| typing_runtime_protocols   | 174 us                                                       | 176 us: 1.01x slower                                                                  |
| thrift                     | 877 us                                                       | 886 us: 1.01x slower                                                                  |
| sympy_expand               | 505 ms                                                       | 511 ms: 1.01x slower                                                                  |
| chaos                      | 61.7 ms                                                      | 62.5 ms: 1.01x slower                                                                 |
| sympy_sum                  | 154 ms                                                       | 156 ms: 1.01x slower                                                                  |
| mako                       | 10.4 ms                                                      | 10.6 ms: 1.01x slower                                                                 |
| async_generators           | 359 ms                                                       | 365 ms: 1.01x slower                                                                  |
| sqlglot_parse              | 1.38 ms                                                      | 1.40 ms: 1.01x slower                                                                 |
| python_startup_no_site     | 8.94 ms                                                      | 9.08 ms: 1.02x slower                                                                 |
| pycparser                  | 1.26 sec                                                     | 1.28 sec: 1.02x slower                                                                |
| asyncio_websockets         | 382 ms                                                       | 389 ms: 1.02x slower                                                                  |
| dask                       | 379 ms                                                       | 386 ms: 1.02x slower                                                                  |
| genshi_text                | 26.6 ms                                                      | 27.1 ms: 1.02x slower                                                                 |
| pprint_safe_repr           | 812 ms                                                       | 829 ms: 1.02x slower                                                                  |
| comprehensions             | 17.3 us                                                      | 17.6 us: 1.02x slower                                                                 |
| scimark_monte_carlo        | 64.9 ms                                                      | 66.5 ms: 1.02x slower                                                                 |
| nqueens                    | 88.2 ms                                                      | 90.7 ms: 1.03x slower                                                                 |
| html5lib                   | 71.9 ms                                                      | 74.1 ms: 1.03x slower                                                                 |
| pprint_pformat             | 1.65 sec                                                     | 1.70 sec: 1.03x slower                                                                |
| xml_etree_iterparse        | 100 ms                                                       | 104 ms: 1.04x slower                                                                  |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.44 ms: 1.04x slower                                                                 |
| django_template            | 38.9 ms                                                      | 40.7 ms: 1.05x slower                                                                 |
| json                       | 5.22 ms                                                      | 5.48 ms: 1.05x slower                                                                 |
| regex_effbot               | 3.37 ms                                                      | 3.56 ms: 1.06x slower                                                                 |
| docutils                   | 2.81 sec                                                     | 3.01 sec: 1.07x slower                                                                |
| json_loads                 | 24.0 us                                                      | 25.8 us: 1.08x slower                                                                 |
| gc_traversal               | 4.11 ms                                                      | 4.75 ms: 1.15x slower                                                                 |
| create_gc_cycles           | 1.76 ms                                                      | 2.04 ms: 1.16x slower                                                                 |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                          |

Benchmark hidden because not significant (9): logging_silent, pyflate, xml_etree_generate, sqlglot_transpile, asyncio_tcp_ssl, xml_etree_parse, bench_mp_pool, scimark_lu, pylint
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 95.19% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x