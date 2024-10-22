# Results vs. base

- fork: PeterYang12
- ref: accelerate_DJBX33A
- machine: linux-x86_64
- commit hash: bf9cfa8
- commit date: 2024-08-24
- overall geometric mean: 1.00x faster
- HPT reliability: 68.16%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240825-pythonperf2-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 284 ms                                                                      | 282 ms: 1.01x faster                                                           |
| html5lib       | 72.8 ms                                                                     | 74.0 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                   |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240825-pythonperf2-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|---------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_generators          | 367 ms                                                                      | 362 ms: 1.01x faster                                                           |
| async_tree_memoization    | 401 ms                                                                      | 397 ms: 1.01x faster                                                           |
| coroutines                | 21.6 ms                                                                     | 21.4 ms: 1.01x faster                                                          |
| async_tree_memoization_tg | 391 ms                                                                      | 389 ms: 1.00x faster                                                           |
| asyncio_websockets        | 384 ms                                                                      | 391 ms: 1.02x slower                                                           |
| Geometric mean            | (ref)                                                                       | 1.00x faster                                                                   |

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_io, async_tree_none, asyncio_tcp_ssl, async_tree_cpu_io_mixed, asyncio_tcp, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240825-pythonperf2-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 253 ms                                                                      | 254 ms: 1.00x slower                                                           |
| float          | 79.2 ms                                                                     | 80.3 ms: 1.01x slower                                                          |
| nbody          | 88.6 ms                                                                     | 92.6 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240825-pythonperf2-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 3.52 ms                                                                     | 3.51 ms: 1.00x faster                                                          |
| regex_v8       | 25.4 ms                                                                     | 27.1 ms: 1.06x slower                                                          |
| regex_dna      | 234 ms                                                                      | 255 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                                       | 1.04x slower                                                                   |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240825-pythonperf2-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 10.8 ms                                                                     | 10.6 ms: 1.02x faster                                                          |
| tomli_loads          | 2.56 sec                                                                    | 2.51 sec: 1.02x faster                                                         |
| unpickle_pure_python | 222 us                                                                      | 218 us: 1.02x faster                                                           |
| xml_etree_parse      | 143 ms                                                                      | 142 ms: 1.00x faster                                                           |
| xml_etree_generate   | 85.1 ms                                                                     | 85.8 ms: 1.01x slower                                                          |
| xml_etree_process    | 59.5 ms                                                                     | 60.2 ms: 1.01x slower                                                          |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                                   |

