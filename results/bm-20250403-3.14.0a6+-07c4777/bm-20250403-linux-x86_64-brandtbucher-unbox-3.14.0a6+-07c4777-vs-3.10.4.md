# Results vs. 3.10.4

- fork: brandtbucher
- ref: unbox
- machine: linux-x86_64
- commit hash: 07c4777
- commit date: 2025-04-03
- overall geometric mean: 1.430x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                          |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                        |
| html5lib       | 88.9 ms                                                | 62.7 ms: 1.42x faster                                         |
| Geometric mean | (ref)                                                  | 1.34x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 631 ms: 2.80x faster                                          |
| async_tree_none         | 728 ms                                                 | 265 ms: 2.75x faster                                          |
| async_tree_memoization  | 870 ms                                                 | 322 ms: 2.70x faster                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 489 ms: 2.08x faster                                          |
| Geometric mean          | (ref)                                                  | 2.56x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 117 ms                                                 | 74.1 ms: 1.58x faster                                         |
| nbody          | 154 ms                                                 | 100 ms: 1.53x faster                                          |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                  | 1.35x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 131 ms: 1.44x faster                                          |
| regex_v8       | 27.8 ms                                                | 22.7 ms: 1.22x faster                                         |
| regex_effbot   | 3.63 ms                                                | 3.25 ms: 1.12x faster                                         |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                          |
| Geometric mean | (ref)                                                  | 1.19x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.86 sec: 1.69x faster                                        |
| pickle_pure_python   | 484 us                                                 | 323 us: 1.50x faster                                          |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                          |
| xml_etree_process    | 79.1 ms                                                | 59.8 ms: 1.32x faster                                         |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.25x faster                                         |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.18x faster                                          |
| xml_etree_generate   | 99.4 ms                                                | 85.2 ms: 1.17x faster                                         |
| xml_etree_iterparse  | 115 ms                                                 | 99.5 ms: 1.16x faster                                         |
| json_loads           | 31.2 us                                                | 34.2 us: 1.10x slower                                         |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                         |
| python_startup_no_site | 5.93 ms                                                | 8.20 ms: 1.38x slower                                         |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.4 ms: 1.49x faster                                         |
| genshi_text     | 31.8 ms                                                | 21.9 ms: 1.45x faster                                         |
| mako            | 16.3 ms                                                | 11.6 ms: 1.41x faster                                         |
| genshi_xml      | 66.0 ms                                                | 50.2 ms: 1.32x faster                                         |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                          |
| async_tree_io            | 1.77 sec                                               | 631 ms: 2.80x faster                                          |
| generators               | 80.1 ms                                                | 28.9 ms: 2.77x faster                                         |
| async_tree_none          | 728 ms                                                 | 265 ms: 2.75x faster                                          |
| async_tree_memoization   | 870 ms                                                 | 322 ms: 2.70x faster                                          |
| deltablue                | 7.91 ms                                                | 3.26 ms: 2.42x faster                                         |
| mdp                      | 2.85 sec                                               | 1.25 sec: 2.28x faster                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 489 ms: 2.08x faster                                          |
| chaos                    | 115 ms                                                 | 57.5 ms: 2.01x faster                                         |
| go                       | 240 ms                                                 | 120 ms: 2.01x faster                                          |
| pylint                   | 551 ms                                                 | 281 ms: 1.96x faster                                          |
| logging_silent           | 190 ns                                                 | 97.6 ns: 1.94x faster                                         |
| deepcopy_memo            | 58.5 us                                                | 30.4 us: 1.92x faster                                         |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.87x faster                                          |
| raytrace                 | 507 ms                                                 | 272 ms: 1.86x faster                                          |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                          |
| spectral_norm            | 170 ms                                                 | 92.5 ms: 1.84x faster                                         |
| richards_super           | 94.7 ms                                                | 51.6 ms: 1.84x faster                                         |
| richards                 | 79.3 ms                                                | 45.3 ms: 1.75x faster                                         |
| scimark_monte_carlo      | 118 ms                                                 | 68.2 ms: 1.73x faster                                         |
| hexiom                   | 10.4 ms                                                | 6.13 ms: 1.70x faster                                         |
| tomli_loads              | 3.14 sec                                               | 1.86 sec: 1.69x faster                                        |
| comprehensions           | 28.8 us                                                | 17.2 us: 1.67x faster                                         |
| coroutines               | 35.1 ms                                                | 21.2 ms: 1.65x faster                                         |
| float                    | 117 ms                                                 | 74.1 ms: 1.58x faster                                         |
| crypto_pyaes             | 128 ms                                                 | 82.1 ms: 1.56x faster                                         |
| pyflate                  | 716 ms                                                 | 461 ms: 1.55x faster                                          |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                         |
| nbody                    | 154 ms                                                 | 100 ms: 1.53x faster                                          |
| pickle_pure_python       | 484 us                                                 | 323 us: 1.50x faster                                          |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                          |
| django_template          | 48.2 ms                                                | 32.4 ms: 1.49x faster                                         |
| logging_simple           | 8.30 us                                                | 5.64 us: 1.47x faster                                         |
| logging_format           | 9.09 us                                                | 6.21 us: 1.46x faster                                         |
| genshi_text              | 31.8 ms                                                | 21.9 ms: 1.45x faster                                         |
| regex_compile            | 188 ms                                                 | 131 ms: 1.44x faster                                          |
| scimark_lu               | 176 ms                                                 | 124 ms: 1.42x faster                                          |
| dulwich_log              | 84.3 ms                                                | 59.4 ms: 1.42x faster                                         |
| html5lib                 | 88.9 ms                                                | 62.7 ms: 1.42x faster                                         |
| mako                     | 16.3 ms                                                | 11.6 ms: 1.41x faster                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.0 ms: 1.38x faster                                         |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                          |
| xml_etree_process        | 79.1 ms                                                | 59.8 ms: 1.32x faster                                         |
| pprint_pformat           | 2.10 sec                                               | 1.59 sec: 1.32x faster                                        |
| genshi_xml               | 66.0 ms                                                | 50.2 ms: 1.32x faster                                         |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                        |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.30x faster                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 132 ms: 1.30x faster                                          |
| pprint_safe_repr         | 1.02 sec                                               | 782 ms: 1.30x faster                                          |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                          |
| nqueens                  | 106 ms                                                 | 83.5 ms: 1.27x faster                                         |
| sympy_str                | 346 ms                                                 | 274 ms: 1.26x faster                                          |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.15 ms: 1.26x faster                                         |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.25x faster                                         |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.23x faster                                         |
| fannkuch                 | 532 ms                                                 | 435 ms: 1.22x faster                                          |
| regex_v8                 | 27.8 ms                                                | 22.7 ms: 1.22x faster                                         |
| scimark_fft              | 466 ms                                                 | 384 ms: 1.21x faster                                          |
| sympy_expand             | 566 ms                                                 | 470 ms: 1.20x faster                                          |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.18x faster                                          |
| xml_etree_generate       | 99.4 ms                                                | 85.2 ms: 1.17x faster                                         |
| xml_etree_iterparse      | 115 ms                                                 | 99.5 ms: 1.16x faster                                         |
| async_generators         | 444 ms                                                 | 394 ms: 1.12x faster                                          |
| regex_effbot             | 3.63 ms                                                | 3.25 ms: 1.12x faster                                         |
| bench_thread_pool        | 986 us                                                 | 885 us: 1.11x faster                                          |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                         |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                          |
| sqlite_synth             | 3.02 us                                                | 2.84 us: 1.06x faster                                         |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                          |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                          |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                          |
| json                     | 5.69 ms                                                | 5.86 ms: 1.03x slower                                         |
| coverage                 | 79.4 ms                                                | 84.7 ms: 1.07x slower                                         |
| telco                    | 7.27 ms                                                | 7.94 ms: 1.09x slower                                         |
| json_loads               | 31.2 us                                                | 34.2 us: 1.10x slower                                         |
| gc_traversal             | 3.62 ms                                                | 4.91 ms: 1.36x slower                                         |
| python_startup_no_site   | 5.93 ms                                                | 8.20 ms: 1.38x slower                                         |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.53x slower                                         |
| bench_mp_pool            | 24.0 ms                                                | 83.6 ms: 3.48x slower                                         |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                  |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250403-3.14.0a6+-07c4777/bm-20250403-linux-x86_64-brandtbucher-unbox-3.14.0a6+-07c4777.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.430x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.28x