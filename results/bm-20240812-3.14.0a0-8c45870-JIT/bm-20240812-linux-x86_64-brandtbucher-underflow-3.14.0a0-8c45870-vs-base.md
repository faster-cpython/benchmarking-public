# Results vs. base

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: 8c45870
- commit date: 2024-08-12
- overall geometric mean: 1.01x slower
- HPT reliability: 93.30%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240812-linux-x86_64-python-9621a7d0170bf1ec48bc-3.14.0a0-9621a7d | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 276 ms                                                                | 280 ms: 1.02x slower                                             |
| docutils       | 3.01 sec                                                              | 3.29 sec: 1.09x slower                                           |
| html5lib       | 66.7 ms                                                               | 68.6 ms: 1.03x slower                                            |
| tornado_http   | 94.0 ms                                                               | 96.9 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240812-linux-x86_64-python-9621a7d0170bf1ec48bc-3.14.0a0-9621a7d | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none  | 328 ms                                                                | 324 ms: 1.01x faster                                             |
| async_generators | 455 ms                                                                | 452 ms: 1.01x faster                                             |
| coroutines       | 22.9 ms                                                               | 23.1 ms: 1.01x slower                                            |
| asyncio_tcp      | 504 ms                                                                | 512 ms: 1.02x slower                                             |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                     |

Benchmark hidden because not significant (9): async_tree_memoization, async_tree_none_tg, async_tree_io, async_tree_cpu_io_mixed_tg, asyncio_websockets, asyncio_tcp_ssl, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240812-linux-x86_64-python-9621a7d0170bf1ec48bc-3.14.0a0-9621a7d | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 70.3 ms                                                               | 70.7 ms: 1.01x slower                                            |
| nbody          | 81.6 ms                                                               | 82.3 ms: 1.01x slower                                            |
| pidigits       | 186 ms                                                                | 188 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240812-linux-x86_64-python-9621a7d0170bf1ec48bc-3.14.0a0-9621a7d | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                               | 24.6 ms: 1.06x faster                                            |
| regex_dna      | 218 ms                                                                | 210 ms: 1.04x faster                                             |
| regex_effbot   | 3.76 ms                                                               | 3.68 ms: 1.02x faster                                            |
| regex_compile  | 138 ms                                                                | 146 ms: 1.06x slower                                             |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240812-linux-x86_64-python-9621a7d0170bf1ec48bc-3.14.0a0-9621a7d | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 215 us                                                                | 194 us: 1.11x faster                                             |
| pickle_pure_python   | 308 us                                                                | 304 us: 1.01x faster                                             |
| xml_etree_process    | 56.7 ms                                                               | 56.3 ms: 1.01x faster                                            |
| xml_etree_iterparse  | 98.3 ms                                                               | 98.7 ms: 1.00x slower                                            |
| json_loads           | 27.9 us                                                               | 28.0 us: 1.01x slower                                            |
| tomli_loads          | 1.92 sec                                                              | 2.09 sec: 1.09x slower                                           |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                     |

