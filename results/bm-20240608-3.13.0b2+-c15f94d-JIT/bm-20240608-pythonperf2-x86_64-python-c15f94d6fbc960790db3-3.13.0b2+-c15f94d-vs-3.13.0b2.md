# Results vs. 3.13.0b2

- fork: python
- ref: c15f94d6fbc960790db3
- machine: linux-x86_64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.02x slower
- HPT reliability: 95.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 306 ms: 1.05x slower                                                         |
| chameleon      | 7.40 ms                                                          | 7.67 ms: 1.04x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.13 sec: 1.05x slower                                                       |
| html5lib       | 74.7 ms                                                          | 73.9 ms: 1.01x faster                                                        |
| tornado_http   | 119 ms                                                           | 122 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                            | 1.03x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|---------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg          | 900 ms                                                           | 843 ms: 1.07x faster                                                         |
| async_tree_memoization    | 460 ms                                                           | 447 ms: 1.03x faster                                                         |
| async_tree_none           | 365 ms                                                           | 376 ms: 1.03x slower                                                         |
| async_tree_none_tg        | 340 ms                                                           | 350 ms: 1.03x slower                                                         |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 627 ms: 1.04x slower                                                         |
| async_tree_memoization_tg | 421 ms                                                           | 438 ms: 1.04x slower                                                         |
| Geometric mean            | (ref)                                                            | 1.01x slower                                                                 |

