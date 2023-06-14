
# Results vs. 3.11.0

- fork: python
- ref: v3.12.0b2
- machine: windows-amd64
- commit hash: e6c0efa
- commit date: 2023-06-06
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf1-amd64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 216 ms: 1.03x slower                                            |
| docutils       | 1.60 sec                                                    | 1.67 sec: 1.04x slower                                          |
| tornado_http   | 91.8 ms                                                     | 88.5 ms: 1.04x faster                                           |
| Geometric mean | (ref)                                                       | 1.01x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf1-amd64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 68.3 ms: 1.02x faster                                           |
| float          | 54.6 ms                                                     | 55.2 ms: 1.01x slower                                           |
| pidigits       | 148 ms                                                      | 153 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                       | 1.01x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf1-amd64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 87.9 ms: 1.03x faster                                           |
| regex_v8       | 13.8 ms                                                     | 13.9 ms: 1.01x slower                                           |
| regex_dna      | 115 ms                                                      | 125 ms: 1.08x slower                                            |
| regex_effbot   | 1.50 ms                                                     | 1.63 ms: 1.09x slower                                           |
| Geometric mean | (ref)                                                       | 1.03x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf1-amd64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.59 ms: 1.35x faster                                           |
| unpickle_pure_python | 152 us                                                      | 135 us: 1.13x faster                                            |
| xml_etree_parse      | 95.9 ms                                                     | 91.6 ms: 1.05x faster                                           |
| tomli_loads          | 1.41 sec                                                    | 1.37 sec: 1.03x faster                                          |
| pickle_dict          | 18.5 us                                                     | 18.2 us: 1.02x faster                                           |
| pickle_pure_python   | 200 us                                                      | 197 us: 1.02x faster                                            |
| xml_etree_process    | 37.1 ms                                                     | 38.3 ms: 1.03x slower                                           |
| xml_etree_iterparse  | 62.6 ms                                                     | 65.0 ms: 1.04x slower                                           |
| unpickle             | 8.09 us                                                     | 8.48 us: 1.05x slower                                           |
| pickle_list          | 2.68 us                                                     | 2.85 us: 1.06x slower                                           |
| json_loads           | 12.9 us                                                     | 13.7 us: 1.06x slower                                           |
| pickle               | 6.61 us                                                     | 7.11 us: 1.08x slower                                           |
| xml_etree_generate   | 52.2 ms                                                     | 57.0 ms: 1.09x slower                                           |
| unpickle_list        | 2.55 us                                                     | 2.90 us: 1.14x slower                                           |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf1-amd64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 18.7 ms                                                     | 20.2 ms: 1.08x slower                                           |
| python_startup_no_site | 15.9 ms                                                     | 17.4 ms: 1.09x slower                                           |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf1-amd64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 7.05 ms: 1.03x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf1-amd64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 95.0 us: 3.39x faster                                           |
| generators               | 33.8 ms                                                     | 22.4 ms: 1.51x faster                                           |
| asyncio_tcp              | 699 ms                                                      | 478 ms: 1.46x faster                                            |
| json_dumps               | 7.56 ms                                                     | 5.59 ms: 1.35x faster                                           |
| richards_super           | 37.5 ms                                                     | 29.2 ms: 1.28x faster                                           |
| deltablue                | 2.61 ms                                                     | 2.08 ms: 1.25x faster                                           |
| mdp                      | 1.67 sec                                                    | 1.38 sec: 1.21x faster                                          |
| sqlglot_parse            | 952 us                                                      | 799 us: 1.19x faster                                            |
| richards                 | 30.6 ms                                                     | 25.7 ms: 1.19x faster                                           |
| unpack_sequence          | 46.1 ns                                                     | 39.1 ns: 1.18x faster                                           |
| logging_silent           | 69.8 ns                                                     | 59.4 ns: 1.18x faster                                           |
| sqlglot_transpile        | 1.16 ms                                                     | 1.01 ms: 1.15x faster                                           |
| hexiom                   | 4.55 ms                                                     | 4.00 ms: 1.14x faster                                           |
| unpickle_pure_python     | 152 us                                                      | 135 us: 1.13x faster                                            |
| raytrace                 | 211 ms                                                      | 187 ms: 1.13x faster                                            |
| scimark_lu               | 63.5 ms                                                     | 56.8 ms: 1.12x faster                                           |
| go                       | 97.3 ms                                                     | 87.8 ms: 1.11x faster                                           |
| comprehensions           | 15.9 us                                                     | 14.4 us: 1.11x faster                                           |
| chaos                    | 47.1 ms                                                     | 42.8 ms: 1.10x faster                                           |
| json                     | 3.25 ms                                                     | 2.99 ms: 1.09x faster                                           |
| async_tree_none          | 320 ms                                                      | 298 ms: 1.08x faster                                            |
| async_tree_memoization   | 371 ms                                                      | 347 ms: 1.07x faster                                            |
| coverage                 | 55.9 ms                                                     | 52.5 ms: 1.06x faster                                           |
| nqueens                  | 64.9 ms                                                     | 61.1 ms: 1.06x faster                                           |
| deepcopy_memo            | 25.2 us                                                     | 23.8 us: 1.06x faster                                           |
| mypy2                    | 229 ms                                                      | 217 ms: 1.06x faster                                            |
| coroutines               | 14.6 ms                                                     | 13.9 ms: 1.05x faster                                           |
| fannkuch                 | 252 ms                                                      | 240 ms: 1.05x faster                                            |
| scimark_monte_carlo      | 44.6 ms                                                     | 42.6 ms: 1.05x faster                                           |
| xml_etree_parse          | 95.9 ms                                                     | 91.6 ms: 1.05x faster                                           |
| async_tree_io            | 779 ms                                                      | 744 ms: 1.05x faster                                            |
| sqlglot_normalize        | 190 ms                                                      | 183 ms: 1.04x faster                                            |
| tornado_http             | 91.8 ms                                                     | 88.5 ms: 1.04x faster                                           |
| tomli_loads              | 1.41 sec                                                    | 1.37 sec: 1.03x faster                                          |
| sqlglot_optimize         | 34.9 ms                                                     | 33.8 ms: 1.03x faster                                           |
| regex_compile            | 90.6 ms                                                     | 87.9 ms: 1.03x faster                                           |
| mako                     | 7.26 ms                                                     | 7.05 ms: 1.03x faster                                           |
| spectral_norm            | 67.9 ms                                                     | 66.0 ms: 1.03x faster                                           |
| pyflate                  | 304 ms                                                      | 296 ms: 1.03x faster                                            |
| scimark_fft              | 178 ms                                                      | 174 ms: 1.03x faster                                            |
| nbody                    | 70.0 ms                                                     | 68.3 ms: 1.02x faster                                           |
| aiohttp                  | 899 us                                                      | 879 us: 1.02x faster                                            |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.52 ms: 1.02x faster                                           |
| pickle_dict              | 18.5 us                                                     | 18.2 us: 1.02x faster                                           |
| deepcopy                 | 246 us                                                      | 241 us: 1.02x faster                                            |
| pickle_pure_python       | 200 us                                                      | 197 us: 1.02x faster                                            |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 493 ms: 1.02x faster                                            |
| pycparser                | 691 ms                                                      | 680 ms: 1.02x faster                                            |
| meteor_contest           | 74.7 ms                                                     | 73.9 ms: 1.01x faster                                           |
| logging_simple           | 6.61 us                                                     | 6.54 us: 1.01x faster                                           |
| crypto_pyaes             | 47.6 ms                                                     | 47.2 ms: 1.01x faster                                           |
| dulwich_log              | 44.5 ms                                                     | 44.2 ms: 1.01x faster                                           |
| pprint_pformat           | 1.04 sec                                                    | 1.03 sec: 1.00x faster                                          |
| regex_v8                 | 13.8 ms                                                     | 13.9 ms: 1.01x slower                                           |
| float                    | 54.6 ms                                                     | 55.2 ms: 1.01x slower                                           |
| deepcopy_reduce          | 2.07 us                                                     | 2.10 us: 1.01x slower                                           |
| bench_thread_pool        | 852 us                                                      | 867 us: 1.02x slower                                            |
| scimark_sor              | 75.6 ms                                                     | 77.3 ms: 1.02x slower                                           |
| 2to3                     | 209 ms                                                      | 216 ms: 1.03x slower                                            |
| xml_etree_process        | 37.1 ms                                                     | 38.3 ms: 1.03x slower                                           |
| pidigits                 | 148 ms                                                      | 153 ms: 1.03x slower                                            |
| xml_etree_iterparse      | 62.6 ms                                                     | 65.0 ms: 1.04x slower                                           |
| docutils                 | 1.60 sec                                                    | 1.67 sec: 1.04x slower                                          |
| gc_traversal             | 1.46 ms                                                     | 1.53 ms: 1.05x slower                                           |
| unpickle                 | 8.09 us                                                     | 8.48 us: 1.05x slower                                           |
| telco                    | 3.90 ms                                                     | 4.15 ms: 1.06x slower                                           |
| pickle_list              | 2.68 us                                                     | 2.85 us: 1.06x slower                                           |
| sqlite_synth             | 1.68 us                                                     | 1.79 us: 1.06x slower                                           |
| json_loads               | 12.9 us                                                     | 13.7 us: 1.06x slower                                           |
| create_gc_cycles         | 693 us                                                      | 744 us: 1.07x slower                                            |
| pickle                   | 6.61 us                                                     | 7.11 us: 1.08x slower                                           |
| regex_dna                | 115 ms                                                      | 125 ms: 1.08x slower                                            |
| python_startup           | 18.7 ms                                                     | 20.2 ms: 1.08x slower                                           |
| regex_effbot             | 1.50 ms                                                     | 1.63 ms: 1.09x slower                                           |
| bench_mp_pool            | 62.5 ms                                                     | 68.0 ms: 1.09x slower                                           |
| xml_etree_generate       | 52.2 ms                                                     | 57.0 ms: 1.09x slower                                           |
| python_startup_no_site   | 15.9 ms                                                     | 17.4 ms: 1.09x slower                                           |
| unpickle_list            | 2.55 us                                                     | 2.90 us: 1.14x slower                                           |
| pathlib                  | 71.4 ms                                                     | 83.2 ms: 1.17x slower                                           |
| async_generators         | 178 ms                                                      | 233 ms: 1.31x slower                                            |
| dask                     | 264 ms                                                      | 373 ms: 1.41x slower                                            |
| Geometric mean           | (ref)                                                       | 1.04x faster                                                    |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, pprint_safe_repr, logging_format
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
