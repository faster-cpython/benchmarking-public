
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: windows-amd64
- commit hash: 730c873
- commit date: 2023-07-01
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf1-amd64-python-3.12-3.12.0b3+-730c873 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 215 ms: 1.03x slower                                        |
| docutils       | 1.60 sec                                                    | 1.68 sec: 1.05x slower                                      |
| tornado_http   | 91.8 ms                                                     | 90.0 ms: 1.02x faster                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf1-amd64-python-3.12-3.12.0b3+-730c873 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                       | 1.00x faster                                                |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf1-amd64-python-3.12-3.12.0b3+-730c873 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 86.1 ms: 1.05x faster                                       |
| regex_v8       | 13.8 ms                                                     | 13.4 ms: 1.04x faster                                       |
| regex_dna      | 115 ms                                                      | 118 ms: 1.02x slower                                        |
| regex_effbot   | 1.50 ms                                                     | 1.82 ms: 1.21x slower                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf1-amd64-python-3.12-3.12.0b3+-730c873 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 6.03 ms: 1.25x faster                                       |
| unpickle_pure_python | 152 us                                                      | 134 us: 1.13x faster                                        |
| pickle_pure_python   | 200 us                                                      | 190 us: 1.05x faster                                        |
| xml_etree_parse      | 95.9 ms                                                     | 93.5 ms: 1.03x faster                                       |
| tomli_loads          | 1.41 sec                                                    | 1.40 sec: 1.01x faster                                      |
| xml_etree_process    | 37.1 ms                                                     | 38.0 ms: 1.03x slower                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 64.7 ms: 1.03x slower                                       |
| xml_etree_generate   | 52.2 ms                                                     | 55.7 ms: 1.07x slower                                       |
| unpickle             | 8.09 us                                                     | 8.68 us: 1.07x slower                                       |
| pickle_list          | 2.68 us                                                     | 2.93 us: 1.09x slower                                       |
| pickle               | 6.61 us                                                     | 7.32 us: 1.11x slower                                       |
| unpickle_list        | 2.55 us                                                     | 2.87 us: 1.13x slower                                       |
| json_loads           | 12.9 us                                                     | 14.6 us: 1.13x slower                                       |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf1-amd64-python-3.12-3.12.0b3+-730c873 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 18.7 ms                                                     | 20.3 ms: 1.09x slower                                       |
| python_startup_no_site | 15.9 ms                                                     | 17.5 ms: 1.10x slower                                       |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf1-amd64-python-3.12-3.12.0b3+-730c873 |
|-----------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 6.93 ms: 1.05x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-pythonperf1-amd64-python-3.12-3.12.0b3+-730c873 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 97.2 us: 3.31x faster                                       |
| generators               | 33.8 ms                                                     | 21.6 ms: 1.57x faster                                       |
| asyncio_tcp              | 699 ms                                                      | 500 ms: 1.40x faster                                        |
| json_dumps               | 7.56 ms                                                     | 6.03 ms: 1.25x faster                                       |
| richards_super           | 37.5 ms                                                     | 30.0 ms: 1.25x faster                                       |
| deltablue                | 2.61 ms                                                     | 2.11 ms: 1.24x faster                                       |
| sqlglot_parse            | 952 us                                                      | 796 us: 1.20x faster                                        |
| logging_silent           | 69.8 ns                                                     | 58.8 ns: 1.19x faster                                       |
| richards                 | 30.6 ms                                                     | 26.1 ms: 1.17x faster                                       |
| unpack_sequence          | 46.1 ns                                                     | 39.5 ns: 1.17x faster                                       |
| sqlglot_transpile        | 1.16 ms                                                     | 1.01 ms: 1.15x faster                                       |
| comprehensions           | 15.9 us                                                     | 13.9 us: 1.15x faster                                       |
| hexiom                   | 4.55 ms                                                     | 4.01 ms: 1.13x faster                                       |
| unpickle_pure_python     | 152 us                                                      | 134 us: 1.13x faster                                        |
| mdp                      | 1.67 sec                                                    | 1.48 sec: 1.13x faster                                      |
| raytrace                 | 211 ms                                                      | 187 ms: 1.13x faster                                        |
| chaos                    | 47.1 ms                                                     | 41.9 ms: 1.13x faster                                       |
| go                       | 97.3 ms                                                     | 86.9 ms: 1.12x faster                                       |
| scimark_lu               | 63.5 ms                                                     | 57.3 ms: 1.11x faster                                       |
| nqueens                  | 64.9 ms                                                     | 59.7 ms: 1.09x faster                                       |
| async_tree_memoization   | 371 ms                                                      | 342 ms: 1.08x faster                                        |
| sqlglot_normalize        | 190 ms                                                      | 176 ms: 1.08x faster                                        |
| scimark_monte_carlo      | 44.6 ms                                                     | 41.6 ms: 1.07x faster                                       |
| async_tree_none          | 320 ms                                                      | 298 ms: 1.07x faster                                        |
| mypy2                    | 229 ms                                                      | 213 ms: 1.07x faster                                        |
| async_tree_io            | 779 ms                                                      | 727 ms: 1.07x faster                                        |
| deepcopy_memo            | 25.2 us                                                     | 23.6 us: 1.07x faster                                       |
| deepcopy                 | 246 us                                                      | 231 us: 1.06x faster                                        |
| fannkuch                 | 252 ms                                                      | 239 ms: 1.06x faster                                        |
| regex_compile            | 90.6 ms                                                     | 86.1 ms: 1.05x faster                                       |
| pickle_pure_python       | 200 us                                                      | 190 us: 1.05x faster                                        |
| mako                     | 7.26 ms                                                     | 6.93 ms: 1.05x faster                                       |
| sqlglot_optimize         | 34.9 ms                                                     | 33.5 ms: 1.04x faster                                       |
| logging_simple           | 6.61 us                                                     | 6.35 us: 1.04x faster                                       |
| regex_v8                 | 13.8 ms                                                     | 13.4 ms: 1.04x faster                                       |
| logging_format           | 7.01 us                                                     | 6.79 us: 1.03x faster                                       |
| coroutines               | 14.6 ms                                                     | 14.2 ms: 1.03x faster                                       |
| coverage                 | 55.9 ms                                                     | 54.2 ms: 1.03x faster                                       |
| xml_etree_parse          | 95.9 ms                                                     | 93.5 ms: 1.03x faster                                       |
| tornado_http             | 91.8 ms                                                     | 90.0 ms: 1.02x faster                                       |
| meteor_contest           | 74.7 ms                                                     | 73.3 ms: 1.02x faster                                       |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 493 ms: 1.02x faster                                        |
| pyflate                  | 304 ms                                                      | 300 ms: 1.01x faster                                        |
| aiohttp                  | 899 us                                                      | 889 us: 1.01x faster                                        |
| tomli_loads              | 1.41 sec                                                    | 1.40 sec: 1.01x faster                                      |
| pprint_pformat           | 1.04 sec                                                    | 1.03 sec: 1.01x faster                                      |
| dulwich_log              | 44.5 ms                                                     | 44.1 ms: 1.01x faster                                       |
| pprint_safe_repr         | 512 ms                                                      | 508 ms: 1.01x faster                                        |
| crypto_pyaes             | 47.6 ms                                                     | 48.1 ms: 1.01x slower                                       |
| pidigits                 | 148 ms                                                      | 150 ms: 1.01x slower                                        |
| bench_thread_pool        | 852 us                                                      | 869 us: 1.02x slower                                        |
| scimark_fft              | 178 ms                                                      | 182 ms: 1.02x slower                                        |
| regex_dna                | 115 ms                                                      | 118 ms: 1.02x slower                                        |
| xml_etree_process        | 37.1 ms                                                     | 38.0 ms: 1.03x slower                                       |
| 2to3                     | 209 ms                                                      | 215 ms: 1.03x slower                                        |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.65 ms: 1.03x slower                                       |
| xml_etree_iterparse      | 62.6 ms                                                     | 64.7 ms: 1.03x slower                                       |
| sqlite_synth             | 1.68 us                                                     | 1.76 us: 1.04x slower                                       |
| docutils                 | 1.60 sec                                                    | 1.68 sec: 1.05x slower                                      |
| spectral_norm            | 67.9 ms                                                     | 71.5 ms: 1.05x slower                                       |
| telco                    | 3.90 ms                                                     | 4.13 ms: 1.06x slower                                       |
| gc_traversal             | 1.46 ms                                                     | 1.54 ms: 1.06x slower                                       |
| xml_etree_generate       | 52.2 ms                                                     | 55.7 ms: 1.07x slower                                       |
| unpickle                 | 8.09 us                                                     | 8.68 us: 1.07x slower                                       |
| scimark_sor              | 75.6 ms                                                     | 81.2 ms: 1.07x slower                                       |
| create_gc_cycles         | 693 us                                                      | 752 us: 1.09x slower                                        |
| python_startup           | 18.7 ms                                                     | 20.3 ms: 1.09x slower                                       |
| pickle_list              | 2.68 us                                                     | 2.93 us: 1.09x slower                                       |
| bench_mp_pool            | 62.5 ms                                                     | 68.8 ms: 1.10x slower                                       |
| python_startup_no_site   | 15.9 ms                                                     | 17.5 ms: 1.10x slower                                       |
| pickle                   | 6.61 us                                                     | 7.32 us: 1.11x slower                                       |
| unpickle_list            | 2.55 us                                                     | 2.87 us: 1.13x slower                                       |
| json_loads               | 12.9 us                                                     | 14.6 us: 1.13x slower                                       |
| pathlib                  | 71.4 ms                                                     | 83.0 ms: 1.16x slower                                       |
| regex_effbot             | 1.50 ms                                                     | 1.82 ms: 1.21x slower                                       |
| async_generators         | 178 ms                                                      | 237 ms: 1.33x slower                                        |
| dask                     | 264 ms                                                      | 365 ms: 1.38x slower                                        |
| Geometric mean           | (ref)                                                       | 1.04x faster                                                |

Benchmark hidden because not significant (7): json, pycparser, float, nbody, deepcopy_reduce, pickle_dict, asyncio_tcp_ssl
Ignored benchmarks (14) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
