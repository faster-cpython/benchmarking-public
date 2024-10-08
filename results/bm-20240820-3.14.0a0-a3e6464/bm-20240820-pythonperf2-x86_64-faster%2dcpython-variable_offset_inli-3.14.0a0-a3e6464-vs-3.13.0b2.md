# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: variable_offset_inli
- machine: linux-x86_64
- commit hash: a3e6464
- commit date: 2024-08-20
- overall geometric mean: 1.02x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 288 ms: 1.01x faster                                                                  |
| docutils       | 2.98 sec                                                         | 2.94 sec: 1.01x faster                                                                |
| html5lib       | 74.7 ms                                                          | 73.8 ms: 1.01x faster                                                                 |
| tornado_http   | 119 ms                                                           | 118 ms: 1.01x faster                                                                  |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 399 ms: 1.15x faster                                                                  |
| async_tree_io_tg           | 900 ms                                                           | 787 ms: 1.14x faster                                                                  |
| async_tree_none            | 365 ms                                                           | 320 ms: 1.14x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                           | 311 ms: 1.10x faster                                                                  |
| async_tree_io              | 873 ms                                                           | 806 ms: 1.08x faster                                                                  |
| async_tree_memoization_tg  | 421 ms                                                           | 393 ms: 1.07x faster                                                                  |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 573 ms: 1.05x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 552 ms: 1.04x faster                                                                  |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 79.7 ms: 1.01x faster                                                                 |
| pidigits       | 254 ms                                                           | 256 ms: 1.01x slower                                                                  |
| Geometric mean | (ref)                                                            | 1.00x slower                                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 139 ms: 1.04x faster                                                                  |
| regex_dna      | 249 ms                                                           | 255 ms: 1.02x slower                                                                  |
| regex_effbot   | 3.40 ms                                                          | 3.52 ms: 1.04x slower                                                                 |
| regex_v8       | 26.0 ms                                                          | 27.6 ms: 1.06x slower                                                                 |
| Geometric mean | (ref)                                                            | 1.02x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.24 sec: 1.07x faster                                                                |
| unpickle_pure_python | 224 us                                                           | 218 us: 1.03x faster                                                                  |
| xml_etree_process    | 59.7 ms                                                          | 58.4 ms: 1.02x faster                                                                 |
| xml_etree_generate   | 85.7 ms                                                          | 84.3 ms: 1.02x faster                                                                 |
| json_dumps           | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                                 |
| pickle_pure_python   | 307 us                                                           | 318 us: 1.04x slower                                                                  |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                                          |

