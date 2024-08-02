# Results vs. base

- fork: faster-cpython
- ref: experimental_branch_
- machine: windows-x86
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                         | 258 ms: 1.02x slower                                                                     |
| docutils       | 1.90 sec                                                                       | 1.92 sec: 1.01x slower                                                                   |
| html5lib       | 47.9 ms                                                                        | 49.5 ms: 1.03x slower                                                                    |
| Geometric mean | (ref)                                                                          | 1.02x slower                                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 478 ms                                                                         | 462 ms: 1.04x faster                                                                     |
| async_tree_cpu_io_mixed    | 490 ms                                                                         | 474 ms: 1.03x faster                                                                     |
| asyncio_tcp_ssl            | 17.0 sec                                                                       | 16.9 sec: 1.01x faster                                                                   |
| coroutines                 | 17.0 ms                                                                        | 17.4 ms: 1.02x slower                                                                    |
| async_tree_memoization_tg  | 245 ms                                                                         | 250 ms: 1.02x slower                                                                     |
| async_tree_io_tg           | 500 ms                                                                         | 517 ms: 1.03x slower                                                                     |
| async_tree_none            | 222 ms                                                                         | 230 ms: 1.04x slower                                                                     |
| async_tree_memoization     | 270 ms                                                                         | 280 ms: 1.04x slower                                                                     |
| async_tree_io              | 538 ms                                                                         | 559 ms: 1.04x slower                                                                     |
| async_generators           | 282 ms                                                                         | 311 ms: 1.10x slower                                                                     |
| Geometric mean             | (ref)                                                                          | 1.02x slower                                                                             |

Benchmark hidden because not significant (2): asyncio_tcp, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                                         | 200 ms: 1.01x slower                                                                     |
| nbody          | 91.7 ms                                                                        | 93.6 ms: 1.02x slower                                                                    |
| float          | 59.1 ms                                                                        | 61.5 ms: 1.04x slower                                                                    |
| Geometric mean | (ref)                                                                          | 1.02x slower                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                                         | 119 ms: 1.01x faster                                                                     |
| regex_v8       | 16.0 ms                                                                        | 16.1 ms: 1.01x slower                                                                    |
| regex_compile  | 103 ms                                                                         | 110 ms: 1.07x slower                                                                     |
| Geometric mean | (ref)                                                                          | 1.02x slower                                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| json_loads           | 20.5 us                                                                        | 20.2 us: 1.02x faster                                                                    |
| xml_etree_generate   | 66.0 ms                                                                        | 66.8 ms: 1.01x slower                                                                    |
| xml_etree_iterparse  | 67.2 ms                                                                        | 68.7 ms: 1.02x slower                                                                    |
| xml_etree_process    | 47.1 ms                                                                        | 50.2 ms: 1.06x slower                                                                    |
| unpickle_pure_python | 168 us                                                                         | 181 us: 1.07x slower                                                                     |
| tomli_loads          | 1.76 sec                                                                       | 1.91 sec: 1.09x slower                                                                   |
| pickle_pure_python   | 235 us                                                                         | 257 us: 1.09x slower                                                                     |
| Geometric mean       | (ref)                                                                          | 1.04x slower                                                                             |

