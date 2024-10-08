# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a4
- machine: windows-amd64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 214 ms: 1.15x faster                                            |
| chameleon      | 5.79 ms                                                     | 5.01 ms: 1.16x faster                                           |
| docutils       | 1.92 sec                                                    | 1.55 sec: 1.24x faster                                          |
| html5lib       | 51.0 ms                                                     | 36.9 ms: 1.38x faster                                           |
| tornado_http   | 108 ms                                                      | 84.3 ms: 1.28x faster                                           |
| Geometric mean | (ref)                                                       | 1.24x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 266 ms: 1.64x faster                                            |
| async_tree_memoization  | 526 ms                                                      | 340 ms: 1.55x faster                                            |
| async_tree_io           | 1.11 sec                                                    | 732 ms: 1.51x faster                                            |
| async_tree_cpu_io_mixed | 638 ms                                                      | 453 ms: 1.41x faster                                            |
| Geometric mean          | (ref)                                                       | 1.52x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 51.0 ms: 1.21x faster                                           |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                            |
| nbody          | 71.3 ms                                                     | 73.2 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                       | 1.06x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 77.8 ms: 1.36x faster                                           |
| regex_dna      | 136 ms                                                      | 115 ms: 1.19x faster                                            |
| regex_v8       | 15.4 ms                                                     | 14.4 ms: 1.07x faster                                           |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                           |
| Geometric mean | (ref)                                                       | 1.16x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.58 ms: 1.64x faster                                           |
| pickle_pure_python   | 270 us                                                      | 186 us: 1.45x faster                                            |
| unpickle_pure_python | 183 us                                                      | 129 us: 1.42x faster                                            |
| xml_etree_process    | 44.5 ms                                                     | 37.1 ms: 1.20x faster                                           |
| tomli_loads          | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                          |
| xml_etree_parse      | 96.8 ms                                                     | 92.2 ms: 1.05x faster                                           |
| unpickle             | 9.09 us                                                     | 8.66 us: 1.05x faster                                           |
| json_loads           | 14.0 us                                                     | 13.7 us: 1.02x faster                                           |
| xml_etree_generate   | 55.5 ms                                                     | 54.5 ms: 1.02x faster                                           |
| unpickle_list        | 2.71 us                                                     | 2.68 us: 1.01x faster                                           |
| pickle_dict          | 17.2 us                                                     | 18.4 us: 1.07x slower                                           |
| pickle               | 6.85 us                                                     | 7.32 us: 1.07x slower                                           |
| pickle_list          | 2.75 us                                                     | 2.96 us: 1.08x slower                                           |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                    |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.2 ms: 1.02x faster                                           |
| python_startup_no_site | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                           |
| Geometric mean         | (ref)                                                       | 1.06x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.29 ms: 1.44x faster                                           |
| django_template | 28.9 ms                                                     | 22.5 ms: 1.28x faster                                           |
| genshi_text     | 19.8 ms                                                     | 16.0 ms: 1.24x faster                                           |
| genshi_xml      | 41.0 ms                                                     | 35.1 ms: 1.17x faster                                           |
| Geometric mean  | (ref)                                                       | 1.28x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 71.0 us: 4.74x faster                                           |
| deltablue                | 4.19 ms                                                     | 1.98 ms: 2.11x faster                                           |
| pylint                   | 350 ms                                                      | 207 ms: 1.69x faster                                            |
| raytrace                 | 273 ms                                                      | 165 ms: 1.66x faster                                            |
| logging_silent           | 94.6 ns                                                     | 57.3 ns: 1.65x faster                                           |
| richards_super           | 52.2 ms                                                     | 31.6 ms: 1.65x faster                                           |
| go                       | 139 ms                                                      | 84.4 ms: 1.65x faster                                           |
| json_dumps               | 9.16 ms                                                     | 5.58 ms: 1.64x faster                                           |
| async_tree_none          | 435 ms                                                      | 266 ms: 1.64x faster                                            |
| sqlglot_parse            | 1.22 ms                                                     | 768 us: 1.58x faster                                            |
| chaos                    | 61.7 ms                                                     | 39.5 ms: 1.56x faster                                           |
| scimark_lu               | 85.8 ms                                                     | 55.0 ms: 1.56x faster                                           |
| generators               | 32.4 ms                                                     | 20.8 ms: 1.56x faster                                           |
| async_tree_memoization   | 526 ms                                                      | 340 ms: 1.55x faster                                            |
| comprehensions           | 16.5 us                                                     | 10.8 us: 1.53x faster                                           |
| asyncio_tcp              | 732 ms                                                      | 481 ms: 1.52x faster                                            |
| richards                 | 42.4 ms                                                     | 28.0 ms: 1.51x faster                                           |
| async_tree_io            | 1.11 sec                                                    | 732 ms: 1.51x faster                                            |
| hexiom                   | 5.74 ms                                                     | 3.82 ms: 1.50x faster                                           |
| sqlglot_transpile        | 1.48 ms                                                     | 983 us: 1.50x faster                                            |
| crypto_pyaes             | 62.5 ms                                                     | 42.8 ms: 1.46x faster                                           |
| pickle_pure_python       | 270 us                                                      | 186 us: 1.45x faster                                            |
| mako                     | 9.03 ms                                                     | 6.29 ms: 1.44x faster                                           |
| pyflate                  | 409 ms                                                      | 285 ms: 1.43x faster                                            |
| unpickle_pure_python     | 183 us                                                      | 129 us: 1.42x faster                                            |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 453 ms: 1.41x faster                                            |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.7 ms: 1.41x faster                                           |
| html5lib                 | 51.0 ms                                                     | 36.9 ms: 1.38x faster                                           |
| scimark_sor              | 106 ms                                                      | 77.9 ms: 1.36x faster                                           |
| regex_compile            | 106 ms                                                      | 77.8 ms: 1.36x faster                                           |
| mypy2                    | 555 ms                                                      | 416 ms: 1.33x faster                                            |
| mdp                      | 1.78 sec                                                    | 1.34 sec: 1.33x faster                                          |
| spectral_norm            | 77.3 ms                                                     | 59.0 ms: 1.31x faster                                           |
| django_template          | 28.9 ms                                                     | 22.5 ms: 1.28x faster                                           |
| tornado_http             | 108 ms                                                      | 84.3 ms: 1.28x faster                                           |
| sympy_sum                | 107 ms                                                      | 83.5 ms: 1.28x faster                                           |
| deepcopy_memo            | 28.8 us                                                     | 23.0 us: 1.25x faster                                           |
| sqlite_synth             | 1.91 us                                                     | 1.53 us: 1.25x faster                                           |
| docutils                 | 1.92 sec                                                    | 1.55 sec: 1.24x faster                                          |
| genshi_text              | 19.8 ms                                                     | 16.0 ms: 1.24x faster                                           |
| sympy_integrate          | 15.3 ms                                                     | 12.4 ms: 1.23x faster                                           |
| pycparser                | 930 ms                                                      | 754 ms: 1.23x faster                                            |
| dulwich_log              | 50.5 ms                                                     | 41.3 ms: 1.22x faster                                           |
| sympy_str                | 194 ms                                                      | 160 ms: 1.22x faster                                            |
| float                    | 61.7 ms                                                     | 51.0 ms: 1.21x faster                                           |
| coroutines               | 16.0 ms                                                     | 13.2 ms: 1.21x faster                                           |
| xml_etree_process        | 44.5 ms                                                     | 37.1 ms: 1.20x faster                                           |
| pprint_pformat           | 1.22 sec                                                    | 1.02 sec: 1.19x faster                                          |
| sqlglot_optimize         | 39.8 ms                                                     | 33.4 ms: 1.19x faster                                           |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.77 sec: 1.19x faster                                          |
| regex_dna                | 136 ms                                                      | 115 ms: 1.19x faster                                            |
| pprint_safe_repr         | 592 ms                                                      | 500 ms: 1.18x faster                                            |
| tomli_loads              | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                          |
| genshi_xml               | 41.0 ms                                                     | 35.1 ms: 1.17x faster                                           |
| sqlglot_normalize        | 205 ms                                                      | 176 ms: 1.17x faster                                            |
| bench_thread_pool        | 958 us                                                      | 824 us: 1.16x faster                                            |
| chameleon                | 5.79 ms                                                     | 5.01 ms: 1.16x faster                                           |
| 2to3                     | 246 ms                                                      | 214 ms: 1.15x faster                                            |
| sympy_expand             | 314 ms                                                      | 274 ms: 1.15x faster                                            |
| nqueens                  | 66.6 ms                                                     | 58.2 ms: 1.14x faster                                           |
| aiohttp                  | 995 us                                                      | 885 us: 1.12x faster                                            |
| deepcopy                 | 255 us                                                      | 233 us: 1.10x faster                                            |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.49 ms: 1.09x faster                                           |
| json                     | 3.14 ms                                                     | 2.91 ms: 1.08x faster                                           |
| create_gc_cycles         | 800 us                                                      | 743 us: 1.08x faster                                            |
| deepcopy_reduce          | 2.20 us                                                     | 2.05 us: 1.08x faster                                           |
| regex_v8                 | 15.4 ms                                                     | 14.4 ms: 1.07x faster                                           |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                           |
| meteor_contest           | 75.9 ms                                                     | 72.2 ms: 1.05x faster                                           |
| xml_etree_parse          | 96.8 ms                                                     | 92.2 ms: 1.05x faster                                           |
| unpickle                 | 9.09 us                                                     | 8.66 us: 1.05x faster                                           |
| scimark_fft              | 187 ms                                                      | 179 ms: 1.04x faster                                            |
| logging_format           | 6.76 us                                                     | 6.57 us: 1.03x faster                                           |
| json_loads               | 14.0 us                                                     | 13.7 us: 1.02x faster                                           |
| fannkuch                 | 256 ms                                                      | 250 ms: 1.02x faster                                            |
| python_startup           | 20.6 ms                                                     | 20.2 ms: 1.02x faster                                           |
| xml_etree_generate       | 55.5 ms                                                     | 54.5 ms: 1.02x faster                                           |
| unpickle_list            | 2.71 us                                                     | 2.68 us: 1.01x faster                                           |
| logging_simple           | 6.22 us                                                     | 6.15 us: 1.01x faster                                           |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                            |
| nbody                    | 71.3 ms                                                     | 73.2 ms: 1.03x slower                                           |
| async_generators         | 222 ms                                                      | 230 ms: 1.04x slower                                            |
| gc_traversal             | 1.41 ms                                                     | 1.50 ms: 1.06x slower                                           |
| pathlib                  | 75.7 ms                                                     | 80.8 ms: 1.07x slower                                           |
| pickle_dict              | 17.2 us                                                     | 18.4 us: 1.07x slower                                           |
| pickle                   | 6.85 us                                                     | 7.32 us: 1.07x slower                                           |
| bench_mp_pool            | 62.0 ms                                                     | 66.4 ms: 1.07x slower                                           |
| pickle_list              | 2.75 us                                                     | 2.96 us: 1.08x slower                                           |
| python_startup_no_site   | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                           |
| telco                    | 3.94 ms                                                     | 4.73 ms: 1.20x slower                                           |
| coverage                 | 39.0 ms                                                     | 47.3 ms: 1.21x slower                                           |
| thrift                   | 617 us                                                      | 8.18 ms: 13.25x slower                                          |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                    |

Benchmark hidden because not significant (2): flaskblogging, xml_etree_iterparse
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown