
# Results vs. 3.10.4

- fork: python
- ref: e95dd40aff35775efce4
- machine: windows-amd64
- commit hash: e95dd40
- commit date: 2023-05-03
- overall geometric mean: 1.18x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 206 ms: 1.15x faster                                                        |
| docutils       | 1.89 sec                                                    | 1.60 sec: 1.18x faster                                                      |
| tornado_http   | 109 ms                                                      | 88.9 ms: 1.23x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 51.6 ms: 1.17x faster                                                       |
| nbody          | 69.3 ms                                                     | 67.9 ms: 1.02x faster                                                       |
| pidigits       | 145 ms                                                      | 152 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 84.3 ms: 1.23x faster                                                       |
| regex_dna      | 132 ms                                                      | 117 ms: 1.13x faster                                                        |
| regex_v8       | 15.0 ms                                                     | 13.9 ms: 1.08x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.53 ms: 1.54x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 186 us: 1.38x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 131 us: 1.30x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 37.1 ms: 1.17x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 92.7 ms: 1.10x faster                                                       |
| unpickle             | 9.17 us                                                     | 8.63 us: 1.06x faster                                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 62.2 ms: 1.02x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 54.1 ms: 1.01x faster                                                       |
| pickle               | 6.80 us                                                     | 7.00 us: 1.03x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 18.0 us: 1.07x slower                                                       |
| pickle_list          | 2.59 us                                                     | 2.85 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (2): json_loads, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 20.0 ms                                                     | 18.4 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-----------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 6.42 ms: 1.37x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-pythonperf1-amd64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.03 ms: 2.05x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 57.6 ns: 1.67x faster                                                       |
| richards                | 41.2 ms                                                     | 24.6 ms: 1.67x faster                                                       |
| mypy2                   | 352 ms                                                      | 215 ms: 1.64x faster                                                        |
| go                      | 136 ms                                                      | 84.7 ms: 1.61x faster                                                       |
| sqlglot_parse           | 1.22 ms                                                     | 768 us: 1.59x faster                                                        |
| generators              | 31.6 ms                                                     | 20.0 ms: 1.58x faster                                                       |
| json_dumps              | 8.50 ms                                                     | 5.53 ms: 1.54x faster                                                       |
| asyncio_tcp             | 712 ms                                                      | 464 ms: 1.54x faster                                                        |
| sqlglot_transpile       | 1.46 ms                                                     | 977 us: 1.50x faster                                                        |
| async_tree_io           | 1.07 sec                                                    | 715 ms: 1.49x faster                                                        |
| scimark_lu              | 85.4 ms                                                     | 57.5 ms: 1.49x faster                                                       |
| raytrace                | 271 ms                                                      | 186 ms: 1.46x faster                                                        |
| async_tree_memoization  | 497 ms                                                      | 345 ms: 1.44x faster                                                        |
| async_tree_none         | 420 ms                                                      | 295 ms: 1.43x faster                                                        |
| hexiom                  | 5.52 ms                                                     | 3.90 ms: 1.41x faster                                                       |
| scimark_sor             | 105 ms                                                      | 74.5 ms: 1.41x faster                                                       |
| pickle_pure_python      | 257 us                                                      | 186 us: 1.38x faster                                                        |
| mako                    | 8.80 ms                                                     | 6.42 ms: 1.37x faster                                                       |
| pyflate                 | 387 ms                                                      | 282 ms: 1.37x faster                                                        |
| scimark_monte_carlo     | 55.9 ms                                                     | 41.0 ms: 1.36x faster                                                       |
| chaos                   | 58.9 ms                                                     | 43.5 ms: 1.35x faster                                                       |
| crypto_pyaes            | 62.3 ms                                                     | 46.5 ms: 1.34x faster                                                       |
| pycparser               | 868 ms                                                      | 658 ms: 1.32x faster                                                        |
| unpickle_pure_python    | 171 us                                                      | 131 us: 1.30x faster                                                        |
| async_tree_cpu_io_mixed | 609 ms                                                      | 468 ms: 1.30x faster                                                        |
| spectral_norm           | 78.0 ms                                                     | 61.8 ms: 1.26x faster                                                       |
| deepcopy_memo           | 28.5 us                                                     | 23.1 us: 1.24x faster                                                       |
| mdp                     | 1.71 sec                                                    | 1.39 sec: 1.23x faster                                                      |
| tornado_http            | 109 ms                                                      | 88.9 ms: 1.23x faster                                                       |
| regex_compile           | 103 ms                                                      | 84.3 ms: 1.23x faster                                                       |
| docutils                | 1.89 sec                                                    | 1.60 sec: 1.18x faster                                                      |
| pprint_safe_repr        | 589 ms                                                      | 500 ms: 1.18x faster                                                        |
| nqueens                 | 67.0 ms                                                     | 57.0 ms: 1.18x faster                                                       |
| xml_etree_process       | 43.4 ms                                                     | 37.1 ms: 1.17x faster                                                       |
| pprint_pformat          | 1.21 sec                                                    | 1.03 sec: 1.17x faster                                                      |
| float                   | 60.2 ms                                                     | 51.6 ms: 1.17x faster                                                       |
| sqlglot_optimize        | 39.0 ms                                                     | 33.8 ms: 1.15x faster                                                       |
| 2to3                    | 237 ms                                                      | 206 ms: 1.15x faster                                                        |
| coroutines              | 15.9 ms                                                     | 14.0 ms: 1.14x faster                                                       |
| create_gc_cycles        | 782 us                                                      | 689 us: 1.13x faster                                                        |
| bench_thread_pool       | 946 us                                                      | 835 us: 1.13x faster                                                        |
| regex_dna               | 132 ms                                                      | 117 ms: 1.13x faster                                                        |
| scimark_fft             | 193 ms                                                      | 172 ms: 1.13x faster                                                        |
| dulwich_log             | 47.6 ms                                                     | 42.4 ms: 1.12x faster                                                       |
| unpack_sequence         | 37.8 ns                                                     | 33.8 ns: 1.12x faster                                                       |
| fannkuch                | 258 ms                                                      | 232 ms: 1.11x faster                                                        |
| sqlglot_normalize       | 202 ms                                                      | 182 ms: 1.11x faster                                                        |
| xml_etree_parse         | 102 ms                                                      | 92.7 ms: 1.10x faster                                                       |
| deepcopy                | 255 us                                                      | 235 us: 1.09x faster                                                        |
| python_startup          | 20.0 ms                                                     | 18.4 ms: 1.08x faster                                                       |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.45 ms: 1.08x faster                                                       |
| sqlite_synth            | 1.84 us                                                     | 1.70 us: 1.08x faster                                                       |
| regex_v8                | 15.0 ms                                                     | 13.9 ms: 1.08x faster                                                       |
| deepcopy_reduce         | 2.16 us                                                     | 2.00 us: 1.08x faster                                                       |
| unpickle                | 9.17 us                                                     | 8.63 us: 1.06x faster                                                       |
| json                    | 3.05 ms                                                     | 2.88 ms: 1.06x faster                                                       |
| regex_effbot            | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                       |
| comprehensions          | 16.0 us                                                     | 15.5 us: 1.03x faster                                                       |
| xml_etree_iterparse     | 63.5 ms                                                     | 62.2 ms: 1.02x faster                                                       |
| nbody                   | 69.3 ms                                                     | 67.9 ms: 1.02x faster                                                       |
| xml_etree_generate      | 54.5 ms                                                     | 54.1 ms: 1.01x faster                                                       |
| logging_simple          | 6.20 us                                                     | 6.24 us: 1.01x slower                                                       |
| logging_format          | 6.66 us                                                     | 6.81 us: 1.02x slower                                                       |
| pickle                  | 6.80 us                                                     | 7.00 us: 1.03x slower                                                       |
| pidigits                | 145 ms                                                      | 152 ms: 1.05x slower                                                        |
| pathlib                 | 77.4 ms                                                     | 81.9 ms: 1.06x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 18.0 us: 1.07x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.44 ms: 1.07x slower                                                       |
| meteor_contest          | 72.5 ms                                                     | 78.7 ms: 1.08x slower                                                       |
| telco                   | 3.78 ms                                                     | 4.16 ms: 1.10x slower                                                       |
| pickle_list             | 2.59 us                                                     | 2.85 us: 1.10x slower                                                       |
| bench_mp_pool           | 60.7 ms                                                     | 67.4 ms: 1.11x slower                                                       |
| dask                    | 305 ms                                                      | 357 ms: 1.17x slower                                                        |
| coverage                | 40.0 ms                                                     | 53.3 ms: 1.33x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.18x faster                                                                |

Benchmark hidden because not significant (4): python_startup_no_site, async_generators, json_loads, unpickle_list
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x
