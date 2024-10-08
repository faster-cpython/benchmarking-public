
# Results vs. 3.12.0

- fork: python
- ref: v3.10.4
- machine: linux-x86_64
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.30x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x slower
- Memory change: 0.84x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 350 ms: 1.23x slower                                         |
| chameleon      | 7.23 ms                                                      | 9.44 ms: 1.31x slower                                        |
| docutils       | 2.87 sec                                                     | 3.41 sec: 1.19x slower                                       |
| tornado_http   | 121 ms                                                       | 157 ms: 1.29x slower                                         |
| Geometric mean | (ref)                                                        | 1.25x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 696 ms                                                       | 936 ms: 1.34x slower                                         |
| async_tree_memoization  | 544 ms                                                       | 819 ms: 1.51x slower                                         |
| async_tree_none         | 452 ms                                                       | 692 ms: 1.53x slower                                         |
| async_tree_io           | 1.04 sec                                                     | 1.60 sec: 1.53x slower                                       |
| Geometric mean          | (ref)                                                        | 1.48x slower                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 271 ms: 1.02x slower                                         |
| float          | 76.6 ms                                                      | 111 ms: 1.45x slower                                         |
| nbody          | 88.0 ms                                                      | 134 ms: 1.52x slower                                         |
| Geometric mean | (ref)                                                        | 1.31x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.09 ms: 1.16x faster                                        |
| regex_dna      | 239 ms                                                       | 261 ms: 1.09x slower                                         |
| regex_v8       | 23.6 ms                                                      | 27.2 ms: 1.15x slower                                        |
| regex_compile  | 144 ms                                                       | 190 ms: 1.32x slower                                         |
| Geometric mean | (ref)                                                        | 1.09x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 29.5 us: 1.10x faster                                        |
| unpickle             | 14.8 us                                                      | 13.5 us: 1.10x faster                                        |
| pickle_list          | 4.43 us                                                      | 4.12 us: 1.08x faster                                        |
| pickle               | 10.5 us                                                      | 9.89 us: 1.06x faster                                        |
| xml_etree_generate   | 86.1 ms                                                      | 92.3 ms: 1.07x slower                                        |
| xml_etree_iterparse  | 103 ms                                                       | 110 ms: 1.07x slower                                         |
| xml_etree_parse      | 144 ms                                                       | 160 ms: 1.11x slower                                         |
| json_loads           | 24.4 us                                                      | 30.3 us: 1.25x slower                                        |
| xml_etree_process    | 58.4 ms                                                      | 75.9 ms: 1.30x slower                                        |
| tomli_loads          | 2.16 sec                                                     | 2.92 sec: 1.35x slower                                       |
| json_dumps           | 10.2 ms                                                      | 14.5 ms: 1.42x slower                                        |
| pickle_pure_python   | 318 us                                                       | 455 us: 1.43x slower                                         |
| unpickle_pure_python | 210 us                                                       | 312 us: 1.49x slower                                         |
| Geometric mean       | (ref)                                                        | 1.14x slower                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 7.33 ms: 1.18x faster                                        |
| python_startup         | 11.6 ms                                                      | 11.5 ms: 1.01x faster                                        |
| Geometric mean         | (ref)                                                        | 1.09x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 50.2 ms: 1.32x slower                                        |
| mako            | 10.0 ms                                                      | 14.7 ms: 1.47x slower                                        |
| Geometric mean  | (ref)                                                        | 1.39x slower                                                 |

All benchmarks:
===============

