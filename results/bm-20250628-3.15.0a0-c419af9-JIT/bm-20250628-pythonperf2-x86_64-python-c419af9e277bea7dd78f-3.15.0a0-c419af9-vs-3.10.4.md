# Results vs. 3.10.4

- fork: python
- ref: c419af9e277bea7dd78f
- machine: linux-x86_64
- commit hash: c419af9
- commit date: 2025-06-28
- overall geometric mean: 1.387x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 286 ms: 1.23x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                      |
| html5lib       | 94.6 ms                                                      | 66.7 ms: 1.42x faster                                                       |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 626 ms: 2.55x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 330 ms: 2.48x faster                                                        |
| async_tree_none         | 692 ms                                                       | 284 ms: 2.44x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 503 ms: 1.86x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.32x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 64.7 ms: 1.72x faster                                                       |
| nbody          | 134 ms                                                       | 99.6 ms: 1.35x faster                                                       |
| pidigits       | 271 ms                                                       | 257 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                        | 1.35x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 132 ms: 1.43x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 23.1 ms: 1.17x faster                                                       |
| regex_dna      | 261 ms                                                       | 223 ms: 1.17x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.55 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                        | 1.14x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 194 us: 1.61x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 1.94 sec: 1.50x faster                                                      |
| pickle_pure_python   | 455 us                                                       | 340 us: 1.34x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 56.8 ms: 1.34x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 11.3 ms: 1.29x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.21x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 133 ms: 1.20x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 95.8 ms: 1.15x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 80.2 ms: 1.15x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.82 ms: 1.20x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                       |
| django_template | 50.2 ms                                                      | 35.6 ms: 1.41x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 23.4 ms: 1.35x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 54.4 ms: 1.16x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.33x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 168 us: 3.19x faster                                                        |
| deltablue                | 7.50 ms                                                      | 2.89 ms: 2.60x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 626 ms: 2.55x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 330 ms: 2.48x faster                                                        |
| async_tree_none          | 692 ms                                                       | 284 ms: 2.44x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.30 sec: 2.32x faster                                                      |
| richards_super           | 90.6 ms                                                      | 42.1 ms: 2.15x faster                                                       |
| richards                 | 75.1 ms                                                      | 35.1 ms: 2.14x faster                                                       |
| go                       | 262 ms                                                       | 129 ms: 2.03x faster                                                        |
| generators               | 57.3 ms                                                      | 29.6 ms: 1.94x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 503 ms: 1.86x faster                                                        |
| chaos                    | 109 ms                                                       | 60.2 ms: 1.80x faster                                                       |
| pyflate                  | 733 ms                                                       | 407 ms: 1.80x faster                                                        |
| logging_silent           | 167 ns                                                       | 93.2 ns: 1.79x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 28.0 us: 1.78x faster                                                       |
| scimark_sor              | 180 ms                                                       | 103 ms: 1.75x faster                                                        |
| pylint                   | 566 ms                                                       | 324 ms: 1.74x faster                                                        |
| scimark_lu               | 167 ms                                                       | 96.9 ms: 1.72x faster                                                       |
| raytrace                 | 489 ms                                                       | 284 ms: 1.72x faster                                                        |
| float                    | 111 ms                                                       | 64.7 ms: 1.72x faster                                                       |
| spectral_norm            | 139 ms                                                       | 81.1 ms: 1.72x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 63.0 ms: 1.70x faster                                                       |
| deepcopy                 | 468 us                                                       | 275 us: 1.70x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 194 us: 1.61x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.12 ms: 1.54x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.4 us: 1.53x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 78.1 ms: 1.53x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 1.94 sec: 1.50x faster                                                      |
| logging_simple           | 8.88 us                                                      | 5.96 us: 1.49x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.52 us: 1.48x faster                                                       |
| regex_compile            | 190 ms                                                       | 132 ms: 1.43x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 66.7 ms: 1.42x faster                                                       |
| thrift                   | 1.18 ms                                                      | 832 us: 1.41x faster                                                        |
| django_template          | 50.2 ms                                                      | 35.6 ms: 1.41x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.55 sec: 1.39x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 764 ms: 1.37x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 59.4 ms: 1.36x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.95 us: 1.36x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.4 ms: 1.35x faster                                                       |
| nbody                    | 134 ms                                                       | 99.6 ms: 1.35x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                      |
| genshi_text              | 31.4 ms                                                      | 23.4 ms: 1.35x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 340 us: 1.34x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 56.8 ms: 1.34x faster                                                       |
| fannkuch                 | 483 ms                                                       | 372 ms: 1.30x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.3 ms: 1.29x faster                                                       |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 17.0 ms: 1.26x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 22.4 ms: 1.26x faster                                                       |
| nqueens                  | 115 ms                                                       | 92.7 ms: 1.24x faster                                                       |
| sympy_str                | 360 ms                                                       | 292 ms: 1.23x faster                                                        |
| 2to3                     | 350 ms                                                       | 286 ms: 1.23x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.0 us: 1.21x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 133 ms: 1.20x faster                                                        |
| sympy_expand             | 600 ms                                                       | 500 ms: 1.20x faster                                                        |
| scimark_fft              | 361 ms                                                       | 303 ms: 1.19x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 23.1 ms: 1.17x faster                                                       |
| regex_dna                | 261 ms                                                       | 223 ms: 1.17x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                      |
| genshi_xml               | 63.3 ms                                                      | 54.4 ms: 1.16x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 95.8 ms: 1.15x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 80.2 ms: 1.15x faster                                                       |
| meteor_contest           | 138 ms                                                       | 122 ms: 1.13x faster                                                        |
| json                     | 5.86 ms                                                      | 5.27 ms: 1.11x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.83 us: 1.06x faster                                                       |
| pidigits                 | 271 ms                                                       | 257 ms: 1.05x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.01 ms: 1.01x faster                                                       |
| async_generators         | 421 ms                                                       | 443 ms: 1.05x slower                                                        |
| telco                    | 7.23 ms                                                      | 7.79 ms: 1.08x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.55 ms: 1.15x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.82 ms: 1.20x slower                                                       |
| coverage                 | 63.3 ms                                                      | 78.5 ms: 1.24x slower                                                       |
| python_startup           | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.82 ms: 1.60x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.42 ms: 1.88x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.39x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250628-3.15.0a0-c419af9-JIT/bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.387x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.39x