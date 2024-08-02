# Results vs. base

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: 2cefb49
- commit date: 2024-07-02
- overall geometric mean: 1.01x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 277 ms: 1.02x slower                                             |
| docutils       | 2.86 sec                                                              | 3.03 sec: 1.06x slower                                           |
| html5lib       | 64.2 ms                                                               | 69.2 ms: 1.08x slower                                            |
| tornado_http   | 92.5 ms                                                               | 97.0 ms: 1.05x slower                                            |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io  | 880 ms                                                                | 853 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                     |

Benchmark hidden because not significant (7): async_tree_none, async_tree_none_tg, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 81.4 ms                                                               | 80.2 ms: 1.02x faster                                            |
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                             |
| float          | 70.1 ms                                                               | 70.6 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.93 ms                                                               | 4.03 ms: 1.03x slower                                            |
| regex_compile  | 135 ms                                                                | 140 ms: 1.03x slower                                             |
| regex_dna      | 229 ms                                                                | 238 ms: 1.04x slower                                             |
| regex_v8       | 25.0 ms                                                               | 26.7 ms: 1.07x slower                                            |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 217 us                                                                | 202 us: 1.07x faster                                             |
| pickle_pure_python   | 293 us                                                                | 296 us: 1.01x slower                                             |
| json_loads           | 27.4 us                                                               | 27.7 us: 1.01x slower                                            |
| json_dumps           | 10.3 ms                                                               | 10.5 ms: 1.02x slower                                            |
| xml_etree_generate   | 80.8 ms                                                               | 82.1 ms: 1.02x slower                                            |
| xml_etree_process    | 57.5 ms                                                               | 59.1 ms: 1.03x slower                                            |
| tomli_loads          | 1.94 sec                                                              | 2.07 sec: 1.07x slower                                           |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                     |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.01x faster                                            |
| python_startup_no_site | 7.12 ms                                                               | 7.08 ms: 1.00x faster                                            |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 25.1 ms                                                               | 24.2 ms: 1.04x faster                                            |
| mako            | 9.76 ms                                                               | 9.85 ms: 1.01x slower                                            |
| django_template | 35.2 ms                                                               | 35.7 ms: 1.01x slower                                            |
| genshi_xml      | 55.6 ms                                                               | 61.8 ms: 1.11x slower                                            |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| logging_silent           | 106 ns                                                                | 97.2 ns: 1.09x faster                                            |
| unpickle_pure_python     | 217 us                                                                | 202 us: 1.07x faster                                             |
| mdp                      | 2.76 sec                                                              | 2.60 sec: 1.06x faster                                           |
| scimark_monte_carlo      | 61.2 ms                                                               | 58.2 ms: 1.05x faster                                            |
| genshi_text              | 25.1 ms                                                               | 24.2 ms: 1.04x faster                                            |
| async_tree_io            | 880 ms                                                                | 853 ms: 1.03x faster                                             |
| coroutines               | 24.0 ms                                                               | 23.3 ms: 1.03x faster                                            |
| deepcopy_reduce          | 2.75 us                                                               | 2.70 us: 1.02x faster                                            |
| pprint_safe_repr         | 724 ms                                                                | 712 ms: 1.02x faster                                             |
| nbody                    | 81.4 ms                                                               | 80.2 ms: 1.02x faster                                            |
| deepcopy_memo            | 28.7 us                                                               | 28.3 us: 1.01x faster                                            |
| scimark_sparse_mat_mult  | 4.48 ms                                                               | 4.45 ms: 1.01x faster                                            |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.01x faster                                            |
| python_startup_no_site   | 7.12 ms                                                               | 7.08 ms: 1.00x faster                                            |
| pathlib                  | 16.1 ms                                                               | 16.0 ms: 1.00x faster                                            |
| comprehensions           | 16.5 us                                                               | 16.4 us: 1.00x faster                                            |
| asyncio_websockets       | 557 ms                                                                | 555 ms: 1.00x faster                                             |
| bpe_tokeniser            | 4.81 sec                                                              | 4.80 sec: 1.00x faster                                           |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.80 sec: 1.00x faster                                           |
| pidigits                 | 185 ms                                                                | 186 ms: 1.00x slower                                             |
| create_gc_cycles         | 1.75 ms                                                               | 1.75 ms: 1.00x slower                                            |
| crypto_pyaes             | 67.7 ms                                                               | 67.9 ms: 1.00x slower                                            |
| raytrace                 | 265 ms                                                                | 266 ms: 1.01x slower                                             |
| float                    | 70.1 ms                                                               | 70.6 ms: 1.01x slower                                            |
| meteor_contest           | 106 ms                                                                | 107 ms: 1.01x slower                                             |
| async_generators         | 454 ms                                                                | 458 ms: 1.01x slower                                             |
| mako                     | 9.76 ms                                                               | 9.85 ms: 1.01x slower                                            |
| go                       | 141 ms                                                                | 143 ms: 1.01x slower                                             |
| nqueens                  | 85.8 ms                                                               | 86.7 ms: 1.01x slower                                            |
| asyncio_tcp              | 500 ms                                                                | 505 ms: 1.01x slower                                             |
| bench_thread_pool        | 828 us                                                                | 837 us: 1.01x slower                                             |
| pickle_pure_python       | 293 us                                                                | 296 us: 1.01x slower                                             |
| sqlglot_optimize         | 55.2 ms                                                               | 55.8 ms: 1.01x slower                                            |
| chaos                    | 58.4 ms                                                               | 59.1 ms: 1.01x slower                                            |
| scimark_lu               | 126 ms                                                                | 127 ms: 1.01x slower                                             |
| spectral_norm            | 103 ms                                                                | 104 ms: 1.01x slower                                             |
| json_loads               | 27.4 us                                                               | 27.7 us: 1.01x slower                                            |
| sqlglot_parse            | 1.28 ms                                                               | 1.29 ms: 1.01x slower                                            |
| django_template          | 35.2 ms                                                               | 35.7 ms: 1.01x slower                                            |
| json_dumps               | 10.3 ms                                                               | 10.5 ms: 1.02x slower                                            |
| xml_etree_generate       | 80.8 ms                                                               | 82.1 ms: 1.02x slower                                            |
| sqlglot_transpile        | 1.59 ms                                                               | 1.62 ms: 1.02x slower                                            |
| logging_simple           | 5.47 us                                                               | 5.56 us: 1.02x slower                                            |
| typing_runtime_protocols | 169 us                                                                | 172 us: 1.02x slower                                             |
| gc_traversal             | 3.70 ms                                                               | 3.77 ms: 1.02x slower                                            |
| richards_super           | 47.0 ms                                                               | 47.9 ms: 1.02x slower                                            |
| 2to3                     | 272 ms                                                                | 277 ms: 1.02x slower                                             |
| pyflate                  | 435 ms                                                                | 444 ms: 1.02x slower                                             |
| hexiom                   | 6.54 ms                                                               | 6.67 ms: 1.02x slower                                            |
| scimark_fft              | 309 ms                                                                | 316 ms: 1.02x slower                                             |
| sympy_sum                | 166 ms                                                                | 169 ms: 1.02x slower                                             |
| logging_format           | 6.03 us                                                               | 6.17 us: 1.02x slower                                            |
| regex_effbot             | 3.93 ms                                                               | 4.03 ms: 1.03x slower                                            |
| sqlglot_normalize        | 111 ms                                                                | 114 ms: 1.03x slower                                             |
| xml_etree_process        | 57.5 ms                                                               | 59.1 ms: 1.03x slower                                            |
| sympy_integrate          | 21.8 ms                                                               | 22.5 ms: 1.03x slower                                            |
| regex_compile            | 135 ms                                                                | 140 ms: 1.03x slower                                             |
| regex_dna                | 229 ms                                                                | 238 ms: 1.04x slower                                             |
| generators               | 29.6 ms                                                               | 30.8 ms: 1.04x slower                                            |
| pycparser                | 1.16 sec                                                              | 1.21 sec: 1.04x slower                                           |
| sympy_str                | 293 ms                                                                | 305 ms: 1.04x slower                                             |
| sympy_expand             | 496 ms                                                                | 518 ms: 1.04x slower                                             |
| tornado_http             | 92.5 ms                                                               | 97.0 ms: 1.05x slower                                            |
| richards                 | 40.9 ms                                                               | 43.0 ms: 1.05x slower                                            |
| dulwich_log              | 67.5 ms                                                               | 71.3 ms: 1.06x slower                                            |
| docutils                 | 2.86 sec                                                              | 3.03 sec: 1.06x slower                                           |
| tomli_loads              | 1.94 sec                                                              | 2.07 sec: 1.07x slower                                           |
| regex_v8                 | 25.0 ms                                                               | 26.7 ms: 1.07x slower                                            |
| pylint                   | 341 ms                                                                | 367 ms: 1.07x slower                                             |
| html5lib                 | 64.2 ms                                                               | 69.2 ms: 1.08x slower                                            |
| genshi_xml               | 55.6 ms                                                               | 61.8 ms: 1.11x slower                                            |
| deltablue                | 3.51 ms                                                               | 4.19 ms: 1.19x slower                                            |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                     |

Benchmark hidden because not significant (19): async_tree_none, async_tree_none_tg, async_tree_io_tg, async_tree_memoization, json, fannkuch, async_tree_memoization_tg, async_tree_cpu_io_mixed, bench_mp_pool, xml_etree_iterparse, async_tree_cpu_io_mixed_tg, coverage, pprint_pformat, deepcopy, scimark_sor, thrift, telco, xml_etree_parse, dask

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x