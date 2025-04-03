# Results vs. 3.10.4

- fork: iritkatriel
- ref: subscr_stats
- machine: linux-x86_64
- commit hash: ebd800a
- commit date: 2025-04-03
- overall geometric mean: 1.454x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.36x faster                                                |
| docutils       | 3.30 sec                                               | 2.60 sec: 1.27x faster                                              |
| html5lib       | 88.9 ms                                                | 61.9 ms: 1.44x faster                                               |
| Geometric mean | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 617 ms: 2.87x faster                                                |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 315 ms: 2.76x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 486 ms: 2.09x faster                                                |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.4 ms: 1.66x faster                                               |
| nbody          | 154 ms                                                 | 96.6 ms: 1.59x faster                                               |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.39x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.49x faster                                                |
| regex_v8       | 27.8 ms                                                | 22.8 ms: 1.22x faster                                               |
| regex_dna      | 227 ms                                                 | 207 ms: 1.09x faster                                                |
| regex_effbot   | 3.63 ms                                                | 3.76 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.59x faster                                              |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                                |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.50x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 58.9 ms: 1.34x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.22x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.20x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 84.8 ms: 1.17x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 98.6 ms: 1.17x faster                                               |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                               |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 8.17 ms: 1.38x slower                                               |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.3 ms: 1.50x faster                                               |
| django_template | 48.2 ms                                                | 32.2 ms: 1.50x faster                                               |
| mako            | 16.3 ms                                                | 11.4 ms: 1.44x faster                                               |
| genshi_xml      | 66.0 ms                                                | 49.5 ms: 1.33x faster                                               |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.31x faster                                                |
| async_tree_io            | 1.77 sec                                               | 617 ms: 2.87x faster                                                |
| generators               | 80.1 ms                                                | 28.6 ms: 2.81x faster                                               |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 315 ms: 2.76x faster                                                |
| deltablue                | 7.91 ms                                                | 3.16 ms: 2.50x faster                                               |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.33x faster                                              |
| go                       | 240 ms                                                 | 114 ms: 2.11x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 486 ms: 2.09x faster                                                |
| chaos                    | 115 ms                                                 | 57.9 ms: 1.99x faster                                               |
| pylint                   | 551 ms                                                 | 278 ms: 1.98x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 29.8 us: 1.96x faster                                               |
| raytrace                 | 507 ms                                                 | 265 ms: 1.91x faster                                                |
| logging_silent           | 190 ns                                                 | 101 ns: 1.89x faster                                                |
| richards_super           | 94.7 ms                                                | 50.3 ms: 1.88x faster                                               |
| deepcopy                 | 479 us                                                 | 255 us: 1.88x faster                                                |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.87x faster                                                |
| richards                 | 79.3 ms                                                | 44.2 ms: 1.79x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 67.2 ms: 1.76x faster                                               |
| spectral_norm            | 170 ms                                                 | 97.7 ms: 1.74x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 73.8 ms: 1.73x faster                                               |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                               |
| float                    | 117 ms                                                 | 70.4 ms: 1.66x faster                                               |
| hexiom                   | 10.4 ms                                                | 6.33 ms: 1.64x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.59x faster                                              |
| nbody                    | 154 ms                                                 | 96.6 ms: 1.59x faster                                               |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                               |
| pyflate                  | 716 ms                                                 | 468 ms: 1.53x faster                                                |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                                |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.50x faster                                                |
| genshi_text              | 31.8 ms                                                | 21.3 ms: 1.50x faster                                               |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.50x faster                                               |
| regex_compile            | 188 ms                                                 | 126 ms: 1.49x faster                                                |
| logging_simple           | 8.30 us                                                | 5.62 us: 1.48x faster                                               |
| logging_format           | 9.09 us                                                | 6.23 us: 1.46x faster                                               |
| dulwich_log              | 84.3 ms                                                | 58.1 ms: 1.45x faster                                               |
| coroutines               | 35.1 ms                                                | 24.3 ms: 1.44x faster                                               |
| html5lib                 | 88.9 ms                                                | 61.9 ms: 1.44x faster                                               |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.44x faster                                               |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.7 ms: 1.40x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.40x faster                                              |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 742 ms: 1.37x faster                                                |
| 2to3                     | 348 ms                                                 | 255 ms: 1.36x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.77 ms: 1.36x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 19.1 ms: 1.35x faster                                               |
| scimark_fft              | 466 ms                                                 | 346 ms: 1.35x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 58.9 ms: 1.34x faster                                               |
| genshi_xml               | 66.0 ms                                                | 49.5 ms: 1.33x faster                                               |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.32x faster                                                |
| sympy_str                | 346 ms                                                 | 267 ms: 1.30x faster                                                |
| nqueens                  | 106 ms                                                 | 82.8 ms: 1.28x faster                                               |
| docutils                 | 3.30 sec                                               | 2.60 sec: 1.27x faster                                              |
| fannkuch                 | 532 ms                                                 | 426 ms: 1.25x faster                                                |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                               |
| sympy_expand             | 566 ms                                                 | 458 ms: 1.24x faster                                                |
| regex_v8                 | 27.8 ms                                                | 22.8 ms: 1.22x faster                                               |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.22x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.20x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 84.8 ms: 1.17x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 98.6 ms: 1.17x faster                                               |
| bench_thread_pool        | 986 us                                                 | 871 us: 1.13x faster                                                |
| async_generators         | 444 ms                                                 | 392 ms: 1.13x faster                                                |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.76 us: 1.09x faster                                               |
| regex_dna                | 227 ms                                                 | 207 ms: 1.09x faster                                                |
| json                     | 5.69 ms                                                | 5.27 ms: 1.08x faster                                               |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                               |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                |
| regex_effbot             | 3.63 ms                                                | 3.76 ms: 1.04x slower                                               |
| coverage                 | 79.4 ms                                                | 84.5 ms: 1.06x slower                                               |
| telco                    | 7.27 ms                                                | 7.86 ms: 1.08x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.82 ms: 1.33x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 8.17 ms: 1.38x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.53x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 82.9 ms: 3.45x slower                                               |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                        |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250403-3.14.0a6+-ebd800a/bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.454x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.29x