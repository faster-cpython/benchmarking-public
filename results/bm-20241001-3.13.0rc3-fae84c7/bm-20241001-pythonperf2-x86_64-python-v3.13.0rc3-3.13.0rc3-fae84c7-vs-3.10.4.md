# Results vs. 3.10.4

- fork: python
- ref: v3.13.0rc3
- machine: linux-x86_64
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.292x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 290 ms: 1.21x faster                                               |
| chameleon      | 9.44 ms                                                      | 7.54 ms: 1.25x faster                                              |
| docutils       | 3.41 sec                                                     | 2.81 sec: 1.22x faster                                             |
| html5lib       | 94.6 ms                                                      | 73.7 ms: 1.28x faster                                              |
| tornado_http   | 157 ms                                                       | 119 ms: 1.31x faster                                               |
| Geometric mean | (ref)                                                        | 1.25x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 842 ms: 1.90x faster                                               |
| async_tree_none         | 692 ms                                                       | 375 ms: 1.84x faster                                               |
| async_tree_memoization  | 819 ms                                                       | 456 ms: 1.80x faster                                               |
| async_tree_cpu_io_mixed | 936 ms                                                       | 603 ms: 1.55x faster                                               |
| Geometric mean          | (ref)                                                        | 1.77x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 87.5 ms: 1.53x faster                                              |
| float          | 111 ms                                                       | 81.6 ms: 1.36x faster                                              |
| pidigits       | 271 ms                                                       | 252 ms: 1.07x faster                                               |
| Geometric mean | (ref)                                                        | 1.31x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 145 ms: 1.31x faster                                               |
| regex_v8       | 27.2 ms                                                      | 25.3 ms: 1.07x faster                                              |
| regex_dna      | 261 ms                                                       | 246 ms: 1.06x faster                                               |
| regex_effbot   | 3.09 ms                                                      | 3.55 ms: 1.15x slower                                              |
| Geometric mean | (ref)                                                        | 1.07x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 216 us: 1.45x faster                                               |
| pickle_pure_python   | 455 us                                                       | 316 us: 1.44x faster                                               |
| json_dumps           | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                              |
| xml_etree_process    | 75.9 ms                                                      | 59.9 ms: 1.27x faster                                              |
| json_loads           | 30.3 us                                                      | 24.5 us: 1.24x faster                                              |
| tomli_loads          | 2.92 sec                                                     | 2.43 sec: 1.20x faster                                             |
| xml_etree_generate   | 92.3 ms                                                      | 85.3 ms: 1.08x faster                                              |
| xml_etree_parse      | 160 ms                                                       | 149 ms: 1.08x faster                                               |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.07x faster                                               |
| pickle_dict          | 29.5 us                                                      | 30.4 us: 1.03x slower                                              |
| pickle               | 9.89 us                                                      | 10.2 us: 1.03x slower                                              |
| unpickle_list        | 4.65 us                                                      | 4.81 us: 1.03x slower                                              |
| pickle_list          | 4.12 us                                                      | 4.31 us: 1.05x slower                                              |
| unpickle             | 13.5 us                                                      | 16.0 us: 1.18x slower                                              |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                              |
| python_startup_no_site | 7.33 ms                                                      | 8.94 ms: 1.22x slower                                              |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                              |
| django_template | 50.2 ms                                                      | 38.8 ms: 1.29x faster                                              |
| genshi_text     | 31.4 ms                                                      | 25.7 ms: 1.22x faster                                              |
| genshi_xml      | 63.3 ms                                                      | 56.0 ms: 1.13x faster                                              |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 176 us: 3.05x faster                                               |
| deltablue                | 7.50 ms                                                      | 3.39 ms: 2.21x faster                                              |
| asyncio_tcp              | 779 ms                                                       | 384 ms: 2.03x faster                                               |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                             |
| async_tree_io            | 1.60 sec                                                     | 842 ms: 1.90x faster                                               |
| raytrace                 | 489 ms                                                       | 262 ms: 1.86x faster                                               |
| async_tree_none          | 692 ms                                                       | 375 ms: 1.84x faster                                               |
| async_tree_memoization   | 819 ms                                                       | 456 ms: 1.80x faster                                               |
| chaos                    | 109 ms                                                       | 60.9 ms: 1.78x faster                                              |
| generators               | 57.3 ms                                                      | 33.2 ms: 1.73x faster                                              |
| scimark_lu               | 167 ms                                                       | 97.1 ms: 1.72x faster                                              |
| logging_silent           | 167 ns                                                       | 97.8 ns: 1.71x faster                                              |
| scimark_monte_carlo      | 107 ms                                                       | 64.9 ms: 1.66x faster                                              |
| pylint                   | 566 ms                                                       | 347 ms: 1.63x faster                                               |
| crypto_pyaes             | 119 ms                                                       | 73.0 ms: 1.63x faster                                              |
| sqlglot_parse            | 2.24 ms                                                      | 1.40 ms: 1.59x faster                                              |
| go                       | 262 ms                                                       | 166 ms: 1.58x faster                                               |
| comprehensions           | 26.7 us                                                      | 17.2 us: 1.55x faster                                              |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 603 ms: 1.55x faster                                               |
| nbody                    | 134 ms                                                       | 87.5 ms: 1.53x faster                                              |
| richards_super           | 90.6 ms                                                      | 59.3 ms: 1.53x faster                                              |
| scimark_sor              | 180 ms                                                       | 118 ms: 1.53x faster                                               |
| pyflate                  | 733 ms                                                       | 487 ms: 1.51x faster                                               |
| sqlglot_transpile        | 2.68 ms                                                      | 1.79 ms: 1.50x faster                                              |
| hexiom                   | 9.42 ms                                                      | 6.33 ms: 1.49x faster                                              |
| spectral_norm            | 139 ms                                                       | 95.8 ms: 1.45x faster                                              |
| unpickle_pure_python     | 312 us                                                       | 216 us: 1.45x faster                                               |
| pickle_pure_python       | 455 us                                                       | 316 us: 1.44x faster                                               |
| richards                 | 75.1 ms                                                      | 52.5 ms: 1.43x faster                                              |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                              |
| float                    | 111 ms                                                       | 81.6 ms: 1.36x faster                                              |
| logging_simple           | 8.88 us                                                      | 6.60 us: 1.35x faster                                              |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.34x faster                                             |
| logging_format           | 9.64 us                                                      | 7.23 us: 1.33x faster                                              |
| fannkuch                 | 483 ms                                                       | 364 ms: 1.33x faster                                               |
| bench_mp_pool            | 6.37 ms                                                      | 4.81 ms: 1.33x faster                                              |
| coroutines               | 30.3 ms                                                      | 23.0 ms: 1.32x faster                                              |
| regex_compile            | 190 ms                                                       | 145 ms: 1.31x faster                                               |
| tornado_http             | 157 ms                                                       | 119 ms: 1.31x faster                                               |
| thrift                   | 1.18 ms                                                      | 895 us: 1.31x faster                                               |
| deepcopy_memo            | 49.8 us                                                      | 37.9 us: 1.31x faster                                              |
| json_dumps               | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                              |
| django_template          | 50.2 ms                                                      | 38.8 ms: 1.29x faster                                              |
| nqueens                  | 115 ms                                                       | 89.1 ms: 1.29x faster                                              |
| pprint_pformat           | 2.15 sec                                                     | 1.67 sec: 1.29x faster                                             |
| html5lib                 | 94.6 ms                                                      | 73.7 ms: 1.28x faster                                              |
| pprint_safe_repr         | 1.05 sec                                                     | 820 ms: 1.28x faster                                               |
| xml_etree_process        | 75.9 ms                                                      | 59.9 ms: 1.27x faster                                              |
| bench_thread_pool        | 1.14 ms                                                      | 906 us: 1.26x faster                                               |
| dulwich_log              | 81.1 ms                                                      | 64.6 ms: 1.25x faster                                              |
| chameleon                | 9.44 ms                                                      | 7.54 ms: 1.25x faster                                              |
| dask                     | 472 ms                                                       | 379 ms: 1.24x faster                                               |
| sympy_sum                | 193 ms                                                       | 155 ms: 1.24x faster                                               |
| json_loads               | 30.3 us                                                      | 24.5 us: 1.24x faster                                              |
| pathlib                  | 21.4 ms                                                      | 17.4 ms: 1.23x faster                                              |
| genshi_text              | 31.4 ms                                                      | 25.7 ms: 1.22x faster                                              |
| deepcopy                 | 468 us                                                       | 384 us: 1.22x faster                                               |
| docutils                 | 3.41 sec                                                     | 2.81 sec: 1.22x faster                                             |
| sympy_str                | 360 ms                                                       | 298 ms: 1.21x faster                                               |
| 2to3                     | 350 ms                                                       | 290 ms: 1.21x faster                                               |
| sympy_integrate          | 28.2 ms                                                      | 23.4 ms: 1.20x faster                                              |
| tomli_loads              | 2.92 sec                                                     | 2.43 sec: 1.20x faster                                             |
| sqlglot_normalize        | 144 ms                                                       | 120 ms: 1.20x faster                                               |
| scimark_fft              | 361 ms                                                       | 302 ms: 1.20x faster                                               |
| sympy_expand             | 600 ms                                                       | 506 ms: 1.19x faster                                               |
| mdp                      | 3.01 sec                                                     | 2.55 sec: 1.18x faster                                             |
| sqlglot_optimize         | 70.1 ms                                                      | 60.1 ms: 1.17x faster                                              |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.36 ms: 1.17x faster                                              |
| deepcopy_reduce          | 4.01 us                                                      | 3.44 us: 1.16x faster                                              |
| async_generators         | 421 ms                                                       | 366 ms: 1.15x faster                                               |
| genshi_xml               | 63.3 ms                                                      | 56.0 ms: 1.13x faster                                              |
| gunicorn                 | 1.16 ms                                                      | 1.03 ms: 1.13x faster                                              |
| json                     | 5.86 ms                                                      | 5.29 ms: 1.11x faster                                              |
| aiohttp                  | 1.19 ms                                                      | 1.08 ms: 1.10x faster                                              |
| xml_etree_generate       | 92.3 ms                                                      | 85.3 ms: 1.08x faster                                              |
| xml_etree_parse          | 160 ms                                                       | 149 ms: 1.08x faster                                               |
| regex_v8                 | 27.2 ms                                                      | 25.3 ms: 1.07x faster                                              |
| pidigits                 | 271 ms                                                       | 252 ms: 1.07x faster                                               |
| xml_etree_iterparse      | 110 ms                                                       | 103 ms: 1.07x faster                                               |
| meteor_contest           | 138 ms                                                       | 130 ms: 1.07x faster                                               |
| sqlite_synth             | 2.99 us                                                      | 2.81 us: 1.07x faster                                              |
| regex_dna                | 261 ms                                                       | 246 ms: 1.06x faster                                               |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                               |
| create_gc_cycles         | 1.76 ms                                                      | 1.80 ms: 1.02x slower                                              |
| pickle_dict              | 29.5 us                                                      | 30.4 us: 1.03x slower                                              |
| pickle                   | 9.89 us                                                      | 10.2 us: 1.03x slower                                              |
| unpickle_list            | 4.65 us                                                      | 4.81 us: 1.03x slower                                              |
| unpack_sequence          | 59.9 ns                                                      | 62.5 ns: 1.04x slower                                              |
| pickle_list              | 4.12 us                                                      | 4.31 us: 1.05x slower                                              |
| flaskblogging            | 4.39 ms                                                      | 4.61 ms: 1.05x slower                                              |
| mypy2                    | 933 ms                                                       | 1.05 sec: 1.13x slower                                             |
| regex_effbot             | 3.09 ms                                                      | 3.55 ms: 1.15x slower                                              |
| python_startup           | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                              |
| telco                    | 7.23 ms                                                      | 8.52 ms: 1.18x slower                                              |
| unpickle                 | 13.5 us                                                      | 16.0 us: 1.18x slower                                              |
| gc_traversal             | 3.42 ms                                                      | 4.10 ms: 1.20x slower                                              |
| python_startup_no_site   | 7.33 ms                                                      | 8.94 ms: 1.22x slower                                              |
| coverage                 | 63.3 ms                                                      | 84.3 ms: 1.33x slower                                              |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                       |
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241001-3.13.0rc3-fae84c7/bm-20241001-pythonperf2-x86_64-python-v3.13.0rc3-3.13.0rc3-fae84c7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.292x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.12x