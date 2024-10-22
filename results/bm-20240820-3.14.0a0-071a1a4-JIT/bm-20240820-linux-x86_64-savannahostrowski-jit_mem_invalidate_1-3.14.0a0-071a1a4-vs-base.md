# Results vs. base

- fork: savannahostrowski
- ref: jit_mem_invalidate_1
- machine: linux-x86_64
- commit hash: 071a1a4
- commit date: 2024-08-20
- overall geometric mean: 1.00x faster
- HPT reliability: 87.18%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| docutils       | 3.01 sec                                                              | 2.97 sec: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                     |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| coroutines       | 23.4 ms                                                               | 23.0 ms: 1.02x faster                                                            |
| async_tree_none  | 323 ms                                                                | 321 ms: 1.01x faster                                                             |
| asyncio_tcp      | 499 ms                                                                | 495 ms: 1.01x faster                                                             |
| asyncio_tcp_ssl  | 1.80 sec                                                              | 1.79 sec: 1.01x faster                                                           |
| async_generators | 452 ms                                                                | 456 ms: 1.01x slower                                                             |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                                     |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_memoization, async_tree_none_tg, async_tree_io_tg, asyncio_websockets, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                                             |
| float          | 70.7 ms                                                               | 72.1 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.75 ms                                                               | 3.56 ms: 1.05x faster                                                            |
| regex_dna      | 221 ms                                                                | 218 ms: 1.01x faster                                                             |
| regex_compile  | 142 ms                                                                | 141 ms: 1.01x faster                                                             |
| regex_v8       | 24.5 ms                                                               | 24.4 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|--------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads        | 1.93 sec                                                              | 1.88 sec: 1.03x faster                                                           |
| xml_etree_process  | 57.5 ms                                                               | 58.0 ms: 1.01x slower                                                            |
| xml_etree_generate | 81.6 ms                                                               | 82.6 ms: 1.01x slower                                                            |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                                     |

