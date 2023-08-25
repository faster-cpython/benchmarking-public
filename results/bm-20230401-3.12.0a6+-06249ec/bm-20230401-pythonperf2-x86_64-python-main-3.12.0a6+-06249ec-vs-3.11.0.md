
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 06249ec
- commit date: 2023-04-01
- overall geometric mean: 1.02x faster \*
- HPT reliability: 99.03%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-pythonperf2-x86_64-python-main-3.12.0a6+-06249ec |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| chameleon      | 7.67 ms                                                      | 7.16 ms: 1.07x faster                                        |
| docutils       | 2.86 sec                                                     | 2.82 sec: 1.01x faster                                       |
| html5lib       | 72.9 ms                                                      | 70.9 ms: 1.03x faster                                        |
| tornado_http   | 122 ms                                                       | 113 ms: 1.07x faster                                         |
| Geometric mean | (ref)                                                        | 1.04x faster                                                 |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-pythonperf2-x86_64-python-main-3.12.0a6+-06249ec |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 86.8 ms: 1.05x faster                                        |
| float          | 74.2 ms                                                      | 73.7 ms: 1.01x faster                                        |
| pidigits       | 251 ms                                                       | 260 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-pythonperf2-x86_64-python-main-3.12.0a6+-06249ec |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 150 ms: 1.05x faster                                         |
| regex_effbot   | 3.50 ms                                                      | 3.38 ms: 1.04x faster                                        |
| regex_v8       | 23.9 ms                                                      | 23.4 ms: 1.02x faster                                        |
| regex_dna      | 227 ms                                                       | 231 ms: 1.02x slower                                         |
| Geometric mean | (ref)                                                        | 1.02x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-pythonperf2-x86_64-python-main-3.12.0a6+-06249ec |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.4 ms: 1.28x faster                                        |
| json_loads           | 28.7 us                                                      | 23.9 us: 1.20x faster                                        |
| unpickle_pure_python | 241 us                                                       | 215 us: 1.12x faster                                         |
| xml_etree_parse      | 158 ms                                                       | 143 ms: 1.10x faster                                         |
| unpickle             | 13.4 us                                                      | 13.0 us: 1.03x faster                                        |
| xml_etree_iterparse  | 104 ms                                                       | 103 ms: 1.01x faster                                         |
| pickle_list          | 3.83 us                                                      | 3.90 us: 1.02x slower                                        |
| pickle_dict          | 30.8 us                                                      | 31.5 us: 1.02x slower                                        |
| xml_etree_process    | 56.5 ms                                                      | 60.0 ms: 1.06x slower                                        |
| pickle               | 9.64 us                                                      | 10.3 us: 1.07x slower                                        |
| xml_etree_generate   | 80.5 ms                                                      | 86.2 ms: 1.07x slower                                        |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                 |

