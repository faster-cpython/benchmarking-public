# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: grand_unified_tailca
- machine: linux-x86_64
- commit hash: d07479b
- commit date: 2025-02-13
- overall geometric mean: 1.485x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.34x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                             |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                           |
| html5lib       | 88.9 ms                                                | 58.4 ms: 1.52x faster                                                            |
| Geometric mean | (ref)                                                  | 1.38x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 611 ms: 2.90x faster                                                             |
| async_tree_none         | 728 ms                                                 | 256 ms: 2.84x faster                                                             |
| async_tree_memoization  | 870 ms                                                 | 314 ms: 2.77x faster                                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 526 ms: 1.93x faster                                                             |
| Geometric mean          | (ref)                                                  | 2.58x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 66.2 ms: 1.77x faster                                                            |
| nbody          | 154 ms                                                 | 86.9 ms: 1.77x faster                                                            |
| pidigits       | 191 ms                                                 | 222 ms: 1.16x slower                                                             |
| Geometric mean | (ref)                                                  | 1.39x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 124 ms: 1.52x faster                                                             |
| regex_dna      | 227 ms                                                 | 196 ms: 1.16x faster                                                             |
| regex_effbot   | 3.63 ms                                                | 3.15 ms: 1.15x faster                                                            |
| regex_v8       | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                            |
| Geometric mean | (ref)                                                  | 1.23x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.81 sec: 1.74x faster                                                           |
| unpickle_pure_python | 331 us                                                 | 211 us: 1.57x faster                                                             |
| pickle_pure_python   | 484 us                                                 | 312 us: 1.55x faster                                                             |
| xml_etree_process    | 79.1 ms                                                | 55.7 ms: 1.42x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 80.4 ms: 1.24x faster                                                            |
| json_dumps           | 14.2 ms                                                | 12.2 ms: 1.16x faster                                                            |
| xml_etree_iterparse  | 115 ms                                                 | 102 ms: 1.13x faster                                                             |
| xml_etree_parse      | 168 ms                                                 | 158 ms: 1.06x faster                                                             |
| json_loads           | 31.2 us                                                | 30.6 us: 1.02x faster                                                            |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                            |
| python_startup_no_site | 5.93 ms                                                | 7.01 ms: 1.18x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 30.4 ms: 1.58x faster                                                            |
| genshi_text     | 31.8 ms                                                | 20.5 ms: 1.55x faster                                                            |
| mako            | 16.3 ms                                                | 11.0 ms: 1.48x faster                                                            |
| genshi_xml      | 66.0 ms                                                | 47.6 ms: 1.39x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.50x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 155 us: 3.50x faster                                                             |
| generators               | 80.1 ms                                                | 27.2 ms: 2.95x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 611 ms: 2.90x faster                                                             |
| async_tree_none          | 728 ms                                                 | 256 ms: 2.84x faster                                                             |
| async_tree_memoization   | 870 ms                                                 | 314 ms: 2.77x faster                                                             |
| deltablue                | 7.91 ms                                                | 3.14 ms: 2.52x faster                                                            |
| logging_silent           | 190 ns                                                 | 86.5 ns: 2.19x faster                                                            |
| chaos                    | 115 ms                                                 | 53.9 ms: 2.14x faster                                                            |
| spectral_norm            | 170 ms                                                 | 81.4 ms: 2.09x faster                                                            |
| scimark_sor              | 220 ms                                                 | 107 ms: 2.05x faster                                                             |
| richards_super           | 94.7 ms                                                | 46.8 ms: 2.03x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 28.9 us: 2.02x faster                                                            |
| pylint                   | 551 ms                                                 | 274 ms: 2.01x faster                                                             |
| go                       | 240 ms                                                 | 120 ms: 2.00x faster                                                             |
| richards                 | 79.3 ms                                                | 40.0 ms: 1.98x faster                                                            |
| deepcopy                 | 479 us                                                 | 242 us: 1.98x faster                                                             |
| raytrace                 | 507 ms                                                 | 258 ms: 1.96x faster                                                             |
| scimark_monte_carlo      | 118 ms                                                 | 60.2 ms: 1.96x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 526 ms: 1.93x faster                                                             |
| float                    | 117 ms                                                 | 66.2 ms: 1.77x faster                                                            |
| nbody                    | 154 ms                                                 | 86.9 ms: 1.77x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 72.6 ms: 1.76x faster                                                            |
| pyflate                  | 716 ms                                                 | 407 ms: 1.76x faster                                                             |
| tomli_loads              | 3.14 sec                                               | 1.81 sec: 1.74x faster                                                           |
| sqlglot_parse            | 2.17 ms                                                | 1.26 ms: 1.72x faster                                                            |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.72x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.47 us: 1.69x faster                                                            |
| scimark_lu               | 176 ms                                                 | 105 ms: 1.67x faster                                                             |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                            |
| scimark_fft              | 466 ms                                                 | 286 ms: 1.63x faster                                                             |
| hexiom                   | 10.4 ms                                                | 6.43 ms: 1.62x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.00 ms: 1.62x faster                                                            |
| django_template          | 48.2 ms                                                | 30.4 ms: 1.58x faster                                                            |
| logging_simple           | 8.30 us                                                | 5.29 us: 1.57x faster                                                            |
| coroutines               | 35.1 ms                                                | 22.4 ms: 1.57x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 211 us: 1.57x faster                                                             |
| pickle_pure_python       | 484 us                                                 | 312 us: 1.55x faster                                                             |
| genshi_text              | 31.8 ms                                                | 20.5 ms: 1.55x faster                                                            |
| logging_format           | 9.09 us                                                | 5.87 us: 1.55x faster                                                            |
| html5lib                 | 88.9 ms                                                | 58.4 ms: 1.52x faster                                                            |
| regex_compile            | 188 ms                                                 | 124 ms: 1.52x faster                                                             |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.48x faster                                                            |
| thrift                   | 1.07 ms                                                | 742 us: 1.45x faster                                                             |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.3 ms: 1.43x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 55.7 ms: 1.42x faster                                                            |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.42x faster                                                           |
| pathlib                  | 20.5 ms                                                | 14.5 ms: 1.41x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 47.6 ms: 1.39x faster                                                            |
| sqlglot_normalize        | 143 ms                                                 | 103 ms: 1.38x faster                                                             |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                             |
| nqueens                  | 106 ms                                                 | 77.2 ms: 1.37x faster                                                            |
| pprint_safe_repr         | 1.02 sec                                               | 743 ms: 1.37x faster                                                             |
| sqlalchemy_declarative   | 172 ms                                                 | 127 ms: 1.36x faster                                                             |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                                           |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                             |
| sympy_integrate          | 25.8 ms                                                | 19.3 ms: 1.34x faster                                                            |
| fannkuch                 | 532 ms                                                 | 400 ms: 1.33x faster                                                             |
| dulwich_log              | 84.3 ms                                                | 63.9 ms: 1.32x faster                                                            |
| sqlglot_optimize         | 69.2 ms                                                | 52.9 ms: 1.31x faster                                                            |
| sympy_str                | 346 ms                                                 | 266 ms: 1.30x faster                                                             |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                           |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                                             |
| xml_etree_generate       | 99.4 ms                                                | 80.4 ms: 1.24x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 837 us: 1.18x faster                                                             |
| json_dumps               | 14.2 ms                                                | 12.2 ms: 1.16x faster                                                            |
| regex_dna                | 227 ms                                                 | 196 ms: 1.16x faster                                                             |
| regex_effbot             | 3.63 ms                                                | 3.15 ms: 1.15x faster                                                            |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.65 us: 1.14x faster                                                            |
| regex_v8                 | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 102 ms: 1.13x faster                                                             |
| async_generators         | 444 ms                                                 | 395 ms: 1.12x faster                                                             |
| xml_etree_parse          | 168 ms                                                 | 158 ms: 1.06x faster                                                             |
| meteor_contest           | 120 ms                                                 | 113 ms: 1.06x faster                                                             |
| json                     | 5.69 ms                                                | 5.49 ms: 1.04x faster                                                            |
| json_loads               | 31.2 us                                                | 30.6 us: 1.02x faster                                                            |
| telco                    | 7.27 ms                                                | 7.14 ms: 1.02x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                             |
| mdp                      | 2.85 sec                                               | 2.90 sec: 1.02x slower                                                           |
| pidigits                 | 191 ms                                                 | 222 ms: 1.16x slower                                                             |
| python_startup_no_site   | 5.93 ms                                                | 7.01 ms: 1.18x slower                                                            |
| gc_traversal             | 3.62 ms                                                | 4.98 ms: 1.38x slower                                                            |
| create_gc_cycles         | 1.62 ms                                                | 2.54 ms: 1.57x slower                                                            |
| bench_mp_pool            | 24.0 ms                                                | 79.6 ms: 3.31x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.46x faster                                                                     |

Benchmark hidden because not significant (1): coverage
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250213-3.14.0a5+-d07479b-CLANG,JIT/bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.485x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.34x

# Memory
- memory change: 1.29x