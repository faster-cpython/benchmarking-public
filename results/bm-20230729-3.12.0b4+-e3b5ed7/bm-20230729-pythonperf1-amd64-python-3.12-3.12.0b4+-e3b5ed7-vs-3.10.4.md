
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: windows-amd64
- commit hash: e3b5ed7
- commit date: 2023-07-29
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf1-amd64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 215 ms: 1.10x faster                                        |
| docutils       | 1.89 sec                                                    | 1.66 sec: 1.14x faster                                      |
| tornado_http   | 109 ms                                                      | 87.8 ms: 1.24x faster                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf1-amd64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 53.6 ms: 1.12x faster                                       |
| nbody          | 69.3 ms                                                     | 66.6 ms: 1.04x faster                                       |
| pidigits       | 145 ms                                                      | 153 ms: 1.05x slower                                        |
| Geometric mean | (ref)                                                       | 1.04x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf1-amd64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 88.2 ms: 1.17x faster                                       |
| regex_v8       | 15.0 ms                                                     | 13.9 ms: 1.08x faster                                       |
| regex_dna      | 132 ms                                                      | 123 ms: 1.07x faster                                        |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf1-amd64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.76 ms: 1.48x faster                                       |
| pickle_pure_python   | 257 us                                                      | 195 us: 1.31x faster                                        |
| unpickle_pure_python | 171 us                                                      | 134 us: 1.27x faster                                        |
| tomli_loads          | 1.62 sec                                                    | 1.37 sec: 1.18x faster                                      |
| xml_etree_process    | 43.4 ms                                                     | 38.6 ms: 1.13x faster                                       |
| xml_etree_parse      | 102 ms                                                      | 93.7 ms: 1.09x faster                                       |
| unpickle             | 9.17 us                                                     | 8.48 us: 1.08x faster                                       |
| json_loads           | 14.2 us                                                     | 13.8 us: 1.03x faster                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 64.5 ms: 1.01x slower                                       |
| xml_etree_generate   | 54.5 ms                                                     | 56.5 ms: 1.04x slower                                       |
| pickle               | 6.80 us                                                     | 7.13 us: 1.05x slower                                       |
| pickle_list          | 2.59 us                                                     | 2.83 us: 1.09x slower                                       |
| pickle_dict          | 16.9 us                                                     | 18.8 us: 1.11x slower                                       |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf1-amd64-python-3.12-3.12.0b4+-e3b5ed7 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.9 ms: 1.05x faster                                       |
| python_startup_no_site | 15.5 ms                                                     | 16.1 ms: 1.03x slower                                       |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf1-amd64-python-3.12-3.12.0b4+-e3b5ed7 |
|-----------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 6.90 ms: 1.28x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-pythonperf1-amd64-python-3.12-3.12.0b4+-e3b5ed7 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 95.3 us: 3.41x faster                                       |
| deltablue                | 4.17 ms                                                     | 2.13 ms: 1.95x faster                                       |
| richards_super           | 51.7 ms                                                     | 29.2 ms: 1.77x faster                                       |
| mypy2                    | 352 ms                                                      | 214 ms: 1.65x faster                                        |
| richards                 | 41.2 ms                                                     | 25.7 ms: 1.60x faster                                       |
| go                       | 136 ms                                                      | 85.3 ms: 1.60x faster                                       |
| logging_silent           | 96.4 ns                                                     | 60.8 ns: 1.58x faster                                       |
| sqlglot_parse            | 1.22 ms                                                     | 798 us: 1.53x faster                                        |
| scimark_lu               | 85.4 ms                                                     | 56.7 ms: 1.51x faster                                       |
| json_dumps               | 8.50 ms                                                     | 5.76 ms: 1.48x faster                                       |
| asyncio_tcp              | 712 ms                                                      | 488 ms: 1.46x faster                                        |
| async_tree_io            | 1.07 sec                                                    | 734 ms: 1.45x faster                                        |
| async_tree_memoization   | 497 ms                                                      | 345 ms: 1.44x faster                                        |
| raytrace                 | 271 ms                                                      | 188 ms: 1.44x faster                                        |
| sqlglot_transpile        | 1.46 ms                                                     | 1.02 ms: 1.43x faster                                       |
| async_tree_none          | 420 ms                                                      | 296 ms: 1.42x faster                                        |
| generators               | 31.6 ms                                                     | 22.4 ms: 1.41x faster                                       |
| hexiom                   | 5.52 ms                                                     | 4.02 ms: 1.37x faster                                       |
| chaos                    | 58.9 ms                                                     | 43.0 ms: 1.37x faster                                       |
| scimark_sor              | 105 ms                                                      | 78.3 ms: 1.34x faster                                       |
| scimark_monte_carlo      | 55.9 ms                                                     | 42.4 ms: 1.32x faster                                       |
| pickle_pure_python       | 257 us                                                      | 195 us: 1.31x faster                                        |
| pyflate                  | 387 ms                                                      | 297 ms: 1.30x faster                                        |
| crypto_pyaes             | 62.3 ms                                                     | 48.2 ms: 1.29x faster                                       |
| mako                     | 8.80 ms                                                     | 6.90 ms: 1.28x faster                                       |
| unpickle_pure_python     | 171 us                                                      | 134 us: 1.27x faster                                        |
| pycparser                | 868 ms                                                      | 686 ms: 1.26x faster                                        |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 484 ms: 1.26x faster                                        |
| tornado_http             | 109 ms                                                      | 87.8 ms: 1.24x faster                                       |
| spectral_norm            | 78.0 ms                                                     | 64.2 ms: 1.22x faster                                       |
| deepcopy_memo            | 28.5 us                                                     | 23.6 us: 1.21x faster                                       |
| tomli_loads              | 1.62 sec                                                    | 1.37 sec: 1.18x faster                                      |
| regex_compile            | 103 ms                                                      | 88.2 ms: 1.17x faster                                       |
| mdp                      | 1.71 sec                                                    | 1.48 sec: 1.16x faster                                      |
| aiohttp                  | 1.01 ms                                                     | 874 us: 1.15x faster                                        |
| pprint_pformat           | 1.21 sec                                                    | 1.05 sec: 1.15x faster                                      |
| pprint_safe_repr         | 589 ms                                                      | 513 ms: 1.15x faster                                        |
| bench_thread_pool        | 946 us                                                      | 828 us: 1.14x faster                                        |
| docutils                 | 1.89 sec                                                    | 1.66 sec: 1.14x faster                                      |
| comprehensions           | 16.0 us                                                     | 14.0 us: 1.14x faster                                       |
| sqlglot_optimize         | 39.0 ms                                                     | 34.4 ms: 1.13x faster                                       |
| xml_etree_process        | 43.4 ms                                                     | 38.6 ms: 1.13x faster                                       |
| float                    | 60.2 ms                                                     | 53.6 ms: 1.12x faster                                       |
| coroutines               | 15.9 ms                                                     | 14.2 ms: 1.12x faster                                       |
| nqueens                  | 67.0 ms                                                     | 60.5 ms: 1.11x faster                                       |
| 2to3                     | 237 ms                                                      | 215 ms: 1.10x faster                                        |
| sqlglot_normalize        | 202 ms                                                      | 184 ms: 1.10x faster                                        |
| xml_etree_parse          | 102 ms                                                      | 93.7 ms: 1.09x faster                                       |
| regex_v8                 | 15.0 ms                                                     | 13.9 ms: 1.08x faster                                       |
| dulwich_log              | 47.6 ms                                                     | 44.0 ms: 1.08x faster                                       |
| unpickle                 | 9.17 us                                                     | 8.48 us: 1.08x faster                                       |
| deepcopy                 | 255 us                                                      | 237 us: 1.08x faster                                        |
| scimark_fft              | 193 ms                                                      | 180 ms: 1.08x faster                                        |
| regex_dna                | 132 ms                                                      | 123 ms: 1.07x faster                                        |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.49 ms: 1.07x faster                                       |
| python_startup           | 20.0 ms                                                     | 18.9 ms: 1.05x faster                                       |
| create_gc_cycles         | 782 us                                                      | 748 us: 1.04x faster                                        |
| fannkuch                 | 258 ms                                                      | 247 ms: 1.04x faster                                        |
| sqlite_synth             | 1.84 us                                                     | 1.76 us: 1.04x faster                                       |
| nbody                    | 69.3 ms                                                     | 66.6 ms: 1.04x faster                                       |
| deepcopy_reduce          | 2.16 us                                                     | 2.08 us: 1.04x faster                                       |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                       |
| json_loads               | 14.2 us                                                     | 13.8 us: 1.03x faster                                       |
| json                     | 3.05 ms                                                     | 2.99 ms: 1.02x faster                                       |
| meteor_contest           | 72.5 ms                                                     | 73.4 ms: 1.01x slower                                       |
| xml_etree_iterparse      | 63.5 ms                                                     | 64.5 ms: 1.01x slower                                       |
| python_startup_no_site   | 15.5 ms                                                     | 16.1 ms: 1.03x slower                                       |
| xml_etree_generate       | 54.5 ms                                                     | 56.5 ms: 1.04x slower                                       |
| pickle                   | 6.80 us                                                     | 7.13 us: 1.05x slower                                       |
| logging_simple           | 6.20 us                                                     | 6.50 us: 1.05x slower                                       |
| pidigits                 | 145 ms                                                      | 153 ms: 1.05x slower                                        |
| async_generators         | 224 ms                                                      | 235 ms: 1.05x slower                                        |
| logging_format           | 6.66 us                                                     | 7.07 us: 1.06x slower                                       |
| telco                    | 3.78 ms                                                     | 4.02 ms: 1.06x slower                                       |
| pathlib                  | 77.4 ms                                                     | 82.9 ms: 1.07x slower                                       |
| pickle_list              | 2.59 us                                                     | 2.83 us: 1.09x slower                                       |
| pickle_dict              | 16.9 us                                                     | 18.8 us: 1.11x slower                                       |
| bench_mp_pool            | 60.7 ms                                                     | 67.8 ms: 1.12x slower                                       |
| gc_traversal             | 1.34 ms                                                     | 1.54 ms: 1.14x slower                                       |
| dask                     | 305 ms                                                      | 365 ms: 1.20x slower                                        |
| coverage                 | 40.0 ms                                                     | 52.1 ms: 1.30x slower                                       |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, unpickle_list, unpack_sequence
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x
