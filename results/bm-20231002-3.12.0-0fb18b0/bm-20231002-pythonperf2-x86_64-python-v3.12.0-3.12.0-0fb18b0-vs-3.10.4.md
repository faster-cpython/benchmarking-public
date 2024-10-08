
# Results vs. 3.10.4

- fork: python
- ref: v3.12.0
- machine: linux-x86_64
- commit hash: 0fb18b0
- commit date: 2023-10-02
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 285 ms: 1.23x faster                                         |
| chameleon      | 9.44 ms                                                      | 7.23 ms: 1.31x faster                                        |
| docutils       | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                       |
| tornado_http   | 157 ms                                                       | 121 ms: 1.29x faster                                         |
| Geometric mean | (ref)                                                        | 1.25x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 1.04 sec: 1.53x faster                                       |
| async_tree_none         | 692 ms                                                       | 452 ms: 1.53x faster                                         |
| async_tree_memoization  | 819 ms                                                       | 544 ms: 1.51x faster                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 696 ms: 1.34x faster                                         |
| Geometric mean          | (ref)                                                        | 1.48x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 88.0 ms: 1.52x faster                                        |
| float          | 111 ms                                                       | 76.6 ms: 1.45x faster                                        |
| pidigits       | 271 ms                                                       | 265 ms: 1.02x faster                                         |
| Geometric mean | (ref)                                                        | 1.31x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 144 ms: 1.32x faster                                         |
| regex_v8       | 27.2 ms                                                      | 23.6 ms: 1.15x faster                                        |
| regex_dna      | 261 ms                                                       | 239 ms: 1.09x faster                                         |
| regex_effbot   | 3.09 ms                                                      | 3.57 ms: 1.16x slower                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 210 us: 1.49x faster                                         |
| pickle_pure_python   | 455 us                                                       | 318 us: 1.43x faster                                         |
| json_dumps           | 14.5 ms                                                      | 10.2 ms: 1.42x faster                                        |
| tomli_loads          | 2.92 sec                                                     | 2.16 sec: 1.35x faster                                       |
| xml_etree_process    | 75.9 ms                                                      | 58.4 ms: 1.30x faster                                        |
| json_loads           | 30.3 us                                                      | 24.4 us: 1.25x faster                                        |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                         |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.07x faster                                         |
| xml_etree_generate   | 92.3 ms                                                      | 86.1 ms: 1.07x faster                                        |
| pickle               | 9.89 us                                                      | 10.5 us: 1.06x slower                                        |
| pickle_list          | 4.12 us                                                      | 4.43 us: 1.08x slower                                        |
| unpickle             | 13.5 us                                                      | 14.8 us: 1.10x slower                                        |
| pickle_dict          | 29.5 us                                                      | 32.5 us: 1.10x slower                                        |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.6 ms: 1.01x slower                                        |
| python_startup_no_site | 7.33 ms                                                      | 8.64 ms: 1.18x slower                                        |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.0 ms: 1.47x faster                                        |
| django_template | 50.2 ms                                                      | 38.2 ms: 1.32x faster                                        |
| Geometric mean  | (ref)                                                        | 1.39x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 152 us: 3.54x faster                                         |
| deltablue                | 7.50 ms                                                      | 3.24 ms: 2.32x faster                                        |
| asyncio_tcp              | 779 ms                                                       | 378 ms: 2.06x faster                                         |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.59 sec: 1.95x faster                                       |
| logging_silent           | 167 ns                                                       | 94.4 ns: 1.77x faster                                        |
| richards_super           | 90.6 ms                                                      | 51.3 ms: 1.76x faster                                        |
| go                       | 262 ms                                                       | 150 ms: 1.75x faster                                         |
| chaos                    | 109 ms                                                       | 64.0 ms: 1.70x faster                                        |
| scimark_lu               | 167 ms                                                       | 98.8 ms: 1.69x faster                                        |
| pyflate                  | 733 ms                                                       | 439 ms: 1.67x faster                                         |
| scimark_sor              | 180 ms                                                       | 109 ms: 1.65x faster                                         |
| richards                 | 75.1 ms                                                      | 45.7 ms: 1.64x faster                                        |
| raytrace                 | 489 ms                                                       | 298 ms: 1.64x faster                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.38 ms: 1.62x faster                                        |
| hexiom                   | 9.42 ms                                                      | 5.96 ms: 1.58x faster                                        |
| scimark_monte_carlo      | 107 ms                                                       | 69.0 ms: 1.56x faster                                        |
| async_tree_io            | 1.60 sec                                                     | 1.04 sec: 1.53x faster                                       |
| generators               | 57.3 ms                                                      | 37.4 ms: 1.53x faster                                        |
| async_tree_none          | 692 ms                                                       | 452 ms: 1.53x faster                                         |
| nbody                    | 134 ms                                                       | 88.0 ms: 1.52x faster                                        |
| spectral_norm            | 139 ms                                                       | 91.6 ms: 1.52x faster                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.78 ms: 1.51x faster                                        |
| async_tree_memoization   | 819 ms                                                       | 544 ms: 1.51x faster                                         |
| unpickle_pure_python     | 312 us                                                       | 210 us: 1.49x faster                                         |
| crypto_pyaes             | 119 ms                                                       | 80.3 ms: 1.48x faster                                        |
| mako                     | 14.7 ms                                                      | 10.0 ms: 1.47x faster                                        |
| float                    | 111 ms                                                       | 76.6 ms: 1.45x faster                                        |
| pickle_pure_python       | 455 us                                                       | 318 us: 1.43x faster                                         |
| json_dumps               | 14.5 ms                                                      | 10.2 ms: 1.42x faster                                        |
| fannkuch                 | 483 ms                                                       | 350 ms: 1.38x faster                                         |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                       |
| deepcopy_memo            | 49.8 us                                                      | 36.8 us: 1.35x faster                                        |
| tomli_loads              | 2.92 sec                                                     | 2.16 sec: 1.35x faster                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 696 ms: 1.34x faster                                         |
| bench_mp_pool            | 6.37 ms                                                      | 4.76 ms: 1.34x faster                                        |
| logging_simple           | 8.88 us                                                      | 6.71 us: 1.32x faster                                        |
| regex_compile            | 190 ms                                                       | 144 ms: 1.32x faster                                         |
| coroutines               | 30.3 ms                                                      | 23.0 ms: 1.32x faster                                        |
| django_template          | 50.2 ms                                                      | 38.2 ms: 1.32x faster                                        |
| chameleon                | 9.44 ms                                                      | 7.23 ms: 1.31x faster                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.30x faster                                       |
| xml_etree_process        | 75.9 ms                                                      | 58.4 ms: 1.30x faster                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 807 ms: 1.30x faster                                         |
| tornado_http             | 157 ms                                                       | 121 ms: 1.29x faster                                         |
| logging_format           | 9.64 us                                                      | 7.48 us: 1.29x faster                                        |
| nqueens                  | 115 ms                                                       | 89.9 ms: 1.28x faster                                        |
| deepcopy                 | 468 us                                                       | 368 us: 1.27x faster                                         |
| json_loads               | 30.3 us                                                      | 24.4 us: 1.25x faster                                        |
| sqlglot_normalize        | 144 ms                                                       | 116 ms: 1.24x faster                                         |
| dulwich_log              | 81.1 ms                                                      | 65.4 ms: 1.24x faster                                        |
| sympy_expand             | 600 ms                                                       | 484 ms: 1.24x faster                                         |
| 2to3                     | 350 ms                                                       | 285 ms: 1.23x faster                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 57.5 ms: 1.22x faster                                        |
| comprehensions           | 26.7 us                                                      | 21.9 us: 1.22x faster                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.7 ms: 1.21x faster                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.21 ms: 1.21x faster                                        |
| dask                     | 472 ms                                                       | 392 ms: 1.20x faster                                         |
| bench_thread_pool        | 1.14 ms                                                      | 950 us: 1.20x faster                                         |
| scimark_fft              | 361 ms                                                       | 301 ms: 1.20x faster                                         |
| sympy_str                | 360 ms                                                       | 302 ms: 1.19x faster                                         |
| docutils                 | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                       |
| sqlalchemy_declarative   | 190 ms                                                       | 159 ms: 1.19x faster                                         |
| deepcopy_reduce          | 4.01 us                                                      | 3.37 us: 1.19x faster                                        |
| sympy_sum                | 193 ms                                                       | 162 ms: 1.19x faster                                         |
| sympy_integrate          | 28.2 ms                                                      | 23.9 ms: 1.18x faster                                        |
| mdp                      | 3.01 sec                                                     | 2.57 sec: 1.17x faster                                       |
| aiohttp                  | 1.19 ms                                                      | 1.02 ms: 1.17x faster                                        |
| gunicorn                 | 1.16 ms                                                      | 1.00 ms: 1.16x faster                                        |
| regex_v8                 | 27.2 ms                                                      | 23.6 ms: 1.15x faster                                        |
| json                     | 5.86 ms                                                      | 5.12 ms: 1.15x faster                                        |
| pathlib                  | 21.4 ms                                                      | 18.9 ms: 1.13x faster                                        |
| unpack_sequence          | 59.9 ns                                                      | 53.2 ns: 1.13x faster                                        |
| mypy2                    | 933 ms                                                       | 830 ms: 1.12x faster                                         |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.11x faster                                         |
| create_gc_cycles         | 1.76 ms                                                      | 1.59 ms: 1.11x faster                                        |
| regex_dna                | 261 ms                                                       | 239 ms: 1.09x faster                                         |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                         |
| async_generators         | 421 ms                                                       | 390 ms: 1.08x faster                                         |
| sqlite_synth             | 2.99 us                                                      | 2.77 us: 1.08x faster                                        |
| xml_etree_iterparse      | 110 ms                                                       | 103 ms: 1.07x faster                                         |
| xml_etree_generate       | 92.3 ms                                                      | 86.1 ms: 1.07x faster                                        |
| telco                    | 7.23 ms                                                      | 6.96 ms: 1.04x faster                                        |
| pidigits                 | 271 ms                                                       | 265 ms: 1.02x faster                                         |
| asyncio_websockets       | 390 ms                                                       | 387 ms: 1.01x faster                                         |
| python_startup           | 11.5 ms                                                      | 11.6 ms: 1.01x slower                                        |
| gc_traversal             | 3.42 ms                                                      | 3.48 ms: 1.02x slower                                        |
| coverage                 | 63.3 ms                                                      | 66.7 ms: 1.05x slower                                        |
| pickle                   | 9.89 us                                                      | 10.5 us: 1.06x slower                                        |
| pickle_list              | 4.12 us                                                      | 4.43 us: 1.08x slower                                        |
| unpickle                 | 13.5 us                                                      | 14.8 us: 1.10x slower                                        |
| pickle_dict              | 29.5 us                                                      | 32.5 us: 1.10x slower                                        |
| regex_effbot             | 3.09 ms                                                      | 3.57 ms: 1.16x slower                                        |
| python_startup_no_site   | 7.33 ms                                                      | 8.64 ms: 1.18x slower                                        |
| Geometric mean           | (ref)                                                        | 1.30x faster                                                 |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x


# Memory

- memory change: 1.23x