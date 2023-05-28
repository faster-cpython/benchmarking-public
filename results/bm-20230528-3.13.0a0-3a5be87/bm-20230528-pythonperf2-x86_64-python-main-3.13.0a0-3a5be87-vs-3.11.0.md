
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3a5be87
- commit date: 2023-05-28
- overall geometric mean: 1.07x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-pythonperf2-x86_64-python-main-3.13.0a0-3a5be87 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 2.87 sec: 1.00x slower                                      |
| html5lib       | 72.9 ms                                                      | 68.7 ms: 1.06x faster                                       |
| tornado_http   | 122 ms                                                       | 114 ms: 1.06x faster                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-pythonperf2-x86_64-python-main-3.13.0a0-3a5be87 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 86.3 ms: 1.05x faster                                       |
| pidigits       | 251 ms                                                       | 260 ms: 1.04x slower                                        |
| float          | 74.2 ms                                                      | 78.7 ms: 1.06x slower                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-pythonperf2-x86_64-python-main-3.13.0a0-3a5be87 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 143 ms: 1.10x faster                                        |
| regex_v8       | 23.9 ms                                                      | 24.6 ms: 1.03x slower                                       |
| regex_effbot   | 3.50 ms                                                      | 3.68 ms: 1.05x slower                                       |
| regex_dna      | 227 ms                                                       | 245 ms: 1.08x slower                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-pythonperf2-x86_64-python-main-3.13.0a0-3a5be87 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.3 ms: 1.31x faster                                       |
| json_loads           | 28.7 us                                                      | 24.1 us: 1.19x faster                                       |
| unpickle_pure_python | 241 us                                                       | 205 us: 1.18x faster                                        |
| xml_etree_parse      | 158 ms                                                       | 147 ms: 1.07x faster                                        |
| tomli_loads          | 2.26 sec                                                     | 2.19 sec: 1.03x faster                                      |
| pickle_pure_python   | 319 us                                                       | 318 us: 1.00x faster                                        |
| xml_etree_process    | 56.5 ms                                                      | 58.6 ms: 1.04x slower                                       |
| unpickle_list        | 4.53 us                                                      | 4.72 us: 1.04x slower                                       |
| xml_etree_generate   | 80.5 ms                                                      | 86.1 ms: 1.07x slower                                       |
| pickle               | 9.64 us                                                      | 10.3 us: 1.07x slower                                       |
| pickle_dict          | 30.8 us                                                      | 33.0 us: 1.07x slower                                       |
| unpickle             | 13.4 us                                                      | 14.6 us: 1.08x slower                                       |
| pickle_list          | 3.83 us                                                      | 4.43 us: 1.16x slower                                       |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-pythonperf2-x86_64-python-main-3.13.0a0-3a5be87 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                       |
| python_startup_no_site | 7.76 ms                                                      | 8.49 ms: 1.09x slower                                       |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-pythonperf2-x86_64-python-main-3.13.0a0-3a5be87 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako           | 11.0 ms                                                      | 9.94 ms: 1.11x faster                                       |
| genshi_xml     | 58.5 ms                                                      | 53.8 ms: 1.09x faster                                       |
| genshi_text    | 26.1 ms                                                      | 24.9 ms: 1.05x faster                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-pythonperf2-x86_64-python-main-3.13.0a0-3a5be87 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 146 us: 3.58x faster                                        |
| asyncio_tcp              | 753 ms                                                       | 381 ms: 1.98x faster                                        |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.57 sec: 1.96x faster                                      |
| generators               | 56.0 ms                                                      | 35.4 ms: 1.58x faster                                       |
| json_dumps               | 13.4 ms                                                      | 10.3 ms: 1.31x faster                                       |
| chaos                    | 80.9 ms                                                      | 63.4 ms: 1.28x faster                                       |
| deltablue                | 4.00 ms                                                      | 3.19 ms: 1.25x faster                                       |
| fannkuch                 | 429 ms                                                       | 344 ms: 1.25x faster                                        |
| mypy2                    | 451 ms                                                       | 362 ms: 1.25x faster                                        |
| hexiom                   | 7.13 ms                                                      | 5.76 ms: 1.24x faster                                       |
| richards_super           | 61.0 ms                                                      | 50.6 ms: 1.21x faster                                       |
| coroutines               | 27.6 ms                                                      | 22.9 ms: 1.20x faster                                       |
| json_loads               | 28.7 us                                                      | 24.1 us: 1.19x faster                                       |
| unpickle_pure_python     | 241 us                                                       | 205 us: 1.18x faster                                        |
| nqueens                  | 103 ms                                                       | 89.4 ms: 1.15x faster                                       |
| scimark_lu               | 115 ms                                                       | 101 ms: 1.14x faster                                        |
| comprehensions           | 24.6 us                                                      | 21.6 us: 1.14x faster                                       |
| go                       | 164 ms                                                       | 145 ms: 1.13x faster                                        |
| async_tree_memoization   | 630 ms                                                       | 562 ms: 1.12x faster                                        |
| json                     | 5.65 ms                                                      | 5.07 ms: 1.11x faster                                       |
| async_tree_none          | 519 ms                                                       | 467 ms: 1.11x faster                                        |
| logging_silent           | 101 ns                                                       | 90.9 ns: 1.11x faster                                       |
| logging_format           | 8.11 us                                                      | 7.34 us: 1.11x faster                                       |
| mako                     | 11.0 ms                                                      | 9.94 ms: 1.11x faster                                       |
| sqlglot_parse            | 1.53 ms                                                      | 1.39 ms: 1.11x faster                                       |
| regex_compile            | 158 ms                                                       | 143 ms: 1.10x faster                                        |
| mdp                      | 2.75 sec                                                     | 2.51 sec: 1.09x faster                                      |
| async_tree_io            | 1.17 sec                                                     | 1.07 sec: 1.09x faster                                      |
| sqlglot_normalize        | 126 ms                                                       | 115 ms: 1.09x faster                                        |
| genshi_xml               | 58.5 ms                                                      | 53.8 ms: 1.09x faster                                       |
| richards                 | 48.3 ms                                                      | 44.6 ms: 1.08x faster                                       |
| sqlglot_transpile        | 1.92 ms                                                      | 1.79 ms: 1.07x faster                                       |
| xml_etree_parse          | 158 ms                                                       | 147 ms: 1.07x faster                                        |
| tornado_http             | 122 ms                                                       | 114 ms: 1.06x faster                                        |
| logging_simple           | 7.19 us                                                      | 6.76 us: 1.06x faster                                       |
| html5lib                 | 72.9 ms                                                      | 68.7 ms: 1.06x faster                                       |
| scimark_sor              | 111 ms                                                       | 105 ms: 1.06x faster                                        |
| bench_thread_pool        | 1.01 ms                                                      | 954 us: 1.06x faster                                        |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 710 ms: 1.06x faster                                        |
| dulwich_log              | 68.4 ms                                                      | 64.9 ms: 1.05x faster                                       |
| deepcopy                 | 399 us                                                       | 379 us: 1.05x faster                                        |
| deepcopy_memo            | 38.8 us                                                      | 36.9 us: 1.05x faster                                       |
| nbody                    | 90.7 ms                                                      | 86.3 ms: 1.05x faster                                       |
| raytrace                 | 317 ms                                                       | 301 ms: 1.05x faster                                        |
| genshi_text              | 26.1 ms                                                      | 24.9 ms: 1.05x faster                                       |
| sqlglot_optimize         | 59.8 ms                                                      | 57.2 ms: 1.04x faster                                       |
| spectral_norm            | 93.3 ms                                                      | 89.4 ms: 1.04x faster                                       |
| pycparser                | 1.32 sec                                                     | 1.27 sec: 1.04x faster                                      |
| tomli_loads              | 2.26 sec                                                     | 2.19 sec: 1.03x faster                                      |
| deepcopy_reduce          | 3.51 us                                                      | 3.42 us: 1.03x faster                                       |
| meteor_contest           | 131 ms                                                       | 127 ms: 1.03x faster                                        |
| pyflate                  | 449 ms                                                       | 437 ms: 1.03x faster                                        |
| gc_traversal             | 3.85 ms                                                      | 3.76 ms: 1.02x faster                                       |
| pprint_pformat           | 1.63 sec                                                     | 1.62 sec: 1.01x faster                                      |
| crypto_pyaes             | 83.4 ms                                                      | 83.0 ms: 1.01x faster                                       |
| pickle_pure_python       | 319 us                                                       | 318 us: 1.00x faster                                        |
| docutils                 | 2.86 sec                                                     | 2.87 sec: 1.00x slower                                      |
| pprint_safe_repr         | 784 ms                                                       | 796 ms: 1.01x slower                                        |
| regex_v8                 | 23.9 ms                                                      | 24.6 ms: 1.03x slower                                       |
| create_gc_cycles         | 1.61 ms                                                      | 1.66 ms: 1.03x slower                                       |
| pidigits                 | 251 ms                                                       | 260 ms: 1.04x slower                                        |
| xml_etree_process        | 56.5 ms                                                      | 58.6 ms: 1.04x slower                                       |
| unpickle_list            | 4.53 us                                                      | 4.72 us: 1.04x slower                                       |
| telco                    | 6.86 ms                                                      | 7.16 ms: 1.04x slower                                       |
| regex_effbot             | 3.50 ms                                                      | 3.68 ms: 1.05x slower                                       |
| python_startup           | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                       |
| coverage                 | 84.8 ms                                                      | 89.4 ms: 1.05x slower                                       |
| float                    | 74.2 ms                                                      | 78.7 ms: 1.06x slower                                       |
| scimark_fft              | 285 ms                                                       | 303 ms: 1.06x slower                                        |
| xml_etree_generate       | 80.5 ms                                                      | 86.1 ms: 1.07x slower                                       |
| pickle                   | 9.64 us                                                      | 10.3 us: 1.07x slower                                       |
| pathlib                  | 19.1 ms                                                      | 20.4 ms: 1.07x slower                                       |
| pickle_dict              | 30.8 us                                                      | 33.0 us: 1.07x slower                                       |
| scimark_monte_carlo      | 68.2 ms                                                      | 73.5 ms: 1.08x slower                                       |
| regex_dna                | 227 ms                                                       | 245 ms: 1.08x slower                                        |
| unpickle                 | 13.4 us                                                      | 14.6 us: 1.08x slower                                       |
| sqlite_synth             | 2.50 us                                                      | 2.73 us: 1.09x slower                                       |
| python_startup_no_site   | 7.76 ms                                                      | 8.49 ms: 1.09x slower                                       |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.43 ms: 1.09x slower                                       |
| unpack_sequence          | 45.6 ns                                                      | 51.8 ns: 1.13x slower                                       |
| pickle_list              | 3.83 us                                                      | 4.43 us: 1.16x slower                                       |
| async_generators         | 316 ms                                                       | 390 ms: 1.24x slower                                        |
| bench_mp_pool            | 4.62 ms                                                      | 6.22 ms: 1.34x slower                                       |
| Geometric mean           | (ref)                                                        | 1.07x faster                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
