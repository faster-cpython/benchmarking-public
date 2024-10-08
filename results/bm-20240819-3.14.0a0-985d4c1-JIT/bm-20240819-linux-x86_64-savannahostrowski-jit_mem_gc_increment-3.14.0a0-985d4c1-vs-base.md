# Results vs. base

- fork: savannahostrowski
- ref: jit_mem_gc_increment
- machine: linux-x86_64
- commit hash: 985d4c1
- commit date: 2024-08-19
- overall geometric mean: 1.00x slower
- HPT reliability: 82.08%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 279 ms                                                                | 283 ms: 1.01x slower                                                             |
| docutils       | 3.01 sec                                                              | 2.98 sec: 1.01x faster                                                           |
| html5lib       | 67.2 ms                                                               | 66.8 ms: 1.01x faster                                                            |
| tornado_http   | 93.4 ms                                                               | 93.1 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| coroutines       | 23.4 ms                                                               | 23.0 ms: 1.02x faster                                                            |
| asyncio_tcp      | 499 ms                                                                | 494 ms: 1.01x faster                                                             |
| asyncio_tcp_ssl  | 1.80 sec                                                              | 1.82 sec: 1.01x slower                                                           |
| async_tree_none  | 323 ms                                                                | 326 ms: 1.01x slower                                                             |
| async_generators | 452 ms                                                                | 458 ms: 1.01x slower                                                             |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                                     |

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_io, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 185 ms                                                                | 188 ms: 1.01x slower                                                             |
| float          | 70.7 ms                                                               | 72.0 ms: 1.02x slower                                                            |
| nbody          | 80.0 ms                                                               | 81.8 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                                | 222 ms: 1.00x slower                                                             |
| regex_effbot   | 3.75 ms                                                               | 3.77 ms: 1.00x slower                                                            |
| regex_v8       | 24.5 ms                                                               | 24.8 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                     |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|---------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads         | 1.93 sec                                                              | 1.91 sec: 1.01x faster                                                           |
| pickle_pure_python  | 302 us                                                                | 300 us: 1.01x faster                                                             |
| xml_etree_iterparse | 98.4 ms                                                               | 98.9 ms: 1.01x slower                                                            |
| json_dumps          | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                            |
| json_loads          | 28.6 us                                                               | 28.8 us: 1.01x slower                                                            |
| xml_etree_process   | 57.5 ms                                                               | 59.3 ms: 1.03x slower                                                            |
| xml_etree_generate  | 81.6 ms                                                               | 85.9 ms: 1.05x slower                                                            |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                                     |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 7.12 ms                                                               | 7.14 ms: 1.00x slower                                                            |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                            |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                               | 25.8 ms: 1.03x faster                                                            |
| django_template | 36.8 ms                                                               | 35.9 ms: 1.02x faster                                                            |
| mako            | 9.98 ms                                                               | 9.84 ms: 1.01x faster                                                            |
| genshi_xml      | 59.9 ms                                                               | 61.1 ms: 1.02x slower                                                            |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text              | 26.6 ms                                                               | 25.8 ms: 1.03x faster                                                            |
| gc_traversal             | 3.67 ms                                                               | 3.58 ms: 1.03x faster                                                            |
| django_template          | 36.8 ms                                                               | 35.9 ms: 1.02x faster                                                            |
| create_gc_cycles         | 1.75 ms                                                               | 1.71 ms: 1.02x faster                                                            |
| coverage                 | 87.5 ms                                                               | 85.5 ms: 1.02x faster                                                            |
| pprint_safe_repr         | 743 ms                                                                | 726 ms: 1.02x faster                                                             |
| logging_silent           | 101 ns                                                                | 99.2 ns: 1.02x faster                                                            |
| pprint_pformat           | 1.54 sec                                                              | 1.51 sec: 1.02x faster                                                           |
| deepcopy_memo            | 27.0 us                                                               | 26.5 us: 1.02x faster                                                            |
| coroutines               | 23.4 ms                                                               | 23.0 ms: 1.02x faster                                                            |
| mako                     | 9.98 ms                                                               | 9.84 ms: 1.01x faster                                                            |
| scimark_lu               | 109 ms                                                                | 107 ms: 1.01x faster                                                             |
| typing_runtime_protocols | 174 us                                                                | 172 us: 1.01x faster                                                             |
| scimark_monte_carlo      | 63.6 ms                                                               | 62.8 ms: 1.01x faster                                                            |
| tomli_loads              | 1.93 sec                                                              | 1.91 sec: 1.01x faster                                                           |
| sqlglot_normalize        | 113 ms                                                                | 112 ms: 1.01x faster                                                             |
| docutils                 | 3.01 sec                                                              | 2.98 sec: 1.01x faster                                                           |
| sympy_sum                | 175 ms                                                                | 174 ms: 1.01x faster                                                             |
| asyncio_tcp              | 499 ms                                                                | 494 ms: 1.01x faster                                                             |
| sqlglot_transpile        | 1.68 ms                                                               | 1.66 ms: 1.01x faster                                                            |
| thrift                   | 797 us                                                                | 790 us: 1.01x faster                                                             |
| pickle_pure_python       | 302 us                                                                | 300 us: 1.01x faster                                                             |
| html5lib                 | 67.2 ms                                                               | 66.8 ms: 1.01x faster                                                            |
| meteor_contest           | 107 ms                                                                | 107 ms: 1.01x faster                                                             |
| pyflate                  | 445 ms                                                                | 443 ms: 1.00x faster                                                             |
| tornado_http             | 93.4 ms                                                               | 93.1 ms: 1.00x faster                                                            |
| python_startup_no_site   | 7.12 ms                                                               | 7.14 ms: 1.00x slower                                                            |
| bench_thread_pool        | 817 us                                                                | 819 us: 1.00x slower                                                             |
| richards                 | 39.4 ms                                                               | 39.6 ms: 1.00x slower                                                            |
| regex_dna                | 221 ms                                                                | 222 ms: 1.00x slower                                                             |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                            |
| regex_effbot             | 3.75 ms                                                               | 3.77 ms: 1.00x slower                                                            |
| raytrace                 | 264 ms                                                                | 265 ms: 1.00x slower                                                             |
| sympy_str                | 301 ms                                                                | 302 ms: 1.00x slower                                                             |
| xml_etree_iterparse      | 98.4 ms                                                               | 98.9 ms: 1.01x slower                                                            |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.82 sec: 1.01x slower                                                           |
| richards_super           | 44.7 ms                                                               | 45.0 ms: 1.01x slower                                                            |
| json_dumps               | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                            |
| scimark_fft              | 308 ms                                                                | 311 ms: 1.01x slower                                                             |
| json_loads               | 28.6 us                                                               | 28.8 us: 1.01x slower                                                            |
| sqlglot_optimize         | 57.8 ms                                                               | 58.3 ms: 1.01x slower                                                            |
| async_tree_none          | 323 ms                                                                | 326 ms: 1.01x slower                                                             |
| deltablue                | 3.11 ms                                                               | 3.14 ms: 1.01x slower                                                            |
| nqueens                  | 85.2 ms                                                               | 86.1 ms: 1.01x slower                                                            |
| sympy_expand             | 506 ms                                                                | 511 ms: 1.01x slower                                                             |
| pidigits                 | 185 ms                                                                | 188 ms: 1.01x slower                                                             |
| async_generators         | 452 ms                                                                | 458 ms: 1.01x slower                                                             |
| 2to3                     | 279 ms                                                                | 283 ms: 1.01x slower                                                             |
| regex_v8                 | 24.5 ms                                                               | 24.8 ms: 1.01x slower                                                            |
| logging_format           | 6.00 us                                                               | 6.09 us: 1.01x slower                                                            |
| deepcopy_reduce          | 2.64 us                                                               | 2.68 us: 1.02x slower                                                            |
| comprehensions           | 16.6 us                                                               | 16.8 us: 1.02x slower                                                            |
| fannkuch                 | 369 ms                                                                | 375 ms: 1.02x slower                                                             |
| logging_simple           | 5.47 us                                                               | 5.57 us: 1.02x slower                                                            |
| float                    | 70.7 ms                                                               | 72.0 ms: 1.02x slower                                                            |
| genshi_xml               | 59.9 ms                                                               | 61.1 ms: 1.02x slower                                                            |
| nbody                    | 80.0 ms                                                               | 81.8 ms: 1.02x slower                                                            |
| generators               | 32.6 ms                                                               | 33.4 ms: 1.02x slower                                                            |
| scimark_sor              | 114 ms                                                                | 117 ms: 1.03x slower                                                             |
| xml_etree_process        | 57.5 ms                                                               | 59.3 ms: 1.03x slower                                                            |
| scimark_sparse_mat_mult  | 4.31 ms                                                               | 4.52 ms: 1.05x slower                                                            |
| xml_etree_generate       | 81.6 ms                                                               | 85.9 ms: 1.05x slower                                                            |
| bpe_tokeniser            | 4.59 sec                                                              | 4.86 sec: 1.06x slower                                                           |
| mdp                      | 2.54 sec                                                              | 2.73 sec: 1.08x slower                                                           |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                                     |

Benchmark hidden because not significant (25): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, xml_etree_parse, go, spectral_norm, asyncio_websockets, pylint, async_tree_io, regex_compile, sqlglot_parse, async_tree_none_tg, bench_mp_pool, hexiom, crypto_pyaes, unpickle_pure_python, pathlib, async_tree_memoization_tg, sympy_integrate, pycparser, json, telco, async_tree_io_tg, deepcopy, chaos

# HPT report

- Reliability score: 82.08% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.98x