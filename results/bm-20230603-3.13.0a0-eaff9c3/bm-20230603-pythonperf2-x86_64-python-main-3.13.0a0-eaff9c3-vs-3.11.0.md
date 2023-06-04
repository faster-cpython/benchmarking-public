
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: eaff9c3
- commit date: 2023-06-03
- overall geometric mean: 1.08x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-pythonperf2-x86_64-python-main-3.13.0a0-eaff9c3 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 2.89 sec: 1.01x slower                                      |
| tornado_http   | 122 ms                                                       | 115 ms: 1.05x faster                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-pythonperf2-x86_64-python-main-3.13.0a0-eaff9c3 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 85.6 ms: 1.06x faster                                       |
| pidigits       | 251 ms                                                       | 261 ms: 1.04x slower                                        |
| float          | 74.2 ms                                                      | 78.2 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-pythonperf2-x86_64-python-main-3.13.0a0-eaff9c3 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 144 ms: 1.09x faster                                        |
| regex_v8       | 23.9 ms                                                      | 24.5 ms: 1.02x slower                                       |
| regex_effbot   | 3.50 ms                                                      | 3.67 ms: 1.05x slower                                       |
| regex_dna      | 227 ms                                                       | 246 ms: 1.08x slower                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-pythonperf2-x86_64-python-main-3.13.0a0-eaff9c3 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                       |
| json_loads           | 28.7 us                                                      | 24.0 us: 1.20x faster                                       |
| unpickle_pure_python | 241 us                                                       | 208 us: 1.16x faster                                        |
| xml_etree_parse      | 158 ms                                                       | 146 ms: 1.08x faster                                        |
| tomli_loads          | 2.26 sec                                                     | 2.16 sec: 1.05x faster                                      |
| xml_etree_iterparse  | 104 ms                                                       | 103 ms: 1.01x faster                                        |
| pickle_pure_python   | 319 us                                                       | 324 us: 1.02x slower                                        |
| pickle               | 9.64 us                                                      | 9.96 us: 1.03x slower                                       |
| xml_etree_process    | 56.5 ms                                                      | 58.4 ms: 1.03x slower                                       |
| pickle_dict          | 30.8 us                                                      | 31.9 us: 1.04x slower                                       |
| unpickle_list        | 4.53 us                                                      | 4.70 us: 1.04x slower                                       |
| xml_etree_generate   | 80.5 ms                                                      | 85.4 ms: 1.06x slower                                       |
| unpickle             | 13.4 us                                                      | 14.3 us: 1.07x slower                                       |
| pickle_list          | 3.83 us                                                      | 4.40 us: 1.15x slower                                       |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-pythonperf2-x86_64-python-main-3.13.0a0-eaff9c3 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                       |
| python_startup_no_site | 7.76 ms                                                      | 8.43 ms: 1.09x slower                                       |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-pythonperf2-x86_64-python-main-3.13.0a0-eaff9c3 |
|-----------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.1 ms: 1.09x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-pythonperf2-x86_64-python-main-3.13.0a0-eaff9c3 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 149 us: 3.52x faster                                        |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.57 sec: 1.97x faster                                      |
| asyncio_tcp              | 753 ms                                                       | 383 ms: 1.96x faster                                        |
| generators               | 56.0 ms                                                      | 35.5 ms: 1.58x faster                                       |
| json_dumps               | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                       |
| chaos                    | 80.9 ms                                                      | 63.3 ms: 1.28x faster                                       |
| deltablue                | 4.00 ms                                                      | 3.23 ms: 1.24x faster                                       |
| mypy2                    | 451 ms                                                       | 366 ms: 1.23x faster                                        |
| hexiom                   | 7.13 ms                                                      | 5.86 ms: 1.22x faster                                       |
| coroutines               | 27.6 ms                                                      | 22.8 ms: 1.21x faster                                       |
| json_loads               | 28.7 us                                                      | 24.0 us: 1.20x faster                                       |
| fannkuch                 | 429 ms                                                       | 361 ms: 1.19x faster                                        |
| scimark_lu               | 115 ms                                                       | 97.0 ms: 1.18x faster                                       |
| richards_super           | 61.0 ms                                                      | 52.4 ms: 1.17x faster                                       |
| unpickle_pure_python     | 241 us                                                       | 208 us: 1.16x faster                                        |
| comprehensions           | 24.6 us                                                      | 21.5 us: 1.14x faster                                       |
| nqueens                  | 103 ms                                                       | 91.0 ms: 1.13x faster                                       |
| async_tree_memoization   | 630 ms                                                       | 558 ms: 1.13x faster                                        |
| go                       | 164 ms                                                       | 146 ms: 1.12x faster                                        |
| logging_format           | 8.11 us                                                      | 7.27 us: 1.12x faster                                       |
| async_tree_none          | 519 ms                                                       | 467 ms: 1.11x faster                                        |
| sqlglot_parse            | 1.53 ms                                                      | 1.39 ms: 1.11x faster                                       |
| json                     | 5.65 ms                                                      | 5.16 ms: 1.09x faster                                       |
| regex_compile            | 158 ms                                                       | 144 ms: 1.09x faster                                        |
| async_tree_io            | 1.17 sec                                                     | 1.07 sec: 1.09x faster                                      |
| sqlglot_normalize        | 126 ms                                                       | 115 ms: 1.09x faster                                        |
| mako                     | 11.0 ms                                                      | 10.1 ms: 1.09x faster                                       |
| gc_traversal             | 3.85 ms                                                      | 3.56 ms: 1.08x faster                                       |
| xml_etree_parse          | 158 ms                                                       | 146 ms: 1.08x faster                                        |
| sqlglot_transpile        | 1.92 ms                                                      | 1.78 ms: 1.08x faster                                       |
| logging_simple           | 7.19 us                                                      | 6.69 us: 1.08x faster                                       |
| mdp                      | 2.75 sec                                                     | 2.56 sec: 1.07x faster                                      |
| bench_thread_pool        | 1.01 ms                                                      | 947 us: 1.07x faster                                        |
| deepcopy                 | 399 us                                                       | 376 us: 1.06x faster                                        |
| logging_silent           | 101 ns                                                       | 94.9 ns: 1.06x faster                                       |
| nbody                    | 90.7 ms                                                      | 85.6 ms: 1.06x faster                                       |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 709 ms: 1.06x faster                                        |
| deepcopy_memo            | 38.8 us                                                      | 36.8 us: 1.05x faster                                       |
| tornado_http             | 122 ms                                                       | 115 ms: 1.05x faster                                        |
| richards                 | 48.3 ms                                                      | 45.9 ms: 1.05x faster                                       |
| dulwich_log              | 68.4 ms                                                      | 65.3 ms: 1.05x faster                                       |
| tomli_loads              | 2.26 sec                                                     | 2.16 sec: 1.05x faster                                      |
| sqlglot_optimize         | 59.8 ms                                                      | 57.5 ms: 1.04x faster                                       |
| meteor_contest           | 131 ms                                                       | 126 ms: 1.04x faster                                        |
| crypto_pyaes             | 83.4 ms                                                      | 80.8 ms: 1.03x faster                                       |
| raytrace                 | 317 ms                                                       | 307 ms: 1.03x faster                                        |
| deepcopy_reduce          | 3.51 us                                                      | 3.41 us: 1.03x faster                                       |
| pycparser                | 1.32 sec                                                     | 1.29 sec: 1.03x faster                                      |
| scimark_sor              | 111 ms                                                       | 108 ms: 1.03x faster                                        |
| xml_etree_iterparse      | 104 ms                                                       | 103 ms: 1.01x faster                                        |
| pyflate                  | 449 ms                                                       | 443 ms: 1.01x faster                                        |
| spectral_norm            | 93.3 ms                                                      | 92.8 ms: 1.01x faster                                       |
| scimark_monte_carlo      | 68.2 ms                                                      | 68.7 ms: 1.01x slower                                       |
| docutils                 | 2.86 sec                                                     | 2.89 sec: 1.01x slower                                      |
| pprint_pformat           | 1.63 sec                                                     | 1.65 sec: 1.01x slower                                      |
| pickle_pure_python       | 319 us                                                       | 324 us: 1.02x slower                                        |
| pathlib                  | 19.1 ms                                                      | 19.5 ms: 1.02x slower                                       |
| regex_v8                 | 23.9 ms                                                      | 24.5 ms: 1.02x slower                                       |
| pprint_safe_repr         | 784 ms                                                       | 808 ms: 1.03x slower                                        |
| pickle                   | 9.64 us                                                      | 9.96 us: 1.03x slower                                       |
| xml_etree_process        | 56.5 ms                                                      | 58.4 ms: 1.03x slower                                       |
| pickle_dict              | 30.8 us                                                      | 31.9 us: 1.04x slower                                       |
| unpickle_list            | 4.53 us                                                      | 4.70 us: 1.04x slower                                       |
| pidigits                 | 251 ms                                                       | 261 ms: 1.04x slower                                        |
| telco                    | 6.86 ms                                                      | 7.12 ms: 1.04x slower                                       |
| regex_effbot             | 3.50 ms                                                      | 3.67 ms: 1.05x slower                                       |
| float                    | 74.2 ms                                                      | 78.2 ms: 1.05x slower                                       |
| python_startup           | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                       |
| xml_etree_generate       | 80.5 ms                                                      | 85.4 ms: 1.06x slower                                       |
| scimark_fft              | 285 ms                                                       | 302 ms: 1.06x slower                                        |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.32 ms: 1.07x slower                                       |
| unpickle                 | 13.4 us                                                      | 14.3 us: 1.07x slower                                       |
| coverage                 | 84.8 ms                                                      | 91.9 ms: 1.08x slower                                       |
| regex_dna                | 227 ms                                                       | 246 ms: 1.08x slower                                        |
| sqlite_synth             | 2.50 us                                                      | 2.71 us: 1.08x slower                                       |
| python_startup_no_site   | 7.76 ms                                                      | 8.43 ms: 1.09x slower                                       |
| bench_mp_pool            | 4.62 ms                                                      | 5.09 ms: 1.10x slower                                       |
| pickle_list              | 3.83 us                                                      | 4.40 us: 1.15x slower                                       |
| unpack_sequence          | 45.6 ns                                                      | 53.5 ns: 1.17x slower                                       |
| async_generators         | 316 ms                                                       | 391 ms: 1.24x slower                                        |
| Geometric mean           | (ref)                                                        | 1.08x faster                                                |

Benchmark hidden because not significant (1): create_gc_cycles
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
