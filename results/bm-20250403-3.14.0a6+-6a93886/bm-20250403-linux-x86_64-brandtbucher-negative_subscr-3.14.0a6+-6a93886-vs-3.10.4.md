# Results vs. 3.10.4

- fork: brandtbucher
- ref: negative_subscr
- machine: linux-x86_64
- commit hash: 6a93886
- commit date: 2025-04-03
- overall geometric mean: 1.461x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 249 ms: 1.40x faster                                                    |
| docutils       | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                  |
| html5lib       | 88.9 ms                                                | 60.6 ms: 1.47x faster                                                   |
| Geometric mean | (ref)                                                  | 1.38x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 616 ms: 2.87x faster                                                    |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 314 ms: 2.77x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 490 ms: 2.07x faster                                                    |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 69.1 ms: 1.70x faster                                                   |
| nbody          | 154 ms                                                 | 93.9 ms: 1.63x faster                                                   |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                  | 1.42x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.50x faster                                                    |
| regex_v8       | 27.8 ms                                                | 23.0 ms: 1.21x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.31 ms: 1.10x faster                                                   |
| regex_dna      | 227 ms                                                 | 219 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                  | 1.20x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.63x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.54x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 58.5 ms: 1.35x faster                                                   |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 83.6 ms: 1.19x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                    |
| xml_etree_iterparse  | 115 ms                                                 | 99.1 ms: 1.16x faster                                                   |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 8.18 ms: 1.38x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                   |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                   |
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 49.0 ms: 1.35x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.33x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 616 ms: 2.87x faster                                                    |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 314 ms: 2.77x faster                                                    |
| generators               | 80.1 ms                                                | 30.7 ms: 2.61x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.34 ms: 2.37x faster                                                   |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.33x faster                                                  |
| go                       | 240 ms                                                 | 112 ms: 2.14x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 490 ms: 2.07x faster                                                    |
| chaos                    | 115 ms                                                 | 56.8 ms: 2.03x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 28.9 us: 2.03x faster                                                   |
| pylint                   | 551 ms                                                 | 279 ms: 1.98x faster                                                    |
| raytrace                 | 507 ms                                                 | 259 ms: 1.96x faster                                                    |
| logging_silent           | 190 ns                                                 | 98.3 ns: 1.93x faster                                                   |
| richards_super           | 94.7 ms                                                | 49.2 ms: 1.92x faster                                                   |
| deepcopy                 | 479 us                                                 | 251 us: 1.91x faster                                                    |
| scimark_sor              | 220 ms                                                 | 116 ms: 1.90x faster                                                    |
| richards                 | 79.3 ms                                                | 42.9 ms: 1.85x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 65.8 ms: 1.80x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 73.1 ms: 1.75x faster                                                   |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                   |
| spectral_norm            | 170 ms                                                 | 98.7 ms: 1.72x faster                                                   |
| float                    | 117 ms                                                 | 69.1 ms: 1.70x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.24 ms: 1.67x faster                                                   |
| nbody                    | 154 ms                                                 | 93.9 ms: 1.63x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.63x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.61 us: 1.60x faster                                                   |
| pyflate                  | 716 ms                                                 | 453 ms: 1.58x faster                                                    |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.54x faster                                                    |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                                    |
| django_template          | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                   |
| regex_compile            | 188 ms                                                 | 126 ms: 1.50x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.53 us: 1.50x faster                                                   |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                                   |
| logging_format           | 9.09 us                                                | 6.15 us: 1.48x faster                                                   |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                   |
| html5lib                 | 88.9 ms                                                | 60.6 ms: 1.47x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 58.6 ms: 1.44x faster                                                   |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 722 ms: 1.41x faster                                                    |
| 2to3                     | 348 ms                                                 | 249 ms: 1.40x faster                                                    |
| scimark_fft              | 466 ms                                                 | 339 ms: 1.37x faster                                                    |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.1 ms: 1.37x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 58.5 ms: 1.35x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 49.0 ms: 1.35x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 19.2 ms: 1.35x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.81 ms: 1.34x faster                                                   |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                    |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.31x faster                                                    |
| nqueens                  | 106 ms                                                 | 81.9 ms: 1.29x faster                                                   |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                    |
| fannkuch                 | 532 ms                                                 | 413 ms: 1.29x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                   |
| sympy_expand             | 566 ms                                                 | 458 ms: 1.23x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 23.0 ms: 1.21x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 83.6 ms: 1.19x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 99.1 ms: 1.16x faster                                                   |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                    |
| bench_thread_pool        | 986 us                                                 | 883 us: 1.12x faster                                                    |
| async_generators         | 444 ms                                                 | 398 ms: 1.12x faster                                                    |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.31 ms: 1.10x faster                                                   |
| json                     | 5.69 ms                                                | 5.36 ms: 1.06x faster                                                   |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                                   |
| regex_dna                | 227 ms                                                 | 219 ms: 1.04x faster                                                    |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                    |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                    |
| coverage                 | 79.4 ms                                                | 85.6 ms: 1.08x slower                                                   |
| telco                    | 7.27 ms                                                | 7.87 ms: 1.08x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 8.18 ms: 1.38x slower                                                   |
| gc_traversal             | 3.62 ms                                                | 5.07 ms: 1.40x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                                   |
| bench_mp_pool            | 24.0 ms                                                | 83.2 ms: 3.46x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                            |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250403-3.14.0a6+-6a93886/bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.461x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.29x