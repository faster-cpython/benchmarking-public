# Results vs. 3.10.4

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-x86_64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.07x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 343 ms: 1.02x faster                                                        |
| chameleon      | 9.44 ms                                                      | 8.61 ms: 1.10x faster                                                       |
| docutils       | 3.41 sec                                                     | 3.46 sec: 1.01x slower                                                      |
| html5lib       | 94.6 ms                                                      | 84.5 ms: 1.12x faster                                                       |
| tornado_http   | 157 ms                                                       | 129 ms: 1.22x faster                                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 898 ms: 1.78x faster                                                        |
| async_tree_none         | 692 ms                                                       | 389 ms: 1.78x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 491 ms: 1.67x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 642 ms: 1.46x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.67x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 95.7 ms: 1.16x faster                                                       |
| nbody          | 134 ms                                                       | 123 ms: 1.09x faster                                                        |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 239 ms: 1.09x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.1 ms: 1.04x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.46 ms: 1.12x slower                                                       |
| regex_compile  | 190 ms                                                       | 214 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                       |
| json_loads           | 30.3 us                                                      | 24.6 us: 1.23x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 67.8 ms: 1.12x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.11x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 440 us: 1.04x faster                                                        |
| unpickle_pure_python | 312 us                                                       | 308 us: 1.01x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.88 sec: 1.01x faster                                                      |
| unpickle_list        | 4.65 us                                                      | 4.68 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 113 ms: 1.02x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 30.7 us: 1.04x slower                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 96.4 ms: 1.04x slower                                                       |
| pickle               | 9.89 us                                                      | 10.5 us: 1.06x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.49 us: 1.09x slower                                                       |
| unpickle             | 13.5 us                                                      | 15.4 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 12.9 ms: 1.12x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 8.90 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.17x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 45.8 ms: 1.10x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 32.7 ms: 1.04x slower                                                       |
| genshi_xml      | 63.3 ms                                                      | 69.9 ms: 1.10x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 200 us: 2.68x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 387 ms: 2.02x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.60 sec: 1.94x faster                                                      |
| async_tree_io            | 1.60 sec                                                     | 898 ms: 1.78x faster                                                        |
| async_tree_none          | 692 ms                                                       | 389 ms: 1.78x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 491 ms: 1.67x faster                                                        |
| generators               | 57.3 ms                                                      | 34.6 ms: 1.66x faster                                                       |
| deltablue                | 7.50 ms                                                      | 4.56 ms: 1.64x faster                                                       |
| raytrace                 | 489 ms                                                       | 333 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 642 ms: 1.46x faster                                                        |
| pylint                   | 566 ms                                                       | 396 ms: 1.43x faster                                                        |
| richards_super           | 90.6 ms                                                      | 66.9 ms: 1.35x faster                                                       |
| chaos                    | 109 ms                                                       | 80.5 ms: 1.35x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.70 us: 1.32x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.9 ms: 1.32x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.36 us: 1.31x faster                                                       |
| go                       | 262 ms                                                       | 203 ms: 1.29x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 93.0 ms: 1.28x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.75 ms: 1.28x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 5.02 ms: 1.27x faster                                                       |
| thrift                   | 1.18 ms                                                      | 927 us: 1.27x faster                                                        |
| richards                 | 75.1 ms                                                      | 59.3 ms: 1.27x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 17.1 ms: 1.25x faster                                                       |
| json_loads               | 30.3 us                                                      | 24.6 us: 1.23x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 2.20 ms: 1.22x faster                                                       |
| tornado_http             | 157 ms                                                       | 129 ms: 1.22x faster                                                        |
| scimark_lu               | 167 ms                                                       | 138 ms: 1.21x faster                                                        |
| float                    | 111 ms                                                       | 95.7 ms: 1.16x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.46 sec: 1.15x faster                                                      |
| pyflate                  | 733 ms                                                       | 645 ms: 1.14x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 84.5 ms: 1.12x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 67.8 ms: 1.12x faster                                                       |
| dask                     | 472 ms                                                       | 423 ms: 1.12x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 1.03 ms: 1.11x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 145 ms: 1.11x faster                                                        |
| django_template          | 50.2 ms                                                      | 45.8 ms: 1.10x faster                                                       |
| chameleon                | 9.44 ms                                                      | 8.61 ms: 1.10x faster                                                       |
| nbody                    | 134 ms                                                       | 123 ms: 1.09x faster                                                        |
| regex_dna                | 261 ms                                                       | 239 ms: 1.09x faster                                                        |
| scimark_sor              | 180 ms                                                       | 166 ms: 1.09x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 98.8 ms: 1.09x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.78 sec: 1.08x faster                                                      |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                        |
| json                     | 5.86 ms                                                      | 5.53 ms: 1.06x faster                                                       |
| logging_silent           | 167 ns                                                       | 161 ns: 1.04x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 26.1 ms: 1.04x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 78.3 ms: 1.04x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 440 us: 1.04x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 2.09 sec: 1.03x faster                                                      |
| sqlite_synth             | 2.99 us                                                      | 2.91 us: 1.03x faster                                                       |
| async_generators         | 421 ms                                                       | 411 ms: 1.02x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 1.03 sec: 1.02x faster                                                      |
| 2to3                     | 350 ms                                                       | 343 ms: 1.02x faster                                                        |
| sympy_sum                | 193 ms                                                       | 189 ms: 1.02x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 308 us: 1.01x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 142 ms: 1.01x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.88 sec: 1.01x faster                                                      |
| sympy_integrate          | 28.2 ms                                                      | 28.3 ms: 1.00x slower                                                       |
| unpickle_list            | 4.65 us                                                      | 4.68 us: 1.01x slower                                                       |
| deepcopy                 | 468 us                                                       | 473 us: 1.01x slower                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 71.0 ms: 1.01x slower                                                       |
| docutils                 | 3.41 sec                                                     | 3.46 sec: 1.01x slower                                                      |
| xml_etree_iterparse      | 110 ms                                                       | 113 ms: 1.02x slower                                                        |
| sympy_str                | 360 ms                                                       | 370 ms: 1.03x slower                                                        |
| nqueens                  | 115 ms                                                       | 119 ms: 1.03x slower                                                        |
| comprehensions           | 26.7 us                                                      | 27.6 us: 1.03x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 30.7 us: 1.04x slower                                                       |
| genshi_text              | 31.4 ms                                                      | 32.7 ms: 1.04x slower                                                       |
| sympy_expand             | 600 ms                                                       | 624 ms: 1.04x slower                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 96.4 ms: 1.04x slower                                                       |
| pickle                   | 9.89 us                                                      | 10.5 us: 1.06x slower                                                       |
| meteor_contest           | 138 ms                                                       | 148 ms: 1.07x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.49 us: 1.09x slower                                                       |
| genshi_xml               | 63.3 ms                                                      | 69.9 ms: 1.10x slower                                                       |
| spectral_norm            | 139 ms                                                       | 155 ms: 1.11x slower                                                        |
| python_startup           | 11.5 ms                                                      | 12.9 ms: 1.12x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.46 ms: 1.12x slower                                                       |
| hexiom                   | 9.42 ms                                                      | 10.6 ms: 1.12x slower                                                       |
| flaskblogging            | 4.39 ms                                                      | 4.95 ms: 1.13x slower                                                       |
| regex_compile            | 190 ms                                                       | 214 ms: 1.13x slower                                                        |
| unpickle                 | 13.5 us                                                      | 15.4 us: 1.14x slower                                                       |
| deepcopy_memo            | 49.8 us                                                      | 58.2 us: 1.17x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.07 ms: 1.18x slower                                                       |
| scimark_fft              | 361 ms                                                       | 429 ms: 1.19x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 8.90 ms: 1.21x slower                                                       |
| coverage                 | 63.3 ms                                                      | 80.7 ms: 1.28x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.51 ms: 1.32x slower                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 6.97 ms: 1.37x slower                                                       |
| telco                    | 7.23 ms                                                      | 182 ms: 25.17x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.07x faster                                                                |

Benchmark hidden because not significant (4): asyncio_websockets, mako, fannkuch, deepcopy_reduce
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.14x