Benchmark hidden because not significant (3): xml_etree_generate, json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240812-linux-x86_64-python-9621a7d0170bf1ec48bc-3.14.0a0-9621a7d | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 7.18 ms                                                               | 7.17 ms: 1.00x faster                                            |
| python_startup         | 10.6 ms                                                               | 10.6 ms: 1.00x faster                                            |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240812-linux-x86_64-python-9621a7d0170bf1ec48bc-3.14.0a0-9621a7d | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 24.5 ms                                                               | 23.8 ms: 1.03x faster                                            |
| mako            | 9.69 ms                                                               | 9.74 ms: 1.01x slower                                            |
| django_template | 34.9 ms                                                               | 36.8 ms: 1.05x slower                                            |
| genshi_xml      | 55.6 ms                                                               | 63.5 ms: 1.14x slower                                            |
| Geometric mean  | (ref)                                                                 | 1.04x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20240812-linux-x86_64-python-9621a7d0170bf1ec48bc-3.14.0a0-9621a7d | bm-20240812-linux-x86_64-brandtbucher-underflow-3.14.0a0-8c45870 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python     | 215 us                                                                | 194 us: 1.11x faster                                             |
| scimark_monte_carlo      | 63.0 ms                                                               | 58.2 ms: 1.08x faster                                            |
| richards_super           | 46.6 ms                                                               | 43.4 ms: 1.08x faster                                            |
| regex_v8                 | 26.0 ms                                                               | 24.6 ms: 1.06x faster                                            |
| richards                 | 40.3 ms                                                               | 38.4 ms: 1.05x faster                                            |
| regex_dna                | 218 ms                                                                | 210 ms: 1.04x faster                                             |
| gc_traversal             | 3.89 ms                                                               | 3.76 ms: 1.03x faster                                            |
| telco                    | 7.92 ms                                                               | 7.68 ms: 1.03x faster                                            |
| raytrace                 | 273 ms                                                                | 265 ms: 1.03x faster                                             |
| genshi_text              | 24.5 ms                                                               | 23.8 ms: 1.03x faster                                            |
| fannkuch                 | 375 ms                                                                | 367 ms: 1.02x faster                                             |
| scimark_sparse_mat_mult  | 4.42 ms                                                               | 4.32 ms: 1.02x faster                                            |
| nqueens                  | 85.0 ms                                                               | 83.1 ms: 1.02x faster                                            |
| regex_effbot             | 3.76 ms                                                               | 3.68 ms: 1.02x faster                                            |
| coverage                 | 92.6 ms                                                               | 90.9 ms: 1.02x faster                                            |
| pathlib                  | 16.4 ms                                                               | 16.1 ms: 1.02x faster                                            |
| pprint_safe_repr         | 757 ms                                                                | 746 ms: 1.01x faster                                             |
| logging_silent           | 98.3 ns                                                               | 97.0 ns: 1.01x faster                                            |
| pickle_pure_python       | 308 us                                                                | 304 us: 1.01x faster                                             |
| async_tree_none          | 328 ms                                                                | 324 ms: 1.01x faster                                             |
| comprehensions           | 16.7 us                                                               | 16.5 us: 1.01x faster                                            |
| xml_etree_process        | 56.7 ms                                                               | 56.3 ms: 1.01x faster                                            |
| hexiom                   | 6.85 ms                                                               | 6.80 ms: 1.01x faster                                            |
| async_generators         | 455 ms                                                                | 452 ms: 1.01x faster                                             |
| deepcopy_memo            | 26.4 us                                                               | 26.3 us: 1.00x faster                                            |
| scimark_fft              | 308 ms                                                                | 307 ms: 1.00x faster                                             |
| go                       | 146 ms                                                                | 146 ms: 1.00x faster                                             |
| python_startup_no_site   | 7.18 ms                                                               | 7.17 ms: 1.00x faster                                            |
| python_startup           | 10.6 ms                                                               | 10.6 ms: 1.00x faster                                            |
| xml_etree_iterparse      | 98.3 ms                                                               | 98.7 ms: 1.00x slower                                            |
| json_loads               | 27.9 us                                                               | 28.0 us: 1.01x slower                                            |
| float                    | 70.3 ms                                                               | 70.7 ms: 1.01x slower                                            |
| mako                     | 9.69 ms                                                               | 9.74 ms: 1.01x slower                                            |
| typing_runtime_protocols | 170 us                                                                | 171 us: 1.01x slower                                             |
| spectral_norm            | 102 ms                                                                | 103 ms: 1.01x slower                                             |
| nbody                    | 81.6 ms                                                               | 82.3 ms: 1.01x slower                                            |
| coroutines               | 22.9 ms                                                               | 23.1 ms: 1.01x slower                                            |
| deltablue                | 3.14 ms                                                               | 3.17 ms: 1.01x slower                                            |
| pidigits                 | 186 ms                                                                | 188 ms: 1.01x slower                                             |
| meteor_contest           | 105 ms                                                                | 106 ms: 1.01x slower                                             |
| asyncio_tcp              | 504 ms                                                                | 512 ms: 1.02x slower                                             |
| 2to3                     | 276 ms                                                                | 280 ms: 1.02x slower                                             |
| pyflate                  | 434 ms                                                                | 442 ms: 1.02x slower                                             |
| deepcopy_reduce          | 2.63 us                                                               | 2.69 us: 1.02x slower                                            |
| html5lib                 | 66.7 ms                                                               | 68.6 ms: 1.03x slower                                            |
| tornado_http             | 94.0 ms                                                               | 96.9 ms: 1.03x slower                                            |
| logging_simple           | 5.49 us                                                               | 5.68 us: 1.03x slower                                            |
| sqlglot_transpile        | 1.65 ms                                                               | 1.72 ms: 1.04x slower                                            |
| logging_format           | 6.06 us                                                               | 6.31 us: 1.04x slower                                            |
| pycparser                | 1.19 sec                                                              | 1.24 sec: 1.04x slower                                           |
| sqlglot_optimize         | 57.2 ms                                                               | 59.9 ms: 1.05x slower                                            |
| sqlglot_normalize        | 112 ms                                                                | 117 ms: 1.05x slower                                             |
| sympy_expand             | 506 ms                                                                | 531 ms: 1.05x slower                                             |
| django_template          | 34.9 ms                                                               | 36.8 ms: 1.05x slower                                            |
| regex_compile            | 138 ms                                                                | 146 ms: 1.06x slower                                             |
| scimark_sor              | 114 ms                                                                | 121 ms: 1.06x slower                                             |
| sympy_str                | 300 ms                                                                | 318 ms: 1.06x slower                                             |
| sympy_integrate          | 23.0 ms                                                               | 24.4 ms: 1.06x slower                                            |
| sympy_sum                | 174 ms                                                                | 187 ms: 1.07x slower                                             |
| mdp                      | 2.54 sec                                                              | 2.74 sec: 1.08x slower                                           |
| tomli_loads              | 1.92 sec                                                              | 2.09 sec: 1.09x slower                                           |
| docutils                 | 3.01 sec                                                              | 3.29 sec: 1.09x slower                                           |
| pylint                   | 370 ms                                                                | 408 ms: 1.10x slower                                             |
| sqlglot_parse            | 1.30 ms                                                               | 1.44 ms: 1.11x slower                                            |
| genshi_xml               | 55.6 ms                                                               | 63.5 ms: 1.14x slower                                            |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                     |

Benchmark hidden because not significant (24): scimark_lu, pprint_pformat, crypto_pyaes, async_tree_memoization, async_tree_none_tg, async_tree_io, xml_etree_generate, async_tree_cpu_io_mixed_tg, bpe_tokeniser, bench_mp_pool, generators, thrift, create_gc_cycles, asyncio_websockets, bench_thread_pool, asyncio_tcp_ssl, async_tree_cpu_io_mixed, json, async_tree_memoization_tg, json_dumps, xml_etree_parse, async_tree_io_tg, deepcopy, chaos

# HPT report

- Reliability score: 93.30% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x