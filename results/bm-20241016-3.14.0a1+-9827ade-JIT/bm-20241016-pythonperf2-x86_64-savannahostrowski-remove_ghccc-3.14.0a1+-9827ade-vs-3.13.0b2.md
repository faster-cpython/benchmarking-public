# Results vs. 3.13.0b2

- fork: savannahostrowski
- ref: remove_ghccc
- machine: linux-x86_64
- commit hash: 9827ade
- commit date: 2024-10-16
- overall geometric mean: 1.07x slower
- HPT reliability: 63.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 314 ms: 1.08x slower                                                            |
| docutils       | 2.98 sec                                                         | 3.19 sec: 1.07x slower                                                          |
| html5lib       | 74.7 ms                                                          | 70.9 ms: 1.05x faster                                                           |
| tornado_http   | 119 ms                                                           | 121 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                            | 1.03x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|---------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 421 ms                                                           | 377 ms: 1.12x faster                                                            |
| async_tree_memoization    | 460 ms                                                           | 413 ms: 1.11x faster                                                            |
| async_tree_none           | 365 ms                                                           | 335 ms: 1.09x faster                                                            |
| async_tree_none_tg        | 340 ms                                                           | 323 ms: 1.05x faster                                                            |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 582 ms: 1.04x faster                                                            |
| async_tree_io_tg          | 900 ms                                                           | 869 ms: 1.04x faster                                                            |
| async_tree_io             | 873 ms                                                           | 854 ms: 1.02x faster                                                            |
| Geometric mean            | (ref)                                                            | 1.06x faster                                                                    |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 83.5 ms: 1.05x faster                                                           |
| float          | 80.2 ms                                                          | 79.4 ms: 1.01x faster                                                           |
| pidigits       | 254 ms                                                           | 252 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 232 ms: 1.08x faster                                                            |
| regex_v8       | 26.0 ms                                                          | 25.0 ms: 1.04x faster                                                           |
| regex_effbot   | 3.40 ms                                                          | 3.47 ms: 1.02x slower                                                           |
| regex_compile  | 144 ms                                                           | 148 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.11 sec: 1.14x faster                                                          |
| xml_etree_generate   | 85.7 ms                                                          | 82.0 ms: 1.05x faster                                                           |
| unpickle             | 15.7 us                                                          | 15.0 us: 1.04x faster                                                           |
| xml_etree_process    | 59.7 ms                                                          | 57.8 ms: 1.03x faster                                                           |
| unpickle_pure_python | 224 us                                                           | 219 us: 1.02x faster                                                            |
| json_loads           | 25.0 us                                                          | 24.5 us: 1.02x faster                                                           |
| xml_etree_iterparse  | 103 ms                                                           | 100 ms: 1.02x faster                                                            |
| xml_etree_parse      | 144 ms                                                           | 143 ms: 1.01x faster                                                            |
| unpickle_list        | 4.70 us                                                          | 4.76 us: 1.01x slower                                                           |
| pickle_dict          | 32.8 us                                                          | 33.3 us: 1.01x slower                                                           |
| pickle               | 10.6 us                                                          | 10.8 us: 1.02x slower                                                           |
| json_dumps           | 10.8 ms                                                          | 11.0 ms: 1.02x slower                                                           |
| pickle_list          | 4.44 us                                                          | 4.64 us: 1.05x slower                                                           |
| pickle_pure_python   | 307 us                                                           | 335 us: 1.09x slower                                                            |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.85 ms                                                          | 8.99 ms: 1.02x slower                                                           |
| python_startup         | 13.2 ms                                                          | 14.9 ms: 1.13x slower                                                           |
| Geometric mean         | (ref)                                                            | 1.07x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.44 ms: 1.10x faster                                                           |
| genshi_xml      | 58.1 ms                                                          | 61.8 ms: 1.07x slower                                                           |
| genshi_text     | 25.9 ms                                                          | 27.9 ms: 1.08x slower                                                           |
| django_template | 39.0 ms                                                          | 43.3 ms: 1.11x slower                                                           |
| Geometric mean  | (ref)                                                            | 1.04x slower                                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|---------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo             | 37.3 us                                                          | 29.6 us: 1.26x faster                                                           |
| deepcopy                  | 377 us                                                           | 313 us: 1.21x faster                                                            |
| richards_super            | 61.2 ms                                                          | 51.4 ms: 1.19x faster                                                           |
| richards                  | 53.4 ms                                                          | 45.5 ms: 1.18x faster                                                           |
| tomli_loads               | 2.40 sec                                                         | 2.11 sec: 1.14x faster                                                          |
| scimark_sor               | 119 ms                                                           | 105 ms: 1.13x faster                                                            |
| deepcopy_reduce           | 3.39 us                                                          | 3.02 us: 1.12x faster                                                           |
| async_tree_memoization_tg | 421 ms                                                           | 377 ms: 1.12x faster                                                            |
| async_tree_memoization    | 460 ms                                                           | 413 ms: 1.11x faster                                                            |
| mako                      | 10.4 ms                                                          | 9.44 ms: 1.10x faster                                                           |
| async_tree_none           | 365 ms                                                           | 335 ms: 1.09x faster                                                            |
| scimark_fft               | 312 ms                                                           | 288 ms: 1.09x faster                                                            |
| pathlib                   | 17.1 ms                                                          | 15.8 ms: 1.08x faster                                                           |
| telco                     | 8.40 ms                                                          | 7.78 ms: 1.08x faster                                                           |
| bpe_tokeniser             | 5.14 sec                                                         | 4.77 sec: 1.08x faster                                                          |
| regex_dna                 | 249 ms                                                           | 232 ms: 1.08x faster                                                            |
| go                        | 165 ms                                                           | 154 ms: 1.07x faster                                                            |
| pyflate                   | 482 ms                                                           | 452 ms: 1.07x faster                                                            |
| async_tree_none_tg        | 340 ms                                                           | 323 ms: 1.05x faster                                                            |
| html5lib                  | 74.7 ms                                                          | 70.9 ms: 1.05x faster                                                           |
| spectral_norm             | 97.3 ms                                                          | 92.5 ms: 1.05x faster                                                           |
| nbody                     | 87.8 ms                                                          | 83.5 ms: 1.05x faster                                                           |
| coverage                  | 83.5 ms                                                          | 79.8 ms: 1.05x faster                                                           |
| logging_silent            | 96.3 ns                                                          | 92.1 ns: 1.05x faster                                                           |
| xml_etree_generate        | 85.7 ms                                                          | 82.0 ms: 1.05x faster                                                           |
| unpickle                  | 15.7 us                                                          | 15.0 us: 1.04x faster                                                           |
| regex_v8                  | 26.0 ms                                                          | 25.0 ms: 1.04x faster                                                           |
| dulwich_log               | 67.3 ms                                                          | 64.6 ms: 1.04x faster                                                           |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 582 ms: 1.04x faster                                                            |
| json                      | 5.35 ms                                                          | 5.16 ms: 1.04x faster                                                           |
| async_tree_io_tg          | 900 ms                                                           | 869 ms: 1.04x faster                                                            |
| crypto_pyaes              | 73.6 ms                                                          | 71.1 ms: 1.04x faster                                                           |
| xml_etree_process         | 59.7 ms                                                          | 57.8 ms: 1.03x faster                                                           |
| sqlite_synth              | 2.80 us                                                          | 2.71 us: 1.03x faster                                                           |
| asyncio_websockets        | 395 ms                                                           | 384 ms: 1.03x faster                                                            |
| pprint_safe_repr          | 818 ms                                                           | 796 ms: 1.03x faster                                                            |
| unpickle_pure_python      | 224 us                                                           | 219 us: 1.02x faster                                                            |
| deltablue                 | 3.37 ms                                                          | 3.30 ms: 1.02x faster                                                           |
| async_tree_io             | 873 ms                                                           | 854 ms: 1.02x faster                                                            |
| json_loads                | 25.0 us                                                          | 24.5 us: 1.02x faster                                                           |
| xml_etree_iterparse       | 103 ms                                                           | 100 ms: 1.02x faster                                                            |
| float                     | 80.2 ms                                                          | 79.4 ms: 1.01x faster                                                           |
| pidigits                  | 254 ms                                                           | 252 ms: 1.01x faster                                                            |
| coroutines                | 22.0 ms                                                          | 21.8 ms: 1.01x faster                                                           |
| xml_etree_parse           | 144 ms                                                           | 143 ms: 1.01x faster                                                            |
| asyncio_tcp_ssl           | 1.58 sec                                                         | 1.58 sec: 1.00x slower                                                          |
| unpickle_list             | 4.70 us                                                          | 4.76 us: 1.01x slower                                                           |
| pickle_dict               | 32.8 us                                                          | 33.3 us: 1.01x slower                                                           |
| logging_format            | 7.11 us                                                          | 7.22 us: 1.01x slower                                                           |
| python_startup_no_site    | 8.85 ms                                                          | 8.99 ms: 1.02x slower                                                           |
| thrift                    | 880 us                                                           | 894 us: 1.02x slower                                                            |
| tornado_http              | 119 ms                                                           | 121 ms: 1.02x slower                                                            |
| pickle                    | 10.6 us                                                          | 10.8 us: 1.02x slower                                                           |
| regex_effbot              | 3.40 ms                                                          | 3.47 ms: 1.02x slower                                                           |
| json_dumps                | 10.8 ms                                                          | 11.0 ms: 1.02x slower                                                           |
| scimark_sparse_mat_mult   | 4.28 ms                                                          | 4.38 ms: 1.02x slower                                                           |
| regex_compile             | 144 ms                                                           | 148 ms: 1.03x slower                                                            |
| logging_simple            | 6.40 us                                                          | 6.59 us: 1.03x slower                                                           |
| meteor_contest            | 128 ms                                                           | 133 ms: 1.04x slower                                                            |
| pickle_list               | 4.44 us                                                          | 4.64 us: 1.05x slower                                                           |
| fannkuch                  | 353 ms                                                           | 371 ms: 1.05x slower                                                            |
| typing_runtime_protocols  | 171 us                                                           | 180 us: 1.05x slower                                                            |
| bench_thread_pool         | 908 us                                                           | 958 us: 1.05x slower                                                            |
| mdp                       | 2.46 sec                                                         | 2.60 sec: 1.06x slower                                                          |
| pycparser                 | 1.22 sec                                                         | 1.30 sec: 1.06x slower                                                          |
| async_generators          | 363 ms                                                           | 386 ms: 1.06x slower                                                            |
| genshi_xml                | 58.1 ms                                                          | 61.8 ms: 1.07x slower                                                           |
| sympy_expand              | 501 ms                                                           | 534 ms: 1.07x slower                                                            |
| docutils                  | 2.98 sec                                                         | 3.19 sec: 1.07x slower                                                          |
| scimark_monte_carlo       | 65.5 ms                                                          | 70.2 ms: 1.07x slower                                                           |
| genshi_text               | 25.9 ms                                                          | 27.9 ms: 1.08x slower                                                           |
| 2to3                      | 291 ms                                                           | 314 ms: 1.08x slower                                                            |
| sqlglot_parse             | 1.39 ms                                                          | 1.51 ms: 1.08x slower                                                           |
| sympy_str                 | 295 ms                                                           | 319 ms: 1.08x slower                                                            |
| pickle_pure_python        | 307 us                                                           | 335 us: 1.09x slower                                                            |
| sqlglot_normalize         | 120 ms                                                           | 132 ms: 1.09x slower                                                            |
| comprehensions            | 17.0 us                                                          | 18.6 us: 1.10x slower                                                           |
| django_template           | 39.0 ms                                                          | 43.3 ms: 1.11x slower                                                           |
| hexiom                    | 6.35 ms                                                          | 7.06 ms: 1.11x slower                                                           |
| chaos                     | 59.6 ms                                                          | 66.4 ms: 1.11x slower                                                           |
| sympy_sum                 | 155 ms                                                           | 174 ms: 1.12x slower                                                            |
| sqlglot_transpile         | 1.76 ms                                                          | 1.99 ms: 1.13x slower                                                           |
| python_startup            | 13.2 ms                                                          | 14.9 ms: 1.13x slower                                                           |
| generators                | 33.5 ms                                                          | 38.1 ms: 1.14x slower                                                           |
| nqueens                   | 88.4 ms                                                          | 102 ms: 1.15x slower                                                            |
| sqlglot_optimize          | 59.5 ms                                                          | 69.5 ms: 1.17x slower                                                           |
| gc_traversal              | 4.69 ms                                                          | 5.48 ms: 1.17x slower                                                           |
| sympy_integrate           | 23.2 ms                                                          | 27.2 ms: 1.17x slower                                                           |
| raytrace                  | 260 ms                                                           | 324 ms: 1.25x slower                                                            |
| pylint                    | 339 ms                                                           | 424 ms: 1.25x slower                                                            |
| create_gc_cycles          | 2.00 ms                                                          | 2.90 ms: 1.45x slower                                                           |
| bench_mp_pool             | 4.91 ms                                                          | 1.98 sec: 403.30x slower                                                        |
| Geometric mean            | (ref)                                                            | 1.07x slower                                                                    |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, asyncio_tcp, scimark_lu, pprint_pformat
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241016-3.14.0a1+-9827ade-JIT/bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 63.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.19x