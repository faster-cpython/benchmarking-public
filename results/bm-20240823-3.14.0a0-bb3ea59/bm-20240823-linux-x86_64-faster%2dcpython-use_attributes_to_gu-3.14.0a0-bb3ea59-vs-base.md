# Results vs. base

- fork: faster-cpython
- ref: use_attributes_to_gu
- machine: linux-x86_64
- commit hash: bb3ea59
- commit date: 2024-08-23
- overall geometric mean: 1.00x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                | 256 ms: 1.01x slower                                                            |
| docutils       | 2.70 sec                                                              | 2.71 sec: 1.01x slower                                                          |
| tornado_http   | 90.4 ms                                                               | 89.6 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| asyncio_tcp      | 482 ms                                                                | 477 ms: 1.01x faster                                                            |
| async_tree_io    | 930 ms                                                                | 932 ms: 1.00x slower                                                            |
| async_generators | 433 ms                                                                | 437 ms: 1.01x slower                                                            |
| coroutines       | 22.8 ms                                                               | 23.4 ms: 1.02x slower                                                           |
| Geometric mean   | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, asyncio_websockets, asyncio_tcp_ssl, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg, async_tree_none, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                | 186 ms: 1.00x faster                                                            |
| float          | 77.3 ms                                                               | 78.4 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.63 ms                                                               | 3.68 ms: 1.01x slower                                                           |
| regex_dna      | 220 ms                                                                | 223 ms: 1.01x slower                                                            |
| regex_v8       | 24.5 ms                                                               | 26.1 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 302 us                                                                | 299 us: 1.01x faster                                                            |
| xml_etree_generate   | 84.5 ms                                                               | 84.9 ms: 1.01x slower                                                           |
| xml_etree_process    | 58.4 ms                                                               | 58.7 ms: 1.01x slower                                                           |
| xml_etree_iterparse  | 105 ms                                                                | 106 ms: 1.01x slower                                                            |
| tomli_loads          | 2.07 sec                                                              | 2.10 sec: 1.01x slower                                                          |
| json_loads           | 28.3 us                                                               | 28.7 us: 1.01x slower                                                           |
| json_dumps           | 10.3 ms                                                               | 10.5 ms: 1.01x slower                                                           |
| unpickle_pure_python | 212 us                                                                | 215 us: 1.01x slower                                                            |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.07 ms                                                               | 7.10 ms: 1.00x slower                                                           |
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                               | 21.9 ms: 1.03x faster                                                           |
| django_template | 34.1 ms                                                               | 33.5 ms: 1.02x faster                                                           |
| genshi_xml      | 49.8 ms                                                               | 49.2 ms: 1.01x faster                                                           |
| mako            | 11.3 ms                                                               | 11.3 ms: 1.00x faster                                                           |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20240823-linux-x86_64-python-0b0f7befaddb2b5eff28-3.14.0a0-0b0f7be | bm-20240823-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-bb3ea59 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| go                       | 161 ms                                                                | 118 ms: 1.36x faster                                                            |
| genshi_text              | 22.6 ms                                                               | 21.9 ms: 1.03x faster                                                           |
| mdp                      | 2.58 sec                                                              | 2.52 sec: 1.03x faster                                                          |
| crypto_pyaes             | 71.9 ms                                                               | 70.7 ms: 1.02x faster                                                           |
| django_template          | 34.1 ms                                                               | 33.5 ms: 1.02x faster                                                           |
| richards                 | 46.1 ms                                                               | 45.4 ms: 1.02x faster                                                           |
| richards_super           | 52.1 ms                                                               | 51.3 ms: 1.02x faster                                                           |
| thrift                   | 777 us                                                                | 765 us: 1.02x faster                                                            |
| genshi_xml               | 49.8 ms                                                               | 49.2 ms: 1.01x faster                                                           |
| logging_format           | 6.17 us                                                               | 6.10 us: 1.01x faster                                                           |
| asyncio_tcp              | 482 ms                                                                | 477 ms: 1.01x faster                                                            |
| pickle_pure_python       | 302 us                                                                | 299 us: 1.01x faster                                                            |
| tornado_http             | 90.4 ms                                                               | 89.6 ms: 1.01x faster                                                           |
| generators               | 27.9 ms                                                               | 27.8 ms: 1.01x faster                                                           |
| sqlglot_normalize        | 108 ms                                                                | 107 ms: 1.00x faster                                                            |
| mako                     | 11.3 ms                                                               | 11.3 ms: 1.00x faster                                                           |
| pidigits                 | 186 ms                                                                | 186 ms: 1.00x faster                                                            |
| async_tree_io            | 930 ms                                                                | 932 ms: 1.00x slower                                                            |
| raytrace                 | 260 ms                                                                | 261 ms: 1.00x slower                                                            |
| python_startup_no_site   | 7.07 ms                                                               | 7.10 ms: 1.00x slower                                                           |
| deepcopy                 | 259 us                                                                | 260 us: 1.00x slower                                                            |
| python_startup           | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                           |
| xml_etree_generate       | 84.5 ms                                                               | 84.9 ms: 1.01x slower                                                           |
| xml_etree_process        | 58.4 ms                                                               | 58.7 ms: 1.01x slower                                                           |
| 2to3                     | 254 ms                                                                | 256 ms: 1.01x slower                                                            |
| typing_runtime_protocols | 158 us                                                                | 159 us: 1.01x slower                                                            |
| docutils                 | 2.70 sec                                                              | 2.71 sec: 1.01x slower                                                          |
| pprint_safe_repr         | 722 ms                                                                | 726 ms: 1.01x slower                                                            |
| sqlglot_parse            | 1.28 ms                                                               | 1.29 ms: 1.01x slower                                                           |
| deepcopy_memo            | 29.6 us                                                               | 29.8 us: 1.01x slower                                                           |
| spectral_norm            | 110 ms                                                                | 111 ms: 1.01x slower                                                            |
| scimark_fft              | 358 ms                                                                | 361 ms: 1.01x slower                                                            |
| scimark_lu               | 113 ms                                                                | 113 ms: 1.01x slower                                                            |
| coverage                 | 85.1 ms                                                               | 85.8 ms: 1.01x slower                                                           |
| comprehensions           | 16.3 us                                                               | 16.5 us: 1.01x slower                                                           |
| fannkuch                 | 398 ms                                                                | 402 ms: 1.01x slower                                                            |
| async_generators         | 433 ms                                                                | 437 ms: 1.01x slower                                                            |
| logging_silent           | 101 ns                                                                | 102 ns: 1.01x slower                                                            |
| xml_etree_iterparse      | 105 ms                                                                | 106 ms: 1.01x slower                                                            |
| create_gc_cycles         | 1.75 ms                                                               | 1.77 ms: 1.01x slower                                                           |
| tomli_loads              | 2.07 sec                                                              | 2.10 sec: 1.01x slower                                                          |
| json_loads               | 28.3 us                                                               | 28.7 us: 1.01x slower                                                           |
| json_dumps               | 10.3 ms                                                               | 10.5 ms: 1.01x slower                                                           |
| unpickle_pure_python     | 212 us                                                                | 215 us: 1.01x slower                                                            |
| regex_effbot             | 3.63 ms                                                               | 3.68 ms: 1.01x slower                                                           |
| float                    | 77.3 ms                                                               | 78.4 ms: 1.01x slower                                                           |
| regex_dna                | 220 ms                                                                | 223 ms: 1.01x slower                                                            |
| telco                    | 8.15 ms                                                               | 8.27 ms: 1.01x slower                                                           |
| nqueens                  | 78.8 ms                                                               | 80.4 ms: 1.02x slower                                                           |
| scimark_sparse_mat_mult  | 4.72 ms                                                               | 4.82 ms: 1.02x slower                                                           |
| coroutines               | 22.8 ms                                                               | 23.4 ms: 1.02x slower                                                           |
| pycparser                | 1.15 sec                                                              | 1.18 sec: 1.03x slower                                                          |
| regex_v8                 | 24.5 ms                                                               | 26.1 ms: 1.07x slower                                                           |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (36): nbody, json, pylint, sympy_expand, chaos, scimark_monte_carlo, regex_compile, deepcopy_reduce, async_tree_cpu_io_mixed, bench_thread_pool, hexiom, async_tree_cpu_io_mixed_tg, sqlglot_optimize, sympy_sum, pprint_pformat, bench_mp_pool, sympy_integrate, sqlglot_transpile, asyncio_websockets, asyncio_tcp_ssl, gc_traversal, pathlib, meteor_contest, async_tree_memoization, async_tree_memoization_tg, bpe_tokeniser, pyflate, scimark_sor, logging_simple, async_tree_none_tg, deltablue, sympy_str, async_tree_none, async_tree_io_tg, html5lib, xml_etree_parse

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x