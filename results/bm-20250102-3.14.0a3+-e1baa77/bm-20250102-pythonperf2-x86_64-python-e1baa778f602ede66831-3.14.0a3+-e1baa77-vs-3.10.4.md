# Results vs. 3.10.4

- fork: python
- ref: e1baa778f602ede66831
- machine: linux-x86_64
- commit hash: e1baa77
- commit date: 2025-01-02
- overall geometric mean: 1.341x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 281 ms: 1.25x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                       |
| html5lib       | 94.6 ms                                                      | 68.2 ms: 1.39x faster                                                        |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 635 ms: 2.52x faster                                                         |
| async_tree_none         | 692 ms                                                       | 289 ms: 2.39x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 352 ms: 2.33x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 513 ms: 1.82x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.25x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 72.1 ms: 1.54x faster                                                        |
| nbody          | 134 ms                                                       | 88.1 ms: 1.52x faster                                                        |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                         |
| Geometric mean | (ref)                                                        | 1.36x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 135 ms: 1.41x faster                                                         |
| regex_dna      | 261 ms                                                       | 235 ms: 1.11x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 26.4 ms: 1.03x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.19 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.12x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 208 us: 1.50x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.07 sec: 1.41x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 326 us: 1.40x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 58.5 ms: 1.30x faster                                                        |
| json_loads           | 30.3 us                                                      | 23.8 us: 1.28x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.5 ms: 1.27x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 135 ms: 1.19x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 94.5 ms: 1.17x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 82.4 ms: 1.12x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 36.2 ms: 1.39x faster                                                        |
| mako            | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 24.7 ms: 1.27x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 54.6 ms: 1.16x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.29x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 174 us: 3.08x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 635 ms: 2.52x faster                                                         |
| async_tree_none          | 692 ms                                                       | 289 ms: 2.39x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 352 ms: 2.33x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.39 ms: 2.21x faster                                                        |
| go                       | 262 ms                                                       | 127 ms: 2.05x faster                                                         |
| generators               | 57.3 ms                                                      | 29.5 ms: 1.94x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 513 ms: 1.82x faster                                                         |
| raytrace                 | 489 ms                                                       | 274 ms: 1.79x faster                                                         |
| pylint                   | 566 ms                                                       | 319 ms: 1.78x faster                                                         |
| richards_super           | 90.6 ms                                                      | 51.7 ms: 1.75x faster                                                        |
| scimark_lu               | 167 ms                                                       | 95.8 ms: 1.74x faster                                                        |
| chaos                    | 109 ms                                                       | 62.4 ms: 1.74x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 62.6 ms: 1.72x faster                                                        |
| logging_silent           | 167 ns                                                       | 98.4 ns: 1.70x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.33 ms: 1.69x faster                                                        |
| deepcopy                 | 468 us                                                       | 285 us: 1.64x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 30.4 us: 1.64x faster                                                        |
| richards                 | 75.1 ms                                                      | 46.0 ms: 1.63x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 73.7 ms: 1.62x faster                                                        |
| pyflate                  | 733 ms                                                       | 453 ms: 1.62x faster                                                         |
| spectral_norm            | 139 ms                                                       | 87.7 ms: 1.59x faster                                                        |
| scimark_sor              | 180 ms                                                       | 115 ms: 1.57x faster                                                         |
| sqlglot_transpile        | 2.68 ms                                                      | 1.73 ms: 1.55x faster                                                        |
| float                    | 111 ms                                                       | 72.1 ms: 1.54x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.15 ms: 1.53x faster                                                        |
| nbody                    | 134 ms                                                       | 88.1 ms: 1.52x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 208 us: 1.50x faster                                                         |
| comprehensions           | 26.7 us                                                      | 17.8 us: 1.50x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.0 ms: 1.44x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.31 us: 1.41x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.07 sec: 1.41x faster                                                       |
| regex_compile            | 190 ms                                                       | 135 ms: 1.41x faster                                                         |
| pickle_pure_python       | 455 us                                                       | 326 us: 1.40x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 2.88 us: 1.39x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 68.2 ms: 1.39x faster                                                        |
| django_template          | 50.2 ms                                                      | 36.2 ms: 1.39x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.00 us: 1.38x faster                                                        |
| thrift                   | 1.18 ms                                                      | 859 us: 1.37x faster                                                         |
| mako                     | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                       |
| fannkuch                 | 483 ms                                                       | 358 ms: 1.35x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 15.9 ms: 1.34x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.61 sec: 1.34x faster                                                       |
| sqlalchemy_declarative   | 190 ms                                                       | 143 ms: 1.33x faster                                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 796 ms: 1.32x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 58.5 ms: 1.30x faster                                                        |
| nqueens                  | 115 ms                                                       | 89.7 ms: 1.28x faster                                                        |
| json_loads               | 30.3 us                                                      | 23.8 us: 1.28x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 24.7 ms: 1.27x faster                                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.9 ms: 1.27x faster                                                        |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 11.5 ms: 1.27x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 115 ms: 1.25x faster                                                         |
| 2to3                     | 350 ms                                                       | 281 ms: 1.25x faster                                                         |
| sympy_str                | 360 ms                                                       | 292 ms: 1.23x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 936 us: 1.22x faster                                                         |
| scimark_fft              | 361 ms                                                       | 297 ms: 1.22x faster                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 57.7 ms: 1.22x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.2 ms: 1.21x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 67.3 ms: 1.21x faster                                                        |
| sympy_expand             | 600 ms                                                       | 498 ms: 1.20x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 135 ms: 1.19x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.55 sec: 1.18x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 94.5 ms: 1.17x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 54.6 ms: 1.16x faster                                                        |
| json                     | 5.86 ms                                                      | 5.09 ms: 1.15x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 82.4 ms: 1.12x faster                                                        |
| regex_dna                | 261 ms                                                       | 235 ms: 1.11x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.59 ms: 1.11x faster                                                        |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                                         |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.84 us: 1.05x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 26.4 ms: 1.03x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 387 ms: 1.01x faster                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.19 ms: 1.03x slower                                                        |
| async_generators         | 421 ms                                                       | 437 ms: 1.04x slower                                                         |
| telco                    | 7.23 ms                                                      | 7.90 ms: 1.09x slower                                                        |
| mypy2                    | 933 ms                                                       | 1.03 sec: 1.10x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                                        |
| coverage                 | 63.3 ms                                                      | 80.1 ms: 1.27x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.85 ms: 1.62x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.41 ms: 1.88x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.59 sec: 249.88x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                                 |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250102-3.14.0a3+-e1baa77/bm-20250102-pythonperf2-x86_64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.341x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.28x