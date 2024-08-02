# Results vs. 3.10.4

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-x86_64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 306 ms: 1.14x faster                                                        |
| chameleon      | 9.44 ms                                                      | 8.00 ms: 1.18x faster                                                       |
| docutils       | 3.41 sec                                                     | 3.15 sec: 1.08x faster                                                      |
| html5lib       | 94.6 ms                                                      | 72.8 ms: 1.30x faster                                                       |
| tornado_http   | 157 ms                                                       | 124 ms: 1.26x faster                                                        |
| Geometric mean | (ref)                                                        | 1.19x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 374 ms: 1.85x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 874 ms: 1.83x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 468 ms: 1.75x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 621 ms: 1.51x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.73x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 82.6 ms: 1.62x faster                                                       |
| float          | 111 ms                                                       | 73.6 ms: 1.51x faster                                                       |
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.38x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 141 ms: 1.35x faster                                                        |
| regex_dna      | 261 ms                                                       | 239 ms: 1.09x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.0 ms: 1.05x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.60 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 214 us: 1.46x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 321 us: 1.42x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.13 sec: 1.37x faster                                                      |
| xml_etree_process    | 75.9 ms                                                      | 58.3 ms: 1.30x faster                                                       |
| json_loads           | 30.3 us                                                      | 24.5 us: 1.24x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 81.4 ms: 1.13x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 99.6 ms: 1.11x faster                                                       |
| unpickle_list        | 4.65 us                                                      | 4.88 us: 1.05x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 32.2 us: 1.09x slower                                                       |
| unpickle             | 13.5 us                                                      | 14.8 us: 1.10x slower                                                       |
| pickle               | 9.89 us                                                      | 10.9 us: 1.11x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.68 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.17x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.43 ms: 1.29x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.23x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.11 ms: 1.61x faster                                                       |
| django_template | 50.2 ms                                                      | 43.4 ms: 1.16x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 29.3 ms: 1.07x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 68.7 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.16x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 186 us: 2.88x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 375 ms: 2.08x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.79 ms: 1.98x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| async_tree_none          | 692 ms                                                       | 374 ms: 1.85x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 874 ms: 1.83x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 468 ms: 1.75x faster                                                        |
| raytrace                 | 489 ms                                                       | 284 ms: 1.72x faster                                                        |
| richards_super           | 90.6 ms                                                      | 52.7 ms: 1.72x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 70.6 ms: 1.69x faster                                                       |
| spectral_norm            | 139 ms                                                       | 83.0 ms: 1.68x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 65.4 ms: 1.64x faster                                                       |
| generators               | 57.3 ms                                                      | 34.9 ms: 1.64x faster                                                       |
| chaos                    | 109 ms                                                       | 66.1 ms: 1.64x faster                                                       |
| richards                 | 75.1 ms                                                      | 46.0 ms: 1.63x faster                                                       |
| nbody                    | 134 ms                                                       | 82.6 ms: 1.62x faster                                                       |
| mako                     | 14.7 ms                                                      | 9.11 ms: 1.61x faster                                                       |
| go                       | 262 ms                                                       | 164 ms: 1.60x faster                                                        |
| logging_silent           | 167 ns                                                       | 105 ns: 1.60x faster                                                        |
| pyflate                  | 733 ms                                                       | 470 ms: 1.56x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.44 ms: 1.56x faster                                                       |
| float                    | 111 ms                                                       | 73.6 ms: 1.51x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 621 ms: 1.51x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.9 us: 1.49x faster                                                       |
| pylint                   | 566 ms                                                       | 383 ms: 1.48x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 214 us: 1.46x faster                                                        |
| scimark_lu               | 167 ms                                                       | 115 ms: 1.45x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.85 ms: 1.45x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.3 ms: 1.42x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 321 us: 1.42x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.68 ms: 1.41x faster                                                       |
| scimark_sor              | 180 ms                                                       | 130 ms: 1.39x faster                                                        |
| fannkuch                 | 483 ms                                                       | 350 ms: 1.38x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.13 sec: 1.37x faster                                                      |
| deepcopy_memo            | 49.8 us                                                      | 36.6 us: 1.36x faster                                                       |
| regex_compile            | 190 ms                                                       | 141 ms: 1.35x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 790 ms: 1.33x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 4.82 ms: 1.32x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                                      |
| pathlib                  | 21.4 ms                                                      | 16.2 ms: 1.31x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.76 us: 1.31x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.31x faster                                                      |
| xml_etree_process        | 75.9 ms                                                      | 58.3 ms: 1.30x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 72.8 ms: 1.30x faster                                                       |
| thrift                   | 1.18 ms                                                      | 910 us: 1.29x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.47 us: 1.29x faster                                                       |
| tornado_http             | 157 ms                                                       | 124 ms: 1.26x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.06 ms: 1.25x faster                                                       |
| scimark_fft              | 361 ms                                                       | 289 ms: 1.25x faster                                                        |
| json_loads               | 30.3 us                                                      | 24.5 us: 1.24x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 67.5 ms: 1.20x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 963 us: 1.18x faster                                                        |
| chameleon                | 9.44 ms                                                      | 8.00 ms: 1.18x faster                                                       |
| nqueens                  | 115 ms                                                       | 97.4 ms: 1.18x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.60 sec: 1.16x faster                                                      |
| django_template          | 50.2 ms                                                      | 43.4 ms: 1.16x faster                                                       |
| dask                     | 472 ms                                                       | 411 ms: 1.15x faster                                                        |
| sympy_sum                | 193 ms                                                       | 168 ms: 1.15x faster                                                        |
| 2to3                     | 350 ms                                                       | 306 ms: 1.14x faster                                                        |
| sympy_str                | 360 ms                                                       | 315 ms: 1.14x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 81.4 ms: 1.13x faster                                                       |
| json                     | 5.86 ms                                                      | 5.18 ms: 1.13x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| sympy_expand             | 600 ms                                                       | 535 ms: 1.12x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 99.6 ms: 1.11x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 130 ms: 1.10x faster                                                        |
| deepcopy                 | 468 us                                                       | 424 us: 1.10x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.67 us: 1.09x faster                                                       |
| regex_dna                | 261 ms                                                       | 239 ms: 1.09x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 64.4 ms: 1.09x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 26.0 ms: 1.09x faster                                                       |
| docutils                 | 3.41 sec                                                     | 3.15 sec: 1.08x faster                                                      |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 29.3 ms: 1.07x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.81 us: 1.07x faster                                                       |
| async_generators         | 421 ms                                                       | 396 ms: 1.06x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 26.0 ms: 1.05x faster                                                       |
| meteor_contest           | 138 ms                                                       | 134 ms: 1.04x faster                                                        |
| unpickle_list            | 4.65 us                                                      | 4.88 us: 1.05x slower                                                       |
| genshi_xml               | 63.3 ms                                                      | 68.7 ms: 1.09x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 32.2 us: 1.09x slower                                                       |
| unpickle                 | 13.5 us                                                      | 14.8 us: 1.10x slower                                                       |
| pickle                   | 9.89 us                                                      | 10.9 us: 1.11x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.96 ms: 1.11x slower                                                       |
| flaskblogging            | 4.39 ms                                                      | 4.96 ms: 1.13x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.68 us: 1.14x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.60 ms: 1.16x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.17x slower                                                       |
| coverage                 | 63.3 ms                                                      | 80.6 ms: 1.27x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.43 ms: 1.29x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.45 ms: 1.30x slower                                                       |
| telco                    | 7.23 ms                                                      | 174 ms: 24.02x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 1.23x