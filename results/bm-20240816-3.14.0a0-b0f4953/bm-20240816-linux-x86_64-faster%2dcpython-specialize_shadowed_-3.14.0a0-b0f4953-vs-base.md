# Results vs. base

- fork: faster-cpython
- ref: specialize_shadowed_
- machine: linux-x86_64
- commit hash: b0f4953
- commit date: 2024-08-16
- overall geometric mean: 1.00x faster
- HPT reliability: 97.61%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240816-linux-x86_64-python-c13e7d98fb8581014a22-3.14.0a0-c13e7d9 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 261 ms                                                                | 254 ms: 1.03x faster                                                            |
| tornado_http   | 91.5 ms                                                               | 90.3 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240816-linux-x86_64-python-c13e7d98fb8581014a22-3.14.0a0-c13e7d9 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines             | 23.4 ms                                                               | 23.1 ms: 1.01x faster                                                           |
| asyncio_tcp_ssl        | 1.78 sec                                                              | 1.79 sec: 1.00x slower                                                          |
| asyncio_websockets     | 556 ms                                                                | 558 ms: 1.00x slower                                                            |
| asyncio_tcp            | 479 ms                                                                | 481 ms: 1.00x slower                                                            |
| async_generators       | 431 ms                                                                | 434 ms: 1.01x slower                                                            |
| async_tree_memoization | 406 ms                                                                | 422 ms: 1.04x slower                                                            |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_none, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240816-linux-x86_64-python-c13e7d98fb8581014a22-3.14.0a0-c13e7d9 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 186 ms: 1.00x faster                                                            |
| float          | 77.7 ms                                                               | 78.9 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240816-linux-x86_64-python-c13e7d98fb8581014a22-3.14.0a0-c13e7d9 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                | 129 ms: 1.01x faster                                                            |
| regex_dna      | 225 ms                                                                | 223 ms: 1.01x faster                                                            |
| regex_effbot   | 3.61 ms                                                               | 3.68 ms: 1.02x slower                                                           |
| regex_v8       | 24.5 ms                                                               | 25.0 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240816-linux-x86_64-python-c13e7d98fb8581014a22-3.14.0a0-c13e7d9 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_generate   | 86.4 ms                                                               | 85.7 ms: 1.01x faster                                                           |
| xml_etree_process    | 59.4 ms                                                               | 58.9 ms: 1.01x faster                                                           |
| pickle_pure_python   | 301 us                                                                | 302 us: 1.00x slower                                                            |
| json_loads           | 28.3 us                                                               | 28.5 us: 1.00x slower                                                           |
| tomli_loads          | 2.09 sec                                                              | 2.10 sec: 1.01x slower                                                          |
| unpickle_pure_python | 213 us                                                                | 218 us: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240816-linux-x86_64-python-c13e7d98fb8581014a22-3.14.0a0-c13e7d9 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.09 ms                                                               | 7.07 ms: 1.00x faster                                                           |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240816-linux-x86_64-python-c13e7d98fb8581014a22-3.14.0a0-c13e7d9 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text    | 23.6 ms                                                               | 22.2 ms: 1.06x faster                                                           |
| genshi_xml     | 51.6 ms                                                               | 49.3 ms: 1.05x faster                                                           |
| mako           | 11.2 ms                                                               | 11.3 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240816-linux-x86_64-python-c13e7d98fb8581014a22-3.14.0a0-c13e7d9 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text              | 23.6 ms                                                               | 22.2 ms: 1.06x faster                                                           |
| genshi_xml               | 51.6 ms                                                               | 49.3 ms: 1.05x faster                                                           |
| typing_runtime_protocols | 165 us                                                                | 159 us: 1.04x faster                                                            |
| fannkuch                 | 418 ms                                                                | 404 ms: 1.03x faster                                                            |
| meteor_contest           | 109 ms                                                                | 106 ms: 1.03x faster                                                            |
| crypto_pyaes             | 73.7 ms                                                               | 71.5 ms: 1.03x faster                                                           |
| 2to3                     | 261 ms                                                                | 254 ms: 1.03x faster                                                            |
| pprint_safe_repr         | 737 ms                                                                | 724 ms: 1.02x faster                                                            |
| pprint_pformat           | 1.51 sec                                                              | 1.49 sec: 1.02x faster                                                          |
| sympy_str                | 275 ms                                                                | 271 ms: 1.01x faster                                                            |
| thrift                   | 777 us                                                                | 766 us: 1.01x faster                                                            |
| regex_compile            | 130 ms                                                                | 129 ms: 1.01x faster                                                            |
| tornado_http             | 91.5 ms                                                               | 90.3 ms: 1.01x faster                                                           |
| json                     | 5.38 ms                                                               | 5.31 ms: 1.01x faster                                                           |
| coroutines               | 23.4 ms                                                               | 23.1 ms: 1.01x faster                                                           |
| pyflate                  | 475 ms                                                                | 469 ms: 1.01x faster                                                            |
| sympy_sum                | 153 ms                                                                | 151 ms: 1.01x faster                                                            |
| spectral_norm            | 114 ms                                                                | 113 ms: 1.01x faster                                                            |
| regex_dna                | 225 ms                                                                | 223 ms: 1.01x faster                                                            |
| sympy_expand             | 462 ms                                                                | 457 ms: 1.01x faster                                                            |
| scimark_fft              | 365 ms                                                                | 361 ms: 1.01x faster                                                            |
| gc_traversal             | 3.74 ms                                                               | 3.71 ms: 1.01x faster                                                           |
| bench_thread_pool        | 791 us                                                                | 784 us: 1.01x faster                                                            |
| xml_etree_generate       | 86.4 ms                                                               | 85.7 ms: 1.01x faster                                                           |
| xml_etree_process        | 59.4 ms                                                               | 58.9 ms: 1.01x faster                                                           |
| sympy_integrate          | 19.9 ms                                                               | 19.8 ms: 1.01x faster                                                           |
| pathlib                  | 15.7 ms                                                               | 15.6 ms: 1.01x faster                                                           |
| python_startup_no_site   | 7.09 ms                                                               | 7.07 ms: 1.00x faster                                                           |
| pidigits                 | 187 ms                                                                | 186 ms: 1.00x faster                                                            |
| nqueens                  | 79.8 ms                                                               | 79.5 ms: 1.00x faster                                                           |
| create_gc_cycles         | 1.74 ms                                                               | 1.73 ms: 1.00x faster                                                           |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl          | 1.78 sec                                                              | 1.79 sec: 1.00x slower                                                          |
| pickle_pure_python       | 301 us                                                                | 302 us: 1.00x slower                                                            |
| asyncio_websockets       | 556 ms                                                                | 558 ms: 1.00x slower                                                            |
| asyncio_tcp              | 479 ms                                                                | 481 ms: 1.00x slower                                                            |
| json_loads               | 28.3 us                                                               | 28.5 us: 1.00x slower                                                           |
| hexiom                   | 6.21 ms                                                               | 6.24 ms: 1.00x slower                                                           |
| comprehensions           | 16.7 us                                                               | 16.7 us: 1.01x slower                                                           |
| async_generators         | 431 ms                                                                | 434 ms: 1.01x slower                                                            |
| tomli_loads              | 2.09 sec                                                              | 2.10 sec: 1.01x slower                                                          |
| deepcopy_reduce          | 2.68 us                                                               | 2.70 us: 1.01x slower                                                           |
| generators               | 27.9 ms                                                               | 28.0 ms: 1.01x slower                                                           |
| mako                     | 11.2 ms                                                               | 11.3 ms: 1.01x slower                                                           |
| scimark_lu               | 114 ms                                                                | 115 ms: 1.01x slower                                                            |
| go                       | 140 ms                                                                | 142 ms: 1.01x slower                                                            |
| sqlglot_normalize        | 107 ms                                                                | 109 ms: 1.01x slower                                                            |
| sqlglot_parse            | 1.27 ms                                                               | 1.29 ms: 1.02x slower                                                           |
| float                    | 77.7 ms                                                               | 78.9 ms: 1.02x slower                                                           |
| raytrace                 | 255 ms                                                                | 260 ms: 1.02x slower                                                            |
| logging_simple           | 5.46 us                                                               | 5.55 us: 1.02x slower                                                           |
| richards_super           | 51.8 ms                                                               | 52.8 ms: 1.02x slower                                                           |
| deltablue                | 3.16 ms                                                               | 3.22 ms: 1.02x slower                                                           |
| richards                 | 45.6 ms                                                               | 46.5 ms: 1.02x slower                                                           |
| unpickle_pure_python     | 213 us                                                                | 218 us: 1.02x slower                                                            |
| telco                    | 8.16 ms                                                               | 8.33 ms: 1.02x slower                                                           |
| regex_effbot             | 3.61 ms                                                               | 3.68 ms: 1.02x slower                                                           |
| deepcopy_memo            | 29.5 us                                                               | 30.1 us: 1.02x slower                                                           |
| regex_v8                 | 24.5 ms                                                               | 25.0 ms: 1.02x slower                                                           |
| logging_format           | 6.02 us                                                               | 6.18 us: 1.03x slower                                                           |
| async_tree_memoization   | 406 ms                                                                | 422 ms: 1.04x slower                                                            |
| scimark_sor              | 123 ms                                                                | 129 ms: 1.05x slower                                                            |
| logging_silent           | 97.0 ns                                                               | 105 ns: 1.09x slower                                                            |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (26): pylint, xml_etree_parse, mdp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, coverage, scimark_sparse_mat_mult, deepcopy, async_tree_none, django_template, html5lib, nbody, pycparser, docutils, bpe_tokeniser, sqlglot_optimize, bench_mp_pool, xml_etree_iterparse, async_tree_none_tg, json_dumps, chaos, sqlglot_transpile, scimark_monte_carlo, async_tree_memoization_tg, async_tree_io_tg

# HPT report

- Reliability score: 97.61% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x