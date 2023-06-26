
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: windows-amd64
- commit hash: 9cd3664
- commit date: 2023-06-24
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230624-pythonperf1-amd64-python-3.12-3.12.0b3+-9cd3664 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 217 ms: 1.04x slower                                        |
| docutils       | 1.60 sec                                                    | 1.66 sec: 1.04x slower                                      |
| tornado_http   | 91.8 ms                                                     | 89.0 ms: 1.03x faster                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230624-pythonperf1-amd64-python-3.12-3.12.0b3+-9cd3664 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 153 ms: 1.03x slower                                        |
| Geometric mean | (ref)                                                       | 1.01x slower                                                |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230624-pythonperf1-amd64-python-3.12-3.12.0b3+-9cd3664 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 88.3 ms: 1.03x faster                                       |
| regex_v8       | 13.8 ms                                                     | 14.1 ms: 1.02x slower                                       |
| regex_dna      | 115 ms                                                      | 125 ms: 1.08x slower                                        |
| regex_effbot   | 1.50 ms                                                     | 2.01 ms: 1.34x slower                                       |
| Geometric mean | (ref)                                                       | 1.10x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230624-pythonperf1-amd64-python-3.12-3.12.0b3+-9cd3664 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.86 ms: 1.29x faster                                       |
| unpickle_pure_python | 152 us                                                      | 135 us: 1.13x faster                                        |
| xml_etree_parse      | 95.9 ms                                                     | 92.5 ms: 1.04x faster                                       |
| pickle_pure_python   | 200 us                                                      | 197 us: 1.01x faster                                        |
| tomli_loads          | 1.41 sec                                                    | 1.42 sec: 1.01x slower                                      |
| xml_etree_iterparse  | 62.6 ms                                                     | 63.6 ms: 1.02x slower                                       |
| xml_etree_process    | 37.1 ms                                                     | 38.5 ms: 1.04x slower                                       |
| xml_etree_generate   | 52.2 ms                                                     | 55.6 ms: 1.06x slower                                       |
| pickle               | 6.61 us                                                     | 7.16 us: 1.08x slower                                       |
| unpickle             | 8.09 us                                                     | 8.82 us: 1.09x slower                                       |
| pickle_list          | 2.68 us                                                     | 2.97 us: 1.11x slower                                       |
| json_loads           | 12.9 us                                                     | 14.4 us: 1.12x slower                                       |
| unpickle_list        | 2.55 us                                                     | 2.84 us: 1.12x slower                                       |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230624-pythonperf1-amd64-python-3.12-3.12.0b3+-9cd3664 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 18.7 ms                                                     | 20.3 ms: 1.08x slower                                       |
| python_startup_no_site | 15.9 ms                                                     | 17.3 ms: 1.09x slower                                       |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230624-pythonperf1-amd64-python-3.12-3.12.0b3+-9cd3664 |
|-----------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 7.10 ms: 1.02x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230624-pythonperf1-amd64-python-3.12-3.12.0b3+-9cd3664 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 95.9 us: 3.36x faster                                       |
| generators               | 33.8 ms                                                     | 22.7 ms: 1.49x faster                                       |
| asyncio_tcp              | 699 ms                                                      | 497 ms: 1.41x faster                                        |
| json_dumps               | 7.56 ms                                                     | 5.86 ms: 1.29x faster                                       |
| deltablue                | 2.61 ms                                                     | 2.06 ms: 1.27x faster                                       |
| richards_super           | 37.5 ms                                                     | 29.7 ms: 1.26x faster                                       |
| mdp                      | 1.67 sec                                                    | 1.38 sec: 1.21x faster                                      |
| unpack_sequence          | 46.1 ns                                                     | 38.1 ns: 1.21x faster                                       |
| sqlglot_parse            | 952 us                                                      | 791 us: 1.20x faster                                        |
| logging_silent           | 69.8 ns                                                     | 59.5 ns: 1.17x faster                                       |
| richards                 | 30.6 ms                                                     | 26.2 ms: 1.17x faster                                       |
| raytrace                 | 211 ms                                                      | 185 ms: 1.14x faster                                        |
| sqlglot_transpile        | 1.16 ms                                                     | 1.02 ms: 1.14x faster                                       |
| unpickle_pure_python     | 152 us                                                      | 135 us: 1.13x faster                                        |
| chaos                    | 47.1 ms                                                     | 41.9 ms: 1.12x faster                                       |
| comprehensions           | 15.9 us                                                     | 14.3 us: 1.11x faster                                       |
| go                       | 97.3 ms                                                     | 88.0 ms: 1.11x faster                                       |
| coverage                 | 55.9 ms                                                     | 50.6 ms: 1.10x faster                                       |
| async_tree_none          | 320 ms                                                      | 291 ms: 1.10x faster                                        |
| scimark_lu               | 63.5 ms                                                     | 57.9 ms: 1.10x faster                                       |
| hexiom                   | 4.55 ms                                                     | 4.17 ms: 1.09x faster                                       |
| json                     | 3.25 ms                                                     | 3.01 ms: 1.08x faster                                       |
| async_tree_memoization   | 371 ms                                                      | 345 ms: 1.08x faster                                        |
| async_tree_io            | 779 ms                                                      | 727 ms: 1.07x faster                                        |
| mypy2                    | 229 ms                                                      | 217 ms: 1.06x faster                                        |
| deepcopy                 | 246 us                                                      | 233 us: 1.05x faster                                        |
| nqueens                  | 64.9 ms                                                     | 62.2 ms: 1.04x faster                                       |
| scimark_monte_carlo      | 44.6 ms                                                     | 43.0 ms: 1.04x faster                                       |
| xml_etree_parse          | 95.9 ms                                                     | 92.5 ms: 1.04x faster                                       |
| sqlglot_normalize        | 190 ms                                                      | 184 ms: 1.03x faster                                        |
| tornado_http             | 91.8 ms                                                     | 89.0 ms: 1.03x faster                                       |
| regex_compile            | 90.6 ms                                                     | 88.3 ms: 1.03x faster                                       |
| mako                     | 7.26 ms                                                     | 7.10 ms: 1.02x faster                                       |
| deepcopy_memo            | 25.2 us                                                     | 24.7 us: 1.02x faster                                       |
| fannkuch                 | 252 ms                                                      | 248 ms: 1.02x faster                                        |
| pyflate                  | 304 ms                                                      | 300 ms: 1.01x faster                                        |
| pickle_pure_python       | 200 us                                                      | 197 us: 1.01x faster                                        |
| crypto_pyaes             | 47.6 ms                                                     | 46.9 ms: 1.01x faster                                       |
| coroutines               | 14.6 ms                                                     | 14.5 ms: 1.01x faster                                       |
| sqlglot_optimize         | 34.9 ms                                                     | 34.6 ms: 1.01x faster                                       |
| meteor_contest           | 74.7 ms                                                     | 74.1 ms: 1.01x faster                                       |
| tomli_loads              | 1.41 sec                                                    | 1.42 sec: 1.01x slower                                      |
| deepcopy_reduce          | 2.07 us                                                     | 2.09 us: 1.01x slower                                       |
| logging_format           | 7.01 us                                                     | 7.07 us: 1.01x slower                                       |
| xml_etree_iterparse      | 62.6 ms                                                     | 63.6 ms: 1.02x slower                                       |
| regex_v8                 | 13.8 ms                                                     | 14.1 ms: 1.02x slower                                       |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.63 ms: 1.02x slower                                       |
| pycparser                | 691 ms                                                      | 710 ms: 1.03x slower                                        |
| bench_thread_pool        | 852 us                                                      | 877 us: 1.03x slower                                        |
| dulwich_log              | 44.5 ms                                                     | 46.0 ms: 1.03x slower                                       |
| pidigits                 | 148 ms                                                      | 153 ms: 1.03x slower                                        |
| 2to3                     | 209 ms                                                      | 217 ms: 1.04x slower                                        |
| docutils                 | 1.60 sec                                                    | 1.66 sec: 1.04x slower                                      |
| xml_etree_process        | 37.1 ms                                                     | 38.5 ms: 1.04x slower                                       |
| scimark_fft              | 178 ms                                                      | 186 ms: 1.04x slower                                        |
| gc_traversal             | 1.46 ms                                                     | 1.54 ms: 1.05x slower                                       |
| xml_etree_generate       | 52.2 ms                                                     | 55.6 ms: 1.06x slower                                       |
| telco                    | 3.90 ms                                                     | 4.20 ms: 1.08x slower                                       |
| create_gc_cycles         | 693 us                                                      | 749 us: 1.08x slower                                        |
| pickle                   | 6.61 us                                                     | 7.16 us: 1.08x slower                                       |
| python_startup           | 18.7 ms                                                     | 20.3 ms: 1.08x slower                                       |
| regex_dna                | 115 ms                                                      | 125 ms: 1.08x slower                                        |
| scimark_sor              | 75.6 ms                                                     | 82.1 ms: 1.09x slower                                       |
| python_startup_no_site   | 15.9 ms                                                     | 17.3 ms: 1.09x slower                                       |
| unpickle                 | 8.09 us                                                     | 8.82 us: 1.09x slower                                       |
| sqlite_synth             | 1.68 us                                                     | 1.85 us: 1.10x slower                                       |
| bench_mp_pool            | 62.5 ms                                                     | 68.9 ms: 1.10x slower                                       |
| pickle_list              | 2.68 us                                                     | 2.97 us: 1.11x slower                                       |
| json_loads               | 12.9 us                                                     | 14.4 us: 1.12x slower                                       |
| unpickle_list            | 2.55 us                                                     | 2.84 us: 1.12x slower                                       |
| pathlib                  | 71.4 ms                                                     | 82.2 ms: 1.15x slower                                       |
| async_generators         | 178 ms                                                      | 232 ms: 1.30x slower                                        |
| regex_effbot             | 1.50 ms                                                     | 2.01 ms: 1.34x slower                                       |
| dask                     | 264 ms                                                      | 369 ms: 1.40x slower                                        |
| Geometric mean           | (ref)                                                       | 1.03x faster                                                |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed, aiohttp, float, pickle_dict, logging_simple, pprint_safe_repr, spectral_norm, pprint_pformat, nbody, asyncio_tcp_ssl
Ignored benchmarks (14) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