Benchmark hidden because not significant (2): xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.7 ms                                                                        | 19.5 ms: 1.01x faster                                                                    |
| Geometric mean         | (ref)                                                                          | 1.00x faster                                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| mako           | 8.06 ms                                                                        | 8.15 ms: 1.01x slower                                                                    |
| genshi_xml     | 47.1 ms                                                                        | 49.3 ms: 1.05x slower                                                                    |
| genshi_text    | 21.7 ms                                                                        | 23.5 ms: 1.09x slower                                                                    |
| Geometric mean | (ref)                                                                          | 1.03x slower                                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 478 ms                                                                         | 462 ms: 1.04x faster                                                                     |
| async_tree_cpu_io_mixed    | 490 ms                                                                         | 474 ms: 1.03x faster                                                                     |
| logging_format             | 8.88 us                                                                        | 8.72 us: 1.02x faster                                                                    |
| fannkuch                   | 317 ms                                                                         | 311 ms: 1.02x faster                                                                     |
| json_loads                 | 20.5 us                                                                        | 20.2 us: 1.02x faster                                                                    |
| create_gc_cycles           | 759 us                                                                         | 746 us: 1.02x faster                                                                     |
| telco                      | 6.31 ms                                                                        | 6.21 ms: 1.02x faster                                                                    |
| python_startup_no_site     | 19.7 ms                                                                        | 19.5 ms: 1.01x faster                                                                    |
| gc_traversal               | 1.46 ms                                                                        | 1.45 ms: 1.01x faster                                                                    |
| asyncio_tcp_ssl            | 17.0 sec                                                                       | 16.9 sec: 1.01x faster                                                                   |
| logging_simple             | 8.19 us                                                                        | 8.13 us: 1.01x faster                                                                    |
| regex_dna                  | 119 ms                                                                         | 119 ms: 1.01x faster                                                                     |
| pathlib                    | 88.1 ms                                                                        | 88.5 ms: 1.00x slower                                                                    |
| dulwich_log                | 50.2 ms                                                                        | 50.5 ms: 1.01x slower                                                                    |
| pidigits                   | 199 ms                                                                         | 200 ms: 1.01x slower                                                                     |
| sympy_expand               | 393 ms                                                                         | 395 ms: 1.01x slower                                                                     |
| mdp                        | 1.68 sec                                                                       | 1.69 sec: 1.01x slower                                                                   |
| regex_v8                   | 16.0 ms                                                                        | 16.1 ms: 1.01x slower                                                                    |
| docutils                   | 1.90 sec                                                                       | 1.92 sec: 1.01x slower                                                                   |
| mako                       | 8.06 ms                                                                        | 8.15 ms: 1.01x slower                                                                    |
| xml_etree_generate         | 66.0 ms                                                                        | 66.8 ms: 1.01x slower                                                                    |
| chaos                      | 51.5 ms                                                                        | 52.2 ms: 1.01x slower                                                                    |
| sympy_str                  | 221 ms                                                                         | 225 ms: 1.02x slower                                                                     |
| 2to3                       | 253 ms                                                                         | 258 ms: 1.02x slower                                                                     |
| nbody                      | 91.7 ms                                                                        | 93.6 ms: 1.02x slower                                                                    |
| sqlglot_optimize           | 44.1 ms                                                                        | 45.0 ms: 1.02x slower                                                                    |
| coroutines                 | 17.0 ms                                                                        | 17.4 ms: 1.02x slower                                                                    |
| sympy_integrate            | 15.3 ms                                                                        | 15.7 ms: 1.02x slower                                                                    |
| async_tree_memoization_tg  | 245 ms                                                                         | 250 ms: 1.02x slower                                                                     |
| xml_etree_iterparse        | 67.2 ms                                                                        | 68.7 ms: 1.02x slower                                                                    |
| sympy_sum                  | 108 ms                                                                         | 110 ms: 1.02x slower                                                                     |
| deepcopy_reduce            | 2.54 us                                                                        | 2.60 us: 1.02x slower                                                                    |
| raytrace                   | 221 ms                                                                         | 226 ms: 1.02x slower                                                                     |
| sqlglot_transpile          | 1.30 ms                                                                        | 1.33 ms: 1.02x slower                                                                    |
| sqlglot_normalize          | 230 ms                                                                         | 236 ms: 1.03x slower                                                                     |
| sqlglot_parse              | 1.04 ms                                                                        | 1.07 ms: 1.03x slower                                                                    |
| logging_silent             | 73.9 ns                                                                        | 76.2 ns: 1.03x slower                                                                    |
| pycparser                  | 847 ms                                                                         | 873 ms: 1.03x slower                                                                     |
| html5lib                   | 47.9 ms                                                                        | 49.5 ms: 1.03x slower                                                                    |
| thrift                     | 744 us                                                                         | 769 us: 1.03x slower                                                                     |
| scimark_sparse_mat_mult    | 3.04 ms                                                                        | 3.14 ms: 1.03x slower                                                                    |
| async_tree_io_tg           | 500 ms                                                                         | 517 ms: 1.03x slower                                                                     |
| async_tree_none            | 222 ms                                                                         | 230 ms: 1.04x slower                                                                     |
| scimark_fft                | 221 ms                                                                         | 230 ms: 1.04x slower                                                                     |
| async_tree_memoization     | 270 ms                                                                         | 280 ms: 1.04x slower                                                                     |
| async_tree_io              | 538 ms                                                                         | 559 ms: 1.04x slower                                                                     |
| float                      | 59.1 ms                                                                        | 61.5 ms: 1.04x slower                                                                    |
| genshi_xml                 | 47.1 ms                                                                        | 49.3 ms: 1.05x slower                                                                    |
| crypto_pyaes               | 55.9 ms                                                                        | 58.6 ms: 1.05x slower                                                                    |
| nqueens                    | 73.1 ms                                                                        | 76.8 ms: 1.05x slower                                                                    |
| pprint_pformat             | 1.34 sec                                                                       | 1.41 sec: 1.05x slower                                                                   |
| pprint_safe_repr           | 653 ms                                                                         | 693 ms: 1.06x slower                                                                     |
| deepcopy                   | 240 us                                                                         | 256 us: 1.06x slower                                                                     |
| xml_etree_process          | 47.1 ms                                                                        | 50.2 ms: 1.06x slower                                                                    |
| regex_compile              | 103 ms                                                                         | 110 ms: 1.07x slower                                                                     |
| deltablue                  | 2.56 ms                                                                        | 2.75 ms: 1.07x slower                                                                    |
| unpickle_pure_python       | 168 us                                                                         | 181 us: 1.07x slower                                                                     |
| meteor_contest             | 77.5 ms                                                                        | 83.2 ms: 1.07x slower                                                                    |
| generators                 | 25.7 ms                                                                        | 27.7 ms: 1.08x slower                                                                    |
| spectral_norm              | 75.6 ms                                                                        | 81.6 ms: 1.08x slower                                                                    |
| genshi_text                | 21.7 ms                                                                        | 23.5 ms: 1.09x slower                                                                    |
| tomli_loads                | 1.76 sec                                                                       | 1.91 sec: 1.09x slower                                                                   |
| hexiom                     | 4.92 ms                                                                        | 5.36 ms: 1.09x slower                                                                    |
| pickle_pure_python         | 235 us                                                                         | 257 us: 1.09x slower                                                                     |
| pyflate                    | 333 ms                                                                         | 364 ms: 1.09x slower                                                                     |
| richards                   | 35.0 ms                                                                        | 38.3 ms: 1.10x slower                                                                    |
| comprehensions             | 13.0 us                                                                        | 14.3 us: 1.10x slower                                                                    |
| scimark_monte_carlo        | 50.7 ms                                                                        | 55.8 ms: 1.10x slower                                                                    |
| richards_super             | 39.4 ms                                                                        | 43.3 ms: 1.10x slower                                                                    |
| async_generators           | 282 ms                                                                         | 311 ms: 1.10x slower                                                                     |
| typing_runtime_protocols   | 137 us                                                                         | 151 us: 1.10x slower                                                                     |
| go                         | 111 ms                                                                         | 125 ms: 1.12x slower                                                                     |
| deepcopy_memo              | 20.5 us                                                                        | 23.4 us: 1.14x slower                                                                    |
| Geometric mean             | (ref)                                                                          | 1.03x slower                                                                             |

Benchmark hidden because not significant (15): asyncio_tcp, scimark_lu, xml_etree_parse, json, scimark_sor, json_dumps, django_template, coverage, bench_mp_pool, python_startup, tornado_http, regex_effbot, bench_thread_pool, pylint, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown