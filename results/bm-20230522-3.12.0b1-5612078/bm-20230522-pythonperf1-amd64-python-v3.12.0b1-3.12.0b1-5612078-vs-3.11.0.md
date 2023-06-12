
# Results vs. 3.11.0

- fork: python
- ref: v3.12.0b1
- machine: windows-amd64
- commit hash: 5612078
- commit date: 2023-05-22
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 218 ms: 1.04x slower                                            |
| docutils       | 1.60 sec                                                    | 1.66 sec: 1.04x slower                                          |
| tornado_http   | 91.8 ms                                                     | 99.2 ms: 1.08x slower                                           |
| Geometric mean | (ref)                                                       | 1.05x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 69.0 ms: 1.01x faster                                           |
| float          | 54.6 ms                                                     | 55.5 ms: 1.02x slower                                           |
| pidigits       | 148 ms                                                      | 153 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                       | 1.01x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 13.8 ms                                                     | 13.3 ms: 1.04x faster                                           |
| regex_compile  | 90.6 ms                                                     | 88.7 ms: 1.02x faster                                           |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                            |
| regex_effbot   | 1.50 ms                                                     | 1.59 ms: 1.06x slower                                           |
| Geometric mean | (ref)                                                       | 1.01x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.67 ms: 1.33x faster                                           |
| unpickle_pure_python | 152 us                                                      | 134 us: 1.13x faster                                            |
| xml_etree_parse      | 95.9 ms                                                     | 92.8 ms: 1.03x faster                                           |
| pickle_pure_python   | 200 us                                                      | 195 us: 1.03x faster                                            |
| tomli_loads          | 1.41 sec                                                    | 1.38 sec: 1.02x faster                                          |
| pickle_dict          | 18.5 us                                                     | 19.2 us: 1.04x slower                                           |
| xml_etree_process    | 37.1 ms                                                     | 38.6 ms: 1.04x slower                                           |
| xml_etree_iterparse  | 62.6 ms                                                     | 66.1 ms: 1.06x slower                                           |
| unpickle             | 8.09 us                                                     | 8.56 us: 1.06x slower                                           |
| json_loads           | 12.9 us                                                     | 13.7 us: 1.06x slower                                           |
| xml_etree_generate   | 52.2 ms                                                     | 56.6 ms: 1.08x slower                                           |
| pickle_list          | 2.68 us                                                     | 2.91 us: 1.08x slower                                           |
| pickle               | 6.61 us                                                     | 7.42 us: 1.12x slower                                           |
| unpickle_list        | 2.55 us                                                     | 2.90 us: 1.14x slower                                           |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 18.7 ms                                                     | 21.0 ms: 1.12x slower                                           |
| python_startup_no_site | 15.9 ms                                                     | 17.8 ms: 1.12x slower                                           |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 6.91 ms: 1.05x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-pythonperf1-amd64-python-v3.12.0b1-3.12.0b1-5612078 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 97.4 us: 3.30x faster                                           |
| generators               | 33.8 ms                                                     | 21.8 ms: 1.55x faster                                           |
| json_dumps               | 7.56 ms                                                     | 5.67 ms: 1.33x faster                                           |
| richards_super           | 37.5 ms                                                     | 29.4 ms: 1.28x faster                                           |
| unpack_sequence          | 46.1 ns                                                     | 37.9 ns: 1.22x faster                                           |
| deltablue                | 2.61 ms                                                     | 2.19 ms: 1.19x faster                                           |
| richards                 | 30.6 ms                                                     | 25.8 ms: 1.19x faster                                           |
| sqlglot_parse            | 952 us                                                      | 814 us: 1.17x faster                                            |
| logging_silent           | 69.8 ns                                                     | 59.9 ns: 1.17x faster                                           |
| hexiom                   | 4.55 ms                                                     | 4.03 ms: 1.13x faster                                           |
| unpickle_pure_python     | 152 us                                                      | 134 us: 1.13x faster                                            |
| sqlglot_transpile        | 1.16 ms                                                     | 1.03 ms: 1.13x faster                                           |
| go                       | 97.3 ms                                                     | 88.1 ms: 1.10x faster                                           |
| mdp                      | 1.67 sec                                                    | 1.53 sec: 1.09x faster                                          |
| raytrace                 | 211 ms                                                      | 194 ms: 1.09x faster                                            |
| comprehensions           | 15.9 us                                                     | 14.7 us: 1.08x faster                                           |
| async_tree_none          | 320 ms                                                      | 297 ms: 1.08x faster                                            |
| json                     | 3.25 ms                                                     | 3.02 ms: 1.08x faster                                           |
| deepcopy_memo            | 25.2 us                                                     | 23.4 us: 1.08x faster                                           |
| coverage                 | 55.9 ms                                                     | 52.4 ms: 1.07x faster                                           |
| nqueens                  | 64.9 ms                                                     | 61.1 ms: 1.06x faster                                           |
| chaos                    | 47.1 ms                                                     | 44.4 ms: 1.06x faster                                           |
| scimark_lu               | 63.5 ms                                                     | 60.0 ms: 1.06x faster                                           |
| mako                     | 7.26 ms                                                     | 6.91 ms: 1.05x faster                                           |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.45 ms: 1.05x faster                                           |
| asyncio_tcp              | 699 ms                                                      | 668 ms: 1.05x faster                                            |
| async_tree_memoization   | 371 ms                                                      | 355 ms: 1.04x faster                                            |
| fannkuch                 | 252 ms                                                      | 242 ms: 1.04x faster                                            |
| scimark_monte_carlo      | 44.6 ms                                                     | 42.8 ms: 1.04x faster                                           |
| regex_v8                 | 13.8 ms                                                     | 13.3 ms: 1.04x faster                                           |
| coroutines               | 14.6 ms                                                     | 14.1 ms: 1.04x faster                                           |
| mypy2                    | 229 ms                                                      | 220 ms: 1.04x faster                                            |
| xml_etree_parse          | 95.9 ms                                                     | 92.8 ms: 1.03x faster                                           |
| pickle_pure_python       | 200 us                                                      | 195 us: 1.03x faster                                            |
| regex_compile            | 90.6 ms                                                     | 88.7 ms: 1.02x faster                                           |
| tomli_loads              | 1.41 sec                                                    | 1.38 sec: 1.02x faster                                          |
| deepcopy                 | 246 us                                                      | 241 us: 1.02x faster                                            |
| pyflate                  | 304 ms                                                      | 299 ms: 1.02x faster                                            |
| async_tree_io            | 779 ms                                                      | 766 ms: 1.02x faster                                            |
| nbody                    | 70.0 ms                                                     | 69.0 ms: 1.01x faster                                           |
| spectral_norm            | 67.9 ms                                                     | 67.2 ms: 1.01x faster                                           |
| pprint_safe_repr         | 512 ms                                                      | 507 ms: 1.01x faster                                            |
| scimark_fft              | 178 ms                                                      | 177 ms: 1.01x faster                                            |
| sqlglot_normalize        | 190 ms                                                      | 189 ms: 1.01x faster                                            |
| meteor_contest           | 74.7 ms                                                     | 74.4 ms: 1.01x faster                                           |
| logging_format           | 7.01 us                                                     | 7.07 us: 1.01x slower                                           |
| crypto_pyaes             | 47.6 ms                                                     | 48.1 ms: 1.01x slower                                           |
| sqlglot_optimize         | 34.9 ms                                                     | 35.3 ms: 1.01x slower                                           |
| deepcopy_reduce          | 2.07 us                                                     | 2.11 us: 1.02x slower                                           |
| float                    | 54.6 ms                                                     | 55.5 ms: 1.02x slower                                           |
| dulwich_log              | 44.5 ms                                                     | 45.3 ms: 1.02x slower                                           |
| scimark_sor              | 75.6 ms                                                     | 77.3 ms: 1.02x slower                                           |
| bench_thread_pool        | 852 us                                                      | 875 us: 1.03x slower                                            |
| sqlite_synth             | 1.68 us                                                     | 1.73 us: 1.03x slower                                           |
| pidigits                 | 148 ms                                                      | 153 ms: 1.03x slower                                            |
| regex_dna                | 115 ms                                                      | 119 ms: 1.03x slower                                            |
| pickle_dict              | 18.5 us                                                     | 19.2 us: 1.04x slower                                           |
| docutils                 | 1.60 sec                                                    | 1.66 sec: 1.04x slower                                          |
| aiohttp                  | 899 us                                                      | 936 us: 1.04x slower                                            |
| xml_etree_process        | 37.1 ms                                                     | 38.6 ms: 1.04x slower                                           |
| 2to3                     | 209 ms                                                      | 218 ms: 1.04x slower                                            |
| xml_etree_iterparse      | 62.6 ms                                                     | 66.1 ms: 1.06x slower                                           |
| unpickle                 | 8.09 us                                                     | 8.56 us: 1.06x slower                                           |
| telco                    | 3.90 ms                                                     | 4.14 ms: 1.06x slower                                           |
| json_loads               | 12.9 us                                                     | 13.7 us: 1.06x slower                                           |
| regex_effbot             | 1.50 ms                                                     | 1.59 ms: 1.06x slower                                           |
| gc_traversal             | 1.46 ms                                                     | 1.55 ms: 1.06x slower                                           |
| tornado_http             | 91.8 ms                                                     | 99.2 ms: 1.08x slower                                           |
| xml_etree_generate       | 52.2 ms                                                     | 56.6 ms: 1.08x slower                                           |
| pickle_list              | 2.68 us                                                     | 2.91 us: 1.08x slower                                           |
| create_gc_cycles         | 693 us                                                      | 765 us: 1.10x slower                                            |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 2.35 sec: 1.11x slower                                          |
| bench_mp_pool            | 62.5 ms                                                     | 69.6 ms: 1.11x slower                                           |
| python_startup           | 18.7 ms                                                     | 21.0 ms: 1.12x slower                                           |
| pickle                   | 6.61 us                                                     | 7.42 us: 1.12x slower                                           |
| python_startup_no_site   | 15.9 ms                                                     | 17.8 ms: 1.12x slower                                           |
| unpickle_list            | 2.55 us                                                     | 2.90 us: 1.14x slower                                           |
| pathlib                  | 71.4 ms                                                     | 87.5 ms: 1.23x slower                                           |
| async_generators         | 178 ms                                                      | 240 ms: 1.35x slower                                            |
| dask                     | 264 ms                                                      | 381 ms: 1.44x slower                                            |
| Geometric mean           | (ref)                                                       | 1.03x faster                                                    |

Benchmark hidden because not significant (4): pprint_pformat, logging_simple, async_tree_cpu_io_mixed, pycparser
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
