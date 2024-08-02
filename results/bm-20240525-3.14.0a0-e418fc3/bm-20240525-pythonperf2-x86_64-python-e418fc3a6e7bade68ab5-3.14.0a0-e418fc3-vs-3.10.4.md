# Results vs. 3.10.4

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-x86_64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 288 ms: 1.22x faster                                                        |
| chameleon      | 9.44 ms                                                      | 7.50 ms: 1.26x faster                                                       |
| docutils       | 3.41 sec                                                     | 2.97 sec: 1.15x faster                                                      |
| html5lib       | 94.6 ms                                                      | 73.3 ms: 1.29x faster                                                       |
| tornado_http   | 157 ms                                                       | 119 ms: 1.32x faster                                                        |
| Geometric mean | (ref)                                                        | 1.24x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 380 ms: 1.82x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 907 ms: 1.76x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 483 ms: 1.70x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 627 ms: 1.49x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.69x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 88.7 ms: 1.51x faster                                                       |
| float          | 111 ms                                                       | 79.9 ms: 1.39x faster                                                       |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 144 ms: 1.32x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 25.1 ms: 1.08x faster                                                       |
| regex_dna      | 261 ms                                                       | 245 ms: 1.07x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.46 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 213 us: 1.46x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 316 us: 1.44x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.8 ms: 1.35x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 60.8 ms: 1.25x faster                                                       |
| json_loads           | 30.3 us                                                      | 24.5 us: 1.24x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.48 sec: 1.17x faster                                                      |
| xml_etree_parse      | 160 ms                                                       | 146 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.07x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 86.4 ms: 1.07x faster                                                       |
| unpickle_list        | 4.65 us                                                      | 4.73 us: 1.02x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.39 us: 1.06x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 31.5 us: 1.07x slower                                                       |
| pickle               | 9.89 us                                                      | 10.7 us: 1.08x slower                                                       |
| unpickle             | 13.5 us                                                      | 15.5 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.11x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.1 ms: 1.14x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 8.83 ms: 1.20x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.17x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                       |
| django_template | 50.2 ms                                                      | 40.1 ms: 1.25x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 26.7 ms: 1.18x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 58.6 ms: 1.08x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.23x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 173 us: 3.10x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.38 ms: 2.22x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 373 ms: 2.09x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                      |
| raytrace                 | 489 ms                                                       | 268 ms: 1.83x faster                                                        |
| async_tree_none          | 692 ms                                                       | 380 ms: 1.82x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 907 ms: 1.76x faster                                                        |
| chaos                    | 109 ms                                                       | 61.9 ms: 1.75x faster                                                       |
| scimark_lu               | 167 ms                                                       | 97.3 ms: 1.71x faster                                                       |
| logging_silent           | 167 ns                                                       | 98.3 ns: 1.70x faster                                                       |
| async_tree_memoization   | 819 ms                                                       | 483 ms: 1.70x faster                                                        |
| generators               | 57.3 ms                                                      | 33.9 ms: 1.69x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 63.6 ms: 1.69x faster                                                       |
| go                       | 262 ms                                                       | 156 ms: 1.68x faster                                                        |
| pylint                   | 566 ms                                                       | 345 ms: 1.64x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 72.9 ms: 1.63x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.40 ms: 1.59x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.0 us: 1.57x faster                                                       |
| richards_super           | 90.6 ms                                                      | 58.9 ms: 1.54x faster                                                       |
| pyflate                  | 733 ms                                                       | 478 ms: 1.53x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.77 ms: 1.52x faster                                                       |
| nbody                    | 134 ms                                                       | 88.7 ms: 1.51x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 627 ms: 1.49x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.38 ms: 1.48x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 213 us: 1.46x faster                                                        |
| scimark_sor              | 180 ms                                                       | 124 ms: 1.46x faster                                                        |
| richards                 | 75.1 ms                                                      | 51.9 ms: 1.45x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 316 us: 1.44x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                       |
| spectral_norm            | 139 ms                                                       | 97.9 ms: 1.42x faster                                                       |
| float                    | 111 ms                                                       | 79.9 ms: 1.39x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.9 ms: 1.38x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.52 us: 1.36x faster                                                       |
| fannkuch                 | 483 ms                                                       | 357 ms: 1.35x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.15 us: 1.35x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 10.8 ms: 1.35x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.76 ms: 1.34x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                      |
| pathlib                  | 21.4 ms                                                      | 16.1 ms: 1.32x faster                                                       |
| thrift                   | 1.18 ms                                                      | 889 us: 1.32x faster                                                        |
| regex_compile            | 190 ms                                                       | 144 ms: 1.32x faster                                                        |
| tornado_http             | 157 ms                                                       | 119 ms: 1.32x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 73.3 ms: 1.29x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.68 sec: 1.28x faster                                                      |
| deepcopy_memo            | 49.8 us                                                      | 39.1 us: 1.27x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 826 ms: 1.27x faster                                                        |
| chameleon                | 9.44 ms                                                      | 7.50 ms: 1.26x faster                                                       |
| django_template          | 50.2 ms                                                      | 40.1 ms: 1.25x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 60.8 ms: 1.25x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 915 us: 1.25x faster                                                        |
| sympy_sum                | 193 ms                                                       | 155 ms: 1.24x faster                                                        |
| json_loads               | 30.3 us                                                      | 24.5 us: 1.24x faster                                                       |
| nqueens                  | 115 ms                                                       | 93.4 ms: 1.23x faster                                                       |
| sympy_str                | 360 ms                                                       | 296 ms: 1.22x faster                                                        |
| 2to3                     | 350 ms                                                       | 288 ms: 1.22x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.49 sec: 1.21x faster                                                      |
| deepcopy                 | 468 us                                                       | 388 us: 1.21x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.4 ms: 1.21x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 67.8 ms: 1.20x faster                                                       |
| dask                     | 472 ms                                                       | 397 ms: 1.19x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.27 ms: 1.19x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 121 ms: 1.19x faster                                                        |
| sympy_expand             | 600 ms                                                       | 507 ms: 1.18x faster                                                        |
| scimark_fft              | 361 ms                                                       | 306 ms: 1.18x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 59.5 ms: 1.18x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 26.7 ms: 1.18x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.48 sec: 1.17x faster                                                      |
| docutils                 | 3.41 sec                                                     | 2.97 sec: 1.15x faster                                                      |
| async_generators         | 421 ms                                                       | 367 ms: 1.15x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.50 us: 1.15x faster                                                       |
| json                     | 5.86 ms                                                      | 5.20 ms: 1.13x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 146 ms: 1.10x faster                                                        |
| meteor_contest           | 138 ms                                                       | 126 ms: 1.10x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 58.6 ms: 1.08x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 25.1 ms: 1.08x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 103 ms: 1.07x faster                                                        |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 86.4 ms: 1.07x faster                                                       |
| regex_dna                | 261 ms                                                       | 245 ms: 1.07x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.81 us: 1.06x faster                                                       |
| unpickle_list            | 4.65 us                                                      | 4.73 us: 1.02x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.39 us: 1.06x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 31.5 us: 1.07x slower                                                       |
| flaskblogging            | 4.39 ms                                                      | 4.73 ms: 1.08x slower                                                       |
| pickle                   | 9.89 us                                                      | 10.7 us: 1.08x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.46 ms: 1.12x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.1 ms: 1.14x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.01 ms: 1.14x slower                                                       |
| unpickle                 | 13.5 us                                                      | 15.5 us: 1.15x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.33 ms: 1.15x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.83 ms: 1.20x slower                                                       |
| coverage                 | 63.3 ms                                                      | 81.2 ms: 1.28x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.71 ms: 1.38x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.12x