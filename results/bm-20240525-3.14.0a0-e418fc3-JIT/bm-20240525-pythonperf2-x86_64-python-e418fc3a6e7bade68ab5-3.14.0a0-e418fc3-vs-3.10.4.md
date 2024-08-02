# Results vs. 3.10.4

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-x86_64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 305 ms: 1.15x faster                                                        |
| chameleon      | 9.44 ms                                                      | 7.68 ms: 1.23x faster                                                       |
| docutils       | 3.41 sec                                                     | 3.13 sec: 1.09x faster                                                      |
| html5lib       | 94.6 ms                                                      | 74.3 ms: 1.27x faster                                                       |
| tornado_http   | 157 ms                                                       | 124 ms: 1.26x faster                                                        |
| Geometric mean | (ref)                                                        | 1.20x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 376 ms: 1.84x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 903 ms: 1.77x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 470 ms: 1.74x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 624 ms: 1.50x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.71x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 81.6 ms: 1.64x faster                                                       |
| float          | 111 ms                                                       | 74.2 ms: 1.50x faster                                                       |
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.39x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 138 ms: 1.38x faster                                                        |
| regex_dna      | 261 ms                                                       | 243 ms: 1.08x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.0 ms: 1.05x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.67 ms: 1.19x slower                                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 318 us: 1.43x faster                                                        |
| unpickle_pure_python | 312 us                                                       | 222 us: 1.41x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.12 sec: 1.37x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 58.0 ms: 1.31x faster                                                       |
| json_loads           | 30.3 us                                                      | 24.5 us: 1.24x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 81.8 ms: 1.13x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.10x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 149 ms: 1.07x faster                                                        |
| unpickle_list        | 4.65 us                                                      | 4.79 us: 1.03x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.45 us: 1.08x slower                                                       |
| pickle               | 9.89 us                                                      | 10.7 us: 1.08x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 32.0 us: 1.09x slower                                                       |
| unpickle             | 13.5 us                                                      | 15.4 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.8 ms: 1.20x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.48 ms: 1.29x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.25x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.14 ms: 1.61x faster                                                       |
| django_template | 50.2 ms                                                      | 41.4 ms: 1.21x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 29.1 ms: 1.08x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 64.8 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.20x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 185 us: 2.90x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 377 ms: 2.07x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.73 ms: 2.01x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| async_tree_none          | 692 ms                                                       | 376 ms: 1.84x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 903 ms: 1.77x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 470 ms: 1.74x faster                                                        |
| raytrace                 | 489 ms                                                       | 284 ms: 1.72x faster                                                        |
| richards_super           | 90.6 ms                                                      | 52.7 ms: 1.72x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 70.2 ms: 1.70x faster                                                       |
| chaos                    | 109 ms                                                       | 64.4 ms: 1.69x faster                                                       |
| generators               | 57.3 ms                                                      | 34.4 ms: 1.67x faster                                                       |
| spectral_norm            | 139 ms                                                       | 84.3 ms: 1.65x faster                                                       |
| nbody                    | 134 ms                                                       | 81.6 ms: 1.64x faster                                                       |
| richards                 | 75.1 ms                                                      | 46.1 ms: 1.63x faster                                                       |
| go                       | 262 ms                                                       | 161 ms: 1.63x faster                                                        |
| mako                     | 14.7 ms                                                      | 9.14 ms: 1.61x faster                                                       |
| pyflate                  | 733 ms                                                       | 463 ms: 1.58x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 68.0 ms: 1.58x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.57x faster                                                       |
| logging_silent           | 167 ns                                                       | 107 ns: 1.57x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 624 ms: 1.50x faster                                                        |
| float                    | 111 ms                                                       | 74.2 ms: 1.50x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.9 us: 1.49x faster                                                       |
| pylint                   | 566 ms                                                       | 380 ms: 1.49x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.82 ms: 1.47x faster                                                       |
| fannkuch                 | 483 ms                                                       | 336 ms: 1.44x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 318 us: 1.43x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.5 ms: 1.41x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 222 us: 1.41x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.70 ms: 1.40x faster                                                       |
| scimark_lu               | 167 ms                                                       | 119 ms: 1.40x faster                                                        |
| scimark_sor              | 180 ms                                                       | 130 ms: 1.38x faster                                                        |
| regex_compile            | 190 ms                                                       | 138 ms: 1.38x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.45 us: 1.38x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.01 us: 1.38x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.12 sec: 1.37x faster                                                      |
| json_dumps               | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.72 ms: 1.35x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 16.2 ms: 1.32x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 37.8 us: 1.32x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 58.0 ms: 1.31x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 802 ms: 1.31x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.28 sec: 1.31x faster                                                      |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 3.91 ms: 1.30x faster                                                       |
| thrift                   | 1.18 ms                                                      | 904 us: 1.30x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.66 sec: 1.30x faster                                                      |
| html5lib                 | 94.6 ms                                                      | 74.3 ms: 1.27x faster                                                       |
| tornado_http             | 157 ms                                                       | 124 ms: 1.26x faster                                                        |
| scimark_fft              | 361 ms                                                       | 288 ms: 1.26x faster                                                        |
| json_loads               | 30.3 us                                                      | 24.5 us: 1.24x faster                                                       |
| chameleon                | 9.44 ms                                                      | 7.68 ms: 1.23x faster                                                       |
| django_template          | 50.2 ms                                                      | 41.4 ms: 1.21x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 67.0 ms: 1.21x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 961 us: 1.19x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.57 sec: 1.17x faster                                                      |
| nqueens                  | 115 ms                                                       | 98.4 ms: 1.17x faster                                                       |
| sympy_sum                | 193 ms                                                       | 166 ms: 1.16x faster                                                        |
| dask                     | 472 ms                                                       | 406 ms: 1.16x faster                                                        |
| 2to3                     | 350 ms                                                       | 305 ms: 1.15x faster                                                        |
| sympy_str                | 360 ms                                                       | 314 ms: 1.15x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 81.8 ms: 1.13x faster                                                       |
| sympy_expand             | 600 ms                                                       | 533 ms: 1.13x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 128 ms: 1.12x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 63.1 ms: 1.11x faster                                                       |
| async_generators         | 421 ms                                                       | 380 ms: 1.11x faster                                                        |
| json                     | 5.86 ms                                                      | 5.30 ms: 1.11x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 101 ms: 1.10x faster                                                        |
| deepcopy                 | 468 us                                                       | 427 us: 1.10x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.13 sec: 1.09x faster                                                      |
| sympy_integrate          | 28.2 ms                                                      | 25.8 ms: 1.09x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.76 us: 1.08x faster                                                       |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 29.1 ms: 1.08x faster                                                       |
| regex_dna                | 261 ms                                                       | 243 ms: 1.08x faster                                                        |
| meteor_contest           | 138 ms                                                       | 129 ms: 1.08x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 149 ms: 1.07x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.74 us: 1.07x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 26.0 ms: 1.05x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 64.8 ms: 1.02x slower                                                       |
| unpickle_list            | 4.65 us                                                      | 4.79 us: 1.03x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.45 us: 1.08x slower                                                       |
| pickle                   | 9.89 us                                                      | 10.7 us: 1.08x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 32.0 us: 1.09x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.98 ms: 1.13x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.17 ms: 1.13x slower                                                       |
| flaskblogging            | 4.39 ms                                                      | 4.96 ms: 1.13x slower                                                       |
| unpickle                 | 13.5 us                                                      | 15.4 us: 1.14x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.67 ms: 1.19x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.8 ms: 1.20x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.48 ms: 1.29x slower                                                       |
| coverage                 | 63.3 ms                                                      | 85.2 ms: 1.35x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.89 ms: 1.43x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.27x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.22x