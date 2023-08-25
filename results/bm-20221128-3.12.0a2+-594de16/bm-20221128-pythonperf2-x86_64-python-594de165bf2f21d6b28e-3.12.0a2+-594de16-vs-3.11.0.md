
# Results vs. 3.11.0

- fork: python
- ref: 594de165bf2f21d6b28e
- machine: linux-x86_64
- commit hash: 594de16
- commit date: 2022-11-28
- overall geometric mean: 1.02x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 280 ms: 1.03x faster                                                         |
| docutils       | 2.86 sec                                                     | 2.77 sec: 1.03x faster                                                       |
| html5lib       | 72.9 ms                                                      | 66.5 ms: 1.10x faster                                                        |
| tornado_http   | 122 ms                                                       | 119 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 89.6 ms: 1.01x faster                                                        |
| pidigits       | 251 ms                                                       | 252 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 149 ms: 1.05x faster                                                         |
| regex_effbot   | 3.50 ms                                                      | 3.36 ms: 1.04x faster                                                        |
| regex_v8       | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                                        |
| regex_dna      | 227 ms                                                       | 229 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.5 ms: 1.28x faster                                                        |
| json_loads           | 28.7 us                                                      | 24.2 us: 1.19x faster                                                        |
| xml_etree_parse      | 158 ms                                                       | 141 ms: 1.12x faster                                                         |
| unpickle_pure_python | 241 us                                                       | 219 us: 1.10x faster                                                         |
| xml_etree_process    | 56.5 ms                                                      | 55.8 ms: 1.01x faster                                                        |
| xml_etree_generate   | 80.5 ms                                                      | 79.8 ms: 1.01x faster                                                        |
| pickle               | 9.64 us                                                      | 9.77 us: 1.01x slower                                                        |
| pickle_dict          | 30.8 us                                                      | 31.7 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                                 |

