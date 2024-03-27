# Results vs. 3.10.4

- fork: brandtbucher
- ref: main
- machine: linux-x86_64
- commit hash: 74c8568
- commit date: 2024-03-27
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 267 ms: 1.30x faster                                         |
| chameleon      | 9.68 ms                                                | 6.82 ms: 1.42x faster                                        |
| docutils       | 3.30 sec                                               | 2.77 sec: 1.19x faster                                       |
| html5lib       | 88.9 ms                                                | 67.9 ms: 1.31x faster                                        |
| tornado_http   | 136 ms                                                 | 94.8 ms: 1.44x faster                                        |
| Geometric mean | (ref)                                                  | 1.33x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization  | 870 ms                                                 | 440 ms: 1.98x faster                                         |
| async_tree_io           | 1.77 sec                                               | 915 ms: 1.93x faster                                         |
| async_tree_none         | 728 ms                                                 | 381 ms: 1.91x faster                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 592 ms: 1.72x faster                                         |
| Geometric mean          | (ref)                                                  | 1.88x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 88.3 ms: 1.74x faster                                        |
| float          | 117 ms                                                 | 76.6 ms: 1.53x faster                                        |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                  | 1.39x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 133 ms: 1.42x faster                                         |
| regex_v8       | 27.8 ms                                                | 26.0 ms: 1.07x faster                                        |
| regex_dna      | 227 ms                                                 | 230 ms: 1.02x slower                                         |
| regex_effbot   | 3.63 ms                                                | 3.81 ms: 1.05x slower                                        |
| Geometric mean | (ref)                                                  | 1.09x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 297 us: 1.63x faster                                         |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                         |
| tomli_loads          | 3.14 sec                                               | 2.20 sec: 1.43x faster                                       |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                        |
| xml_etree_process    | 79.1 ms                                                | 59.8 ms: 1.32x faster                                        |
| xml_etree_generate   | 99.4 ms                                                | 85.8 ms: 1.16x faster                                        |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                        |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                         |
| xml_etree_parse      | 168 ms                                                 | 161 ms: 1.04x faster                                         |
| unpickle_list        | 5.20 us                                                | 5.26 us: 1.01x slower                                        |
| pickle_list          | 5.08 us                                                | 5.40 us: 1.06x slower                                        |
| pickle               | 10.7 us                                                | 12.0 us: 1.13x slower                                        |
| unpickle             | 14.4 us                                                | 16.7 us: 1.16x slower                                        |
| pickle_dict          | 29.6 us                                                | 35.6 us: 1.20x slower                                        |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.37x faster                                        |
| python_startup_no_site | 5.93 ms                                                | 9.00 ms: 1.52x slower                                        |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.7 ms: 1.52x faster                                        |
| django_template | 48.2 ms                                                | 34.8 ms: 1.38x faster                                        |
| genshi_text     | 31.8 ms                                                | 24.0 ms: 1.33x faster                                        |
| genshi_xml      | 66.0 ms                                                | 50.8 ms: 1.30x faster                                        |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 111 us: 4.91x faster                                         |
| generators               | 80.1 ms                                                | 29.5 ms: 2.71x faster                                        |
| deltablue                | 7.91 ms                                                | 3.26 ms: 2.43x faster                                        |
| async_tree_memoization   | 870 ms                                                 | 440 ms: 1.98x faster                                         |
| chaos                    | 115 ms                                                 | 59.7 ms: 1.93x faster                                        |
| async_tree_io            | 1.77 sec                                               | 915 ms: 1.93x faster                                         |
| raytrace                 | 507 ms                                                 | 263 ms: 1.92x faster                                         |
| logging_silent           | 190 ns                                                 | 98.9 ns: 1.92x faster                                        |
| async_tree_none          | 728 ms                                                 | 381 ms: 1.91x faster                                         |
| richards_super           | 94.7 ms                                                | 51.2 ms: 1.85x faster                                        |
| asyncio_tcp              | 922 ms                                                 | 501 ms: 1.84x faster                                         |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.80x faster                                         |
| scimark_monte_carlo      | 118 ms                                                 | 66.0 ms: 1.79x faster                                        |
| crypto_pyaes             | 128 ms                                                 | 73.1 ms: 1.75x faster                                        |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.75x faster                                        |
| richards                 | 79.3 ms                                                | 45.4 ms: 1.75x faster                                        |
| nbody                    | 154 ms                                                 | 88.3 ms: 1.74x faster                                        |
| pylint                   | 551 ms                                                 | 318 ms: 1.74x faster                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 592 ms: 1.72x faster                                         |
| go                       | 240 ms                                                 | 140 ms: 1.72x faster                                         |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                        |
| hexiom                   | 10.4 ms                                                | 6.19 ms: 1.68x faster                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                        |
| pickle_pure_python       | 484 us                                                 | 297 us: 1.63x faster                                         |
| deepcopy_memo            | 58.5 us                                                | 37.0 us: 1.58x faster                                        |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.55x faster                                         |
| spectral_norm            | 170 ms                                                 | 110 ms: 1.55x faster                                         |
| pyflate                  | 716 ms                                                 | 464 ms: 1.54x faster                                         |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                         |
| float                    | 117 ms                                                 | 76.6 ms: 1.53x faster                                        |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                        |
| mako                     | 16.3 ms                                                | 10.7 ms: 1.52x faster                                        |
| tornado_http             | 136 ms                                                 | 94.8 ms: 1.44x faster                                        |
| tomli_loads              | 3.14 sec                                               | 2.20 sec: 1.43x faster                                       |
| chameleon                | 9.68 ms                                                | 6.82 ms: 1.42x faster                                        |
| regex_compile            | 188 ms                                                 | 133 ms: 1.42x faster                                         |
| logging_simple           | 8.30 us                                                | 5.87 us: 1.41x faster                                        |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.84 sec: 1.40x faster                                       |
| django_template          | 48.2 ms                                                | 34.8 ms: 1.38x faster                                        |
| deepcopy                 | 479 us                                                 | 347 us: 1.38x faster                                         |
| logging_format           | 9.09 us                                                | 6.59 us: 1.38x faster                                        |
| pprint_safe_repr         | 1.02 sec                                               | 740 ms: 1.38x faster                                         |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.37x faster                                        |
| fannkuch                 | 532 ms                                                 | 391 ms: 1.36x faster                                         |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                        |
| unpack_sequence          | 60.0 ns                                                | 44.4 ns: 1.35x faster                                        |
| deepcopy_reduce          | 4.17 us                                                | 3.10 us: 1.34x faster                                        |
| genshi_text              | 31.8 ms                                                | 24.0 ms: 1.33x faster                                        |
| xml_etree_process        | 79.1 ms                                                | 59.8 ms: 1.32x faster                                        |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                         |
| nqueens                  | 106 ms                                                 | 80.5 ms: 1.31x faster                                        |
| html5lib                 | 88.9 ms                                                | 67.9 ms: 1.31x faster                                        |
| thrift                   | 1.07 ms                                                | 819 us: 1.31x faster                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.95 ms: 1.31x faster                                        |
| 2to3                     | 348 ms                                                 | 267 ms: 1.30x faster                                         |
| scimark_fft              | 466 ms                                                 | 358 ms: 1.30x faster                                         |
| genshi_xml               | 66.0 ms                                                | 50.8 ms: 1.30x faster                                        |
| sympy_integrate          | 25.8 ms                                                | 20.0 ms: 1.29x faster                                        |
| pycparser                | 1.58 sec                                               | 1.22 sec: 1.29x faster                                       |
| sympy_sum                | 196 ms                                                 | 153 ms: 1.29x faster                                         |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                         |
| sqlglot_optimize         | 69.2 ms                                                | 54.7 ms: 1.26x faster                                        |
| dulwich_log              | 84.3 ms                                                | 67.3 ms: 1.25x faster                                        |
| sympy_expand             | 566 ms                                                 | 461 ms: 1.23x faster                                         |
| aiohttp                  | 1.44 ms                                                | 1.18 ms: 1.22x faster                                        |
| mypy2                    | 894 ms                                                 | 733 ms: 1.22x faster                                         |
| djangocms                | 38.4 us                                                | 31.7 us: 1.21x faster                                        |
| gunicorn                 | 1.53 ms                                                | 1.28 ms: 1.20x faster                                        |
| dask                     | 441 ms                                                 | 367 ms: 1.20x faster                                         |
| bench_thread_pool        | 986 us                                                 | 825 us: 1.19x faster                                         |
| docutils                 | 3.30 sec                                               | 2.77 sec: 1.19x faster                                       |
| xml_etree_generate       | 99.4 ms                                                | 85.8 ms: 1.16x faster                                        |
| pathlib                  | 20.5 ms                                                | 18.5 ms: 1.10x faster                                        |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                         |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                        |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                         |
| regex_v8                 | 27.8 ms                                                | 26.0 ms: 1.07x faster                                        |
| json                     | 5.69 ms                                                | 5.37 ms: 1.06x faster                                        |
| mdp                      | 2.85 sec                                               | 2.70 sec: 1.05x faster                                       |
| sqlite_synth             | 3.02 us                                                | 2.88 us: 1.05x faster                                        |
| xml_etree_parse          | 168 ms                                                 | 161 ms: 1.04x faster                                         |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                         |
| bench_mp_pool            | 24.0 ms                                                | 23.8 ms: 1.01x faster                                        |
| async_generators         | 444 ms                                                 | 441 ms: 1.01x faster                                         |
| unpickle_list            | 5.20 us                                                | 5.26 us: 1.01x slower                                        |
| regex_dna                | 227 ms                                                 | 230 ms: 1.02x slower                                         |
| asyncio_websockets       | 559 ms                                                 | 569 ms: 1.02x slower                                         |
| create_gc_cycles         | 1.62 ms                                                | 1.68 ms: 1.04x slower                                        |
| regex_effbot             | 3.63 ms                                                | 3.81 ms: 1.05x slower                                        |
| pickle_list              | 5.08 us                                                | 5.40 us: 1.06x slower                                        |
| gc_traversal             | 3.62 ms                                                | 4.01 ms: 1.11x slower                                        |
| pickle                   | 10.7 us                                                | 12.0 us: 1.13x slower                                        |
| unpickle                 | 14.4 us                                                | 16.7 us: 1.16x slower                                        |
| telco                    | 7.27 ms                                                | 8.59 ms: 1.18x slower                                        |
| pickle_dict              | 29.6 us                                                | 35.6 us: 1.20x slower                                        |
| coverage                 | 79.4 ms                                                | 97.2 ms: 1.22x slower                                        |
| python_startup_no_site   | 5.93 ms                                                | 9.00 ms: 1.52x slower                                        |
| Geometric mean           | (ref)                                                  | 1.35x faster                                                 |
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240327-3.13.0a5+-74c8568/bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.27x


# Memory

- memory change: 1.09x