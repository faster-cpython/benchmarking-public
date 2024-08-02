# Results vs. base

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: 55cda27
- commit date: 2024-07-02
- overall geometric mean: 1.02x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 284 ms: 1.05x slower                                             |
| docutils       | 2.86 sec                                                              | 3.03 sec: 1.06x slower                                           |
| html5lib       | 64.2 ms                                                               | 68.4 ms: 1.06x slower                                            |
| tornado_http   | 92.5 ms                                                               | 97.4 ms: 1.05x slower                                            |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_io_tg, async_tree_none_tg, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 81.4 ms                                                               | 79.1 ms: 1.03x faster                                            |
| float          | 70.1 ms                                                               | 69.6 ms: 1.01x faster                                            |
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                             |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.93 ms                                                               | 3.67 ms: 1.07x faster                                            |
| regex_dna      | 229 ms                                                                | 221 ms: 1.04x faster                                             |
| regex_compile  | 135 ms                                                                | 139 ms: 1.02x slower                                             |
| regex_v8       | 25.0 ms                                                               | 26.0 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 217 us                                                                | 204 us: 1.06x faster                                             |
| xml_etree_process    | 57.5 ms                                                               | 57.9 ms: 1.01x slower                                            |
| xml_etree_iterparse  | 98.8 ms                                                               | 99.7 ms: 1.01x slower                                            |
| xml_etree_parse      | 146 ms                                                                | 148 ms: 1.01x slower                                             |
| xml_etree_generate   | 80.8 ms                                                               | 82.0 ms: 1.01x slower                                            |
| json_loads           | 27.4 us                                                               | 27.8 us: 1.02x slower                                            |
| pickle_pure_python   | 293 us                                                                | 300 us: 1.02x slower                                             |
| tomli_loads          | 1.94 sec                                                              | 2.04 sec: 1.05x slower                                           |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                     |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.01x faster                                            |
| python_startup_no_site | 7.12 ms                                                               | 7.08 ms: 1.00x faster                                            |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 25.1 ms                                                               | 24.4 ms: 1.03x faster                                            |
| mako            | 9.76 ms                                                               | 9.61 ms: 1.02x faster                                            |
| django_template | 35.2 ms                                                               | 36.9 ms: 1.05x slower                                            |
| genshi_xml      | 55.6 ms                                                               | 62.7 ms: 1.13x slower                                            |
| Geometric mean  | (ref)                                                                 | 1.03x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| logging_silent           | 106 ns                                                                | 97.6 ns: 1.09x faster                                            |
| mdp                      | 2.76 sec                                                              | 2.55 sec: 1.08x faster                                           |
| regex_effbot             | 3.93 ms                                                               | 3.67 ms: 1.07x faster                                            |
| scimark_monte_carlo      | 61.2 ms                                                               | 57.3 ms: 1.07x faster                                            |
| unpickle_pure_python     | 217 us                                                                | 204 us: 1.06x faster                                             |
| regex_dna                | 229 ms                                                                | 221 ms: 1.04x faster                                             |
| coroutines               | 24.0 ms                                                               | 23.2 ms: 1.03x faster                                            |
| genshi_text              | 25.1 ms                                                               | 24.4 ms: 1.03x faster                                            |
| nbody                    | 81.4 ms                                                               | 79.1 ms: 1.03x faster                                            |
| scimark_sparse_mat_mult  | 4.48 ms                                                               | 4.37 ms: 1.03x faster                                            |
| mako                     | 9.76 ms                                                               | 9.61 ms: 1.02x faster                                            |
| scimark_fft              | 309 ms                                                                | 305 ms: 1.01x faster                                             |
| json                     | 5.16 ms                                                               | 5.09 ms: 1.01x faster                                            |
| crypto_pyaes             | 67.7 ms                                                               | 66.8 ms: 1.01x faster                                            |
| deepcopy_memo            | 28.7 us                                                               | 28.4 us: 1.01x faster                                            |
| pathlib                  | 16.1 ms                                                               | 15.9 ms: 1.01x faster                                            |
| float                    | 70.1 ms                                                               | 69.6 ms: 1.01x faster                                            |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.01x faster                                            |
| pyflate                  | 435 ms                                                                | 432 ms: 1.01x faster                                             |
| python_startup_no_site   | 7.12 ms                                                               | 7.08 ms: 1.00x faster                                            |
| create_gc_cycles         | 1.75 ms                                                               | 1.75 ms: 1.00x slower                                            |
| pidigits                 | 185 ms                                                                | 186 ms: 1.00x slower                                             |
| spectral_norm            | 103 ms                                                                | 103 ms: 1.01x slower                                             |
| hexiom                   | 6.54 ms                                                               | 6.58 ms: 1.01x slower                                            |
| xml_etree_process        | 57.5 ms                                                               | 57.9 ms: 1.01x slower                                            |
| meteor_contest           | 106 ms                                                                | 107 ms: 1.01x slower                                             |
| sqlglot_parse            | 1.28 ms                                                               | 1.29 ms: 1.01x slower                                            |
| bench_thread_pool        | 828 us                                                                | 836 us: 1.01x slower                                             |
| xml_etree_iterparse      | 98.8 ms                                                               | 99.7 ms: 1.01x slower                                            |
| async_generators         | 454 ms                                                                | 459 ms: 1.01x slower                                             |
| xml_etree_parse          | 146 ms                                                                | 148 ms: 1.01x slower                                             |
| asyncio_tcp              | 500 ms                                                                | 507 ms: 1.01x slower                                             |
| xml_etree_generate       | 80.8 ms                                                               | 82.0 ms: 1.01x slower                                            |
| dask                     | 363 ms                                                                | 369 ms: 1.01x slower                                             |
| logging_simple           | 5.47 us                                                               | 5.55 us: 1.02x slower                                            |
| json_loads               | 27.4 us                                                               | 27.8 us: 1.02x slower                                            |
| telco                    | 7.92 ms                                                               | 8.07 ms: 1.02x slower                                            |
| raytrace                 | 265 ms                                                                | 270 ms: 1.02x slower                                             |
| deepcopy                 | 268 us                                                                | 274 us: 1.02x slower                                             |
| typing_runtime_protocols | 169 us                                                                | 172 us: 1.02x slower                                             |
| go                       | 141 ms                                                                | 144 ms: 1.02x slower                                             |
| logging_format           | 6.03 us                                                               | 6.17 us: 1.02x slower                                            |
| regex_compile            | 135 ms                                                                | 139 ms: 1.02x slower                                             |
| pickle_pure_python       | 293 us                                                                | 300 us: 1.02x slower                                             |
| pprint_safe_repr         | 724 ms                                                                | 744 ms: 1.03x slower                                             |
| gc_traversal             | 3.70 ms                                                               | 3.81 ms: 1.03x slower                                            |
| chaos                    | 58.4 ms                                                               | 60.5 ms: 1.04x slower                                            |
| sqlglot_transpile        | 1.59 ms                                                               | 1.65 ms: 1.04x slower                                            |
| pycparser                | 1.16 sec                                                              | 1.21 sec: 1.04x slower                                           |
| sqlglot_optimize         | 55.2 ms                                                               | 57.5 ms: 1.04x slower                                            |
| regex_v8                 | 25.0 ms                                                               | 26.0 ms: 1.04x slower                                            |
| sympy_expand             | 496 ms                                                                | 517 ms: 1.04x slower                                             |
| 2to3                     | 272 ms                                                                | 284 ms: 1.05x slower                                             |
| django_template          | 35.2 ms                                                               | 36.9 ms: 1.05x slower                                            |
| tomli_loads              | 1.94 sec                                                              | 2.04 sec: 1.05x slower                                           |
| tornado_http             | 92.5 ms                                                               | 97.4 ms: 1.05x slower                                            |
| docutils                 | 2.86 sec                                                              | 3.03 sec: 1.06x slower                                           |
| sympy_str                | 293 ms                                                                | 310 ms: 1.06x slower                                             |
| sympy_integrate          | 21.8 ms                                                               | 23.2 ms: 1.06x slower                                            |
| html5lib                 | 64.2 ms                                                               | 68.4 ms: 1.06x slower                                            |
| richards_super           | 47.0 ms                                                               | 50.1 ms: 1.07x slower                                            |
| dulwich_log              | 67.5 ms                                                               | 72.3 ms: 1.07x slower                                            |
| sqlglot_normalize        | 111 ms                                                                | 119 ms: 1.07x slower                                             |
| richards                 | 40.9 ms                                                               | 44.2 ms: 1.08x slower                                            |
| pprint_pformat           | 1.47 sec                                                              | 1.59 sec: 1.08x slower                                           |
| sympy_sum                | 166 ms                                                                | 179 ms: 1.08x slower                                             |
| genshi_xml               | 55.6 ms                                                               | 62.7 ms: 1.13x slower                                            |
| pylint                   | 341 ms                                                                | 398 ms: 1.17x slower                                             |
| deltablue                | 3.51 ms                                                               | 4.10 ms: 1.17x slower                                            |
| generators               | 29.6 ms                                                               | 51.2 ms: 1.73x slower                                            |
| Geometric mean           | (ref)                                                                 | 1.02x slower                                                     |

Benchmark hidden because not significant (21): async_tree_io, async_tree_io_tg, async_tree_none_tg, async_tree_memoization, async_tree_none, fannkuch, async_tree_cpu_io_mixed, bench_mp_pool, asyncio_tcp_ssl, thrift, async_tree_cpu_io_mixed_tg, scimark_lu, coverage, asyncio_websockets, bpe_tokeniser, scimark_sor, comprehensions, json_dumps, async_tree_memoization_tg, deepcopy_reduce, nqueens

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x