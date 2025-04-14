# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_10_9
- machine: linux-x86_64
- commit hash: 07ab4d7
- commit date: 2025-03-28
- overall geometric mean: 1.431x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 266 ms: 1.31x faster                                                |
| docutils       | 3.30 sec                                               | 2.70 sec: 1.22x faster                                              |
| html5lib       | 88.9 ms                                                | 63.6 ms: 1.40x faster                                               |
| Geometric mean | (ref)                                                  | 1.31x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 619 ms: 2.86x faster                                                |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 323 ms: 2.69x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 495 ms: 2.05x faster                                                |
| Geometric mean          | (ref)                                                  | 2.57x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 66.1 ms: 1.77x faster                                               |
| nbody          | 154 ms                                                 | 88.0 ms: 1.74x faster                                               |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.47x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                |
| regex_v8       | 27.8 ms                                                | 23.5 ms: 1.18x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.40 ms: 1.07x faster                                               |
| regex_dna      | 227 ms                                                 | 214 ms: 1.06x faster                                                |
| Geometric mean | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.86 sec: 1.69x faster                                              |
| unpickle_pure_python | 331 us                                                 | 212 us: 1.56x faster                                                |
| pickle_pure_python   | 484 us                                                 | 325 us: 1.49x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 56.8 ms: 1.39x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 80.4 ms: 1.24x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 98.0 ms: 1.18x faster                                               |
| json_loads           | 31.2 us                                                | 29.6 us: 1.05x faster                                               |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 8.21 ms: 1.38x slower                                               |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.7 ms: 1.52x faster                                               |
| genshi_text     | 31.8 ms                                                | 21.3 ms: 1.49x faster                                               |
| mako            | 16.3 ms                                                | 11.0 ms: 1.49x faster                                               |
| genshi_xml      | 66.0 ms                                                | 50.6 ms: 1.30x faster                                               |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 173 us: 3.15x faster                                                |
| async_tree_io            | 1.77 sec                                               | 619 ms: 2.86x faster                                                |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                                |
| generators               | 80.1 ms                                                | 28.9 ms: 2.77x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 323 ms: 2.69x faster                                                |
| deltablue                | 7.91 ms                                                | 3.05 ms: 2.59x faster                                               |
| richards_super           | 94.7 ms                                                | 45.6 ms: 2.08x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 495 ms: 2.05x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 28.8 us: 2.03x faster                                               |
| pylint                   | 551 ms                                                 | 284 ms: 1.94x faster                                                |
| richards                 | 79.3 ms                                                | 40.8 ms: 1.94x faster                                               |
| chaos                    | 115 ms                                                 | 60.0 ms: 1.92x faster                                               |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                |
| go                       | 240 ms                                                 | 128 ms: 1.88x faster                                                |
| spectral_norm            | 170 ms                                                 | 91.9 ms: 1.85x faster                                               |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                |
| logging_silent           | 190 ns                                                 | 105 ns: 1.81x faster                                                |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.81x faster                                                |
| float                    | 117 ms                                                 | 66.1 ms: 1.77x faster                                               |
| nbody                    | 154 ms                                                 | 88.0 ms: 1.74x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 68.3 ms: 1.73x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 75.5 ms: 1.69x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.86 sec: 1.69x faster                                              |
| unpickle_pure_python     | 331 us                                                 | 212 us: 1.56x faster                                                |
| pyflate                  | 716 ms                                                 | 461 ms: 1.55x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                               |
| django_template          | 48.2 ms                                                | 31.7 ms: 1.52x faster                                               |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.51x faster                                                |
| comprehensions           | 28.8 us                                                | 19.1 us: 1.50x faster                                               |
| genshi_text              | 31.8 ms                                                | 21.3 ms: 1.49x faster                                               |
| pickle_pure_python       | 484 us                                                 | 325 us: 1.49x faster                                                |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.49x faster                                               |
| logging_simple           | 8.30 us                                                | 5.60 us: 1.48x faster                                               |
| coroutines               | 35.1 ms                                                | 23.7 ms: 1.48x faster                                               |
| logging_format           | 9.09 us                                                | 6.17 us: 1.47x faster                                               |
| hexiom                   | 10.4 ms                                                | 7.10 ms: 1.47x faster                                               |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                |
| html5lib                 | 88.9 ms                                                | 63.6 ms: 1.40x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 56.8 ms: 1.39x faster                                               |
| dulwich_log              | 84.3 ms                                                | 60.7 ms: 1.39x faster                                               |
| thrift                   | 1.07 ms                                                | 781 us: 1.37x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.36x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.81 ms: 1.35x faster                                               |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.4 ms: 1.34x faster                                               |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.34x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 769 ms: 1.32x faster                                                |
| 2to3                     | 348 ms                                                 | 266 ms: 1.31x faster                                                |
| genshi_xml               | 66.0 ms                                                | 50.6 ms: 1.30x faster                                               |
| sqlalchemy_declarative   | 172 ms                                                 | 136 ms: 1.27x faster                                                |
| sympy_sum                | 196 ms                                                 | 155 ms: 1.27x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 20.4 ms: 1.27x faster                                               |
| fannkuch                 | 532 ms                                                 | 427 ms: 1.24x faster                                                |
| sympy_str                | 346 ms                                                 | 279 ms: 1.24x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 80.4 ms: 1.24x faster                                               |
| nqueens                  | 106 ms                                                 | 85.8 ms: 1.23x faster                                               |
| docutils                 | 3.30 sec                                               | 2.70 sec: 1.22x faster                                              |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                               |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.21x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                |
| regex_v8                 | 27.8 ms                                                | 23.5 ms: 1.18x faster                                               |
| sympy_expand             | 566 ms                                                 | 479 ms: 1.18x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 98.0 ms: 1.18x faster                                               |
| mdp                      | 2.85 sec                                               | 2.49 sec: 1.14x faster                                              |
| bench_thread_pool        | 986 us                                                 | 888 us: 1.11x faster                                                |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.73 us: 1.11x faster                                               |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.09x faster                                                |
| async_generators         | 444 ms                                                 | 414 ms: 1.07x faster                                                |
| json                     | 5.69 ms                                                | 5.31 ms: 1.07x faster                                               |
| regex_effbot             | 3.63 ms                                                | 3.40 ms: 1.07x faster                                               |
| regex_dna                | 227 ms                                                 | 214 ms: 1.06x faster                                                |
| json_loads               | 31.2 us                                                | 29.6 us: 1.05x faster                                               |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                |
| telco                    | 7.27 ms                                                | 7.87 ms: 1.08x slower                                               |
| coverage                 | 79.4 ms                                                | 86.5 ms: 1.09x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.82 ms: 1.33x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 8.21 ms: 1.38x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.54x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 83.1 ms: 3.46x slower                                               |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                        |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250328-3.14.0a6+-07ab4d7-JIT/bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.431x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.29x