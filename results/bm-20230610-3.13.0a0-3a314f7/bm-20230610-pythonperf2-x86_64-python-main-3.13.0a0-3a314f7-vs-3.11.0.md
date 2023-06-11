
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3a314f7
- commit date: 2023-06-10
- overall geometric mean: 1.08x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-pythonperf2-x86_64-python-main-3.13.0a0-3a314f7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 2.89 sec: 1.01x slower                                      |
| tornado_http   | 122 ms                                                       | 114 ms: 1.06x faster                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-pythonperf2-x86_64-python-main-3.13.0a0-3a314f7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 86.3 ms: 1.05x faster                                       |
| pidigits       | 251 ms                                                       | 261 ms: 1.04x slower                                        |
| float          | 74.2 ms                                                      | 79.4 ms: 1.07x slower                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-pythonperf2-x86_64-python-main-3.13.0a0-3a314f7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 147 ms: 1.08x faster                                        |
| regex_effbot   | 3.50 ms                                                      | 3.63 ms: 1.04x slower                                       |
| regex_v8       | 23.9 ms                                                      | 24.8 ms: 1.04x slower                                       |
| regex_dna      | 227 ms                                                       | 247 ms: 1.09x slower                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-pythonperf2-x86_64-python-main-3.13.0a0-3a314f7 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.2 ms: 1.32x faster                                       |
| json_loads           | 28.7 us                                                      | 24.2 us: 1.18x faster                                       |
| unpickle_pure_python | 241 us                                                       | 214 us: 1.13x faster                                        |
| xml_etree_parse      | 158 ms                                                       | 146 ms: 1.08x faster                                        |
| xml_etree_iterparse  | 104 ms                                                       | 104 ms: 1.01x faster                                        |
| tomli_loads          | 2.26 sec                                                     | 2.25 sec: 1.01x faster                                      |
| unpickle_list        | 4.53 us                                                      | 4.71 us: 1.04x slower                                       |
| pickle               | 9.64 us                                                      | 10.1 us: 1.04x slower                                       |
| xml_etree_process    | 56.5 ms                                                      | 59.3 ms: 1.05x slower                                       |
| xml_etree_generate   | 80.5 ms                                                      | 85.8 ms: 1.07x slower                                       |
| unpickle             | 13.4 us                                                      | 14.5 us: 1.08x slower                                       |
| pickle_list          | 3.83 us                                                      | 4.37 us: 1.14x slower                                       |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                |

