# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: disable_tailcall
- machine: linux-aarch64
- commit hash: da5ad58
- commit date: 2025-02-25
- overall geometric mean: 1.181x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: 1.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 337 ms: 1.13x faster                                                           |
| docutils       | 3.53 sec                                                              | 3.16 sec: 1.12x faster                                                         |
| html5lib       | 86.5 ms                                                               | 70.3 ms: 1.23x faster                                                          |
| Geometric mean | (ref)                                                                 | 1.16x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 999 ms: 2.29x faster                                                           |
| async_tree_none         | 950 ms                                                                | 434 ms: 2.19x faster                                                           |
| async_tree_memoization  | 1.13 sec                                                              | 534 ms: 2.12x faster                                                           |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 789 ms: 1.61x faster                                                           |
| Geometric mean          | (ref)                                                                 | 2.03x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 100 ms: 1.35x faster                                                           |
| nbody          | 166 ms                                                                | 145 ms: 1.14x faster                                                           |
| pidigits       | 235 ms                                                                | 310 ms: 1.32x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 156 ms: 1.13x faster                                                           |
| regex_dna      | 257 ms                                                                | 244 ms: 1.06x faster                                                           |
| regex_v8       | 32.2 ms                                                               | 35.4 ms: 1.10x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 465 us: 1.14x faster                                                           |
| unpickle_pure_python | 366 us                                                                | 333 us: 1.10x faster                                                           |
| xml_etree_process    | 99.5 ms                                                               | 92.9 ms: 1.07x faster                                                          |
| tomli_loads          | 3.36 sec                                                              | 3.26 sec: 1.03x faster                                                         |
| xml_etree_parse      | 212 ms                                                                | 216 ms: 1.02x slower                                                           |
| xml_etree_iterparse  | 156 ms                                                                | 164 ms: 1.05x slower                                                           |
| json_loads           | 30.9 us                                                               | 36.6 us: 1.18x slower                                                          |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                                   |