Benchmark hidden because not significant (2): async_tree_io, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 73.3 ms: 1.09x faster                                                        |
| nbody          | 87.8 ms                                                          | 84.0 ms: 1.05x faster                                                        |
| pidigits       | 254 ms                                                           | 250 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                            | 1.05x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                          | 25.2 ms: 1.03x faster                                                        |
| regex_compile  | 144 ms                                                           | 140 ms: 1.03x faster                                                         |
| regex_dna      | 249 ms                                                           | 251 ms: 1.01x slower                                                         |
| regex_effbot   | 3.40 ms                                                          | 3.62 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                            | 1.00x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.09 sec: 1.15x faster                                                       |
| unpickle             | 15.7 us                                                          | 14.8 us: 1.06x faster                                                        |
| xml_etree_generate   | 85.7 ms                                                          | 82.9 ms: 1.03x faster                                                        |
| xml_etree_process    | 59.7 ms                                                          | 58.4 ms: 1.02x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 100 ms: 1.02x faster                                                         |
| unpickle_pure_python | 224 us                                                           | 221 us: 1.02x faster                                                         |
| json_loads           | 25.0 us                                                          | 24.7 us: 1.02x faster                                                        |
| json_dumps           | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                        |
| xml_etree_parse      | 144 ms                                                           | 143 ms: 1.00x faster                                                         |
| pickle_list          | 4.44 us                                                          | 4.54 us: 1.02x slower                                                        |
| pickle               | 10.6 us                                                          | 10.9 us: 1.02x slower                                                        |
| pickle_pure_python   | 307 us                                                           | 316 us: 1.03x slower                                                         |
| pickle_dict          | 32.8 us                                                          | 34.0 us: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.8 ms: 1.05x slower                                                        |
| python_startup_no_site | 8.85 ms                                                          | 9.44 ms: 1.07x slower                                                        |
| Geometric mean         | (ref)                                                            | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.15 ms: 1.13x faster                                                        |
| genshi_xml      | 58.1 ms                                                          | 62.4 ms: 1.07x slower                                                        |
| django_template | 39.0 ms                                                          | 41.9 ms: 1.08x slower                                                        |
| genshi_text     | 25.9 ms                                                          | 28.0 ms: 1.08x slower                                                        |
| Geometric mean  | (ref)                                                            | 1.02x slower                                                                 |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|---------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| spectral_norm             | 97.3 ms                                                          | 81.6 ms: 1.19x faster                                                        |
| richards                  | 53.4 ms                                                          | 45.4 ms: 1.18x faster                                                        |
| richards_super            | 61.2 ms                                                          | 52.4 ms: 1.17x faster                                                        |
| tomli_loads               | 2.40 sec                                                         | 2.09 sec: 1.15x faster                                                       |
| mako                      | 10.4 ms                                                          | 9.15 ms: 1.13x faster                                                        |
| float                     | 80.2 ms                                                          | 73.3 ms: 1.09x faster                                                        |
| async_tree_io_tg          | 900 ms                                                           | 843 ms: 1.07x faster                                                         |
| scimark_sparse_mat_mult   | 4.28 ms                                                          | 4.02 ms: 1.06x faster                                                        |
| scimark_fft               | 312 ms                                                           | 295 ms: 1.06x faster                                                         |
| gc_traversal              | 4.69 ms                                                          | 4.44 ms: 1.06x faster                                                        |
| unpickle                  | 15.7 us                                                          | 14.8 us: 1.06x faster                                                        |
| nbody                     | 87.8 ms                                                          | 84.0 ms: 1.05x faster                                                        |
| pyflate                   | 482 ms                                                           | 463 ms: 1.04x faster                                                         |
| coverage                  | 83.5 ms                                                          | 80.5 ms: 1.04x faster                                                        |
| crypto_pyaes              | 73.6 ms                                                          | 71.1 ms: 1.03x faster                                                        |
| xml_etree_generate        | 85.7 ms                                                          | 82.9 ms: 1.03x faster                                                        |
| create_gc_cycles          | 2.00 ms                                                          | 1.94 ms: 1.03x faster                                                        |
| regex_v8                  | 26.0 ms                                                          | 25.2 ms: 1.03x faster                                                        |
| regex_compile             | 144 ms                                                           | 140 ms: 1.03x faster                                                         |
| fannkuch                  | 353 ms                                                           | 343 ms: 1.03x faster                                                         |
| async_tree_memoization    | 460 ms                                                           | 447 ms: 1.03x faster                                                         |
| telco                     | 8.40 ms                                                          | 8.19 ms: 1.03x faster                                                        |
| xml_etree_process         | 59.7 ms                                                          | 58.4 ms: 1.02x faster                                                        |
| dulwich_log               | 67.3 ms                                                          | 65.9 ms: 1.02x faster                                                        |
| xml_etree_iterparse       | 103 ms                                                           | 100 ms: 1.02x faster                                                         |
| unpickle_pure_python      | 224 us                                                           | 221 us: 1.02x faster                                                         |
| json_loads                | 25.0 us                                                          | 24.7 us: 1.02x faster                                                        |
| asyncio_websockets        | 395 ms                                                           | 389 ms: 1.01x faster                                                         |
| pidigits                  | 254 ms                                                           | 250 ms: 1.01x faster                                                         |
| logging_format            | 7.11 us                                                          | 7.02 us: 1.01x faster                                                        |
| deepcopy_memo             | 37.3 us                                                          | 36.9 us: 1.01x faster                                                        |
| json_dumps                | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                        |
| html5lib                  | 74.7 ms                                                          | 73.9 ms: 1.01x faster                                                        |
| coroutines                | 22.0 ms                                                          | 21.8 ms: 1.01x faster                                                        |
| pprint_pformat            | 1.66 sec                                                         | 1.65 sec: 1.01x faster                                                       |
| go                        | 165 ms                                                           | 164 ms: 1.01x faster                                                         |
| json                      | 5.35 ms                                                          | 5.33 ms: 1.00x faster                                                        |
| xml_etree_parse           | 144 ms                                                           | 143 ms: 1.00x faster                                                         |
| asyncio_tcp               | 378 ms                                                           | 380 ms: 1.00x slower                                                         |
| regex_dna                 | 249 ms                                                           | 251 ms: 1.01x slower                                                         |
| pycparser                 | 1.22 sec                                                         | 1.23 sec: 1.01x slower                                                       |
| scimark_monte_carlo       | 65.5 ms                                                          | 66.3 ms: 1.01x slower                                                        |
| sqlglot_parse             | 1.39 ms                                                          | 1.42 ms: 1.02x slower                                                        |
| pickle_list               | 4.44 us                                                          | 4.54 us: 1.02x slower                                                        |
| meteor_contest            | 128 ms                                                           | 131 ms: 1.02x slower                                                         |
| pickle                    | 10.6 us                                                          | 10.9 us: 1.02x slower                                                        |
| generators                | 33.5 ms                                                          | 34.3 ms: 1.02x slower                                                        |
| tornado_http              | 119 ms                                                           | 122 ms: 1.03x slower                                                         |
| pathlib                   | 17.1 ms                                                          | 17.6 ms: 1.03x slower                                                        |
| async_tree_none           | 365 ms                                                           | 376 ms: 1.03x slower                                                         |
| pickle_pure_python        | 307 us                                                           | 316 us: 1.03x slower                                                         |
| async_tree_none_tg        | 340 ms                                                           | 350 ms: 1.03x slower                                                         |
| dask                      | 391 ms                                                           | 403 ms: 1.03x slower                                                         |
| sqlglot_transpile         | 1.76 ms                                                          | 1.82 ms: 1.03x slower                                                        |
| pickle_dict               | 32.8 us                                                          | 34.0 us: 1.04x slower                                                        |
| chameleon                 | 7.40 ms                                                          | 7.67 ms: 1.04x slower                                                        |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 627 ms: 1.04x slower                                                         |
| thrift                    | 880 us                                                           | 915 us: 1.04x slower                                                         |
| mdp                       | 2.46 sec                                                         | 2.56 sec: 1.04x slower                                                       |
| async_generators          | 363 ms                                                           | 378 ms: 1.04x slower                                                         |
| async_tree_memoization_tg | 421 ms                                                           | 438 ms: 1.04x slower                                                         |
| python_startup            | 13.2 ms                                                          | 13.8 ms: 1.05x slower                                                        |
| flaskblogging             | 4.68 ms                                                          | 4.90 ms: 1.05x slower                                                        |
| hexiom                    | 6.35 ms                                                          | 6.65 ms: 1.05x slower                                                        |
| docutils                  | 2.98 sec                                                         | 3.13 sec: 1.05x slower                                                       |
| 2to3                      | 291 ms                                                           | 306 ms: 1.05x slower                                                         |
| bench_thread_pool         | 908 us                                                           | 954 us: 1.05x slower                                                         |
| sympy_expand              | 501 ms                                                           | 529 ms: 1.06x slower                                                         |
| sympy_str                 | 295 ms                                                           | 312 ms: 1.06x slower                                                         |
| sqlglot_optimize          | 59.5 ms                                                          | 63.0 ms: 1.06x slower                                                        |
| regex_effbot              | 3.40 ms                                                          | 3.62 ms: 1.06x slower                                                        |
| comprehensions            | 17.0 us                                                          | 18.1 us: 1.07x slower                                                        |
| sqlglot_normalize         | 120 ms                                                           | 128 ms: 1.07x slower                                                         |
| python_startup_no_site    | 8.85 ms                                                          | 9.44 ms: 1.07x slower                                                        |
| typing_runtime_protocols  | 171 us                                                           | 182 us: 1.07x slower                                                         |
| genshi_xml                | 58.1 ms                                                          | 62.4 ms: 1.07x slower                                                        |
| django_template           | 39.0 ms                                                          | 41.9 ms: 1.08x slower                                                        |
| sympy_sum                 | 155 ms                                                           | 167 ms: 1.08x slower                                                         |
| genshi_text               | 25.9 ms                                                          | 28.0 ms: 1.08x slower                                                        |
| deepcopy_reduce           | 3.39 us                                                          | 3.68 us: 1.09x slower                                                        |
| aiohttp                   | 1.07 ms                                                          | 1.17 ms: 1.09x slower                                                        |
| nqueens                   | 88.4 ms                                                          | 96.9 ms: 1.10x slower                                                        |
| chaos                     | 59.6 ms                                                          | 65.6 ms: 1.10x slower                                                        |
| sympy_integrate           | 23.2 ms                                                          | 25.7 ms: 1.11x slower                                                        |
| deepcopy                  | 377 us                                                           | 418 us: 1.11x slower                                                         |
| pylint                    | 339 ms                                                           | 376 ms: 1.11x slower                                                         |
| deltablue                 | 3.37 ms                                                          | 3.74 ms: 1.11x slower                                                        |
| gunicorn                  | 1.04 ms                                                          | 1.16 ms: 1.11x slower                                                        |
| mypy2                     | 764 ms                                                           | 855 ms: 1.12x slower                                                         |
| raytrace                  | 260 ms                                                           | 298 ms: 1.14x slower                                                         |
| scimark_sor               | 119 ms                                                           | 138 ms: 1.16x slower                                                         |
| scimark_lu                | 97.5 ms                                                          | 114 ms: 1.17x slower                                                         |
| logging_silent            | 96.3 ns                                                          | 120 ns: 1.25x slower                                                         |
| Geometric mean            | (ref)                                                            | 1.02x slower                                                                 |

Benchmark hidden because not significant (8): bench_mp_pool, pprint_safe_repr, sqlite_synth, asyncio_tcp_ssl, unpickle_list, logging_simple, async_tree_io, async_tree_cpu_io_mixed_tg
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 95.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x