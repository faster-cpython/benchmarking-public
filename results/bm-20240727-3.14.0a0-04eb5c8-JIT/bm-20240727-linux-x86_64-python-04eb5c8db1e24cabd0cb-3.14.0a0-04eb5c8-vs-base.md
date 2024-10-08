# Results vs. base

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.00x faster
- HPT reliability: 82.65%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 264 ms                                                                                                          | 271 ms: 1.03x slower                                                                                                |
| docutils       | 2.74 sec                                                                                                        | 2.91 sec: 1.06x slower                                                                                              |
| html5lib       | 65.6 ms                                                                                                         | 65.0 ms: 1.01x faster                                                                                               |
| tornado_http   | 90.9 ms                                                                                                         | 92.8 ms: 1.02x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.03x slower                                                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| asyncio_websockets     | 560 ms                                                                                                          | 557 ms: 1.00x faster                                                                                                |
| async_tree_none        | 323 ms                                                                                                          | 326 ms: 1.01x slower                                                                                                |
| asyncio_tcp_ssl        | 1.79 sec                                                                                                        | 1.81 sec: 1.01x slower                                                                                              |
| asyncio_tcp            | 487 ms                                                                                                          | 504 ms: 1.03x slower                                                                                                |
| async_tree_memoization | 409 ms                                                                                                          | 427 ms: 1.04x slower                                                                                                |
| async_generators       | 437 ms                                                                                                          | 460 ms: 1.05x slower                                                                                                |
| Geometric mean         | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmark hidden because not significant (7): async_tree_io_tg, coroutines, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| float          | 78.1 ms                                                                                                         | 70.6 ms: 1.11x faster                                                                                               |
| nbody          | 89.0 ms                                                                                                         | 81.5 ms: 1.09x faster                                                                                               |
| pidigits       | 187 ms                                                                                                          | 186 ms: 1.01x faster                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.07x faster                                                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 226 ms                                                                                                          | 220 ms: 1.03x faster                                                                                                |
| regex_compile  | 131 ms                                                                                                          | 134 ms: 1.02x slower                                                                                                |
| regex_effbot   | 3.67 ms                                                                                                         | 3.76 ms: 1.03x slower                                                                                               |
| regex_v8       | 24.6 ms                                                                                                         | 25.5 ms: 1.03x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                                                                         | 80.7 ms: 1.08x faster                                                                                               |
| xml_etree_process    | 60.2 ms                                                                                                         | 56.5 ms: 1.07x faster                                                                                               |
| xml_etree_parse      | 154 ms                                                                                                          | 146 ms: 1.06x faster                                                                                                |
| xml_etree_iterparse  | 105 ms                                                                                                          | 99.1 ms: 1.06x faster                                                                                               |
| tomli_loads          | 2.03 sec                                                                                                        | 1.93 sec: 1.05x faster                                                                                              |
| pickle_pure_python   | 306 us                                                                                                          | 299 us: 1.02x faster                                                                                                |
| json_loads           | 27.6 us                                                                                                         | 27.9 us: 1.01x slower                                                                                               |
| unpickle_pure_python | 212 us                                                                                                          | 214 us: 1.01x slower                                                                                                |
| Geometric mean       | (ref)                                                                                                           | 1.03x faster                                                                                                        |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                                                                         | 10.6 ms: 1.00x slower                                                                                               |
| python_startup_no_site | 7.10 ms                                                                                                         | 7.16 ms: 1.01x slower                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.00x slower                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako            | 11.0 ms                                                                                                         | 9.75 ms: 1.13x faster                                                                                               |
| genshi_text     | 23.7 ms                                                                                                         | 24.8 ms: 1.05x slower                                                                                               |
| django_template | 34.5 ms                                                                                                         | 36.3 ms: 1.05x slower                                                                                               |
| genshi_xml      | 52.4 ms                                                                                                         | 58.6 ms: 1.12x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.02x slower                                                                                                        |

All benchmarks:
===============

