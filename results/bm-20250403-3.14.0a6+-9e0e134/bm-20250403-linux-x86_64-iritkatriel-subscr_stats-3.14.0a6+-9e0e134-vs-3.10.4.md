# Results vs. 3.10.4

- fork: iritkatriel
- ref: subscr_stats
- machine: linux-x86_64
- commit hash: 9e0e134
- commit date: 2025-04-03
- overall geometric mean: 1.462x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                              |
| html5lib       | 88.9 ms                                                | 62.5 ms: 1.42x faster                                               |
| Geometric mean | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 608 ms: 2.91x faster                                                |
| async_tree_none         | 728 ms                                                 | 260 ms: 2.80x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 312 ms: 2.79x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 488 ms: 2.08x faster                                                |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 69.0 ms: 1.70x faster                                               |
| nbody          | 154 ms                                                 | 97.7 ms: 1.57x faster                                               |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.40x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.50x faster                                                |
| regex_v8       | 27.8 ms                                                | 22.9 ms: 1.21x faster                                               |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                |
| regex_effbot   | 3.63 ms                                                | 3.81 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                  | 1.16x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.00 sec: 1.57x faster                                              |
| pickle_pure_python   | 484 us                                                 | 317 us: 1.53x faster                                                |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 58.5 ms: 1.35x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.23x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.18x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 84.2 ms: 1.18x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 98.4 ms: 1.17x faster                                               |
| json_loads           | 31.2 us                                                | 29.5 us: 1.06x faster                                               |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 8.19 ms: 1.38x slower                                               |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.4 ms: 1.53x faster                                               |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                               |
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                               |
| genshi_xml      | 66.0 ms                                                | 48.8 ms: 1.35x faster                                               |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.39x faster                                                |
| async_tree_io            | 1.77 sec                                               | 608 ms: 2.91x faster                                                |
| async_tree_none          | 728 ms                                                 | 260 ms: 2.80x faster                                                |
| generators               | 80.1 ms                                                | 28.6 ms: 2.80x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 312 ms: 2.79x faster                                                |
| deltablue                | 7.91 ms                                                | 3.11 ms: 2.54x faster                                               |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.32x faster                                              |
| go                       | 240 ms                                                 | 112 ms: 2.14x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 488 ms: 2.08x faster                                                |
| pylint                   | 551 ms                                                 | 276 ms: 2.00x faster                                                |
| chaos                    | 115 ms                                                 | 58.3 ms: 1.98x faster                                               |
| deepcopy_memo            | 58.5 us                                                | 29.6 us: 1.97x faster                                               |
| logging_silent           | 190 ns                                                 | 96.1 ns: 1.97x faster                                               |
| raytrace                 | 507 ms                                                 | 266 ms: 1.91x faster                                                |
| richards_super           | 94.7 ms                                                | 50.0 ms: 1.90x faster                                               |
| deepcopy                 | 479 us                                                 | 254 us: 1.89x faster                                                |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                                |
| richards                 | 79.3 ms                                                | 44.1 ms: 1.80x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 73.0 ms: 1.75x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 67.7 ms: 1.75x faster                                               |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                               |
| hexiom                   | 10.4 ms                                                | 6.08 ms: 1.71x faster                                               |
| spectral_norm            | 170 ms                                                 | 100.0 ms: 1.70x faster                                              |
| float                    | 117 ms                                                 | 69.0 ms: 1.70x faster                                               |
| pyflate                  | 716 ms                                                 | 432 ms: 1.66x faster                                                |
| tomli_loads              | 3.14 sec                                               | 2.00 sec: 1.57x faster                                              |
| nbody                    | 154 ms                                                 | 97.7 ms: 1.57x faster                                               |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.55x faster                                               |
| django_template          | 48.2 ms                                                | 31.4 ms: 1.53x faster                                               |
| pickle_pure_python       | 484 us                                                 | 317 us: 1.53x faster                                                |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                |
| logging_simple           | 8.30 us                                                | 5.48 us: 1.51x faster                                               |
| regex_compile            | 188 ms                                                 | 126 ms: 1.50x faster                                                |
| logging_format           | 9.09 us                                                | 6.07 us: 1.50x faster                                               |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                               |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.47x faster                                               |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                               |
| dulwich_log              | 84.3 ms                                                | 58.5 ms: 1.44x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                              |
| html5lib                 | 88.9 ms                                                | 62.5 ms: 1.42x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 722 ms: 1.41x faster                                                |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.6 ms: 1.41x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.63 ms: 1.40x faster                                               |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 19.0 ms: 1.36x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 58.5 ms: 1.35x faster                                               |
| genshi_xml               | 66.0 ms                                                | 48.8 ms: 1.35x faster                                               |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                              |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.33x faster                                                |
| scimark_fft              | 466 ms                                                 | 354 ms: 1.32x faster                                                |
| sympy_str                | 346 ms                                                 | 266 ms: 1.30x faster                                                |
| nqueens                  | 106 ms                                                 | 81.8 ms: 1.29x faster                                               |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                              |
| fannkuch                 | 532 ms                                                 | 419 ms: 1.27x faster                                                |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                               |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                                |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.23x faster                                               |
| regex_v8                 | 27.8 ms                                                | 22.9 ms: 1.21x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.18x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 84.2 ms: 1.18x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 98.4 ms: 1.17x faster                                               |
| bench_thread_pool        | 986 us                                                 | 869 us: 1.13x faster                                                |
| async_generators         | 444 ms                                                 | 392 ms: 1.13x faster                                                |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.76 us: 1.10x faster                                               |
| json                     | 5.69 ms                                                | 5.28 ms: 1.08x faster                                               |
| json_loads               | 31.2 us                                                | 29.5 us: 1.06x faster                                               |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                |
| coverage                 | 79.4 ms                                                | 82.8 ms: 1.04x slower                                               |
| regex_effbot             | 3.63 ms                                                | 3.81 ms: 1.05x slower                                               |
| telco                    | 7.27 ms                                                | 7.89 ms: 1.09x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.85 ms: 1.34x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 8.19 ms: 1.38x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 82.9 ms: 3.45x slower                                               |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                        |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250403-3.14.0a6+-9e0e134/bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.462x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.28x