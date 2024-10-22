# Results vs. 3.13.0

- fork: savannahostrowski
- ref: remove_ghccc
- machine: linux-x86_64
- commit hash: 9827ade
- commit date: 2024-10-16
- overall geometric mean: 1.08x slower
- HPT reliability: 74.11%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 314 ms: 1.08x slower                                                            |
| docutils       | 2.81 sec                                                     | 3.19 sec: 1.14x slower                                                          |
| html5lib       | 71.9 ms                                                      | 70.9 ms: 1.01x faster                                                           |
| tornado_http   | 120 ms                                                       | 121 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 377 ms: 1.22x faster                                                            |
| async_tree_none            | 372 ms                                                       | 335 ms: 1.11x faster                                                            |
| async_tree_memoization     | 452 ms                                                       | 413 ms: 1.09x faster                                                            |
| async_tree_none_tg         | 340 ms                                                       | 323 ms: 1.05x faster                                                            |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 582 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 566 ms: 1.01x faster                                                            |
| asyncio_tcp                | 380 ms                                                       | 376 ms: 1.01x faster                                                            |
| coroutines                 | 21.6 ms                                                      | 21.8 ms: 1.01x slower                                                           |
| async_tree_io_tg           | 819 ms                                                       | 869 ms: 1.06x slower                                                            |
| async_generators           | 359 ms                                                       | 386 ms: 1.07x slower                                                            |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                    |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 83.5 ms: 1.05x faster                                                           |
| float          | 81.9 ms                                                      | 79.4 ms: 1.03x faster                                                           |
| pidigits       | 253 ms                                                       | 252 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 232 ms: 1.05x faster                                                            |
| regex_v8       | 26.2 ms                                                      | 25.0 ms: 1.05x faster                                                           |
| regex_compile  | 144 ms                                                       | 148 ms: 1.03x slower                                                            |
| regex_effbot   | 3.37 ms                                                      | 3.47 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.11 sec: 1.14x faster                                                          |
| xml_etree_process    | 60.9 ms                                                      | 57.8 ms: 1.05x faster                                                           |
| xml_etree_generate   | 85.3 ms                                                      | 82.0 ms: 1.04x faster                                                           |
| xml_etree_parse      | 145 ms                                                       | 143 ms: 1.01x faster                                                            |
| unpickle             | 15.1 us                                                      | 15.0 us: 1.01x faster                                                           |
| json_dumps           | 11.0 ms                                                      | 11.0 ms: 1.01x slower                                                           |
| pickle_list          | 4.59 us                                                      | 4.64 us: 1.01x slower                                                           |
| json_loads           | 24.0 us                                                      | 24.5 us: 1.02x slower                                                           |
| unpickle_pure_python | 214 us                                                       | 219 us: 1.02x slower                                                            |
| pickle               | 10.5 us                                                      | 10.8 us: 1.02x slower                                                           |
| unpickle_list        | 4.62 us                                                      | 4.76 us: 1.03x slower                                                           |
| pickle_dict          | 32.1 us                                                      | 33.3 us: 1.04x slower                                                           |
| pickle_pure_python   | 318 us                                                       | 335 us: 1.05x slower                                                            |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 8.99 ms: 1.00x slower                                                           |
| python_startup         | 13.3 ms                                                      | 14.9 ms: 1.12x slower                                                           |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.44 ms: 1.10x faster                                                           |
| genshi_text     | 26.6 ms                                                      | 27.9 ms: 1.05x slower                                                           |
| genshi_xml      | 57.3 ms                                                      | 61.8 ms: 1.08x slower                                                           |
| django_template | 38.9 ms                                                      | 43.3 ms: 1.11x slower                                                           |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 29.6 us: 1.33x faster                                                           |
| deepcopy                   | 397 us                                                       | 313 us: 1.27x faster                                                            |
| async_tree_memoization_tg  | 461 ms                                                       | 377 ms: 1.22x faster                                                            |
| scimark_sor                | 126 ms                                                       | 105 ms: 1.20x faster                                                            |
| deepcopy_reduce            | 3.54 us                                                      | 3.02 us: 1.17x faster                                                           |
| richards_super             | 59.8 ms                                                      | 51.4 ms: 1.16x faster                                                           |
| richards                   | 52.7 ms                                                      | 45.5 ms: 1.16x faster                                                           |
| tomli_loads                | 2.41 sec                                                     | 2.11 sec: 1.14x faster                                                          |
| async_tree_none            | 372 ms                                                       | 335 ms: 1.11x faster                                                            |
| telco                      | 8.58 ms                                                      | 7.78 ms: 1.10x faster                                                           |
| mako                       | 10.4 ms                                                      | 9.44 ms: 1.10x faster                                                           |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                                           |
| async_tree_memoization     | 452 ms                                                       | 413 ms: 1.09x faster                                                            |
| scimark_fft                | 314 ms                                                       | 288 ms: 1.09x faster                                                            |
| pyflate                    | 492 ms                                                       | 452 ms: 1.09x faster                                                            |
| bpe_tokeniser              | 5.10 sec                                                     | 4.77 sec: 1.07x faster                                                          |
| logging_silent             | 97.7 ns                                                      | 92.1 ns: 1.06x faster                                                           |
| nbody                      | 88.0 ms                                                      | 83.5 ms: 1.05x faster                                                           |
| xml_etree_process          | 60.9 ms                                                      | 57.8 ms: 1.05x faster                                                           |
| spectral_norm              | 97.4 ms                                                      | 92.5 ms: 1.05x faster                                                           |
| regex_dna                  | 244 ms                                                       | 232 ms: 1.05x faster                                                            |
| async_tree_none_tg         | 340 ms                                                       | 323 ms: 1.05x faster                                                            |
| regex_v8                   | 26.2 ms                                                      | 25.0 ms: 1.05x faster                                                           |
| go                         | 160 ms                                                       | 154 ms: 1.04x faster                                                            |
| xml_etree_generate         | 85.3 ms                                                      | 82.0 ms: 1.04x faster                                                           |
| deltablue                  | 3.41 ms                                                      | 3.30 ms: 1.03x faster                                                           |
| float                      | 81.9 ms                                                      | 79.4 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 582 ms: 1.03x faster                                                            |
| sqlite_synth               | 2.79 us                                                      | 2.71 us: 1.03x faster                                                           |
| crypto_pyaes               | 72.8 ms                                                      | 71.1 ms: 1.02x faster                                                           |
| pprint_safe_repr           | 812 ms                                                       | 796 ms: 1.02x faster                                                            |
| coverage                   | 81.1 ms                                                      | 79.8 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 566 ms: 1.01x faster                                                            |
| xml_etree_parse            | 145 ms                                                       | 143 ms: 1.01x faster                                                            |
| html5lib                   | 71.9 ms                                                      | 70.9 ms: 1.01x faster                                                           |
| dulwich_log                | 65.5 ms                                                      | 64.6 ms: 1.01x faster                                                           |
| json                       | 5.22 ms                                                      | 5.16 ms: 1.01x faster                                                           |
| asyncio_tcp                | 380 ms                                                       | 376 ms: 1.01x faster                                                            |
| unpickle                   | 15.1 us                                                      | 15.0 us: 1.01x faster                                                           |
| pidigits                   | 253 ms                                                       | 252 ms: 1.00x faster                                                            |
| python_startup_no_site     | 8.94 ms                                                      | 8.99 ms: 1.00x slower                                                           |
| json_dumps                 | 11.0 ms                                                      | 11.0 ms: 1.01x slower                                                           |
| coroutines                 | 21.6 ms                                                      | 21.8 ms: 1.01x slower                                                           |
| pickle_list                | 4.59 us                                                      | 4.64 us: 1.01x slower                                                           |
| tornado_http               | 120 ms                                                       | 121 ms: 1.01x slower                                                            |
| fannkuch                   | 365 ms                                                       | 371 ms: 1.02x slower                                                            |
| thrift                     | 877 us                                                       | 894 us: 1.02x slower                                                            |
| logging_format             | 7.07 us                                                      | 7.22 us: 1.02x slower                                                           |
| json_loads                 | 24.0 us                                                      | 24.5 us: 1.02x slower                                                           |
| unpickle_pure_python       | 214 us                                                       | 219 us: 1.02x slower                                                            |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.38 ms: 1.02x slower                                                           |
| pickle                     | 10.5 us                                                      | 10.8 us: 1.02x slower                                                           |
| regex_compile              | 144 ms                                                       | 148 ms: 1.03x slower                                                            |
| unpickle_list              | 4.62 us                                                      | 4.76 us: 1.03x slower                                                           |
| regex_effbot               | 3.37 ms                                                      | 3.47 ms: 1.03x slower                                                           |
| logging_simple             | 6.40 us                                                      | 6.59 us: 1.03x slower                                                           |
| mdp                        | 2.52 sec                                                     | 2.60 sec: 1.03x slower                                                          |
| typing_runtime_protocols   | 174 us                                                       | 180 us: 1.03x slower                                                            |
| pycparser                  | 1.26 sec                                                     | 1.30 sec: 1.03x slower                                                          |
| meteor_contest             | 128 ms                                                       | 133 ms: 1.04x slower                                                            |
| pickle_dict                | 32.1 us                                                      | 33.3 us: 1.04x slower                                                           |
| genshi_text                | 26.6 ms                                                      | 27.9 ms: 1.05x slower                                                           |
| pickle_pure_python         | 318 us                                                       | 335 us: 1.05x slower                                                            |
| sympy_expand               | 505 ms                                                       | 534 ms: 1.06x slower                                                            |
| async_tree_io_tg           | 819 ms                                                       | 869 ms: 1.06x slower                                                            |
| bench_thread_pool          | 901 us                                                       | 958 us: 1.06x slower                                                            |
| async_generators           | 359 ms                                                       | 386 ms: 1.07x slower                                                            |
| comprehensions             | 17.3 us                                                      | 18.6 us: 1.08x slower                                                           |
| chaos                      | 61.7 ms                                                      | 66.4 ms: 1.08x slower                                                           |
| genshi_xml                 | 57.3 ms                                                      | 61.8 ms: 1.08x slower                                                           |
| sympy_str                  | 296 ms                                                       | 319 ms: 1.08x slower                                                            |
| 2to3                       | 291 ms                                                       | 314 ms: 1.08x slower                                                            |
| scimark_monte_carlo        | 64.9 ms                                                      | 70.2 ms: 1.08x slower                                                           |
| sqlglot_parse              | 1.38 ms                                                      | 1.51 ms: 1.09x slower                                                           |
| sqlglot_normalize          | 118 ms                                                       | 132 ms: 1.11x slower                                                            |
| django_template            | 38.9 ms                                                      | 43.3 ms: 1.11x slower                                                           |
| hexiom                     | 6.33 ms                                                      | 7.06 ms: 1.12x slower                                                           |
| sqlglot_transpile          | 1.78 ms                                                      | 1.99 ms: 1.12x slower                                                           |
| python_startup             | 13.3 ms                                                      | 14.9 ms: 1.12x slower                                                           |
| raytrace                   | 289 ms                                                       | 324 ms: 1.12x slower                                                            |
| sympy_sum                  | 154 ms                                                       | 174 ms: 1.13x slower                                                            |
| docutils                   | 2.81 sec                                                     | 3.19 sec: 1.14x slower                                                          |
| generators                 | 33.5 ms                                                      | 38.1 ms: 1.14x slower                                                           |
| nqueens                    | 88.2 ms                                                      | 102 ms: 1.16x slower                                                            |
| sqlglot_optimize           | 59.7 ms                                                      | 69.5 ms: 1.16x slower                                                           |
| sympy_integrate            | 23.3 ms                                                      | 27.2 ms: 1.17x slower                                                           |
| pylint                     | 346 ms                                                       | 424 ms: 1.23x slower                                                            |
| gc_traversal               | 4.11 ms                                                      | 5.48 ms: 1.33x slower                                                           |
| unpack_sequence            | 56.8 ns                                                      | 88.4 ns: 1.56x slower                                                           |
| create_gc_cycles           | 1.76 ms                                                      | 2.90 ms: 1.65x slower                                                           |
| bench_mp_pool              | 4.65 ms                                                      | 1.98 sec: 425.39x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                                    |

Benchmark hidden because not significant (6): scimark_lu, asyncio_tcp_ssl, pprint_pformat, xml_etree_iterparse, asyncio_websockets, async_tree_io
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241016-3.14.0a1+-9827ade-JIT/bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade.json: sphinx

# HPT report

- Reliability score: 74.11% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.20x