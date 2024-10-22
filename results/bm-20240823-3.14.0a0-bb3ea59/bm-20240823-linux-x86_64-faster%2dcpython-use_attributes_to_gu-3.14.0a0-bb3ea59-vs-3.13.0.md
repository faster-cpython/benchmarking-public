# Results vs. 3.13.0

- fork: faster-cpython
- ref: use_attributes_to_gu
- machine: linux-x86_64
- commit hash: bb3ea59
- commit date: 2024-08-23
- overall geometric mean: 1.02x faster
- HPT reliability: 97.61%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 256 ms: 1.04x faster                                                            |
| docutils       | 2.58 sec                                               | 2.71 sec: 1.05x slower                                                          |
| html5lib       | 64.5 ms                                                | 66.2 ms: 1.03x slower                                                           |
| tornado_http   | 91.5 ms                                                | 89.6 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 402 ms: 1.15x faster                                                            |
| async_tree_memoization    | 442 ms                                                 | 391 ms: 1.13x faster                                                            |
| async_tree_none           | 354 ms                                                 | 324 ms: 1.09x faster                                                            |
| async_tree_none_tg        | 320 ms                                                 | 308 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 555 ms: 1.03x faster                                                            |
| asyncio_tcp               | 488 ms                                                 | 477 ms: 1.02x faster                                                            |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                          |
| async_generators          | 433 ms                                                 | 437 ms: 1.01x slower                                                            |
| coroutines                | 22.5 ms                                                | 23.4 ms: 1.04x slower                                                           |
| async_tree_io_tg          | 825 ms                                                 | 901 ms: 1.09x slower                                                            |
| async_tree_io             | 843 ms                                                 | 932 ms: 1.11x slower                                                            |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                            |
| nbody          | 85.7 ms                                                | 86.5 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.68 ms: 1.06x faster                                                           |
| regex_compile  | 131 ms                                                 | 128 ms: 1.02x faster                                                            |
| regex_dna      | 220 ms                                                 | 223 ms: 1.02x slower                                                            |
| regex_v8       | 25.3 ms                                                | 26.1 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 58.7 ms: 1.03x faster                                                           |
| xml_etree_generate   | 87.0 ms                                                | 84.9 ms: 1.02x faster                                                           |
| tomli_loads          | 2.11 sec                                               | 2.10 sec: 1.01x faster                                                          |
| pickle_pure_python   | 300 us                                                 | 299 us: 1.00x faster                                                            |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                            |
| xml_etree_iterparse  | 102 ms                                                 | 106 ms: 1.04x slower                                                            |
| json_loads           | 27.0 us                                                | 28.7 us: 1.06x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                           |
| python_startup_no_site | 6.99 ms                                                | 7.10 ms: 1.02x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 21.9 ms: 1.04x faster                                                           |
| django_template | 34.4 ms                                                | 33.5 ms: 1.03x faster                                                           |
| genshi_xml      | 50.3 ms                                                | 49.2 ms: 1.02x faster                                                           |
| mako            | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                  | 352 us                                                 | 260 us: 1.35x faster                                                            |
| deepcopy_memo             | 38.0 us                                                | 29.8 us: 1.27x faster                                                           |
| go                        | 142 ms                                                 | 118 ms: 1.20x faster                                                            |
| deepcopy_reduce           | 3.17 us                                                | 2.67 us: 1.19x faster                                                           |
| async_tree_memoization_tg | 465 ms                                                 | 402 ms: 1.15x faster                                                            |
| async_tree_memoization    | 442 ms                                                 | 391 ms: 1.13x faster                                                            |
| async_tree_none           | 354 ms                                                 | 324 ms: 1.09x faster                                                            |
| mdp                       | 2.74 sec                                               | 2.52 sec: 1.09x faster                                                          |
| pathlib                   | 17.1 ms                                                | 15.9 ms: 1.08x faster                                                           |
| richards                  | 48.1 ms                                                | 45.4 ms: 1.06x faster                                                           |
| richards_super            | 54.4 ms                                                | 51.3 ms: 1.06x faster                                                           |
| regex_effbot              | 3.88 ms                                                | 3.68 ms: 1.06x faster                                                           |
| genshi_text               | 22.9 ms                                                | 21.9 ms: 1.04x faster                                                           |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.82 ms: 1.04x faster                                                           |
| thrift                    | 796 us                                                 | 765 us: 1.04x faster                                                            |
| bench_thread_pool         | 815 us                                                 | 785 us: 1.04x faster                                                            |
| generators                | 28.8 ms                                                | 27.8 ms: 1.04x faster                                                           |
| async_tree_none_tg        | 320 ms                                                 | 308 ms: 1.04x faster                                                            |
| 2to3                      | 265 ms                                                 | 256 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 555 ms: 1.03x faster                                                            |
| spectral_norm             | 115 ms                                                 | 111 ms: 1.03x faster                                                            |
| crypto_pyaes              | 73.0 ms                                                | 70.7 ms: 1.03x faster                                                           |
| xml_etree_process         | 60.4 ms                                                | 58.7 ms: 1.03x faster                                                           |
| django_template           | 34.4 ms                                                | 33.5 ms: 1.03x faster                                                           |
| logging_simple            | 5.66 us                                                | 5.52 us: 1.03x faster                                                           |
| logging_format            | 6.25 us                                                | 6.10 us: 1.03x faster                                                           |
| pprint_safe_repr          | 744 ms                                                 | 726 ms: 1.02x faster                                                            |
| xml_etree_generate        | 87.0 ms                                                | 84.9 ms: 1.02x faster                                                           |
| asyncio_tcp               | 488 ms                                                 | 477 ms: 1.02x faster                                                            |
| pprint_pformat            | 1.51 sec                                               | 1.48 sec: 1.02x faster                                                          |
| genshi_xml                | 50.3 ms                                                | 49.2 ms: 1.02x faster                                                           |
| sympy_str                 | 274 ms                                                 | 267 ms: 1.02x faster                                                            |
| regex_compile             | 131 ms                                                 | 128 ms: 1.02x faster                                                            |
| gc_traversal              | 3.81 ms                                                | 3.72 ms: 1.02x faster                                                           |
| telco                     | 8.45 ms                                                | 8.27 ms: 1.02x faster                                                           |
| tornado_http              | 91.5 ms                                                | 89.6 ms: 1.02x faster                                                           |
| sympy_sum                 | 150 ms                                                 | 147 ms: 1.02x faster                                                            |
| scimark_fft               | 369 ms                                                 | 361 ms: 1.02x faster                                                            |
| sympy_expand              | 462 ms                                                 | 453 ms: 1.02x faster                                                            |
| sympy_integrate           | 19.9 ms                                                | 19.5 ms: 1.02x faster                                                           |
| scimark_lu                | 115 ms                                                 | 113 ms: 1.01x faster                                                            |
| pycparser                 | 1.19 sec                                               | 1.18 sec: 1.01x faster                                                          |
| sqlglot_optimize          | 53.9 ms                                                | 53.4 ms: 1.01x faster                                                           |
| tomli_loads               | 2.11 sec                                               | 2.10 sec: 1.01x faster                                                          |
| pickle_pure_python        | 300 us                                                 | 299 us: 1.00x faster                                                            |
| raytrace                  | 262 ms                                                 | 261 ms: 1.00x faster                                                            |
| meteor_contest            | 108 ms                                                 | 107 ms: 1.00x faster                                                            |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                          |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                           |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x slower                                                            |
| chaos                     | 58.4 ms                                                | 58.6 ms: 1.00x slower                                                           |
| comprehensions            | 16.4 us                                                | 16.5 us: 1.01x slower                                                           |
| unpickle_pure_python      | 213 us                                                 | 215 us: 1.01x slower                                                            |
| nbody                     | 85.7 ms                                                | 86.5 ms: 1.01x slower                                                           |
| async_generators          | 433 ms                                                 | 437 ms: 1.01x slower                                                            |
| deltablue                 | 3.15 ms                                                | 3.19 ms: 1.01x slower                                                           |
| python_startup_no_site    | 6.99 ms                                                | 7.10 ms: 1.02x slower                                                           |
| regex_dna                 | 220 ms                                                 | 223 ms: 1.02x slower                                                            |
| sqlglot_parse             | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                           |
| scimark_monte_carlo       | 66.3 ms                                                | 67.5 ms: 1.02x slower                                                           |
| mako                      | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                           |
| json                      | 5.20 ms                                                | 5.30 ms: 1.02x slower                                                           |
| pyflate                   | 460 ms                                                 | 471 ms: 1.02x slower                                                            |
| coverage                  | 83.7 ms                                                | 85.8 ms: 1.03x slower                                                           |
| html5lib                  | 64.5 ms                                                | 66.2 ms: 1.03x slower                                                           |
| bpe_tokeniser             | 4.69 sec                                               | 4.82 sec: 1.03x slower                                                          |
| scimark_sor               | 122 ms                                                 | 126 ms: 1.03x slower                                                            |
| regex_v8                  | 25.3 ms                                                | 26.1 ms: 1.03x slower                                                           |
| xml_etree_iterparse       | 102 ms                                                 | 106 ms: 1.04x slower                                                            |
| coroutines                | 22.5 ms                                                | 23.4 ms: 1.04x slower                                                           |
| docutils                  | 2.58 sec                                               | 2.71 sec: 1.05x slower                                                          |
| fannkuch                  | 381 ms                                                 | 402 ms: 1.06x slower                                                            |
| json_loads                | 27.0 us                                                | 28.7 us: 1.06x slower                                                           |
| async_tree_io_tg          | 825 ms                                                 | 901 ms: 1.09x slower                                                            |
| create_gc_cycles          | 1.61 ms                                                | 1.77 ms: 1.10x slower                                                           |
| async_tree_io             | 843 ms                                                 | 932 ms: 1.11x slower                                                            |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (13): async_tree_cpu_io_mixed_tg, logging_silent, nqueens, sqlglot_normalize, float, typing_runtime_protocols, sqlglot_transpile, bench_mp_pool, hexiom, xml_etree_parse, asyncio_websockets, json_dumps, pylint
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 97.61% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x