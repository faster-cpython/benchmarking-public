# Results vs. 3.10.4

- fork: faster-cpython
- ref: tier2_hot_cold_split
- machine: linux-x86_64
- commit hash: 96941be
- commit date: 2024-03-19
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 333 ms: 1.05x faster                                                                   |
| chameleon      | 9.44 ms                                                      | 7.56 ms: 1.25x faster                                                                  |
| docutils       | 3.41 sec                                                     | 3.11 sec: 1.10x faster                                                                 |
| html5lib       | 94.6 ms                                                      | 79.8 ms: 1.19x faster                                                                  |
| tornado_http   | 157 ms                                                       | 131 ms: 1.20x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.15x faster                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 452 ms: 1.53x faster                                                                   |
| async_tree_memoization  | 819 ms                                                       | 571 ms: 1.44x faster                                                                   |
| async_tree_io           | 1.60 sec                                                     | 1.12 sec: 1.43x faster                                                                 |
| async_tree_cpu_io_mixed | 936 ms                                                       | 720 ms: 1.30x faster                                                                   |
| Geometric mean          | (ref)                                                        | 1.42x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 102 ms: 1.09x faster                                                                   |
| pidigits       | 271 ms                                                       | 264 ms: 1.03x faster                                                                   |
| nbody          | 134 ms                                                       | 143 ms: 1.07x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 244 ms: 1.07x faster                                                                   |
| regex_v8       | 27.2 ms                                                      | 26.2 ms: 1.03x faster                                                                  |
| regex_compile  | 190 ms                                                       | 215 ms: 1.13x slower                                                                   |
| regex_effbot   | 3.09 ms                                                      | 3.63 ms: 1.17x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 326 us: 1.40x faster                                                                   |
| json_dumps           | 14.5 ms                                                      | 10.9 ms: 1.33x faster                                                                  |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.21x faster                                                                  |
| xml_etree_process    | 75.9 ms                                                      | 63.7 ms: 1.19x faster                                                                  |
| xml_etree_parse      | 160 ms                                                       | 148 ms: 1.08x faster                                                                   |
| unpickle_pure_python | 312 us                                                       | 305 us: 1.02x faster                                                                   |
| unpickle_list        | 4.65 us                                                      | 4.74 us: 1.02x slower                                                                  |
| tomli_loads          | 2.92 sec                                                     | 2.97 sec: 1.02x slower                                                                 |
| xml_etree_iterparse  | 110 ms                                                       | 114 ms: 1.03x slower                                                                   |
| pickle_list          | 4.12 us                                                      | 4.50 us: 1.09x slower                                                                  |
| unpickle             | 13.5 us                                                      | 14.8 us: 1.10x slower                                                                  |
| pickle_dict          | 29.5 us                                                      | 33.0 us: 1.12x slower                                                                  |
| pickle               | 9.89 us                                                      | 11.1 us: 1.12x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                           |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 12.8 ms: 1.11x slower                                                                  |
| python_startup_no_site | 7.33 ms                                                      | 11.2 ms: 1.53x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.30x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 40.3 ms: 1.25x faster                                                                  |
| genshi_text     | 31.4 ms                                                      | 28.2 ms: 1.11x faster                                                                  |
| mako            | 14.7 ms                                                      | 13.9 ms: 1.06x faster                                                                  |
| genshi_xml      | 63.3 ms                                                      | 64.3 ms: 1.02x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.10x faster                                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 131 us: 4.09x faster                                                                   |
| asyncio_tcp              | 779 ms                                                       | 380 ms: 2.05x faster                                                                   |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.60 sec: 1.94x faster                                                                 |
| deltablue                | 7.50 ms                                                      | 4.14 ms: 1.81x faster                                                                  |
| generators               | 57.3 ms                                                      | 33.9 ms: 1.69x faster                                                                  |
| logging_silent           | 167 ns                                                       | 100 ns: 1.67x faster                                                                   |
| async_tree_none          | 692 ms                                                       | 452 ms: 1.53x faster                                                                   |
| pylint                   | 566 ms                                                       | 374 ms: 1.51x faster                                                                   |
| async_tree_memoization   | 819 ms                                                       | 571 ms: 1.44x faster                                                                   |
| async_tree_io            | 1.60 sec                                                     | 1.12 sec: 1.43x faster                                                                 |
| chaos                    | 109 ms                                                       | 77.5 ms: 1.40x faster                                                                  |
| raytrace                 | 489 ms                                                       | 349 ms: 1.40x faster                                                                   |
| pickle_pure_python       | 455 us                                                       | 326 us: 1.40x faster                                                                   |
| crypto_pyaes             | 119 ms                                                       | 85.4 ms: 1.39x faster                                                                  |
| sqlglot_parse            | 2.24 ms                                                      | 1.62 ms: 1.38x faster                                                                  |
| richards_super           | 90.6 ms                                                      | 67.5 ms: 1.34x faster                                                                  |
| coroutines               | 30.3 ms                                                      | 22.6 ms: 1.34x faster                                                                  |
| thrift                   | 1.18 ms                                                      | 880 us: 1.34x faster                                                                   |
| json_dumps               | 14.5 ms                                                      | 10.9 ms: 1.33x faster                                                                  |
| logging_simple           | 8.88 us                                                      | 6.79 us: 1.31x faster                                                                  |
| sqlglot_transpile        | 2.68 ms                                                      | 2.06 ms: 1.30x faster                                                                  |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 720 ms: 1.30x faster                                                                   |
| logging_format           | 9.64 us                                                      | 7.48 us: 1.29x faster                                                                  |
| go                       | 262 ms                                                       | 208 ms: 1.26x faster                                                                   |
| scimark_lu               | 167 ms                                                       | 132 ms: 1.26x faster                                                                   |
| chameleon                | 9.44 ms                                                      | 7.56 ms: 1.25x faster                                                                  |
| django_template          | 50.2 ms                                                      | 40.3 ms: 1.25x faster                                                                  |
| bench_mp_pool            | 6.37 ms                                                      | 5.12 ms: 1.24x faster                                                                  |
| richards                 | 75.1 ms                                                      | 61.2 ms: 1.23x faster                                                                  |
| json_loads               | 30.3 us                                                      | 25.0 us: 1.21x faster                                                                  |
| tornado_http             | 157 ms                                                       | 131 ms: 1.20x faster                                                                   |
| xml_etree_process        | 75.9 ms                                                      | 63.7 ms: 1.19x faster                                                                  |
| html5lib                 | 94.6 ms                                                      | 79.8 ms: 1.19x faster                                                                  |
| deepcopy                 | 468 us                                                       | 404 us: 1.16x faster                                                                   |
| sqlglot_normalize        | 144 ms                                                       | 125 ms: 1.15x faster                                                                   |
| scimark_sor              | 180 ms                                                       | 159 ms: 1.14x faster                                                                   |
| dask                     | 472 ms                                                       | 416 ms: 1.13x faster                                                                   |
| deepcopy_reduce          | 4.01 us                                                      | 3.54 us: 1.13x faster                                                                  |
| scimark_monte_carlo      | 107 ms                                                       | 95.8 ms: 1.12x faster                                                                  |
| mdp                      | 3.01 sec                                                     | 2.70 sec: 1.11x faster                                                                 |
| genshi_text              | 31.4 ms                                                      | 28.2 ms: 1.11x faster                                                                  |
| pyflate                  | 733 ms                                                       | 660 ms: 1.11x faster                                                                   |
| deepcopy_memo            | 49.8 us                                                      | 44.9 us: 1.11x faster                                                                  |
| pycparser                | 1.67 sec                                                     | 1.51 sec: 1.11x faster                                                                 |
| create_gc_cycles         | 1.76 ms                                                      | 1.60 ms: 1.10x faster                                                                  |
| sympy_integrate          | 28.2 ms                                                      | 25.6 ms: 1.10x faster                                                                  |
| docutils                 | 3.41 sec                                                     | 3.11 sec: 1.10x faster                                                                 |
| sympy_sum                | 193 ms                                                       | 176 ms: 1.10x faster                                                                   |
| comprehensions           | 26.7 us                                                      | 24.5 us: 1.09x faster                                                                  |
| float                    | 111 ms                                                       | 102 ms: 1.09x faster                                                                   |
| xml_etree_parse          | 160 ms                                                       | 148 ms: 1.08x faster                                                                   |
| json                     | 5.86 ms                                                      | 5.45 ms: 1.08x faster                                                                  |
| regex_dna                | 261 ms                                                       | 244 ms: 1.07x faster                                                                   |
| pprint_safe_repr         | 1.05 sec                                                     | 981 ms: 1.07x faster                                                                   |
| sqlite_synth             | 2.99 us                                                      | 2.81 us: 1.07x faster                                                                  |
| pprint_pformat           | 2.15 sec                                                     | 2.02 sec: 1.06x faster                                                                 |
| gunicorn                 | 1.16 ms                                                      | 1.09 ms: 1.06x faster                                                                  |
| aiohttp                  | 1.19 ms                                                      | 1.12 ms: 1.06x faster                                                                  |
| pathlib                  | 21.4 ms                                                      | 20.2 ms: 1.06x faster                                                                  |
| async_generators         | 421 ms                                                       | 398 ms: 1.06x faster                                                                   |
| mako                     | 14.7 ms                                                      | 13.9 ms: 1.06x faster                                                                  |
| sympy_str                | 360 ms                                                       | 342 ms: 1.05x faster                                                                   |
| 2to3                     | 350 ms                                                       | 333 ms: 1.05x faster                                                                   |
| regex_v8                 | 27.2 ms                                                      | 26.2 ms: 1.03x faster                                                                  |
| dulwich_log              | 81.1 ms                                                      | 78.4 ms: 1.03x faster                                                                  |
| pidigits                 | 271 ms                                                       | 264 ms: 1.03x faster                                                                   |
| sympy_expand             | 600 ms                                                       | 585 ms: 1.03x faster                                                                   |
| unpickle_pure_python     | 312 us                                                       | 305 us: 1.02x faster                                                                   |
| sqlglot_optimize         | 70.1 ms                                                      | 69.5 ms: 1.01x faster                                                                  |
| meteor_contest           | 138 ms                                                       | 139 ms: 1.01x slower                                                                   |
| genshi_xml               | 63.3 ms                                                      | 64.3 ms: 1.02x slower                                                                  |
| unpickle_list            | 4.65 us                                                      | 4.74 us: 1.02x slower                                                                  |
| tomli_loads              | 2.92 sec                                                     | 2.97 sec: 1.02x slower                                                                 |
| xml_etree_iterparse      | 110 ms                                                       | 114 ms: 1.03x slower                                                                   |
| gc_traversal             | 3.42 ms                                                      | 3.54 ms: 1.04x slower                                                                  |
| spectral_norm            | 139 ms                                                       | 147 ms: 1.06x slower                                                                   |
| nbody                    | 134 ms                                                       | 143 ms: 1.07x slower                                                                   |
| fannkuch                 | 483 ms                                                       | 519 ms: 1.08x slower                                                                   |
| pickle_list              | 4.12 us                                                      | 4.50 us: 1.09x slower                                                                  |
| unpickle                 | 13.5 us                                                      | 14.8 us: 1.10x slower                                                                  |
| python_startup           | 11.5 ms                                                      | 12.8 ms: 1.11x slower                                                                  |
| pickle_dict              | 29.5 us                                                      | 33.0 us: 1.12x slower                                                                  |
| pickle                   | 9.89 us                                                      | 11.1 us: 1.12x slower                                                                  |
| regex_compile            | 190 ms                                                       | 215 ms: 1.13x slower                                                                   |
| hexiom                   | 9.42 ms                                                      | 10.7 ms: 1.13x slower                                                                  |
| unpack_sequence          | 59.9 ns                                                      | 68.0 ns: 1.14x slower                                                                  |
| regex_effbot             | 3.09 ms                                                      | 3.63 ms: 1.17x slower                                                                  |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.98 ms: 1.18x slower                                                                  |
| scimark_fft              | 361 ms                                                       | 432 ms: 1.20x slower                                                                   |
| telco                    | 7.23 ms                                                      | 8.67 ms: 1.20x slower                                                                  |
| coverage                 | 63.3 ms                                                      | 89.3 ms: 1.41x slower                                                                  |
| python_startup_no_site   | 7.33 ms                                                      | 11.2 ms: 1.53x slower                                                                  |
| Geometric mean           | (ref)                                                        | 1.13x faster                                                                           |

Benchmark hidden because not significant (5): asyncio_websockets, nqueens, xml_etree_generate, bench_thread_pool, mypy2
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240319-3.13.0a5+-96941be-PYTHON_UOPS/bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x


# Memory

- memory change: 1.08x