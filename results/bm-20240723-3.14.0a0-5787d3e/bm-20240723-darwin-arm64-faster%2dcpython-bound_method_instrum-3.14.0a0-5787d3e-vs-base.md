# Results vs. base

- fork: faster-cpython
- ref: bound_method_instrum
- machine: darwin-arm64
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.00x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                                | 162 ms: 1.00x slower                                                            |
| tornado_http   | 67.9 ms                                                               | 65.1 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager_tg              | 41.1 ms                                                               | 40.6 ms: 1.01x faster                                                           |
| async_tree_eager                 | 61.2 ms                                                               | 60.6 ms: 1.01x faster                                                           |
| async_tree_memoization           | 236 ms                                                                | 235 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 446 ms                                                                | 444 ms: 1.01x faster                                                            |
| async_generators                 | 281 ms                                                                | 280 ms: 1.00x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 332 ms                                                                | 330 ms: 1.00x faster                                                            |
| asyncio_websockets               | 408 ms                                                                | 408 ms: 1.00x faster                                                            |
| Geometric mean                   | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (14): asyncio_tcp, async_tree_io_tg, async_tree_none_tg, async_tree_eager_memoization_tg, async_tree_eager_memoization, async_tree_none, async_tree_io, async_tree_eager_io, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_eager_io_tg, async_tree_eager_cpu_io_mixed, coroutines, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 49.4 ms                                                               | 48.3 ms: 1.02x faster                                                           |
| pidigits       | 281 ms                                                                | 281 ms: 1.00x faster                                                            |
| nbody          | 60.1 ms                                                               | 62.2 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.62 ms                                                               | 2.54 ms: 1.03x faster                                                           |
| regex_compile  | 68.5 ms                                                               | 68.0 ms: 1.01x faster                                                           |
| regex_v8       | 17.8 ms                                                               | 17.7 ms: 1.01x faster                                                           |
| regex_dna      | 149 ms                                                                | 149 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|--------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads         | 17.1 us                                                               | 17.0 us: 1.01x faster                                                           |
| xml_etree_generate | 52.7 ms                                                               | 52.3 ms: 1.01x faster                                                           |
| pickle_pure_python | 183 us                                                                | 182 us: 1.01x faster                                                            |
| json_dumps         | 6.36 ms                                                               | 6.41 ms: 1.01x slower                                                           |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (5): unpickle_pure_python, xml_etree_parse, xml_etree_process, tomli_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup | 15.1 ms                                                               | 14.9 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 7.19 ms                                                               | 6.93 ms: 1.04x faster                                                           |
| genshi_xml     | 30.2 ms                                                               | 30.8 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                        | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tornado_http                     | 67.9 ms                                                               | 65.1 ms: 1.04x faster                                                           |
| mako                             | 7.19 ms                                                               | 6.93 ms: 1.04x faster                                                           |
| chaos                            | 35.9 ms                                                               | 34.8 ms: 1.03x faster                                                           |
| regex_effbot                     | 2.62 ms                                                               | 2.54 ms: 1.03x faster                                                           |
| float                            | 49.4 ms                                                               | 48.3 ms: 1.02x faster                                                           |
| json                             | 3.01 ms                                                               | 2.95 ms: 1.02x faster                                                           |
| raytrace                         | 149 ms                                                                | 146 ms: 1.02x faster                                                            |
| mdp                              | 1.43 sec                                                              | 1.41 sec: 1.02x faster                                                          |
| pprint_safe_repr                 | 473 ms                                                                | 464 ms: 1.02x faster                                                            |
| thrift                           | 438 us                                                                | 431 us: 1.02x faster                                                            |
| deepcopy_reduce                  | 1.52 us                                                               | 1.49 us: 1.02x faster                                                           |
| logging_format                   | 3.38 us                                                               | 3.33 us: 1.01x faster                                                           |
| deepcopy_memo                    | 16.9 us                                                               | 16.7 us: 1.01x faster                                                           |
| async_tree_eager_tg              | 41.1 ms                                                               | 40.6 ms: 1.01x faster                                                           |
| logging_simple                   | 3.07 us                                                               | 3.03 us: 1.01x faster                                                           |
| pprint_pformat                   | 960 ms                                                                | 948 ms: 1.01x faster                                                            |
| coverage                         | 45.2 ms                                                               | 44.7 ms: 1.01x faster                                                           |
| deltablue                        | 2.12 ms                                                               | 2.09 ms: 1.01x faster                                                           |
| python_startup                   | 15.1 ms                                                               | 14.9 ms: 1.01x faster                                                           |
| generators                       | 20.9 ms                                                               | 20.7 ms: 1.01x faster                                                           |
| json_loads                       | 17.1 us                                                               | 17.0 us: 1.01x faster                                                           |
| async_tree_eager                 | 61.2 ms                                                               | 60.6 ms: 1.01x faster                                                           |
| xml_etree_generate               | 52.7 ms                                                               | 52.3 ms: 1.01x faster                                                           |
| scimark_lu                       | 69.8 ms                                                               | 69.3 ms: 1.01x faster                                                           |
| telco                            | 4.65 ms                                                               | 4.61 ms: 1.01x faster                                                           |
| pathlib                          | 23.0 ms                                                               | 22.9 ms: 1.01x faster                                                           |
| sqlglot_parse                    | 746 us                                                                | 741 us: 1.01x faster                                                            |
| regex_compile                    | 68.5 ms                                                               | 68.0 ms: 1.01x faster                                                           |
| async_tree_memoization           | 236 ms                                                                | 235 ms: 1.01x faster                                                            |
| sqlglot_transpile                | 909 us                                                                | 902 us: 1.01x faster                                                            |
| pickle_pure_python               | 183 us                                                                | 182 us: 1.01x faster                                                            |
| create_gc_cycles                 | 899 us                                                                | 893 us: 1.01x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 446 ms                                                                | 444 ms: 1.01x faster                                                            |
| regex_v8                         | 17.8 ms                                                               | 17.7 ms: 1.01x faster                                                           |
| sympy_sum                        | 70.3 ms                                                               | 70.0 ms: 1.01x faster                                                           |
| async_generators                 | 281 ms                                                                | 280 ms: 1.00x faster                                                            |
| spectral_norm                    | 66.4 ms                                                               | 66.0 ms: 1.00x faster                                                           |
| richards                         | 31.3 ms                                                               | 31.2 ms: 1.00x faster                                                           |
| richards_super                   | 34.4 ms                                                               | 34.3 ms: 1.00x faster                                                           |
| scimark_monte_carlo              | 42.8 ms                                                               | 42.7 ms: 1.00x faster                                                           |
| async_tree_eager_cpu_io_mixed_tg | 332 ms                                                                | 330 ms: 1.00x faster                                                            |
| crypto_pyaes                     | 50.6 ms                                                               | 50.5 ms: 1.00x faster                                                           |
| scimark_sparse_mat_mult          | 2.81 ms                                                               | 2.80 ms: 1.00x faster                                                           |
| nqueens                          | 54.0 ms                                                               | 53.8 ms: 1.00x faster                                                           |
| meteor_contest                   | 71.6 ms                                                               | 71.5 ms: 1.00x faster                                                           |
| scimark_fft                      | 183 ms                                                                | 183 ms: 1.00x faster                                                            |
| bpe_tokeniser                    | 3.11 sec                                                              | 3.10 sec: 1.00x faster                                                          |
| pidigits                         | 281 ms                                                                | 281 ms: 1.00x faster                                                            |
| asyncio_websockets               | 408 ms                                                                | 408 ms: 1.00x faster                                                            |
| regex_dna                        | 149 ms                                                                | 149 ms: 1.00x faster                                                            |
| logging_silent                   | 59.3 ns                                                               | 59.3 ns: 1.00x slower                                                           |
| bench_thread_pool                | 452 us                                                                | 453 us: 1.00x slower                                                            |
| 2to3                             | 161 ms                                                                | 162 ms: 1.00x slower                                                            |
| pyflate                          | 322 ms                                                                | 324 ms: 1.01x slower                                                            |
| json_dumps                       | 6.36 ms                                                               | 6.41 ms: 1.01x slower                                                           |
| hexiom                           | 4.08 ms                                                               | 4.11 ms: 1.01x slower                                                           |
| fannkuch                         | 263 ms                                                                | 267 ms: 1.02x slower                                                            |
| genshi_xml                       | 30.2 ms                                                               | 30.8 ms: 1.02x slower                                                           |
| typing_runtime_protocols         | 90.8 us                                                               | 92.7 us: 1.02x slower                                                           |
| comprehensions                   | 10.6 us                                                               | 10.9 us: 1.02x slower                                                           |
| nbody                            | 60.1 ms                                                               | 62.2 ms: 1.03x slower                                                           |
| go                               | 98.3 ms                                                               | 104 ms: 1.06x slower                                                            |
| Geometric mean                   | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (36): asyncio_tcp, async_tree_io_tg, async_tree_none_tg, async_tree_eager_memoization_tg, bench_mp_pool, async_tree_eager_memoization, async_tree_none, dask, async_tree_io, async_tree_eager_io, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_eager_io_tg, async_tree_eager_cpu_io_mixed, unpickle_pure_python, xml_etree_parse, sympy_str, pycparser, python_startup_no_site, sqlglot_optimize, genshi_text, html5lib, coroutines, pylint, gc_traversal, scimark_sor, sqlglot_normalize, xml_etree_process, sympy_integrate, django_template, deepcopy, sympy_expand, asyncio_tcp_ssl, docutils, tomli_loads, xml_etree_iterparse

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x