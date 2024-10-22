# Results vs. 3.13.0

- fork: faster-cpython
- ref: more_robust_immortal
- machine: linux-x86_64
- commit hash: 94f8fd0
- commit date: 2024-10-10
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 280 ms: 1.04x faster                                                                  |
| docutils       | 2.81 sec                                                     | 2.87 sec: 1.02x slower                                                                |
| html5lib       | 71.9 ms                                                      | 70.7 ms: 1.02x faster                                                                 |
| tornado_http   | 120 ms                                                       | 116 ms: 1.04x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 391 ms: 1.18x faster                                                                  |
| async_tree_none            | 372 ms                                                       | 320 ms: 1.16x faster                                                                  |
| async_tree_memoization     | 452 ms                                                       | 400 ms: 1.13x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                       | 310 ms: 1.10x faster                                                                  |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 571 ms: 1.05x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.05x faster                                                                  |
| async_tree_io              | 847 ms                                                       | 812 ms: 1.04x faster                                                                  |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                                 |
| async_tree_io_tg           | 819 ms                                                       | 795 ms: 1.03x faster                                                                  |
| asyncio_tcp                | 380 ms                                                       | 370 ms: 1.03x faster                                                                  |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                                                |
| asyncio_websockets         | 382 ms                                                       | 392 ms: 1.02x slower                                                                  |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                          |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 79.7 ms: 1.03x faster                                                                 |
| pidigits       | 253 ms                                                       | 252 ms: 1.00x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 137 ms: 1.05x faster                                                                  |
| regex_v8       | 26.2 ms                                                      | 26.2 ms: 1.00x slower                                                                 |
| regex_dna      | 244 ms                                                       | 247 ms: 1.01x slower                                                                  |
| regex_effbot   | 3.37 ms                                                      | 3.57 ms: 1.06x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| json_loads           | 24.0 us                                                      | 23.4 us: 1.02x faster                                                                 |
| xml_etree_parse      | 145 ms                                                       | 142 ms: 1.02x faster                                                                  |
| xml_etree_process    | 60.9 ms                                                      | 59.6 ms: 1.02x faster                                                                 |
| pickle_pure_python   | 318 us                                                       | 312 us: 1.02x faster                                                                  |
| pickle               | 10.5 us                                                      | 10.4 us: 1.02x faster                                                                 |
| xml_etree_generate   | 85.3 ms                                                      | 84.7 ms: 1.01x faster                                                                 |
| unpickle_pure_python | 214 us                                                       | 213 us: 1.01x faster                                                                  |
| json_dumps           | 11.0 ms                                                      | 11.1 ms: 1.01x slower                                                                 |
| unpickle_list        | 4.62 us                                                      | 4.72 us: 1.02x slower                                                                 |
| tomli_loads          | 2.41 sec                                                     | 2.52 sec: 1.05x slower                                                                |
| pickle_list          | 4.59 us                                                      | 4.81 us: 1.05x slower                                                                 |
| pickle_dict          | 32.1 us                                                      | 33.9 us: 1.06x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                          |

