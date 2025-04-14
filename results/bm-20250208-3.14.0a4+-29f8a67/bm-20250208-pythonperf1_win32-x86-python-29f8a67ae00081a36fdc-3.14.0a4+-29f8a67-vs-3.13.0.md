# Results vs. 3.13.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: windows-x86
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.027x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 270 ms: 1.08x slower                                                            |
| docutils       | 1.78 sec                                                        | 1.89 sec: 1.06x slower                                                          |
| sphinx         | 719 ms                                                          | 768 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                    |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 526 ms                                                          | 491 ms: 1.07x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 268 ms: 1.05x faster                                                            |
| async_tree_none            | 245 ms                                                          | 233 ms: 1.05x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 283 ms: 1.05x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 353 ms: 1.03x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 488 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 494 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 479 ms: 1.05x slower                                                            |
| async_generators           | 270 ms                                                          | 307 ms: 1.14x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): async_tree_none_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 203 ms: 1.01x slower                                                            |
| float          | 54.6 ms                                                         | 59.8 ms: 1.09x slower                                                           |
| nbody          | 80.0 ms                                                         | 93.9 ms: 1.17x slower                                                           |
| Geometric mean | (ref)                                                           | 1.09x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.57 ms: 1.15x faster                                                           |
| regex_compile  | 101 ms                                                          | 110 ms: 1.09x slower                                                            |
| regex_dna      | 114 ms                                                          | 125 ms: 1.10x slower                                                            |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                          | 108 ms: 1.01x slower                                                            |
| tomli_loads          | 1.71 sec                                                        | 1.74 sec: 1.02x slower                                                          |
| json_loads           | 21.6 us                                                         | 22.4 us: 1.04x slower                                                           |
| xml_etree_iterparse  | 62.6 ms                                                         | 68.1 ms: 1.09x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 67.7 ms: 1.10x slower                                                           |
| unpickle_pure_python | 160 us                                                          | 184 us: 1.15x slower                                                            |
| xml_etree_process    | 44.2 ms                                                         | 50.8 ms: 1.15x slower                                                           |
| json_dumps           | 7.30 ms                                                         | 9.21 ms: 1.26x slower                                                           |
| pickle_pure_python   | 231 us                                                          | 297 us: 1.28x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.12x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 28.9 ms: 1.02x slower                                                           |
| python_startup_no_site | 19.7 ms                                                         | 22.1 ms: 1.12x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 21.5 ms                                                         | 23.8 ms: 1.11x slower                                                           |
| mako            | 7.09 ms                                                         | 8.13 ms: 1.15x slower                                                           |
| django_template | 29.8 ms                                                         | 37.9 ms: 1.27x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.12x slower                                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 807 us: 12.37x faster                                                           |
| coverage                   | 324 ms                                                          | 52.9 ms: 6.12x faster                                                           |
| pathlib                    | 82.9 ms                                                         | 67.5 ms: 1.23x faster                                                           |
| deepcopy                   | 314 us                                                          | 258 us: 1.22x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.57 ms: 1.15x faster                                                           |
| deepcopy_memo              | 25.4 us                                                         | 22.4 us: 1.13x faster                                                           |
| deepcopy_reduce            | 2.92 us                                                         | 2.71 us: 1.08x faster                                                           |
| async_tree_io              | 526 ms                                                          | 491 ms: 1.07x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 268 ms: 1.05x faster                                                            |
| async_tree_none            | 245 ms                                                          | 233 ms: 1.05x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 283 ms: 1.05x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 353 ms: 1.03x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.92 us: 1.02x faster                                                           |
| async_tree_io_tg           | 494 ms                                                          | 488 ms: 1.01x faster                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 3.43 sec: 1.01x faster                                                          |
| fannkuch                   | 299 ms                                                          | 297 ms: 1.01x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 108 ms: 1.01x slower                                                            |
| pidigits                   | 201 ms                                                          | 203 ms: 1.01x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.88 ms: 1.01x slower                                                           |
| tomli_loads                | 1.71 sec                                                        | 1.74 sec: 1.02x slower                                                          |
| python_startup             | 28.3 ms                                                         | 28.9 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 494 ms: 1.02x slower                                                            |
| shortest_path              | 290 ms                                                          | 297 ms: 1.02x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 1.79 ms: 1.02x slower                                                           |
| pycparser                  | 872 ms                                                          | 901 ms: 1.03x slower                                                            |
| json_loads                 | 21.6 us                                                         | 22.4 us: 1.04x slower                                                           |
| telco                      | 6.96 ms                                                         | 7.24 ms: 1.04x slower                                                           |
| mdp                        | 1.62 sec                                                        | 1.70 sec: 1.04x slower                                                          |
| meteor_contest             | 74.6 ms                                                         | 78.3 ms: 1.05x slower                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 479 ms: 1.05x slower                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 95.5 ms: 1.05x slower                                                           |
| bench_thread_pool          | 1.00 ms                                                         | 1.06 ms: 1.06x slower                                                           |
| sympy_expand               | 373 ms                                                          | 395 ms: 1.06x slower                                                            |
| sympy_sum                  | 106 ms                                                          | 112 ms: 1.06x slower                                                            |
| docutils                   | 1.78 sec                                                        | 1.89 sec: 1.06x slower                                                          |
| sympy_str                  | 212 ms                                                          | 226 ms: 1.07x slower                                                            |
| json                       | 4.27 ms                                                         | 4.56 ms: 1.07x slower                                                           |
| scimark_fft                | 205 ms                                                          | 219 ms: 1.07x slower                                                            |
| sphinx                     | 719 ms                                                          | 768 ms: 1.07x slower                                                            |
| go                         | 109 ms                                                          | 116 ms: 1.07x slower                                                            |
| 2to3                       | 250 ms                                                          | 270 ms: 1.08x slower                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 61.4 ms: 1.08x slower                                                           |
| logging_format             | 8.72 us                                                         | 9.40 us: 1.08x slower                                                           |
| regex_compile              | 101 ms                                                          | 110 ms: 1.09x slower                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 68.1 ms: 1.09x slower                                                           |
| dulwich_log                | 48.8 ms                                                         | 53.2 ms: 1.09x slower                                                           |
| pprint_safe_repr           | 648 ms                                                          | 709 ms: 1.09x slower                                                            |
| float                      | 54.6 ms                                                         | 59.8 ms: 1.09x slower                                                           |
| sympy_integrate            | 15.0 ms                                                         | 16.5 ms: 1.10x slower                                                           |
| regex_dna                  | 114 ms                                                          | 125 ms: 1.10x slower                                                            |
| logging_simple             | 7.99 us                                                         | 8.80 us: 1.10x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 67.7 ms: 1.10x slower                                                           |
| genshi_text                | 21.5 ms                                                         | 23.8 ms: 1.11x slower                                                           |
| nqueens                    | 72.1 ms                                                         | 79.7 ms: 1.11x slower                                                           |
| spectral_norm              | 69.4 ms                                                         | 76.9 ms: 1.11x slower                                                           |
| pprint_pformat             | 1.33 sec                                                        | 1.48 sec: 1.12x slower                                                          |
| comprehensions             | 12.5 us                                                         | 14.0 us: 1.12x slower                                                           |
| typing_runtime_protocols   | 138 us                                                          | 154 us: 1.12x slower                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 22.1 ms: 1.12x slower                                                           |
| pyflate                    | 320 ms                                                          | 361 ms: 1.13x slower                                                            |
| sqlglot_normalize          | 216 ms                                                          | 246 ms: 1.14x slower                                                            |
| async_generators           | 270 ms                                                          | 307 ms: 1.14x slower                                                            |
| sqlglot_optimize           | 41.4 ms                                                         | 47.3 ms: 1.14x slower                                                           |
| unpickle_pure_python       | 160 us                                                          | 184 us: 1.15x slower                                                            |
| mako                       | 7.09 ms                                                         | 8.13 ms: 1.15x slower                                                           |
| xml_etree_process          | 44.2 ms                                                         | 50.8 ms: 1.15x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 69.8 ms: 1.16x slower                                                           |
| sqlglot_transpile          | 1.24 ms                                                         | 1.44 ms: 1.16x slower                                                           |
| nbody                      | 80.0 ms                                                         | 93.9 ms: 1.17x slower                                                           |
| scimark_monte_carlo        | 47.7 ms                                                         | 56.1 ms: 1.18x slower                                                           |
| chaos                      | 50.2 ms                                                         | 59.3 ms: 1.18x slower                                                           |
| sqlglot_parse              | 1.00 ms                                                         | 1.19 ms: 1.19x slower                                                           |
| scimark_sor                | 85.9 ms                                                         | 107 ms: 1.25x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 5.55 ms: 1.25x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 9.21 ms: 1.26x slower                                                           |
| django_template            | 29.8 ms                                                         | 37.9 ms: 1.27x slower                                                           |
| many_optionals             | 436 us                                                          | 560 us: 1.28x slower                                                            |
| pickle_pure_python         | 231 us                                                          | 297 us: 1.28x slower                                                            |
| generators                 | 21.8 ms                                                         | 28.1 ms: 1.29x slower                                                           |
| richards_super             | 36.7 ms                                                         | 47.5 ms: 1.29x slower                                                           |
| richards                   | 32.7 ms                                                         | 42.4 ms: 1.30x slower                                                           |
| deltablue                  | 2.33 ms                                                         | 3.05 ms: 1.31x slower                                                           |
| logging_silent             | 60.3 ns                                                         | 81.6 ns: 1.35x slower                                                           |
| raytrace                   | 201 ms                                                          | 290 ms: 1.44x slower                                                            |
| subparsers                 | 14.8 ms                                                         | 22.3 ms: 1.51x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.03x slower                                                                    |

Benchmark hidden because not significant (9): regex_v8, genshi_xml, html5lib, create_gc_cycles, async_tree_none_tg, coroutines, connected_components, k_core, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-pythonperf1_win32-x86-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.027x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown