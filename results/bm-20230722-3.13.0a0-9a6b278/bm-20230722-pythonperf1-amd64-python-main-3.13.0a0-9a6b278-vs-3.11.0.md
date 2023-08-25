
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 9a6b278
- commit date: 2023-07-22
- overall geometric mean: 1.02x faster
- HPT reliability: 71.75%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230722-pythonperf1-amd64-python-main-3.13.0a0-9a6b278 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| docutils       | 1.60 sec                                                    | 1.67 sec: 1.04x slower                                     |
| tornado_http   | 91.8 ms                                                     | 88.8 ms: 1.03x faster                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230722-pythonperf1-amd64-python-main-3.13.0a0-9a6b278 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                       |
| float          | 54.6 ms                                                     | 56.1 ms: 1.03x slower                                      |
| nbody          | 70.0 ms                                                     | 77.9 ms: 1.11x slower                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230722-pythonperf1-amd64-python-main-3.13.0a0-9a6b278 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 93.1 ms: 1.03x slower                                      |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                       |
| regex_effbot   | 1.50 ms                                                     | 1.57 ms: 1.05x slower                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230722-pythonperf1-amd64-python-main-3.13.0a0-9a6b278 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.75 ms: 1.31x faster                                      |
| unpickle_pure_python | 152 us                                                      | 143 us: 1.06x faster                                       |
| xml_etree_parse      | 95.9 ms                                                     | 91.5 ms: 1.05x faster                                      |
| pickle_pure_python   | 200 us                                                      | 199 us: 1.00x faster                                       |
| unpickle             | 8.09 us                                                     | 8.28 us: 1.02x slower                                      |
| xml_etree_iterparse  | 62.6 ms                                                     | 64.2 ms: 1.03x slower                                      |
| pickle_list          | 2.68 us                                                     | 2.78 us: 1.04x slower                                      |
| json_loads           | 12.9 us                                                     | 13.6 us: 1.05x slower                                      |
| xml_etree_process    | 37.1 ms                                                     | 39.1 ms: 1.05x slower                                      |
| pickle               | 6.61 us                                                     | 7.07 us: 1.07x slower                                      |
| xml_etree_generate   | 52.2 ms                                                     | 56.6 ms: 1.08x slower                                      |
| unpickle_list        | 2.55 us                                                     | 2.77 us: 1.09x slower                                      |
| tomli_loads          | 1.41 sec                                                    | 1.61 sec: 1.14x slower                                     |
| Geometric mean       | (ref)                                                       | 1.01x slower                                               |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230722-pythonperf1-amd64-python-main-3.13.0a0-9a6b278 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.6 ms: 1.02x faster                                      |
| Geometric mean         | (ref)                                                       | 1.01x faster                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230722-pythonperf1-amd64-python-main-3.13.0a0-9a6b278 |
|-----------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 7.62 ms: 1.05x slower                                      |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230722-pythonperf1-amd64-python-main-3.13.0a0-9a6b278 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 95.2 us: 3.38x faster                                      |
| asyncio_tcp              | 699 ms                                                      | 479 ms: 1.46x faster                                       |
| generators               | 33.8 ms                                                     | 24.2 ms: 1.40x faster                                      |
| json_dumps               | 7.56 ms                                                     | 5.75 ms: 1.31x faster                                      |
| unpack_sequence          | 46.1 ns                                                     | 39.6 ns: 1.16x faster                                      |
| mdp                      | 1.67 sec                                                    | 1.45 sec: 1.15x faster                                     |
| deltablue                | 2.61 ms                                                     | 2.29 ms: 1.14x faster                                      |
| raytrace                 | 211 ms                                                      | 187 ms: 1.13x faster                                       |
| json                     | 3.25 ms                                                     | 2.91 ms: 1.12x faster                                      |
| sqlglot_parse            | 952 us                                                      | 852 us: 1.12x faster                                       |
| chaos                    | 47.1 ms                                                     | 43.3 ms: 1.09x faster                                      |
| sqlglot_transpile        | 1.16 ms                                                     | 1.08 ms: 1.08x faster                                      |
| richards_super           | 37.5 ms                                                     | 34.7 ms: 1.08x faster                                      |
| async_tree_none          | 320 ms                                                      | 297 ms: 1.08x faster                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.97 sec: 1.07x faster                                     |
| logging_silent           | 69.8 ns                                                     | 65.4 ns: 1.07x faster                                      |
| comprehensions           | 15.9 us                                                     | 15.0 us: 1.06x faster                                      |
| unpickle_pure_python     | 152 us                                                      | 143 us: 1.06x faster                                       |
| async_tree_memoization   | 371 ms                                                      | 349 ms: 1.06x faster                                       |
| async_tree_io            | 779 ms                                                      | 740 ms: 1.05x faster                                       |
| xml_etree_parse          | 95.9 ms                                                     | 91.5 ms: 1.05x faster                                      |
| coverage                 | 55.9 ms                                                     | 53.7 ms: 1.04x faster                                      |
| nqueens                  | 64.9 ms                                                     | 62.4 ms: 1.04x faster                                      |
| mypy2                    | 229 ms                                                      | 221 ms: 1.04x faster                                       |
| tornado_http             | 91.8 ms                                                     | 88.8 ms: 1.03x faster                                      |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 487 ms: 1.03x faster                                       |
| hexiom                   | 4.55 ms                                                     | 4.43 ms: 1.03x faster                                      |
| bench_thread_pool        | 852 us                                                      | 831 us: 1.03x faster                                       |
| python_startup_no_site   | 15.9 ms                                                     | 15.6 ms: 1.02x faster                                      |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.52 ms: 1.02x faster                                      |
| crypto_pyaes             | 47.6 ms                                                     | 46.8 ms: 1.02x faster                                      |
| scimark_lu               | 63.5 ms                                                     | 62.9 ms: 1.01x faster                                      |
| pickle_pure_python       | 200 us                                                      | 199 us: 1.00x faster                                       |
| richards                 | 30.6 ms                                                     | 30.7 ms: 1.00x slower                                      |
| sqlglot_normalize        | 190 ms                                                      | 191 ms: 1.01x slower                                       |
| go                       | 97.3 ms                                                     | 98.4 ms: 1.01x slower                                      |
| pidigits                 | 148 ms                                                      | 150 ms: 1.01x slower                                       |
| fannkuch                 | 252 ms                                                      | 258 ms: 1.02x slower                                       |
| sqlglot_optimize         | 34.9 ms                                                     | 35.7 ms: 1.02x slower                                      |
| unpickle                 | 8.09 us                                                     | 8.28 us: 1.02x slower                                      |
| xml_etree_iterparse      | 62.6 ms                                                     | 64.2 ms: 1.03x slower                                      |
| regex_compile            | 90.6 ms                                                     | 93.1 ms: 1.03x slower                                      |
| float                    | 54.6 ms                                                     | 56.1 ms: 1.03x slower                                      |
| gc_traversal             | 1.46 ms                                                     | 1.50 ms: 1.03x slower                                      |
| coroutines               | 14.6 ms                                                     | 15.1 ms: 1.03x slower                                      |
| regex_dna                | 115 ms                                                      | 119 ms: 1.03x slower                                       |
| pickle_list              | 2.68 us                                                     | 2.78 us: 1.04x slower                                      |
| sqlite_synth             | 1.68 us                                                     | 1.74 us: 1.04x slower                                      |
| scimark_fft              | 178 ms                                                      | 185 ms: 1.04x slower                                       |
| logging_simple           | 6.61 us                                                     | 6.88 us: 1.04x slower                                      |
| create_gc_cycles         | 693 us                                                      | 721 us: 1.04x slower                                       |
| docutils                 | 1.60 sec                                                    | 1.67 sec: 1.04x slower                                     |
| pprint_safe_repr         | 512 ms                                                      | 533 ms: 1.04x slower                                       |
| mako                     | 7.26 ms                                                     | 7.62 ms: 1.05x slower                                      |
| logging_format           | 7.01 us                                                     | 7.36 us: 1.05x slower                                      |
| pprint_pformat           | 1.04 sec                                                    | 1.09 sec: 1.05x slower                                     |
| regex_effbot             | 1.50 ms                                                     | 1.57 ms: 1.05x slower                                      |
| json_loads               | 12.9 us                                                     | 13.6 us: 1.05x slower                                      |
| pyflate                  | 304 ms                                                      | 320 ms: 1.05x slower                                       |
| xml_etree_process        | 37.1 ms                                                     | 39.1 ms: 1.05x slower                                      |
| deepcopy_reduce          | 2.07 us                                                     | 2.20 us: 1.06x slower                                      |
| pycparser                | 691 ms                                                      | 735 ms: 1.06x slower                                       |
| bench_mp_pool            | 62.5 ms                                                     | 66.6 ms: 1.07x slower                                      |
| pickle                   | 6.61 us                                                     | 7.07 us: 1.07x slower                                      |
| xml_etree_generate       | 52.2 ms                                                     | 56.6 ms: 1.08x slower                                      |
| unpickle_list            | 2.55 us                                                     | 2.77 us: 1.09x slower                                      |
| scimark_sor              | 75.6 ms                                                     | 82.4 ms: 1.09x slower                                      |
| nbody                    | 70.0 ms                                                     | 77.9 ms: 1.11x slower                                      |
| pathlib                  | 71.4 ms                                                     | 80.2 ms: 1.12x slower                                      |
| tomli_loads              | 1.41 sec                                                    | 1.61 sec: 1.14x slower                                     |
| telco                    | 3.90 ms                                                     | 4.53 ms: 1.16x slower                                      |
| async_generators         | 178 ms                                                      | 240 ms: 1.35x slower                                       |
| dask                     | 264 ms                                                      | 381 ms: 1.44x slower                                       |
| Geometric mean           | (ref)                                                       | 1.02x faster                                               |

Benchmark hidden because not significant (9): python_startup, scimark_monte_carlo, meteor_contest, dulwich_log, pickle_dict, spectral_norm, deepcopy, deepcopy_memo, regex_v8
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 71.75% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