Benchmark hidden because not significant (2): unpickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 8.95 ms: 1.00x slower                                                                 |
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 24.2 ms: 1.10x faster                                                                 |
| genshi_xml      | 57.3 ms                                                      | 52.3 ms: 1.10x faster                                                                 |
| mako            | 10.4 ms                                                      | 10.6 ms: 1.02x slower                                                                 |
| django_template | 38.9 ms                                                      | 41.8 ms: 1.08x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf2-x86_64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 284 us: 1.40x faster                                                                  |
| deepcopy_memo              | 39.5 us                                                      | 28.9 us: 1.37x faster                                                                 |
| unpack_sequence            | 56.8 ns                                                      | 42.7 ns: 1.33x faster                                                                 |
| deepcopy_reduce            | 3.54 us                                                      | 2.90 us: 1.22x faster                                                                 |
| go                         | 160 ms                                                       | 133 ms: 1.21x faster                                                                  |
| generators                 | 33.5 ms                                                      | 28.0 ms: 1.19x faster                                                                 |
| async_tree_memoization_tg  | 461 ms                                                       | 391 ms: 1.18x faster                                                                  |
| async_tree_none            | 372 ms                                                       | 320 ms: 1.16x faster                                                                  |
| scimark_sor                | 126 ms                                                       | 108 ms: 1.16x faster                                                                  |
| async_tree_memoization     | 452 ms                                                       | 400 ms: 1.13x faster                                                                  |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.10x faster                                                                 |
| genshi_text                | 26.6 ms                                                      | 24.2 ms: 1.10x faster                                                                 |
| async_tree_none_tg         | 340 ms                                                       | 310 ms: 1.10x faster                                                                  |
| genshi_xml                 | 57.3 ms                                                      | 52.3 ms: 1.10x faster                                                                 |
| telco                      | 8.58 ms                                                      | 7.87 ms: 1.09x faster                                                                 |
| raytrace                   | 289 ms                                                       | 266 ms: 1.09x faster                                                                  |
| bpe_tokeniser              | 5.10 sec                                                     | 4.74 sec: 1.08x faster                                                                |
| scimark_fft                | 314 ms                                                       | 294 ms: 1.07x faster                                                                  |
| richards_super             | 59.8 ms                                                      | 56.8 ms: 1.05x faster                                                                 |
| regex_compile              | 144 ms                                                       | 137 ms: 1.05x faster                                                                  |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 571 ms: 1.05x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.05x faster                                                                  |
| async_tree_io              | 847 ms                                                       | 812 ms: 1.04x faster                                                                  |
| richards                   | 52.7 ms                                                      | 50.8 ms: 1.04x faster                                                                 |
| 2to3                       | 291 ms                                                       | 280 ms: 1.04x faster                                                                  |
| tornado_http               | 120 ms                                                       | 116 ms: 1.04x faster                                                                  |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.14 ms: 1.03x faster                                                                 |
| scimark_lu                 | 97.8 ms                                                      | 94.8 ms: 1.03x faster                                                                 |
| pycparser                  | 1.26 sec                                                     | 1.22 sec: 1.03x faster                                                                |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                                 |
| async_tree_io_tg           | 819 ms                                                       | 795 ms: 1.03x faster                                                                  |
| asyncio_tcp                | 380 ms                                                       | 370 ms: 1.03x faster                                                                  |
| float                      | 81.9 ms                                                      | 79.7 ms: 1.03x faster                                                                 |
| pprint_safe_repr           | 812 ms                                                       | 792 ms: 1.02x faster                                                                  |
| json_loads                 | 24.0 us                                                      | 23.4 us: 1.02x faster                                                                 |
| json                       | 5.22 ms                                                      | 5.10 ms: 1.02x faster                                                                 |
| pprint_pformat             | 1.65 sec                                                     | 1.61 sec: 1.02x faster                                                                |
| bench_thread_pool          | 901 us                                                       | 881 us: 1.02x faster                                                                  |
| spectral_norm              | 97.4 ms                                                      | 95.3 ms: 1.02x faster                                                                 |
| sympy_str                  | 296 ms                                                       | 289 ms: 1.02x faster                                                                  |
| pyflate                    | 492 ms                                                       | 481 ms: 1.02x faster                                                                  |
| hexiom                     | 6.33 ms                                                      | 6.20 ms: 1.02x faster                                                                 |
| xml_etree_parse            | 145 ms                                                       | 142 ms: 1.02x faster                                                                  |
| xml_etree_process          | 60.9 ms                                                      | 59.6 ms: 1.02x faster                                                                 |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                                  |
| pickle_pure_python         | 318 us                                                       | 312 us: 1.02x faster                                                                  |
| sqlite_synth               | 2.79 us                                                      | 2.74 us: 1.02x faster                                                                 |
| comprehensions             | 17.3 us                                                      | 16.9 us: 1.02x faster                                                                 |
| fannkuch                   | 365 ms                                                       | 358 ms: 1.02x faster                                                                  |
| html5lib                   | 71.9 ms                                                      | 70.7 ms: 1.02x faster                                                                 |
| mdp                        | 2.52 sec                                                     | 2.48 sec: 1.02x faster                                                                |
| sympy_sum                  | 154 ms                                                       | 151 ms: 1.02x faster                                                                  |
| sympy_expand               | 505 ms                                                       | 497 ms: 1.02x faster                                                                  |
| pickle                     | 10.5 us                                                      | 10.4 us: 1.02x faster                                                                 |
| deltablue                  | 3.41 ms                                                      | 3.36 ms: 1.01x faster                                                                 |
| nqueens                    | 88.2 ms                                                      | 87.2 ms: 1.01x faster                                                                 |
| scimark_monte_carlo        | 64.9 ms                                                      | 64.4 ms: 1.01x faster                                                                 |
| xml_etree_generate         | 85.3 ms                                                      | 84.7 ms: 1.01x faster                                                                 |
| sympy_integrate            | 23.3 ms                                                      | 23.2 ms: 1.01x faster                                                                 |
| unpickle_pure_python       | 214 us                                                       | 213 us: 1.01x faster                                                                  |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                                                |
| pidigits                   | 253 ms                                                       | 252 ms: 1.00x faster                                                                  |
| python_startup_no_site     | 8.94 ms                                                      | 8.95 ms: 1.00x slower                                                                 |
| regex_v8                   | 26.2 ms                                                      | 26.2 ms: 1.00x slower                                                                 |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                                 |
| sqlglot_normalize          | 118 ms                                                       | 119 ms: 1.01x slower                                                                  |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                                                 |
| coverage                   | 81.1 ms                                                      | 81.9 ms: 1.01x slower                                                                 |
| json_dumps                 | 11.0 ms                                                      | 11.1 ms: 1.01x slower                                                                 |
| regex_dna                  | 244 ms                                                       | 247 ms: 1.01x slower                                                                  |
| logging_simple             | 6.40 us                                                      | 6.50 us: 1.02x slower                                                                 |
| mako                       | 10.4 ms                                                      | 10.6 ms: 1.02x slower                                                                 |
| unpickle_list              | 4.62 us                                                      | 4.72 us: 1.02x slower                                                                 |
| docutils                   | 2.81 sec                                                     | 2.87 sec: 1.02x slower                                                                |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                                 |
| asyncio_websockets         | 382 ms                                                       | 392 ms: 1.02x slower                                                                  |
| tomli_loads                | 2.41 sec                                                     | 2.52 sec: 1.05x slower                                                                |
| pickle_list                | 4.59 us                                                      | 4.81 us: 1.05x slower                                                                 |
| pickle_dict                | 32.1 us                                                      | 33.9 us: 1.06x slower                                                                 |
| regex_effbot               | 3.37 ms                                                      | 3.57 ms: 1.06x slower                                                                 |
| django_template            | 38.9 ms                                                      | 41.8 ms: 1.08x slower                                                                 |
| create_gc_cycles           | 1.76 ms                                                      | 2.02 ms: 1.15x slower                                                                 |
| gc_traversal               | 4.11 ms                                                      | 4.74 ms: 1.15x slower                                                                 |
| bench_mp_pool              | 4.65 ms                                                      | 1.92 sec: 412.95x slower                                                              |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                          |

Benchmark hidden because not significant (13): typing_runtime_protocols, unpickle, pylint, async_generators, sqlglot_optimize, dulwich_log, xml_etree_iterparse, thrift, crypto_pyaes, logging_format, chaos, logging_silent, nbody
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.01x