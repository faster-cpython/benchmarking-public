# Results vs. base

- fork: faster-cpython
- ref: lower_before
- machine: linux-x86_64
- commit hash: 68df0a5
- commit date: 2024-06-17
- overall geometric mean: 1.00x faster
- HPT reliability: 65.19%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240617-linux-x86_64-python-3df2022931f77c5cadb3-3.14.0a0-3df2022 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 271 ms                                                                | 270 ms: 1.00x faster                                                    |
| html5lib       | 67.6 ms                                                               | 68.9 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240617-linux-x86_64-python-3df2022931f77c5cadb3-3.14.0a0-3df2022 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|---------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg        | 342 ms                                                                | 332 ms: 1.03x faster                                                    |
| async_tree_memoization_tg | 445 ms                                                                | 460 ms: 1.03x slower                                                    |
| async_tree_memoization    | 470 ms                                                                | 489 ms: 1.04x slower                                                    |
| async_tree_io_tg          | 946 ms                                                                | 1.01 sec: 1.07x slower                                                  |
| Geometric mean            | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (4): async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240617-linux-x86_64-python-3df2022931f77c5cadb3-3.14.0a0-3df2022 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 79.0 ms                                                               | 78.1 ms: 1.01x faster                                                   |
| nbody          | 89.1 ms                                                               | 88.3 ms: 1.01x faster                                                   |
| pidigits       | 191 ms                                                                | 190 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240617-linux-x86_64-python-3df2022931f77c5cadb3-3.14.0a0-3df2022 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 28.0 ms                                                               | 24.2 ms: 1.15x faster                                                   |
| regex_dna      | 240 ms                                                                | 232 ms: 1.04x faster                                                    |
| regex_effbot   | 3.83 ms                                                               | 3.79 ms: 1.01x faster                                                   |
| regex_compile  | 133 ms                                                                | 134 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240617-linux-x86_64-python-3df2022931f77c5cadb3-3.14.0a0-3df2022 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle               | 12.0 us                                                               | 11.6 us: 1.03x faster                                                   |
| pickle_dict          | 35.5 us                                                               | 34.7 us: 1.02x faster                                                   |
| unpickle_pure_python | 215 us                                                                | 216 us: 1.00x slower                                                    |
| xml_etree_generate   | 86.0 ms                                                               | 86.3 ms: 1.00x slower                                                   |
| json_dumps           | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                   |
| json_loads           | 28.7 us                                                               | 29.0 us: 1.01x slower                                                   |
| unpickle_list        | 5.33 us                                                               | 5.50 us: 1.03x slower                                                   |
| tomli_loads          | 2.11 sec                                                              | 2.18 sec: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (6): unpickle, xml_etree_iterparse, pickle_pure_python, pickle_list, xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240617-linux-x86_64-python-3df2022931f77c5cadb3-3.14.0a0-3df2022 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 10.7 ms                                                               | 10.7 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240617-linux-x86_64-python-3df2022931f77c5cadb3-3.14.0a0-3df2022 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 35.3 ms                                                               | 34.4 ms: 1.03x faster                                                   |
| genshi_text     | 24.2 ms                                                               | 23.7 ms: 1.02x faster                                                   |
| mako            | 11.2 ms                                                               | 11.2 ms: 1.01x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20240617-linux-x86_64-python-3df2022931f77c5cadb3-3.14.0a0-3df2022 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|---------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8                  | 28.0 ms                                                               | 24.2 ms: 1.15x faster                                                   |
| pycparser                 | 1.21 sec                                                              | 1.16 sec: 1.05x faster                                                  |
| regex_dna                 | 240 ms                                                                | 232 ms: 1.04x faster                                                    |
| pickle                    | 12.0 us                                                               | 11.6 us: 1.03x faster                                                   |
| async_tree_none_tg        | 342 ms                                                                | 332 ms: 1.03x faster                                                    |
| bench_thread_pool         | 830 us                                                                | 807 us: 1.03x faster                                                    |
| django_template           | 35.3 ms                                                               | 34.4 ms: 1.03x faster                                                   |
| logging_simple            | 5.75 us                                                               | 5.62 us: 1.02x faster                                                   |
| nqueens                   | 80.0 ms                                                               | 78.2 ms: 1.02x faster                                                   |
| pickle_dict               | 35.5 us                                                               | 34.7 us: 1.02x faster                                                   |
| genshi_text               | 24.2 ms                                                               | 23.7 ms: 1.02x faster                                                   |
| hexiom                    | 6.20 ms                                                               | 6.09 ms: 1.02x faster                                                   |
| scimark_sor               | 135 ms                                                                | 133 ms: 1.01x faster                                                    |
| scimark_sparse_mat_mult   | 5.14 ms                                                               | 5.07 ms: 1.01x faster                                                   |
| regex_effbot              | 3.83 ms                                                               | 3.79 ms: 1.01x faster                                                   |
| spectral_norm             | 114 ms                                                                | 113 ms: 1.01x faster                                                    |
| float                     | 79.0 ms                                                               | 78.1 ms: 1.01x faster                                                   |
| raytrace                  | 267 ms                                                                | 264 ms: 1.01x faster                                                    |
| nbody                     | 89.1 ms                                                               | 88.3 ms: 1.01x faster                                                   |
| meteor_contest            | 109 ms                                                                | 108 ms: 1.01x faster                                                    |
| logging_format            | 6.41 us                                                               | 6.35 us: 1.01x faster                                                   |
| go                        | 146 ms                                                                | 145 ms: 1.01x faster                                                    |
| async_generators          | 445 ms                                                                | 442 ms: 1.01x faster                                                    |
| scimark_lu                | 115 ms                                                                | 114 ms: 1.01x faster                                                    |
| deltablue                 | 3.27 ms                                                               | 3.24 ms: 1.01x faster                                                   |
| pathlib                   | 16.4 ms                                                               | 16.3 ms: 1.01x faster                                                   |
| sympy_integrate           | 20.3 ms                                                               | 20.2 ms: 1.01x faster                                                   |
| pidigits                  | 191 ms                                                                | 190 ms: 1.00x faster                                                    |
| sqlglot_transpile         | 1.63 ms                                                               | 1.62 ms: 1.00x faster                                                   |
| 2to3                      | 271 ms                                                                | 270 ms: 1.00x faster                                                    |
| python_startup            | 10.7 ms                                                               | 10.7 ms: 1.00x slower                                                   |
| unpickle_pure_python      | 215 us                                                                | 216 us: 1.00x slower                                                    |
| xml_etree_generate        | 86.0 ms                                                               | 86.3 ms: 1.00x slower                                                   |
| generators                | 29.2 ms                                                               | 29.4 ms: 1.01x slower                                                   |
| regex_compile             | 133 ms                                                                | 134 ms: 1.01x slower                                                    |
| asyncio_websockets        | 563 ms                                                                | 567 ms: 1.01x slower                                                    |
| mako                      | 11.2 ms                                                               | 11.2 ms: 1.01x slower                                                   |
| json_dumps                | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                   |
| comprehensions            | 16.6 us                                                               | 16.7 us: 1.01x slower                                                   |
| chaos                     | 60.0 ms                                                               | 60.4 ms: 1.01x slower                                                   |
| sqlglot_optimize          | 54.6 ms                                                               | 55.0 ms: 1.01x slower                                                   |
| dulwich_log               | 65.0 ms                                                               | 65.6 ms: 1.01x slower                                                   |
| json_loads                | 28.7 us                                                               | 29.0 us: 1.01x slower                                                   |
| deepcopy_memo             | 29.6 us                                                               | 29.9 us: 1.01x slower                                                   |
| bpe_tokeniser             | 4.91 sec                                                              | 4.97 sec: 1.01x slower                                                  |
| deepcopy                  | 266 us                                                                | 270 us: 1.01x slower                                                    |
| sqlglot_normalize         | 109 ms                                                                | 111 ms: 1.01x slower                                                    |
| thrift                    | 796 us                                                                | 810 us: 1.02x slower                                                    |
| scimark_monte_carlo       | 67.9 ms                                                               | 69.1 ms: 1.02x slower                                                   |
| richards_super            | 55.1 ms                                                               | 56.1 ms: 1.02x slower                                                   |
| html5lib                  | 67.6 ms                                                               | 68.9 ms: 1.02x slower                                                   |
| mdp                       | 2.57 sec                                                              | 2.63 sec: 1.02x slower                                                  |
| richards                  | 48.5 ms                                                               | 49.8 ms: 1.03x slower                                                   |
| deepcopy_reduce           | 2.70 us                                                               | 2.78 us: 1.03x slower                                                   |
| fannkuch                  | 389 ms                                                                | 401 ms: 1.03x slower                                                    |
| unpickle_list             | 5.33 us                                                               | 5.50 us: 1.03x slower                                                   |
| tomli_loads               | 2.11 sec                                                              | 2.18 sec: 1.03x slower                                                  |
| async_tree_memoization_tg | 445 ms                                                                | 460 ms: 1.03x slower                                                    |
| async_tree_memoization    | 470 ms                                                                | 489 ms: 1.04x slower                                                    |
| scimark_fft               | 361 ms                                                                | 377 ms: 1.04x slower                                                    |
| coroutines                | 23.3 ms                                                               | 24.3 ms: 1.05x slower                                                   |
| pyflate                   | 470 ms                                                                | 492 ms: 1.05x slower                                                    |
| gc_traversal              | 3.61 ms                                                               | 3.80 ms: 1.05x slower                                                   |
| async_tree_io_tg          | 946 ms                                                                | 1.01 sec: 1.07x slower                                                  |
| Geometric mean            | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (33): async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_cpu_io_mixed, logging_silent, unpickle, dask, xml_etree_iterparse, crypto_pyaes, sqlglot_parse, sqlite_synth, sympy_sum, genshi_xml, pylint, pickle_pure_python, tornado_http, telco, asyncio_tcp_ssl, pickle_list, xml_etree_process, python_startup_no_site, sympy_str, create_gc_cycles, json, bench_mp_pool, asyncio_tcp, sympy_expand, pprint_pformat, docutils, typing_runtime_protocols, pprint_safe_repr, coverage, xml_etree_parse

# HPT report

- Reliability score: 65.19% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x