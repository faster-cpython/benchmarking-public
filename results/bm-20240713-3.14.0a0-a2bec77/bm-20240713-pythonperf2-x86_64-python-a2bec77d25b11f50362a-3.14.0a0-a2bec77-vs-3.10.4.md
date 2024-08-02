# Results vs. 3.10.4

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-x86_64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 289 ms: 1.21x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.96 sec: 1.15x faster                                                      |
| html5lib       | 94.6 ms                                                      | 74.0 ms: 1.28x faster                                                       |
| tornado_http   | 157 ms                                                       | 117 ms: 1.34x faster                                                        |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 335 ms: 2.07x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 403 ms: 2.04x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 811 ms: 1.97x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 579 ms: 1.62x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.91x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 88.3 ms: 1.52x faster                                                       |
| float          | 111 ms                                                       | 80.6 ms: 1.38x faster                                                       |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 140 ms: 1.36x faster                                                        |
| regex_dna      | 261 ms                                                       | 240 ms: 1.09x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.2 ms: 1.04x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.52 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 216 us: 1.44x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 325 us: 1.40x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.9 ms: 1.34x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.25 sec: 1.30x faster                                                      |
| xml_etree_process    | 75.9 ms                                                      | 59.2 ms: 1.28x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.4 us: 1.19x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 146 ms: 1.10x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 84.6 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.06x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.24x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.01 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                                       |
| django_template | 50.2 ms                                                      | 38.3 ms: 1.31x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 25.0 ms: 1.26x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 54.6 ms: 1.16x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.28x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 171 us: 3.14x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.50 ms: 2.14x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 374 ms: 2.08x faster                                                        |
| async_tree_none          | 692 ms                                                       | 335 ms: 2.07x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 403 ms: 2.04x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 811 ms: 1.97x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                      |
| raytrace                 | 489 ms                                                       | 269 ms: 1.82x faster                                                        |
| chaos                    | 109 ms                                                       | 61.4 ms: 1.77x faster                                                       |
| generators               | 57.3 ms                                                      | 33.5 ms: 1.71x faster                                                       |
| scimark_lu               | 167 ms                                                       | 98.4 ms: 1.70x faster                                                       |
| logging_silent           | 167 ns                                                       | 98.8 ns: 1.69x faster                                                       |
| pylint                   | 566 ms                                                       | 335 ms: 1.69x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 29.8 us: 1.67x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 71.7 ms: 1.66x faster                                                       |
| deepcopy                 | 468 us                                                       | 284 us: 1.65x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 579 ms: 1.62x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 67.5 ms: 1.59x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.59x faster                                                       |
| go                       | 262 ms                                                       | 166 ms: 1.58x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.1 us: 1.56x faster                                                       |
| richards_super           | 90.6 ms                                                      | 58.5 ms: 1.55x faster                                                       |
| nbody                    | 134 ms                                                       | 88.3 ms: 1.52x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.78 ms: 1.51x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.27 ms: 1.50x faster                                                       |
| pyflate                  | 733 ms                                                       | 490 ms: 1.49x faster                                                        |
| richards                 | 75.1 ms                                                      | 51.5 ms: 1.46x faster                                                       |
| spectral_norm            | 139 ms                                                       | 95.8 ms: 1.45x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 216 us: 1.44x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.2 ms: 1.43x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 325 us: 1.40x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.39 us: 1.39x faster                                                       |
| float                    | 111 ms                                                       | 80.6 ms: 1.38x faster                                                       |
| scimark_sor              | 180 ms                                                       | 131 ms: 1.38x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.93 us: 1.37x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.05 us: 1.37x faster                                                       |
| regex_compile            | 190 ms                                                       | 140 ms: 1.36x faster                                                        |
| tornado_http             | 157 ms                                                       | 117 ms: 1.34x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.9 ms: 1.34x faster                                                       |
| thrift                   | 1.18 ms                                                      | 882 us: 1.33x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 4.80 ms: 1.33x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.32x faster                                                      |
| pathlib                  | 21.4 ms                                                      | 16.2 ms: 1.32x faster                                                       |
| django_template          | 50.2 ms                                                      | 38.3 ms: 1.31x faster                                                       |
| nqueens                  | 115 ms                                                       | 87.7 ms: 1.31x faster                                                       |
| fannkuch                 | 483 ms                                                       | 368 ms: 1.31x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 873 us: 1.31x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.25 sec: 1.30x faster                                                      |
| pprint_pformat           | 2.15 sec                                                     | 1.66 sec: 1.30x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 812 ms: 1.29x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 59.2 ms: 1.28x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 74.0 ms: 1.28x faster                                                       |
| sympy_sum                | 193 ms                                                       | 153 ms: 1.26x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 25.0 ms: 1.26x faster                                                       |
| sympy_str                | 360 ms                                                       | 292 ms: 1.23x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 66.2 ms: 1.22x faster                                                       |
| dask                     | 472 ms                                                       | 386 ms: 1.22x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.0 ms: 1.22x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.21x faster                                                        |
| 2to3                     | 350 ms                                                       | 289 ms: 1.21x faster                                                        |
| sympy_expand             | 600 ms                                                       | 496 ms: 1.21x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.49 sec: 1.21x faster                                                      |
| json_loads               | 30.3 us                                                      | 25.4 us: 1.19x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 58.9 ms: 1.19x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 54.6 ms: 1.16x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.38 ms: 1.16x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.96 sec: 1.15x faster                                                      |
| async_generators         | 421 ms                                                       | 367 ms: 1.15x faster                                                        |
| scimark_fft              | 361 ms                                                       | 315 ms: 1.15x faster                                                        |
| meteor_contest           | 138 ms                                                       | 126 ms: 1.10x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 146 ms: 1.10x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 84.6 ms: 1.09x faster                                                       |
| regex_dna                | 261 ms                                                       | 240 ms: 1.09x faster                                                        |
| json                     | 5.86 ms                                                      | 5.47 ms: 1.07x faster                                                       |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 104 ms: 1.06x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 26.2 ms: 1.04x faster                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.99 ms: 1.13x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.52 ms: 1.14x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.25 ms: 1.14x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.01 ms: 1.23x slower                                                       |
| coverage                 | 63.3 ms                                                      | 78.4 ms: 1.24x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.46 ms: 1.31x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.34x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.12x