
# Results vs. 3.11.0

- fork: python
- ref: 2ac103c346ffe9d0e4c1
- machine: linux-x86_64
- commit hash: 2ac103c
- commit date: 2023-08-07
- overall geometric mean: 1.04x faster
- HPT reliability: 76.53%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 2.92 sec: 1.02x slower                                                      |
| tornado_http   | 122 ms                                                       | 120 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 89.1 ms: 1.02x faster                                                       |
| pidigits       | 251 ms                                                       | 260 ms: 1.03x slower                                                        |
| float          | 74.2 ms                                                      | 81.3 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 151 ms: 1.05x faster                                                        |
| regex_v8       | 23.9 ms                                                      | 24.0 ms: 1.00x slower                                                       |
| regex_effbot   | 3.50 ms                                                      | 3.67 ms: 1.05x slower                                                       |
| regex_dna      | 227 ms                                                       | 252 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                                       |
| json_loads           | 28.7 us                                                      | 25.7 us: 1.12x faster                                                       |
| xml_etree_parse      | 158 ms                                                       | 147 ms: 1.07x faster                                                        |
| unpickle_pure_python | 241 us                                                       | 236 us: 1.02x faster                                                        |
| pickle_pure_python   | 319 us                                                       | 321 us: 1.01x slower                                                        |
| xml_etree_iterparse  | 104 ms                                                       | 106 ms: 1.02x slower                                                        |
| xml_etree_generate   | 80.5 ms                                                      | 84.9 ms: 1.05x slower                                                       |
| xml_etree_process    | 56.5 ms                                                      | 59.6 ms: 1.05x slower                                                       |
| unpickle_list        | 4.53 us                                                      | 4.79 us: 1.06x slower                                                       |
| pickle               | 9.64 us                                                      | 10.2 us: 1.06x slower                                                       |
| pickle_dict          | 30.8 us                                                      | 32.7 us: 1.06x slower                                                       |
| tomli_loads          | 2.26 sec                                                     | 2.41 sec: 1.06x slower                                                      |
| unpickle             | 13.4 us                                                      | 15.1 us: 1.12x slower                                                       |
| pickle_list          | 3.83 us                                                      | 4.54 us: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.6 ms: 1.08x slower                                                       |
| python_startup_no_site | 7.76 ms                                                      | 8.63 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c |
|-----------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.3 ms: 1.07x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230807-pythonperf2-x86_64-python-2ac103c346ffe9d0e4c1-3.13.0a0-2ac103c |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 156 us: 3.34x faster                                                        |
| asyncio_tcp              | 753 ms                                                       | 369 ms: 2.04x faster                                                        |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.58 sec: 1.95x faster                                                      |
| generators               | 56.0 ms                                                      | 37.4 ms: 1.50x faster                                                       |
| json_dumps               | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                                       |
| chaos                    | 80.9 ms                                                      | 62.7 ms: 1.29x faster                                                       |
| mypy2                    | 451 ms                                                       | 372 ms: 1.21x faster                                                        |
| coroutines               | 27.6 ms                                                      | 23.7 ms: 1.16x faster                                                       |
| scimark_lu               | 115 ms                                                       | 99.0 ms: 1.16x faster                                                       |
| raytrace                 | 317 ms                                                       | 281 ms: 1.13x faster                                                        |
| crypto_pyaes             | 83.4 ms                                                      | 74.4 ms: 1.12x faster                                                       |
| nqueens                  | 103 ms                                                       | 91.9 ms: 1.12x faster                                                       |
| json_loads               | 28.7 us                                                      | 25.7 us: 1.12x faster                                                       |
| comprehensions           | 24.6 us                                                      | 22.1 us: 1.11x faster                                                       |
| async_tree_memoization   | 630 ms                                                       | 567 ms: 1.11x faster                                                        |
| async_tree_none          | 519 ms                                                       | 470 ms: 1.10x faster                                                        |
| gc_traversal             | 3.85 ms                                                      | 3.52 ms: 1.09x faster                                                       |
| hexiom                   | 7.13 ms                                                      | 6.53 ms: 1.09x faster                                                       |
| logging_format           | 8.11 us                                                      | 7.44 us: 1.09x faster                                                       |
| deltablue                | 4.00 ms                                                      | 3.67 ms: 1.09x faster                                                       |
| fannkuch                 | 429 ms                                                       | 394 ms: 1.09x faster                                                        |
| async_tree_io            | 1.17 sec                                                     | 1.08 sec: 1.08x faster                                                      |
| json                     | 5.65 ms                                                      | 5.22 ms: 1.08x faster                                                       |
| mdp                      | 2.75 sec                                                     | 2.55 sec: 1.08x faster                                                      |
| sqlglot_parse            | 1.53 ms                                                      | 1.43 ms: 1.07x faster                                                       |
| sqlglot_normalize        | 126 ms                                                       | 118 ms: 1.07x faster                                                        |
| xml_etree_parse          | 158 ms                                                       | 147 ms: 1.07x faster                                                        |
| mako                     | 11.0 ms                                                      | 10.3 ms: 1.07x faster                                                       |
| logging_simple           | 7.19 us                                                      | 6.83 us: 1.05x faster                                                       |
| bench_thread_pool        | 1.01 ms                                                      | 961 us: 1.05x faster                                                        |
| sqlglot_transpile        | 1.92 ms                                                      | 1.83 ms: 1.05x faster                                                       |
| regex_compile            | 158 ms                                                       | 151 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 717 ms: 1.04x faster                                                        |
| deepcopy                 | 399 us                                                       | 384 us: 1.04x faster                                                        |
| logging_silent           | 101 ns                                                       | 97.0 ns: 1.04x faster                                                       |
| deepcopy_memo            | 38.8 us                                                      | 37.7 us: 1.03x faster                                                       |
| deepcopy_reduce          | 3.51 us                                                      | 3.44 us: 1.02x faster                                                       |
| nbody                    | 90.7 ms                                                      | 89.1 ms: 1.02x faster                                                       |
| unpickle_pure_python     | 241 us                                                       | 236 us: 1.02x faster                                                        |
| sqlglot_optimize         | 59.8 ms                                                      | 58.8 ms: 1.02x faster                                                       |
| tornado_http             | 122 ms                                                       | 120 ms: 1.01x faster                                                        |
| meteor_contest           | 131 ms                                                       | 130 ms: 1.00x faster                                                        |
| regex_v8                 | 23.9 ms                                                      | 24.0 ms: 1.00x slower                                                       |
| scimark_monte_carlo      | 68.2 ms                                                      | 68.7 ms: 1.01x slower                                                       |
| pickle_pure_python       | 319 us                                                       | 321 us: 1.01x slower                                                        |
| pprint_pformat           | 1.63 sec                                                     | 1.65 sec: 1.01x slower                                                      |
| xml_etree_iterparse      | 104 ms                                                       | 106 ms: 1.02x slower                                                        |
| richards_super           | 61.0 ms                                                      | 62.0 ms: 1.02x slower                                                       |
| spectral_norm            | 93.3 ms                                                      | 94.8 ms: 1.02x slower                                                       |
| create_gc_cycles         | 1.61 ms                                                      | 1.64 ms: 1.02x slower                                                       |
| docutils                 | 2.86 sec                                                     | 2.92 sec: 1.02x slower                                                      |
| pathlib                  | 19.1 ms                                                      | 19.5 ms: 1.02x slower                                                       |
| pprint_safe_repr         | 784 ms                                                       | 808 ms: 1.03x slower                                                        |
| pidigits                 | 251 ms                                                       | 260 ms: 1.03x slower                                                        |
| bench_mp_pool            | 4.62 ms                                                      | 4.83 ms: 1.04x slower                                                       |
| regex_effbot             | 3.50 ms                                                      | 3.67 ms: 1.05x slower                                                       |
| xml_etree_generate       | 80.5 ms                                                      | 84.9 ms: 1.05x slower                                                       |
| xml_etree_process        | 56.5 ms                                                      | 59.6 ms: 1.05x slower                                                       |
| coverage                 | 84.8 ms                                                      | 89.4 ms: 1.05x slower                                                       |
| unpickle_list            | 4.53 us                                                      | 4.79 us: 1.06x slower                                                       |
| pickle                   | 9.64 us                                                      | 10.2 us: 1.06x slower                                                       |
| unpack_sequence          | 45.6 ns                                                      | 48.4 ns: 1.06x slower                                                       |
| pickle_dict              | 30.8 us                                                      | 32.7 us: 1.06x slower                                                       |
| go                       | 164 ms                                                       | 174 ms: 1.06x slower                                                        |
| tomli_loads              | 2.26 sec                                                     | 2.41 sec: 1.06x slower                                                      |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.34 ms: 1.07x slower                                                       |
| scimark_fft              | 285 ms                                                       | 308 ms: 1.08x slower                                                        |
| python_startup           | 10.8 ms                                                      | 11.6 ms: 1.08x slower                                                       |
| float                    | 74.2 ms                                                      | 81.3 ms: 1.10x slower                                                       |
| sqlite_synth             | 2.50 us                                                      | 2.76 us: 1.11x slower                                                       |
| regex_dna                | 227 ms                                                       | 252 ms: 1.11x slower                                                        |
| python_startup_no_site   | 7.76 ms                                                      | 8.63 ms: 1.11x slower                                                       |
| unpickle                 | 13.4 us                                                      | 15.1 us: 1.12x slower                                                       |
| pyflate                  | 449 ms                                                       | 514 ms: 1.15x slower                                                        |
| richards                 | 48.3 ms                                                      | 55.5 ms: 1.15x slower                                                       |
| pickle_list              | 3.83 us                                                      | 4.54 us: 1.18x slower                                                       |
| telco                    | 6.86 ms                                                      | 8.15 ms: 1.19x slower                                                       |
| async_generators         | 316 ms                                                       | 395 ms: 1.25x slower                                                        |
| scimark_sor              | 111 ms                                                       | 144 ms: 1.30x slower                                                        |
| dask                     | 410 ms                                                       | 589 ms: 1.44x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (2): dulwich_log, pycparser
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 76.53% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
