
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 8c17729
- commit date: 2023-07-16
- overall geometric mean: 1.01x faster
- HPT reliability: 83.59%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-pythonperf1-amd64-python-main-3.13.0a0-8c17729 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| docutils       | 1.60 sec                                                    | 1.66 sec: 1.04x slower                                     |
| tornado_http   | 91.8 ms                                                     | 89.4 ms: 1.03x faster                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-pythonperf1-amd64-python-main-3.13.0a0-8c17729 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                       |
| float          | 54.6 ms                                                     | 56.1 ms: 1.03x slower                                      |
| nbody          | 70.0 ms                                                     | 76.8 ms: 1.10x slower                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-pythonperf1-amd64-python-main-3.13.0a0-8c17729 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_v8       | 13.8 ms                                                     | 14.0 ms: 1.01x slower                                      |
| regex_compile  | 90.6 ms                                                     | 93.4 ms: 1.03x slower                                      |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                       |
| regex_effbot   | 1.50 ms                                                     | 1.58 ms: 1.06x slower                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-pythonperf1-amd64-python-main-3.13.0a0-8c17729 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.75 ms: 1.31x faster                                      |
| unpickle_pure_python | 152 us                                                      | 145 us: 1.05x faster                                       |
| pickle_dict          | 18.5 us                                                     | 18.0 us: 1.03x faster                                      |
| xml_etree_parse      | 95.9 ms                                                     | 93.8 ms: 1.02x faster                                      |
| pickle_pure_python   | 200 us                                                      | 201 us: 1.01x slower                                       |
| pickle_list          | 2.68 us                                                     | 2.72 us: 1.01x slower                                      |
| unpickle             | 8.09 us                                                     | 8.38 us: 1.04x slower                                      |
| xml_etree_iterparse  | 62.6 ms                                                     | 65.6 ms: 1.05x slower                                      |
| json_loads           | 12.9 us                                                     | 13.6 us: 1.05x slower                                      |
| pickle               | 6.61 us                                                     | 6.98 us: 1.06x slower                                      |
| xml_etree_process    | 37.1 ms                                                     | 39.2 ms: 1.06x slower                                      |
| xml_etree_generate   | 52.2 ms                                                     | 56.8 ms: 1.09x slower                                      |
| unpickle_list        | 2.55 us                                                     | 2.77 us: 1.09x slower                                      |
| tomli_loads          | 1.41 sec                                                    | 1.61 sec: 1.14x slower                                     |
| Geometric mean       | (ref)                                                       | 1.01x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-pythonperf1-amd64-python-main-3.13.0a0-8c17729 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.5 ms: 1.02x faster                                      |
| python_startup         | 18.7 ms                                                     | 18.3 ms: 1.02x faster                                      |
| Geometric mean         | (ref)                                                       | 1.02x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-pythonperf1-amd64-python-main-3.13.0a0-8c17729 |
|-----------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 7.43 ms: 1.02x slower                                      |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-pythonperf1-amd64-python-main-3.13.0a0-8c17729 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 99.6 us: 3.23x faster                                      |
| asyncio_tcp              | 699 ms                                                      | 481 ms: 1.45x faster                                       |
| generators               | 33.8 ms                                                     | 24.2 ms: 1.39x faster                                      |
| json_dumps               | 7.56 ms                                                     | 5.75 ms: 1.31x faster                                      |
| json                     | 3.25 ms                                                     | 2.83 ms: 1.15x faster                                      |
| deltablue                | 2.61 ms                                                     | 2.28 ms: 1.15x faster                                      |
| raytrace                 | 211 ms                                                      | 186 ms: 1.14x faster                                       |
| mdp                      | 1.67 sec                                                    | 1.49 sec: 1.12x faster                                     |
| sqlglot_parse            | 952 us                                                      | 853 us: 1.12x faster                                       |
| unpack_sequence          | 46.1 ns                                                     | 42.2 ns: 1.09x faster                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.94 sec: 1.09x faster                                     |
| richards_super           | 37.5 ms                                                     | 34.7 ms: 1.08x faster                                      |
| chaos                    | 47.1 ms                                                     | 43.7 ms: 1.08x faster                                      |
| async_tree_none          | 320 ms                                                      | 297 ms: 1.08x faster                                       |
| sqlglot_transpile        | 1.16 ms                                                     | 1.08 ms: 1.07x faster                                      |
| logging_silent           | 69.8 ns                                                     | 65.1 ns: 1.07x faster                                      |
| async_tree_memoization   | 371 ms                                                      | 348 ms: 1.07x faster                                       |
| async_tree_io            | 779 ms                                                      | 733 ms: 1.06x faster                                       |
| crypto_pyaes             | 47.6 ms                                                     | 45.4 ms: 1.05x faster                                      |
| coverage                 | 55.9 ms                                                     | 53.4 ms: 1.05x faster                                      |
| unpickle_pure_python     | 152 us                                                      | 145 us: 1.05x faster                                       |
| mypy2                    | 229 ms                                                      | 219 ms: 1.04x faster                                       |
| hexiom                   | 4.55 ms                                                     | 4.38 ms: 1.04x faster                                      |
| comprehensions           | 15.9 us                                                     | 15.5 us: 1.03x faster                                      |
| bench_thread_pool        | 852 us                                                      | 829 us: 1.03x faster                                       |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 488 ms: 1.03x faster                                       |
| tornado_http             | 91.8 ms                                                     | 89.4 ms: 1.03x faster                                      |
| pickle_dict              | 18.5 us                                                     | 18.0 us: 1.03x faster                                      |
| python_startup_no_site   | 15.9 ms                                                     | 15.5 ms: 1.02x faster                                      |
| python_startup           | 18.7 ms                                                     | 18.3 ms: 1.02x faster                                      |
| xml_etree_parse          | 95.9 ms                                                     | 93.8 ms: 1.02x faster                                      |
| nqueens                  | 64.9 ms                                                     | 64.3 ms: 1.01x faster                                      |
| scimark_lu               | 63.5 ms                                                     | 63.0 ms: 1.01x faster                                      |
| dulwich_log              | 44.5 ms                                                     | 44.1 ms: 1.01x faster                                      |
| meteor_contest           | 74.7 ms                                                     | 75.0 ms: 1.00x slower                                      |
| richards                 | 30.6 ms                                                     | 30.7 ms: 1.00x slower                                      |
| pickle_pure_python       | 200 us                                                      | 201 us: 1.01x slower                                       |
| regex_v8                 | 13.8 ms                                                     | 14.0 ms: 1.01x slower                                      |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.60 ms: 1.01x slower                                      |
| deepcopy                 | 246 us                                                      | 248 us: 1.01x slower                                       |
| go                       | 97.3 ms                                                     | 98.3 ms: 1.01x slower                                      |
| pidigits                 | 148 ms                                                      | 150 ms: 1.01x slower                                       |
| pickle_list              | 2.68 us                                                     | 2.72 us: 1.01x slower                                      |
| scimark_monte_carlo      | 44.6 ms                                                     | 45.4 ms: 1.02x slower                                      |
| sqlglot_normalize        | 190 ms                                                      | 194 ms: 1.02x slower                                       |
| gc_traversal             | 1.46 ms                                                     | 1.49 ms: 1.02x slower                                      |
| mako                     | 7.26 ms                                                     | 7.43 ms: 1.02x slower                                      |
| float                    | 54.6 ms                                                     | 56.1 ms: 1.03x slower                                      |
| pyflate                  | 304 ms                                                      | 313 ms: 1.03x slower                                       |
| regex_compile            | 90.6 ms                                                     | 93.4 ms: 1.03x slower                                      |
| logging_simple           | 6.61 us                                                     | 6.84 us: 1.03x slower                                      |
| unpickle                 | 8.09 us                                                     | 8.38 us: 1.04x slower                                      |
| sqlglot_optimize         | 34.9 ms                                                     | 36.1 ms: 1.04x slower                                      |
| docutils                 | 1.60 sec                                                    | 1.66 sec: 1.04x slower                                     |
| pprint_safe_repr         | 512 ms                                                      | 533 ms: 1.04x slower                                       |
| regex_dna                | 115 ms                                                      | 120 ms: 1.04x slower                                       |
| logging_format           | 7.01 us                                                     | 7.33 us: 1.04x slower                                      |
| sqlite_synth             | 1.68 us                                                     | 1.76 us: 1.05x slower                                      |
| xml_etree_iterparse      | 62.6 ms                                                     | 65.6 ms: 1.05x slower                                      |
| coroutines               | 14.6 ms                                                     | 15.4 ms: 1.05x slower                                      |
| pprint_pformat           | 1.04 sec                                                    | 1.09 sec: 1.05x slower                                     |
| json_loads               | 12.9 us                                                     | 13.6 us: 1.05x slower                                      |
| create_gc_cycles         | 693 us                                                      | 730 us: 1.05x slower                                       |
| regex_effbot             | 1.50 ms                                                     | 1.58 ms: 1.06x slower                                      |
| pickle                   | 6.61 us                                                     | 6.98 us: 1.06x slower                                      |
| xml_etree_process        | 37.1 ms                                                     | 39.2 ms: 1.06x slower                                      |
| bench_mp_pool            | 62.5 ms                                                     | 66.3 ms: 1.06x slower                                      |
| pycparser                | 691 ms                                                      | 733 ms: 1.06x slower                                       |
| deepcopy_reduce          | 2.07 us                                                     | 2.21 us: 1.07x slower                                      |
| xml_etree_generate       | 52.2 ms                                                     | 56.8 ms: 1.09x slower                                      |
| unpickle_list            | 2.55 us                                                     | 2.77 us: 1.09x slower                                      |
| nbody                    | 70.0 ms                                                     | 76.8 ms: 1.10x slower                                      |
| scimark_fft              | 178 ms                                                      | 196 ms: 1.10x slower                                       |
| pathlib                  | 71.4 ms                                                     | 79.4 ms: 1.11x slower                                      |
| telco                    | 3.90 ms                                                     | 4.39 ms: 1.12x slower                                      |
| tomli_loads              | 1.41 sec                                                    | 1.61 sec: 1.14x slower                                     |
| scimark_sor              | 75.6 ms                                                     | 86.3 ms: 1.14x slower                                      |
| async_generators         | 178 ms                                                      | 247 ms: 1.39x slower                                       |
| dask                     | 264 ms                                                      | 382 ms: 1.45x slower                                       |
| Geometric mean           | (ref)                                                       | 1.01x faster                                               |

Benchmark hidden because not significant (3): spectral_norm, deepcopy_memo, fannkuch
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 83.59% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
