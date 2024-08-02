# Results vs. base

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: 091375e
- commit date: 2024-07-03
- overall geometric mean: 1.02x slower
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 279 ms: 1.03x slower                                             |
| docutils       | 2.86 sec                                                              | 3.01 sec: 1.05x slower                                           |
| html5lib       | 64.2 ms                                                               | 68.3 ms: 1.06x slower                                            |
| tornado_http   | 92.5 ms                                                               | 97.7 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_io_tg, async_tree_none_tg, async_tree_none, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 81.4 ms                                                               | 79.9 ms: 1.02x faster                                            |
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                             |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                     |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.93 ms                                                               | 3.60 ms: 1.09x faster                                            |
| regex_v8       | 25.0 ms                                                               | 24.3 ms: 1.03x faster                                            |
| regex_dna      | 229 ms                                                                | 230 ms: 1.00x slower                                             |
| regex_compile  | 135 ms                                                                | 138 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 217 us                                                                | 200 us: 1.08x faster                                             |
| json_loads           | 27.4 us                                                               | 27.3 us: 1.00x faster                                            |
| xml_etree_iterparse  | 98.8 ms                                                               | 99.3 ms: 1.01x slower                                            |
| json_dumps           | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                            |
| pickle_pure_python   | 293 us                                                                | 297 us: 1.02x slower                                             |
| tomli_loads          | 1.94 sec                                                              | 2.03 sec: 1.05x slower                                           |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                     |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 7.12 ms                                                               | 7.13 ms: 1.00x slower                                            |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                     |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 25.1 ms                                                               | 24.1 ms: 1.04x faster                                            |
| mako            | 9.76 ms                                                               | 9.86 ms: 1.01x slower                                            |
| django_template | 35.2 ms                                                               | 36.6 ms: 1.04x slower                                            |
| genshi_xml      | 55.6 ms                                                               | 62.6 ms: 1.13x slower                                            |
| Geometric mean  | (ref)                                                                 | 1.03x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240703-linux-x86_64-brandtbucher-underflow-3.14.0a0-091375e |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot             | 3.93 ms                                                               | 3.60 ms: 1.09x faster                                            |
| unpickle_pure_python     | 217 us                                                                | 200 us: 1.08x faster                                             |
| mdp                      | 2.76 sec                                                              | 2.55 sec: 1.08x faster                                           |
| logging_silent           | 106 ns                                                                | 98.4 ns: 1.08x faster                                            |
| scimark_monte_carlo      | 61.2 ms                                                               | 57.4 ms: 1.07x faster                                            |
| scimark_sparse_mat_mult  | 4.48 ms                                                               | 4.30 ms: 1.04x faster                                            |
| genshi_text              | 25.1 ms                                                               | 24.1 ms: 1.04x faster                                            |
| coroutines               | 24.0 ms                                                               | 23.0 ms: 1.04x faster                                            |
| regex_v8                 | 25.0 ms                                                               | 24.3 ms: 1.03x faster                                            |
| nbody                    | 81.4 ms                                                               | 79.9 ms: 1.02x faster                                            |
| pyflate                  | 435 ms                                                                | 427 ms: 1.02x faster                                             |
| crypto_pyaes             | 67.7 ms                                                               | 66.9 ms: 1.01x faster                                            |
| deepcopy_memo            | 28.7 us                                                               | 28.4 us: 1.01x faster                                            |
| scimark_lu               | 126 ms                                                                | 124 ms: 1.01x faster                                             |
| coverage                 | 93.1 ms                                                               | 92.4 ms: 1.01x faster                                            |
| bpe_tokeniser            | 4.81 sec                                                              | 4.78 sec: 1.01x faster                                           |
| json_loads               | 27.4 us                                                               | 27.3 us: 1.00x faster                                            |
| pidigits                 | 185 ms                                                                | 186 ms: 1.00x slower                                             |
| python_startup_no_site   | 7.12 ms                                                               | 7.13 ms: 1.00x slower                                            |
| regex_dna                | 229 ms                                                                | 230 ms: 1.00x slower                                             |
| pathlib                  | 16.1 ms                                                               | 16.2 ms: 1.00x slower                                            |
| xml_etree_iterparse      | 98.8 ms                                                               | 99.3 ms: 1.01x slower                                            |
| json_dumps               | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                            |
| sqlglot_parse            | 1.28 ms                                                               | 1.29 ms: 1.01x slower                                            |
| create_gc_cycles         | 1.75 ms                                                               | 1.76 ms: 1.01x slower                                            |
| hexiom                   | 6.54 ms                                                               | 6.59 ms: 1.01x slower                                            |
| comprehensions           | 16.5 us                                                               | 16.6 us: 1.01x slower                                            |
| scimark_fft              | 309 ms                                                                | 312 ms: 1.01x slower                                             |
| mako                     | 9.76 ms                                                               | 9.86 ms: 1.01x slower                                            |
| go                       | 141 ms                                                                | 143 ms: 1.01x slower                                             |
| bench_thread_pool        | 828 us                                                                | 837 us: 1.01x slower                                             |
| spectral_norm            | 103 ms                                                                | 104 ms: 1.01x slower                                             |
| raytrace                 | 265 ms                                                                | 268 ms: 1.01x slower                                             |
| async_generators         | 454 ms                                                                | 460 ms: 1.01x slower                                             |
| dask                     | 363 ms                                                                | 369 ms: 1.02x slower                                             |
| asyncio_tcp              | 500 ms                                                                | 508 ms: 1.02x slower                                             |
| pickle_pure_python       | 293 us                                                                | 297 us: 1.02x slower                                             |
| typing_runtime_protocols | 169 us                                                                | 172 us: 1.02x slower                                             |
| regex_compile            | 135 ms                                                                | 138 ms: 1.02x slower                                             |
| pprint_safe_repr         | 724 ms                                                                | 739 ms: 1.02x slower                                             |
| deepcopy                 | 268 us                                                                | 274 us: 1.02x slower                                             |
| logging_simple           | 5.47 us                                                               | 5.59 us: 1.02x slower                                            |
| chaos                    | 58.4 ms                                                               | 59.8 ms: 1.02x slower                                            |
| 2to3                     | 272 ms                                                                | 279 ms: 1.03x slower                                             |
| sqlglot_transpile        | 1.59 ms                                                               | 1.64 ms: 1.03x slower                                            |
| gc_traversal             | 3.70 ms                                                               | 3.85 ms: 1.04x slower                                            |
| django_template          | 35.2 ms                                                               | 36.6 ms: 1.04x slower                                            |
| logging_format           | 6.03 us                                                               | 6.27 us: 1.04x slower                                            |
| sympy_expand             | 496 ms                                                                | 517 ms: 1.04x slower                                             |
| sqlglot_optimize         | 55.2 ms                                                               | 57.6 ms: 1.05x slower                                            |
| tomli_loads              | 1.94 sec                                                              | 2.03 sec: 1.05x slower                                           |
| docutils                 | 2.86 sec                                                              | 3.01 sec: 1.05x slower                                           |
| sympy_str                | 293 ms                                                                | 309 ms: 1.06x slower                                             |
| tornado_http             | 92.5 ms                                                               | 97.7 ms: 1.06x slower                                            |
| richards_super           | 47.0 ms                                                               | 49.7 ms: 1.06x slower                                            |
| pprint_pformat           | 1.47 sec                                                              | 1.56 sec: 1.06x slower                                           |
| sympy_integrate          | 21.8 ms                                                               | 23.2 ms: 1.06x slower                                            |
| html5lib                 | 64.2 ms                                                               | 68.3 ms: 1.06x slower                                            |
| dulwich_log              | 67.5 ms                                                               | 71.8 ms: 1.06x slower                                            |
| sqlglot_normalize        | 111 ms                                                                | 119 ms: 1.07x slower                                             |
| sympy_sum                | 166 ms                                                                | 178 ms: 1.08x slower                                             |
| richards                 | 40.9 ms                                                               | 44.6 ms: 1.09x slower                                            |
| genshi_xml               | 55.6 ms                                                               | 62.6 ms: 1.13x slower                                            |
| pylint                   | 341 ms                                                                | 397 ms: 1.16x slower                                             |
| deltablue                | 3.51 ms                                                               | 4.10 ms: 1.17x slower                                            |
| generators               | 29.6 ms                                                               | 48.4 ms: 1.63x slower                                            |
| Geometric mean           | (ref)                                                                 | 1.02x slower                                                     |

Benchmark hidden because not significant (25): async_tree_io, async_tree_io_tg, async_tree_none_tg, deepcopy_reduce, json, nqueens, pycparser, async_tree_none, async_tree_memoization, xml_etree_parse, async_tree_memoization_tg, meteor_contest, xml_etree_process, asyncio_tcp_ssl, bench_mp_pool, python_startup, scimark_sor, xml_etree_generate, float, asyncio_websockets, async_tree_cpu_io_mixed_tg, thrift, fannkuch, async_tree_cpu_io_mixed, telco

# HPT report

- Reliability score: 99.95% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x