Benchmark hidden because not significant (5): xml_etree_iterparse, pickle_pure_python, unpickle_list, pickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 10.8 ms: 1.00x slower                                                        |
| python_startup_no_site | 7.76 ms                                                      | 7.85 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 58.5 ms                                                      | 52.3 ms: 1.12x faster                                                        |
| mako           | 11.0 ms                                                      | 10.2 ms: 1.08x faster                                                        |
| genshi_text    | 26.1 ms                                                      | 24.5 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221128-pythonperf2-x86_64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps              | 13.4 ms                                                      | 10.5 ms: 1.28x faster                                                        |
| mypy2                   | 451 ms                                                       | 372 ms: 1.21x faster                                                         |
| json_loads              | 28.7 us                                                      | 24.2 us: 1.19x faster                                                        |
| xml_etree_parse         | 158 ms                                                       | 141 ms: 1.12x faster                                                         |
| genshi_xml              | 58.5 ms                                                      | 52.3 ms: 1.12x faster                                                        |
| json                    | 5.65 ms                                                      | 5.08 ms: 1.11x faster                                                        |
| scimark_lu              | 115 ms                                                       | 103 ms: 1.11x faster                                                         |
| chaos                   | 80.9 ms                                                      | 73.0 ms: 1.11x faster                                                        |
| unpickle_pure_python    | 241 us                                                       | 219 us: 1.10x faster                                                         |
| html5lib                | 72.9 ms                                                      | 66.5 ms: 1.10x faster                                                        |
| aiohttp                 | 985 us                                                       | 904 us: 1.09x faster                                                         |
| gunicorn                | 973 us                                                       | 895 us: 1.09x faster                                                         |
| gc_traversal            | 3.85 ms                                                      | 3.56 ms: 1.08x faster                                                        |
| mako                    | 11.0 ms                                                      | 10.2 ms: 1.08x faster                                                        |
| deltablue               | 4.00 ms                                                      | 3.71 ms: 1.08x faster                                                        |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 3.77 ms: 1.08x faster                                                        |
| fannkuch                | 429 ms                                                       | 399 ms: 1.07x faster                                                         |
| genshi_text             | 26.1 ms                                                      | 24.5 ms: 1.07x faster                                                        |
| regex_compile           | 158 ms                                                       | 149 ms: 1.05x faster                                                         |
| sqlglot_normalize       | 126 ms                                                       | 120 ms: 1.05x faster                                                         |
| hexiom                  | 7.13 ms                                                      | 6.78 ms: 1.05x faster                                                        |
| bench_thread_pool       | 1.01 ms                                                      | 970 us: 1.04x faster                                                         |
| regex_effbot            | 3.50 ms                                                      | 3.36 ms: 1.04x faster                                                        |
| pycparser               | 1.32 sec                                                     | 1.27 sec: 1.04x faster                                                       |
| raytrace                | 317 ms                                                       | 305 ms: 1.04x faster                                                         |
| nqueens                 | 103 ms                                                       | 99.3 ms: 1.04x faster                                                        |
| logging_format          | 8.11 us                                                      | 7.84 us: 1.03x faster                                                        |
| pprint_pformat          | 1.63 sec                                                     | 1.58 sec: 1.03x faster                                                       |
| docutils                | 2.86 sec                                                     | 2.77 sec: 1.03x faster                                                       |
| sqlglot_optimize        | 59.8 ms                                                      | 57.9 ms: 1.03x faster                                                        |
| regex_v8                | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                                        |
| create_gc_cycles        | 1.61 ms                                                      | 1.56 ms: 1.03x faster                                                        |
| 2to3                    | 288 ms                                                       | 280 ms: 1.03x faster                                                         |
| telco                   | 6.86 ms                                                      | 6.69 ms: 1.03x faster                                                        |
| async_tree_memoization  | 630 ms                                                       | 616 ms: 1.02x faster                                                         |
| sympy_expand            | 555 ms                                                       | 543 ms: 1.02x faster                                                         |
| tornado_http            | 122 ms                                                       | 119 ms: 1.02x faster                                                         |
| dulwich_log             | 68.4 ms                                                      | 67.1 ms: 1.02x faster                                                        |
| pprint_safe_repr        | 784 ms                                                       | 768 ms: 1.02x faster                                                         |
| meteor_contest          | 131 ms                                                       | 128 ms: 1.02x faster                                                         |
| go                      | 164 ms                                                       | 162 ms: 1.01x faster                                                         |
| async_tree_io           | 1.17 sec                                                     | 1.16 sec: 1.01x faster                                                       |
| nbody                   | 90.7 ms                                                      | 89.6 ms: 1.01x faster                                                        |
| xml_etree_process       | 56.5 ms                                                      | 55.8 ms: 1.01x faster                                                        |
| pathlib                 | 19.1 ms                                                      | 18.8 ms: 1.01x faster                                                        |
| sympy_str               | 337 ms                                                       | 334 ms: 1.01x faster                                                         |
| asyncio_tcp             | 753 ms                                                       | 745 ms: 1.01x faster                                                         |
| scimark_fft             | 285 ms                                                       | 282 ms: 1.01x faster                                                         |
| sympy_integrate         | 25.8 ms                                                      | 25.5 ms: 1.01x faster                                                        |
| xml_etree_generate      | 80.5 ms                                                      | 79.8 ms: 1.01x faster                                                        |
| mdp                     | 2.75 sec                                                     | 2.73 sec: 1.00x faster                                                       |
| pidigits                | 251 ms                                                       | 252 ms: 1.00x slower                                                         |
| python_startup          | 10.8 ms                                                      | 10.8 ms: 1.00x slower                                                        |
| scimark_sor             | 111 ms                                                       | 112 ms: 1.01x slower                                                         |
| coverage                | 84.8 ms                                                      | 85.4 ms: 1.01x slower                                                        |
| regex_dna               | 227 ms                                                       | 229 ms: 1.01x slower                                                         |
| sqlglot_parse           | 1.53 ms                                                      | 1.55 ms: 1.01x slower                                                        |
| python_startup_no_site  | 7.76 ms                                                      | 7.85 ms: 1.01x slower                                                        |
| async_tree_cpu_io_mixed | 749 ms                                                       | 758 ms: 1.01x slower                                                         |
| richards                | 48.3 ms                                                      | 48.9 ms: 1.01x slower                                                        |
| thrift                  | 925 us                                                       | 937 us: 1.01x slower                                                         |
| dask                    | 410 ms                                                       | 415 ms: 1.01x slower                                                         |
| pickle                  | 9.64 us                                                      | 9.77 us: 1.01x slower                                                        |
| coroutines              | 27.6 ms                                                      | 28.2 ms: 1.02x slower                                                        |
| deepcopy_reduce         | 3.51 us                                                      | 3.59 us: 1.02x slower                                                        |
| sqlite_synth            | 2.50 us                                                      | 2.56 us: 1.03x slower                                                        |
| pickle_dict             | 30.8 us                                                      | 31.7 us: 1.03x slower                                                        |
| deepcopy                | 399 us                                                       | 415 us: 1.04x slower                                                         |
| async_generators        | 316 ms                                                       | 332 ms: 1.05x slower                                                         |
| scimark_monte_carlo     | 68.2 ms                                                      | 72.0 ms: 1.06x slower                                                        |
| spectral_norm           | 93.3 ms                                                      | 98.7 ms: 1.06x slower                                                        |
| generators              | 56.0 ms                                                      | 61.1 ms: 1.09x slower                                                        |
| comprehensions          | 24.6 us                                                      | 26.8 us: 1.09x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (18): async_tree_none, float, django_template, pyflate, chameleon, unpack_sequence, xml_etree_iterparse, sympy_sum, deepcopy_memo, sqlglot_transpile, logging_silent, pickle_pure_python, unpickle_list, crypto_pyaes, bench_mp_pool, pickle_list, unpickle, logging_simple
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
