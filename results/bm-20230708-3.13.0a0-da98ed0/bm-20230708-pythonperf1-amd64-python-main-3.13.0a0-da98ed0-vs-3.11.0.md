
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: da98ed0
- commit date: 2023-07-08
- overall geometric mean: 1.01x slower
- HPT reliability: 99.68%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf1-amd64-python-main-3.13.0a0-da98ed0 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| docutils       | 1.60 sec                                                    | 1.68 sec: 1.05x slower                                     |
| tornado_http   | 91.8 ms                                                     | 98.1 ms: 1.07x slower                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf1-amd64-python-main-3.13.0a0-da98ed0 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                       |
| float          | 54.6 ms                                                     | 56.9 ms: 1.04x slower                                      |
| nbody          | 70.0 ms                                                     | 81.2 ms: 1.16x slower                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf1-amd64-python-main-3.13.0a0-da98ed0 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                       |
| regex_compile  | 90.6 ms                                                     | 94.6 ms: 1.04x slower                                      |
| regex_effbot   | 1.50 ms                                                     | 1.60 ms: 1.07x slower                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf1-amd64-python-main-3.13.0a0-da98ed0 |
|---------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps          | 7.56 ms                                                     | 5.79 ms: 1.31x faster                                      |
| xml_etree_parse     | 95.9 ms                                                     | 91.7 ms: 1.05x faster                                      |
| pickle_dict         | 18.5 us                                                     | 19.1 us: 1.03x slower                                      |
| pickle_list         | 2.68 us                                                     | 2.80 us: 1.05x slower                                      |
| xml_etree_iterparse | 62.6 ms                                                     | 65.4 ms: 1.05x slower                                      |
| pickle_pure_python  | 200 us                                                      | 210 us: 1.05x slower                                       |
| unpickle            | 8.09 us                                                     | 8.57 us: 1.06x slower                                      |
| json_loads          | 12.9 us                                                     | 13.7 us: 1.06x slower                                      |
| pickle              | 6.61 us                                                     | 7.10 us: 1.07x slower                                      |
| xml_etree_process   | 37.1 ms                                                     | 40.8 ms: 1.10x slower                                      |
| unpickle_list       | 2.55 us                                                     | 2.83 us: 1.11x slower                                      |
| xml_etree_generate  | 52.2 ms                                                     | 58.9 ms: 1.13x slower                                      |
| tomli_loads         | 1.41 sec                                                    | 1.61 sec: 1.14x slower                                     |
| Geometric mean      | (ref)                                                       | 1.04x slower                                               |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf1-amd64-python-main-3.13.0a0-da98ed0 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 18.7 ms                                                     | 19.9 ms: 1.06x slower                                      |
| python_startup_no_site | 15.9 ms                                                     | 17.0 ms: 1.07x slower                                      |
| Geometric mean         | (ref)                                                       | 1.07x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf1-amd64-python-main-3.13.0a0-da98ed0 |
|-----------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 7.63 ms: 1.05x slower                                      |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-pythonperf1-amd64-python-main-3.13.0a0-da98ed0 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 97.8 us: 3.29x faster                                      |
| generators               | 33.8 ms                                                     | 25.0 ms: 1.35x faster                                      |
| json_dumps               | 7.56 ms                                                     | 5.79 ms: 1.31x faster                                      |
| asyncio_tcp              | 699 ms                                                      | 553 ms: 1.26x faster                                       |
| raytrace                 | 211 ms                                                      | 185 ms: 1.14x faster                                       |
| json                     | 3.25 ms                                                     | 2.89 ms: 1.13x faster                                      |
| mdp                      | 1.67 sec                                                    | 1.49 sec: 1.12x faster                                     |
| deltablue                | 2.61 ms                                                     | 2.38 ms: 1.10x faster                                      |
| unpack_sequence          | 46.1 ns                                                     | 42.1 ns: 1.09x faster                                      |
| async_tree_none          | 320 ms                                                      | 296 ms: 1.08x faster                                       |
| async_tree_io            | 779 ms                                                      | 732 ms: 1.06x faster                                       |
| sqlglot_parse            | 952 us                                                      | 896 us: 1.06x faster                                       |
| coverage                 | 55.9 ms                                                     | 52.8 ms: 1.06x faster                                      |
| async_tree_memoization   | 371 ms                                                      | 352 ms: 1.05x faster                                       |
| richards_super           | 37.5 ms                                                     | 35.6 ms: 1.05x faster                                      |
| xml_etree_parse          | 95.9 ms                                                     | 91.7 ms: 1.05x faster                                      |
| chaos                    | 47.1 ms                                                     | 45.2 ms: 1.04x faster                                      |
| sqlglot_transpile        | 1.16 ms                                                     | 1.13 ms: 1.03x faster                                      |
| comprehensions           | 15.9 us                                                     | 15.5 us: 1.03x faster                                      |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 488 ms: 1.03x faster                                       |
| mypy2                    | 229 ms                                                      | 223 ms: 1.03x faster                                       |
| logging_silent           | 69.8 ns                                                     | 68.4 ns: 1.02x faster                                      |
| spectral_norm            | 67.9 ms                                                     | 67.3 ms: 1.01x faster                                      |
| pidigits                 | 148 ms                                                      | 150 ms: 1.01x slower                                       |
| gc_traversal             | 1.46 ms                                                     | 1.47 ms: 1.01x slower                                      |
| sqlglot_normalize        | 190 ms                                                      | 193 ms: 1.02x slower                                       |
| nqueens                  | 64.9 ms                                                     | 66.1 ms: 1.02x slower                                      |
| bench_thread_pool        | 852 us                                                      | 872 us: 1.02x slower                                       |
| meteor_contest           | 74.7 ms                                                     | 76.6 ms: 1.03x slower                                      |
| dulwich_log              | 44.5 ms                                                     | 45.8 ms: 1.03x slower                                      |
| pickle_dict              | 18.5 us                                                     | 19.1 us: 1.03x slower                                      |
| go                       | 97.3 ms                                                     | 100 ms: 1.03x slower                                       |
| regex_dna                | 115 ms                                                      | 119 ms: 1.03x slower                                       |
| richards                 | 30.6 ms                                                     | 31.5 ms: 1.03x slower                                      |
| sqlglot_optimize         | 34.9 ms                                                     | 36.1 ms: 1.04x slower                                      |
| scimark_lu               | 63.5 ms                                                     | 66.0 ms: 1.04x slower                                      |
| coroutines               | 14.6 ms                                                     | 15.2 ms: 1.04x slower                                      |
| float                    | 54.6 ms                                                     | 56.9 ms: 1.04x slower                                      |
| regex_compile            | 90.6 ms                                                     | 94.6 ms: 1.04x slower                                      |
| sqlite_synth             | 1.68 us                                                     | 1.76 us: 1.05x slower                                      |
| pickle_list              | 2.68 us                                                     | 2.80 us: 1.05x slower                                      |
| xml_etree_iterparse      | 62.6 ms                                                     | 65.4 ms: 1.05x slower                                      |
| pickle_pure_python       | 200 us                                                      | 210 us: 1.05x slower                                       |
| docutils                 | 1.60 sec                                                    | 1.68 sec: 1.05x slower                                     |
| mako                     | 7.26 ms                                                     | 7.63 ms: 1.05x slower                                      |
| deepcopy                 | 246 us                                                      | 258 us: 1.05x slower                                       |
| deepcopy_memo            | 25.2 us                                                     | 26.5 us: 1.05x slower                                      |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.71 ms: 1.06x slower                                      |
| create_gc_cycles         | 693 us                                                      | 732 us: 1.06x slower                                       |
| unpickle                 | 8.09 us                                                     | 8.57 us: 1.06x slower                                      |
| logging_simple           | 6.61 us                                                     | 7.01 us: 1.06x slower                                      |
| json_loads               | 12.9 us                                                     | 13.7 us: 1.06x slower                                      |
| python_startup           | 18.7 ms                                                     | 19.9 ms: 1.06x slower                                      |
| logging_format           | 7.01 us                                                     | 7.48 us: 1.07x slower                                      |
| regex_effbot             | 1.50 ms                                                     | 1.60 ms: 1.07x slower                                      |
| crypto_pyaes             | 47.6 ms                                                     | 50.8 ms: 1.07x slower                                      |
| tornado_http             | 91.8 ms                                                     | 98.1 ms: 1.07x slower                                      |
| bench_mp_pool            | 62.5 ms                                                     | 67.0 ms: 1.07x slower                                      |
| python_startup_no_site   | 15.9 ms                                                     | 17.0 ms: 1.07x slower                                      |
| pickle                   | 6.61 us                                                     | 7.10 us: 1.07x slower                                      |
| pyflate                  | 304 ms                                                      | 327 ms: 1.08x slower                                       |
| pprint_safe_repr         | 512 ms                                                      | 552 ms: 1.08x slower                                       |
| pprint_pformat           | 1.04 sec                                                    | 1.13 sec: 1.09x slower                                     |
| pycparser                | 691 ms                                                      | 750 ms: 1.09x slower                                       |
| xml_etree_process        | 37.1 ms                                                     | 40.8 ms: 1.10x slower                                      |
| deepcopy_reduce          | 2.07 us                                                     | 2.28 us: 1.10x slower                                      |
| fannkuch                 | 252 ms                                                      | 279 ms: 1.10x slower                                       |
| unpickle_list            | 2.55 us                                                     | 2.83 us: 1.11x slower                                      |
| scimark_monte_carlo      | 44.6 ms                                                     | 49.7 ms: 1.11x slower                                      |
| xml_etree_generate       | 52.2 ms                                                     | 58.9 ms: 1.13x slower                                      |
| tomli_loads              | 1.41 sec                                                    | 1.61 sec: 1.14x slower                                     |
| telco                    | 3.90 ms                                                     | 4.48 ms: 1.15x slower                                      |
| scimark_fft              | 178 ms                                                      | 205 ms: 1.15x slower                                       |
| nbody                    | 70.0 ms                                                     | 81.2 ms: 1.16x slower                                      |
| pathlib                  | 71.4 ms                                                     | 83.1 ms: 1.16x slower                                      |
| scimark_sor              | 75.6 ms                                                     | 92.9 ms: 1.23x slower                                      |
| async_generators         | 178 ms                                                      | 244 ms: 1.37x slower                                       |
| dask                     | 264 ms                                                      | 394 ms: 1.49x slower                                       |
| Geometric mean           | (ref)                                                       | 1.01x slower                                               |

Benchmark hidden because not significant (4): asyncio_tcp_ssl, unpickle_pure_python, hexiom, regex_v8
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 99.68% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x
