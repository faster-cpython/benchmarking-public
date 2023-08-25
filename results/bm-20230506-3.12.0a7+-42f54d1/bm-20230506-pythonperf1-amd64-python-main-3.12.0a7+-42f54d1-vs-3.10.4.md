
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 42f54d1
- commit date: 2023-05-06
- overall geometric mean: 1.17x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 207 ms: 1.14x faster                                        |
| docutils       | 1.89 sec                                                    | 1.58 sec: 1.19x faster                                      |
| tornado_http   | 109 ms                                                      | 88.3 ms: 1.24x faster                                       |
| Geometric mean | (ref)                                                       | 1.19x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 51.7 ms: 1.16x faster                                       |
| pidigits       | 145 ms                                                      | 151 ms: 1.04x slower                                        |
| Geometric mean | (ref)                                                       | 1.04x faster                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 84.5 ms: 1.22x faster                                       |
| regex_dna      | 132 ms                                                      | 119 ms: 1.10x faster                                        |
| regex_v8       | 15.0 ms                                                     | 14.0 ms: 1.08x faster                                       |
| regex_effbot   | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.63 ms: 1.51x faster                                       |
| pickle_pure_python   | 257 us                                                      | 190 us: 1.35x faster                                        |
| unpickle_pure_python | 171 us                                                      | 134 us: 1.28x faster                                        |
| xml_etree_process    | 43.4 ms                                                     | 38.2 ms: 1.14x faster                                       |
| unpickle             | 9.17 us                                                     | 8.29 us: 1.11x faster                                       |
| xml_etree_parse      | 102 ms                                                      | 92.1 ms: 1.11x faster                                       |
| json_loads           | 14.2 us                                                     | 13.9 us: 1.02x faster                                       |
| unpickle_list        | 2.81 us                                                     | 2.86 us: 1.02x slower                                       |
| xml_etree_generate   | 54.5 ms                                                     | 55.9 ms: 1.03x slower                                       |
| pickle               | 6.80 us                                                     | 7.04 us: 1.04x slower                                       |
| pickle_dict          | 16.9 us                                                     | 18.1 us: 1.07x slower                                       |
| pickle_list          | 2.59 us                                                     | 2.83 us: 1.09x slower                                       |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup | 20.0 ms                                                     | 18.4 ms: 1.09x faster                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|-----------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 6.48 ms: 1.36x faster                                       |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-pythonperf1-amd64-python-main-3.12.0a7+-42f54d1 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.04 ms: 2.04x faster                                       |
| logging_silent          | 96.4 ns                                                     | 58.0 ns: 1.66x faster                                       |
| richards                | 41.2 ms                                                     | 25.1 ms: 1.64x faster                                       |
| mypy2                   | 352 ms                                                      | 217 ms: 1.62x faster                                        |
| go                      | 136 ms                                                      | 86.0 ms: 1.58x faster                                       |
| asyncio_tcp             | 712 ms                                                      | 454 ms: 1.57x faster                                        |
| generators              | 31.6 ms                                                     | 20.3 ms: 1.56x faster                                       |
| sqlglot_parse           | 1.22 ms                                                     | 787 us: 1.55x faster                                        |
| scimark_lu              | 85.4 ms                                                     | 56.4 ms: 1.51x faster                                       |
| json_dumps              | 8.50 ms                                                     | 5.63 ms: 1.51x faster                                       |
| async_tree_io           | 1.07 sec                                                    | 716 ms: 1.49x faster                                        |
| raytrace                | 271 ms                                                      | 184 ms: 1.47x faster                                        |
| sqlglot_transpile       | 1.46 ms                                                     | 996 us: 1.47x faster                                        |
| async_tree_memoization  | 497 ms                                                      | 351 ms: 1.42x faster                                        |
| async_tree_none         | 420 ms                                                      | 300 ms: 1.40x faster                                        |
| hexiom                  | 5.52 ms                                                     | 3.95 ms: 1.40x faster                                       |
| pyflate                 | 387 ms                                                      | 284 ms: 1.36x faster                                        |
| mako                    | 8.80 ms                                                     | 6.48 ms: 1.36x faster                                       |
| pickle_pure_python      | 257 us                                                      | 190 us: 1.35x faster                                        |
| crypto_pyaes            | 62.3 ms                                                     | 46.3 ms: 1.35x faster                                       |
| chaos                   | 58.9 ms                                                     | 43.8 ms: 1.34x faster                                       |
| scimark_sor             | 105 ms                                                      | 78.7 ms: 1.33x faster                                       |
| pycparser               | 868 ms                                                      | 664 ms: 1.31x faster                                        |
| async_tree_cpu_io_mixed | 609 ms                                                      | 468 ms: 1.30x faster                                        |
| scimark_monte_carlo     | 55.9 ms                                                     | 43.1 ms: 1.30x faster                                       |
| unpickle_pure_python    | 171 us                                                      | 134 us: 1.28x faster                                        |
| spectral_norm           | 78.0 ms                                                     | 61.7 ms: 1.26x faster                                       |
| tornado_http            | 109 ms                                                      | 88.3 ms: 1.24x faster                                       |
| regex_compile           | 103 ms                                                      | 84.5 ms: 1.22x faster                                       |
| mdp                     | 1.71 sec                                                    | 1.42 sec: 1.21x faster                                      |
| docutils                | 1.89 sec                                                    | 1.58 sec: 1.19x faster                                      |
| deepcopy_memo           | 28.5 us                                                     | 23.9 us: 1.19x faster                                       |
| pprint_pformat          | 1.21 sec                                                    | 1.03 sec: 1.17x faster                                      |
| float                   | 60.2 ms                                                     | 51.7 ms: 1.16x faster                                       |
| nqueens                 | 67.0 ms                                                     | 57.9 ms: 1.16x faster                                       |
| pprint_safe_repr        | 589 ms                                                      | 509 ms: 1.16x faster                                        |
| coroutines              | 15.9 ms                                                     | 13.9 ms: 1.15x faster                                       |
| 2to3                    | 237 ms                                                      | 207 ms: 1.14x faster                                        |
| xml_etree_process       | 43.4 ms                                                     | 38.2 ms: 1.14x faster                                       |
| dulwich_log             | 47.6 ms                                                     | 42.0 ms: 1.13x faster                                       |
| bench_thread_pool       | 946 us                                                      | 837 us: 1.13x faster                                        |
| create_gc_cycles        | 782 us                                                      | 693 us: 1.13x faster                                        |
| sqlglot_optimize        | 39.0 ms                                                     | 34.9 ms: 1.12x faster                                       |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.39 ms: 1.11x faster                                       |
| unpickle                | 9.17 us                                                     | 8.29 us: 1.11x faster                                       |
| xml_etree_parse         | 102 ms                                                      | 92.1 ms: 1.11x faster                                       |
| regex_dna               | 132 ms                                                      | 119 ms: 1.10x faster                                        |
| scimark_fft             | 193 ms                                                      | 175 ms: 1.10x faster                                        |
| deepcopy                | 255 us                                                      | 233 us: 1.10x faster                                        |
| python_startup          | 20.0 ms                                                     | 18.4 ms: 1.09x faster                                       |
| regex_v8                | 15.0 ms                                                     | 14.0 ms: 1.08x faster                                       |
| sqlite_synth            | 1.84 us                                                     | 1.71 us: 1.07x faster                                       |
| json                    | 3.05 ms                                                     | 2.85 ms: 1.07x faster                                       |
| fannkuch                | 258 ms                                                      | 242 ms: 1.06x faster                                        |
| sqlglot_normalize       | 202 ms                                                      | 191 ms: 1.06x faster                                        |
| deepcopy_reduce         | 2.16 us                                                     | 2.08 us: 1.04x faster                                       |
| regex_effbot            | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                       |
| comprehensions          | 16.0 us                                                     | 15.5 us: 1.03x faster                                       |
| json_loads              | 14.2 us                                                     | 13.9 us: 1.02x faster                                       |
| unpickle_list           | 2.81 us                                                     | 2.86 us: 1.02x slower                                       |
| xml_etree_generate      | 54.5 ms                                                     | 55.9 ms: 1.03x slower                                       |
| logging_simple          | 6.20 us                                                     | 6.39 us: 1.03x slower                                       |
| pickle                  | 6.80 us                                                     | 7.04 us: 1.04x slower                                       |
| pidigits                | 145 ms                                                      | 151 ms: 1.04x slower                                        |
| logging_format          | 6.66 us                                                     | 6.94 us: 1.04x slower                                       |
| pathlib                 | 77.4 ms                                                     | 81.2 ms: 1.05x slower                                       |
| async_generators        | 224 ms                                                      | 235 ms: 1.05x slower                                        |
| telco                   | 3.78 ms                                                     | 4.00 ms: 1.06x slower                                       |
| pickle_dict             | 16.9 us                                                     | 18.1 us: 1.07x slower                                       |
| gc_traversal            | 1.34 ms                                                     | 1.46 ms: 1.08x slower                                       |
| bench_mp_pool           | 60.7 ms                                                     | 66.3 ms: 1.09x slower                                       |
| pickle_list             | 2.59 us                                                     | 2.83 us: 1.09x slower                                       |
| dask                    | 305 ms                                                      | 360 ms: 1.18x slower                                        |
| coverage                | 40.0 ms                                                     | 53.8 ms: 1.34x slower                                       |
| Geometric mean          | (ref)                                                       | 1.17x faster                                                |

Benchmark hidden because not significant (5): xml_etree_iterparse, unpack_sequence, nbody, meteor_contest, python_startup_no_site
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x
