# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: fix_not_specialized_
- machine: linux-x86_64
- commit hash: 10855bc
- commit date: 2024-08-22
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 287 ms: 1.02x faster                                                                  |
| docutils       | 2.98 sec                                                         | 2.94 sec: 1.01x faster                                                                |
| html5lib       | 74.7 ms                                                          | 72.8 ms: 1.03x faster                                                                 |
| tornado_http   | 119 ms                                                           | 117 ms: 1.02x faster                                                                  |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|----------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 398 ms: 1.15x faster                                                                  |
| async_tree_io_tg           | 900 ms                                                           | 781 ms: 1.15x faster                                                                  |
| async_tree_none            | 365 ms                                                           | 318 ms: 1.15x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                           | 307 ms: 1.11x faster                                                                  |
| async_tree_io              | 873 ms                                                           | 797 ms: 1.10x faster                                                                  |
| async_tree_memoization_tg  | 421 ms                                                           | 388 ms: 1.08x faster                                                                  |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 568 ms: 1.06x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 544 ms: 1.05x faster                                                                  |
| Geometric mean             | (ref)                                                            | 1.11x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 79.3 ms: 1.01x faster                                                                 |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                          |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 138 ms: 1.04x faster                                                                  |
| regex_dna      | 249 ms                                                           | 240 ms: 1.04x faster                                                                  |
| regex_v8       | 26.0 ms                                                          | 26.1 ms: 1.00x slower                                                                 |
| regex_effbot   | 3.40 ms                                                          | 3.62 ms: 1.07x slower                                                                 |
| Geometric mean | (ref)                                                            | 1.00x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|----------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 224 us                                                           | 212 us: 1.06x faster                                                                  |
| tomli_loads          | 2.40 sec                                                         | 2.30 sec: 1.05x faster                                                                |
| xml_etree_generate   | 85.7 ms                                                          | 84.2 ms: 1.02x faster                                                                 |
| xml_etree_iterparse  | 103 ms                                                           | 101 ms: 1.02x faster                                                                  |
| xml_etree_parse      | 144 ms                                                           | 142 ms: 1.01x faster                                                                  |
| json_dumps           | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                                 |
| xml_etree_process    | 59.7 ms                                                          | 59.3 ms: 1.01x faster                                                                 |
| json_loads           | 25.0 us                                                          | 24.9 us: 1.00x faster                                                                 |
| pickle_pure_python   | 307 us                                                           | 321 us: 1.04x slower                                                                  |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                                 |
| python_startup_no_site | 8.85 ms                                                          | 9.04 ms: 1.02x slower                                                                 |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|-----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 55.5 ms: 1.05x faster                                                                 |
| django_template | 39.0 ms                                                          | 39.7 ms: 1.02x slower                                                                 |
| Geometric mean  | (ref)                                                            | 1.01x faster                                                                          |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|----------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 287 us: 1.32x faster                                                                  |
| deepcopy_memo              | 37.3 us                                                          | 29.9 us: 1.24x faster                                                                 |
| generators                 | 33.5 ms                                                          | 28.4 ms: 1.18x faster                                                                 |
| async_tree_memoization     | 460 ms                                                           | 398 ms: 1.15x faster                                                                  |
| deepcopy_reduce            | 3.39 us                                                          | 2.94 us: 1.15x faster                                                                 |
| async_tree_io_tg           | 900 ms                                                           | 781 ms: 1.15x faster                                                                  |
| async_tree_none            | 365 ms                                                           | 318 ms: 1.15x faster                                                                  |
| richards_super             | 61.2 ms                                                          | 55.1 ms: 1.11x faster                                                                 |
| async_tree_none_tg         | 340 ms                                                           | 307 ms: 1.11x faster                                                                  |
| async_tree_io              | 873 ms                                                           | 797 ms: 1.10x faster                                                                  |
| richards                   | 53.4 ms                                                          | 49.0 ms: 1.09x faster                                                                 |
| async_tree_memoization_tg  | 421 ms                                                           | 388 ms: 1.08x faster                                                                  |
| pathlib                    | 17.1 ms                                                          | 15.9 ms: 1.07x faster                                                                 |
| coverage                   | 83.5 ms                                                          | 78.0 ms: 1.07x faster                                                                 |
| bench_mp_pool              | 4.91 ms                                                          | 4.61 ms: 1.07x faster                                                                 |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 568 ms: 1.06x faster                                                                  |
| unpickle_pure_python       | 224 us                                                           | 212 us: 1.06x faster                                                                  |
| bench_thread_pool          | 908 us                                                           | 862 us: 1.05x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 544 ms: 1.05x faster                                                                  |
| telco                      | 8.40 ms                                                          | 7.98 ms: 1.05x faster                                                                 |
| bpe_tokeniser              | 5.14 sec                                                         | 4.91 sec: 1.05x faster                                                                |
| genshi_xml                 | 58.1 ms                                                          | 55.5 ms: 1.05x faster                                                                 |
| tomli_loads                | 2.40 sec                                                         | 2.30 sec: 1.05x faster                                                                |
| regex_compile              | 144 ms                                                           | 138 ms: 1.04x faster                                                                  |
| gc_traversal               | 4.69 ms                                                          | 4.50 ms: 1.04x faster                                                                 |
| regex_dna                  | 249 ms                                                           | 240 ms: 1.04x faster                                                                  |
| scimark_lu                 | 97.5 ms                                                          | 94.7 ms: 1.03x faster                                                                 |
| asyncio_tcp                | 378 ms                                                           | 368 ms: 1.03x faster                                                                  |
| sympy_sum                  | 155 ms                                                           | 151 ms: 1.03x faster                                                                  |
| html5lib                   | 74.7 ms                                                          | 72.8 ms: 1.03x faster                                                                 |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.18 ms: 1.03x faster                                                                 |
| tornado_http               | 119 ms                                                           | 117 ms: 1.02x faster                                                                  |
| pyflate                    | 482 ms                                                           | 471 ms: 1.02x faster                                                                  |
| sqlglot_optimize           | 59.5 ms                                                          | 58.5 ms: 1.02x faster                                                                 |
| thrift                     | 880 us                                                           | 864 us: 1.02x faster                                                                  |
| xml_etree_generate         | 85.7 ms                                                          | 84.2 ms: 1.02x faster                                                                 |
| xml_etree_iterparse        | 103 ms                                                           | 101 ms: 1.02x faster                                                                  |
| 2to3                       | 291 ms                                                           | 287 ms: 1.02x faster                                                                  |
| logging_format             | 7.11 us                                                          | 7.01 us: 1.01x faster                                                                 |
| docutils                   | 2.98 sec                                                         | 2.94 sec: 1.01x faster                                                                |
| crypto_pyaes               | 73.6 ms                                                          | 72.6 ms: 1.01x faster                                                                 |
| coroutines                 | 22.0 ms                                                          | 21.7 ms: 1.01x faster                                                                 |
| xml_etree_parse            | 144 ms                                                           | 142 ms: 1.01x faster                                                                  |
| sympy_str                  | 295 ms                                                           | 291 ms: 1.01x faster                                                                  |
| float                      | 80.2 ms                                                          | 79.3 ms: 1.01x faster                                                                 |
| asyncio_websockets         | 395 ms                                                           | 391 ms: 1.01x faster                                                                  |
| sympy_integrate            | 23.2 ms                                                          | 22.9 ms: 1.01x faster                                                                 |
| logging_simple             | 6.40 us                                                          | 6.34 us: 1.01x faster                                                                 |
| json_dumps                 | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                                 |
| xml_etree_process          | 59.7 ms                                                          | 59.3 ms: 1.01x faster                                                                 |
| meteor_contest             | 128 ms                                                           | 128 ms: 1.01x faster                                                                  |
| json_loads                 | 25.0 us                                                          | 24.9 us: 1.00x faster                                                                 |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.58 sec: 1.00x faster                                                                |
| regex_v8                   | 26.0 ms                                                          | 26.1 ms: 1.00x slower                                                                 |
| go                         | 165 ms                                                           | 166 ms: 1.01x slower                                                                  |
| sqlglot_transpile          | 1.76 ms                                                          | 1.78 ms: 1.01x slower                                                                 |
| scimark_monte_carlo        | 65.5 ms                                                          | 66.0 ms: 1.01x slower                                                                 |
| sqlglot_parse              | 1.39 ms                                                          | 1.41 ms: 1.01x slower                                                                 |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                                 |
| pprint_pformat             | 1.66 sec                                                         | 1.68 sec: 1.01x slower                                                                |
| pprint_safe_repr           | 818 ms                                                           | 827 ms: 1.01x slower                                                                  |
| deltablue                  | 3.37 ms                                                          | 3.43 ms: 1.02x slower                                                                 |
| django_template            | 39.0 ms                                                          | 39.7 ms: 1.02x slower                                                                 |
| python_startup_no_site     | 8.85 ms                                                          | 9.04 ms: 1.02x slower                                                                 |
| logging_silent             | 96.3 ns                                                          | 98.5 ns: 1.02x slower                                                                 |
| chaos                      | 59.6 ms                                                          | 61.1 ms: 1.02x slower                                                                 |
| raytrace                   | 260 ms                                                           | 267 ms: 1.03x slower                                                                  |
| mdp                        | 2.46 sec                                                         | 2.53 sec: 1.03x slower                                                                |
| typing_runtime_protocols   | 171 us                                                           | 176 us: 1.03x slower                                                                  |
| pycparser                  | 1.22 sec                                                         | 1.27 sec: 1.04x slower                                                                |
| pickle_pure_python         | 307 us                                                           | 321 us: 1.04x slower                                                                  |
| comprehensions             | 17.0 us                                                          | 17.8 us: 1.05x slower                                                                 |
| fannkuch                   | 353 ms                                                           | 371 ms: 1.05x slower                                                                  |
| scimark_sor                | 119 ms                                                           | 126 ms: 1.06x slower                                                                  |
| regex_effbot               | 3.40 ms                                                          | 3.62 ms: 1.07x slower                                                                 |
| Geometric mean             | (ref)                                                            | 1.03x faster                                                                          |

Benchmark hidden because not significant (14): scimark_fft, nbody, json, genshi_text, spectral_norm, async_generators, pidigits, sympy_expand, mako, create_gc_cycles, nqueens, hexiom, sqlglot_normalize, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x