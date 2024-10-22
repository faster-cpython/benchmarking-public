# Results vs. base

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-x86_64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.01x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240730-pythonperf2-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 286 ms                                                                      | 288 ms: 1.01x slower                                                                  |
| html5lib       | 72.4 ms                                                                     | 74.1 ms: 1.02x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                          |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240730-pythonperf2-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|---------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl           | 1.58 sec                                                                    | 1.58 sec: 1.00x slower                                                                |
| async_tree_memoization_tg | 386 ms                                                                      | 388 ms: 1.00x slower                                                                  |
| asyncio_tcp               | 373 ms                                                                      | 375 ms: 1.01x slower                                                                  |
| Geometric mean            | (ref)                                                                       | 1.01x slower                                                                          |

Benchmark hidden because not significant (10): async_generators, coroutines, asyncio_websockets, async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240730-pythonperf2-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                                     | 85.6 ms: 1.02x faster                                                                 |
| pidigits       | 252 ms                                                                      | 254 ms: 1.01x slower                                                                  |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240730-pythonperf2-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_dna      | 245 ms                                                                      | 236 ms: 1.04x faster                                                                  |
| regex_v8       | 25.9 ms                                                                     | 25.6 ms: 1.01x faster                                                                 |
| regex_effbot   | 3.48 ms                                                                     | 3.56 ms: 1.02x slower                                                                 |
| regex_compile  | 139 ms                                                                      | 143 ms: 1.03x slower                                                                  |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240730-pythonperf2-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 2.26 sec                                                                    | 2.21 sec: 1.02x faster                                                                |
| json_dumps           | 10.9 ms                                                                     | 10.8 ms: 1.01x faster                                                                 |
| unpickle_pure_python | 212 us                                                                      | 210 us: 1.01x faster                                                                  |
| xml_etree_generate   | 85.7 ms                                                                     | 85.3 ms: 1.00x faster                                                                 |
| json_loads           | 25.7 us                                                                     | 25.8 us: 1.01x slower                                                                 |
| xml_etree_iterparse  | 101 ms                                                                      | 104 ms: 1.02x slower                                                                  |
| xml_etree_parse      | 142 ms                                                                      | 145 ms: 1.03x slower                                                                  |
| Geometric mean       | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240730-pythonperf2-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup | 13.4 ms                                                                     | 13.4 ms: 1.00x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240730-pythonperf2-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                                     | 10.6 ms: 1.01x slower                                                                 |
| genshi_xml      | 53.8 ms                                                                     | 54.7 ms: 1.02x slower                                                                 |
| django_template | 39.5 ms                                                                     | 40.7 ms: 1.03x slower                                                                 |
| genshi_text     | 24.9 ms                                                                     | 27.1 ms: 1.09x slower                                                                 |
| Geometric mean  | (ref)                                                                       | 1.04x slower                                                                          |

All benchmarks:
===============

