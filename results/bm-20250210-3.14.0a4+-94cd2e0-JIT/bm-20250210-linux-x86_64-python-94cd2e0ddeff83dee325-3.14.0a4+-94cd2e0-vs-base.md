# Results vs. base

- fork: python
- ref: 94cd2e0ddeff83dee325
- machine: linux-x86_64
- commit hash: 94cd2e0
- commit date: 2025-02-10
- overall geometric mean: 1.010x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250210-3.14.0a4+-94cd2e0/bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0.json | results/bm-20250210-3.14.0a4+-94cd2e0-JIT/bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                                                            | 258 ms: 1.03x slower                                                                                                  |
| docutils       | 2.60 sec                                                                                                          | 2.69 sec: 1.04x slower                                                                                                |
| html5lib       | 61.6 ms                                                                                                           | 62.2 ms: 1.01x slower                                                                                                 |
| sphinx         | 999 ms                                                                                                            | 1.02 sec: 1.02x slower                                                                                                |
| Geometric mean | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | results/bm-20250210-3.14.0a4+-94cd2e0/bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0.json | results/bm-20250210-3.14.0a4+-94cd2e0-JIT/bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| coroutines             | 23.3 ms                                                                                                           | 23.0 ms: 1.01x faster                                                                                                 |
| async_tree_none_tg     | 257 ms                                                                                                            | 260 ms: 1.01x slower                                                                                                  |
| async_tree_io          | 619 ms                                                                                                            | 627 ms: 1.01x slower                                                                                                  |
| async_tree_memoization | 323 ms                                                                                                            | 328 ms: 1.01x slower                                                                                                  |
| async_tree_none        | 264 ms                                                                                                            | 269 ms: 1.02x slower                                                                                                  |
| async_generators       | 376 ms                                                                                                            | 411 ms: 1.09x slower                                                                                                  |
| Geometric mean         | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (5): async_tree_memoization_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250210-3.14.0a4+-94cd2e0/bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0.json | results/bm-20250210-3.14.0a4+-94cd2e0-JIT/bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                                                            | 186 ms: 1.00x faster                                                                                                  |
| nbody          | 92.6 ms                                                                                                           | 96.6 ms: 1.04x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250210-3.14.0a4+-94cd2e0/bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0.json | results/bm-20250210-3.14.0a4+-94cd2e0-JIT/bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 3.40 ms                                                                                                           | 3.09 ms: 1.10x faster                                                                                                 |
| regex_v8       | 25.1 ms                                                                                                           | 24.1 ms: 1.04x faster                                                                                                 |
| regex_dna      | 215 ms                                                                                                            | 209 ms: 1.03x faster                                                                                                  |
| regex_compile  | 126 ms                                                                                                            | 127 ms: 1.01x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.04x faster                                                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250210-3.14.0a4+-94cd2e0/bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0.json | results/bm-20250210-3.14.0a4+-94cd2e0-JIT/bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 217 us                                                                                                            | 201 us: 1.08x faster                                                                                                  |
| xml_etree_generate   | 83.1 ms                                                                                                           | 79.1 ms: 1.05x faster                                                                                                 |
| tomli_loads          | 1.94 sec                                                                                                          | 1.85 sec: 1.05x faster                                                                                                |
| xml_etree_process    | 58.0 ms                                                                                                           | 56.1 ms: 1.03x faster                                                                                                 |
| xml_etree_parse      | 139 ms                                                                                                            | 137 ms: 1.02x faster                                                                                                  |
| xml_etree_iterparse  | 96.6 ms                                                                                                           | 95.0 ms: 1.02x faster                                                                                                 |
| pickle_pure_python   | 321 us                                                                                                            | 318 us: 1.01x faster                                                                                                  |
| json_loads           | 28.6 us                                                                                                           | 28.8 us: 1.01x slower                                                                                                 |
| json_dumps           | 11.7 ms                                                                                                           | 11.8 ms: 1.01x slower                                                                                                 |
| Geometric mean       | (ref)                                                                                                             | 1.03x faster                                                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250210-3.14.0a4+-94cd2e0/bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0.json | results/bm-20250210-3.14.0a4+-94cd2e0-JIT/bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                                                           | 12.8 ms: 1.00x slower                                                                                                 |
| python_startup_no_site | 7.05 ms                                                                                                           | 7.06 ms: 1.00x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.00x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250210-3.14.0a4+-94cd2e0/bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0.json | results/bm-20250210-3.14.0a4+-94cd2e0-JIT/bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako           | 11.0 ms                                                                                                           | 9.83 ms: 1.11x faster                                                                                                 |
| genshi_xml     | 47.9 ms                                                                                                           | 49.6 ms: 1.03x slower                                                                                                 |
| genshi_text    | 21.5 ms                                                                                                           | 22.3 ms: 1.04x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | results/bm-20250210-3.14.0a4+-94cd2e0/bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0.json | results/bm-20250210-3.14.0a4+-94cd2e0-JIT/bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0.json |
|--------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako                     | 11.0 ms                                                                                                           | 9.83 ms: 1.11x faster                                                                                                 |
| regex_effbot             | 3.40 ms                                                                                                           | 3.09 ms: 1.10x faster                                                                                                 |
| unpickle_pure_python     | 217 us                                                                                                            | 201 us: 1.08x faster                                                                                                  |
| scimark_fft              | 340 ms                                                                                                            | 315 ms: 1.08x faster                                                                                                  |
| gc_traversal             | 4.95 ms                                                                                                           | 4.63 ms: 1.07x faster                                                                                                 |
| xml_etree_generate       | 83.1 ms                                                                                                           | 79.1 ms: 1.05x faster                                                                                                 |
| tomli_loads              | 1.94 sec                                                                                                          | 1.85 sec: 1.05x faster                                                                                                |
| telco                    | 7.94 ms                                                                                                           | 7.63 ms: 1.04x faster                                                                                                 |
| regex_v8                 | 25.1 ms                                                                                                           | 24.1 ms: 1.04x faster                                                                                                 |
| pyflate                  | 461 ms                                                                                                            | 444 ms: 1.04x faster                                                                                                  |
| scimark_sparse_mat_mult  | 4.74 ms                                                                                                           | 4.57 ms: 1.04x faster                                                                                                 |
| xml_etree_process        | 58.0 ms                                                                                                           | 56.1 ms: 1.03x faster                                                                                                 |
| regex_dna                | 215 ms                                                                                                            | 209 ms: 1.03x faster                                                                                                  |
| sqlite_synth             | 2.80 us                                                                                                           | 2.73 us: 1.03x faster                                                                                                 |
| xml_etree_parse          | 139 ms                                                                                                            | 137 ms: 1.02x faster                                                                                                  |
| xml_etree_iterparse      | 96.6 ms                                                                                                           | 95.0 ms: 1.02x faster                                                                                                 |
| scimark_sor              | 121 ms                                                                                                            | 119 ms: 1.02x faster                                                                                                  |
| fannkuch                 | 403 ms                                                                                                            | 397 ms: 1.01x faster                                                                                                  |
| coroutines               | 23.3 ms                                                                                                           | 23.0 ms: 1.01x faster                                                                                                 |
| scimark_monte_carlo      | 67.2 ms                                                                                                           | 66.4 ms: 1.01x faster                                                                                                 |
| pickle_pure_python       | 321 us                                                                                                            | 318 us: 1.01x faster                                                                                                  |
| create_gc_cycles         | 2.48 ms                                                                                                           | 2.45 ms: 1.01x faster                                                                                                 |
| crypto_pyaes             | 70.0 ms                                                                                                           | 69.6 ms: 1.01x faster                                                                                                 |
| pidigits                 | 186 ms                                                                                                            | 186 ms: 1.00x faster                                                                                                  |
| python_startup           | 12.8 ms                                                                                                           | 12.8 ms: 1.00x slower                                                                                                 |
| python_startup_no_site   | 7.05 ms                                                                                                           | 7.06 ms: 1.00x slower                                                                                                 |
| bpe_tokeniser            | 4.35 sec                                                                                                          | 4.36 sec: 1.00x slower                                                                                                |
| generators               | 28.1 ms                                                                                                           | 28.3 ms: 1.01x slower                                                                                                 |
| thrift                   | 767 us                                                                                                            | 772 us: 1.01x slower                                                                                                  |
| bench_mp_pool            | 80.7 ms                                                                                                           | 81.2 ms: 1.01x slower                                                                                                 |
| json_loads               | 28.6 us                                                                                                           | 28.8 us: 1.01x slower                                                                                                 |
| scimark_lu               | 115 ms                                                                                                            | 115 ms: 1.01x slower                                                                                                  |
| html5lib                 | 61.6 ms                                                                                                           | 62.2 ms: 1.01x slower                                                                                                 |
| regex_compile            | 126 ms                                                                                                            | 127 ms: 1.01x slower                                                                                                  |
| async_tree_none_tg       | 257 ms                                                                                                            | 260 ms: 1.01x slower                                                                                                  |
| json_dumps               | 11.7 ms                                                                                                           | 11.8 ms: 1.01x slower                                                                                                 |
| deepcopy                 | 258 us                                                                                                            | 261 us: 1.01x slower                                                                                                  |
| async_tree_io            | 619 ms                                                                                                            | 627 ms: 1.01x slower                                                                                                  |
| async_tree_memoization   | 323 ms                                                                                                            | 328 ms: 1.01x slower                                                                                                  |
| sphinx                   | 999 ms                                                                                                            | 1.02 sec: 1.02x slower                                                                                                |
| async_tree_none          | 264 ms                                                                                                            | 269 ms: 1.02x slower                                                                                                  |
| k_core                   | 2.26 sec                                                                                                          | 2.30 sec: 1.02x slower                                                                                                |
| mdp                      | 2.50 sec                                                                                                          | 2.55 sec: 1.02x slower                                                                                                |
| chaos                    | 57.7 ms                                                                                                           | 58.8 ms: 1.02x slower                                                                                                 |
| subparsers               | 20.5 ms                                                                                                           | 20.9 ms: 1.02x slower                                                                                                 |
| logging_format           | 6.11 us                                                                                                           | 6.24 us: 1.02x slower                                                                                                 |
| connected_components     | 435 ms                                                                                                            | 445 ms: 1.02x slower                                                                                                  |
| sqlglot_parse            | 1.24 ms                                                                                                           | 1.27 ms: 1.02x slower                                                                                                 |
| richards_super           | 50.4 ms                                                                                                           | 51.6 ms: 1.02x slower                                                                                                 |
| shortest_path            | 474 ms                                                                                                            | 486 ms: 1.03x slower                                                                                                  |
| logging_simple           | 5.48 us                                                                                                           | 5.63 us: 1.03x slower                                                                                                 |
| 2to3                     | 251 ms                                                                                                            | 258 ms: 1.03x slower                                                                                                  |
| pathlib                  | 16.3 ms                                                                                                           | 16.7 ms: 1.03x slower                                                                                                 |
| sqlglot_transpile        | 1.54 ms                                                                                                           | 1.59 ms: 1.03x slower                                                                                                 |
| sqlalchemy_declarative   | 127 ms                                                                                                            | 131 ms: 1.03x slower                                                                                                  |
| richards                 | 44.1 ms                                                                                                           | 45.5 ms: 1.03x slower                                                                                                 |
| meteor_contest           | 105 ms                                                                                                            | 109 ms: 1.03x slower                                                                                                  |
| bench_thread_pool        | 860 us                                                                                                            | 888 us: 1.03x slower                                                                                                  |
| raytrace                 | 272 ms                                                                                                            | 281 ms: 1.03x slower                                                                                                  |
| logging_silent           | 107 ns                                                                                                            | 110 ns: 1.03x slower                                                                                                  |
| genshi_xml               | 47.9 ms                                                                                                           | 49.6 ms: 1.03x slower                                                                                                 |
| dulwich_log              | 64.0 ms                                                                                                           | 66.2 ms: 1.04x slower                                                                                                 |
| sqlglot_normalize        | 103 ms                                                                                                            | 107 ms: 1.04x slower                                                                                                  |
| many_optionals           | 927 us                                                                                                            | 960 us: 1.04x slower                                                                                                  |
| sympy_integrate          | 19.6 ms                                                                                                           | 20.3 ms: 1.04x slower                                                                                                 |
| docutils                 | 2.60 sec                                                                                                          | 2.69 sec: 1.04x slower                                                                                                |
| genshi_text              | 21.5 ms                                                                                                           | 22.3 ms: 1.04x slower                                                                                                 |
| sympy_sum                | 145 ms                                                                                                            | 151 ms: 1.04x slower                                                                                                  |
| sqlglot_optimize         | 51.7 ms                                                                                                           | 53.7 ms: 1.04x slower                                                                                                 |
| nbody                    | 92.6 ms                                                                                                           | 96.6 ms: 1.04x slower                                                                                                 |
| sqlalchemy_imperative    | 16.2 ms                                                                                                           | 16.9 ms: 1.04x slower                                                                                                 |
| sympy_str                | 264 ms                                                                                                            | 276 ms: 1.04x slower                                                                                                  |
| pprint_safe_repr         | 716 ms                                                                                                            | 748 ms: 1.04x slower                                                                                                  |
| typing_runtime_protocols | 156 us                                                                                                            | 163 us: 1.05x slower                                                                                                  |
| sympy_expand             | 450 ms                                                                                                            | 472 ms: 1.05x slower                                                                                                  |
| pprint_pformat           | 1.46 sec                                                                                                          | 1.54 sec: 1.05x slower                                                                                                |
| comprehensions           | 16.3 us                                                                                                           | 17.2 us: 1.06x slower                                                                                                 |
| deltablue                | 3.19 ms                                                                                                           | 3.44 ms: 1.08x slower                                                                                                 |
| async_generators         | 376 ms                                                                                                            | 411 ms: 1.09x slower                                                                                                  |
| go                       | 117 ms                                                                                                            | 131 ms: 1.13x slower                                                                                                  |
| nqueens                  | 79.3 ms                                                                                                           | 89.4 ms: 1.13x slower                                                                                                 |
| hexiom                   | 6.11 ms                                                                                                           | 6.95 ms: 1.14x slower                                                                                                 |
| Geometric mean           | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (14): pycparser, coverage, async_tree_memoization_tg, django_template, json, asyncio_websockets, deepcopy_reduce, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, deepcopy_memo, spectral_norm, float, async_tree_io_tg, pylint

- Geometric mean (including insignificant results): 1.010x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x