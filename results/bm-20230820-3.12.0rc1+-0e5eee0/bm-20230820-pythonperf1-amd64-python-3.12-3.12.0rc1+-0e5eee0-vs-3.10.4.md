
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: windows-amd64
- commit hash: 0e5eee0
- commit date: 2023-08-20
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-pythonperf1-amd64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 212 ms: 1.12x faster                                         |
| docutils       | 1.89 sec                                                    | 1.60 sec: 1.18x faster                                       |
| tornado_http   | 109 ms                                                      | 87.4 ms: 1.25x faster                                        |
| Geometric mean | (ref)                                                       | 1.18x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-pythonperf1-amd64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 53.3 ms: 1.13x faster                                        |
| pidigits       | 145 ms                                                      | 147 ms: 1.01x slower                                         |
| nbody          | 69.3 ms                                                     | 70.2 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                       | 1.03x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-pythonperf1-amd64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 86.7 ms: 1.19x faster                                        |
| regex_v8       | 15.0 ms                                                     | 13.3 ms: 1.13x faster                                        |
| regex_dna      | 132 ms                                                      | 119 ms: 1.11x faster                                         |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                        |
| Geometric mean | (ref)                                                       | 1.12x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-pythonperf1-amd64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.65 ms: 1.51x faster                                        |
| pickle_pure_python   | 257 us                                                      | 193 us: 1.33x faster                                         |
| unpickle_pure_python | 171 us                                                      | 134 us: 1.28x faster                                         |
| tomli_loads          | 1.62 sec                                                    | 1.36 sec: 1.20x faster                                       |
| xml_etree_process    | 43.4 ms                                                     | 37.8 ms: 1.15x faster                                        |
| xml_etree_parse      | 102 ms                                                      | 89.8 ms: 1.13x faster                                        |
| unpickle             | 9.17 us                                                     | 8.37 us: 1.10x faster                                        |
| json_loads           | 14.2 us                                                     | 13.5 us: 1.05x faster                                        |
| xml_etree_iterparse  | 63.5 ms                                                     | 62.5 ms: 1.02x faster                                        |
| xml_etree_generate   | 54.5 ms                                                     | 55.1 ms: 1.01x slower                                        |
| pickle               | 6.80 us                                                     | 7.27 us: 1.07x slower                                        |
| pickle_dict          | 16.9 us                                                     | 18.2 us: 1.07x slower                                        |
| pickle_list          | 2.59 us                                                     | 2.86 us: 1.11x slower                                        |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-pythonperf1-amd64-python-3.12-3.12.0rc1+-0e5eee0 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.5 ms: 1.03x faster                                        |
| python_startup_no_site | 15.5 ms                                                     | 16.7 ms: 1.08x slower                                        |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-pythonperf1-amd64-python-3.12-3.12.0rc1+-0e5eee0 |
|-----------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 6.80 ms: 1.29x faster                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-pythonperf1-amd64-python-3.12-3.12.0rc1+-0e5eee0 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 98.4 us: 3.30x faster                                        |
| deltablue                | 4.17 ms                                                     | 2.11 ms: 1.98x faster                                        |
| richards_super           | 51.7 ms                                                     | 29.8 ms: 1.74x faster                                        |
| mypy2                    | 352 ms                                                      | 208 ms: 1.69x faster                                         |
| logging_silent           | 96.4 ns                                                     | 59.9 ns: 1.61x faster                                        |
| richards                 | 41.2 ms                                                     | 26.2 ms: 1.57x faster                                        |
| go                       | 136 ms                                                      | 87.5 ms: 1.56x faster                                        |
| sqlglot_parse            | 1.22 ms                                                     | 804 us: 1.52x faster                                         |
| asyncio_tcp              | 712 ms                                                      | 473 ms: 1.51x faster                                         |
| json_dumps               | 8.50 ms                                                     | 5.65 ms: 1.51x faster                                        |
| scimark_lu               | 85.4 ms                                                     | 56.9 ms: 1.50x faster                                        |
| async_tree_memoization   | 497 ms                                                      | 334 ms: 1.49x faster                                         |
| async_tree_io            | 1.07 sec                                                    | 717 ms: 1.49x faster                                         |
| async_tree_none          | 420 ms                                                      | 287 ms: 1.47x faster                                         |
| generators               | 31.6 ms                                                     | 21.9 ms: 1.44x faster                                        |
| raytrace                 | 271 ms                                                      | 188 ms: 1.44x faster                                         |
| sqlglot_transpile        | 1.46 ms                                                     | 1.02 ms: 1.44x faster                                        |
| hexiom                   | 5.52 ms                                                     | 4.01 ms: 1.38x faster                                        |
| chaos                    | 58.9 ms                                                     | 43.0 ms: 1.37x faster                                        |
| pyflate                  | 387 ms                                                      | 290 ms: 1.33x faster                                         |
| crypto_pyaes             | 62.3 ms                                                     | 46.7 ms: 1.33x faster                                        |
| pickle_pure_python       | 257 us                                                      | 193 us: 1.33x faster                                         |
| scimark_monte_carlo      | 55.9 ms                                                     | 42.1 ms: 1.33x faster                                        |
| scimark_sor              | 105 ms                                                      | 80.1 ms: 1.31x faster                                        |
| mako                     | 8.80 ms                                                     | 6.80 ms: 1.29x faster                                        |
| pycparser                | 868 ms                                                      | 674 ms: 1.29x faster                                         |
| unpickle_pure_python     | 171 us                                                      | 134 us: 1.28x faster                                         |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 476 ms: 1.28x faster                                         |
| tornado_http             | 109 ms                                                      | 87.4 ms: 1.25x faster                                        |
| mdp                      | 1.71 sec                                                    | 1.39 sec: 1.23x faster                                       |
| deepcopy_memo            | 28.5 us                                                     | 23.4 us: 1.22x faster                                        |
| tomli_loads              | 1.62 sec                                                    | 1.36 sec: 1.20x faster                                       |
| regex_compile            | 103 ms                                                      | 86.7 ms: 1.19x faster                                        |
| pprint_pformat           | 1.21 sec                                                    | 1.02 sec: 1.19x faster                                       |
| docutils                 | 1.89 sec                                                    | 1.60 sec: 1.18x faster                                       |
| pprint_safe_repr         | 589 ms                                                      | 500 ms: 1.18x faster                                         |
| spectral_norm            | 78.0 ms                                                     | 66.3 ms: 1.18x faster                                        |
| aiohttp                  | 1.01 ms                                                     | 862 us: 1.17x faster                                         |
| dulwich_log              | 47.6 ms                                                     | 41.1 ms: 1.16x faster                                        |
| sqlglot_optimize         | 39.0 ms                                                     | 33.8 ms: 1.15x faster                                        |
| xml_etree_process        | 43.4 ms                                                     | 37.8 ms: 1.15x faster                                        |
| bench_thread_pool        | 946 us                                                      | 829 us: 1.14x faster                                         |
| xml_etree_parse          | 102 ms                                                      | 89.8 ms: 1.13x faster                                        |
| float                    | 60.2 ms                                                     | 53.3 ms: 1.13x faster                                        |
| regex_v8                 | 15.0 ms                                                     | 13.3 ms: 1.13x faster                                        |
| sqlglot_normalize        | 202 ms                                                      | 180 ms: 1.12x faster                                         |
| scimark_fft              | 193 ms                                                      | 172 ms: 1.12x faster                                         |
| comprehensions           | 16.0 us                                                     | 14.2 us: 1.12x faster                                        |
| 2to3                     | 237 ms                                                      | 212 ms: 1.12x faster                                         |
| coroutines               | 15.9 ms                                                     | 14.3 ms: 1.11x faster                                        |
| nqueens                  | 67.0 ms                                                     | 60.1 ms: 1.11x faster                                        |
| regex_dna                | 132 ms                                                      | 119 ms: 1.11x faster                                         |
| unpickle                 | 9.17 us                                                     | 8.37 us: 1.10x faster                                        |
| deepcopy                 | 255 us                                                      | 234 us: 1.09x faster                                         |
| create_gc_cycles         | 782 us                                                      | 721 us: 1.08x faster                                         |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.46 ms: 1.08x faster                                        |
| fannkuch                 | 258 ms                                                      | 240 ms: 1.07x faster                                         |
| sqlite_synth             | 1.84 us                                                     | 1.74 us: 1.05x faster                                        |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                        |
| json_loads               | 14.2 us                                                     | 13.5 us: 1.05x faster                                        |
| python_startup           | 20.0 ms                                                     | 19.5 ms: 1.03x faster                                        |
| json                     | 3.05 ms                                                     | 2.97 ms: 1.03x faster                                        |
| xml_etree_iterparse      | 63.5 ms                                                     | 62.5 ms: 1.02x faster                                        |
| deepcopy_reduce          | 2.16 us                                                     | 2.13 us: 1.01x faster                                        |
| meteor_contest           | 72.5 ms                                                     | 71.7 ms: 1.01x faster                                        |
| xml_etree_generate       | 54.5 ms                                                     | 55.1 ms: 1.01x slower                                        |
| pidigits                 | 145 ms                                                      | 147 ms: 1.01x slower                                         |
| nbody                    | 69.3 ms                                                     | 70.2 ms: 1.01x slower                                        |
| unpack_sequence          | 37.8 ns                                                     | 38.5 ns: 1.02x slower                                        |
| async_generators         | 224 ms                                                      | 234 ms: 1.05x slower                                         |
| telco                    | 3.78 ms                                                     | 4.01 ms: 1.06x slower                                        |
| pickle                   | 6.80 us                                                     | 7.27 us: 1.07x slower                                        |
| pickle_dict              | 16.9 us                                                     | 18.2 us: 1.07x slower                                        |
| python_startup_no_site   | 15.5 ms                                                     | 16.7 ms: 1.08x slower                                        |
| bench_mp_pool            | 60.7 ms                                                     | 66.1 ms: 1.09x slower                                        |
| gc_traversal             | 1.34 ms                                                     | 1.48 ms: 1.10x slower                                        |
| pickle_list              | 2.59 us                                                     | 2.86 us: 1.11x slower                                        |
| dask                     | 305 ms                                                      | 362 ms: 1.19x slower                                         |
| coverage                 | 40.0 ms                                                     | 51.1 ms: 1.28x slower                                        |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                 |

Benchmark hidden because not significant (5): unpickle_list, asyncio_tcp_ssl, logging_simple, logging_format, pathlib
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.12x