Benchmark hidden because not significant (2): pickle_pure_python, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-pythonperf2-x86_64-python-main-3.13.0a0-3a314f7 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                       |
| python_startup_no_site | 7.76 ms                                                      | 8.29 ms: 1.07x slower                                       |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-pythonperf2-x86_64-python-main-3.13.0a0-3a314f7 |
|-----------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.2 ms: 1.08x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-pythonperf2-x86_64-python-main-3.13.0a0-3a314f7 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 149 us: 3.50x faster                                        |
| asyncio_tcp              | 753 ms                                                       | 381 ms: 1.98x faster                                        |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.57 sec: 1.97x faster                                      |
| generators               | 56.0 ms                                                      | 36.9 ms: 1.52x faster                                       |
| json_dumps               | 13.4 ms                                                      | 10.2 ms: 1.32x faster                                       |
| chaos                    | 80.9 ms                                                      | 63.6 ms: 1.27x faster                                       |
| coroutines               | 27.6 ms                                                      | 21.9 ms: 1.26x faster                                       |
| mypy2                    | 451 ms                                                       | 366 ms: 1.23x faster                                        |
| deltablue                | 4.00 ms                                                      | 3.25 ms: 1.23x faster                                       |
| scimark_lu               | 115 ms                                                       | 93.2 ms: 1.23x faster                                       |
| hexiom                   | 7.13 ms                                                      | 5.89 ms: 1.21x faster                                       |
| fannkuch                 | 429 ms                                                       | 357 ms: 1.20x faster                                        |
| json_loads               | 28.7 us                                                      | 24.2 us: 1.18x faster                                       |
| richards_super           | 61.0 ms                                                      | 52.2 ms: 1.17x faster                                       |
| comprehensions           | 24.6 us                                                      | 21.7 us: 1.13x faster                                       |
| unpickle_pure_python     | 241 us                                                       | 214 us: 1.13x faster                                        |
| nqueens                  | 103 ms                                                       | 91.7 ms: 1.12x faster                                       |
| async_tree_memoization   | 630 ms                                                       | 565 ms: 1.12x faster                                        |
| json                     | 5.65 ms                                                      | 5.12 ms: 1.10x faster                                       |
| sqlglot_parse            | 1.53 ms                                                      | 1.39 ms: 1.10x faster                                       |
| logging_format           | 8.11 us                                                      | 7.36 us: 1.10x faster                                       |
| async_tree_none          | 519 ms                                                       | 472 ms: 1.10x faster                                        |
| logging_silent           | 101 ns                                                       | 91.9 ns: 1.10x faster                                       |
| go                       | 164 ms                                                       | 150 ms: 1.09x faster                                        |
| async_tree_io            | 1.17 sec                                                     | 1.08 sec: 1.08x faster                                      |
| mdp                      | 2.75 sec                                                     | 2.53 sec: 1.08x faster                                      |
| mako                     | 11.0 ms                                                      | 10.2 ms: 1.08x faster                                       |
| sqlglot_normalize        | 126 ms                                                       | 117 ms: 1.08x faster                                        |
| xml_etree_parse          | 158 ms                                                       | 146 ms: 1.08x faster                                        |
| deepcopy                 | 399 us                                                       | 371 us: 1.08x faster                                        |
| regex_compile            | 158 ms                                                       | 147 ms: 1.08x faster                                        |
| sqlglot_transpile        | 1.92 ms                                                      | 1.80 ms: 1.07x faster                                       |
| tornado_http             | 122 ms                                                       | 114 ms: 1.06x faster                                        |
| richards                 | 48.3 ms                                                      | 45.4 ms: 1.06x faster                                       |
| logging_simple           | 7.19 us                                                      | 6.78 us: 1.06x faster                                       |
| spectral_norm            | 93.3 ms                                                      | 88.0 ms: 1.06x faster                                       |
| nbody                    | 90.7 ms                                                      | 86.3 ms: 1.05x faster                                       |
| raytrace                 | 317 ms                                                       | 302 ms: 1.05x faster                                        |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 715 ms: 1.05x faster                                        |
| bench_thread_pool        | 1.01 ms                                                      | 966 us: 1.05x faster                                        |
| scimark_sor              | 111 ms                                                       | 106 ms: 1.04x faster                                        |
| pycparser                | 1.32 sec                                                     | 1.28 sec: 1.04x faster                                      |
| dulwich_log              | 68.4 ms                                                      | 66.3 ms: 1.03x faster                                       |
| sqlglot_optimize         | 59.8 ms                                                      | 57.9 ms: 1.03x faster                                       |
| deepcopy_memo            | 38.8 us                                                      | 37.7 us: 1.03x faster                                       |
| deepcopy_reduce          | 3.51 us                                                      | 3.42 us: 1.03x faster                                       |
| crypto_pyaes             | 83.4 ms                                                      | 81.6 ms: 1.02x faster                                       |
| meteor_contest           | 131 ms                                                       | 128 ms: 1.02x faster                                        |
| xml_etree_iterparse      | 104 ms                                                       | 104 ms: 1.01x faster                                        |
| pprint_pformat           | 1.63 sec                                                     | 1.62 sec: 1.01x faster                                      |
| tomli_loads              | 2.26 sec                                                     | 2.25 sec: 1.01x faster                                      |
| docutils                 | 2.86 sec                                                     | 2.89 sec: 1.01x slower                                      |
| pprint_safe_repr         | 784 ms                                                       | 796 ms: 1.02x slower                                        |
| unpack_sequence          | 45.6 ns                                                      | 46.8 ns: 1.03x slower                                       |
| pathlib                  | 19.1 ms                                                      | 19.6 ms: 1.03x slower                                       |
| scimark_fft              | 285 ms                                                       | 294 ms: 1.03x slower                                        |
| scimark_monte_carlo      | 68.2 ms                                                      | 70.5 ms: 1.03x slower                                       |
| regex_effbot             | 3.50 ms                                                      | 3.63 ms: 1.04x slower                                       |
| regex_v8                 | 23.9 ms                                                      | 24.8 ms: 1.04x slower                                       |
| pidigits                 | 251 ms                                                       | 261 ms: 1.04x slower                                        |
| unpickle_list            | 4.53 us                                                      | 4.71 us: 1.04x slower                                       |
| create_gc_cycles         | 1.61 ms                                                      | 1.67 ms: 1.04x slower                                       |
| python_startup           | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                       |
| pickle                   | 9.64 us                                                      | 10.1 us: 1.04x slower                                       |
| xml_etree_process        | 56.5 ms                                                      | 59.3 ms: 1.05x slower                                       |
| coverage                 | 84.8 ms                                                      | 89.0 ms: 1.05x slower                                       |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.27 ms: 1.05x slower                                       |
| telco                    | 6.86 ms                                                      | 7.25 ms: 1.06x slower                                       |
| bench_mp_pool            | 4.62 ms                                                      | 4.92 ms: 1.06x slower                                       |
| xml_etree_generate       | 80.5 ms                                                      | 85.8 ms: 1.07x slower                                       |
| python_startup_no_site   | 7.76 ms                                                      | 8.29 ms: 1.07x slower                                       |
| float                    | 74.2 ms                                                      | 79.4 ms: 1.07x slower                                       |
| unpickle                 | 13.4 us                                                      | 14.5 us: 1.08x slower                                       |
| sqlite_synth             | 2.50 us                                                      | 2.71 us: 1.08x slower                                       |
| regex_dna                | 227 ms                                                       | 247 ms: 1.09x slower                                        |
| pickle_list              | 3.83 us                                                      | 4.37 us: 1.14x slower                                       |
| async_generators         | 316 ms                                                       | 394 ms: 1.25x slower                                        |
| Geometric mean           | (ref)                                                        | 1.08x faster                                                |

Benchmark hidden because not significant (4): pyflate, gc_traversal, pickle_pure_python, pickle_dict
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