Benchmark hidden because not significant (2): json_dumps, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.39 ms: 1.36x slower                                                          |
| python_startup         | 11.2 ms                                                               | 16.9 ms: 1.51x slower                                                          |
| Geometric mean         | (ref)                                                                 | 1.44x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 16.0 ms: 1.18x faster                                                          |
| django_template | 53.3 ms                                                               | 45.5 ms: 1.17x faster                                                          |
| genshi_text     | 35.2 ms                                                               | 33.7 ms: 1.04x faster                                                          |
| genshi_xml      | 69.8 ms                                                               | 73.1 ms: 1.05x slower                                                          |
| Geometric mean  | (ref)                                                                 | 1.08x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 217 us: 3.05x faster                                                           |
| async_tree_io            | 2.28 sec                                                              | 999 ms: 2.29x faster                                                           |
| async_tree_none          | 950 ms                                                                | 434 ms: 2.19x faster                                                           |
| async_tree_memoization   | 1.13 sec                                                              | 534 ms: 2.12x faster                                                           |
| deltablue                | 8.94 ms                                                               | 4.82 ms: 1.86x faster                                                          |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 789 ms: 1.61x faster                                                           |
| raytrace                 | 573 ms                                                                | 368 ms: 1.56x faster                                                           |
| logging_silent           | 222 ns                                                                | 147 ns: 1.51x faster                                                           |
| go                       | 264 ms                                                                | 175 ms: 1.51x faster                                                           |
| pylint                   | 485 ms                                                                | 324 ms: 1.50x faster                                                           |
| spectral_norm            | 186 ms                                                                | 125 ms: 1.49x faster                                                           |
| richards                 | 91.7 ms                                                               | 61.6 ms: 1.49x faster                                                          |
| comprehensions           | 33.1 us                                                               | 22.4 us: 1.48x faster                                                          |
| chaos                    | 121 ms                                                                | 82.2 ms: 1.47x faster                                                          |
| richards_super           | 107 ms                                                                | 73.0 ms: 1.47x faster                                                          |
| generators               | 68.1 ms                                                               | 48.5 ms: 1.40x faster                                                          |
| sqlglot_parse            | 2.40 ms                                                               | 1.76 ms: 1.37x faster                                                          |
| sqlglot_transpile        | 2.84 ms                                                               | 2.09 ms: 1.36x faster                                                          |
| deepcopy                 | 511 us                                                                | 379 us: 1.35x faster                                                           |
| float                    | 135 ms                                                                | 100 ms: 1.35x faster                                                           |
| scimark_sor              | 246 ms                                                                | 185 ms: 1.33x faster                                                           |
| crypto_pyaes             | 134 ms                                                                | 101 ms: 1.32x faster                                                           |
| scimark_lu               | 227 ms                                                                | 172 ms: 1.32x faster                                                           |
| deepcopy_memo            | 61.7 us                                                               | 47.8 us: 1.29x faster                                                          |
| sqlalchemy_declarative   | 197 ms                                                                | 154 ms: 1.28x faster                                                           |
| scimark_monte_carlo      | 128 ms                                                                | 101 ms: 1.26x faster                                                           |
| pyflate                  | 795 ms                                                                | 633 ms: 1.26x faster                                                           |
| html5lib                 | 86.5 ms                                                               | 70.3 ms: 1.23x faster                                                          |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.25 ms: 1.22x faster                                                          |
| hexiom                   | 10.9 ms                                                               | 9.10 ms: 1.20x faster                                                          |
| sqlalchemy_imperative    | 20.5 ms                                                               | 17.4 ms: 1.18x faster                                                          |
| mako                     | 18.9 ms                                                               | 16.0 ms: 1.18x faster                                                          |
| logging_format           | 10.6 us                                                               | 9.02 us: 1.18x faster                                                          |
| logging_simple           | 9.78 us                                                               | 8.33 us: 1.17x faster                                                          |
| django_template          | 53.3 ms                                                               | 45.5 ms: 1.17x faster                                                          |
| pycparser                | 1.69 sec                                                              | 1.44 sec: 1.17x faster                                                         |
| thrift                   | 1.26 ms                                                               | 1.09 ms: 1.15x faster                                                          |
| coroutines               | 37.2 ms                                                               | 32.4 ms: 1.15x faster                                                          |
| nbody                    | 166 ms                                                                | 145 ms: 1.14x faster                                                           |
| sympy_sum                | 184 ms                                                                | 161 ms: 1.14x faster                                                           |
| deepcopy_reduce          | 4.60 us                                                               | 4.03 us: 1.14x faster                                                          |
| bench_thread_pool        | 1.59 ms                                                               | 1.40 ms: 1.14x faster                                                          |
| pickle_pure_python       | 529 us                                                                | 465 us: 1.14x faster                                                           |
| 2to3                     | 381 ms                                                                | 337 ms: 1.13x faster                                                           |
| regex_compile            | 177 ms                                                                | 156 ms: 1.13x faster                                                           |
| pathlib                  | 26.3 ms                                                               | 23.3 ms: 1.13x faster                                                          |
| sympy_integrate          | 26.5 ms                                                               | 23.5 ms: 1.13x faster                                                          |
| docutils                 | 3.53 sec                                                              | 3.16 sec: 1.12x faster                                                         |
| scimark_fft              | 500 ms                                                                | 448 ms: 1.12x faster                                                           |
| unpickle_pure_python     | 366 us                                                                | 333 us: 1.10x faster                                                           |
| sympy_str                | 329 ms                                                                | 303 ms: 1.08x faster                                                           |
| sqlglot_optimize         | 75.4 ms                                                               | 70.4 ms: 1.07x faster                                                          |
| xml_etree_process        | 99.5 ms                                                               | 92.9 ms: 1.07x faster                                                          |
| mdp                      | 3.70 sec                                                              | 3.46 sec: 1.07x faster                                                         |
| dulwich_log              | 73.5 ms                                                               | 69.5 ms: 1.06x faster                                                          |
| regex_dna                | 257 ms                                                                | 244 ms: 1.06x faster                                                           |
| genshi_text              | 35.2 ms                                                               | 33.7 ms: 1.04x faster                                                          |
| tomli_loads              | 3.36 sec                                                              | 3.26 sec: 1.03x faster                                                         |
| pprint_pformat           | 2.36 sec                                                              | 2.32 sec: 1.02x faster                                                         |
| xml_etree_parse          | 212 ms                                                                | 216 ms: 1.02x slower                                                           |
| sqlite_synth             | 4.12 us                                                               | 4.26 us: 1.04x slower                                                          |
| meteor_contest           | 126 ms                                                                | 131 ms: 1.04x slower                                                           |
| asyncio_websockets       | 657 ms                                                                | 686 ms: 1.04x slower                                                           |
| genshi_xml               | 69.8 ms                                                               | 73.1 ms: 1.05x slower                                                          |
| xml_etree_iterparse      | 156 ms                                                                | 164 ms: 1.05x slower                                                           |
| async_generators         | 452 ms                                                                | 484 ms: 1.07x slower                                                           |
| json                     | 5.88 ms                                                               | 6.34 ms: 1.08x slower                                                          |
| regex_v8                 | 32.2 ms                                                               | 35.4 ms: 1.10x slower                                                          |
| fannkuch                 | 546 ms                                                                | 624 ms: 1.14x slower                                                           |
| json_loads               | 30.9 us                                                               | 36.6 us: 1.18x slower                                                          |
| telco                    | 8.49 ms                                                               | 10.1 ms: 1.19x slower                                                          |
| coverage                 | 83.6 ms                                                               | 104 ms: 1.24x slower                                                           |
| pidigits                 | 235 ms                                                                | 310 ms: 1.32x slower                                                           |
| python_startup_no_site   | 6.89 ms                                                               | 9.39 ms: 1.36x slower                                                          |
| python_startup           | 11.2 ms                                                               | 16.9 ms: 1.51x slower                                                          |
| gc_traversal             | 4.15 ms                                                               | 6.79 ms: 1.63x slower                                                          |
| create_gc_cycles         | 2.26 ms                                                               | 3.79 ms: 1.68x slower                                                          |
| bench_mp_pool            | 14.5 ms                                                               | 8.30 sec: 571.09x slower                                                       |
| Geometric mean           | (ref)                                                                 | 1.07x faster                                                                   |

Benchmark hidden because not significant (7): json_dumps, sqlglot_normalize, sympy_expand, regex_effbot, pprint_safe_repr, xml_etree_generate, nqueens
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250225-3.14.0a5+-da5ad58-CLANG/bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.181x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: 1.39x