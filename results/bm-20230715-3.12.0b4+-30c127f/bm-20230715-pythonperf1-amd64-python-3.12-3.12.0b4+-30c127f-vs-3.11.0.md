
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: windows-amd64
- commit hash: 30c127f
- commit date: 2023-07-15
- overall geometric mean: 1.05x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-pythonperf1-amd64-python-3.12-3.12.0b4+-30c127f |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| tornado_http   | 91.8 ms                                                     | 86.4 ms: 1.06x faster                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-pythonperf1-amd64-python-3.12-3.12.0b4+-30c127f |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 54.6 ms                                                     | 53.3 ms: 1.03x faster                                       |
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                        |
| nbody          | 70.0 ms                                                     | 70.6 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                       | 1.00x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-pythonperf1-amd64-python-3.12-3.12.0b4+-30c127f |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 87.4 ms: 1.04x faster                                       |
| regex_v8       | 13.8 ms                                                     | 13.8 ms: 1.00x faster                                       |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                        |
| regex_effbot   | 1.50 ms                                                     | 1.59 ms: 1.06x slower                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-pythonperf1-amd64-python-3.12-3.12.0b4+-30c127f |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.71 ms: 1.32x faster                                       |
| unpickle_pure_python | 152 us                                                      | 134 us: 1.13x faster                                        |
| xml_etree_parse      | 95.9 ms                                                     | 89.3 ms: 1.07x faster                                       |
| tomli_loads          | 1.41 sec                                                    | 1.38 sec: 1.02x faster                                      |
| pickle_pure_python   | 200 us                                                      | 196 us: 1.02x faster                                        |
| unpickle             | 8.09 us                                                     | 8.19 us: 1.01x slower                                       |
| xml_etree_process    | 37.1 ms                                                     | 38.0 ms: 1.02x slower                                       |
| json_loads           | 12.9 us                                                     | 13.6 us: 1.05x slower                                       |
| xml_etree_generate   | 52.2 ms                                                     | 55.1 ms: 1.06x slower                                       |
| pickle_list          | 2.68 us                                                     | 2.84 us: 1.06x slower                                       |
| pickle               | 6.61 us                                                     | 7.03 us: 1.06x slower                                       |
| unpickle_list        | 2.55 us                                                     | 2.82 us: 1.11x slower                                       |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                |

