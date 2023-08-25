
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: a47c13c
- commit date: 2023-08-19
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-pythonperf2-x86_64-python-main-3.13.0a0-a47c13c |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 3.40 sec                                                     | 2.87 sec: 1.19x faster                                      |
| tornado_http   | 152 ms                                                       | 120 ms: 1.26x faster                                        |
| Geometric mean | (ref)                                                        | 1.22x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-pythonperf2-x86_64-python-main-3.13.0a0-a47c13c |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 137 ms                                                       | 84.9 ms: 1.62x faster                                       |
| float          | 110 ms                                                       | 77.4 ms: 1.42x faster                                       |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                        |
| Geometric mean | (ref)                                                        | 1.34x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-pythonperf2-x86_64-python-main-3.13.0a0-a47c13c |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 148 ms: 1.30x faster                                        |
| regex_dna      | 259 ms                                                       | 248 ms: 1.05x faster                                        |
| regex_v8       | 26.6 ms                                                      | 26.3 ms: 1.01x faster                                       |
| regex_effbot   | 2.99 ms                                                      | 3.71 ms: 1.24x slower                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-pythonperf2-x86_64-python-main-3.13.0a0-a47c13c |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                       | 317 us: 1.44x faster                                        |
| unpickle_pure_python | 321 us                                                       | 228 us: 1.41x faster                                        |
| json_dumps           | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                       |
| tomli_loads          | 2.97 sec                                                     | 2.23 sec: 1.33x faster                                      |
| xml_etree_process    | 76.0 ms                                                      | 58.8 ms: 1.29x faster                                       |
| json_loads           | 30.0 us                                                      | 25.2 us: 1.19x faster                                       |
| xml_etree_parse      | 162 ms                                                       | 145 ms: 1.11x faster                                        |
| xml_etree_generate   | 94.6 ms                                                      | 86.6 ms: 1.09x faster                                       |
| xml_etree_iterparse  | 110 ms                                                       | 106 ms: 1.05x faster                                        |
| unpickle             | 14.2 us                                                      | 14.4 us: 1.01x slower                                       |
| pickle               | 9.94 us                                                      | 10.1 us: 1.02x slower                                       |
| unpickle_list        | 4.49 us                                                      | 4.60 us: 1.02x slower                                       |
| pickle_list          | 4.11 us                                                      | 4.38 us: 1.07x slower                                       |
| pickle_dict          | 30.0 us                                                      | 32.5 us: 1.08x slower                                       |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-pythonperf2-x86_64-python-main-3.13.0a0-a47c13c |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.6 ms: 1.01x slower                                       |
| python_startup_no_site | 7.32 ms                                                      | 8.64 ms: 1.18x slower                                       |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-pythonperf2-x86_64-python-main-3.13.0a0-a47c13c |
|-----------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-pythonperf2-x86_64-python-main-3.13.0a0-a47c13c |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 150 us: 3.49x faster                                        |
| asyncio_tcp              | 782 ms                                                       | 372 ms: 2.10x faster                                        |
| deltablue                | 7.47 ms                                                      | 3.71 ms: 2.01x faster                                       |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.58 sec: 1.96x faster                                      |
| raytrace                 | 488 ms                                                       | 274 ms: 1.78x faster                                        |
| chaos                    | 107 ms                                                       | 62.4 ms: 1.72x faster                                       |
| logging_silent           | 166 ns                                                       | 100 ns: 1.66x faster                                        |
| scimark_lu               | 164 ms                                                       | 101 ms: 1.63x faster                                        |
| nbody                    | 137 ms                                                       | 84.9 ms: 1.62x faster                                       |
| crypto_pyaes             | 118 ms                                                       | 73.2 ms: 1.61x faster                                       |
| generators               | 58.0 ms                                                      | 36.2 ms: 1.60x faster                                       |
| bench_mp_pool            | 7.18 ms                                                      | 4.48 ms: 1.60x faster                                       |
| scimark_monte_carlo      | 109 ms                                                       | 68.5 ms: 1.60x faster                                       |
| async_tree_none          | 700 ms                                                       | 441 ms: 1.59x faster                                        |
| sqlglot_parse            | 2.26 ms                                                      | 1.43 ms: 1.58x faster                                       |
| go                       | 259 ms                                                       | 170 ms: 1.52x faster                                        |
| richards_super           | 90.8 ms                                                      | 60.6 ms: 1.50x faster                                       |
| async_tree_memoization   | 824 ms                                                       | 555 ms: 1.49x faster                                        |
| async_tree_io            | 1.61 sec                                                     | 1.09 sec: 1.47x faster                                      |
| sqlglot_transpile        | 2.71 ms                                                      | 1.85 ms: 1.47x faster                                       |
| hexiom                   | 9.52 ms                                                      | 6.52 ms: 1.46x faster                                       |
| pickle_pure_python       | 457 us                                                       | 317 us: 1.44x faster                                        |
| float                    | 110 ms                                                       | 77.4 ms: 1.42x faster                                       |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                       |
| unpickle_pure_python     | 321 us                                                       | 228 us: 1.41x faster                                        |
| json_dumps               | 14.2 ms                                                      | 10.3 ms: 1.38x faster                                       |
| richards                 | 74.1 ms                                                      | 53.8 ms: 1.38x faster                                       |
| pyflate                  | 697 ms                                                       | 509 ms: 1.37x faster                                        |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 704 ms: 1.35x faster                                        |
| spectral_norm            | 136 ms                                                       | 101 ms: 1.34x faster                                        |
| tomli_loads              | 2.97 sec                                                     | 2.23 sec: 1.33x faster                                      |
| coroutines               | 30.4 ms                                                      | 22.9 ms: 1.33x faster                                       |
| logging_simple           | 8.90 us                                                      | 6.74 us: 1.32x faster                                       |
| regex_compile            | 194 ms                                                       | 148 ms: 1.30x faster                                        |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 3.99 ms: 1.30x faster                                       |
| xml_etree_process        | 76.0 ms                                                      | 58.8 ms: 1.29x faster                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.67 sec: 1.29x faster                                      |
| logging_format           | 9.57 us                                                      | 7.45 us: 1.28x faster                                       |
| deepcopy_memo            | 48.9 us                                                      | 38.1 us: 1.28x faster                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 819 ms: 1.28x faster                                        |
| tornado_http             | 152 ms                                                       | 120 ms: 1.26x faster                                        |
| nqueens                  | 112 ms                                                       | 89.9 ms: 1.25x faster                                       |
| fannkuch                 | 496 ms                                                       | 399 ms: 1.24x faster                                        |
| sqlglot_normalize        | 144 ms                                                       | 116 ms: 1.24x faster                                        |
| pycparser                | 1.66 sec                                                     | 1.34 sec: 1.24x faster                                      |
| scimark_fft              | 359 ms                                                       | 294 ms: 1.22x faster                                        |
| comprehensions           | 26.9 us                                                      | 22.2 us: 1.21x faster                                       |
| sqlglot_optimize         | 70.3 ms                                                      | 58.3 ms: 1.20x faster                                       |
| scimark_sor              | 177 ms                                                       | 147 ms: 1.20x faster                                        |
| deepcopy_reduce          | 4.03 us                                                      | 3.38 us: 1.19x faster                                       |
| mdp                      | 3.03 sec                                                     | 2.54 sec: 1.19x faster                                      |
| deepcopy                 | 454 us                                                       | 381 us: 1.19x faster                                        |
| json_loads               | 30.0 us                                                      | 25.2 us: 1.19x faster                                       |
| docutils                 | 3.40 sec                                                     | 2.87 sec: 1.19x faster                                      |
| bench_thread_pool        | 1.14 ms                                                      | 978 us: 1.16x faster                                        |
| dulwich_log              | 80.1 ms                                                      | 68.9 ms: 1.16x faster                                       |
| json                     | 5.96 ms                                                      | 5.20 ms: 1.15x faster                                       |
| create_gc_cycles         | 1.82 ms                                                      | 1.59 ms: 1.14x faster                                       |
| pathlib                  | 21.7 ms                                                      | 19.3 ms: 1.12x faster                                       |
| xml_etree_parse          | 162 ms                                                       | 145 ms: 1.11x faster                                        |
| xml_etree_generate       | 94.6 ms                                                      | 86.6 ms: 1.09x faster                                       |
| sqlite_synth             | 2.97 us                                                      | 2.72 us: 1.09x faster                                       |
| async_generators         | 422 ms                                                       | 392 ms: 1.08x faster                                        |
| regex_dna                | 259 ms                                                       | 248 ms: 1.05x faster                                        |
| meteor_contest           | 137 ms                                                       | 131 ms: 1.05x faster                                        |
| xml_etree_iterparse      | 110 ms                                                       | 106 ms: 1.05x faster                                        |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                        |
| regex_v8                 | 26.6 ms                                                      | 26.3 ms: 1.01x faster                                       |
| python_startup           | 11.5 ms                                                      | 11.6 ms: 1.01x slower                                       |
| unpickle                 | 14.2 us                                                      | 14.4 us: 1.01x slower                                       |
| pickle                   | 9.94 us                                                      | 10.1 us: 1.02x slower                                       |
| unpickle_list            | 4.49 us                                                      | 4.60 us: 1.02x slower                                       |
| unpack_sequence          | 59.5 ns                                                      | 62.6 ns: 1.05x slower                                       |
| pickle_list              | 4.11 us                                                      | 4.38 us: 1.07x slower                                       |
| pickle_dict              | 30.0 us                                                      | 32.5 us: 1.08x slower                                       |
| gc_traversal             | 3.45 ms                                                      | 3.75 ms: 1.09x slower                                       |
| telco                    | 7.14 ms                                                      | 7.94 ms: 1.11x slower                                       |
| python_startup_no_site   | 7.32 ms                                                      | 8.64 ms: 1.18x slower                                       |
| regex_effbot             | 2.99 ms                                                      | 3.71 ms: 1.24x slower                                       |
| dask                     | 463 ms                                                       | 589 ms: 1.27x slower                                        |
| coverage                 | 64.0 ms                                                      | 84.0 ms: 1.31x slower                                       |
| Geometric mean           | (ref)                                                        | 1.27x faster                                                |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x
