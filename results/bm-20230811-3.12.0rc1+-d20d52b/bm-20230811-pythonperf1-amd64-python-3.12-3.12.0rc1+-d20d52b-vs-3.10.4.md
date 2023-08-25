
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: windows-amd64
- commit hash: d20d52b
- commit date: 2023-08-11
- overall geometric mean: 1.16x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-pythonperf1-amd64-python-3.12-3.12.0rc1+-d20d52b |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 214 ms: 1.11x faster                                         |
| docutils       | 1.89 sec                                                    | 1.61 sec: 1.17x faster                                       |
| tornado_http   | 109 ms                                                      | 87.3 ms: 1.25x faster                                        |
| Geometric mean | (ref)                                                       | 1.18x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-pythonperf1-amd64-python-3.12-3.12.0rc1+-d20d52b |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 54.2 ms: 1.11x faster                                        |
| pidigits       | 145 ms                                                      | 147 ms: 1.01x slower                                         |
| nbody          | 69.3 ms                                                     | 71.8 ms: 1.04x slower                                        |
| Geometric mean | (ref)                                                       | 1.02x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-pythonperf1-amd64-python-3.12-3.12.0rc1+-d20d52b |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 89.7 ms: 1.15x faster                                        |
| regex_v8       | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                        |
| regex_dna      | 132 ms                                                      | 121 ms: 1.09x faster                                         |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                        |
| Geometric mean | (ref)                                                       | 1.09x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-pythonperf1-amd64-python-3.12-3.12.0rc1+-d20d52b |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.86 ms: 1.45x faster                                        |
| pickle_pure_python   | 257 us                                                      | 202 us: 1.27x faster                                         |
| unpickle_pure_python | 171 us                                                      | 139 us: 1.23x faster                                         |
| tomli_loads          | 1.62 sec                                                    | 1.42 sec: 1.14x faster                                       |
| xml_etree_parse      | 102 ms                                                      | 90.4 ms: 1.13x faster                                        |
| unpickle             | 9.17 us                                                     | 8.18 us: 1.12x faster                                        |
| xml_etree_process    | 43.4 ms                                                     | 39.1 ms: 1.11x faster                                        |
| json_loads           | 14.2 us                                                     | 13.6 us: 1.04x faster                                        |
| xml_etree_iterparse  | 63.5 ms                                                     | 64.3 ms: 1.01x slower                                        |
| xml_etree_generate   | 54.5 ms                                                     | 56.7 ms: 1.04x slower                                        |
| pickle               | 6.80 us                                                     | 7.25 us: 1.07x slower                                        |
| pickle_dict          | 16.9 us                                                     | 18.1 us: 1.07x slower                                        |
| pickle_list          | 2.59 us                                                     | 2.86 us: 1.11x slower                                        |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-pythonperf1-amd64-python-3.12-3.12.0rc1+-d20d52b |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.6 ms: 1.02x faster                                        |
| python_startup_no_site | 15.5 ms                                                     | 16.6 ms: 1.07x slower                                        |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-pythonperf1-amd64-python-3.12-3.12.0rc1+-d20d52b |
|-----------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 6.94 ms: 1.27x faster                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-pythonperf1-amd64-python-3.12-3.12.0rc1+-d20d52b |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 95.1 us: 3.41x faster                                        |
| deltablue                | 4.17 ms                                                     | 2.18 ms: 1.92x faster                                        |
| richards_super           | 51.7 ms                                                     | 30.0 ms: 1.73x faster                                        |
| mypy2                    | 352 ms                                                      | 209 ms: 1.68x faster                                         |
| logging_silent           | 96.4 ns                                                     | 60.7 ns: 1.59x faster                                        |
| richards                 | 41.2 ms                                                     | 26.5 ms: 1.56x faster                                        |
| go                       | 136 ms                                                      | 89.0 ms: 1.53x faster                                        |
| asyncio_tcp              | 712 ms                                                      | 472 ms: 1.51x faster                                         |
| async_tree_io            | 1.07 sec                                                    | 720 ms: 1.48x faster                                         |
| sqlglot_parse            | 1.22 ms                                                     | 825 us: 1.48x faster                                         |
| async_tree_memoization   | 497 ms                                                      | 337 ms: 1.48x faster                                         |
| json_dumps               | 8.50 ms                                                     | 5.86 ms: 1.45x faster                                        |
| async_tree_none          | 420 ms                                                      | 290 ms: 1.45x faster                                         |
| scimark_lu               | 85.4 ms                                                     | 59.9 ms: 1.43x faster                                        |
| sqlglot_transpile        | 1.46 ms                                                     | 1.04 ms: 1.40x faster                                        |
| raytrace                 | 271 ms                                                      | 193 ms: 1.40x faster                                         |
| generators               | 31.6 ms                                                     | 23.0 ms: 1.37x faster                                        |
| chaos                    | 58.9 ms                                                     | 44.2 ms: 1.33x faster                                        |
| hexiom                   | 5.52 ms                                                     | 4.21 ms: 1.31x faster                                        |
| crypto_pyaes             | 62.3 ms                                                     | 47.7 ms: 1.31x faster                                        |
| pyflate                  | 387 ms                                                      | 299 ms: 1.29x faster                                         |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 477 ms: 1.28x faster                                         |
| scimark_monte_carlo      | 55.9 ms                                                     | 43.9 ms: 1.27x faster                                        |
| pickle_pure_python       | 257 us                                                      | 202 us: 1.27x faster                                         |
| mako                     | 8.80 ms                                                     | 6.94 ms: 1.27x faster                                        |
| pycparser                | 868 ms                                                      | 688 ms: 1.26x faster                                         |
| scimark_sor              | 105 ms                                                      | 83.7 ms: 1.25x faster                                        |
| tornado_http             | 109 ms                                                      | 87.3 ms: 1.25x faster                                        |
| unpickle_pure_python     | 171 us                                                      | 139 us: 1.23x faster                                         |
| aiohttp                  | 1.01 ms                                                     | 856 us: 1.18x faster                                         |
| spectral_norm            | 78.0 ms                                                     | 66.4 ms: 1.18x faster                                        |
| docutils                 | 1.89 sec                                                    | 1.61 sec: 1.17x faster                                       |
| mdp                      | 1.71 sec                                                    | 1.47 sec: 1.17x faster                                       |
| dulwich_log              | 47.6 ms                                                     | 41.3 ms: 1.15x faster                                        |
| regex_compile            | 103 ms                                                      | 89.7 ms: 1.15x faster                                        |
| tomli_loads              | 1.62 sec                                                    | 1.42 sec: 1.14x faster                                       |
| sqlglot_optimize         | 39.0 ms                                                     | 34.5 ms: 1.13x faster                                        |
| xml_etree_parse          | 102 ms                                                      | 90.4 ms: 1.13x faster                                        |
| pprint_pformat           | 1.21 sec                                                    | 1.07 sec: 1.12x faster                                       |
| coroutines               | 15.9 ms                                                     | 14.2 ms: 1.12x faster                                        |
| deepcopy_memo            | 28.5 us                                                     | 25.5 us: 1.12x faster                                        |
| unpickle                 | 9.17 us                                                     | 8.18 us: 1.12x faster                                        |
| bench_thread_pool        | 946 us                                                      | 844 us: 1.12x faster                                         |
| pprint_safe_repr         | 589 ms                                                      | 530 ms: 1.11x faster                                         |
| float                    | 60.2 ms                                                     | 54.2 ms: 1.11x faster                                        |
| xml_etree_process        | 43.4 ms                                                     | 39.1 ms: 1.11x faster                                        |
| 2to3                     | 237 ms                                                      | 214 ms: 1.11x faster                                         |
| regex_v8                 | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                        |
| comprehensions           | 16.0 us                                                     | 14.7 us: 1.09x faster                                        |
| regex_dna                | 132 ms                                                      | 121 ms: 1.09x faster                                         |
| create_gc_cycles         | 782 us                                                      | 719 us: 1.09x faster                                         |
| sqlglot_normalize        | 202 ms                                                      | 187 ms: 1.08x faster                                         |
| nqueens                  | 67.0 ms                                                     | 62.1 ms: 1.08x faster                                        |
| fannkuch                 | 258 ms                                                      | 244 ms: 1.06x faster                                         |
| scimark_fft              | 193 ms                                                      | 184 ms: 1.05x faster                                         |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.53 ms: 1.05x faster                                        |
| deepcopy                 | 255 us                                                      | 244 us: 1.05x faster                                         |
| sqlite_synth             | 1.84 us                                                     | 1.76 us: 1.05x faster                                        |
| json_loads               | 14.2 us                                                     | 13.6 us: 1.04x faster                                        |
| asyncio_tcp_ssl          | 2.03 sec                                                    | 1.96 sec: 1.04x faster                                       |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                        |
| json                     | 3.05 ms                                                     | 2.95 ms: 1.03x faster                                        |
| python_startup           | 20.0 ms                                                     | 19.6 ms: 1.02x faster                                        |
| pathlib                  | 77.4 ms                                                     | 78.1 ms: 1.01x slower                                        |
| unpack_sequence          | 37.8 ns                                                     | 38.2 ns: 1.01x slower                                        |
| deepcopy_reduce          | 2.16 us                                                     | 2.18 us: 1.01x slower                                        |
| meteor_contest           | 72.5 ms                                                     | 73.4 ms: 1.01x slower                                        |
| xml_etree_iterparse      | 63.5 ms                                                     | 64.3 ms: 1.01x slower                                        |
| pidigits                 | 145 ms                                                      | 147 ms: 1.01x slower                                         |
| nbody                    | 69.3 ms                                                     | 71.8 ms: 1.04x slower                                        |
| xml_etree_generate       | 54.5 ms                                                     | 56.7 ms: 1.04x slower                                        |
| async_generators         | 224 ms                                                      | 233 ms: 1.04x slower                                         |
| logging_format           | 6.66 us                                                     | 7.02 us: 1.05x slower                                        |
| logging_simple           | 6.20 us                                                     | 6.56 us: 1.06x slower                                        |
| pickle                   | 6.80 us                                                     | 7.25 us: 1.07x slower                                        |
| python_startup_no_site   | 15.5 ms                                                     | 16.6 ms: 1.07x slower                                        |
| pickle_dict              | 16.9 us                                                     | 18.1 us: 1.07x slower                                        |
| telco                    | 3.78 ms                                                     | 4.11 ms: 1.09x slower                                        |
| bench_mp_pool            | 60.7 ms                                                     | 66.5 ms: 1.10x slower                                        |
| pickle_list              | 2.59 us                                                     | 2.86 us: 1.11x slower                                        |
| gc_traversal             | 1.34 ms                                                     | 1.51 ms: 1.12x slower                                        |
| dask                     | 305 ms                                                      | 367 ms: 1.20x slower                                         |
| coverage                 | 40.0 ms                                                     | 51.0 ms: 1.27x slower                                        |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                 |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x
