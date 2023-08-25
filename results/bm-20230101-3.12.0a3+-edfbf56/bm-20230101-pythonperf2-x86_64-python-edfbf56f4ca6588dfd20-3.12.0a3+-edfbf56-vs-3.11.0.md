
# Results vs. 3.11.0

- fork: python
- ref: edfbf56f4ca6588dfd20
- machine: linux-x86_64
- commit hash: edfbf56
- commit date: 2023-01-01
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230101-pythonperf2-x86_64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 284 ms: 1.01x faster                                                         |
| chameleon      | 7.67 ms                                                      | 7.29 ms: 1.05x faster                                                        |
| docutils       | 2.86 sec                                                     | 2.76 sec: 1.03x faster                                                       |
| html5lib       | 72.9 ms                                                      | 66.2 ms: 1.10x faster                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230101-pythonperf2-x86_64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 74.2 ms                                                      | 72.5 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230101-pythonperf2-x86_64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 149 ms: 1.06x faster                                                         |
| regex_v8       | 23.9 ms                                                      | 22.9 ms: 1.05x faster                                                        |
| regex_effbot   | 3.50 ms                                                      | 3.40 ms: 1.03x faster                                                        |
| regex_dna      | 227 ms                                                       | 229 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230101-pythonperf2-x86_64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                                        |
| json_loads           | 28.7 us                                                      | 24.1 us: 1.19x faster                                                        |
| unpickle_pure_python | 241 us                                                       | 210 us: 1.15x faster                                                         |
| xml_etree_parse      | 158 ms                                                       | 141 ms: 1.12x faster                                                         |
| unpickle             | 13.4 us                                                      | 12.9 us: 1.04x faster                                                        |
| xml_etree_process    | 56.5 ms                                                      | 54.1 ms: 1.04x faster                                                        |
| xml_etree_generate   | 80.5 ms                                                      | 78.0 ms: 1.03x faster                                                        |
| unpickle_list        | 4.53 us                                                      | 4.43 us: 1.02x faster                                                        |
| pickle_pure_python   | 319 us                                                       | 313 us: 1.02x faster                                                         |
| pickle               | 9.64 us                                                      | 9.84 us: 1.02x slower                                                        |
| pickle_dict          | 30.8 us                                                      | 31.7 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.06x faster                                                                 |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230101-pythonperf2-x86_64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 10.7 ms: 1.00x faster                                                        |
| python_startup_no_site | 7.76 ms                                                      | 7.83 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230101-pythonperf2-x86_64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 58.5 ms                                                      | 53.9 ms: 1.09x faster                                                        |
| mako            | 11.0 ms                                                      | 10.1 ms: 1.09x faster                                                        |
| genshi_text     | 26.1 ms                                                      | 25.1 ms: 1.04x faster                                                        |
| django_template | 40.2 ms                                                      | 39.5 ms: 1.02x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230101-pythonperf2-x86_64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 753 ms                                                       | 391 ms: 1.93x faster                                                         |
| json_dumps              | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                                        |
| mypy2                   | 451 ms                                                       | 378 ms: 1.20x faster                                                         |
| json_loads              | 28.7 us                                                      | 24.1 us: 1.19x faster                                                        |
| unpickle_pure_python    | 241 us                                                       | 210 us: 1.15x faster                                                         |
| scimark_lu              | 115 ms                                                       | 100 ms: 1.14x faster                                                         |
| xml_etree_parse         | 158 ms                                                       | 141 ms: 1.12x faster                                                         |
| json                    | 5.65 ms                                                      | 5.08 ms: 1.11x faster                                                        |
| chaos                   | 80.9 ms                                                      | 72.8 ms: 1.11x faster                                                        |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 3.66 ms: 1.11x faster                                                        |
| html5lib                | 72.9 ms                                                      | 66.2 ms: 1.10x faster                                                        |
| deltablue               | 4.00 ms                                                      | 3.64 ms: 1.10x faster                                                        |
| fannkuch                | 429 ms                                                       | 392 ms: 1.09x faster                                                         |
| nqueens                 | 103 ms                                                       | 94.4 ms: 1.09x faster                                                        |
| genshi_xml              | 58.5 ms                                                      | 53.9 ms: 1.09x faster                                                        |
| mako                    | 11.0 ms                                                      | 10.1 ms: 1.09x faster                                                        |
| deepcopy_memo           | 38.8 us                                                      | 35.7 us: 1.09x faster                                                        |
| sqlglot_normalize       | 126 ms                                                       | 119 ms: 1.06x faster                                                         |
| deepcopy_reduce         | 3.51 us                                                      | 3.32 us: 1.06x faster                                                        |
| raytrace                | 317 ms                                                       | 300 ms: 1.06x faster                                                         |
| regex_compile           | 158 ms                                                       | 149 ms: 1.06x faster                                                         |
| chameleon               | 7.67 ms                                                      | 7.29 ms: 1.05x faster                                                        |
| dulwich_log             | 68.4 ms                                                      | 65.1 ms: 1.05x faster                                                        |
| deepcopy                | 399 us                                                       | 380 us: 1.05x faster                                                         |
| pyflate                 | 449 ms                                                       | 429 ms: 1.05x faster                                                         |
| thrift                  | 925 us                                                       | 885 us: 1.05x faster                                                         |
| regex_v8                | 23.9 ms                                                      | 22.9 ms: 1.05x faster                                                        |
| pprint_pformat          | 1.63 sec                                                     | 1.56 sec: 1.05x faster                                                       |
| richards                | 48.3 ms                                                      | 46.3 ms: 1.04x faster                                                        |
| unpickle                | 13.4 us                                                      | 12.9 us: 1.04x faster                                                        |
| xml_etree_process       | 56.5 ms                                                      | 54.1 ms: 1.04x faster                                                        |
| genshi_text             | 26.1 ms                                                      | 25.1 ms: 1.04x faster                                                        |
| bench_thread_pool       | 1.01 ms                                                      | 971 us: 1.04x faster                                                         |
| logging_format          | 8.11 us                                                      | 7.80 us: 1.04x faster                                                        |
| sqlglot_optimize        | 59.8 ms                                                      | 57.5 ms: 1.04x faster                                                        |
| sympy_expand            | 555 ms                                                       | 533 ms: 1.04x faster                                                         |
| hexiom                  | 7.13 ms                                                      | 6.86 ms: 1.04x faster                                                        |
| pycparser               | 1.32 sec                                                     | 1.28 sec: 1.04x faster                                                       |
| scimark_sor             | 111 ms                                                       | 107 ms: 1.04x faster                                                         |
| crypto_pyaes            | 83.4 ms                                                      | 80.5 ms: 1.04x faster                                                        |
| docutils                | 2.86 sec                                                     | 2.76 sec: 1.03x faster                                                       |
| scimark_fft             | 285 ms                                                       | 275 ms: 1.03x faster                                                         |
| pprint_safe_repr        | 784 ms                                                       | 758 ms: 1.03x faster                                                         |
| xml_etree_generate      | 80.5 ms                                                      | 78.0 ms: 1.03x faster                                                        |
| scimark_monte_carlo     | 68.2 ms                                                      | 66.1 ms: 1.03x faster                                                        |
| regex_effbot            | 3.50 ms                                                      | 3.40 ms: 1.03x faster                                                        |
| go                      | 164 ms                                                       | 159 ms: 1.03x faster                                                         |
| logging_simple          | 7.19 us                                                      | 6.98 us: 1.03x faster                                                        |
| async_tree_memoization  | 630 ms                                                       | 613 ms: 1.03x faster                                                         |
| unpack_sequence         | 45.6 ns                                                      | 44.5 ns: 1.03x faster                                                        |
| float                   | 74.2 ms                                                      | 72.5 ms: 1.02x faster                                                        |
| unpickle_list           | 4.53 us                                                      | 4.43 us: 1.02x faster                                                        |
| sympy_str               | 337 ms                                                       | 330 ms: 1.02x faster                                                         |
| pickle_pure_python      | 319 us                                                       | 313 us: 1.02x faster                                                         |
| sympy_integrate         | 25.8 ms                                                      | 25.3 ms: 1.02x faster                                                        |
| async_tree_none         | 519 ms                                                       | 510 ms: 1.02x faster                                                         |
| django_template         | 40.2 ms                                                      | 39.5 ms: 1.02x faster                                                        |
| gc_traversal            | 3.85 ms                                                      | 3.78 ms: 1.02x faster                                                        |
| meteor_contest          | 131 ms                                                       | 129 ms: 1.02x faster                                                         |
| create_gc_cycles        | 1.61 ms                                                      | 1.58 ms: 1.02x faster                                                        |
| telco                   | 6.86 ms                                                      | 6.76 ms: 1.01x faster                                                        |
| coroutines              | 27.6 ms                                                      | 27.2 ms: 1.01x faster                                                        |
| 2to3                    | 288 ms                                                       | 284 ms: 1.01x faster                                                         |
| async_tree_io           | 1.17 sec                                                     | 1.16 sec: 1.01x faster                                                       |
| sympy_sum               | 185 ms                                                       | 183 ms: 1.01x faster                                                         |
| python_startup          | 10.8 ms                                                      | 10.7 ms: 1.00x faster                                                        |
| regex_dna               | 227 ms                                                       | 229 ms: 1.01x slower                                                         |
| sqlglot_transpile       | 1.92 ms                                                      | 1.93 ms: 1.01x slower                                                        |
| spectral_norm           | 93.3 ms                                                      | 94.2 ms: 1.01x slower                                                        |
| python_startup_no_site  | 7.76 ms                                                      | 7.83 ms: 1.01x slower                                                        |
| pathlib                 | 19.1 ms                                                      | 19.2 ms: 1.01x slower                                                        |
| pickle                  | 9.64 us                                                      | 9.84 us: 1.02x slower                                                        |
| sqlglot_parse           | 1.53 ms                                                      | 1.57 ms: 1.03x slower                                                        |
| sqlite_synth            | 2.50 us                                                      | 2.57 us: 1.03x slower                                                        |
| pickle_dict             | 30.8 us                                                      | 31.7 us: 1.03x slower                                                        |
| async_generators        | 316 ms                                                       | 326 ms: 1.03x slower                                                         |
| mdp                     | 2.75 sec                                                     | 2.83 sec: 1.03x slower                                                       |
| generators              | 56.0 ms                                                      | 59.9 ms: 1.07x slower                                                        |
| coverage                | 84.8 ms                                                      | 93.0 ms: 1.10x slower                                                        |
| comprehensions          | 24.6 us                                                      | 27.2 us: 1.10x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.04x faster                                                                 |

Benchmark hidden because not significant (8): xml_etree_iterparse, nbody, async_tree_cpu_io_mixed, logging_silent, pidigits, pickle_list, dask, bench_mp_pool
Ignored benchmarks (11) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
