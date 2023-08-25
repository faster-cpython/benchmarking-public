
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 42f54d1
- commit date: 2023-05-06
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 207 ms: 1.01x faster                                        |
| docutils       | 1.60 sec                                                    | 1.58 sec: 1.01x faster                                      |
| tornado_http   | 91.8 ms                                                     | 88.3 ms: 1.04x faster                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 54.6 ms                                                     | 51.7 ms: 1.06x faster                                       |
| nbody          | 70.0 ms                                                     | 69.4 ms: 1.01x faster                                       |
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                       | 1.01x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 84.5 ms: 1.07x faster                                       |
| regex_v8       | 13.8 ms                                                     | 14.0 ms: 1.01x slower                                       |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                        |
| regex_effbot   | 1.50 ms                                                     | 1.62 ms: 1.08x slower                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.63 ms: 1.34x faster                                       |
| unpickle_pure_python | 152 us                                                      | 134 us: 1.14x faster                                        |
| pickle_pure_python   | 200 us                                                      | 190 us: 1.05x faster                                        |
| xml_etree_parse      | 95.9 ms                                                     | 92.1 ms: 1.04x faster                                       |
| pickle_dict          | 18.5 us                                                     | 18.1 us: 1.02x faster                                       |
| unpickle             | 8.09 us                                                     | 8.29 us: 1.02x slower                                       |
| xml_etree_process    | 37.1 ms                                                     | 38.2 ms: 1.03x slower                                       |
| pickle_list          | 2.68 us                                                     | 2.83 us: 1.06x slower                                       |
| pickle               | 6.61 us                                                     | 7.04 us: 1.07x slower                                       |
| xml_etree_generate   | 52.2 ms                                                     | 55.9 ms: 1.07x slower                                       |
| json_loads           | 12.9 us                                                     | 13.9 us: 1.08x slower                                       |
| unpickle_list        | 2.55 us                                                     | 2.86 us: 1.12x slower                                       |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.6 ms: 1.02x faster                                       |
| python_startup         | 18.7 ms                                                     | 18.4 ms: 1.01x faster                                       |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|-----------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 6.48 ms: 1.12x faster                                       |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| generators              | 33.8 ms                                                     | 20.3 ms: 1.67x faster                                       |
| asyncio_tcp             | 699 ms                                                      | 454 ms: 1.54x faster                                        |
| json_dumps              | 7.56 ms                                                     | 5.63 ms: 1.34x faster                                       |
| deltablue               | 2.61 ms                                                     | 2.04 ms: 1.28x faster                                       |
| richards                | 30.6 ms                                                     | 25.1 ms: 1.22x faster                                       |
| unpack_sequence         | 46.1 ns                                                     | 37.8 ns: 1.22x faster                                       |
| sqlglot_parse           | 952 us                                                      | 787 us: 1.21x faster                                        |
| logging_silent          | 69.8 ns                                                     | 58.0 ns: 1.20x faster                                       |
| mdp                     | 1.67 sec                                                    | 1.42 sec: 1.17x faster                                      |
| sqlglot_transpile       | 1.16 ms                                                     | 996 us: 1.17x faster                                        |
| hexiom                  | 4.55 ms                                                     | 3.95 ms: 1.15x faster                                       |
| raytrace                | 211 ms                                                      | 184 ms: 1.14x faster                                        |
| json                    | 3.25 ms                                                     | 2.85 ms: 1.14x faster                                       |
| unpickle_pure_python    | 152 us                                                      | 134 us: 1.14x faster                                        |
| go                      | 97.3 ms                                                     | 86.0 ms: 1.13x faster                                       |
| scimark_lu              | 63.5 ms                                                     | 56.4 ms: 1.13x faster                                       |
| mako                    | 7.26 ms                                                     | 6.48 ms: 1.12x faster                                       |
| nqueens                 | 64.9 ms                                                     | 57.9 ms: 1.12x faster                                       |
| spectral_norm           | 67.9 ms                                                     | 61.7 ms: 1.10x faster                                       |
| async_tree_io           | 779 ms                                                      | 716 ms: 1.09x faster                                        |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.39 ms: 1.08x faster                                       |
| chaos                   | 47.1 ms                                                     | 43.8 ms: 1.08x faster                                       |
| regex_compile           | 90.6 ms                                                     | 84.5 ms: 1.07x faster                                       |
| pyflate                 | 304 ms                                                      | 284 ms: 1.07x faster                                        |
| async_tree_cpu_io_mixed | 501 ms                                                      | 468 ms: 1.07x faster                                        |
| async_tree_none         | 320 ms                                                      | 300 ms: 1.07x faster                                        |
| dulwich_log             | 44.5 ms                                                     | 42.0 ms: 1.06x faster                                       |
| async_tree_memoization  | 371 ms                                                      | 351 ms: 1.06x faster                                        |
| mypy2                   | 229 ms                                                      | 217 ms: 1.06x faster                                        |
| float                   | 54.6 ms                                                     | 51.7 ms: 1.06x faster                                       |
| deepcopy                | 246 us                                                      | 233 us: 1.05x faster                                        |
| deepcopy_memo           | 25.2 us                                                     | 23.9 us: 1.05x faster                                       |
| coroutines              | 14.6 ms                                                     | 13.9 ms: 1.05x faster                                       |
| pickle_pure_python      | 200 us                                                      | 190 us: 1.05x faster                                        |
| xml_etree_parse         | 95.9 ms                                                     | 92.1 ms: 1.04x faster                                       |
| fannkuch                | 252 ms                                                      | 242 ms: 1.04x faster                                        |
| pycparser               | 691 ms                                                      | 664 ms: 1.04x faster                                        |
| tornado_http            | 91.8 ms                                                     | 88.3 ms: 1.04x faster                                       |
| coverage                | 55.9 ms                                                     | 53.8 ms: 1.04x faster                                       |
| scimark_monte_carlo     | 44.6 ms                                                     | 43.1 ms: 1.04x faster                                       |
| logging_simple          | 6.61 us                                                     | 6.39 us: 1.04x faster                                       |
| meteor_contest          | 74.7 ms                                                     | 72.6 ms: 1.03x faster                                       |
| crypto_pyaes            | 47.6 ms                                                     | 46.3 ms: 1.03x faster                                       |
| comprehensions          | 15.9 us                                                     | 15.5 us: 1.03x faster                                       |
| pickle_dict             | 18.5 us                                                     | 18.1 us: 1.02x faster                                       |
| bench_thread_pool       | 852 us                                                      | 837 us: 1.02x faster                                        |
| python_startup_no_site  | 15.9 ms                                                     | 15.6 ms: 1.02x faster                                       |
| scimark_fft             | 178 ms                                                      | 175 ms: 1.02x faster                                        |
| python_startup          | 18.7 ms                                                     | 18.4 ms: 1.01x faster                                       |
| docutils                | 1.60 sec                                                    | 1.58 sec: 1.01x faster                                      |
| logging_format          | 7.01 us                                                     | 6.94 us: 1.01x faster                                       |
| nbody                   | 70.0 ms                                                     | 69.4 ms: 1.01x faster                                       |
| 2to3                    | 209 ms                                                      | 207 ms: 1.01x faster                                        |
| pprint_pformat          | 1.04 sec                                                    | 1.03 sec: 1.01x faster                                      |
| regex_v8                | 13.8 ms                                                     | 14.0 ms: 1.01x slower                                       |
| sqlite_synth            | 1.68 us                                                     | 1.71 us: 1.02x slower                                       |
| pidigits                | 148 ms                                                      | 151 ms: 1.02x slower                                        |
| telco                   | 3.90 ms                                                     | 4.00 ms: 1.02x slower                                       |
| unpickle                | 8.09 us                                                     | 8.29 us: 1.02x slower                                       |
| xml_etree_process       | 37.1 ms                                                     | 38.2 ms: 1.03x slower                                       |
| regex_dna               | 115 ms                                                      | 119 ms: 1.03x slower                                        |
| scimark_sor             | 75.6 ms                                                     | 78.7 ms: 1.04x slower                                       |
| pickle_list             | 2.68 us                                                     | 2.83 us: 1.06x slower                                       |
| bench_mp_pool           | 62.5 ms                                                     | 66.3 ms: 1.06x slower                                       |
| pickle                  | 6.61 us                                                     | 7.04 us: 1.07x slower                                       |
| xml_etree_generate      | 52.2 ms                                                     | 55.9 ms: 1.07x slower                                       |
| json_loads              | 12.9 us                                                     | 13.9 us: 1.08x slower                                       |
| regex_effbot            | 1.50 ms                                                     | 1.62 ms: 1.08x slower                                       |
| unpickle_list           | 2.55 us                                                     | 2.86 us: 1.12x slower                                       |
| pathlib                 | 71.4 ms                                                     | 81.2 ms: 1.14x slower                                       |
| async_generators        | 178 ms                                                      | 235 ms: 1.33x slower                                        |
| dask                    | 264 ms                                                      | 360 ms: 1.36x slower                                        |
| Geometric mean          | (ref)                                                       | 1.05x faster                                                |

Benchmark hidden because not significant (7): pprint_safe_repr, gc_traversal, sqlglot_optimize, create_gc_cycles, deepcopy_reduce, sqlglot_normalize, xml_etree_iterparse
Ignored benchmarks (19) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
