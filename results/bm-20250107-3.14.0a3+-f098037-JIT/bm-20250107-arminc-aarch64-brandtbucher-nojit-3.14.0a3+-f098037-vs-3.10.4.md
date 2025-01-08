# Results vs. 3.10.4

- fork: brandtbucher
- ref: nojit
- machine: linux-aarch64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.220x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 324 ms: 1.18x faster                                            |
| docutils       | 3.53 sec                                                              | 3.20 sec: 1.10x faster                                          |
| html5lib       | 86.5 ms                                                               | 72.8 ms: 1.19x faster                                           |
| Geometric mean | (ref)                                                                 | 1.15x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 933 ms: 2.45x faster                                            |
| async_tree_none         | 950 ms                                                                | 404 ms: 2.35x faster                                            |
| async_tree_memoization  | 1.13 sec                                                              | 525 ms: 2.16x faster                                            |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 698 ms: 1.82x faster                                            |
| Geometric mean          | (ref)                                                                 | 2.18x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 135 ms                                                                | 90.9 ms: 1.48x faster                                           |
| nbody          | 166 ms                                                                | 114 ms: 1.46x faster                                            |
| pidigits       | 235 ms                                                                | 242 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 141 ms: 1.25x faster                                            |
| regex_effbot   | 4.25 ms                                                               | 3.98 ms: 1.07x faster                                           |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                    |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 262 us: 1.40x faster                                            |
| tomli_loads          | 3.36 sec                                                              | 2.54 sec: 1.32x faster                                          |
| pickle_pure_python   | 529 us                                                                | 412 us: 1.28x faster                                            |
| xml_etree_process    | 99.5 ms                                                               | 81.4 ms: 1.22x faster                                           |
| json_dumps           | 16.7 ms                                                               | 14.4 ms: 1.16x faster                                           |
| xml_etree_parse      | 212 ms                                                                | 183 ms: 1.16x faster                                            |
| xml_etree_iterparse  | 156 ms                                                                | 142 ms: 1.10x faster                                            |
| Geometric mean       | (ref)                                                                 | 1.18x faster                                                    |

