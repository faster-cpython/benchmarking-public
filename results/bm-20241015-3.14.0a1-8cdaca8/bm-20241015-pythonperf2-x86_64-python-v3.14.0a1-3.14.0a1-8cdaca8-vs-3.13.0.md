# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a1
- machine: linux-x86_64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.05x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 282 ms: 1.03x faster                                             |
| docutils       | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                           |
| html5lib       | 71.9 ms                                                      | 71.1 ms: 1.01x faster                                            |
| tornado_http   | 120 ms                                                       | 117 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                        | 1.01x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 386 ms: 1.20x faster                                             |
| async_tree_none            | 372 ms                                                       | 332 ms: 1.12x faster                                             |
| async_tree_memoization     | 452 ms                                                       | 415 ms: 1.09x faster                                             |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 558 ms: 1.07x faster                                             |
| async_tree_none_tg         | 340 ms                                                       | 323 ms: 1.05x faster                                             |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.03x faster                                            |
| async_tree_io              | 847 ms                                                       | 827 ms: 1.02x faster                                             |
| asyncio_tcp                | 380 ms                                                       | 371 ms: 1.02x faster                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 563 ms: 1.02x faster                                             |
| asyncio_websockets         | 382 ms                                                       | 385 ms: 1.01x slower                                             |
| async_generators           | 359 ms                                                       | 364 ms: 1.01x slower                                             |
| async_tree_io_tg           | 819 ms                                                       | 837 ms: 1.02x slower                                             |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                     |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 253 ms                                                       | 252 ms: 1.00x faster                                             |
| nbody          | 88.0 ms                                                      | 90.1 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 24.7 ms: 1.06x faster                                            |
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                             |
| regex_dna      | 244 ms                                                       | 243 ms: 1.00x faster                                             |
| regex_effbot   | 3.37 ms                                                      | 3.43 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                        | 1.02x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|---------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_list         | 4.59 us                                                      | 4.31 us: 1.06x faster                                            |
| pickle_dict         | 32.1 us                                                      | 31.0 us: 1.03x faster                                            |
| xml_etree_process   | 60.9 ms                                                      | 60.0 ms: 1.02x faster                                            |
| unpickle_list       | 4.62 us                                                      | 4.58 us: 1.01x faster                                            |
| pickle              | 10.5 us                                                      | 10.5 us: 1.01x faster                                            |
| pickle_pure_python  | 318 us                                                       | 320 us: 1.01x slower                                             |
| xml_etree_iterparse | 100 ms                                                       | 102 ms: 1.01x slower                                             |
| tomli_loads         | 2.41 sec                                                     | 2.50 sec: 1.04x slower                                           |
| json_dumps          | 11.0 ms                                                      | 11.4 ms: 1.04x slower                                            |
| json_loads          | 24.0 us                                                      | 25.3 us: 1.05x slower                                            |
| Geometric mean      | (ref)                                                        | 1.00x slower                                                     |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_generate, unpickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 8.96 ms: 1.00x slower                                            |
| python_startup         | 13.3 ms                                                      | 15.0 ms: 1.12x slower                                            |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 25.0 ms: 1.06x faster                                            |
| genshi_xml      | 57.3 ms                                                      | 54.4 ms: 1.05x faster                                            |
| mako            | 10.4 ms                                                      | 10.7 ms: 1.03x slower                                            |
| django_template | 38.9 ms                                                      | 41.0 ms: 1.06x slower                                            |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 289 us: 1.37x faster                                             |
| deepcopy_memo              | 39.5 us                                                      | 29.4 us: 1.34x faster                                            |
| go                         | 160 ms                                                       | 133 ms: 1.21x faster                                             |
| deepcopy_reduce            | 3.54 us                                                      | 2.96 us: 1.20x faster                                            |
| async_tree_memoization_tg  | 461 ms                                                       | 386 ms: 1.20x faster                                             |
| generators                 | 33.5 ms                                                      | 29.3 ms: 1.14x faster                                            |
| scimark_sor                | 126 ms                                                       | 111 ms: 1.13x faster                                             |
| async_tree_none            | 372 ms                                                       | 332 ms: 1.12x faster                                             |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.10x faster                                            |
| scimark_fft                | 314 ms                                                       | 286 ms: 1.10x faster                                             |
| async_tree_memoization     | 452 ms                                                       | 415 ms: 1.09x faster                                             |
| richards_super             | 59.8 ms                                                      | 55.6 ms: 1.07x faster                                            |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 558 ms: 1.07x faster                                             |
| raytrace                   | 289 ms                                                       | 270 ms: 1.07x faster                                             |
| richards                   | 52.7 ms                                                      | 49.5 ms: 1.07x faster                                            |
| pickle_list                | 4.59 us                                                      | 4.31 us: 1.06x faster                                            |
| genshi_text                | 26.6 ms                                                      | 25.0 ms: 1.06x faster                                            |
| regex_v8                   | 26.2 ms                                                      | 24.7 ms: 1.06x faster                                            |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.06 ms: 1.06x faster                                            |
| genshi_xml                 | 57.3 ms                                                      | 54.4 ms: 1.05x faster                                            |
| async_tree_none_tg         | 340 ms                                                       | 323 ms: 1.05x faster                                             |
| bpe_tokeniser              | 5.10 sec                                                     | 4.86 sec: 1.05x faster                                           |
| pyflate                    | 492 ms                                                       | 469 ms: 1.05x faster                                             |
| telco                      | 8.58 ms                                                      | 8.23 ms: 1.04x faster                                            |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                             |
| scimark_lu                 | 97.8 ms                                                      | 94.2 ms: 1.04x faster                                            |
| pickle_dict                | 32.1 us                                                      | 31.0 us: 1.03x faster                                            |
| 2to3                       | 291 ms                                                       | 282 ms: 1.03x faster                                             |
| fannkuch                   | 365 ms                                                       | 354 ms: 1.03x faster                                             |
| meteor_contest             | 128 ms                                                       | 125 ms: 1.03x faster                                             |
| tornado_http               | 120 ms                                                       | 117 ms: 1.03x faster                                             |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.03x faster                                            |
| async_tree_io              | 847 ms                                                       | 827 ms: 1.02x faster                                             |
| asyncio_tcp                | 380 ms                                                       | 371 ms: 1.02x faster                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 563 ms: 1.02x faster                                             |
| sqlite_synth               | 2.79 us                                                      | 2.74 us: 1.02x faster                                            |
| chaos                      | 61.7 ms                                                      | 60.7 ms: 1.02x faster                                            |
| xml_etree_process          | 60.9 ms                                                      | 60.0 ms: 1.02x faster                                            |
| spectral_norm              | 97.4 ms                                                      | 96.0 ms: 1.01x faster                                            |
| hexiom                     | 6.33 ms                                                      | 6.24 ms: 1.01x faster                                            |
| sympy_expand               | 505 ms                                                       | 498 ms: 1.01x faster                                             |
| html5lib                   | 71.9 ms                                                      | 71.1 ms: 1.01x faster                                            |
| json                       | 5.22 ms                                                      | 5.16 ms: 1.01x faster                                            |
| pprint_pformat             | 1.65 sec                                                     | 1.63 sec: 1.01x faster                                           |
| pprint_safe_repr           | 812 ms                                                       | 803 ms: 1.01x faster                                             |
| sympy_str                  | 296 ms                                                       | 293 ms: 1.01x faster                                             |
| unpickle_list              | 4.62 us                                                      | 4.58 us: 1.01x faster                                            |
| sqlglot_optimize           | 59.7 ms                                                      | 59.1 ms: 1.01x faster                                            |
| pycparser                  | 1.26 sec                                                     | 1.25 sec: 1.01x faster                                           |
| mdp                        | 2.52 sec                                                     | 2.51 sec: 1.01x faster                                           |
| pickle                     | 10.5 us                                                      | 10.5 us: 1.01x faster                                            |
| sympy_sum                  | 154 ms                                                       | 153 ms: 1.01x faster                                             |
| sqlglot_transpile          | 1.78 ms                                                      | 1.77 ms: 1.01x faster                                            |
| regex_dna                  | 244 ms                                                       | 243 ms: 1.00x faster                                             |
| pidigits                   | 253 ms                                                       | 252 ms: 1.00x faster                                             |
| nqueens                    | 88.2 ms                                                      | 88.0 ms: 1.00x faster                                            |
| python_startup_no_site     | 8.94 ms                                                      | 8.96 ms: 1.00x slower                                            |
| sympy_integrate            | 23.3 ms                                                      | 23.4 ms: 1.00x slower                                            |
| pickle_pure_python         | 318 us                                                       | 320 us: 1.01x slower                                             |
| scimark_monte_carlo        | 64.9 ms                                                      | 65.4 ms: 1.01x slower                                            |
| asyncio_websockets         | 382 ms                                                       | 385 ms: 1.01x slower                                             |
| comprehensions             | 17.3 us                                                      | 17.4 us: 1.01x slower                                            |
| crypto_pyaes               | 72.8 ms                                                      | 73.4 ms: 1.01x slower                                            |
| logging_format             | 7.07 us                                                      | 7.14 us: 1.01x slower                                            |
| sqlglot_parse              | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                            |
| deltablue                  | 3.41 ms                                                      | 3.44 ms: 1.01x slower                                            |
| async_generators           | 359 ms                                                       | 364 ms: 1.01x slower                                             |
| xml_etree_iterparse        | 100 ms                                                       | 102 ms: 1.01x slower                                             |
| regex_effbot               | 3.37 ms                                                      | 3.43 ms: 1.02x slower                                            |
| coverage                   | 81.1 ms                                                      | 82.6 ms: 1.02x slower                                            |
| async_tree_io_tg           | 819 ms                                                       | 837 ms: 1.02x slower                                             |
| nbody                      | 88.0 ms                                                      | 90.1 ms: 1.02x slower                                            |
| logging_simple             | 6.40 us                                                      | 6.57 us: 1.03x slower                                            |
| mako                       | 10.4 ms                                                      | 10.7 ms: 1.03x slower                                            |
| dulwich_log                | 65.5 ms                                                      | 67.5 ms: 1.03x slower                                            |
| docutils                   | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                           |
| unpack_sequence            | 56.8 ns                                                      | 58.9 ns: 1.04x slower                                            |
| tomli_loads                | 2.41 sec                                                     | 2.50 sec: 1.04x slower                                           |
| json_dumps                 | 11.0 ms                                                      | 11.4 ms: 1.04x slower                                            |
| json_loads                 | 24.0 us                                                      | 25.3 us: 1.05x slower                                            |
| django_template            | 38.9 ms                                                      | 41.0 ms: 1.06x slower                                            |
| python_startup             | 13.3 ms                                                      | 15.0 ms: 1.12x slower                                            |
| gc_traversal               | 4.11 ms                                                      | 5.32 ms: 1.29x slower                                            |
| create_gc_cycles           | 1.76 ms                                                      | 2.97 ms: 1.69x slower                                            |
| bench_mp_pool              | 4.65 ms                                                      | 1.94 sec: 416.26x slower                                         |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                     |

Benchmark hidden because not significant (12): typing_runtime_protocols, xml_etree_parse, thrift, pylint, xml_etree_generate, asyncio_tcp_ssl, sqlglot_normalize, unpickle_pure_python, logging_silent, float, unpickle, bench_thread_pool
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: sphinx

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x