Benchmark hidden because not significant (6): unpickle_pure_python, json_dumps, xml_etree_iterparse, pickle_pure_python, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 7.12 ms                                                               | 7.13 ms: 1.00x slower                                                            |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                            |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.8 ms                                                               | 36.2 ms: 1.02x faster                                                            |
| genshi_text     | 26.6 ms                                                               | 26.2 ms: 1.02x faster                                                            |
| mako            | 9.98 ms                                                               | 9.88 ms: 1.01x faster                                                            |
| genshi_xml      | 59.9 ms                                                               | 62.0 ms: 1.03x slower                                                            |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot             | 3.75 ms                                                               | 3.56 ms: 1.05x faster                                                            |
| pprint_pformat           | 1.54 sec                                                              | 1.50 sec: 1.03x faster                                                           |
| logging_silent           | 101 ns                                                                | 98.5 ns: 1.03x faster                                                            |
| tomli_loads              | 1.93 sec                                                              | 1.88 sec: 1.03x faster                                                           |
| deepcopy_memo            | 27.0 us                                                               | 26.3 us: 1.03x faster                                                            |
| pycparser                | 1.20 sec                                                              | 1.17 sec: 1.03x faster                                                           |
| pyflate                  | 445 ms                                                                | 434 ms: 1.03x faster                                                             |
| scimark_monte_carlo      | 63.6 ms                                                               | 62.1 ms: 1.03x faster                                                            |
| spectral_norm            | 102 ms                                                                | 100 ms: 1.02x faster                                                             |
| django_template          | 36.8 ms                                                               | 36.2 ms: 1.02x faster                                                            |
| coverage                 | 87.5 ms                                                               | 86.0 ms: 1.02x faster                                                            |
| coroutines               | 23.4 ms                                                               | 23.0 ms: 1.02x faster                                                            |
| bpe_tokeniser            | 4.59 sec                                                              | 4.52 sec: 1.02x faster                                                           |
| genshi_text              | 26.6 ms                                                               | 26.2 ms: 1.02x faster                                                            |
| typing_runtime_protocols | 174 us                                                                | 171 us: 1.02x faster                                                             |
| regex_dna                | 221 ms                                                                | 218 ms: 1.01x faster                                                             |
| meteor_contest           | 107 ms                                                                | 106 ms: 1.01x faster                                                             |
| thrift                   | 797 us                                                                | 785 us: 1.01x faster                                                             |
| docutils                 | 3.01 sec                                                              | 2.97 sec: 1.01x faster                                                           |
| crypto_pyaes             | 66.4 ms                                                               | 65.7 ms: 1.01x faster                                                            |
| logging_simple           | 5.47 us                                                               | 5.41 us: 1.01x faster                                                            |
| mako                     | 9.98 ms                                                               | 9.88 ms: 1.01x faster                                                            |
| richards                 | 39.4 ms                                                               | 39.1 ms: 1.01x faster                                                            |
| create_gc_cycles         | 1.75 ms                                                               | 1.73 ms: 1.01x faster                                                            |
| pathlib                  | 16.1 ms                                                               | 16.0 ms: 1.01x faster                                                            |
| async_tree_none          | 323 ms                                                                | 321 ms: 1.01x faster                                                             |
| asyncio_tcp              | 499 ms                                                                | 495 ms: 1.01x faster                                                             |
| regex_compile            | 142 ms                                                                | 141 ms: 1.01x faster                                                             |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.79 sec: 1.01x faster                                                           |
| sqlglot_transpile        | 1.68 ms                                                               | 1.67 ms: 1.00x faster                                                            |
| regex_v8                 | 24.5 ms                                                               | 24.4 ms: 1.00x faster                                                            |
| bench_thread_pool        | 817 us                                                                | 816 us: 1.00x faster                                                             |
| python_startup_no_site   | 7.12 ms                                                               | 7.13 ms: 1.00x slower                                                            |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                            |
| pidigits                 | 185 ms                                                                | 186 ms: 1.00x slower                                                             |
| logging_format           | 6.00 us                                                               | 6.03 us: 1.01x slower                                                            |
| comprehensions           | 16.6 us                                                               | 16.7 us: 1.01x slower                                                            |
| sympy_integrate          | 22.9 ms                                                               | 23.1 ms: 1.01x slower                                                            |
| raytrace                 | 264 ms                                                                | 266 ms: 1.01x slower                                                             |
| sympy_expand             | 506 ms                                                                | 510 ms: 1.01x slower                                                             |
| xml_etree_process        | 57.5 ms                                                               | 58.0 ms: 1.01x slower                                                            |
| deltablue                | 3.11 ms                                                               | 3.14 ms: 1.01x slower                                                            |
| sympy_sum                | 175 ms                                                                | 177 ms: 1.01x slower                                                             |
| async_generators         | 452 ms                                                                | 456 ms: 1.01x slower                                                             |
| sympy_str                | 301 ms                                                                | 304 ms: 1.01x slower                                                             |
| scimark_sor              | 114 ms                                                                | 115 ms: 1.01x slower                                                             |
| xml_etree_generate       | 81.6 ms                                                               | 82.6 ms: 1.01x slower                                                            |
| hexiom                   | 6.81 ms                                                               | 6.90 ms: 1.01x slower                                                            |
| richards_super           | 44.7 ms                                                               | 45.4 ms: 1.02x slower                                                            |
| float                    | 70.7 ms                                                               | 72.1 ms: 1.02x slower                                                            |
| gc_traversal             | 3.67 ms                                                               | 3.75 ms: 1.02x slower                                                            |
| fannkuch                 | 369 ms                                                                | 377 ms: 1.02x slower                                                             |
| generators               | 32.6 ms                                                               | 33.6 ms: 1.03x slower                                                            |
| genshi_xml               | 59.9 ms                                                               | 62.0 ms: 1.03x slower                                                            |
| scimark_sparse_mat_mult  | 4.31 ms                                                               | 4.46 ms: 1.04x slower                                                            |
| mdp                      | 2.54 sec                                                              | 2.68 sec: 1.06x slower                                                           |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                                     |

Benchmark hidden because not significant (33): async_tree_cpu_io_mixed, pprint_safe_repr, async_tree_cpu_io_mixed_tg, async_tree_io, deepcopy, pylint, sqlglot_parse, go, scimark_fft, tornado_http, async_tree_memoization, nqueens, bench_mp_pool, unpickle_pure_python, nbody, json_dumps, xml_etree_iterparse, telco, sqlglot_optimize, async_tree_none_tg, html5lib, pickle_pure_python, deepcopy_reduce, async_tree_io_tg, 2to3, scimark_lu, asyncio_websockets, json_loads, sqlglot_normalize, json, xml_etree_parse, async_tree_memoization_tg, chaos

# HPT report

- Reliability score: 87.18% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x