Benchmark hidden because not significant (2): xml_etree_generate, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.16 ms: 1.33x slower                                           |
| python_startup         | 11.2 ms                                                               | 16.4 ms: 1.47x slower                                           |
| Geometric mean         | (ref)                                                                 | 1.40x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.9 ms: 1.36x faster                                           |
| django_template | 53.3 ms                                                               | 48.4 ms: 1.10x faster                                           |
| genshi_xml      | 69.8 ms                                                               | 82.7 ms: 1.18x slower                                           |
| Geometric mean  | (ref)                                                                 | 1.07x faster                                                    |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 215 us: 3.07x faster                                            |
| async_tree_io            | 2.28 sec                                                              | 933 ms: 2.45x faster                                            |
| async_tree_none          | 950 ms                                                                | 404 ms: 2.35x faster                                            |
| async_tree_memoization   | 1.13 sec                                                              | 525 ms: 2.16x faster                                            |
| deltablue                | 8.94 ms                                                               | 4.56 ms: 1.96x faster                                           |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 698 ms: 1.82x faster                                            |
| richards_super           | 107 ms                                                                | 64.2 ms: 1.67x faster                                           |
| richards                 | 91.7 ms                                                               | 56.4 ms: 1.63x faster                                           |
| raytrace                 | 573 ms                                                                | 368 ms: 1.56x faster                                            |
| deepcopy_memo            | 61.7 us                                                               | 40.2 us: 1.53x faster                                           |
| scimark_monte_carlo      | 128 ms                                                                | 83.9 ms: 1.52x faster                                           |
| scimark_sor              | 246 ms                                                                | 162 ms: 1.52x faster                                            |
| go                       | 264 ms                                                                | 174 ms: 1.51x faster                                            |
| logging_silent           | 222 ns                                                                | 147 ns: 1.51x faster                                            |
| sqlglot_parse            | 2.40 ms                                                               | 1.61 ms: 1.49x faster                                           |
| sqlglot_transpile        | 2.84 ms                                                               | 1.91 ms: 1.49x faster                                           |
| float                    | 135 ms                                                                | 90.9 ms: 1.48x faster                                           |
| nbody                    | 166 ms                                                                | 114 ms: 1.46x faster                                            |
| chaos                    | 121 ms                                                                | 83.5 ms: 1.45x faster                                           |
| scimark_lu               | 227 ms                                                                | 157 ms: 1.45x faster                                            |
| crypto_pyaes             | 134 ms                                                                | 92.9 ms: 1.44x faster                                           |
| pylint                   | 485 ms                                                                | 345 ms: 1.41x faster                                            |
| unpickle_pure_python     | 366 us                                                                | 262 us: 1.40x faster                                            |
| mako                     | 18.9 ms                                                               | 13.9 ms: 1.36x faster                                           |
| generators               | 68.1 ms                                                               | 50.6 ms: 1.35x faster                                           |
| spectral_norm            | 186 ms                                                                | 140 ms: 1.33x faster                                            |
| comprehensions           | 33.1 us                                                               | 24.9 us: 1.33x faster                                           |
| pyflate                  | 795 ms                                                                | 599 ms: 1.33x faster                                            |
| tomli_loads              | 3.36 sec                                                              | 2.54 sec: 1.32x faster                                          |
| deepcopy                 | 511 us                                                                | 392 us: 1.30x faster                                            |
| pickle_pure_python       | 529 us                                                                | 412 us: 1.28x faster                                            |
| thrift                   | 1.26 ms                                                               | 1000 us: 1.26x faster                                           |
| regex_compile            | 177 ms                                                                | 141 ms: 1.25x faster                                            |
| coroutines               | 37.2 ms                                                               | 30.0 ms: 1.24x faster                                           |
| xml_etree_process        | 99.5 ms                                                               | 81.4 ms: 1.22x faster                                           |
| logging_simple           | 9.78 us                                                               | 8.08 us: 1.21x faster                                           |
| sqlalchemy_declarative   | 197 ms                                                                | 164 ms: 1.21x faster                                            |
| logging_format           | 10.6 us                                                               | 8.87 us: 1.20x faster                                           |
| html5lib                 | 86.5 ms                                                               | 72.8 ms: 1.19x faster                                           |
| scimark_fft              | 500 ms                                                                | 422 ms: 1.19x faster                                            |
| pathlib                  | 26.3 ms                                                               | 22.3 ms: 1.18x faster                                           |
| sqlalchemy_imperative    | 20.5 ms                                                               | 17.4 ms: 1.18x faster                                           |
| 2to3                     | 381 ms                                                                | 324 ms: 1.18x faster                                            |
| json_dumps               | 16.7 ms                                                               | 14.4 ms: 1.16x faster                                           |
| xml_etree_parse          | 212 ms                                                                | 183 ms: 1.16x faster                                            |
| bench_thread_pool        | 1.59 ms                                                               | 1.38 ms: 1.16x faster                                           |
| pycparser                | 1.69 sec                                                              | 1.47 sec: 1.15x faster                                          |
| deepcopy_reduce          | 4.60 us                                                               | 4.04 us: 1.14x faster                                           |
| hexiom                   | 10.9 ms                                                               | 9.60 ms: 1.14x faster                                           |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.72 ms: 1.14x faster                                           |
| sqlglot_normalize        | 156 ms                                                                | 139 ms: 1.13x faster                                            |
| sympy_integrate          | 26.5 ms                                                               | 24.0 ms: 1.11x faster                                           |
| docutils                 | 3.53 sec                                                              | 3.20 sec: 1.10x faster                                          |
| django_template          | 53.3 ms                                                               | 48.4 ms: 1.10x faster                                           |
| sympy_sum                | 184 ms                                                                | 167 ms: 1.10x faster                                            |
| xml_etree_iterparse      | 156 ms                                                                | 142 ms: 1.10x faster                                            |
| sqlglot_optimize         | 75.4 ms                                                               | 69.6 ms: 1.08x faster                                           |
| fannkuch                 | 546 ms                                                                | 507 ms: 1.08x faster                                            |
| regex_effbot             | 4.25 ms                                                               | 3.98 ms: 1.07x faster                                           |
| sympy_str                | 329 ms                                                                | 309 ms: 1.06x faster                                            |
| mdp                      | 3.70 sec                                                              | 3.60 sec: 1.03x faster                                          |
| asyncio_websockets       | 657 ms                                                                | 675 ms: 1.03x slower                                            |
| pidigits                 | 235 ms                                                                | 242 ms: 1.03x slower                                            |
| pprint_safe_repr         | 1.15 sec                                                              | 1.24 sec: 1.08x slower                                          |
| nqueens                  | 117 ms                                                                | 127 ms: 1.08x slower                                            |
| pprint_pformat           | 2.36 sec                                                              | 2.58 sec: 1.10x slower                                          |
| telco                    | 8.49 ms                                                               | 9.52 ms: 1.12x slower                                           |
| mypy2                    | 936 ms                                                                | 1.10 sec: 1.18x slower                                          |
| async_generators         | 452 ms                                                                | 534 ms: 1.18x slower                                            |
| genshi_xml               | 69.8 ms                                                               | 82.7 ms: 1.18x slower                                           |
| python_startup_no_site   | 6.89 ms                                                               | 9.16 ms: 1.33x slower                                           |
| coverage                 | 83.6 ms                                                               | 111 ms: 1.33x slower                                            |
| python_startup           | 11.2 ms                                                               | 16.4 ms: 1.47x slower                                           |
| create_gc_cycles         | 2.26 ms                                                               | 3.56 ms: 1.57x slower                                           |
| gc_traversal             | 4.15 ms                                                               | 6.94 ms: 1.67x slower                                           |
| bench_mp_pool            | 14.5 ms                                                               | 1.51 sec: 103.66x slower                                        |
| Geometric mean           | (ref)                                                                 | 1.13x faster                                                    |

Benchmark hidden because not significant (10): xml_etree_generate, genshi_text, dulwich_log, sympy_expand, json, regex_dna, regex_v8, sqlite_synth, meteor_contest, json_loads
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250107-3.14.0a3+-f098037-JIT/bm-20250107-arminc-aarch64-brandtbucher-nojit-3.14.0a3+-f098037.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.220x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: 1.33x