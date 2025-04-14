# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_11_9
- machine: linux-x86_64
- commit hash: 9ab9d22
- commit date: 2025-03-27
- overall geometric mean: 1.438x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_9-3.14.0a6+-9ab9d22 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 266 ms: 1.31x faster                                                |
| docutils       | 3.30 sec                                               | 2.71 sec: 1.22x faster                                              |
| html5lib       | 88.9 ms                                                | 63.2 ms: 1.40x faster                                               |
| Geometric mean | (ref)                                                  | 1.31x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_9-3.14.0a6+-9ab9d22 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 620 ms: 2.85x faster                                                |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 315 ms: 2.76x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 494 ms: 2.06x faster                                                |
| Geometric mean          | (ref)                                                  | 2.59x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_9-3.14.0a6+-9ab9d22 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.2 ms: 1.79x faster                                               |
| nbody          | 154 ms                                                 | 88.0 ms: 1.75x faster                                               |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.48x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_9-3.14.0a6+-9ab9d22 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.47x faster                                                |
| regex_v8       | 27.8 ms                                                | 23.4 ms: 1.19x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.26 ms: 1.11x faster                                               |
| regex_dna      | 227 ms                                                 | 215 ms: 1.05x faster                                                |
| Geometric mean | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_9-3.14.0a6+-9ab9d22 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.87 sec: 1.68x faster                                              |
| unpickle_pure_python | 331 us                                                 | 212 us: 1.56x faster                                                |
| pickle_pure_python   | 484 us                                                 | 324 us: 1.50x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 56.9 ms: 1.39x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 80.9 ms: 1.23x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 97.8 ms: 1.18x faster                                               |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                               |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_9-3.14.0a6+-9ab9d22 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 8.18 ms: 1.38x slower                                               |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_9-3.14.0a6+-9ab9d22 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.4 ms: 1.49x faster                                               |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                               |
| mako            | 16.3 ms                                                | 11.1 ms: 1.48x faster                                               |
| genshi_xml      | 66.0 ms                                                | 49.3 ms: 1.34x faster                                               |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_9-3.14.0a6+-9ab9d22 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.22x faster                                                |
| async_tree_io            | 1.77 sec                                               | 620 ms: 2.85x faster                                                |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                                |
| generators               | 80.1 ms                                                | 29.0 ms: 2.77x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 315 ms: 2.76x faster                                                |
| deltablue                | 7.91 ms                                                | 3.04 ms: 2.60x faster                                               |
| richards_super           | 94.7 ms                                                | 43.8 ms: 2.16x faster                                               |
| richards                 | 79.3 ms                                                | 37.8 ms: 2.09x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 494 ms: 2.06x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 28.8 us: 2.03x faster                                               |
| logging_silent           | 190 ns                                                 | 95.5 ns: 1.99x faster                                               |
| pylint                   | 551 ms                                                 | 282 ms: 1.95x faster                                                |
| chaos                    | 115 ms                                                 | 59.7 ms: 1.93x faster                                               |
| raytrace                 | 507 ms                                                 | 265 ms: 1.91x faster                                                |
| go                       | 240 ms                                                 | 127 ms: 1.89x faster                                                |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.87x faster                                                |
| deepcopy                 | 479 us                                                 | 266 us: 1.80x faster                                                |
| float                    | 117 ms                                                 | 65.2 ms: 1.79x faster                                               |
| spectral_norm            | 170 ms                                                 | 96.3 ms: 1.76x faster                                               |
| nbody                    | 154 ms                                                 | 88.0 ms: 1.75x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 68.1 ms: 1.73x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 75.4 ms: 1.69x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.87 sec: 1.68x faster                                              |
| pyflate                  | 716 ms                                                 | 435 ms: 1.65x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 212 us: 1.56x faster                                                |
| comprehensions           | 28.8 us                                                | 18.6 us: 1.54x faster                                               |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                                |
| hexiom                   | 10.4 ms                                                | 6.86 ms: 1.52x faster                                               |
| deepcopy_reduce          | 4.17 us                                                | 2.77 us: 1.51x faster                                               |
| scimark_fft              | 466 ms                                                 | 311 ms: 1.50x faster                                                |
| pickle_pure_python       | 484 us                                                 | 324 us: 1.50x faster                                                |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.49x faster                                               |
| logging_simple           | 8.30 us                                                | 5.58 us: 1.49x faster                                               |
| django_template          | 48.2 ms                                                | 32.4 ms: 1.49x faster                                               |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                               |
| logging_format           | 9.09 us                                                | 6.15 us: 1.48x faster                                               |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.48x faster                                               |
| regex_compile            | 188 ms                                                 | 129 ms: 1.47x faster                                                |
| html5lib                 | 88.9 ms                                                | 63.2 ms: 1.40x faster                                               |
| dulwich_log              | 84.3 ms                                                | 60.3 ms: 1.40x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 56.9 ms: 1.39x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.67 ms: 1.38x faster                                               |
| thrift                   | 1.07 ms                                                | 790 us: 1.36x faster                                                |
| genshi_xml               | 66.0 ms                                                | 49.3 ms: 1.34x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                              |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.5 ms: 1.33x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 764 ms: 1.33x faster                                                |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.33x faster                                              |
| 2to3                     | 348 ms                                                 | 266 ms: 1.31x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 135 ms: 1.28x faster                                                |
| sympy_sum                | 196 ms                                                 | 154 ms: 1.27x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 20.3 ms: 1.27x faster                                               |
| fannkuch                 | 532 ms                                                 | 424 ms: 1.25x faster                                                |
| sympy_str                | 346 ms                                                 | 276 ms: 1.25x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 80.9 ms: 1.23x faster                                               |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.23x faster                                               |
| nqueens                  | 106 ms                                                 | 86.4 ms: 1.22x faster                                               |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                               |
| docutils                 | 3.30 sec                                               | 2.71 sec: 1.22x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                |
| regex_v8                 | 27.8 ms                                                | 23.4 ms: 1.19x faster                                               |
| sympy_expand             | 566 ms                                                 | 477 ms: 1.19x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 97.8 ms: 1.18x faster                                               |
| mdp                      | 2.85 sec                                               | 2.53 sec: 1.13x faster                                              |
| bench_thread_pool        | 986 us                                                 | 879 us: 1.12x faster                                                |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                               |
| regex_effbot             | 3.63 ms                                                | 3.26 ms: 1.11x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.72 us: 1.11x faster                                               |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                                |
| async_generators         | 444 ms                                                 | 416 ms: 1.07x faster                                                |
| json                     | 5.69 ms                                                | 5.35 ms: 1.06x faster                                               |
| regex_dna                | 227 ms                                                 | 215 ms: 1.05x faster                                                |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                               |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                |
| coverage                 | 79.4 ms                                                | 86.1 ms: 1.08x slower                                               |
| telco                    | 7.27 ms                                                | 8.04 ms: 1.11x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.85 ms: 1.34x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 8.18 ms: 1.38x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.54x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 82.9 ms: 3.45x slower                                               |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                        |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250327-3.14.0a6+-9ab9d22-JIT/bm-20250327-linux-x86_64-brandtbucher-jit_up_11_9-3.14.0a6+-9ab9d22.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.438x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.30x