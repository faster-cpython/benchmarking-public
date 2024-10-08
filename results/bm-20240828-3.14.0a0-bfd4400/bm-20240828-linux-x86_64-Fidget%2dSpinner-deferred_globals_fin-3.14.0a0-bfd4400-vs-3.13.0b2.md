# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: linux-x86_64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 261 ms: 1.05x faster                                                            |
| docutils       | 2.83 sec                                                   | 2.70 sec: 1.05x faster                                                          |
| html5lib       | 67.2 ms                                                    | 64.8 ms: 1.04x faster                                                           |
| tornado_http   | 94.6 ms                                                    | 90.2 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                      | 1.05x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 406 ms: 1.14x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 531 ms: 1.11x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 560 ms: 1.09x faster                                                            |
| async_tree_io_tg           | 936 ms                                                     | 885 ms: 1.06x faster                                                            |
| async_tree_io              | 939 ms                                                     | 907 ms: 1.03x faster                                                            |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                            |
| float          | 78.9 ms                                                    | 77.9 ms: 1.01x faster                                                           |
| nbody          | 88.3 ms                                                    | 87.3 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                      | 1.02x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 130 ms: 1.06x faster                                                            |
| regex_v8       | 25.1 ms                                                    | 24.5 ms: 1.02x faster                                                           |
| regex_effbot   | 3.67 ms                                                    | 3.60 ms: 1.02x faster                                                           |
| regex_dna      | 221 ms                                                     | 221 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                      | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.02x faster                                                            |
| xml_etree_process    | 61.2 ms                                                    | 59.8 ms: 1.02x faster                                                           |
| tomli_loads          | 2.12 sec                                                   | 2.08 sec: 1.02x faster                                                          |
| unpickle_pure_python | 218 us                                                     | 214 us: 1.02x faster                                                            |
| json_loads           | 28.9 us                                                    | 28.3 us: 1.02x faster                                                           |
| pickle_pure_python   | 305 us                                                     | 300 us: 1.02x faster                                                            |
| xml_etree_parse      | 162 ms                                                     | 159 ms: 1.02x faster                                                            |
| xml_etree_generate   | 87.4 ms                                                    | 86.4 ms: 1.01x faster                                                           |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 23.0 ms: 1.03x faster                                                           |
| django_template | 34.8 ms                                                    | 34.3 ms: 1.02x faster                                                           |
| genshi_xml      | 51.6 ms                                                    | 51.0 ms: 1.01x faster                                                           |
| mako            | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-linux-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 259 us: 1.42x faster                                                            |
| deepcopy_memo              | 39.7 us                                                    | 29.8 us: 1.33x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                    | 2.68 us: 1.25x faster                                                           |
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 406 ms: 1.14x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 393 ms: 1.13x faster                                                            |
| richards                   | 50.9 ms                                                    | 45.4 ms: 1.12x faster                                                           |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                            |
| coverage                   | 93.1 ms                                                    | 84.0 ms: 1.11x faster                                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 531 ms: 1.11x faster                                                            |
| richards_super             | 57.4 ms                                                    | 51.9 ms: 1.11x faster                                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 560 ms: 1.09x faster                                                            |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                           |
| scimark_fft                | 392 ms                                                     | 361 ms: 1.09x faster                                                            |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.08x faster                                                            |
| logging_format             | 6.47 us                                                    | 6.07 us: 1.07x faster                                                           |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.96 ms: 1.06x faster                                                           |
| bench_thread_pool          | 834 us                                                     | 786 us: 1.06x faster                                                            |
| async_tree_io_tg           | 936 ms                                                     | 885 ms: 1.06x faster                                                            |
| chaos                      | 61.3 ms                                                    | 58.1 ms: 1.06x faster                                                           |
| regex_compile              | 137 ms                                                     | 130 ms: 1.06x faster                                                            |
| logging_simple             | 5.74 us                                                    | 5.45 us: 1.05x faster                                                           |
| crypto_pyaes               | 77.5 ms                                                    | 73.5 ms: 1.05x faster                                                           |
| generators                 | 29.6 ms                                                    | 28.1 ms: 1.05x faster                                                           |
| bpe_tokeniser              | 5.02 sec                                                   | 4.78 sec: 1.05x faster                                                          |
| 2to3                       | 274 ms                                                     | 261 ms: 1.05x faster                                                            |
| tornado_http               | 94.6 ms                                                    | 90.2 ms: 1.05x faster                                                           |
| docutils                   | 2.83 sec                                                   | 2.70 sec: 1.05x faster                                                          |
| thrift                     | 823 us                                                     | 787 us: 1.05x faster                                                            |
| asyncio_tcp                | 508 ms                                                     | 486 ms: 1.05x faster                                                            |
| mdp                        | 2.79 sec                                                   | 2.67 sec: 1.05x faster                                                          |
| sqlglot_optimize           | 55.5 ms                                                    | 53.2 ms: 1.04x faster                                                           |
| raytrace                   | 267 ms                                                     | 256 ms: 1.04x faster                                                            |
| pyflate                    | 484 ms                                                     | 464 ms: 1.04x faster                                                            |
| sympy_str                  | 282 ms                                                     | 271 ms: 1.04x faster                                                            |
| go                         | 145 ms                                                     | 139 ms: 1.04x faster                                                            |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                                           |
| sympy_integrate            | 20.5 ms                                                    | 19.7 ms: 1.04x faster                                                           |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                           |
| scimark_monte_carlo        | 69.2 ms                                                    | 66.6 ms: 1.04x faster                                                           |
| sqlglot_transpile          | 1.63 ms                                                    | 1.58 ms: 1.04x faster                                                           |
| html5lib                   | 67.2 ms                                                    | 64.8 ms: 1.04x faster                                                           |
| async_tree_io              | 939 ms                                                     | 907 ms: 1.03x faster                                                            |
| deltablue                  | 3.25 ms                                                    | 3.14 ms: 1.03x faster                                                           |
| sympy_expand               | 473 ms                                                     | 457 ms: 1.03x faster                                                            |
| telco                      | 8.41 ms                                                    | 8.14 ms: 1.03x faster                                                           |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                                            |
| nqueens                    | 81.4 ms                                                    | 78.8 ms: 1.03x faster                                                           |
| gc_traversal               | 3.98 ms                                                    | 3.85 ms: 1.03x faster                                                           |
| hexiom                     | 6.30 ms                                                    | 6.10 ms: 1.03x faster                                                           |
| sympy_sum                  | 156 ms                                                     | 151 ms: 1.03x faster                                                            |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                            |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                          |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                                           |
| genshi_text                | 23.7 ms                                                    | 23.0 ms: 1.03x faster                                                           |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                           |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                            |
| pycparser                  | 1.16 sec                                                   | 1.13 sec: 1.03x faster                                                          |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.02x faster                                                            |
| xml_etree_process          | 61.2 ms                                                    | 59.8 ms: 1.02x faster                                                           |
| spectral_norm              | 116 ms                                                     | 114 ms: 1.02x faster                                                            |
| pprint_pformat             | 1.56 sec                                                   | 1.52 sec: 1.02x faster                                                          |
| regex_v8                   | 25.1 ms                                                    | 24.5 ms: 1.02x faster                                                           |
| tomli_loads                | 2.12 sec                                                   | 2.08 sec: 1.02x faster                                                          |
| unpickle_pure_python       | 218 us                                                     | 214 us: 1.02x faster                                                            |
| regex_effbot               | 3.67 ms                                                    | 3.60 ms: 1.02x faster                                                           |
| json_loads                 | 28.9 us                                                    | 28.3 us: 1.02x faster                                                           |
| async_generators           | 442 ms                                                     | 434 ms: 1.02x faster                                                            |
| pickle_pure_python         | 305 us                                                     | 300 us: 1.02x faster                                                            |
| xml_etree_parse            | 162 ms                                                     | 159 ms: 1.02x faster                                                            |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                            |
| pprint_safe_repr           | 758 ms                                                     | 746 ms: 1.02x faster                                                            |
| django_template            | 34.8 ms                                                    | 34.3 ms: 1.02x faster                                                           |
| typing_runtime_protocols   | 165 us                                                     | 162 us: 1.02x faster                                                            |
| fannkuch                   | 402 ms                                                     | 396 ms: 1.01x faster                                                            |
| xml_etree_generate         | 87.4 ms                                                    | 86.4 ms: 1.01x faster                                                           |
| float                      | 78.9 ms                                                    | 77.9 ms: 1.01x faster                                                           |
| genshi_xml                 | 51.6 ms                                                    | 51.0 ms: 1.01x faster                                                           |
| nbody                      | 88.3 ms                                                    | 87.3 ms: 1.01x faster                                                           |
| scimark_sor                | 127 ms                                                     | 126 ms: 1.01x faster                                                            |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                           |
| python_startup_no_site     | 7.11 ms                                                    | 7.05 ms: 1.01x faster                                                           |
| regex_dna                  | 221 ms                                                     | 221 ms: 1.00x faster                                                            |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.00x slower                                                           |
| mako                       | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                                           |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                    |

Benchmark hidden because not significant (4): logging_silent, pylint, json, coroutines
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.01x