Benchmark hidden because not significant (3): pickle_pure_python, xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240825-pythonperf2-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 9.01 ms                                                                     | 9.04 ms: 1.00x slower                                                          |
| python_startup         | 13.3 ms                                                                     | 13.3 ms: 1.01x slower                                                          |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240825-pythonperf2-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|-----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 54.3 ms                                                                     | 52.2 ms: 1.04x faster                                                          |
| genshi_text     | 24.8 ms                                                                     | 24.1 ms: 1.03x faster                                                          |
| django_template | 41.5 ms                                                                     | 40.5 ms: 1.03x faster                                                          |
| Geometric mean  | (ref)                                                                       | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20240825-pythonperf2-x86_64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|---------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| raytrace                  | 287 ms                                                                      | 270 ms: 1.06x faster                                                           |
| scimark_sparse_mat_mult   | 4.36 ms                                                                     | 4.12 ms: 1.06x faster                                                          |
| scimark_sor               | 123 ms                                                                      | 118 ms: 1.04x faster                                                           |
| genshi_xml                | 54.3 ms                                                                     | 52.2 ms: 1.04x faster                                                          |
| genshi_text               | 24.8 ms                                                                     | 24.1 ms: 1.03x faster                                                          |
| django_template           | 41.5 ms                                                                     | 40.5 ms: 1.03x faster                                                          |
| json_dumps                | 10.8 ms                                                                     | 10.6 ms: 1.02x faster                                                          |
| chaos                     | 62.5 ms                                                                     | 61.2 ms: 1.02x faster                                                          |
| logging_simple            | 6.37 us                                                                     | 6.24 us: 1.02x faster                                                          |
| tomli_loads               | 2.56 sec                                                                    | 2.51 sec: 1.02x faster                                                         |
| scimark_fft               | 304 ms                                                                      | 298 ms: 1.02x faster                                                           |
| spectral_norm             | 97.1 ms                                                                     | 95.3 ms: 1.02x faster                                                          |
| deepcopy_reduce           | 2.98 us                                                                     | 2.92 us: 1.02x faster                                                          |
| unpickle_pure_python      | 222 us                                                                      | 218 us: 1.02x faster                                                           |
| richards                  | 50.5 ms                                                                     | 49.6 ms: 1.02x faster                                                          |
| go                        | 179 ms                                                                      | 177 ms: 1.01x faster                                                           |
| deltablue                 | 3.41 ms                                                                     | 3.37 ms: 1.01x faster                                                          |
| async_generators          | 367 ms                                                                      | 362 ms: 1.01x faster                                                           |
| pycparser                 | 1.25 sec                                                                    | 1.24 sec: 1.01x faster                                                         |
| crypto_pyaes              | 73.3 ms                                                                     | 72.4 ms: 1.01x faster                                                          |
| pyflate                   | 478 ms                                                                      | 472 ms: 1.01x faster                                                           |
| async_tree_memoization    | 401 ms                                                                      | 397 ms: 1.01x faster                                                           |
| richards_super            | 56.3 ms                                                                     | 55.7 ms: 1.01x faster                                                          |
| coroutines                | 21.6 ms                                                                     | 21.4 ms: 1.01x faster                                                          |
| 2to3                      | 284 ms                                                                      | 282 ms: 1.01x faster                                                           |
| pprint_pformat            | 1.67 sec                                                                    | 1.66 sec: 1.01x faster                                                         |
| thrift                    | 858 us                                                                      | 853 us: 1.01x faster                                                           |
| pathlib                   | 15.9 ms                                                                     | 15.8 ms: 1.01x faster                                                          |
| hexiom                    | 6.25 ms                                                                     | 6.22 ms: 1.01x faster                                                          |
| async_tree_memoization_tg | 391 ms                                                                      | 389 ms: 1.00x faster                                                           |
| xml_etree_parse           | 143 ms                                                                      | 142 ms: 1.00x faster                                                           |
| regex_effbot              | 3.52 ms                                                                     | 3.51 ms: 1.00x faster                                                          |
| scimark_monte_carlo       | 67.0 ms                                                                     | 67.2 ms: 1.00x slower                                                          |
| python_startup_no_site    | 9.01 ms                                                                     | 9.04 ms: 1.00x slower                                                          |
| coverage                  | 79.5 ms                                                                     | 79.7 ms: 1.00x slower                                                          |
| sympy_str                 | 291 ms                                                                      | 292 ms: 1.00x slower                                                           |
| pidigits                  | 253 ms                                                                      | 254 ms: 1.00x slower                                                           |
| mdp                       | 2.50 sec                                                                    | 2.52 sec: 1.01x slower                                                         |
| python_startup            | 13.3 ms                                                                     | 13.3 ms: 1.01x slower                                                          |
| xml_etree_generate        | 85.1 ms                                                                     | 85.8 ms: 1.01x slower                                                          |
| logging_silent            | 98.0 ns                                                                     | 98.9 ns: 1.01x slower                                                          |
| meteor_contest            | 125 ms                                                                      | 127 ms: 1.01x slower                                                           |
| sympy_expand              | 500 ms                                                                      | 505 ms: 1.01x slower                                                           |
| xml_etree_process         | 59.5 ms                                                                     | 60.2 ms: 1.01x slower                                                          |
| sympy_sum                 | 151 ms                                                                      | 153 ms: 1.01x slower                                                           |
| deepcopy_memo             | 29.8 us                                                                     | 30.2 us: 1.01x slower                                                          |
| float                     | 79.2 ms                                                                     | 80.3 ms: 1.01x slower                                                          |
| html5lib                  | 72.8 ms                                                                     | 74.0 ms: 1.02x slower                                                          |
| typing_runtime_protocols  | 172 us                                                                      | 175 us: 1.02x slower                                                           |
| generators                | 28.8 ms                                                                     | 29.3 ms: 1.02x slower                                                          |
| asyncio_websockets        | 384 ms                                                                      | 391 ms: 1.02x slower                                                           |
| bpe_tokeniser             | 4.87 sec                                                                    | 4.96 sec: 1.02x slower                                                         |
| fannkuch                  | 356 ms                                                                      | 365 ms: 1.03x slower                                                           |
| nbody                     | 88.6 ms                                                                     | 92.6 ms: 1.04x slower                                                          |
| regex_v8                  | 25.4 ms                                                                     | 27.1 ms: 1.06x slower                                                          |
| regex_dna                 | 234 ms                                                                      | 255 ms: 1.09x slower                                                           |
| Geometric mean            | (ref)                                                                       | 1.00x faster                                                                   |

Benchmark hidden because not significant (33): json, pickle_pure_python, async_tree_io_tg, sqlglot_transpile, comprehensions, async_tree_io, regex_compile, async_tree_none, xml_etree_iterparse, logging_format, asyncio_tcp_ssl, sqlglot_optimize, async_tree_cpu_io_mixed, create_gc_cycles, deepcopy, json_loads, sqlglot_parse, pprint_safe_repr, sympy_integrate, nqueens, docutils, tornado_http, bench_mp_pool, bench_thread_pool, sqlglot_normalize, pylint, asyncio_tcp, async_tree_none_tg, telco, gc_traversal, mako, async_tree_cpu_io_mixed_tg, scimark_lu

# HPT report

- Reliability score: 68.16% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x