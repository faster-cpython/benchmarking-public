
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: windows-amd64
- commit hash: 0e5eee0
- commit date: 2023-08-20
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230820-pythonperf1-amd64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 212 ms: 1.01x slower                                         |
| tornado_http   | 91.8 ms                                                     | 87.4 ms: 1.05x faster                                        |
| Geometric mean | (ref)                                                       | 1.01x faster                                                 |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230820-pythonperf1-amd64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 54.6 ms                                                     | 53.3 ms: 1.03x faster                                        |
| pidigits       | 148 ms                                                      | 147 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                       | 1.01x faster                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230820-pythonperf1-amd64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 86.7 ms: 1.04x faster                                        |
| regex_v8       | 13.8 ms                                                     | 13.3 ms: 1.04x faster                                        |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                         |
| regex_effbot   | 1.50 ms                                                     | 1.58 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                       | 1.00x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230820-pythonperf1-amd64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.65 ms: 1.34x faster                                        |
| unpickle_pure_python | 152 us                                                      | 134 us: 1.14x faster                                         |
| xml_etree_parse      | 95.9 ms                                                     | 89.8 ms: 1.07x faster                                        |
| tomli_loads          | 1.41 sec                                                    | 1.36 sec: 1.04x faster                                       |
| pickle_pure_python   | 200 us                                                      | 193 us: 1.04x faster                                         |
| pickle_dict          | 18.5 us                                                     | 18.2 us: 1.02x faster                                        |
| xml_etree_process    | 37.1 ms                                                     | 37.8 ms: 1.02x slower                                        |
| unpickle             | 8.09 us                                                     | 8.37 us: 1.03x slower                                        |
| json_loads           | 12.9 us                                                     | 13.5 us: 1.05x slower                                        |
| xml_etree_generate   | 52.2 ms                                                     | 55.1 ms: 1.06x slower                                        |
| pickle_list          | 2.68 us                                                     | 2.86 us: 1.07x slower                                        |
| unpickle_list        | 2.55 us                                                     | 2.78 us: 1.09x slower                                        |
| pickle               | 6.61 us                                                     | 7.27 us: 1.10x slower                                        |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230820-pythonperf1-amd64-python-3.12-3.12.0rc1+-0e5eee0 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 18.7 ms                                                     | 19.5 ms: 1.04x slower                                        |
| python_startup_no_site | 15.9 ms                                                     | 16.7 ms: 1.05x slower                                        |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230820-pythonperf1-amd64-python-3.12-3.12.0rc1+-0e5eee0 |
|-----------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 6.80 ms: 1.07x faster                                        |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230820-pythonperf1-amd64-python-3.12-3.12.0rc1+-0e5eee0 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 98.4 us: 3.27x faster                                        |
| generators               | 33.8 ms                                                     | 21.9 ms: 1.54x faster                                        |
| asyncio_tcp              | 699 ms                                                      | 473 ms: 1.48x faster                                         |
| json_dumps               | 7.56 ms                                                     | 5.65 ms: 1.34x faster                                        |
| richards_super           | 37.5 ms                                                     | 29.8 ms: 1.26x faster                                        |
| deltablue                | 2.61 ms                                                     | 2.11 ms: 1.24x faster                                        |
| mdp                      | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                       |
| unpack_sequence          | 46.1 ns                                                     | 38.5 ns: 1.20x faster                                        |
| sqlglot_parse            | 952 us                                                      | 804 us: 1.18x faster                                         |
| logging_silent           | 69.8 ns                                                     | 59.9 ns: 1.17x faster                                        |
| richards                 | 30.6 ms                                                     | 26.2 ms: 1.16x faster                                        |
| sqlglot_transpile        | 1.16 ms                                                     | 1.02 ms: 1.14x faster                                        |
| hexiom                   | 4.55 ms                                                     | 4.01 ms: 1.14x faster                                        |
| unpickle_pure_python     | 152 us                                                      | 134 us: 1.14x faster                                         |
| raytrace                 | 211 ms                                                      | 188 ms: 1.12x faster                                         |
| comprehensions           | 15.9 us                                                     | 14.2 us: 1.12x faster                                        |
| async_tree_none          | 320 ms                                                      | 287 ms: 1.12x faster                                         |
| scimark_lu               | 63.5 ms                                                     | 56.9 ms: 1.12x faster                                        |
| go                       | 97.3 ms                                                     | 87.5 ms: 1.11x faster                                        |
| async_tree_memoization   | 371 ms                                                      | 334 ms: 1.11x faster                                         |
| mypy2                    | 229 ms                                                      | 208 ms: 1.10x faster                                         |
| chaos                    | 47.1 ms                                                     | 43.0 ms: 1.10x faster                                        |
| json                     | 3.25 ms                                                     | 2.97 ms: 1.10x faster                                        |
| coverage                 | 55.9 ms                                                     | 51.1 ms: 1.09x faster                                        |
| async_tree_io            | 779 ms                                                      | 717 ms: 1.09x faster                                         |
| dulwich_log              | 44.5 ms                                                     | 41.1 ms: 1.08x faster                                        |
| nqueens                  | 64.9 ms                                                     | 60.1 ms: 1.08x faster                                        |
| deepcopy_memo            | 25.2 us                                                     | 23.4 us: 1.08x faster                                        |
| mako                     | 7.26 ms                                                     | 6.80 ms: 1.07x faster                                        |
| xml_etree_parse          | 95.9 ms                                                     | 89.8 ms: 1.07x faster                                        |
| logging_simple           | 6.61 us                                                     | 6.20 us: 1.07x faster                                        |
| scimark_monte_carlo      | 44.6 ms                                                     | 42.1 ms: 1.06x faster                                        |
| sqlglot_normalize        | 190 ms                                                      | 180 ms: 1.06x faster                                         |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 476 ms: 1.05x faster                                         |
| deepcopy                 | 246 us                                                      | 234 us: 1.05x faster                                         |
| logging_format           | 7.01 us                                                     | 6.68 us: 1.05x faster                                        |
| tornado_http             | 91.8 ms                                                     | 87.4 ms: 1.05x faster                                        |
| fannkuch                 | 252 ms                                                      | 240 ms: 1.05x faster                                         |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 2.01 sec: 1.05x faster                                       |
| pyflate                  | 304 ms                                                      | 290 ms: 1.05x faster                                         |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.46 ms: 1.05x faster                                        |
| regex_compile            | 90.6 ms                                                     | 86.7 ms: 1.04x faster                                        |
| meteor_contest           | 74.7 ms                                                     | 71.7 ms: 1.04x faster                                        |
| aiohttp                  | 899 us                                                      | 862 us: 1.04x faster                                         |
| tomli_loads              | 1.41 sec                                                    | 1.36 sec: 1.04x faster                                       |
| regex_v8                 | 13.8 ms                                                     | 13.3 ms: 1.04x faster                                        |
| scimark_fft              | 178 ms                                                      | 172 ms: 1.04x faster                                         |
| pickle_pure_python       | 200 us                                                      | 193 us: 1.04x faster                                         |
| sqlglot_optimize         | 34.9 ms                                                     | 33.8 ms: 1.03x faster                                        |
| bench_thread_pool        | 852 us                                                      | 829 us: 1.03x faster                                         |
| pycparser                | 691 ms                                                      | 674 ms: 1.03x faster                                         |
| float                    | 54.6 ms                                                     | 53.3 ms: 1.03x faster                                        |
| spectral_norm            | 67.9 ms                                                     | 66.3 ms: 1.02x faster                                        |
| coroutines               | 14.6 ms                                                     | 14.3 ms: 1.02x faster                                        |
| pprint_pformat           | 1.04 sec                                                    | 1.02 sec: 1.02x faster                                       |
| pprint_safe_repr         | 512 ms                                                      | 500 ms: 1.02x faster                                         |
| pickle_dict              | 18.5 us                                                     | 18.2 us: 1.02x faster                                        |
| crypto_pyaes             | 47.6 ms                                                     | 46.7 ms: 1.02x faster                                        |
| pidigits                 | 148 ms                                                      | 147 ms: 1.01x faster                                         |
| 2to3                     | 209 ms                                                      | 212 ms: 1.01x slower                                         |
| gc_traversal             | 1.46 ms                                                     | 1.48 ms: 1.01x slower                                        |
| xml_etree_process        | 37.1 ms                                                     | 37.8 ms: 1.02x slower                                        |
| deepcopy_reduce          | 2.07 us                                                     | 2.13 us: 1.03x slower                                        |
| telco                    | 3.90 ms                                                     | 4.01 ms: 1.03x slower                                        |
| regex_dna                | 115 ms                                                      | 119 ms: 1.03x slower                                         |
| unpickle                 | 8.09 us                                                     | 8.37 us: 1.03x slower                                        |
| sqlite_synth             | 1.68 us                                                     | 1.74 us: 1.04x slower                                        |
| create_gc_cycles         | 693 us                                                      | 721 us: 1.04x slower                                         |
| python_startup           | 18.7 ms                                                     | 19.5 ms: 1.04x slower                                        |
| json_loads               | 12.9 us                                                     | 13.5 us: 1.05x slower                                        |
| python_startup_no_site   | 15.9 ms                                                     | 16.7 ms: 1.05x slower                                        |
| regex_effbot             | 1.50 ms                                                     | 1.58 ms: 1.06x slower                                        |
| xml_etree_generate       | 52.2 ms                                                     | 55.1 ms: 1.06x slower                                        |
| bench_mp_pool            | 62.5 ms                                                     | 66.1 ms: 1.06x slower                                        |
| scimark_sor              | 75.6 ms                                                     | 80.1 ms: 1.06x slower                                        |
| pickle_list              | 2.68 us                                                     | 2.86 us: 1.07x slower                                        |
| unpickle_list            | 2.55 us                                                     | 2.78 us: 1.09x slower                                        |
| pathlib                  | 71.4 ms                                                     | 77.9 ms: 1.09x slower                                        |
| pickle                   | 6.61 us                                                     | 7.27 us: 1.10x slower                                        |
| async_generators         | 178 ms                                                      | 234 ms: 1.32x slower                                         |
| dask                     | 264 ms                                                      | 362 ms: 1.37x slower                                         |
| Geometric mean           | (ref)                                                       | 1.06x faster                                                 |

Benchmark hidden because not significant (3): xml_etree_iterparse, docutils, nbody
Ignored benchmarks (14) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