Benchmark hidden because not significant (2): pickle_dict, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-pythonperf1-amd64-python-3.12-3.12.0b4+-30c127f |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.5 ms: 1.02x faster                                       |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-pythonperf1-amd64-python-3.12-3.12.0b4+-30c127f |
|-----------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 6.65 ms: 1.09x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230715-pythonperf1-amd64-python-3.12-3.12.0b4+-30c127f |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 95.7 us: 3.36x faster                                       |
| generators               | 33.8 ms                                                     | 22.1 ms: 1.53x faster                                       |
| asyncio_tcp              | 699 ms                                                      | 477 ms: 1.46x faster                                        |
| json_dumps               | 7.56 ms                                                     | 5.71 ms: 1.32x faster                                       |
| deltablue                | 2.61 ms                                                     | 2.10 ms: 1.24x faster                                       |
| richards_super           | 37.5 ms                                                     | 30.6 ms: 1.23x faster                                       |
| mdp                      | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                      |
| sqlglot_parse            | 952 us                                                      | 813 us: 1.17x faster                                        |
| unpack_sequence          | 46.1 ns                                                     | 39.3 ns: 1.17x faster                                       |
| logging_silent           | 69.8 ns                                                     | 61.4 ns: 1.14x faster                                       |
| sqlglot_transpile        | 1.16 ms                                                     | 1.02 ms: 1.14x faster                                       |
| raytrace                 | 211 ms                                                      | 186 ms: 1.13x faster                                        |
| unpickle_pure_python     | 152 us                                                      | 134 us: 1.13x faster                                        |
| richards                 | 30.6 ms                                                     | 27.1 ms: 1.13x faster                                       |
| comprehensions           | 15.9 us                                                     | 14.1 us: 1.13x faster                                       |
| async_tree_none          | 320 ms                                                      | 284 ms: 1.13x faster                                        |
| async_tree_memoization   | 371 ms                                                      | 330 ms: 1.12x faster                                        |
| async_tree_io            | 779 ms                                                      | 694 ms: 1.12x faster                                        |
| json                     | 3.25 ms                                                     | 2.91 ms: 1.12x faster                                       |
| coverage                 | 55.9 ms                                                     | 50.7 ms: 1.10x faster                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.92 sec: 1.10x faster                                      |
| hexiom                   | 4.55 ms                                                     | 4.14 ms: 1.10x faster                                       |
| mypy2                    | 229 ms                                                      | 209 ms: 1.09x faster                                        |
| mako                     | 7.26 ms                                                     | 6.65 ms: 1.09x faster                                       |
| chaos                    | 47.1 ms                                                     | 43.2 ms: 1.09x faster                                       |
| go                       | 97.3 ms                                                     | 89.4 ms: 1.09x faster                                       |
| xml_etree_parse          | 95.9 ms                                                     | 89.3 ms: 1.07x faster                                       |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 468 ms: 1.07x faster                                        |
| nqueens                  | 64.9 ms                                                     | 60.9 ms: 1.07x faster                                       |
| scimark_lu               | 63.5 ms                                                     | 59.7 ms: 1.06x faster                                       |
| sqlglot_normalize        | 190 ms                                                      | 179 ms: 1.06x faster                                        |
| tornado_http             | 91.8 ms                                                     | 86.4 ms: 1.06x faster                                       |
| aiohttp                  | 899 us                                                      | 847 us: 1.06x faster                                        |
| dulwich_log              | 44.5 ms                                                     | 42.5 ms: 1.05x faster                                       |
| sqlglot_optimize         | 34.9 ms                                                     | 33.6 ms: 1.04x faster                                       |
| coroutines               | 14.6 ms                                                     | 14.1 ms: 1.04x faster                                       |
| regex_compile            | 90.6 ms                                                     | 87.4 ms: 1.04x faster                                       |
| pycparser                | 691 ms                                                      | 668 ms: 1.03x faster                                        |
| deepcopy                 | 246 us                                                      | 238 us: 1.03x faster                                        |
| bench_thread_pool        | 852 us                                                      | 831 us: 1.03x faster                                        |
| float                    | 54.6 ms                                                     | 53.3 ms: 1.03x faster                                       |
| deepcopy_memo            | 25.2 us                                                     | 24.6 us: 1.02x faster                                       |
| tomli_loads              | 1.41 sec                                                    | 1.38 sec: 1.02x faster                                      |
| python_startup_no_site   | 15.9 ms                                                     | 15.5 ms: 1.02x faster                                       |
| logging_simple           | 6.61 us                                                     | 6.47 us: 1.02x faster                                       |
| pickle_pure_python       | 200 us                                                      | 196 us: 1.02x faster                                        |
| scimark_monte_carlo      | 44.6 ms                                                     | 43.8 ms: 1.02x faster                                       |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.53 ms: 1.02x faster                                       |
| pyflate                  | 304 ms                                                      | 300 ms: 1.01x faster                                        |
| meteor_contest           | 74.7 ms                                                     | 73.9 ms: 1.01x faster                                       |
| logging_format           | 7.01 us                                                     | 6.97 us: 1.01x faster                                       |
| regex_v8                 | 13.8 ms                                                     | 13.8 ms: 1.00x faster                                       |
| pidigits                 | 148 ms                                                      | 150 ms: 1.01x slower                                        |
| nbody                    | 70.0 ms                                                     | 70.6 ms: 1.01x slower                                       |
| unpickle                 | 8.09 us                                                     | 8.19 us: 1.01x slower                                       |
| deepcopy_reduce          | 2.07 us                                                     | 2.11 us: 1.02x slower                                       |
| scimark_fft              | 178 ms                                                      | 181 ms: 1.02x slower                                        |
| xml_etree_process        | 37.1 ms                                                     | 38.0 ms: 1.02x slower                                       |
| crypto_pyaes             | 47.6 ms                                                     | 48.9 ms: 1.03x slower                                       |
| regex_dna                | 115 ms                                                      | 119 ms: 1.03x slower                                        |
| sqlite_synth             | 1.68 us                                                     | 1.74 us: 1.03x slower                                       |
| telco                    | 3.90 ms                                                     | 4.05 ms: 1.04x slower                                       |
| create_gc_cycles         | 693 us                                                      | 722 us: 1.04x slower                                        |
| json_loads               | 12.9 us                                                     | 13.6 us: 1.05x slower                                       |
| xml_etree_generate       | 52.2 ms                                                     | 55.1 ms: 1.06x slower                                       |
| pickle_list              | 2.68 us                                                     | 2.84 us: 1.06x slower                                       |
| regex_effbot             | 1.50 ms                                                     | 1.59 ms: 1.06x slower                                       |
| pickle                   | 6.61 us                                                     | 7.03 us: 1.06x slower                                       |
| bench_mp_pool            | 62.5 ms                                                     | 67.0 ms: 1.07x slower                                       |
| unpickle_list            | 2.55 us                                                     | 2.82 us: 1.11x slower                                       |
| pathlib                  | 71.4 ms                                                     | 79.1 ms: 1.11x slower                                       |
| scimark_sor              | 75.6 ms                                                     | 83.9 ms: 1.11x slower                                       |
| async_generators         | 178 ms                                                      | 227 ms: 1.28x slower                                        |
| dask                     | 264 ms                                                      | 362 ms: 1.37x slower                                        |
| Geometric mean           | (ref)                                                       | 1.05x faster                                                |

Benchmark hidden because not significant (10): pickle_dict, python_startup, pprint_pformat, pprint_safe_repr, fannkuch, docutils, gc_traversal, spectral_norm, 2to3, xml_etree_iterparse
Ignored benchmarks (14) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
