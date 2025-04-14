# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_10_6
- machine: linux-x86_64
- commit hash: 89bbf67
- commit date: 2025-03-29
- overall geometric mean: 1.439x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 267 ms: 1.31x faster                                                |
| docutils       | 3.30 sec                                               | 2.70 sec: 1.22x faster                                              |
| html5lib       | 88.9 ms                                                | 63.2 ms: 1.41x faster                                               |
| Geometric mean | (ref)                                                  | 1.31x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 616 ms: 2.87x faster                                                |
| async_tree_none         | 728 ms                                                 | 260 ms: 2.80x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 315 ms: 2.76x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 492 ms: 2.06x faster                                                |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 64.8 ms: 1.81x faster                                               |
| nbody          | 154 ms                                                 | 86.6 ms: 1.77x faster                                               |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.49x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                |
| regex_v8       | 27.8 ms                                                | 22.7 ms: 1.22x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.08 ms: 1.18x faster                                               |
| regex_dna      | 227 ms                                                 | 211 ms: 1.07x faster                                                |
| Geometric mean | (ref)                                                  | 1.23x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.89 sec: 1.66x faster                                              |
| unpickle_pure_python | 331 us                                                 | 211 us: 1.57x faster                                                |
| pickle_pure_python   | 484 us                                                 | 328 us: 1.48x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 56.7 ms: 1.40x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 80.2 ms: 1.24x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 98.7 ms: 1.17x faster                                               |
| json_loads           | 31.2 us                                                | 30.1 us: 1.04x faster                                               |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 8.23 ms: 1.39x slower                                               |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.8 ms: 1.52x faster                                               |
| genshi_text     | 31.8 ms                                                | 21.2 ms: 1.50x faster                                               |
| mako            | 16.3 ms                                                | 11.1 ms: 1.48x faster                                               |
| genshi_xml      | 66.0 ms                                                | 49.8 ms: 1.33x faster                                               |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.24x faster                                                |
| async_tree_io            | 1.77 sec                                               | 616 ms: 2.87x faster                                                |
| async_tree_none          | 728 ms                                                 | 260 ms: 2.80x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 315 ms: 2.76x faster                                                |
| generators               | 80.1 ms                                                | 29.0 ms: 2.76x faster                                               |
| deltablue                | 7.91 ms                                                | 3.03 ms: 2.61x faster                                               |
| richards_super           | 94.7 ms                                                | 42.8 ms: 2.21x faster                                               |
| richards                 | 79.3 ms                                                | 37.2 ms: 2.13x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 492 ms: 2.06x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 29.1 us: 2.01x faster                                               |
| pylint                   | 551 ms                                                 | 285 ms: 1.94x faster                                                |
| chaos                    | 115 ms                                                 | 59.8 ms: 1.93x faster                                               |
| raytrace                 | 507 ms                                                 | 267 ms: 1.90x faster                                                |
| logging_silent           | 190 ns                                                 | 100 ns: 1.89x faster                                                |
| go                       | 240 ms                                                 | 129 ms: 1.86x faster                                                |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                |
| deepcopy                 | 479 us                                                 | 265 us: 1.81x faster                                                |
| float                    | 117 ms                                                 | 64.8 ms: 1.81x faster                                               |
| nbody                    | 154 ms                                                 | 86.6 ms: 1.77x faster                                               |
| spectral_norm            | 170 ms                                                 | 97.4 ms: 1.74x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 68.5 ms: 1.73x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 76.0 ms: 1.68x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.89 sec: 1.66x faster                                              |
| pyflate                  | 716 ms                                                 | 443 ms: 1.62x faster                                                |
| comprehensions           | 28.8 us                                                | 18.4 us: 1.57x faster                                               |
| unpickle_pure_python     | 331 us                                                 | 211 us: 1.57x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                               |
| django_template          | 48.2 ms                                                | 31.8 ms: 1.52x faster                                               |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                               |
| genshi_text              | 31.8 ms                                                | 21.2 ms: 1.50x faster                                               |
| logging_simple           | 8.30 us                                                | 5.55 us: 1.50x faster                                               |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                               |
| pickle_pure_python       | 484 us                                                 | 328 us: 1.48x faster                                                |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.48x faster                                               |
| hexiom                   | 10.4 ms                                                | 7.04 ms: 1.48x faster                                               |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                |
| html5lib                 | 88.9 ms                                                | 63.2 ms: 1.41x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 56.7 ms: 1.40x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.65 ms: 1.39x faster                                               |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                              |
| dulwich_log              | 84.3 ms                                                | 61.0 ms: 1.38x faster                                               |
| thrift                   | 1.07 ms                                                | 776 us: 1.38x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 759 ms: 1.34x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.58 sec: 1.34x faster                                              |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.6 ms: 1.33x faster                                               |
| genshi_xml               | 66.0 ms                                                | 49.8 ms: 1.33x faster                                               |
| 2to3                     | 348 ms                                                 | 267 ms: 1.31x faster                                                |
| sympy_sum                | 196 ms                                                 | 155 ms: 1.27x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 20.4 ms: 1.27x faster                                               |
| fannkuch                 | 532 ms                                                 | 422 ms: 1.26x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 138 ms: 1.25x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 80.2 ms: 1.24x faster                                               |
| sympy_str                | 346 ms                                                 | 279 ms: 1.24x faster                                                |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                               |
| nqueens                  | 106 ms                                                 | 86.3 ms: 1.23x faster                                               |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.22x faster                                               |
| regex_v8                 | 27.8 ms                                                | 22.7 ms: 1.22x faster                                               |
| docutils                 | 3.30 sec                                               | 2.70 sec: 1.22x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                |
| sympy_expand             | 566 ms                                                 | 478 ms: 1.18x faster                                                |
| regex_effbot             | 3.63 ms                                                | 3.08 ms: 1.18x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 98.7 ms: 1.17x faster                                               |
| mdp                      | 2.85 sec                                               | 2.51 sec: 1.14x faster                                              |
| bench_thread_pool        | 986 us                                                 | 889 us: 1.11x faster                                                |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                               |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.76 us: 1.09x faster                                               |
| regex_dna                | 227 ms                                                 | 211 ms: 1.07x faster                                                |
| json                     | 5.69 ms                                                | 5.31 ms: 1.07x faster                                               |
| async_generators         | 444 ms                                                 | 415 ms: 1.07x faster                                                |
| json_loads               | 31.2 us                                                | 30.1 us: 1.04x faster                                               |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                |
| coverage                 | 79.4 ms                                                | 86.2 ms: 1.09x slower                                               |
| telco                    | 7.27 ms                                                | 8.16 ms: 1.12x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.82 ms: 1.33x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 8.23 ms: 1.39x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.54x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 83.4 ms: 3.47x slower                                               |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                        |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250329-3.14.0a6+-89bbf67-JIT/bm-20250329-linux-x86_64-brandtbucher-jit_up_10_6-3.14.0a6+-89bbf67.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.439x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.30x