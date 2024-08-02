# Results vs. 3.10.4

- fork: python
- ref: c15f94d6fbc960790db3
- machine: linux-x86_64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 291 ms: 1.20x faster                                                         |
| chameleon      | 9.44 ms                                                      | 7.40 ms: 1.28x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.99 sec: 1.14x faster                                                       |
| html5lib       | 94.6 ms                                                      | 75.3 ms: 1.26x faster                                                        |
| tornado_http   | 157 ms                                                       | 119 ms: 1.32x faster                                                         |
| Geometric mean | (ref)                                                        | 1.24x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 371 ms: 1.86x faster                                                         |
| async_tree_io           | 1.60 sec                                                     | 884 ms: 1.81x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 465 ms: 1.76x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 614 ms: 1.52x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.74x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 89.4 ms: 1.50x faster                                                        |
| float          | 111 ms                                                       | 80.8 ms: 1.38x faster                                                        |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 145 ms: 1.31x faster                                                         |
| regex_dna      | 261 ms                                                       | 248 ms: 1.05x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 26.4 ms: 1.03x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.72 ms: 1.20x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 309 us: 1.47x faster                                                         |
| unpickle_pure_python | 312 us                                                       | 226 us: 1.38x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 11.1 ms: 1.32x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 59.3 ms: 1.28x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.8 us: 1.23x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.39 sec: 1.22x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 102 ms: 1.08x faster                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 85.2 ms: 1.08x faster                                                        |
| unpickle_list        | 4.65 us                                                      | 4.80 us: 1.03x slower                                                        |
| pickle               | 9.89 us                                                      | 10.6 us: 1.07x slower                                                        |
| pickle_list          | 4.12 us                                                      | 4.46 us: 1.08x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 33.3 us: 1.13x slower                                                        |
| unpickle             | 13.5 us                                                      | 15.7 us: 1.17x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.11x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.2 ms: 1.15x slower                                                        |
| python_startup_no_site | 7.33 ms                                                      | 8.84 ms: 1.21x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.18x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                                        |
| django_template | 50.2 ms                                                      | 39.1 ms: 1.28x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 25.0 ms: 1.26x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 55.5 ms: 1.14x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 173 us: 3.10x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.36 ms: 2.23x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 378 ms: 2.06x faster                                                         |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                       |
| async_tree_none          | 692 ms                                                       | 371 ms: 1.86x faster                                                         |
| raytrace                 | 489 ms                                                       | 268 ms: 1.83x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 884 ms: 1.81x faster                                                         |
| chaos                    | 109 ms                                                       | 60.5 ms: 1.80x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 465 ms: 1.76x faster                                                         |
| logging_silent           | 167 ns                                                       | 96.3 ns: 1.74x faster                                                        |
| generators               | 57.3 ms                                                      | 33.4 ms: 1.72x faster                                                        |
| scimark_lu               | 167 ms                                                       | 97.9 ms: 1.70x faster                                                        |
| pylint                   | 566 ms                                                       | 340 ms: 1.67x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 65.5 ms: 1.64x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 73.9 ms: 1.61x faster                                                        |
| go                       | 262 ms                                                       | 163 ms: 1.60x faster                                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.40 ms: 1.59x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.1 us: 1.56x faster                                                        |
| scimark_sor              | 180 ms                                                       | 117 ms: 1.54x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 614 ms: 1.52x faster                                                         |
| pyflate                  | 733 ms                                                       | 484 ms: 1.51x faster                                                         |
| sqlglot_transpile        | 2.68 ms                                                      | 1.78 ms: 1.51x faster                                                        |
| richards_super           | 90.6 ms                                                      | 60.3 ms: 1.50x faster                                                        |
| nbody                    | 134 ms                                                       | 89.4 ms: 1.50x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.37 ms: 1.48x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 309 us: 1.47x faster                                                         |
| spectral_norm            | 139 ms                                                       | 97.2 ms: 1.43x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                                        |
| richards                 | 75.1 ms                                                      | 53.5 ms: 1.40x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.40 us: 1.39x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 226 us: 1.38x faster                                                         |
| float                    | 111 ms                                                       | 80.8 ms: 1.38x faster                                                        |
| coroutines               | 30.3 ms                                                      | 22.0 ms: 1.38x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.02 us: 1.37x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.71 ms: 1.35x faster                                                        |
| fannkuch                 | 483 ms                                                       | 358 ms: 1.35x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 11.1 ms: 1.32x faster                                                        |
| tornado_http             | 157 ms                                                       | 119 ms: 1.32x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 37.8 us: 1.32x faster                                                        |
| thrift                   | 1.18 ms                                                      | 894 us: 1.31x faster                                                         |
| regex_compile            | 190 ms                                                       | 145 ms: 1.31x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.66 sec: 1.30x faster                                                       |
| nqueens                  | 115 ms                                                       | 88.8 ms: 1.29x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 814 ms: 1.29x faster                                                         |
| django_template          | 50.2 ms                                                      | 39.1 ms: 1.28x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 59.3 ms: 1.28x faster                                                        |
| chameleon                | 9.44 ms                                                      | 7.40 ms: 1.28x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 25.0 ms: 1.26x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 75.3 ms: 1.26x faster                                                        |
| sympy_sum                | 193 ms                                                       | 155 ms: 1.25x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 918 us: 1.24x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 17.3 ms: 1.24x faster                                                        |
| deepcopy                 | 468 us                                                       | 381 us: 1.23x faster                                                         |
| json_loads               | 30.3 us                                                      | 24.8 us: 1.23x faster                                                        |
| mypy2                    | 933 ms                                                       | 764 ms: 1.22x faster                                                         |
| sympy_str                | 360 ms                                                       | 295 ms: 1.22x faster                                                         |
| tomli_loads              | 2.92 sec                                                     | 2.39 sec: 1.22x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.18 ms: 1.21x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 67.2 ms: 1.21x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.21x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 23.4 ms: 1.20x faster                                                        |
| 2to3                     | 350 ms                                                       | 291 ms: 1.20x faster                                                         |
| sympy_expand             | 600 ms                                                       | 501 ms: 1.20x faster                                                         |
| dask                     | 472 ms                                                       | 396 ms: 1.19x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 3.37 us: 1.19x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 59.0 ms: 1.19x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.53 sec: 1.19x faster                                                       |
| scimark_fft              | 361 ms                                                       | 308 ms: 1.17x faster                                                         |
| docutils                 | 3.41 sec                                                     | 2.99 sec: 1.14x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 55.5 ms: 1.14x faster                                                        |
| async_generators         | 421 ms                                                       | 370 ms: 1.14x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                         |
| gunicorn                 | 1.16 ms                                                      | 1.04 ms: 1.11x faster                                                        |
| json                     | 5.86 ms                                                      | 5.28 ms: 1.11x faster                                                        |
| aiohttp                  | 1.19 ms                                                      | 1.07 ms: 1.11x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 102 ms: 1.08x faster                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 85.2 ms: 1.08x faster                                                        |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                                         |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.80 us: 1.07x faster                                                        |
| regex_dna                | 261 ms                                                       | 248 ms: 1.05x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 26.4 ms: 1.03x faster                                                        |
| unpickle_list            | 4.65 us                                                      | 4.80 us: 1.03x slower                                                        |
| flaskblogging            | 4.39 ms                                                      | 4.66 ms: 1.06x slower                                                        |
| pickle                   | 9.89 us                                                      | 10.6 us: 1.07x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.46 us: 1.08x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 33.3 us: 1.13x slower                                                        |
| python_startup           | 11.5 ms                                                      | 13.2 ms: 1.15x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.04 ms: 1.16x slower                                                        |
| telco                    | 7.23 ms                                                      | 8.41 ms: 1.16x slower                                                        |
| unpickle                 | 13.5 us                                                      | 15.7 us: 1.17x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.72 ms: 1.20x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 8.84 ms: 1.21x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 4.38 ms: 1.28x slower                                                        |
| coverage                 | 63.3 ms                                                      | 84.1 ms: 1.33x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.12x