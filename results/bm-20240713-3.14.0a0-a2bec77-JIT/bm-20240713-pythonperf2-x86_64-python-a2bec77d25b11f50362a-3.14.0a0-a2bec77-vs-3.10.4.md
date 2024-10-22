# Results vs. 3.10.4

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-x86_64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 306 ms: 1.14x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.10 sec: 1.10x faster                                                      |
| html5lib       | 94.6 ms                                                      | 70.8 ms: 1.34x faster                                                       |
| tornado_http   | 157 ms                                                       | 121 ms: 1.29x faster                                                        |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 340 ms: 2.03x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 414 ms: 1.98x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 819 ms: 1.95x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 583 ms: 1.61x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.88x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 82.6 ms: 1.62x faster                                                       |
| float          | 111 ms                                                       | 75.1 ms: 1.48x faster                                                       |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.37x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 138 ms: 1.38x faster                                                        |
| regex_dna      | 261 ms                                                       | 235 ms: 1.11x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 312 us: 1.46x faster                                                        |
| unpickle_pure_python | 312 us                                                       | 217 us: 1.44x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.09 sec: 1.39x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 11.0 ms: 1.32x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 58.0 ms: 1.31x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.3 us: 1.20x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 82.5 ms: 1.12x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 99.8 ms: 1.11x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.27x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.06 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.22 ms: 1.59x faster                                                       |
| django_template | 50.2 ms                                                      | 43.3 ms: 1.16x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 28.7 ms: 1.09x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 64.7 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.19x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 189 us: 2.84x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 380 ms: 2.05x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.66 ms: 2.05x faster                                                       |
| async_tree_none          | 692 ms                                                       | 340 ms: 2.03x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 414 ms: 1.98x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| async_tree_io            | 1.60 sec                                                     | 819 ms: 1.95x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 27.7 us: 1.80x faster                                                       |
| richards_super           | 90.6 ms                                                      | 53.0 ms: 1.71x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 70.3 ms: 1.70x faster                                                       |
| spectral_norm            | 139 ms                                                       | 82.5 ms: 1.69x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 64.2 ms: 1.67x faster                                                       |
| richards                 | 75.1 ms                                                      | 44.9 ms: 1.67x faster                                                       |
| pyflate                  | 733 ms                                                       | 445 ms: 1.65x faster                                                        |
| chaos                    | 109 ms                                                       | 66.0 ms: 1.65x faster                                                       |
| raytrace                 | 489 ms                                                       | 298 ms: 1.64x faster                                                        |
| logging_silent           | 167 ns                                                       | 102 ns: 1.64x faster                                                        |
| nbody                    | 134 ms                                                       | 82.6 ms: 1.62x faster                                                       |
| generators               | 57.3 ms                                                      | 35.3 ms: 1.62x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 583 ms: 1.61x faster                                                        |
| go                       | 262 ms                                                       | 164 ms: 1.60x faster                                                        |
| mako                     | 14.7 ms                                                      | 9.22 ms: 1.59x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.59x faster                                                       |
| deepcopy                 | 468 us                                                       | 305 us: 1.53x faster                                                        |
| pylint                   | 566 ms                                                       | 372 ms: 1.52x faster                                                        |
| float                    | 111 ms                                                       | 75.1 ms: 1.48x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.81 ms: 1.48x faster                                                       |
| scimark_lu               | 167 ms                                                       | 114 ms: 1.47x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 312 us: 1.46x faster                                                        |
| comprehensions           | 26.7 us                                                      | 18.3 us: 1.46x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.0 ms: 1.45x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 217 us: 1.44x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.66 ms: 1.41x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.09 sec: 1.39x faster                                                      |
| fannkuch                 | 483 ms                                                       | 346 ms: 1.39x faster                                                        |
| scimark_sor              | 180 ms                                                       | 131 ms: 1.38x faster                                                        |
| regex_compile            | 190 ms                                                       | 138 ms: 1.38x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.47 us: 1.37x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.70 ms: 1.36x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 70.8 ms: 1.34x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.25 us: 1.33x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.62 sec: 1.33x faster                                                      |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                      |
| json_dumps               | 14.5 ms                                                      | 11.0 ms: 1.32x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 796 ms: 1.32x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.05 us: 1.32x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 58.0 ms: 1.31x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 16.3 ms: 1.31x faster                                                       |
| thrift                   | 1.18 ms                                                      | 908 us: 1.29x faster                                                        |
| tornado_http             | 157 ms                                                       | 121 ms: 1.29x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 65.3 ms: 1.24x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.09 ms: 1.24x faster                                                       |
| scimark_fft              | 361 ms                                                       | 293 ms: 1.23x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 929 us: 1.23x faster                                                        |
| nqueens                  | 115 ms                                                       | 94.8 ms: 1.21x faster                                                       |
| json_loads               | 30.3 us                                                      | 25.3 us: 1.20x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.53 sec: 1.19x faster                                                      |
| dask                     | 472 ms                                                       | 400 ms: 1.18x faster                                                        |
| sympy_sum                | 193 ms                                                       | 164 ms: 1.17x faster                                                        |
| sympy_str                | 360 ms                                                       | 308 ms: 1.17x faster                                                        |
| django_template          | 50.2 ms                                                      | 43.3 ms: 1.16x faster                                                       |
| sympy_expand             | 600 ms                                                       | 521 ms: 1.15x faster                                                        |
| 2to3                     | 350 ms                                                       | 306 ms: 1.14x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 82.5 ms: 1.12x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| regex_dna                | 261 ms                                                       | 235 ms: 1.11x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 63.2 ms: 1.11x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 99.8 ms: 1.11x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 130 ms: 1.10x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 25.5 ms: 1.10x faster                                                       |
| docutils                 | 3.41 sec                                                     | 3.10 sec: 1.10x faster                                                      |
| genshi_text              | 31.4 ms                                                      | 28.7 ms: 1.09x faster                                                       |
| async_generators         | 421 ms                                                       | 386 ms: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                       |
| meteor_contest           | 138 ms                                                       | 131 ms: 1.06x faster                                                        |
| json                     | 5.86 ms                                                      | 5.54 ms: 1.06x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 64.7 ms: 1.02x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.93 ms: 1.09x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.34 ms: 1.15x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.06 ms: 1.24x slower                                                       |
| coverage                 | 63.3 ms                                                      | 80.2 ms: 1.27x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.44 ms: 1.30x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.33x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.20x