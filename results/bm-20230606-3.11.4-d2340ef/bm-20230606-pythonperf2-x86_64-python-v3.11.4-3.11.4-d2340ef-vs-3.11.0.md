
# Results vs. 3.11.0

- fork: python
- ref: v3.11.4
- machine: linux-x86_64
- commit hash: d2340ef
- commit date: 2023-06-06
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf2-x86_64-python-v3.11.4-3.11.4-d2340ef |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 285 ms: 1.01x faster                                         |
| chameleon      | 7.67 ms                                                      | 7.63 ms: 1.01x faster                                        |
| docutils       | 2.86 sec                                                     | 2.83 sec: 1.01x faster                                       |
| html5lib       | 72.9 ms                                                      | 71.5 ms: 1.02x faster                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf2-x86_64-python-v3.11.4-3.11.4-d2340ef |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 74.2 ms                                                      | 73.8 ms: 1.01x faster                                        |
| nbody          | 90.7 ms                                                      | 95.6 ms: 1.05x slower                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf2-x86_64-python-v3.11.4-3.11.4-d2340ef |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 155 ms: 1.02x faster                                         |
| regex_effbot   | 3.50 ms                                                      | 3.46 ms: 1.01x faster                                        |
| regex_dna      | 227 ms                                                       | 231 ms: 1.02x slower                                         |
| regex_v8       | 23.9 ms                                                      | 24.5 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf2-x86_64-python-v3.11.4-3.11.4-d2340ef |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_dict          | 30.8 us                                                      | 29.7 us: 1.04x faster                                        |
| unpickle             | 13.4 us                                                      | 13.0 us: 1.03x faster                                        |
| pickle_list          | 3.83 us                                                      | 3.70 us: 1.03x faster                                        |
| json_loads           | 28.7 us                                                      | 28.4 us: 1.01x faster                                        |
| tomli_loads          | 2.26 sec                                                     | 2.27 sec: 1.00x slower                                       |
| pickle_pure_python   | 319 us                                                       | 321 us: 1.01x slower                                         |
| xml_etree_generate   | 80.5 ms                                                      | 81.0 ms: 1.01x slower                                        |
| unpickle_pure_python | 241 us                                                       | 243 us: 1.01x slower                                         |
| pickle               | 9.64 us                                                      | 9.96 us: 1.03x slower                                        |
| unpickle_list        | 4.53 us                                                      | 4.69 us: 1.03x slower                                        |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                 |