Benchmark hidden because not significant (3): json_loads, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                                 |
| python_startup_no_site | 8.85 ms                                                          | 9.07 ms: 1.02x slower                                                                 |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|-----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 54.9 ms: 1.06x faster                                                                 |
| django_template | 39.0 ms                                                          | 39.4 ms: 1.01x slower                                                                 |
| Geometric mean  | (ref)                                                            | 1.01x faster                                                                          |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 286 us: 1.32x faster                                                                  |
| deepcopy_memo              | 37.3 us                                                          | 29.2 us: 1.28x faster                                                                 |
| deepcopy_reduce            | 3.39 us                                                          | 2.91 us: 1.17x faster                                                                 |
| async_tree_memoization     | 460 ms                                                           | 399 ms: 1.15x faster                                                                  |
| async_tree_io_tg           | 900 ms                                                           | 787 ms: 1.14x faster                                                                  |
| async_tree_none            | 365 ms                                                           | 320 ms: 1.14x faster                                                                  |
| generators                 | 33.5 ms                                                          | 30.2 ms: 1.11x faster                                                                 |
| async_tree_none_tg         | 340 ms                                                           | 311 ms: 1.10x faster                                                                  |
| async_tree_io              | 873 ms                                                           | 806 ms: 1.08x faster                                                                  |
| richards_super             | 61.2 ms                                                          | 56.5 ms: 1.08x faster                                                                 |
| tomli_loads                | 2.40 sec                                                         | 2.24 sec: 1.07x faster                                                                |
| async_tree_memoization_tg  | 421 ms                                                           | 393 ms: 1.07x faster                                                                  |
| pathlib                    | 17.1 ms                                                          | 16.0 ms: 1.07x faster                                                                 |
| bench_mp_pool              | 4.91 ms                                                          | 4.59 ms: 1.07x faster                                                                 |
| richards                   | 53.4 ms                                                          | 50.1 ms: 1.07x faster                                                                 |
| coverage                   | 83.5 ms                                                          | 78.4 ms: 1.06x faster                                                                 |
| bench_thread_pool          | 908 us                                                           | 854 us: 1.06x faster                                                                  |
| genshi_xml                 | 58.1 ms                                                          | 54.9 ms: 1.06x faster                                                                 |
| telco                      | 8.40 ms                                                          | 7.95 ms: 1.06x faster                                                                 |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 573 ms: 1.05x faster                                                                  |
| bpe_tokeniser              | 5.14 sec                                                         | 4.92 sec: 1.04x faster                                                                |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 552 ms: 1.04x faster                                                                  |
| scimark_fft                | 312 ms                                                           | 301 ms: 1.04x faster                                                                  |
| regex_compile              | 144 ms                                                           | 139 ms: 1.04x faster                                                                  |
| go                         | 165 ms                                                           | 160 ms: 1.03x faster                                                                  |
| asyncio_websockets         | 395 ms                                                           | 384 ms: 1.03x faster                                                                  |
| unpickle_pure_python       | 224 us                                                           | 218 us: 1.03x faster                                                                  |
| coroutines                 | 22.0 ms                                                          | 21.4 ms: 1.03x faster                                                                 |
| asyncio_tcp                | 378 ms                                                           | 368 ms: 1.03x faster                                                                  |
| logging_format             | 7.11 us                                                          | 6.95 us: 1.02x faster                                                                 |
| xml_etree_process          | 59.7 ms                                                          | 58.4 ms: 1.02x faster                                                                 |
| gc_traversal               | 4.69 ms                                                          | 4.58 ms: 1.02x faster                                                                 |
| scimark_lu                 | 97.5 ms                                                          | 95.3 ms: 1.02x faster                                                                 |
| sympy_sum                  | 155 ms                                                           | 152 ms: 1.02x faster                                                                  |
| meteor_contest             | 128 ms                                                           | 126 ms: 1.02x faster                                                                  |
| sqlglot_optimize           | 59.5 ms                                                          | 58.4 ms: 1.02x faster                                                                 |
| thrift                     | 880 us                                                           | 864 us: 1.02x faster                                                                  |
| sympy_str                  | 295 ms                                                           | 290 ms: 1.02x faster                                                                  |
| xml_etree_generate         | 85.7 ms                                                          | 84.3 ms: 1.02x faster                                                                 |
| scimark_sor                | 119 ms                                                           | 117 ms: 1.02x faster                                                                  |
| docutils                   | 2.98 sec                                                         | 2.94 sec: 1.01x faster                                                                |
| spectral_norm              | 97.3 ms                                                          | 96.1 ms: 1.01x faster                                                                 |
| sqlglot_normalize          | 120 ms                                                           | 119 ms: 1.01x faster                                                                  |
| html5lib                   | 74.7 ms                                                          | 73.8 ms: 1.01x faster                                                                 |
| sympy_integrate            | 23.2 ms                                                          | 22.9 ms: 1.01x faster                                                                 |
| 2to3                       | 291 ms                                                           | 288 ms: 1.01x faster                                                                  |
| tornado_http               | 119 ms                                                           | 118 ms: 1.01x faster                                                                  |
| json_dumps                 | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                                 |
| sympy_expand               | 501 ms                                                           | 497 ms: 1.01x faster                                                                  |
| float                      | 80.2 ms                                                          | 79.7 ms: 1.01x faster                                                                 |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.58 sec: 1.00x faster                                                                |
| nqueens                    | 88.4 ms                                                          | 88.6 ms: 1.00x slower                                                                 |
| logging_simple             | 6.40 us                                                          | 6.44 us: 1.01x slower                                                                 |
| pidigits                   | 254 ms                                                           | 256 ms: 1.01x slower                                                                  |
| pyflate                    | 482 ms                                                           | 487 ms: 1.01x slower                                                                  |
| django_template            | 39.0 ms                                                          | 39.4 ms: 1.01x slower                                                                 |
| typing_runtime_protocols   | 171 us                                                           | 173 us: 1.01x slower                                                                  |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                                 |
| mdp                        | 2.46 sec                                                         | 2.49 sec: 1.01x slower                                                                |
| async_generators           | 363 ms                                                           | 368 ms: 1.02x slower                                                                  |
| comprehensions             | 17.0 us                                                          | 17.3 us: 1.02x slower                                                                 |
| pprint_safe_repr           | 818 ms                                                           | 834 ms: 1.02x slower                                                                  |
| regex_dna                  | 249 ms                                                           | 255 ms: 1.02x slower                                                                  |
| create_gc_cycles           | 2.00 ms                                                          | 2.05 ms: 1.02x slower                                                                 |
| python_startup_no_site     | 8.85 ms                                                          | 9.07 ms: 1.02x slower                                                                 |
| deltablue                  | 3.37 ms                                                          | 3.46 ms: 1.03x slower                                                                 |
| pprint_pformat             | 1.66 sec                                                         | 1.70 sec: 1.03x slower                                                                |
| regex_effbot               | 3.40 ms                                                          | 3.52 ms: 1.04x slower                                                                 |
| pickle_pure_python         | 307 us                                                           | 318 us: 1.04x slower                                                                  |
| scimark_monte_carlo        | 65.5 ms                                                          | 68.2 ms: 1.04x slower                                                                 |
| regex_v8                   | 26.0 ms                                                          | 27.6 ms: 1.06x slower                                                                 |
| chaos                      | 59.6 ms                                                          | 63.8 ms: 1.07x slower                                                                 |
| logging_silent             | 96.3 ns                                                          | 103 ns: 1.07x slower                                                                  |
| raytrace                   | 260 ms                                                           | 291 ms: 1.12x slower                                                                  |
| Geometric mean             | (ref)                                                            | 1.02x faster                                                                          |

Benchmark hidden because not significant (15): json, json_loads, sqlglot_parse, hexiom, sqlglot_transpile, nbody, genshi_text, xml_etree_parse, scimark_sparse_mat_mult, crypto_pyaes, fannkuch, mako, pycparser, xml_etree_iterparse, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x