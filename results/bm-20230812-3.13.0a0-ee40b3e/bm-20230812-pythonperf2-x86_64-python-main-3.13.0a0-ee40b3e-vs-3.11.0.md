
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: ee40b3e
- commit date: 2023-08-12
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-pythonperf2-x86_64-python-main-3.13.0a0-ee40b3e |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 2.89 sec: 1.01x slower                                      |
| Geometric mean | (ref)                                                        | 1.01x slower                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-pythonperf2-x86_64-python-main-3.13.0a0-ee40b3e |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 260 ms: 1.03x slower                                        |
| float          | 74.2 ms                                                      | 81.3 ms: 1.10x slower                                       |
| Geometric mean | (ref)                                                        | 1.04x slower                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-pythonperf2-x86_64-python-main-3.13.0a0-ee40b3e |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_effbot   | 3.50 ms                                                      | 3.33 ms: 1.05x faster                                       |
| regex_compile  | 158 ms                                                       | 151 ms: 1.04x faster                                        |
| regex_v8       | 23.9 ms                                                      | 23.5 ms: 1.02x faster                                       |
| regex_dna      | 227 ms                                                       | 238 ms: 1.05x slower                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-pythonperf2-x86_64-python-main-3.13.0a0-ee40b3e |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.5 ms: 1.28x faster                                       |
| json_loads           | 28.7 us                                                      | 25.8 us: 1.11x faster                                       |
| unpickle_pure_python | 241 us                                                       | 225 us: 1.07x faster                                        |
| xml_etree_parse      | 158 ms                                                       | 150 ms: 1.05x faster                                        |
| tomli_loads          | 2.26 sec                                                     | 2.28 sec: 1.01x slower                                      |
| pickle_pure_python   | 319 us                                                       | 324 us: 1.02x slower                                        |
| xml_etree_iterparse  | 104 ms                                                       | 106 ms: 1.02x slower                                        |
| pickle_dict          | 30.8 us                                                      | 31.6 us: 1.03x slower                                       |
| xml_etree_process    | 56.5 ms                                                      | 58.8 ms: 1.04x slower                                       |
| unpickle_list        | 4.53 us                                                      | 4.74 us: 1.04x slower                                       |
| xml_etree_generate   | 80.5 ms                                                      | 85.2 ms: 1.06x slower                                       |
| pickle               | 9.64 us                                                      | 10.2 us: 1.06x slower                                       |
| unpickle             | 13.4 us                                                      | 14.8 us: 1.10x slower                                       |
| pickle_list          | 3.83 us                                                      | 4.35 us: 1.14x slower                                       |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-pythonperf2-x86_64-python-main-3.13.0a0-ee40b3e |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.6 ms: 1.08x slower                                       |
| python_startup_no_site | 7.76 ms                                                      | 8.65 ms: 1.12x slower                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-pythonperf2-x86_64-python-main-3.13.0a0-ee40b3e |
|-----------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 10.3 ms: 1.06x faster                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-pythonperf2-x86_64-python-main-3.13.0a0-ee40b3e |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 153 us: 3.41x faster                                        |
| asyncio_tcp              | 753 ms                                                       | 369 ms: 2.04x faster                                        |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.59 sec: 1.94x faster                                      |
| generators               | 56.0 ms                                                      | 36.5 ms: 1.54x faster                                       |
| json_dumps               | 13.4 ms                                                      | 10.5 ms: 1.28x faster                                       |
| chaos                    | 80.9 ms                                                      | 63.6 ms: 1.27x faster                                       |
| coroutines               | 27.6 ms                                                      | 23.2 ms: 1.19x faster                                       |
| async_tree_none          | 519 ms                                                       | 441 ms: 1.18x faster                                        |
| scimark_lu               | 115 ms                                                       | 100 ms: 1.14x faster                                        |
| async_tree_memoization   | 630 ms                                                       | 552 ms: 1.14x faster                                        |
| raytrace                 | 317 ms                                                       | 278 ms: 1.14x faster                                        |
| nqueens                  | 103 ms                                                       | 90.5 ms: 1.14x faster                                       |
| json_loads               | 28.7 us                                                      | 25.8 us: 1.11x faster                                       |
| fannkuch                 | 429 ms                                                       | 386 ms: 1.11x faster                                        |
| crypto_pyaes             | 83.4 ms                                                      | 75.7 ms: 1.10x faster                                       |
| async_tree_io            | 1.17 sec                                                     | 1.08 sec: 1.09x faster                                      |
| mdp                      | 2.75 sec                                                     | 2.54 sec: 1.08x faster                                      |
| comprehensions           | 24.6 us                                                      | 22.9 us: 1.08x faster                                       |
| json                     | 5.65 ms                                                      | 5.27 ms: 1.07x faster                                       |
| hexiom                   | 7.13 ms                                                      | 6.65 ms: 1.07x faster                                       |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 700 ms: 1.07x faster                                        |
| sqlglot_normalize        | 126 ms                                                       | 118 ms: 1.07x faster                                        |
| unpickle_pure_python     | 241 us                                                       | 225 us: 1.07x faster                                        |
| logging_format           | 8.11 us                                                      | 7.60 us: 1.07x faster                                       |
| sqlglot_parse            | 1.53 ms                                                      | 1.44 ms: 1.06x faster                                       |
| mako                     | 11.0 ms                                                      | 10.3 ms: 1.06x faster                                       |
| xml_etree_parse          | 158 ms                                                       | 150 ms: 1.05x faster                                        |
| regex_effbot             | 3.50 ms                                                      | 3.33 ms: 1.05x faster                                       |
| regex_compile            | 158 ms                                                       | 151 ms: 1.04x faster                                        |
| deltablue                | 4.00 ms                                                      | 3.84 ms: 1.04x faster                                       |
| bench_thread_pool        | 1.01 ms                                                      | 974 us: 1.04x faster                                        |
| sqlglot_transpile        | 1.92 ms                                                      | 1.85 ms: 1.04x faster                                       |
| gc_traversal             | 3.85 ms                                                      | 3.72 ms: 1.03x faster                                       |
| coverage                 | 84.8 ms                                                      | 82.5 ms: 1.03x faster                                       |
| regex_v8                 | 23.9 ms                                                      | 23.5 ms: 1.02x faster                                       |
| logging_simple           | 7.19 us                                                      | 7.07 us: 1.02x faster                                       |
| meteor_contest           | 131 ms                                                       | 129 ms: 1.01x faster                                        |
| deepcopy_memo            | 38.8 us                                                      | 38.6 us: 1.00x faster                                       |
| tomli_loads              | 2.26 sec                                                     | 2.28 sec: 1.01x slower                                      |
| dulwich_log              | 68.4 ms                                                      | 69.3 ms: 1.01x slower                                       |
| docutils                 | 2.86 sec                                                     | 2.89 sec: 1.01x slower                                      |
| create_gc_cycles         | 1.61 ms                                                      | 1.63 ms: 1.02x slower                                       |
| pickle_pure_python       | 319 us                                                       | 324 us: 1.02x slower                                        |
| xml_etree_iterparse      | 104 ms                                                       | 106 ms: 1.02x slower                                        |
| spectral_norm            | 93.3 ms                                                      | 95.1 ms: 1.02x slower                                       |
| deepcopy                 | 399 us                                                       | 407 us: 1.02x slower                                        |
| richards_super           | 61.0 ms                                                      | 62.6 ms: 1.02x slower                                       |
| pathlib                  | 19.1 ms                                                      | 19.5 ms: 1.02x slower                                       |
| pickle_dict              | 30.8 us                                                      | 31.6 us: 1.03x slower                                       |
| pprint_pformat           | 1.63 sec                                                     | 1.68 sec: 1.03x slower                                      |
| scimark_monte_carlo      | 68.2 ms                                                      | 70.4 ms: 1.03x slower                                       |
| deepcopy_reduce          | 3.51 us                                                      | 3.62 us: 1.03x slower                                       |
| pidigits                 | 251 ms                                                       | 260 ms: 1.03x slower                                        |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.20 ms: 1.04x slower                                       |
| xml_etree_process        | 56.5 ms                                                      | 58.8 ms: 1.04x slower                                       |
| unpickle_list            | 4.53 us                                                      | 4.74 us: 1.04x slower                                       |
| regex_dna                | 227 ms                                                       | 238 ms: 1.05x slower                                        |
| pprint_safe_repr         | 784 ms                                                       | 825 ms: 1.05x slower                                        |
| scimark_fft              | 285 ms                                                       | 301 ms: 1.06x slower                                        |
| xml_etree_generate       | 80.5 ms                                                      | 85.2 ms: 1.06x slower                                       |
| pickle                   | 9.64 us                                                      | 10.2 us: 1.06x slower                                       |
| sqlite_synth             | 2.50 us                                                      | 2.68 us: 1.07x slower                                       |
| python_startup           | 10.8 ms                                                      | 11.6 ms: 1.08x slower                                       |
| float                    | 74.2 ms                                                      | 81.3 ms: 1.10x slower                                       |
| go                       | 164 ms                                                       | 180 ms: 1.10x slower                                        |
| unpickle                 | 13.4 us                                                      | 14.8 us: 1.10x slower                                       |
| python_startup_no_site   | 7.76 ms                                                      | 8.65 ms: 1.12x slower                                       |
| pickle_list              | 3.83 us                                                      | 4.35 us: 1.14x slower                                       |
| pyflate                  | 449 ms                                                       | 512 ms: 1.14x slower                                        |
| richards                 | 48.3 ms                                                      | 56.3 ms: 1.17x slower                                       |
| telco                    | 6.86 ms                                                      | 8.09 ms: 1.18x slower                                       |
| unpack_sequence          | 45.6 ns                                                      | 56.8 ns: 1.25x slower                                       |
| async_generators         | 316 ms                                                       | 402 ms: 1.27x slower                                        |
| scimark_sor              | 111 ms                                                       | 153 ms: 1.38x slower                                        |
| dask                     | 410 ms                                                       | 594 ms: 1.45x slower                                        |
| Geometric mean           | (ref)                                                        | 1.03x faster                                                |

Benchmark hidden because not significant (7): logging_silent, sqlglot_optimize, bench_mp_pool, tornado_http, nbody, pycparser, mypy2
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