Benchmark hidden because not significant (4): xml_etree_process, json_dumps, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf2-x86_64-python-v3.11.4-3.11.4-d2340ef |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 10.7 ms: 1.01x faster                                        |
| python_startup_no_site | 7.76 ms                                                      | 7.72 ms: 1.01x faster                                        |
| Geometric mean         | (ref)                                                        | 1.01x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf2-x86_64-python-v3.11.4-3.11.4-d2340ef |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_text    | 26.1 ms                                                      | 25.6 ms: 1.02x faster                                        |
| mako           | 11.0 ms                                                      | 10.8 ms: 1.02x faster                                        |
| genshi_xml     | 58.5 ms                                                      | 57.9 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-pythonperf2-x86_64-python-v3.11.4-3.11.4-d2340ef |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| chaos                   | 80.9 ms                                                      | 75.0 ms: 1.08x faster                                        |
| logging_format          | 8.11 us                                                      | 7.58 us: 1.07x faster                                        |
| nqueens                 | 103 ms                                                       | 98.5 ms: 1.04x faster                                        |
| gc_traversal            | 3.85 ms                                                      | 3.70 ms: 1.04x faster                                        |
| sqlglot_normalize       | 126 ms                                                       | 122 ms: 1.04x faster                                         |
| deepcopy_reduce         | 3.51 us                                                      | 3.39 us: 1.04x faster                                        |
| pickle_dict             | 30.8 us                                                      | 29.7 us: 1.04x faster                                        |
| unpickle                | 13.4 us                                                      | 13.0 us: 1.03x faster                                        |
| pickle_list             | 3.83 us                                                      | 3.70 us: 1.03x faster                                        |
| pycparser               | 1.32 sec                                                     | 1.28 sec: 1.03x faster                                       |
| deepcopy                | 399 us                                                       | 387 us: 1.03x faster                                         |
| json                    | 5.65 ms                                                      | 5.48 ms: 1.03x faster                                        |
| generators              | 56.0 ms                                                      | 54.7 ms: 1.02x faster                                        |
| sqlalchemy_imperative   | 20.1 ms                                                      | 19.6 ms: 1.02x faster                                        |
| logging_simple          | 7.19 us                                                      | 7.05 us: 1.02x faster                                        |
| html5lib                | 72.9 ms                                                      | 71.5 ms: 1.02x faster                                        |
| deepcopy_memo           | 38.8 us                                                      | 38.1 us: 1.02x faster                                        |
| dask                    | 410 ms                                                       | 402 ms: 1.02x faster                                         |
| genshi_text             | 26.1 ms                                                      | 25.6 ms: 1.02x faster                                        |
| mako                    | 11.0 ms                                                      | 10.8 ms: 1.02x faster                                        |
| raytrace                | 317 ms                                                       | 311 ms: 1.02x faster                                         |
| sqlglot_optimize        | 59.8 ms                                                      | 58.7 ms: 1.02x faster                                        |
| regex_compile           | 158 ms                                                       | 155 ms: 1.02x faster                                         |
| telco                   | 6.86 ms                                                      | 6.75 ms: 1.02x faster                                        |
| thrift                  | 925 us                                                       | 912 us: 1.01x faster                                         |
| scimark_fft             | 285 ms                                                       | 281 ms: 1.01x faster                                         |
| dulwich_log             | 68.4 ms                                                      | 67.6 ms: 1.01x faster                                        |
| scimark_lu              | 115 ms                                                       | 113 ms: 1.01x faster                                         |
| sympy_str               | 337 ms                                                       | 334 ms: 1.01x faster                                         |
| docutils                | 2.86 sec                                                     | 2.83 sec: 1.01x faster                                       |
| genshi_xml              | 58.5 ms                                                      | 57.9 ms: 1.01x faster                                        |
| regex_effbot            | 3.50 ms                                                      | 3.46 ms: 1.01x faster                                        |
| hexiom                  | 7.13 ms                                                      | 7.06 ms: 1.01x faster                                        |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 4.01 ms: 1.01x faster                                        |
| json_loads              | 28.7 us                                                      | 28.4 us: 1.01x faster                                        |
| sympy_sum               | 185 ms                                                       | 183 ms: 1.01x faster                                         |
| python_startup          | 10.8 ms                                                      | 10.7 ms: 1.01x faster                                        |
| sympy_expand            | 555 ms                                                       | 550 ms: 1.01x faster                                         |
| 2to3                    | 288 ms                                                       | 285 ms: 1.01x faster                                         |
| pprint_pformat          | 1.63 sec                                                     | 1.62 sec: 1.01x faster                                       |
| sqlite_synth            | 2.50 us                                                      | 2.48 us: 1.01x faster                                        |
| pathlib                 | 19.1 ms                                                      | 18.9 ms: 1.01x faster                                        |
| meteor_contest          | 131 ms                                                       | 130 ms: 1.01x faster                                         |
| chameleon               | 7.67 ms                                                      | 7.63 ms: 1.01x faster                                        |
| float                   | 74.2 ms                                                      | 73.8 ms: 1.01x faster                                        |
| python_startup_no_site  | 7.76 ms                                                      | 7.72 ms: 1.01x faster                                        |
| sympy_integrate         | 25.8 ms                                                      | 25.6 ms: 1.01x faster                                        |
| aiohttp                 | 985 us                                                       | 980 us: 1.00x faster                                         |
| asyncio_tcp_ssl         | 3.08 sec                                                     | 3.07 sec: 1.00x faster                                       |
| asyncio_tcp             | 753 ms                                                       | 751 ms: 1.00x faster                                         |
| tomli_loads             | 2.26 sec                                                     | 2.27 sec: 1.00x slower                                       |
| pickle_pure_python      | 319 us                                                       | 321 us: 1.01x slower                                         |
| xml_etree_generate      | 80.5 ms                                                      | 81.0 ms: 1.01x slower                                        |
| gunicorn                | 973 us                                                       | 981 us: 1.01x slower                                         |
| coroutines              | 27.6 ms                                                      | 27.8 ms: 1.01x slower                                        |
| sqlglot_parse           | 1.53 ms                                                      | 1.55 ms: 1.01x slower                                        |
| spectral_norm           | 93.3 ms                                                      | 94.1 ms: 1.01x slower                                        |
| unpickle_pure_python    | 241 us                                                       | 243 us: 1.01x slower                                         |
| async_tree_cpu_io_mixed | 749 ms                                                       | 758 ms: 1.01x slower                                         |
| comprehensions          | 24.6 us                                                      | 24.9 us: 1.01x slower                                        |
| deltablue               | 4.00 ms                                                      | 4.06 ms: 1.02x slower                                        |
| regex_dna               | 227 ms                                                       | 231 ms: 1.02x slower                                         |
| scimark_monte_carlo     | 68.2 ms                                                      | 69.5 ms: 1.02x slower                                        |
| async_generators        | 316 ms                                                       | 322 ms: 1.02x slower                                         |
| pyflate                 | 449 ms                                                       | 458 ms: 1.02x slower                                         |
| regex_v8                | 23.9 ms                                                      | 24.5 ms: 1.02x slower                                        |
| fannkuch                | 429 ms                                                       | 441 ms: 1.03x slower                                         |
| scimark_sor             | 111 ms                                                       | 115 ms: 1.03x slower                                         |
| pickle                  | 9.64 us                                                      | 9.96 us: 1.03x slower                                        |
| unpickle_list           | 4.53 us                                                      | 4.69 us: 1.03x slower                                        |
| go                      | 164 ms                                                       | 170 ms: 1.04x slower                                         |
| mdp                     | 2.75 sec                                                     | 2.86 sec: 1.04x slower                                       |
| nbody                   | 90.7 ms                                                      | 95.6 ms: 1.05x slower                                        |
| richards_super          | 61.0 ms                                                      | 65.2 ms: 1.07x slower                                        |
| richards                | 48.3 ms                                                      | 52.2 ms: 1.08x slower                                        |
| mypy2                   | 451 ms                                                       | 535 ms: 1.19x slower                                         |
| Geometric mean          | (ref)                                                        | 1.00x faster                                                 |

Benchmark hidden because not significant (22): bench_thread_pool, django_template, pylint, bench_mp_pool, tornado_http, crypto_pyaes, sqlglot_transpile, xml_etree_process, flaskblogging, unpack_sequence, async_tree_io, pprint_safe_repr, async_tree_memoization, json_dumps, pidigits, logging_silent, sqlalchemy_declarative, xml_etree_iterparse, typing_runtime_protocols, async_tree_none, xml_etree_parse, create_gc_cycles
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: coverage
