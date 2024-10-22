# Results vs. base

- fork: savannahostrowski
- ref: jit_mem_invalidate_3
- machine: linux-x86_64
- commit hash: e6fcb4b
- commit date: 2024-08-20
- overall geometric mean: 1.00x faster
- HPT reliability: 73.30%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 279 ms                                                                | 280 ms: 1.00x slower                                                             |
| docutils       | 3.01 sec                                                              | 2.97 sec: 1.01x faster                                                           |
| html5lib       | 67.2 ms                                                               | 66.2 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|--------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| coroutines         | 23.4 ms                                                               | 22.8 ms: 1.03x faster                                                            |
| asyncio_websockets | 558 ms                                                                | 554 ms: 1.01x faster                                                             |
| asyncio_tcp        | 499 ms                                                                | 496 ms: 1.00x faster                                                             |
| asyncio_tcp_ssl    | 1.80 sec                                                              | 1.80 sec: 1.00x faster                                                           |
| async_generators   | 452 ms                                                                | 463 ms: 1.03x slower                                                             |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                                     |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io, async_tree_none, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                                             |
| float          | 70.7 ms                                                               | 72.1 ms: 1.02x slower                                                            |
| nbody          | 80.0 ms                                                               | 81.7 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.75 ms                                                               | 3.64 ms: 1.03x faster                                                            |
| regex_v8       | 24.5 ms                                                               | 24.2 ms: 1.01x faster                                                            |
| regex_dna      | 221 ms                                                                | 219 ms: 1.01x faster                                                             |
| regex_compile  | 142 ms                                                                | 143 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.93 sec                                                              | 1.89 sec: 1.02x faster                                                           |
| json_dumps           | 10.4 ms                                                               | 10.3 ms: 1.02x faster                                                            |
| json_loads           | 28.6 us                                                               | 28.4 us: 1.01x faster                                                            |
| xml_etree_iterparse  | 98.4 ms                                                               | 98.9 ms: 1.00x slower                                                            |
| unpickle_pure_python | 212 us                                                                | 213 us: 1.01x slower                                                             |
| xml_etree_generate   | 81.6 ms                                                               | 82.4 ms: 1.01x slower                                                            |
| xml_etree_process    | 57.5 ms                                                               | 59.1 ms: 1.03x slower                                                            |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                     |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 7.12 ms                                                               | 7.15 ms: 1.00x slower                                                            |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.01x slower                                                            |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.8 ms                                                               | 36.0 ms: 1.02x faster                                                            |
| mako            | 9.98 ms                                                               | 10.0 ms: 1.01x slower                                                            |
| genshi_xml      | 59.9 ms                                                               | 60.9 ms: 1.02x slower                                                            |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                                     |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| spectral_norm            | 102 ms                                                                | 97.4 ms: 1.05x faster                                                            |
| regex_effbot             | 3.75 ms                                                               | 3.64 ms: 1.03x faster                                                            |
| pyflate                  | 445 ms                                                                | 432 ms: 1.03x faster                                                             |
| coroutines               | 23.4 ms                                                               | 22.8 ms: 1.03x faster                                                            |
| pprint_pformat           | 1.54 sec                                                              | 1.51 sec: 1.02x faster                                                           |
| tomli_loads              | 1.93 sec                                                              | 1.89 sec: 1.02x faster                                                           |
| django_template          | 36.8 ms                                                               | 36.0 ms: 1.02x faster                                                            |
| scimark_monte_carlo      | 63.6 ms                                                               | 62.5 ms: 1.02x faster                                                            |
| create_gc_cycles         | 1.75 ms                                                               | 1.72 ms: 1.02x faster                                                            |
| coverage                 | 87.5 ms                                                               | 86.0 ms: 1.02x faster                                                            |
| pprint_safe_repr         | 743 ms                                                                | 730 ms: 1.02x faster                                                             |
| typing_runtime_protocols | 174 us                                                                | 171 us: 1.02x faster                                                             |
| crypto_pyaes             | 66.4 ms                                                               | 65.3 ms: 1.02x faster                                                            |
| json_dumps               | 10.4 ms                                                               | 10.3 ms: 1.02x faster                                                            |
| deepcopy_memo            | 27.0 us                                                               | 26.6 us: 1.02x faster                                                            |
| sympy_sum                | 175 ms                                                                | 173 ms: 1.02x faster                                                             |
| html5lib                 | 67.2 ms                                                               | 66.2 ms: 1.02x faster                                                            |
| logging_silent           | 101 ns                                                                | 100.0 ns: 1.01x faster                                                           |
| docutils                 | 3.01 sec                                                              | 2.97 sec: 1.01x faster                                                           |
| regex_v8                 | 24.5 ms                                                               | 24.2 ms: 1.01x faster                                                            |
| meteor_contest           | 107 ms                                                                | 106 ms: 1.01x faster                                                             |
| richards                 | 39.4 ms                                                               | 39.0 ms: 1.01x faster                                                            |
| regex_dna                | 221 ms                                                                | 219 ms: 1.01x faster                                                             |
| scimark_fft              | 308 ms                                                                | 306 ms: 1.01x faster                                                             |
| sqlglot_normalize        | 113 ms                                                                | 112 ms: 1.01x faster                                                             |
| pathlib                  | 16.1 ms                                                               | 16.0 ms: 1.01x faster                                                            |
| asyncio_websockets       | 558 ms                                                                | 554 ms: 1.01x faster                                                             |
| sympy_integrate          | 22.9 ms                                                               | 22.8 ms: 1.01x faster                                                            |
| json_loads               | 28.6 us                                                               | 28.4 us: 1.01x faster                                                            |
| asyncio_tcp              | 499 ms                                                                | 496 ms: 1.00x faster                                                             |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.80 sec: 1.00x faster                                                           |
| gc_traversal             | 3.67 ms                                                               | 3.67 ms: 1.00x faster                                                            |
| pidigits                 | 185 ms                                                                | 186 ms: 1.00x slower                                                             |
| 2to3                     | 279 ms                                                                | 280 ms: 1.00x slower                                                             |
| sympy_expand             | 506 ms                                                                | 508 ms: 1.00x slower                                                             |
| python_startup_no_site   | 7.12 ms                                                               | 7.15 ms: 1.00x slower                                                            |
| xml_etree_iterparse      | 98.4 ms                                                               | 98.9 ms: 1.00x slower                                                            |
| scimark_sor              | 114 ms                                                                | 114 ms: 1.00x slower                                                             |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.01x slower                                                            |
| mako                     | 9.98 ms                                                               | 10.0 ms: 1.01x slower                                                            |
| hexiom                   | 6.81 ms                                                               | 6.84 ms: 1.01x slower                                                            |
| regex_compile            | 142 ms                                                                | 143 ms: 1.01x slower                                                             |
| unpickle_pure_python     | 212 us                                                                | 213 us: 1.01x slower                                                             |
| deepcopy_reduce          | 2.64 us                                                               | 2.66 us: 1.01x slower                                                            |
| xml_etree_generate       | 81.6 ms                                                               | 82.4 ms: 1.01x slower                                                            |
| telco                    | 7.76 ms                                                               | 7.84 ms: 1.01x slower                                                            |
| richards_super           | 44.7 ms                                                               | 45.1 ms: 1.01x slower                                                            |
| deepcopy                 | 263 us                                                                | 266 us: 1.01x slower                                                             |
| raytrace                 | 264 ms                                                                | 267 ms: 1.01x slower                                                             |
| nqueens                  | 85.2 ms                                                               | 86.3 ms: 1.01x slower                                                            |
| json                     | 5.32 ms                                                               | 5.40 ms: 1.01x slower                                                            |
| genshi_xml               | 59.9 ms                                                               | 60.9 ms: 1.02x slower                                                            |
| pycparser                | 1.20 sec                                                              | 1.22 sec: 1.02x slower                                                           |
| float                    | 70.7 ms                                                               | 72.1 ms: 1.02x slower                                                            |
| deltablue                | 3.11 ms                                                               | 3.18 ms: 1.02x slower                                                            |
| nbody                    | 80.0 ms                                                               | 81.7 ms: 1.02x slower                                                            |
| mdp                      | 2.54 sec                                                              | 2.60 sec: 1.02x slower                                                           |
| async_generators         | 452 ms                                                                | 463 ms: 1.03x slower                                                             |
| generators               | 32.6 ms                                                               | 33.5 ms: 1.03x slower                                                            |
| xml_etree_process        | 57.5 ms                                                               | 59.1 ms: 1.03x slower                                                            |
| scimark_sparse_mat_mult  | 4.31 ms                                                               | 4.50 ms: 1.05x slower                                                            |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                                     |

Benchmark hidden because not significant (28): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io, thrift, logging_simple, sympy_str, pylint, chaos, fannkuch, bench_mp_pool, sqlglot_optimize, bpe_tokeniser, bench_thread_pool, xml_etree_parse, pickle_pure_python, logging_format, comprehensions, scimark_lu, go, tornado_http, async_tree_none, sqlglot_parse, sqlglot_transpile, async_tree_none_tg, async_tree_memoization_tg, genshi_text, async_tree_io_tg

# HPT report

- Reliability score: 73.30% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x