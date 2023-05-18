
# Results vs. 3.11.0

- fork: adr26
- ref: condvar
- machine: windows-amd64
- commit hash: 4f0355f
- commit date: 2023-05-16
- overall geometric mean: 1.05x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7+-4f0355f |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 214 ms: 1.02x slower                                          |
| docutils       | 1.60 sec                                                    | 1.63 sec: 1.01x slower                                        |
| tornado_http   | 91.8 ms                                                     | 87.4 ms: 1.05x faster                                         |
| Geometric mean | (ref)                                                       | 1.00x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7+-4f0355f |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 54.6 ms                                                     | 55.2 ms: 1.01x slower                                         |
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                          |
| nbody          | 70.0 ms                                                     | 72.7 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                       | 1.02x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7+-4f0355f |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 85.8 ms: 1.06x faster                                         |
| regex_v8       | 13.8 ms                                                     | 13.8 ms: 1.01x faster                                         |
| regex_dna      | 115 ms                                                      | 117 ms: 1.01x slower                                          |
| regex_effbot   | 1.50 ms                                                     | 1.58 ms: 1.05x slower                                         |
| Geometric mean | (ref)                                                       | 1.00x slower                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7+-4f0355f |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.71 ms: 1.32x faster                                         |
| unpickle_pure_python | 152 us                                                      | 136 us: 1.12x faster                                          |
| pickle_pure_python   | 200 us                                                      | 193 us: 1.04x faster                                          |
| xml_etree_parse      | 95.9 ms                                                     | 93.0 ms: 1.03x faster                                         |
| tomli_loads          | 1.41 sec                                                    | 1.39 sec: 1.02x faster                                        |
| xml_etree_iterparse  | 62.6 ms                                                     | 64.2 ms: 1.03x slower                                         |
| unpickle             | 8.09 us                                                     | 8.45 us: 1.04x slower                                         |
| xml_etree_process    | 37.1 ms                                                     | 38.9 ms: 1.05x slower                                         |
| pickle_list          | 2.68 us                                                     | 2.83 us: 1.05x slower                                         |
| json_loads           | 12.9 us                                                     | 13.6 us: 1.05x slower                                         |
| unpickle_list        | 2.55 us                                                     | 2.77 us: 1.09x slower                                         |
| xml_etree_generate   | 52.2 ms                                                     | 57.7 ms: 1.11x slower                                         |
| pickle               | 6.61 us                                                     | 7.44 us: 1.13x slower                                         |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                  |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7+-4f0355f |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 16.3 ms: 1.02x slower                                         |
| python_startup         | 18.7 ms                                                     | 19.2 ms: 1.03x slower                                         |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7+-4f0355f |
|-----------|:-----------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 6.87 ms: 1.06x faster                                         |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230516-pythonperf1-amd64-adr26-condvar-3.12.0a7+-4f0355f |
|--------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 99.4 us: 3.24x faster                                         |
| generators               | 33.8 ms                                                     | 23.1 ms: 1.46x faster                                         |
| asyncio_tcp              | 699 ms                                                      | 484 ms: 1.44x faster                                          |
| json_dumps               | 7.56 ms                                                     | 5.71 ms: 1.32x faster                                         |
| unpack_sequence          | 46.1 ns                                                     | 36.5 ns: 1.26x faster                                         |
| richards_super           | 37.5 ms                                                     | 30.4 ms: 1.23x faster                                         |
| deltablue                | 2.61 ms                                                     | 2.17 ms: 1.21x faster                                         |
| sqlglot_parse            | 952 us                                                      | 810 us: 1.17x faster                                          |
| mdp                      | 1.67 sec                                                    | 1.44 sec: 1.16x faster                                        |
| logging_silent           | 69.8 ns                                                     | 61.2 ns: 1.14x faster                                         |
| async_tree_none          | 320 ms                                                      | 281 ms: 1.14x faster                                          |
| sqlglot_transpile        | 1.16 ms                                                     | 1.02 ms: 1.14x faster                                         |
| richards                 | 30.6 ms                                                     | 27.0 ms: 1.13x faster                                         |
| hexiom                   | 4.55 ms                                                     | 4.05 ms: 1.12x faster                                         |
| comprehensions           | 15.9 us                                                     | 14.2 us: 1.12x faster                                         |
| unpickle_pure_python     | 152 us                                                      | 136 us: 1.12x faster                                          |
| async_tree_memoization   | 371 ms                                                      | 332 ms: 1.12x faster                                          |
| raytrace                 | 211 ms                                                      | 189 ms: 1.12x faster                                          |
| go                       | 97.3 ms                                                     | 87.6 ms: 1.11x faster                                         |
| chaos                    | 47.1 ms                                                     | 42.8 ms: 1.10x faster                                         |
| coverage                 | 55.9 ms                                                     | 50.9 ms: 1.10x faster                                         |
| fannkuch                 | 252 ms                                                      | 233 ms: 1.08x faster                                          |
| mypy2                    | 229 ms                                                      | 212 ms: 1.08x faster                                          |
| nqueens                  | 64.9 ms                                                     | 60.1 ms: 1.08x faster                                         |
| async_tree_io            | 779 ms                                                      | 728 ms: 1.07x faster                                          |
| dulwich_log              | 44.5 ms                                                     | 41.6 ms: 1.07x faster                                         |
| scimark_lu               | 63.5 ms                                                     | 59.5 ms: 1.07x faster                                         |
| json                     | 3.25 ms                                                     | 3.05 ms: 1.07x faster                                         |
| mako                     | 7.26 ms                                                     | 6.87 ms: 1.06x faster                                         |
| regex_compile            | 90.6 ms                                                     | 85.8 ms: 1.06x faster                                         |
| spectral_norm            | 67.9 ms                                                     | 64.3 ms: 1.06x faster                                         |
| deepcopy_memo            | 25.2 us                                                     | 23.9 us: 1.05x faster                                         |
| tornado_http             | 91.8 ms                                                     | 87.4 ms: 1.05x faster                                         |
| bench_thread_pool        | 852 us                                                      | 814 us: 1.05x faster                                          |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 481 ms: 1.04x faster                                          |
| pickle_pure_python       | 200 us                                                      | 193 us: 1.04x faster                                          |
| sqlglot_normalize        | 190 ms                                                      | 184 ms: 1.03x faster                                          |
| xml_etree_parse          | 95.9 ms                                                     | 93.0 ms: 1.03x faster                                         |
| pyflate                  | 304 ms                                                      | 297 ms: 1.02x faster                                          |
| deepcopy                 | 246 us                                                      | 241 us: 1.02x faster                                          |
| tomli_loads              | 1.41 sec                                                    | 1.39 sec: 1.02x faster                                        |
| logging_simple           | 6.61 us                                                     | 6.49 us: 1.02x faster                                         |
| scimark_monte_carlo      | 44.6 ms                                                     | 43.8 ms: 1.02x faster                                         |
| crypto_pyaes             | 47.6 ms                                                     | 46.7 ms: 1.02x faster                                         |
| aiohttp                  | 899 us                                                      | 886 us: 1.01x faster                                          |
| sqlglot_optimize         | 34.9 ms                                                     | 34.4 ms: 1.01x faster                                         |
| coroutines               | 14.6 ms                                                     | 14.4 ms: 1.01x faster                                         |
| logging_format           | 7.01 us                                                     | 6.92 us: 1.01x faster                                         |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.54 ms: 1.01x faster                                         |
| regex_v8                 | 13.8 ms                                                     | 13.8 ms: 1.01x faster                                         |
| meteor_contest           | 74.7 ms                                                     | 75.2 ms: 1.01x slower                                         |
| pprint_pformat           | 1.04 sec                                                    | 1.05 sec: 1.01x slower                                        |
| regex_dna                | 115 ms                                                      | 117 ms: 1.01x slower                                          |
| float                    | 54.6 ms                                                     | 55.2 ms: 1.01x slower                                         |
| docutils                 | 1.60 sec                                                    | 1.63 sec: 1.01x slower                                        |
| pprint_safe_repr         | 512 ms                                                      | 519 ms: 1.01x slower                                          |
| create_gc_cycles         | 693 us                                                      | 704 us: 1.02x slower                                          |
| pidigits                 | 148 ms                                                      | 151 ms: 1.02x slower                                          |
| 2to3                     | 209 ms                                                      | 214 ms: 1.02x slower                                          |
| python_startup_no_site   | 15.9 ms                                                     | 16.3 ms: 1.02x slower                                         |
| xml_etree_iterparse      | 62.6 ms                                                     | 64.2 ms: 1.03x slower                                         |
| python_startup           | 18.7 ms                                                     | 19.2 ms: 1.03x slower                                         |
| nbody                    | 70.0 ms                                                     | 72.7 ms: 1.04x slower                                         |
| deepcopy_reduce          | 2.07 us                                                     | 2.16 us: 1.04x slower                                         |
| unpickle                 | 8.09 us                                                     | 8.45 us: 1.04x slower                                         |
| xml_etree_process        | 37.1 ms                                                     | 38.9 ms: 1.05x slower                                         |
| regex_effbot             | 1.50 ms                                                     | 1.58 ms: 1.05x slower                                         |
| pickle_list              | 2.68 us                                                     | 2.83 us: 1.05x slower                                         |
| json_loads               | 12.9 us                                                     | 13.6 us: 1.05x slower                                         |
| scimark_sor              | 75.6 ms                                                     | 80.2 ms: 1.06x slower                                         |
| telco                    | 3.90 ms                                                     | 4.16 ms: 1.06x slower                                         |
| unpickle_list            | 2.55 us                                                     | 2.77 us: 1.09x slower                                         |
| bench_mp_pool            | 62.5 ms                                                     | 68.1 ms: 1.09x slower                                         |
| xml_etree_generate       | 52.2 ms                                                     | 57.7 ms: 1.11x slower                                         |
| pickle                   | 6.61 us                                                     | 7.44 us: 1.13x slower                                         |
| pathlib                  | 71.4 ms                                                     | 82.9 ms: 1.16x slower                                         |
| async_generators         | 178 ms                                                      | 229 ms: 1.29x slower                                          |
| dask                     | 264 ms                                                      | 371 ms: 1.40x slower                                          |
| Geometric mean           | (ref)                                                       | 1.05x faster                                                  |

Benchmark hidden because not significant (6): asyncio_tcp_ssl, pycparser, scimark_fft, gc_traversal, sqlite_synth, pickle_dict
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