| Benchmark                | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site   | 8.64 ms                                                      | 7.33 ms: 1.18x faster                                        |
| regex_effbot             | 3.57 ms                                                      | 3.09 ms: 1.16x faster                                        |
| pickle_dict              | 32.5 us                                                      | 29.5 us: 1.10x faster                                        |
| unpickle                 | 14.8 us                                                      | 13.5 us: 1.10x faster                                        |
| pickle_list              | 4.43 us                                                      | 4.12 us: 1.08x faster                                        |
| pickle                   | 10.5 us                                                      | 9.89 us: 1.06x faster                                        |
| coverage                 | 66.7 ms                                                      | 63.3 ms: 1.05x faster                                        |
| gc_traversal             | 3.48 ms                                                      | 3.42 ms: 1.02x faster                                        |
| python_startup           | 11.6 ms                                                      | 11.5 ms: 1.01x faster                                        |
| asyncio_websockets       | 387 ms                                                       | 390 ms: 1.01x slower                                         |
| pidigits                 | 265 ms                                                       | 271 ms: 1.02x slower                                         |
| telco                    | 6.96 ms                                                      | 7.23 ms: 1.04x slower                                        |
| xml_etree_generate       | 86.1 ms                                                      | 92.3 ms: 1.07x slower                                        |
| xml_etree_iterparse      | 103 ms                                                       | 110 ms: 1.07x slower                                         |
| sqlite_synth             | 2.77 us                                                      | 2.99 us: 1.08x slower                                        |
| async_generators         | 390 ms                                                       | 421 ms: 1.08x slower                                         |
| meteor_contest           | 128 ms                                                       | 138 ms: 1.08x slower                                         |
| regex_dna                | 239 ms                                                       | 261 ms: 1.09x slower                                         |
| create_gc_cycles         | 1.59 ms                                                      | 1.76 ms: 1.11x slower                                        |
| xml_etree_parse          | 144 ms                                                       | 160 ms: 1.11x slower                                         |
| mypy2                    | 830 ms                                                       | 933 ms: 1.12x slower                                         |
| unpack_sequence          | 53.2 ns                                                      | 59.9 ns: 1.13x slower                                        |
| pathlib                  | 18.9 ms                                                      | 21.4 ms: 1.13x slower                                        |
| json                     | 5.12 ms                                                      | 5.86 ms: 1.15x slower                                        |
| regex_v8                 | 23.6 ms                                                      | 27.2 ms: 1.15x slower                                        |
| gunicorn                 | 1.00 ms                                                      | 1.16 ms: 1.16x slower                                        |
| aiohttp                  | 1.02 ms                                                      | 1.19 ms: 1.17x slower                                        |
| mdp                      | 2.57 sec                                                     | 3.01 sec: 1.17x slower                                       |
| sympy_integrate          | 23.9 ms                                                      | 28.2 ms: 1.18x slower                                        |
| sympy_sum                | 162 ms                                                       | 193 ms: 1.19x slower                                         |
| deepcopy_reduce          | 3.37 us                                                      | 4.01 us: 1.19x slower                                        |
| sqlalchemy_declarative   | 159 ms                                                       | 190 ms: 1.19x slower                                         |
| docutils                 | 2.87 sec                                                     | 3.41 sec: 1.19x slower                                       |
| sympy_str                | 302 ms                                                       | 360 ms: 1.19x slower                                         |
| scimark_fft              | 301 ms                                                       | 361 ms: 1.20x slower                                         |
| bench_thread_pool        | 950 us                                                       | 1.14 ms: 1.20x slower                                        |
| dask                     | 392 ms                                                       | 472 ms: 1.20x slower                                         |
| scimark_sparse_mat_mult  | 4.21 ms                                                      | 5.08 ms: 1.21x slower                                        |
| sqlalchemy_imperative    | 18.7 ms                                                      | 22.7 ms: 1.21x slower                                        |
| comprehensions           | 21.9 us                                                      | 26.7 us: 1.22x slower                                        |
| sqlglot_optimize         | 57.5 ms                                                      | 70.1 ms: 1.22x slower                                        |
| 2to3                     | 285 ms                                                       | 350 ms: 1.23x slower                                         |
| sympy_expand             | 484 ms                                                       | 600 ms: 1.24x slower                                         |
| dulwich_log              | 65.4 ms                                                      | 81.1 ms: 1.24x slower                                        |
| sqlglot_normalize        | 116 ms                                                       | 144 ms: 1.24x slower                                         |
| json_loads               | 24.4 us                                                      | 30.3 us: 1.25x slower                                        |
| deepcopy                 | 368 us                                                       | 468 us: 1.27x slower                                         |
| nqueens                  | 89.9 ms                                                      | 115 ms: 1.28x slower                                         |
| logging_format           | 7.48 us                                                      | 9.64 us: 1.29x slower                                        |
| tornado_http             | 121 ms                                                       | 157 ms: 1.29x slower                                         |
| pprint_safe_repr         | 807 ms                                                       | 1.05 sec: 1.30x slower                                       |
| xml_etree_process        | 58.4 ms                                                      | 75.9 ms: 1.30x slower                                        |
| pprint_pformat           | 1.65 sec                                                     | 2.15 sec: 1.30x slower                                       |
| chameleon                | 7.23 ms                                                      | 9.44 ms: 1.31x slower                                        |
| django_template          | 38.2 ms                                                      | 50.2 ms: 1.32x slower                                        |
| coroutines               | 23.0 ms                                                      | 30.3 ms: 1.32x slower                                        |
| regex_compile            | 144 ms                                                       | 190 ms: 1.32x slower                                         |
| logging_simple           | 6.71 us                                                      | 8.88 us: 1.32x slower                                        |
| bench_mp_pool            | 4.76 ms                                                      | 6.37 ms: 1.34x slower                                        |
| async_tree_cpu_io_mixed  | 696 ms                                                       | 936 ms: 1.34x slower                                         |
| tomli_loads              | 2.16 sec                                                     | 2.92 sec: 1.35x slower                                       |
| deepcopy_memo            | 36.8 us                                                      | 49.8 us: 1.35x slower                                        |
| pycparser                | 1.23 sec                                                     | 1.67 sec: 1.36x slower                                       |
| fannkuch                 | 350 ms                                                       | 483 ms: 1.38x slower                                         |
| json_dumps               | 10.2 ms                                                      | 14.5 ms: 1.42x slower                                        |
| pickle_pure_python       | 318 us                                                       | 455 us: 1.43x slower                                         |
| float                    | 76.6 ms                                                      | 111 ms: 1.45x slower                                         |
| mako                     | 10.0 ms                                                      | 14.7 ms: 1.47x slower                                        |
| crypto_pyaes             | 80.3 ms                                                      | 119 ms: 1.48x slower                                         |
| unpickle_pure_python     | 210 us                                                       | 312 us: 1.49x slower                                         |
| async_tree_memoization   | 544 ms                                                       | 819 ms: 1.51x slower                                         |
| sqlglot_transpile        | 1.78 ms                                                      | 2.68 ms: 1.51x slower                                        |
| spectral_norm            | 91.6 ms                                                      | 139 ms: 1.52x slower                                         |
| nbody                    | 88.0 ms                                                      | 134 ms: 1.52x slower                                         |
| async_tree_none          | 452 ms                                                       | 692 ms: 1.53x slower                                         |
| generators               | 37.4 ms                                                      | 57.3 ms: 1.53x slower                                        |
| async_tree_io            | 1.04 sec                                                     | 1.60 sec: 1.53x slower                                       |
| scimark_monte_carlo      | 69.0 ms                                                      | 107 ms: 1.56x slower                                         |
| hexiom                   | 5.96 ms                                                      | 9.42 ms: 1.58x slower                                        |
| sqlglot_parse            | 1.38 ms                                                      | 2.24 ms: 1.62x slower                                        |
| raytrace                 | 298 ms                                                       | 489 ms: 1.64x slower                                         |
| richards                 | 45.7 ms                                                      | 75.1 ms: 1.64x slower                                        |
| scimark_sor              | 109 ms                                                       | 180 ms: 1.65x slower                                         |
| pyflate                  | 439 ms                                                       | 733 ms: 1.67x slower                                         |
| scimark_lu               | 98.8 ms                                                      | 167 ms: 1.69x slower                                         |
| chaos                    | 64.0 ms                                                      | 109 ms: 1.70x slower                                         |
| go                       | 150 ms                                                       | 262 ms: 1.75x slower                                         |
| richards_super           | 51.3 ms                                                      | 90.6 ms: 1.76x slower                                        |
| logging_silent           | 94.4 ns                                                      | 167 ns: 1.77x slower                                         |
| asyncio_tcp_ssl          | 1.59 sec                                                     | 3.10 sec: 1.95x slower                                       |
| asyncio_tcp              | 378 ms                                                       | 779 ms: 2.06x slower                                         |
| deltablue                | 3.24 ms                                                      | 7.50 ms: 2.32x slower                                        |
| typing_runtime_protocols | 152 us                                                       | 537 us: 3.54x slower                                         |
| Geometric mean           | (ref)                                                        | 1.30x slower                                                 |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.25x
- 95% likely to have a slowdown of 1.24x
- 99% likely to have a slowdown of 1.22x


# Memory

- memory change: 0.84x