| Benchmark                | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|--------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| scimark_monte_carlo      | 68.6 ms                                                                                                         | 60.0 ms: 1.14x faster                                                                                               |
| spectral_norm            | 113 ms                                                                                                          | 100 ms: 1.13x faster                                                                                                |
| scimark_fft              | 351 ms                                                                                                          | 310 ms: 1.13x faster                                                                                                |
| richards                 | 45.9 ms                                                                                                         | 40.6 ms: 1.13x faster                                                                                               |
| mako                     | 11.0 ms                                                                                                         | 9.75 ms: 1.13x faster                                                                                               |
| richards_super           | 51.8 ms                                                                                                         | 46.3 ms: 1.12x faster                                                                                               |
| crypto_pyaes             | 73.6 ms                                                                                                         | 66.4 ms: 1.11x faster                                                                                               |
| float                    | 78.1 ms                                                                                                         | 70.6 ms: 1.11x faster                                                                                               |
| fannkuch                 | 405 ms                                                                                                          | 366 ms: 1.11x faster                                                                                                |
| pyflate                  | 470 ms                                                                                                          | 430 ms: 1.09x faster                                                                                                |
| nbody                    | 89.0 ms                                                                                                         | 81.5 ms: 1.09x faster                                                                                               |
| bpe_tokeniser            | 4.86 sec                                                                                                        | 4.50 sec: 1.08x faster                                                                                              |
| xml_etree_generate       | 87.0 ms                                                                                                         | 80.7 ms: 1.08x faster                                                                                               |
| scimark_sparse_mat_mult  | 4.62 ms                                                                                                         | 4.30 ms: 1.07x faster                                                                                               |
| xml_etree_process        | 60.2 ms                                                                                                         | 56.5 ms: 1.07x faster                                                                                               |
| xml_etree_parse          | 154 ms                                                                                                          | 146 ms: 1.06x faster                                                                                                |
| xml_etree_iterparse      | 105 ms                                                                                                          | 99.1 ms: 1.06x faster                                                                                               |
| pprint_pformat           | 1.54 sec                                                                                                        | 1.46 sec: 1.05x faster                                                                                              |
| tomli_loads              | 2.03 sec                                                                                                        | 1.93 sec: 1.05x faster                                                                                              |
| pprint_safe_repr         | 748 ms                                                                                                          | 712 ms: 1.05x faster                                                                                                |
| chaos                    | 59.3 ms                                                                                                         | 57.5 ms: 1.03x faster                                                                                               |
| regex_dna                | 226 ms                                                                                                          | 220 ms: 1.03x faster                                                                                                |
| pickle_pure_python       | 306 us                                                                                                          | 299 us: 1.02x faster                                                                                                |
| telco                    | 8.10 ms                                                                                                         | 7.93 ms: 1.02x faster                                                                                               |
| deepcopy_reduce          | 2.76 us                                                                                                         | 2.70 us: 1.02x faster                                                                                               |
| meteor_contest           | 108 ms                                                                                                          | 107 ms: 1.01x faster                                                                                                |
| logging_silent           | 104 ns                                                                                                          | 103 ns: 1.01x faster                                                                                                |
| pidigits                 | 187 ms                                                                                                          | 186 ms: 1.01x faster                                                                                                |
| html5lib                 | 65.6 ms                                                                                                         | 65.0 ms: 1.01x faster                                                                                               |
| asyncio_websockets       | 560 ms                                                                                                          | 557 ms: 1.00x faster                                                                                                |
| comprehensions           | 16.6 us                                                                                                         | 16.5 us: 1.00x faster                                                                                               |
| python_startup           | 10.5 ms                                                                                                         | 10.6 ms: 1.00x slower                                                                                               |
| gc_traversal             | 3.75 ms                                                                                                         | 3.76 ms: 1.00x slower                                                                                               |
| mdp                      | 2.52 sec                                                                                                        | 2.54 sec: 1.00x slower                                                                                              |
| generators               | 28.5 ms                                                                                                         | 28.7 ms: 1.01x slower                                                                                               |
| python_startup_no_site   | 7.10 ms                                                                                                         | 7.16 ms: 1.01x slower                                                                                               |
| async_tree_none          | 323 ms                                                                                                          | 326 ms: 1.01x slower                                                                                                |
| json_loads               | 27.6 us                                                                                                         | 27.9 us: 1.01x slower                                                                                               |
| deepcopy                 | 267 us                                                                                                          | 269 us: 1.01x slower                                                                                                |
| unpickle_pure_python     | 212 us                                                                                                          | 214 us: 1.01x slower                                                                                                |
| sqlglot_transpile        | 1.58 ms                                                                                                         | 1.59 ms: 1.01x slower                                                                                               |
| scimark_sor              | 126 ms                                                                                                          | 127 ms: 1.01x slower                                                                                                |
| asyncio_tcp_ssl          | 1.79 sec                                                                                                        | 1.81 sec: 1.01x slower                                                                                              |
| create_gc_cycles         | 1.74 ms                                                                                                         | 1.76 ms: 1.01x slower                                                                                               |
| raytrace                 | 261 ms                                                                                                          | 265 ms: 1.01x slower                                                                                                |
| typing_runtime_protocols | 166 us                                                                                                          | 169 us: 1.02x slower                                                                                                |
| logging_simple           | 5.49 us                                                                                                         | 5.59 us: 1.02x slower                                                                                               |
| go                       | 139 ms                                                                                                          | 142 ms: 1.02x slower                                                                                                |
| tornado_http             | 90.9 ms                                                                                                         | 92.8 ms: 1.02x slower                                                                                               |
| regex_compile            | 131 ms                                                                                                          | 134 ms: 1.02x slower                                                                                                |
| regex_effbot             | 3.67 ms                                                                                                         | 3.76 ms: 1.03x slower                                                                                               |
| 2to3                     | 264 ms                                                                                                          | 271 ms: 1.03x slower                                                                                                |
| pycparser                | 1.13 sec                                                                                                        | 1.16 sec: 1.03x slower                                                                                              |
| dask                     | 355 ms                                                                                                          | 365 ms: 1.03x slower                                                                                                |
| thrift                   | 777 us                                                                                                          | 801 us: 1.03x slower                                                                                                |
| asyncio_tcp              | 487 ms                                                                                                          | 504 ms: 1.03x slower                                                                                                |
| regex_v8                 | 24.6 ms                                                                                                         | 25.5 ms: 1.03x slower                                                                                               |
| pathlib                  | 15.7 ms                                                                                                         | 16.3 ms: 1.03x slower                                                                                               |
| async_tree_memoization   | 409 ms                                                                                                          | 427 ms: 1.04x slower                                                                                                |
| genshi_text              | 23.7 ms                                                                                                         | 24.8 ms: 1.05x slower                                                                                               |
| bench_thread_pool        | 789 us                                                                                                          | 824 us: 1.05x slower                                                                                                |
| async_generators         | 437 ms                                                                                                          | 460 ms: 1.05x slower                                                                                                |
| hexiom                   | 6.22 ms                                                                                                         | 6.54 ms: 1.05x slower                                                                                               |
| django_template          | 34.5 ms                                                                                                         | 36.3 ms: 1.05x slower                                                                                               |
| sqlglot_optimize         | 53.2 ms                                                                                                         | 56.4 ms: 1.06x slower                                                                                               |
| coverage                 | 85.4 ms                                                                                                         | 90.5 ms: 1.06x slower                                                                                               |
| docutils                 | 2.74 sec                                                                                                        | 2.91 sec: 1.06x slower                                                                                              |
| sqlglot_normalize        | 106 ms                                                                                                          | 114 ms: 1.07x slower                                                                                                |
| deltablue                | 3.24 ms                                                                                                         | 3.46 ms: 1.07x slower                                                                                               |
| nqueens                  | 79.8 ms                                                                                                         | 85.4 ms: 1.07x slower                                                                                               |
| sympy_str                | 274 ms                                                                                                          | 297 ms: 1.08x slower                                                                                                |
| sympy_expand             | 464 ms                                                                                                          | 502 ms: 1.08x slower                                                                                                |
| pylint                   | 318 ms                                                                                                          | 351 ms: 1.10x slower                                                                                                |
| scimark_lu               | 113 ms                                                                                                          | 125 ms: 1.11x slower                                                                                                |
| sympy_sum                | 152 ms                                                                                                          | 170 ms: 1.12x slower                                                                                                |
| genshi_xml               | 52.4 ms                                                                                                         | 58.6 ms: 1.12x slower                                                                                               |
| sympy_integrate          | 19.8 ms                                                                                                         | 22.2 ms: 1.12x slower                                                                                               |
| Geometric mean           | (ref)                                                                                                           | 1.00x faster                                                                                                        |

Benchmark hidden because not significant (13): deepcopy_memo, json, logging_format, json_dumps, async_tree_io_tg, coroutines, async_tree_memoization_tg, bench_mp_pool, async_tree_cpu_io_mixed, sqlglot_parse, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io

# HPT report

- Reliability score: 82.65% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x