Benchmark hidden because not significant (2): unpickle_list, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-pythonperf2-x86_64-python-main-3.12.0a6+-06249ec |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.0 ms: 1.03x slower                                        |
| python_startup_no_site | 7.76 ms                                                      | 8.31 ms: 1.07x slower                                        |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-pythonperf2-x86_64-python-main-3.12.0a6+-06249ec |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako           | 11.0 ms                                                      | 10.1 ms: 1.09x faster                                        |
| genshi_xml     | 58.5 ms                                                      | 56.5 ms: 1.04x faster                                        |
| genshi_text    | 26.1 ms                                                      | 26.4 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-pythonperf2-x86_64-python-main-3.12.0a6+-06249ec |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| asyncio_tcp             | 753 ms                                                       | 385 ms: 1.95x faster                                         |
| generators              | 56.0 ms                                                      | 38.7 ms: 1.45x faster                                        |
| json_dumps              | 13.4 ms                                                      | 10.4 ms: 1.28x faster                                        |
| json_loads              | 28.7 us                                                      | 23.9 us: 1.20x faster                                        |
| mypy2                   | 451 ms                                                       | 386 ms: 1.17x faster                                         |
| scimark_lu              | 115 ms                                                       | 101 ms: 1.14x faster                                         |
| chaos                   | 80.9 ms                                                      | 71.4 ms: 1.13x faster                                        |
| json                    | 5.65 ms                                                      | 5.05 ms: 1.12x faster                                        |
| unpickle_pure_python    | 241 us                                                       | 215 us: 1.12x faster                                         |
| xml_etree_parse         | 158 ms                                                       | 143 ms: 1.10x faster                                         |
| deltablue               | 4.00 ms                                                      | 3.63 ms: 1.10x faster                                        |
| mako                    | 11.0 ms                                                      | 10.1 ms: 1.09x faster                                        |
| scimark_fft             | 285 ms                                                       | 264 ms: 1.08x faster                                         |
| tornado_http            | 122 ms                                                       | 113 ms: 1.07x faster                                         |
| chameleon               | 7.67 ms                                                      | 7.16 ms: 1.07x faster                                        |
| deepcopy_memo           | 38.8 us                                                      | 36.2 us: 1.07x faster                                        |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 3.78 ms: 1.07x faster                                        |
| mdp                     | 2.75 sec                                                     | 2.57 sec: 1.07x faster                                       |
| raytrace                | 317 ms                                                       | 296 ms: 1.07x faster                                         |
| logging_silent          | 101 ns                                                       | 94.8 ns: 1.06x faster                                        |
| hexiom                  | 7.13 ms                                                      | 6.77 ms: 1.05x faster                                        |
| regex_compile           | 158 ms                                                       | 150 ms: 1.05x faster                                         |
| pycparser               | 1.32 sec                                                     | 1.26 sec: 1.05x faster                                       |
| coroutines              | 27.6 ms                                                      | 26.2 ms: 1.05x faster                                        |
| nbody                   | 90.7 ms                                                      | 86.8 ms: 1.05x faster                                        |
| sqlglot_normalize       | 126 ms                                                       | 121 ms: 1.04x faster                                         |
| unpack_sequence         | 45.6 ns                                                      | 44.0 ns: 1.04x faster                                        |
| regex_effbot            | 3.50 ms                                                      | 3.38 ms: 1.04x faster                                        |
| pprint_pformat          | 1.63 sec                                                     | 1.57 sec: 1.04x faster                                       |
| genshi_xml              | 58.5 ms                                                      | 56.5 ms: 1.04x faster                                        |
| unpickle                | 13.4 us                                                      | 13.0 us: 1.03x faster                                        |
| dulwich_log             | 68.4 ms                                                      | 66.4 ms: 1.03x faster                                        |
| html5lib                | 72.9 ms                                                      | 70.9 ms: 1.03x faster                                        |
| async_tree_memoization  | 630 ms                                                       | 614 ms: 1.03x faster                                         |
| bench_thread_pool       | 1.01 ms                                                      | 987 us: 1.02x faster                                         |
| regex_v8                | 23.9 ms                                                      | 23.4 ms: 1.02x faster                                        |
| sympy_expand            | 555 ms                                                       | 541 ms: 1.02x faster                                         |
| logging_simple          | 7.19 us                                                      | 7.03 us: 1.02x faster                                        |
| meteor_contest          | 131 ms                                                       | 128 ms: 1.02x faster                                         |
| sqlglot_optimize        | 59.8 ms                                                      | 58.8 ms: 1.02x faster                                        |
| pprint_safe_repr        | 784 ms                                                       | 771 ms: 1.02x faster                                         |
| docutils                | 2.86 sec                                                     | 2.82 sec: 1.01x faster                                       |
| scimark_monte_carlo     | 68.2 ms                                                      | 67.5 ms: 1.01x faster                                        |
| xml_etree_iterparse     | 104 ms                                                       | 103 ms: 1.01x faster                                         |
| sympy_str               | 337 ms                                                       | 334 ms: 1.01x faster                                         |
| sympy_integrate         | 25.8 ms                                                      | 25.6 ms: 1.01x faster                                        |
| float                   | 74.2 ms                                                      | 73.7 ms: 1.01x faster                                        |
| spectral_norm           | 93.3 ms                                                      | 94.1 ms: 1.01x slower                                        |
| genshi_text             | 26.1 ms                                                      | 26.4 ms: 1.01x slower                                        |
| async_tree_cpu_io_mixed | 749 ms                                                       | 756 ms: 1.01x slower                                         |
| telco                   | 6.86 ms                                                      | 6.93 ms: 1.01x slower                                        |
| sympy_sum               | 185 ms                                                       | 188 ms: 1.02x slower                                         |
| richards                | 48.3 ms                                                      | 49.1 ms: 1.02x slower                                        |
| regex_dna               | 227 ms                                                       | 231 ms: 1.02x slower                                         |
| thrift                  | 925 us                                                       | 942 us: 1.02x slower                                         |
| pickle_list             | 3.83 us                                                      | 3.90 us: 1.02x slower                                        |
| sqlglot_transpile       | 1.92 ms                                                      | 1.96 ms: 1.02x slower                                        |
| pickle_dict             | 30.8 us                                                      | 31.5 us: 1.02x slower                                        |
| pyflate                 | 449 ms                                                       | 459 ms: 1.02x slower                                         |
| scimark_sor             | 111 ms                                                       | 114 ms: 1.03x slower                                         |
| python_startup          | 10.8 ms                                                      | 11.0 ms: 1.03x slower                                        |
| nqueens                 | 103 ms                                                       | 106 ms: 1.03x slower                                         |
| pidigits                | 251 ms                                                       | 260 ms: 1.04x slower                                         |
| pathlib                 | 19.1 ms                                                      | 19.7 ms: 1.04x slower                                        |
| fannkuch                | 429 ms                                                       | 445 ms: 1.04x slower                                         |
| sqlglot_parse           | 1.53 ms                                                      | 1.60 ms: 1.04x slower                                        |
| create_gc_cycles        | 1.61 ms                                                      | 1.68 ms: 1.05x slower                                        |
| sqlite_synth            | 2.50 us                                                      | 2.62 us: 1.05x slower                                        |
| gc_traversal            | 3.85 ms                                                      | 4.04 ms: 1.05x slower                                        |
| go                      | 164 ms                                                       | 173 ms: 1.05x slower                                         |
| xml_etree_process       | 56.5 ms                                                      | 60.0 ms: 1.06x slower                                        |
| pickle                  | 9.64 us                                                      | 10.3 us: 1.07x slower                                        |
| xml_etree_generate      | 80.5 ms                                                      | 86.2 ms: 1.07x slower                                        |
| python_startup_no_site  | 7.76 ms                                                      | 8.31 ms: 1.07x slower                                        |
| comprehensions          | 24.6 us                                                      | 27.7 us: 1.13x slower                                        |
| async_generators        | 316 ms                                                       | 391 ms: 1.24x slower                                         |
| dask                    | 410 ms                                                       | 577 ms: 1.41x slower                                         |
| Geometric mean          | (ref)                                                        | 1.02x faster                                                 |

Benchmark hidden because not significant (12): logging_format, django_template, async_tree_none, unpickle_list, coverage, async_tree_io, deepcopy_reduce, deepcopy, pickle_pure_python, crypto_pyaes, 2to3, bench_mp_pool
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.03% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
