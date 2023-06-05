
# Results vs. 3.11.0

- fork: faster-cpython
- ref: remove_remaining_sup
- machine: linux-x86_64
- commit hash: 6cde1a4
- commit date: 2023-06-02
- overall geometric mean: 1.06x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-pythonperf2-x86_64-faster%2dcpython-remove_remaining_sup-3.13.0a0-6cde1a4 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 2.89 sec: 1.01x slower                                                                |
| tornado_http   | 122 ms                                                       | 117 ms: 1.04x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-pythonperf2-x86_64-faster%2dcpython-remove_remaining_sup-3.13.0a0-6cde1a4 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 87.9 ms: 1.03x faster                                                                 |
| pidigits       | 251 ms                                                       | 261 ms: 1.04x slower                                                                  |
| float          | 74.2 ms                                                      | 78.4 ms: 1.06x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-pythonperf2-x86_64-faster%2dcpython-remove_remaining_sup-3.13.0a0-6cde1a4 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 147 ms: 1.07x faster                                                                  |
| regex_v8       | 23.9 ms                                                      | 24.4 ms: 1.02x slower                                                                 |
| regex_effbot   | 3.50 ms                                                      | 3.62 ms: 1.03x slower                                                                 |
| regex_dna      | 227 ms                                                       | 245 ms: 1.08x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-pythonperf2-x86_64-faster%2dcpython-remove_remaining_sup-3.13.0a0-6cde1a4 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.1 ms: 1.32x faster                                                                 |
| json_loads           | 28.7 us                                                      | 24.5 us: 1.17x faster                                                                 |
| unpickle_pure_python | 241 us                                                       | 212 us: 1.14x faster                                                                  |
| xml_etree_parse      | 158 ms                                                       | 148 ms: 1.06x faster                                                                  |
| tomli_loads          | 2.26 sec                                                     | 2.22 sec: 1.02x faster                                                                |
| pickle_pure_python   | 319 us                                                       | 322 us: 1.01x slower                                                                  |
| xml_etree_iterparse  | 104 ms                                                       | 106 ms: 1.02x slower                                                                  |
| unpickle_list        | 4.53 us                                                      | 4.64 us: 1.02x slower                                                                 |
| pickle_dict          | 30.8 us                                                      | 31.8 us: 1.03x slower                                                                 |
| pickle               | 9.64 us                                                      | 10.0 us: 1.04x slower                                                                 |
| xml_etree_process    | 56.5 ms                                                      | 59.9 ms: 1.06x slower                                                                 |
| unpickle             | 13.4 us                                                      | 14.6 us: 1.08x slower                                                                 |
| xml_etree_generate   | 80.5 ms                                                      | 87.4 ms: 1.09x slower                                                                 |
| pickle_list          | 3.83 us                                                      | 4.27 us: 1.12x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-pythonperf2-x86_64-faster%2dcpython-remove_remaining_sup-3.13.0a0-6cde1a4 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.2 ms: 1.05x slower                                                                 |
| python_startup_no_site | 7.76 ms                                                      | 8.33 ms: 1.07x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-pythonperf2-x86_64-faster%2dcpython-remove_remaining_sup-3.13.0a0-6cde1a4 |
|-----------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.2 ms: 1.08x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230602-pythonperf2-x86_64-faster%2dcpython-remove_remaining_sup-3.13.0a0-6cde1a4 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 150 us: 3.49x faster                                                                  |
| asyncio_tcp              | 753 ms                                                       | 382 ms: 1.97x faster                                                                  |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.57 sec: 1.96x faster                                                                |
| generators               | 56.0 ms                                                      | 35.8 ms: 1.57x faster                                                                 |
| json_dumps               | 13.4 ms                                                      | 10.1 ms: 1.32x faster                                                                 |
| chaos                    | 80.9 ms                                                      | 63.6 ms: 1.27x faster                                                                 |
| coroutines               | 27.6 ms                                                      | 22.1 ms: 1.24x faster                                                                 |
| mypy2                    | 451 ms                                                       | 365 ms: 1.24x faster                                                                  |
| deltablue                | 4.00 ms                                                      | 3.24 ms: 1.23x faster                                                                 |
| scimark_lu               | 115 ms                                                       | 94.8 ms: 1.21x faster                                                                 |
| hexiom                   | 7.13 ms                                                      | 5.95 ms: 1.20x faster                                                                 |
| fannkuch                 | 429 ms                                                       | 358 ms: 1.20x faster                                                                  |
| json_loads               | 28.7 us                                                      | 24.5 us: 1.17x faster                                                                 |
| richards_super           | 61.0 ms                                                      | 53.3 ms: 1.14x faster                                                                 |
| unpickle_pure_python     | 241 us                                                       | 212 us: 1.14x faster                                                                  |
| async_tree_memoization   | 630 ms                                                       | 558 ms: 1.13x faster                                                                  |
| nqueens                  | 103 ms                                                       | 91.4 ms: 1.13x faster                                                                 |
| comprehensions           | 24.6 us                                                      | 21.9 us: 1.12x faster                                                                 |
| async_tree_none          | 519 ms                                                       | 466 ms: 1.12x faster                                                                  |
| json                     | 5.65 ms                                                      | 5.13 ms: 1.10x faster                                                                 |
| logging_format           | 8.11 us                                                      | 7.37 us: 1.10x faster                                                                 |
| async_tree_io            | 1.17 sec                                                     | 1.07 sec: 1.10x faster                                                                |
| sqlglot_parse            | 1.53 ms                                                      | 1.41 ms: 1.09x faster                                                                 |
| mdp                      | 2.75 sec                                                     | 2.52 sec: 1.09x faster                                                                |
| sqlglot_normalize        | 126 ms                                                       | 116 ms: 1.09x faster                                                                  |
| gc_traversal             | 3.85 ms                                                      | 3.56 ms: 1.08x faster                                                                 |
| mako                     | 11.0 ms                                                      | 10.2 ms: 1.08x faster                                                                 |
| go                       | 164 ms                                                       | 153 ms: 1.07x faster                                                                  |
| regex_compile            | 158 ms                                                       | 147 ms: 1.07x faster                                                                  |
| sqlglot_transpile        | 1.92 ms                                                      | 1.80 ms: 1.07x faster                                                                 |
| xml_etree_parse          | 158 ms                                                       | 148 ms: 1.06x faster                                                                  |
| spectral_norm            | 93.3 ms                                                      | 88.0 ms: 1.06x faster                                                                 |
| deepcopy                 | 399 us                                                       | 377 us: 1.06x faster                                                                  |
| logging_simple           | 7.19 us                                                      | 6.83 us: 1.05x faster                                                                 |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 711 ms: 1.05x faster                                                                  |
| bench_thread_pool        | 1.01 ms                                                      | 961 us: 1.05x faster                                                                  |
| dulwich_log              | 68.4 ms                                                      | 65.6 ms: 1.04x faster                                                                 |
| logging_silent           | 101 ns                                                       | 96.7 ns: 1.04x faster                                                                 |
| tornado_http             | 122 ms                                                       | 117 ms: 1.04x faster                                                                  |
| sqlglot_optimize         | 59.8 ms                                                      | 57.9 ms: 1.03x faster                                                                 |
| pycparser                | 1.32 sec                                                     | 1.28 sec: 1.03x faster                                                                |
| nbody                    | 90.7 ms                                                      | 87.9 ms: 1.03x faster                                                                 |
| raytrace                 | 317 ms                                                       | 308 ms: 1.03x faster                                                                  |
| crypto_pyaes             | 83.4 ms                                                      | 81.1 ms: 1.03x faster                                                                 |
| deepcopy_reduce          | 3.51 us                                                      | 3.43 us: 1.02x faster                                                                 |
| tomli_loads              | 2.26 sec                                                     | 2.22 sec: 1.02x faster                                                                |
| richards                 | 48.3 ms                                                      | 47.4 ms: 1.02x faster                                                                 |
| scimark_sor              | 111 ms                                                       | 109 ms: 1.02x faster                                                                  |
| meteor_contest           | 131 ms                                                       | 129 ms: 1.01x faster                                                                  |
| deepcopy_memo            | 38.8 us                                                      | 38.4 us: 1.01x faster                                                                 |
| scimark_monte_carlo      | 68.2 ms                                                      | 68.8 ms: 1.01x slower                                                                 |
| pickle_pure_python       | 319 us                                                       | 322 us: 1.01x slower                                                                  |
| docutils                 | 2.86 sec                                                     | 2.89 sec: 1.01x slower                                                                |
| xml_etree_iterparse      | 104 ms                                                       | 106 ms: 1.02x slower                                                                  |
| regex_v8                 | 23.9 ms                                                      | 24.4 ms: 1.02x slower                                                                 |
| unpickle_list            | 4.53 us                                                      | 4.64 us: 1.02x slower                                                                 |
| pprint_pformat           | 1.63 sec                                                     | 1.68 sec: 1.03x slower                                                                |
| pickle_dict              | 30.8 us                                                      | 31.8 us: 1.03x slower                                                                 |
| pathlib                  | 19.1 ms                                                      | 19.7 ms: 1.03x slower                                                                 |
| regex_effbot             | 3.50 ms                                                      | 3.62 ms: 1.03x slower                                                                 |
| pidigits                 | 251 ms                                                       | 261 ms: 1.04x slower                                                                  |
| pickle                   | 9.64 us                                                      | 10.0 us: 1.04x slower                                                                 |
| python_startup           | 10.8 ms                                                      | 11.2 ms: 1.05x slower                                                                 |
| coverage                 | 84.8 ms                                                      | 89.1 ms: 1.05x slower                                                                 |
| pprint_safe_repr         | 784 ms                                                       | 827 ms: 1.06x slower                                                                  |
| telco                    | 6.86 ms                                                      | 7.24 ms: 1.06x slower                                                                 |
| float                    | 74.2 ms                                                      | 78.4 ms: 1.06x slower                                                                 |
| unpack_sequence          | 45.6 ns                                                      | 48.3 ns: 1.06x slower                                                                 |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.29 ms: 1.06x slower                                                                 |
| scimark_fft              | 285 ms                                                       | 302 ms: 1.06x slower                                                                  |
| xml_etree_process        | 56.5 ms                                                      | 59.9 ms: 1.06x slower                                                                 |
| python_startup_no_site   | 7.76 ms                                                      | 8.33 ms: 1.07x slower                                                                 |
| sqlite_synth             | 2.50 us                                                      | 2.70 us: 1.08x slower                                                                 |
| regex_dna                | 227 ms                                                       | 245 ms: 1.08x slower                                                                  |
| unpickle                 | 13.4 us                                                      | 14.6 us: 1.08x slower                                                                 |
| xml_etree_generate       | 80.5 ms                                                      | 87.4 ms: 1.09x slower                                                                 |
| pickle_list              | 3.83 us                                                      | 4.27 us: 1.12x slower                                                                 |
| async_generators         | 316 ms                                                       | 394 ms: 1.25x slower                                                                  |
| bench_mp_pool            | 4.62 ms                                                      | 9.37 ms: 2.03x slower                                                                 |
| Geometric mean           | (ref)                                                        | 1.06x faster                                                                          |

Benchmark hidden because not significant (2): pyflate, create_gc_cycles
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
