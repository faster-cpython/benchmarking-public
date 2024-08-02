# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: bound_method_instrum
- machine: linux-x86_64
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.02x faster
- HPT reliability: 99.87%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 287 ms: 1.02x faster                                                                  |
| docutils       | 2.98 sec                                                         | 2.97 sec: 1.00x faster                                                                |
| html5lib       | 74.7 ms                                                          | 74.1 ms: 1.01x faster                                                                 |
| tornado_http   | 119 ms                                                           | 117 ms: 1.02x faster                                                                  |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 775 ms: 1.16x faster                                                                  |
| async_tree_memoization     | 460 ms                                                           | 405 ms: 1.13x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                           | 306 ms: 1.11x faster                                                                  |
| async_tree_none            | 365 ms                                                           | 335 ms: 1.09x faster                                                                  |
| async_tree_memoization_tg  | 421 ms                                                           | 386 ms: 1.09x faster                                                                  |
| async_tree_io              | 873 ms                                                           | 817 ms: 1.07x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 542 ms: 1.06x faster                                                                  |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 580 ms: 1.04x faster                                                                  |
| Geometric mean             | (ref)                                                            | 1.09x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 85.1 ms: 1.03x faster                                                                 |
| float          | 80.2 ms                                                          | 80.6 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 141 ms: 1.02x faster                                                                  |
| regex_v8       | 26.0 ms                                                          | 25.5 ms: 1.02x faster                                                                 |
| regex_dna      | 249 ms                                                           | 245 ms: 1.02x faster                                                                  |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 224 us                                                           | 216 us: 1.04x faster                                                                  |
| xml_etree_generate   | 85.7 ms                                                          | 85.4 ms: 1.00x faster                                                                 |
| xml_etree_parse      | 144 ms                                                           | 144 ms: 1.01x slower                                                                  |
| tomli_loads          | 2.40 sec                                                         | 2.45 sec: 1.02x slower                                                                |
| xml_etree_iterparse  | 103 ms                                                           | 104 ms: 1.02x slower                                                                  |
| pickle_pure_python   | 307 us                                                           | 319 us: 1.04x slower                                                                  |
| Geometric mean       | (ref)                                                            | 1.00x slower                                                                          |

