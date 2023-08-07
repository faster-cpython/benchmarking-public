
# Results vs. 3.11.0

- fork: brandtbucher
- ref: uops_enabled
- machine: linux-x86_64
- commit hash: 9016d52
- commit date: 2023-08-06
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 3.05 sec: 1.07x slower                                                    |
| tornado_http   | 122 ms                                                       | 125 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                        | 1.05x slower                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 260 ms: 1.03x slower                                                      |
| nbody          | 90.7 ms                                                      | 98.3 ms: 1.08x slower                                                     |
| float          | 74.2 ms                                                      | 86.9 ms: 1.17x slower                                                     |
| Geometric mean | (ref)                                                        | 1.10x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 23.9 ms                                                      | 24.9 ms: 1.04x slower                                                     |
| regex_effbot   | 3.50 ms                                                      | 3.69 ms: 1.05x slower                                                     |
| regex_compile  | 158 ms                                                       | 171 ms: 1.08x slower                                                      |
| regex_dna      | 227 ms                                                       | 249 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                        | 1.07x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.4 ms: 1.28x faster                                                     |
| json_loads           | 28.7 us                                                      | 25.9 us: 1.11x faster                                                     |
| unpickle_pure_python | 241 us                                                       | 237 us: 1.02x faster                                                      |
| xml_etree_parse      | 158 ms                                                       | 155 ms: 1.02x faster                                                      |
| pickle_pure_python   | 319 us                                                       | 329 us: 1.03x slower                                                      |
| unpickle_list        | 4.53 us                                                      | 4.68 us: 1.03x slower                                                     |
| pickle               | 9.64 us                                                      | 10.2 us: 1.06x slower                                                     |
| xml_etree_iterparse  | 104 ms                                                       | 112 ms: 1.08x slower                                                      |
| xml_etree_process    | 56.5 ms                                                      | 60.8 ms: 1.08x slower                                                     |
| pickle_dict          | 30.8 us                                                      | 33.8 us: 1.10x slower                                                     |
| unpickle             | 13.4 us                                                      | 14.8 us: 1.10x slower                                                     |
| xml_etree_generate   | 80.5 ms                                                      | 90.0 ms: 1.12x slower                                                     |
| pickle_list          | 3.83 us                                                      | 4.54 us: 1.19x slower                                                     |
| tomli_loads          | 2.26 sec                                                     | 2.84 sec: 1.26x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.7 ms: 1.09x slower                                                     |
| python_startup_no_site | 7.76 ms                                                      | 8.70 ms: 1.12x slower                                                     |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|-----------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 12.3 ms: 1.12x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf2-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 159 us: 3.28x faster                                                      |
| asyncio_tcp              | 753 ms                                                       | 374 ms: 2.01x faster                                                      |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.58 sec: 1.95x faster                                                    |
| generators               | 56.0 ms                                                      | 38.0 ms: 1.47x faster                                                     |
| json_dumps               | 13.4 ms                                                      | 10.4 ms: 1.28x faster                                                     |
| chaos                    | 80.9 ms                                                      | 68.0 ms: 1.19x faster                                                     |
| mypy2                    | 451 ms                                                       | 386 ms: 1.17x faster                                                      |
| coroutines               | 27.6 ms                                                      | 23.9 ms: 1.15x faster                                                     |
| json_loads               | 28.7 us                                                      | 25.9 us: 1.11x faster                                                     |
| async_tree_memoization   | 630 ms                                                       | 578 ms: 1.09x faster                                                      |
| async_tree_none          | 519 ms                                                       | 478 ms: 1.09x faster                                                      |
| logging_format           | 8.11 us                                                      | 7.53 us: 1.08x faster                                                     |
| crypto_pyaes             | 83.4 ms                                                      | 77.6 ms: 1.08x faster                                                     |
| raytrace                 | 317 ms                                                       | 295 ms: 1.07x faster                                                      |
| json                     | 5.65 ms                                                      | 5.29 ms: 1.07x faster                                                     |
| async_tree_io            | 1.17 sec                                                     | 1.10 sec: 1.07x faster                                                    |
| scimark_lu               | 115 ms                                                       | 107 ms: 1.07x faster                                                      |
| logging_simple           | 7.19 us                                                      | 6.91 us: 1.04x faster                                                     |
| sqlglot_normalize        | 126 ms                                                       | 122 ms: 1.03x faster                                                      |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 727 ms: 1.03x faster                                                      |
| sqlglot_parse            | 1.53 ms                                                      | 1.49 ms: 1.03x faster                                                     |
| unpickle_pure_python     | 241 us                                                       | 237 us: 1.02x faster                                                      |
| xml_etree_parse          | 158 ms                                                       | 155 ms: 1.02x faster                                                      |
| mdp                      | 2.75 sec                                                     | 2.71 sec: 1.01x faster                                                    |
| deltablue                | 4.00 ms                                                      | 3.96 ms: 1.01x faster                                                     |
| deepcopy                 | 399 us                                                       | 395 us: 1.01x faster                                                      |
| richards_super           | 61.0 ms                                                      | 62.1 ms: 1.02x slower                                                     |
| gc_traversal             | 3.85 ms                                                      | 3.92 ms: 1.02x slower                                                     |
| tornado_http             | 122 ms                                                       | 125 ms: 1.03x slower                                                      |
| pathlib                  | 19.1 ms                                                      | 19.6 ms: 1.03x slower                                                     |
| dulwich_log              | 68.4 ms                                                      | 70.5 ms: 1.03x slower                                                     |
| pickle_pure_python       | 319 us                                                       | 329 us: 1.03x slower                                                      |
| unpickle_list            | 4.53 us                                                      | 4.68 us: 1.03x slower                                                     |
| pidigits                 | 251 ms                                                       | 260 ms: 1.03x slower                                                      |
| create_gc_cycles         | 1.61 ms                                                      | 1.67 ms: 1.04x slower                                                     |
| scimark_monte_carlo      | 68.2 ms                                                      | 71.0 ms: 1.04x slower                                                     |
| pycparser                | 1.32 sec                                                     | 1.38 sec: 1.04x slower                                                    |
| regex_v8                 | 23.9 ms                                                      | 24.9 ms: 1.04x slower                                                     |
| sqlglot_optimize         | 59.8 ms                                                      | 62.5 ms: 1.05x slower                                                     |
| pprint_pformat           | 1.63 sec                                                     | 1.71 sec: 1.05x slower                                                    |
| regex_effbot             | 3.50 ms                                                      | 3.69 ms: 1.05x slower                                                     |
| pickle                   | 9.64 us                                                      | 10.2 us: 1.06x slower                                                     |
| docutils                 | 2.86 sec                                                     | 3.05 sec: 1.07x slower                                                    |
| pprint_safe_repr         | 784 ms                                                       | 839 ms: 1.07x slower                                                      |
| coverage                 | 84.8 ms                                                      | 90.8 ms: 1.07x slower                                                     |
| xml_etree_iterparse      | 104 ms                                                       | 112 ms: 1.08x slower                                                      |
| xml_etree_process        | 56.5 ms                                                      | 60.8 ms: 1.08x slower                                                     |
| spectral_norm            | 93.3 ms                                                      | 101 ms: 1.08x slower                                                      |
| nbody                    | 90.7 ms                                                      | 98.3 ms: 1.08x slower                                                     |
| regex_compile            | 158 ms                                                       | 171 ms: 1.08x slower                                                      |
| python_startup           | 10.8 ms                                                      | 11.7 ms: 1.09x slower                                                     |
| regex_dna                | 227 ms                                                       | 249 ms: 1.10x slower                                                      |
| pickle_dict              | 30.8 us                                                      | 33.8 us: 1.10x slower                                                     |
| unpickle                 | 13.4 us                                                      | 14.8 us: 1.10x slower                                                     |
| meteor_contest           | 131 ms                                                       | 144 ms: 1.10x slower                                                      |
| nqueens                  | 103 ms                                                       | 114 ms: 1.11x slower                                                      |
| sqlite_synth             | 2.50 us                                                      | 2.78 us: 1.11x slower                                                     |
| mako                     | 11.0 ms                                                      | 12.3 ms: 1.12x slower                                                     |
| xml_etree_generate       | 80.5 ms                                                      | 90.0 ms: 1.12x slower                                                     |
| python_startup_no_site   | 7.76 ms                                                      | 8.70 ms: 1.12x slower                                                     |
| fannkuch                 | 429 ms                                                       | 482 ms: 1.12x slower                                                      |
| comprehensions           | 24.6 us                                                      | 27.9 us: 1.13x slower                                                     |
| deepcopy_memo            | 38.8 us                                                      | 44.3 us: 1.14x slower                                                     |
| go                       | 164 ms                                                       | 188 ms: 1.15x slower                                                      |
| richards                 | 48.3 ms                                                      | 55.7 ms: 1.15x slower                                                     |
| float                    | 74.2 ms                                                      | 86.9 ms: 1.17x slower                                                     |
| pickle_list              | 3.83 us                                                      | 4.54 us: 1.19x slower                                                     |
| hexiom                   | 7.13 ms                                                      | 8.48 ms: 1.19x slower                                                     |
| telco                    | 6.86 ms                                                      | 8.30 ms: 1.21x slower                                                     |
| unpack_sequence          | 45.6 ns                                                      | 55.7 ns: 1.22x slower                                                     |
| scimark_fft              | 285 ms                                                       | 349 ms: 1.22x slower                                                      |
| pyflate                  | 449 ms                                                       | 559 ms: 1.25x slower                                                      |
| tomli_loads              | 2.26 sec                                                     | 2.84 sec: 1.26x slower                                                    |
| async_generators         | 316 ms                                                       | 410 ms: 1.30x slower                                                      |
| scimark_sor              | 111 ms                                                       | 151 ms: 1.36x slower                                                      |
| dask                     | 410 ms                                                       | 603 ms: 1.47x slower                                                      |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 6.61 ms: 1.63x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.02x slower                                                              |

Benchmark hidden because not significant (5): bench_mp_pool, bench_thread_pool, sqlglot_transpile, logging_silent, deepcopy_reduce
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
