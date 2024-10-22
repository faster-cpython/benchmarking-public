# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b1
- machine: linux-x86_64
- commit hash: 2268289
- commit date: 2024-05-08
- overall geometric mean: 1.04x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 290 ms: 1.00x faster                                             |
| chameleon      | 7.42 ms                                                      | 7.66 ms: 1.03x slower                                            |
| docutils       | 2.81 sec                                                     | 3.03 sec: 1.08x slower                                           |
| html5lib       | 71.9 ms                                                      | 75.9 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                        | 1.03x slower                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 444 ms: 1.04x faster                                             |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                           |
| async_tree_none_tg         | 340 ms                                                       | 345 ms: 1.01x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 586 ms: 1.02x slower                                             |
| async_generators           | 359 ms                                                       | 367 ms: 1.02x slower                                             |
| asyncio_websockets         | 382 ms                                                       | 393 ms: 1.03x slower                                             |
| async_tree_io              | 847 ms                                                       | 870 ms: 1.03x slower                                             |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 619 ms: 1.03x slower                                             |
| async_tree_memoization     | 452 ms                                                       | 467 ms: 1.03x slower                                             |
| async_tree_io_tg           | 819 ms                                                       | 889 ms: 1.09x slower                                             |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                     |

Benchmark hidden because not significant (3): coroutines, async_tree_none, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 81.1 ms: 1.01x faster                                            |
| pidigits       | 253 ms                                                       | 252 ms: 1.00x faster                                             |
| Geometric mean | (ref)                                                        | 1.00x slower                                                     |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 25.6 ms: 1.02x faster                                            |
| regex_dna      | 244 ms                                                       | 243 ms: 1.00x faster                                             |
| regex_compile  | 144 ms                                                       | 147 ms: 1.02x slower                                             |
| regex_effbot   | 3.37 ms                                                      | 3.56 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_dict          | 32.1 us                                                      | 31.2 us: 1.03x faster                                            |
| pickle_list          | 4.59 us                                                      | 4.49 us: 1.02x faster                                            |
| pickle               | 10.5 us                                                      | 10.4 us: 1.01x faster                                            |
| json_dumps           | 11.0 ms                                                      | 10.9 ms: 1.01x faster                                            |
| xml_etree_process    | 60.9 ms                                                      | 60.6 ms: 1.00x faster                                            |
| json_loads           | 24.0 us                                                      | 24.4 us: 1.02x slower                                            |
| unpickle             | 15.1 us                                                      | 15.5 us: 1.02x slower                                            |
| xml_etree_iterparse  | 100 ms                                                       | 103 ms: 1.03x slower                                             |
| unpickle_list        | 4.62 us                                                      | 4.75 us: 1.03x slower                                            |
| unpickle_pure_python | 214 us                                                       | 222 us: 1.04x slower                                             |
| xml_etree_generate   | 85.3 ms                                                      | 88.9 ms: 1.04x slower                                            |
| tomli_loads          | 2.41 sec                                                     | 2.58 sec: 1.07x slower                                           |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 12.9 ms: 1.03x faster                                            |
| python_startup_no_site | 8.94 ms                                                      | 8.86 ms: 1.01x faster                                            |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 26.2 ms: 1.01x faster                                            |
| genshi_xml      | 57.3 ms                                                      | 57.8 ms: 1.01x slower                                            |
| django_template | 38.9 ms                                                      | 39.5 ms: 1.02x slower                                            |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                     |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mypy2                      | 1.05 sec                                                     | 780 ms: 1.34x faster                                             |
| raytrace                   | 289 ms                                                       | 268 ms: 1.08x faster                                             |
| scimark_sor                | 126 ms                                                       | 117 ms: 1.07x faster                                             |
| chaos                      | 61.7 ms                                                      | 59.4 ms: 1.04x faster                                            |
| async_tree_memoization_tg  | 461 ms                                                       | 444 ms: 1.04x faster                                             |
| pickle_dict                | 32.1 us                                                      | 31.2 us: 1.03x faster                                            |
| python_startup             | 13.3 ms                                                      | 12.9 ms: 1.03x faster                                            |
| pyflate                    | 492 ms                                                       | 480 ms: 1.02x faster                                             |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.19 ms: 1.02x faster                                            |
| regex_v8                   | 26.2 ms                                                      | 25.6 ms: 1.02x faster                                            |
| pickle_list                | 4.59 us                                                      | 4.49 us: 1.02x faster                                            |
| deepcopy_reduce            | 3.54 us                                                      | 3.48 us: 1.02x faster                                            |
| genshi_text                | 26.6 ms                                                      | 26.2 ms: 1.01x faster                                            |
| pickle                     | 10.5 us                                                      | 10.4 us: 1.01x faster                                            |
| logging_silent             | 97.7 ns                                                      | 96.6 ns: 1.01x faster                                            |
| mdp                        | 2.52 sec                                                     | 2.50 sec: 1.01x faster                                           |
| python_startup_no_site     | 8.94 ms                                                      | 8.86 ms: 1.01x faster                                            |
| float                      | 81.9 ms                                                      | 81.1 ms: 1.01x faster                                            |
| comprehensions             | 17.3 us                                                      | 17.1 us: 1.01x faster                                            |
| deltablue                  | 3.41 ms                                                      | 3.39 ms: 1.01x faster                                            |
| generators                 | 33.5 ms                                                      | 33.3 ms: 1.01x faster                                            |
| pathlib                    | 17.4 ms                                                      | 17.3 ms: 1.01x faster                                            |
| json_dumps                 | 11.0 ms                                                      | 10.9 ms: 1.01x faster                                            |
| regex_dna                  | 244 ms                                                       | 243 ms: 1.00x faster                                             |
| xml_etree_process          | 60.9 ms                                                      | 60.6 ms: 1.00x faster                                            |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                           |
| 2to3                       | 291 ms                                                       | 290 ms: 1.00x faster                                             |
| pidigits                   | 253 ms                                                       | 252 ms: 1.00x faster                                             |
| hexiom                     | 6.33 ms                                                      | 6.37 ms: 1.01x slower                                            |
| sqlglot_optimize           | 59.7 ms                                                      | 60.1 ms: 1.01x slower                                            |
| genshi_xml                 | 57.3 ms                                                      | 57.8 ms: 1.01x slower                                            |
| aiohttp                    | 1.07 ms                                                      | 1.08 ms: 1.01x slower                                            |
| pycparser                  | 1.26 sec                                                     | 1.27 sec: 1.01x slower                                           |
| async_tree_none_tg         | 340 ms                                                       | 345 ms: 1.01x slower                                             |
| django_template            | 38.9 ms                                                      | 39.5 ms: 1.02x slower                                            |
| logging_simple             | 6.40 us                                                      | 6.50 us: 1.02x slower                                            |
| sqlite_synth               | 2.79 us                                                      | 2.83 us: 1.02x slower                                            |
| sympy_expand               | 505 ms                                                       | 514 ms: 1.02x slower                                             |
| sympy_integrate            | 23.3 ms                                                      | 23.8 ms: 1.02x slower                                            |
| json_loads                 | 24.0 us                                                      | 24.4 us: 1.02x slower                                            |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 586 ms: 1.02x slower                                             |
| richards_super             | 59.8 ms                                                      | 61.0 ms: 1.02x slower                                            |
| sympy_str                  | 296 ms                                                       | 302 ms: 1.02x slower                                             |
| async_generators           | 359 ms                                                       | 367 ms: 1.02x slower                                             |
| regex_compile              | 144 ms                                                       | 147 ms: 1.02x slower                                             |
| sympy_sum                  | 154 ms                                                       | 157 ms: 1.02x slower                                             |
| pprint_safe_repr           | 812 ms                                                       | 830 ms: 1.02x slower                                             |
| unpickle                   | 15.1 us                                                      | 15.5 us: 1.02x slower                                            |
| richards                   | 52.7 ms                                                      | 54.0 ms: 1.02x slower                                            |
| pprint_pformat             | 1.65 sec                                                     | 1.69 sec: 1.02x slower                                           |
| sqlglot_normalize          | 118 ms                                                       | 121 ms: 1.02x slower                                             |
| json                       | 5.22 ms                                                      | 5.36 ms: 1.03x slower                                            |
| asyncio_websockets         | 382 ms                                                       | 393 ms: 1.03x slower                                             |
| xml_etree_iterparse        | 100 ms                                                       | 103 ms: 1.03x slower                                             |
| async_tree_io              | 847 ms                                                       | 870 ms: 1.03x slower                                             |
| unpickle_list              | 4.62 us                                                      | 4.75 us: 1.03x slower                                            |
| sqlglot_transpile          | 1.78 ms                                                      | 1.83 ms: 1.03x slower                                            |
| flaskblogging              | 4.62 ms                                                      | 4.75 ms: 1.03x slower                                            |
| meteor_contest             | 128 ms                                                       | 132 ms: 1.03x slower                                             |
| coverage                   | 81.1 ms                                                      | 83.7 ms: 1.03x slower                                            |
| dulwich_log                | 65.5 ms                                                      | 67.6 ms: 1.03x slower                                            |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 619 ms: 1.03x slower                                             |
| chameleon                  | 7.42 ms                                                      | 7.66 ms: 1.03x slower                                            |
| nqueens                    | 88.2 ms                                                      | 91.1 ms: 1.03x slower                                            |
| scimark_lu                 | 97.8 ms                                                      | 101 ms: 1.03x slower                                             |
| async_tree_memoization     | 452 ms                                                       | 467 ms: 1.03x slower                                             |
| thrift                     | 877 us                                                       | 908 us: 1.04x slower                                             |
| unpickle_pure_python       | 214 us                                                       | 222 us: 1.04x slower                                             |
| xml_etree_generate         | 85.3 ms                                                      | 88.9 ms: 1.04x slower                                            |
| sqlglot_parse              | 1.38 ms                                                      | 1.44 ms: 1.04x slower                                            |
| scimark_fft                | 314 ms                                                       | 328 ms: 1.04x slower                                             |
| dask                       | 379 ms                                                       | 396 ms: 1.05x slower                                             |
| html5lib                   | 71.9 ms                                                      | 75.9 ms: 1.06x slower                                            |
| regex_effbot               | 3.37 ms                                                      | 3.56 ms: 1.06x slower                                            |
| scimark_monte_carlo        | 64.9 ms                                                      | 69.5 ms: 1.07x slower                                            |
| tomli_loads                | 2.41 sec                                                     | 2.58 sec: 1.07x slower                                           |
| docutils                   | 2.81 sec                                                     | 3.03 sec: 1.08x slower                                           |
| async_tree_io_tg           | 819 ms                                                       | 889 ms: 1.09x slower                                             |
| gc_traversal               | 4.11 ms                                                      | 4.66 ms: 1.13x slower                                            |
| create_gc_cycles           | 1.76 ms                                                      | 2.02 ms: 1.15x slower                                            |
| telco                      | 8.58 ms                                                      | 175 ms: 20.35x slower                                            |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                     |

Benchmark hidden because not significant (20): bench_thread_pool, xml_etree_parse, deepcopy, coroutines, pickle_pure_python, async_tree_none, deepcopy_memo, go, pylint, asyncio_tcp, fannkuch, spectral_norm, crypto_pyaes, logging_format, typing_runtime_protocols, tornado_http, gunicorn, mako, nbody, bench_mp_pool
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x