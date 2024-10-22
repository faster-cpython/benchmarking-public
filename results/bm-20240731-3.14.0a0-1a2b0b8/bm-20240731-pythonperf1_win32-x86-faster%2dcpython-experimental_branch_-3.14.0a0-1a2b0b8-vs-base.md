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
| 2to3           | 251 ms                                                                         | 258 ms: 1.03x slower                                                                     |
| docutils       | 1.91 sec                                                                       | 1.92 sec: 1.01x slower                                                                   |
| html5lib       | 47.8 ms                                                                        | 49.5 ms: 1.04x slower                                                                    |
| Geometric mean | (ref)                                                                          | 1.02x slower                                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 17.0 sec                                                                       | 16.9 sec: 1.01x faster                                                                   |
| coroutines                 | 17.3 ms                                                                        | 17.4 ms: 1.01x slower                                                                    |
| async_tree_cpu_io_mixed    | 467 ms                                                                         | 474 ms: 1.02x slower                                                                     |
| async_tree_cpu_io_mixed_tg | 454 ms                                                                         | 462 ms: 1.02x slower                                                                     |
| async_tree_io              | 549 ms                                                                         | 559 ms: 1.02x slower                                                                     |
| async_tree_none            | 224 ms                                                                         | 230 ms: 1.02x slower                                                                     |
| async_generators           | 280 ms                                                                         | 311 ms: 1.11x slower                                                                     |
| Geometric mean             | (ref)                                                                          | 1.02x slower                                                                             |