| Benchmark                 | bm-20240730-pythonperf2-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|---------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_dna                 | 245 ms                                                                      | 236 ms: 1.04x faster                                                                  |
| coverage                  | 81.1 ms                                                                     | 78.8 ms: 1.03x faster                                                                 |
| scimark_sor               | 118 ms                                                                      | 115 ms: 1.03x faster                                                                  |
| tomli_loads               | 2.26 sec                                                                    | 2.21 sec: 1.02x faster                                                                |
| mdp                       | 2.56 sec                                                                    | 2.50 sec: 1.02x faster                                                                |
| nbody                     | 87.0 ms                                                                     | 85.6 ms: 1.02x faster                                                                 |
| raytrace                  | 271 ms                                                                      | 266 ms: 1.02x faster                                                                  |
| json                      | 5.57 ms                                                                     | 5.48 ms: 1.02x faster                                                                 |
| json_dumps                | 10.9 ms                                                                     | 10.8 ms: 1.01x faster                                                                 |
| bpe_tokeniser             | 4.96 sec                                                                    | 4.90 sec: 1.01x faster                                                                |
| regex_v8                  | 25.9 ms                                                                     | 25.6 ms: 1.01x faster                                                                 |
| unpickle_pure_python      | 212 us                                                                      | 210 us: 1.01x faster                                                                  |
| generators                | 28.9 ms                                                                     | 28.7 ms: 1.01x faster                                                                 |
| xml_etree_generate        | 85.7 ms                                                                     | 85.3 ms: 1.00x faster                                                                 |
| spectral_norm             | 96.5 ms                                                                     | 96.1 ms: 1.00x faster                                                                 |
| meteor_contest            | 128 ms                                                                      | 128 ms: 1.00x faster                                                                  |
| asyncio_tcp_ssl           | 1.58 sec                                                                    | 1.58 sec: 1.00x slower                                                                |
| python_startup            | 13.4 ms                                                                     | 13.4 ms: 1.00x slower                                                                 |
| async_tree_memoization_tg | 386 ms                                                                      | 388 ms: 1.00x slower                                                                  |
| chaos                     | 62.1 ms                                                                     | 62.5 ms: 1.01x slower                                                                 |
| richards                  | 50.7 ms                                                                     | 51.0 ms: 1.01x slower                                                                 |
| logging_silent            | 96.8 ns                                                                     | 97.4 ns: 1.01x slower                                                                 |
| pprint_pformat            | 1.69 sec                                                                    | 1.70 sec: 1.01x slower                                                                |
| pidigits                  | 252 ms                                                                      | 254 ms: 1.01x slower                                                                  |
| 2to3                      | 286 ms                                                                      | 288 ms: 1.01x slower                                                                  |
| comprehensions            | 17.5 us                                                                     | 17.6 us: 1.01x slower                                                                 |
| json_loads                | 25.7 us                                                                     | 25.8 us: 1.01x slower                                                                 |
| sympy_integrate           | 23.4 ms                                                                     | 23.5 ms: 1.01x slower                                                                 |
| asyncio_tcp               | 373 ms                                                                      | 375 ms: 1.01x slower                                                                  |
| logging_simple            | 6.21 us                                                                     | 6.25 us: 1.01x slower                                                                 |
| thrift                    | 879 us                                                                      | 886 us: 1.01x slower                                                                  |
| sympy_sum                 | 155 ms                                                                      | 156 ms: 1.01x slower                                                                  |
| deepcopy_reduce           | 2.92 us                                                                     | 2.95 us: 1.01x slower                                                                 |
| sympy_str                 | 295 ms                                                                      | 299 ms: 1.01x slower                                                                  |
| mako                      | 10.4 ms                                                                     | 10.6 ms: 1.01x slower                                                                 |
| gc_traversal              | 4.69 ms                                                                     | 4.75 ms: 1.01x slower                                                                 |
| hexiom                    | 6.31 ms                                                                     | 6.39 ms: 1.01x slower                                                                 |
| richards_super            | 56.5 ms                                                                     | 57.3 ms: 1.01x slower                                                                 |
| sympy_expand              | 503 ms                                                                      | 511 ms: 1.02x slower                                                                  |
| scimark_monte_carlo       | 65.5 ms                                                                     | 66.5 ms: 1.02x slower                                                                 |
| genshi_xml                | 53.8 ms                                                                     | 54.7 ms: 1.02x slower                                                                 |
| dask                      | 379 ms                                                                      | 386 ms: 1.02x slower                                                                  |
| telco                     | 7.93 ms                                                                     | 8.09 ms: 1.02x slower                                                                 |
| typing_runtime_protocols  | 172 us                                                                      | 176 us: 1.02x slower                                                                  |
| xml_etree_iterparse       | 101 ms                                                                      | 104 ms: 1.02x slower                                                                  |
| go                        | 156 ms                                                                      | 160 ms: 1.02x slower                                                                  |
| html5lib                  | 72.4 ms                                                                     | 74.1 ms: 1.02x slower                                                                 |
| regex_effbot              | 3.48 ms                                                                     | 3.56 ms: 1.02x slower                                                                 |
| scimark_lu                | 96.7 ms                                                                     | 99.2 ms: 1.03x slower                                                                 |
| nqueens                   | 88.5 ms                                                                     | 90.7 ms: 1.03x slower                                                                 |
| xml_etree_parse           | 142 ms                                                                      | 145 ms: 1.03x slower                                                                  |
| scimark_fft               | 301 ms                                                                      | 310 ms: 1.03x slower                                                                  |
| regex_compile             | 139 ms                                                                      | 143 ms: 1.03x slower                                                                  |
| pyflate                   | 478 ms                                                                      | 491 ms: 1.03x slower                                                                  |
| django_template           | 39.5 ms                                                                     | 40.7 ms: 1.03x slower                                                                 |
| pycparser                 | 1.22 sec                                                                    | 1.28 sec: 1.05x slower                                                                |
| genshi_text               | 24.9 ms                                                                     | 27.1 ms: 1.09x slower                                                                 |
| scimark_sparse_mat_mult   | 4.03 ms                                                                     | 4.44 ms: 1.10x slower                                                                 |
| Geometric mean            | (ref)                                                                       | 1.01x slower                                                                          |

Benchmark hidden because not significant (32): deltablue, bench_mp_pool, sqlglot_optimize, pickle_pure_python, float, deepcopy_memo, sqlglot_transpile, python_startup_no_site, async_generators, crypto_pyaes, coroutines, xml_etree_process, pprint_safe_repr, sqlglot_normalize, asyncio_websockets, fannkuch, pathlib, create_gc_cycles, docutils, deepcopy, sqlglot_parse, pylint, logging_format, async_tree_none_tg, tornado_http, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_io, bench_thread_pool, async_tree_memoization, async_tree_cpu_io_mixed

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x