Benchmark hidden because not significant (3): json_loads, xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                                 |
| python_startup_no_site | 8.85 ms                                                          | 9.06 ms: 1.02x slower                                                                 |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 54.0 ms: 1.07x faster                                                                 |
| genshi_text     | 25.9 ms                                                          | 25.0 ms: 1.04x faster                                                                 |
| mako            | 10.4 ms                                                          | 10.5 ms: 1.01x slower                                                                 |
| django_template | 39.0 ms                                                          | 40.2 ms: 1.03x slower                                                                 |
| Geometric mean  | (ref)                                                            | 1.02x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 289 us: 1.31x faster                                                                  |
| deepcopy_memo              | 37.3 us                                                          | 30.7 us: 1.21x faster                                                                 |
| deepcopy_reduce            | 3.39 us                                                          | 2.90 us: 1.17x faster                                                                 |
| async_tree_io_tg           | 900 ms                                                           | 775 ms: 1.16x faster                                                                  |
| generators                 | 33.5 ms                                                          | 29.0 ms: 1.16x faster                                                                 |
| async_tree_memoization     | 460 ms                                                           | 405 ms: 1.13x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                           | 306 ms: 1.11x faster                                                                  |
| async_tree_none            | 365 ms                                                           | 335 ms: 1.09x faster                                                                  |
| async_tree_memoization_tg  | 421 ms                                                           | 386 ms: 1.09x faster                                                                  |
| pathlib                    | 17.1 ms                                                          | 15.9 ms: 1.08x faster                                                                 |
| bench_mp_pool              | 4.91 ms                                                          | 4.57 ms: 1.08x faster                                                                 |
| genshi_xml                 | 58.1 ms                                                          | 54.0 ms: 1.07x faster                                                                 |
| async_tree_io              | 873 ms                                                           | 817 ms: 1.07x faster                                                                  |
| telco                      | 8.40 ms                                                          | 7.89 ms: 1.06x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 542 ms: 1.06x faster                                                                  |
| scimark_fft                | 312 ms                                                           | 297 ms: 1.05x faster                                                                  |
| gc_traversal               | 4.69 ms                                                          | 4.49 ms: 1.04x faster                                                                 |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 580 ms: 1.04x faster                                                                  |
| bpe_tokeniser              | 5.14 sec                                                         | 4.94 sec: 1.04x faster                                                                |
| bench_thread_pool          | 908 us                                                           | 874 us: 1.04x faster                                                                  |
| unpickle_pure_python       | 224 us                                                           | 216 us: 1.04x faster                                                                  |
| genshi_text                | 25.9 ms                                                          | 25.0 ms: 1.04x faster                                                                 |
| logging_format             | 7.11 us                                                          | 6.86 us: 1.04x faster                                                                 |
| crypto_pyaes               | 73.6 ms                                                          | 71.3 ms: 1.03x faster                                                                 |
| nbody                      | 87.8 ms                                                          | 85.1 ms: 1.03x faster                                                                 |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.15 ms: 1.03x faster                                                                 |
| richards_super             | 61.2 ms                                                          | 59.5 ms: 1.03x faster                                                                 |
| logging_simple             | 6.40 us                                                          | 6.23 us: 1.03x faster                                                                 |
| richards                   | 53.4 ms                                                          | 52.1 ms: 1.03x faster                                                                 |
| spectral_norm              | 97.3 ms                                                          | 95.2 ms: 1.02x faster                                                                 |
| regex_compile              | 144 ms                                                           | 141 ms: 1.02x faster                                                                  |
| tornado_http               | 119 ms                                                           | 117 ms: 1.02x faster                                                                  |
| regex_v8                   | 26.0 ms                                                          | 25.5 ms: 1.02x faster                                                                 |
| regex_dna                  | 249 ms                                                           | 245 ms: 1.02x faster                                                                  |
| sqlglot_normalize          | 120 ms                                                           | 118 ms: 1.02x faster                                                                  |
| dask                       | 391 ms                                                           | 384 ms: 1.02x faster                                                                  |
| dulwich_log                | 67.3 ms                                                          | 66.2 ms: 1.02x faster                                                                 |
| sqlglot_optimize           | 59.5 ms                                                          | 58.6 ms: 1.02x faster                                                                 |
| 2to3                       | 291 ms                                                           | 287 ms: 1.02x faster                                                                  |
| meteor_contest             | 128 ms                                                           | 126 ms: 1.01x faster                                                                  |
| nqueens                    | 88.4 ms                                                          | 87.2 ms: 1.01x faster                                                                 |
| go                         | 165 ms                                                           | 163 ms: 1.01x faster                                                                  |
| asyncio_tcp                | 378 ms                                                           | 374 ms: 1.01x faster                                                                  |
| sympy_sum                  | 155 ms                                                           | 154 ms: 1.01x faster                                                                  |
| asyncio_websockets         | 395 ms                                                           | 392 ms: 1.01x faster                                                                  |
| html5lib                   | 74.7 ms                                                          | 74.1 ms: 1.01x faster                                                                 |
| pycparser                  | 1.22 sec                                                         | 1.21 sec: 1.01x faster                                                                |
| coroutines                 | 22.0 ms                                                          | 21.9 ms: 1.00x faster                                                                 |
| xml_etree_generate         | 85.7 ms                                                          | 85.4 ms: 1.00x faster                                                                 |
| docutils                   | 2.98 sec                                                         | 2.97 sec: 1.00x faster                                                                |
| sympy_str                  | 295 ms                                                           | 294 ms: 1.00x faster                                                                  |
| sympy_expand               | 501 ms                                                           | 503 ms: 1.00x slower                                                                  |
| float                      | 80.2 ms                                                          | 80.6 ms: 1.01x slower                                                                 |
| xml_etree_parse            | 144 ms                                                           | 144 ms: 1.01x slower                                                                  |
| sqlglot_transpile          | 1.76 ms                                                          | 1.78 ms: 1.01x slower                                                                 |
| pyflate                    | 482 ms                                                           | 485 ms: 1.01x slower                                                                  |
| scimark_sor                | 119 ms                                                           | 120 ms: 1.01x slower                                                                  |
| coverage                   | 83.5 ms                                                          | 84.2 ms: 1.01x slower                                                                 |
| typing_runtime_protocols   | 171 us                                                           | 173 us: 1.01x slower                                                                  |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                                 |
| pprint_pformat             | 1.66 sec                                                         | 1.68 sec: 1.01x slower                                                                |
| mako                       | 10.4 ms                                                          | 10.5 ms: 1.01x slower                                                                 |
| json                       | 5.35 ms                                                          | 5.43 ms: 1.01x slower                                                                 |
| async_generators           | 363 ms                                                           | 368 ms: 1.01x slower                                                                  |
| deltablue                  | 3.37 ms                                                          | 3.43 ms: 1.02x slower                                                                 |
| tomli_loads                | 2.40 sec                                                         | 2.45 sec: 1.02x slower                                                                |
| xml_etree_iterparse        | 103 ms                                                           | 104 ms: 1.02x slower                                                                  |
| logging_silent             | 96.3 ns                                                          | 98.1 ns: 1.02x slower                                                                 |
| comprehensions             | 17.0 us                                                          | 17.4 us: 1.02x slower                                                                 |
| python_startup_no_site     | 8.85 ms                                                          | 9.06 ms: 1.02x slower                                                                 |
| django_template            | 39.0 ms                                                          | 40.2 ms: 1.03x slower                                                                 |
| mdp                        | 2.46 sec                                                         | 2.55 sec: 1.03x slower                                                                |
| pickle_pure_python         | 307 us                                                           | 319 us: 1.04x slower                                                                  |
| scimark_monte_carlo        | 65.5 ms                                                          | 68.3 ms: 1.04x slower                                                                 |
| chaos                      | 59.6 ms                                                          | 62.9 ms: 1.05x slower                                                                 |
| raytrace                   | 260 ms                                                           | 275 ms: 1.06x slower                                                                  |
| fannkuch                   | 353 ms                                                           | 373 ms: 1.06x slower                                                                  |
| Geometric mean             | (ref)                                                            | 1.02x faster                                                                          |

Benchmark hidden because not significant (14): json_loads, thrift, create_gc_cycles, hexiom, asyncio_tcp_ssl, regex_effbot, xml_etree_process, pidigits, pprint_safe_repr, json_dumps, sympy_integrate, sqlglot_parse, scimark_lu, pylint
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.87% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x