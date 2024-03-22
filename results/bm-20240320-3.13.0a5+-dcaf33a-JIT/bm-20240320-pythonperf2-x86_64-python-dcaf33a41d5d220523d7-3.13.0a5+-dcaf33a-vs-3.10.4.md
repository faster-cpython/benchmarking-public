# Results vs. 3.10.4

- fork: python
- ref: dcaf33a41d5d220523d7
- machine: linux-x86_64
- commit hash: dcaf33a
- commit date: 2024-03-20
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 332 ms: 1.05x faster                                                         |
| chameleon      | 9.44 ms                                                      | 7.21 ms: 1.31x faster                                                        |
| docutils       | 3.41 sec                                                     | 4.70 sec: 1.38x slower                                                       |
| html5lib       | 94.6 ms                                                      | 82.5 ms: 1.15x faster                                                        |
| tornado_http   | 157 ms                                                       | 128 ms: 1.23x faster                                                         |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 936 ms                                                       | 3.32 sec: 3.54x slower                                                       |
| async_tree_none         | 692 ms                                                       | 2.74 sec: 3.97x slower                                                       |
| async_tree_memoization  | 819 ms                                                       | 3.44 sec: 4.20x slower                                                       |
| async_tree_io           | 1.60 sec                                                     | 9.75 sec: 6.10x slower                                                       |
| Geometric mean          | (ref)                                                        | 4.36x slower                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 94.7 ms: 1.42x faster                                                        |
| pidigits       | 271 ms                                                       | 261 ms: 1.04x faster                                                         |
| float          | 111 ms                                                       | 154 ms: 1.38x slower                                                         |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 146 ms: 1.30x faster                                                         |
| regex_dna      | 261 ms                                                       | 241 ms: 1.08x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.57 ms: 1.16x slower                                                        |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 319 us: 1.43x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 10.5 ms: 1.38x faster                                                        |
| unpickle_pure_python | 312 us                                                       | 229 us: 1.36x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.15 sec: 1.36x faster                                                       |
| json_loads           | 30.3 us                                                      | 24.8 us: 1.22x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 68.1 ms: 1.11x faster                                                        |
| pickle               | 9.89 us                                                      | 10.5 us: 1.07x slower                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 98.9 ms: 1.07x slower                                                        |
| pickle_list          | 4.12 us                                                      | 4.44 us: 1.08x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 33.0 us: 1.12x slower                                                        |
| unpickle             | 13.5 us                                                      | 15.4 us: 1.14x slower                                                        |
| xml_etree_parse      | 160 ms                                                       | 209 ms: 1.30x slower                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 168 ms: 1.52x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 14.5 ms: 1.26x slower                                                        |
| python_startup_no_site | 7.33 ms                                                      | 12.6 ms: 1.72x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.47x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.98 ms: 1.47x faster                                                        |
| django_template | 50.2 ms                                                      | 38.1 ms: 1.32x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 29.5 ms: 1.07x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 66.9 ms: 1.06x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.18x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 115 us: 4.67x faster                                                         |
| asyncio_tcp              | 779 ms                                                       | 371 ms: 2.10x faster                                                         |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                       |
| deltablue                | 7.50 ms                                                      | 4.02 ms: 1.87x faster                                                        |
| generators               | 57.3 ms                                                      | 33.3 ms: 1.72x faster                                                        |
| logging_silent           | 167 ns                                                       | 97.7 ns: 1.71x faster                                                        |
| chaos                    | 109 ms                                                       | 66.7 ms: 1.63x faster                                                        |
| richards_super           | 90.6 ms                                                      | 57.3 ms: 1.58x faster                                                        |
| raytrace                 | 489 ms                                                       | 310 ms: 1.58x faster                                                         |
| crypto_pyaes             | 119 ms                                                       | 77.8 ms: 1.53x faster                                                        |
| go                       | 262 ms                                                       | 175 ms: 1.50x faster                                                         |
| spectral_norm            | 139 ms                                                       | 93.8 ms: 1.48x faster                                                        |
| mako                     | 14.7 ms                                                      | 9.98 ms: 1.47x faster                                                        |
| richards                 | 75.1 ms                                                      | 51.5 ms: 1.46x faster                                                        |
| scimark_lu               | 167 ms                                                       | 115 ms: 1.45x faster                                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.55 ms: 1.44x faster                                                        |
| pyflate                  | 733 ms                                                       | 513 ms: 1.43x faster                                                         |
| pickle_pure_python       | 455 us                                                       | 319 us: 1.43x faster                                                         |
| nbody                    | 134 ms                                                       | 94.7 ms: 1.42x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 76.6 ms: 1.40x faster                                                        |
| comprehensions           | 26.7 us                                                      | 19.1 us: 1.40x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.5 ms: 1.38x faster                                                        |
| thrift                   | 1.18 ms                                                      | 859 us: 1.37x faster                                                         |
| unpickle_pure_python     | 312 us                                                       | 229 us: 1.36x faster                                                         |
| logging_simple           | 8.88 us                                                      | 6.52 us: 1.36x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.15 sec: 1.36x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 36.9 us: 1.35x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.16 us: 1.35x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 4.76 ms: 1.34x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 2.02 ms: 1.33x faster                                                        |
| coroutines               | 30.3 ms                                                      | 22.8 ms: 1.33x faster                                                        |
| django_template          | 50.2 ms                                                      | 38.1 ms: 1.32x faster                                                        |
| chameleon                | 9.44 ms                                                      | 7.21 ms: 1.31x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 7.21 ms: 1.31x faster                                                        |
| regex_compile            | 190 ms                                                       | 146 ms: 1.30x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.70 sec: 1.27x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 830 ms: 1.26x faster                                                         |
| deepcopy                 | 468 us                                                       | 379 us: 1.23x faster                                                         |
| tornado_http             | 157 ms                                                       | 128 ms: 1.23x faster                                                         |
| json_loads               | 30.3 us                                                      | 24.8 us: 1.22x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 935 us: 1.22x faster                                                         |
| fannkuch                 | 483 ms                                                       | 396 ms: 1.22x faster                                                         |
| sympy_sum                | 193 ms                                                       | 159 ms: 1.21x faster                                                         |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.21x faster                                                         |
| sympy_str                | 360 ms                                                       | 300 ms: 1.20x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 3.38 us: 1.18x faster                                                        |
| scimark_sor              | 180 ms                                                       | 153 ms: 1.18x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 68.9 ms: 1.18x faster                                                        |
| sympy_expand             | 600 ms                                                       | 511 ms: 1.18x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.37 ms: 1.16x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 24.3 ms: 1.16x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 82.5 ms: 1.15x faster                                                        |
| nqueens                  | 115 ms                                                       | 100 ms: 1.14x faster                                                         |
| scimark_fft              | 361 ms                                                       | 322 ms: 1.12x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.68 sec: 1.12x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 68.1 ms: 1.11x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 19.2 ms: 1.11x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.71 us: 1.10x faster                                                        |
| json                     | 5.86 ms                                                      | 5.36 ms: 1.09x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 64.5 ms: 1.09x faster                                                        |
| regex_dna                | 261 ms                                                       | 241 ms: 1.08x faster                                                         |
| mypy2                    | 933 ms                                                       | 863 ms: 1.08x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 29.5 ms: 1.07x faster                                                        |
| 2to3                     | 350 ms                                                       | 332 ms: 1.05x faster                                                         |
| meteor_contest           | 138 ms                                                       | 131 ms: 1.05x faster                                                         |
| create_gc_cycles         | 1.76 ms                                                      | 1.68 ms: 1.05x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.60 sec: 1.04x faster                                                       |
| pidigits                 | 271 ms                                                       | 261 ms: 1.04x faster                                                         |
| gunicorn                 | 1.16 ms                                                      | 1.12 ms: 1.04x faster                                                        |
| aiohttp                  | 1.19 ms                                                      | 1.15 ms: 1.03x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 387 ms: 1.01x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 66.9 ms: 1.06x slower                                                        |
| pickle                   | 9.89 us                                                      | 10.5 us: 1.07x slower                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 98.9 ms: 1.07x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.44 us: 1.08x slower                                                        |
| telco                    | 7.23 ms                                                      | 8.07 ms: 1.12x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 33.0 us: 1.12x slower                                                        |
| async_generators         | 421 ms                                                       | 474 ms: 1.13x slower                                                         |
| unpickle                 | 13.5 us                                                      | 15.4 us: 1.14x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.57 ms: 1.16x slower                                                        |
| unpack_sequence          | 59.9 ns                                                      | 74.0 ns: 1.24x slower                                                        |
| python_startup           | 11.5 ms                                                      | 14.5 ms: 1.26x slower                                                        |
| coverage                 | 63.3 ms                                                      | 81.0 ms: 1.28x slower                                                        |
| xml_etree_parse          | 160 ms                                                       | 209 ms: 1.30x slower                                                         |
| gc_traversal             | 3.42 ms                                                      | 4.47 ms: 1.31x slower                                                        |
| docutils                 | 3.41 sec                                                     | 4.70 sec: 1.38x slower                                                       |
| float                    | 111 ms                                                       | 154 ms: 1.38x slower                                                         |
| pylint                   | 566 ms                                                       | 839 ms: 1.48x slower                                                         |
| dask                     | 472 ms                                                       | 711 ms: 1.51x slower                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 168 ms: 1.52x slower                                                         |
| python_startup_no_site   | 7.33 ms                                                      | 12.6 ms: 1.72x slower                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 3.32 sec: 3.54x slower                                                       |
| async_tree_none          | 692 ms                                                       | 2.74 sec: 3.97x slower                                                       |
| async_tree_memoization   | 819 ms                                                       | 3.44 sec: 4.20x slower                                                       |
| async_tree_io            | 1.60 sec                                                     | 9.75 sec: 6.10x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.09x faster                                                                 |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240320-3.13.0a5+-dcaf33a-JIT/bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x


# Memory

- memory change: 1.23x