Benchmark hidden because not significant (5): asyncio_tcp, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                                         | 200 ms: 1.01x slower                                                                     |
| float          | 58.2 ms                                                                        | 61.5 ms: 1.06x slower                                                                    |
| nbody          | 88.5 ms                                                                        | 93.6 ms: 1.06x slower                                                                    |
| Geometric mean | (ref)                                                                          | 1.04x slower                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_dna      | 122 ms                                                                         | 119 ms: 1.03x faster                                                                     |
| regex_v8       | 16.3 ms                                                                        | 16.1 ms: 1.01x faster                                                                    |
| regex_compile  | 103 ms                                                                         | 110 ms: 1.06x slower                                                                     |
| Geometric mean | (ref)                                                                          | 1.01x slower                                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 69.2 ms                                                                        | 68.7 ms: 1.01x faster                                                                    |
| xml_etree_parse      | 107 ms                                                                         | 106 ms: 1.01x faster                                                                     |
| json_loads           | 20.0 us                                                                        | 20.2 us: 1.01x slower                                                                    |
| json_dumps           | 7.53 ms                                                                        | 7.63 ms: 1.01x slower                                                                    |
| tomli_loads          | 1.82 sec                                                                       | 1.91 sec: 1.05x slower                                                                   |
| pickle_pure_python   | 244 us                                                                         | 257 us: 1.05x slower                                                                     |
| xml_etree_process    | 47.3 ms                                                                        | 50.2 ms: 1.06x slower                                                                    |
| unpickle_pure_python | 169 us                                                                         | 181 us: 1.07x slower                                                                     |
| Geometric mean       | (ref)                                                                          | 1.03x slower                                                                             |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.7 ms                                                                        | 19.5 ms: 1.01x faster                                                                    |
| Geometric mean         | (ref)                                                                          | 1.00x faster                                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| django_template | 34.7 ms                                                                        | 34.0 ms: 1.02x faster                                                                    |
| mako            | 8.01 ms                                                                        | 8.15 ms: 1.02x slower                                                                    |
| genshi_xml      | 46.4 ms                                                                        | 49.3 ms: 1.06x slower                                                                    |
| genshi_text     | 21.6 ms                                                                        | 23.5 ms: 1.09x slower                                                                    |
| Geometric mean  | (ref)                                                                          | 1.04x slower                                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_dna                  | 122 ms                                                                         | 119 ms: 1.03x faster                                                                     |
| scimark_lu                 | 70.1 ms                                                                        | 68.4 ms: 1.02x faster                                                                    |
| django_template            | 34.7 ms                                                                        | 34.0 ms: 1.02x faster                                                                    |
| logging_format             | 8.87 us                                                                        | 8.72 us: 1.02x faster                                                                    |
| create_gc_cycles           | 758 us                                                                         | 746 us: 1.02x faster                                                                     |
| regex_v8                   | 16.3 ms                                                                        | 16.1 ms: 1.01x faster                                                                    |
| python_startup_no_site     | 19.7 ms                                                                        | 19.5 ms: 1.01x faster                                                                    |
| xml_etree_iterparse        | 69.2 ms                                                                        | 68.7 ms: 1.01x faster                                                                    |
| asyncio_tcp_ssl            | 17.0 sec                                                                       | 16.9 sec: 1.01x faster                                                                   |
| xml_etree_parse            | 107 ms                                                                         | 106 ms: 1.01x faster                                                                     |
| fannkuch                   | 310 ms                                                                         | 311 ms: 1.01x slower                                                                     |
| bench_mp_pool              | 73.4 ms                                                                        | 73.8 ms: 1.01x slower                                                                    |
| docutils                   | 1.91 sec                                                                       | 1.92 sec: 1.01x slower                                                                   |
| coverage                   | 51.8 ms                                                                        | 52.1 ms: 1.01x slower                                                                    |
| coroutines                 | 17.3 ms                                                                        | 17.4 ms: 1.01x slower                                                                    |
| pidigits                   | 199 ms                                                                         | 200 ms: 1.01x slower                                                                     |
| json_loads                 | 20.0 us                                                                        | 20.2 us: 1.01x slower                                                                    |
| telco                      | 6.15 ms                                                                        | 6.21 ms: 1.01x slower                                                                    |
| gc_traversal               | 1.43 ms                                                                        | 1.45 ms: 1.01x slower                                                                    |
| sqlglot_parse              | 1.06 ms                                                                        | 1.07 ms: 1.01x slower                                                                    |
| json_dumps                 | 7.53 ms                                                                        | 7.63 ms: 1.01x slower                                                                    |
| sympy_sum                  | 109 ms                                                                         | 110 ms: 1.01x slower                                                                     |
| async_tree_cpu_io_mixed    | 467 ms                                                                         | 474 ms: 1.02x slower                                                                     |
| mdp                        | 1.67 sec                                                                       | 1.69 sec: 1.02x slower                                                                   |
| async_tree_cpu_io_mixed_tg | 454 ms                                                                         | 462 ms: 1.02x slower                                                                     |
| mako                       | 8.01 ms                                                                        | 8.15 ms: 1.02x slower                                                                    |
| sympy_integrate            | 15.4 ms                                                                        | 15.7 ms: 1.02x slower                                                                    |
| async_tree_io              | 549 ms                                                                         | 559 ms: 1.02x slower                                                                     |
| sqlglot_transpile          | 1.30 ms                                                                        | 1.33 ms: 1.02x slower                                                                    |
| deepcopy_reduce            | 2.55 us                                                                        | 2.60 us: 1.02x slower                                                                    |
| dulwich_log                | 49.4 ms                                                                        | 50.5 ms: 1.02x slower                                                                    |
| async_tree_none            | 224 ms                                                                         | 230 ms: 1.02x slower                                                                     |
| sqlglot_optimize           | 44.0 ms                                                                        | 45.0 ms: 1.02x slower                                                                    |
| sqlglot_normalize          | 230 ms                                                                         | 236 ms: 1.03x slower                                                                     |
| 2to3                       | 251 ms                                                                         | 258 ms: 1.03x slower                                                                     |
| logging_silent             | 74.2 ns                                                                        | 76.2 ns: 1.03x slower                                                                    |
| sympy_expand               | 385 ms                                                                         | 395 ms: 1.03x slower                                                                     |
| chaos                      | 50.5 ms                                                                        | 52.2 ms: 1.03x slower                                                                    |
| scimark_sor                | 94.8 ms                                                                        | 98.0 ms: 1.03x slower                                                                    |
| sympy_str                  | 217 ms                                                                         | 225 ms: 1.03x slower                                                                     |
| raytrace                   | 218 ms                                                                         | 226 ms: 1.04x slower                                                                     |
| html5lib                   | 47.8 ms                                                                        | 49.5 ms: 1.04x slower                                                                    |
| nqueens                    | 73.9 ms                                                                        | 76.8 ms: 1.04x slower                                                                    |
| pycparser                  | 836 ms                                                                         | 873 ms: 1.04x slower                                                                     |
| crypto_pyaes               | 55.9 ms                                                                        | 58.6 ms: 1.05x slower                                                                    |
| thrift                     | 733 us                                                                         | 769 us: 1.05x slower                                                                     |
| tomli_loads                | 1.82 sec                                                                       | 1.91 sec: 1.05x slower                                                                   |
| pprint_pformat             | 1.34 sec                                                                       | 1.41 sec: 1.05x slower                                                                   |
| pprint_safe_repr           | 657 ms                                                                         | 693 ms: 1.05x slower                                                                     |
| pickle_pure_python         | 244 us                                                                         | 257 us: 1.05x slower                                                                     |
| float                      | 58.2 ms                                                                        | 61.5 ms: 1.06x slower                                                                    |
| nbody                      | 88.5 ms                                                                        | 93.6 ms: 1.06x slower                                                                    |
| deepcopy                   | 241 us                                                                         | 256 us: 1.06x slower                                                                     |
| scimark_fft                | 217 ms                                                                         | 230 ms: 1.06x slower                                                                     |
| xml_etree_process          | 47.3 ms                                                                        | 50.2 ms: 1.06x slower                                                                    |
| regex_compile              | 103 ms                                                                         | 110 ms: 1.06x slower                                                                     |
| genshi_xml                 | 46.4 ms                                                                        | 49.3 ms: 1.06x slower                                                                    |
| spectral_norm              | 76.5 ms                                                                        | 81.6 ms: 1.07x slower                                                                    |
| richards                   | 35.8 ms                                                                        | 38.3 ms: 1.07x slower                                                                    |
| unpickle_pure_python       | 169 us                                                                         | 181 us: 1.07x slower                                                                     |
| deltablue                  | 2.57 ms                                                                        | 2.75 ms: 1.07x slower                                                                    |
| hexiom                     | 4.99 ms                                                                        | 5.36 ms: 1.07x slower                                                                    |
| generators                 | 25.7 ms                                                                        | 27.7 ms: 1.07x slower                                                                    |
| richards_super             | 40.2 ms                                                                        | 43.3 ms: 1.08x slower                                                                    |
| meteor_contest             | 76.7 ms                                                                        | 83.2 ms: 1.08x slower                                                                    |
| genshi_text                | 21.6 ms                                                                        | 23.5 ms: 1.09x slower                                                                    |
| comprehensions             | 13.1 us                                                                        | 14.3 us: 1.09x slower                                                                    |
| pyflate                    | 331 ms                                                                         | 364 ms: 1.10x slower                                                                     |
| scimark_monte_carlo        | 50.6 ms                                                                        | 55.8 ms: 1.10x slower                                                                    |
| typing_runtime_protocols   | 137 us                                                                         | 151 us: 1.10x slower                                                                     |
| async_generators           | 280 ms                                                                         | 311 ms: 1.11x slower                                                                     |
| deepcopy_memo              | 21.1 us                                                                        | 23.4 us: 1.11x slower                                                                    |
| go                         | 111 ms                                                                         | 125 ms: 1.13x slower                                                                     |
| Geometric mean             | (ref)                                                                          | 1.03x slower                                                                             |

Benchmark hidden because not significant (15): asyncio_tcp, json, pathlib, scimark_sparse_mat_mult, xml_etree_generate, logging_simple, python_startup, tornado_http, regex_effbot, pylint, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg, bench_thread_pool

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown