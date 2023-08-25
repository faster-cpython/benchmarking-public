
# Results vs. 3.11.0

- fork: python
- ref: e95dd40aff35775efce4
- machine: windows-amd64
- commit hash: e95dd40
- commit date: 2023-05-03
- overall geometric mean: 1.06x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 206 ms: 1.01x faster                                                        |
| tornado_http   | 91.8 ms                                                     | 88.9 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 54.6 ms                                                     | 51.6 ms: 1.06x faster                                                       |
| nbody          | 70.0 ms                                                     | 67.9 ms: 1.03x faster                                                       |
| pidigits       | 148 ms                                                      | 152 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 84.3 ms: 1.07x faster                                                       |
| regex_v8       | 13.8 ms                                                     | 13.9 ms: 1.01x slower                                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.58 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.53 ms: 1.37x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 131 us: 1.16x faster                                                        |
| pickle_pure_python   | 200 us                                                      | 186 us: 1.07x faster                                                        |
| xml_etree_parse      | 95.9 ms                                                     | 92.7 ms: 1.04x faster                                                       |
| pickle_dict          | 18.5 us                                                     | 18.0 us: 1.03x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 54.1 ms: 1.04x slower                                                       |
| pickle               | 6.61 us                                                     | 7.00 us: 1.06x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.85 us: 1.06x slower                                                       |
| unpickle             | 8.09 us                                                     | 8.63 us: 1.07x slower                                                       |
| json_loads           | 12.9 us                                                     | 14.3 us: 1.11x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.88 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.5 ms: 1.02x faster                                                       |
| python_startup         | 18.7 ms                                                     | 18.4 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 6.42 ms: 1.13x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 33.8 ms                                                     | 20.0 ms: 1.69x faster                                                       |
| asyncio_tcp             | 699 ms                                                      | 464 ms: 1.51x faster                                                        |
| json_dumps              | 7.56 ms                                                     | 5.53 ms: 1.37x faster                                                       |
| unpack_sequence         | 46.1 ns                                                     | 33.8 ns: 1.36x faster                                                       |
| deltablue               | 2.61 ms                                                     | 2.03 ms: 1.28x faster                                                       |
| richards                | 30.6 ms                                                     | 24.6 ms: 1.24x faster                                                       |
| sqlglot_parse           | 952 us                                                      | 768 us: 1.24x faster                                                        |
| logging_silent          | 69.8 ns                                                     | 57.6 ns: 1.21x faster                                                       |
| mdp                     | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                      |
| sqlglot_transpile       | 1.16 ms                                                     | 977 us: 1.19x faster                                                        |
| hexiom                  | 4.55 ms                                                     | 3.90 ms: 1.17x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 131 us: 1.16x faster                                                        |
| go                      | 97.3 ms                                                     | 84.7 ms: 1.15x faster                                                       |
| nqueens                 | 64.9 ms                                                     | 57.0 ms: 1.14x faster                                                       |
| mako                    | 7.26 ms                                                     | 6.42 ms: 1.13x faster                                                       |
| raytrace                | 211 ms                                                      | 186 ms: 1.13x faster                                                        |
| json                    | 3.25 ms                                                     | 2.88 ms: 1.13x faster                                                       |
| scimark_lu              | 63.5 ms                                                     | 57.5 ms: 1.11x faster                                                       |
| spectral_norm           | 67.9 ms                                                     | 61.8 ms: 1.10x faster                                                       |
| deepcopy_memo           | 25.2 us                                                     | 23.1 us: 1.09x faster                                                       |
| async_tree_io           | 779 ms                                                      | 715 ms: 1.09x faster                                                        |
| scimark_monte_carlo     | 44.6 ms                                                     | 41.0 ms: 1.09x faster                                                       |
| fannkuch                | 252 ms                                                      | 232 ms: 1.09x faster                                                        |
| async_tree_none         | 320 ms                                                      | 295 ms: 1.09x faster                                                        |
| chaos                   | 47.1 ms                                                     | 43.5 ms: 1.08x faster                                                       |
| pyflate                 | 304 ms                                                      | 282 ms: 1.08x faster                                                        |
| regex_compile           | 90.6 ms                                                     | 84.3 ms: 1.07x faster                                                       |
| pickle_pure_python      | 200 us                                                      | 186 us: 1.07x faster                                                        |
| async_tree_memoization  | 371 ms                                                      | 345 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed | 501 ms                                                      | 468 ms: 1.07x faster                                                        |
| mypy2                   | 229 ms                                                      | 215 ms: 1.06x faster                                                        |
| logging_simple          | 6.61 us                                                     | 6.24 us: 1.06x faster                                                       |
| float                   | 54.6 ms                                                     | 51.6 ms: 1.06x faster                                                       |
| pycparser               | 691 ms                                                      | 658 ms: 1.05x faster                                                        |
| dulwich_log             | 44.5 ms                                                     | 42.4 ms: 1.05x faster                                                       |
| coverage                | 55.9 ms                                                     | 53.3 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.45 ms: 1.05x faster                                                       |
| coroutines              | 14.6 ms                                                     | 14.0 ms: 1.05x faster                                                       |
| deepcopy                | 246 us                                                      | 235 us: 1.05x faster                                                        |
| sqlglot_normalize       | 190 ms                                                      | 182 ms: 1.04x faster                                                        |
| scimark_fft             | 178 ms                                                      | 172 ms: 1.04x faster                                                        |
| xml_etree_parse         | 95.9 ms                                                     | 92.7 ms: 1.04x faster                                                       |
| deepcopy_reduce         | 2.07 us                                                     | 2.00 us: 1.03x faster                                                       |
| tornado_http            | 91.8 ms                                                     | 88.9 ms: 1.03x faster                                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 33.8 ms: 1.03x faster                                                       |
| nbody                   | 70.0 ms                                                     | 67.9 ms: 1.03x faster                                                       |
| logging_format          | 7.01 us                                                     | 6.81 us: 1.03x faster                                                       |
| pickle_dict             | 18.5 us                                                     | 18.0 us: 1.03x faster                                                       |
| comprehensions          | 15.9 us                                                     | 15.5 us: 1.02x faster                                                       |
| python_startup_no_site  | 15.9 ms                                                     | 15.5 ms: 1.02x faster                                                       |
| pprint_safe_repr        | 512 ms                                                      | 500 ms: 1.02x faster                                                        |
| crypto_pyaes            | 47.6 ms                                                     | 46.5 ms: 1.02x faster                                                       |
| bench_thread_pool       | 852 us                                                      | 835 us: 1.02x faster                                                        |
| gc_traversal            | 1.46 ms                                                     | 1.44 ms: 1.02x faster                                                       |
| scimark_sor             | 75.6 ms                                                     | 74.5 ms: 1.01x faster                                                       |
| python_startup          | 18.7 ms                                                     | 18.4 ms: 1.01x faster                                                       |
| 2to3                    | 209 ms                                                      | 206 ms: 1.01x faster                                                        |
| pprint_pformat          | 1.04 sec                                                    | 1.03 sec: 1.00x faster                                                      |
| regex_v8                | 13.8 ms                                                     | 13.9 ms: 1.01x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.70 us: 1.01x slower                                                       |
| regex_dna               | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| pidigits                | 148 ms                                                      | 152 ms: 1.02x slower                                                        |
| xml_etree_generate      | 52.2 ms                                                     | 54.1 ms: 1.04x slower                                                       |
| meteor_contest          | 74.7 ms                                                     | 78.7 ms: 1.05x slower                                                       |
| regex_effbot            | 1.50 ms                                                     | 1.58 ms: 1.06x slower                                                       |
| pickle                  | 6.61 us                                                     | 7.00 us: 1.06x slower                                                       |
| pickle_list             | 2.68 us                                                     | 2.85 us: 1.06x slower                                                       |
| telco                   | 3.90 ms                                                     | 4.16 ms: 1.06x slower                                                       |
| unpickle                | 8.09 us                                                     | 8.63 us: 1.07x slower                                                       |
| bench_mp_pool           | 62.5 ms                                                     | 67.4 ms: 1.08x slower                                                       |
| json_loads              | 12.9 us                                                     | 14.3 us: 1.11x slower                                                       |
| unpickle_list           | 2.55 us                                                     | 2.88 us: 1.13x slower                                                       |
| pathlib                 | 71.4 ms                                                     | 81.9 ms: 1.15x slower                                                       |
| async_generators        | 178 ms                                                      | 224 ms: 1.26x slower                                                        |
| dask                    | 264 ms                                                      | 357 ms: 1.35x slower                                                        |
| Geometric mean          | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (4): xml_etree_iterparse, create_gc_cycles, xml_etree_process, docutils
Ignored benchmarks (19) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
