
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 2cd1c87
- commit date: 2023-05-14
- overall geometric mean: 1.07x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230514-pythonperf2-x86_64-python-main-3.12.0a7+-2cd1c87 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 283 ms: 1.02x faster                                         |
| docutils       | 2.86 sec                                                     | 2.87 sec: 1.01x slower                                       |
| tornado_http   | 122 ms                                                       | 112 ms: 1.08x faster                                         |
| Geometric mean | (ref)                                                        | 1.03x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230514-pythonperf2-x86_64-python-main-3.12.0a7+-2cd1c87 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 86.2 ms: 1.05x faster                                        |
| pidigits       | 251 ms                                                       | 261 ms: 1.04x slower                                         |
| float          | 74.2 ms                                                      | 79.0 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230514-pythonperf2-x86_64-python-main-3.12.0a7+-2cd1c87 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 144 ms: 1.09x faster                                         |
| regex_v8       | 23.9 ms                                                      | 22.9 ms: 1.04x faster                                        |
| regex_effbot   | 3.50 ms                                                      | 3.44 ms: 1.02x faster                                        |
| regex_dna      | 227 ms                                                       | 228 ms: 1.00x slower                                         |
| Geometric mean | (ref)                                                        | 1.04x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230514-pythonperf2-x86_64-python-main-3.12.0a7+-2cd1c87 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                        |
| unpickle_pure_python | 241 us                                                       | 201 us: 1.20x faster                                         |
| json_loads           | 28.7 us                                                      | 24.0 us: 1.19x faster                                        |
| xml_etree_parse      | 158 ms                                                       | 148 ms: 1.06x faster                                         |
| tomli_loads          | 2.26 sec                                                     | 2.20 sec: 1.03x faster                                       |
| pickle_pure_python   | 319 us                                                       | 321 us: 1.01x slower                                         |
| unpickle_list        | 4.53 us                                                      | 4.61 us: 1.02x slower                                        |
| xml_etree_process    | 56.5 ms                                                      | 59.1 ms: 1.05x slower                                        |
| pickle               | 9.64 us                                                      | 10.2 us: 1.05x slower                                        |
| pickle_dict          | 30.8 us                                                      | 32.8 us: 1.07x slower                                        |
| xml_etree_generate   | 80.5 ms                                                      | 86.0 ms: 1.07x slower                                        |
| unpickle             | 13.4 us                                                      | 14.9 us: 1.11x slower                                        |
| pickle_list          | 3.83 us                                                      | 4.29 us: 1.12x slower                                        |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230514-pythonperf2-x86_64-python-main-3.12.0a7+-2cd1c87 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                        |
| python_startup_no_site | 7.76 ms                                                      | 8.40 ms: 1.08x slower                                        |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230514-pythonperf2-x86_64-python-main-3.12.0a7+-2cd1c87 |
|-----------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 9.96 ms: 1.10x faster                                        |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230514-pythonperf2-x86_64-python-main-3.12.0a7+-2cd1c87 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 157 us: 3.34x faster                                         |
| asyncio_tcp              | 753 ms                                                       | 379 ms: 1.98x faster                                         |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.57 sec: 1.96x faster                                       |
| generators               | 56.0 ms                                                      | 36.4 ms: 1.54x faster                                        |
| json_dumps               | 13.4 ms                                                      | 10.2 ms: 1.31x faster                                        |
| chaos                    | 80.9 ms                                                      | 64.3 ms: 1.26x faster                                        |
| mypy2                    | 451 ms                                                       | 362 ms: 1.25x faster                                         |
| fannkuch                 | 429 ms                                                       | 349 ms: 1.23x faster                                         |
| deltablue                | 4.00 ms                                                      | 3.26 ms: 1.23x faster                                        |
| coroutines               | 27.6 ms                                                      | 22.5 ms: 1.23x faster                                        |
| hexiom                   | 7.13 ms                                                      | 5.82 ms: 1.23x faster                                        |
| unpickle_pure_python     | 241 us                                                       | 201 us: 1.20x faster                                         |
| json_loads               | 28.7 us                                                      | 24.0 us: 1.19x faster                                        |
| richards_super           | 61.0 ms                                                      | 51.6 ms: 1.18x faster                                        |
| scimark_lu               | 115 ms                                                       | 99.7 ms: 1.15x faster                                        |
| nqueens                  | 103 ms                                                       | 90.0 ms: 1.14x faster                                        |
| async_tree_memoization   | 630 ms                                                       | 552 ms: 1.14x faster                                         |
| async_tree_none          | 519 ms                                                       | 458 ms: 1.13x faster                                         |
| comprehensions           | 24.6 us                                                      | 21.9 us: 1.12x faster                                        |
| go                       | 164 ms                                                       | 147 ms: 1.12x faster                                         |
| async_tree_io            | 1.17 sec                                                     | 1.05 sec: 1.12x faster                                       |
| json                     | 5.65 ms                                                      | 5.09 ms: 1.11x faster                                        |
| sqlglot_parse            | 1.53 ms                                                      | 1.38 ms: 1.11x faster                                        |
| mako                     | 11.0 ms                                                      | 9.96 ms: 1.10x faster                                        |
| logging_silent           | 101 ns                                                       | 91.9 ns: 1.10x faster                                        |
| regex_compile            | 158 ms                                                       | 144 ms: 1.09x faster                                         |
| sqlglot_normalize        | 126 ms                                                       | 115 ms: 1.09x faster                                         |
| mdp                      | 2.75 sec                                                     | 2.52 sec: 1.09x faster                                       |
| logging_format           | 8.11 us                                                      | 7.46 us: 1.09x faster                                        |
| tornado_http             | 122 ms                                                       | 112 ms: 1.08x faster                                         |
| sqlglot_transpile        | 1.92 ms                                                      | 1.78 ms: 1.08x faster                                        |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 698 ms: 1.07x faster                                         |
| deepcopy_memo            | 38.8 us                                                      | 36.3 us: 1.07x faster                                        |
| logging_simple           | 7.19 us                                                      | 6.75 us: 1.07x faster                                        |
| deepcopy                 | 399 us                                                       | 375 us: 1.06x faster                                         |
| xml_etree_parse          | 158 ms                                                       | 148 ms: 1.06x faster                                         |
| richards                 | 48.3 ms                                                      | 45.4 ms: 1.06x faster                                        |
| pycparser                | 1.32 sec                                                     | 1.25 sec: 1.06x faster                                       |
| bench_thread_pool        | 1.01 ms                                                      | 960 us: 1.05x faster                                         |
| nbody                    | 90.7 ms                                                      | 86.2 ms: 1.05x faster                                        |
| dulwich_log              | 68.4 ms                                                      | 65.1 ms: 1.05x faster                                        |
| regex_v8                 | 23.9 ms                                                      | 22.9 ms: 1.04x faster                                        |
| crypto_pyaes             | 83.4 ms                                                      | 80.1 ms: 1.04x faster                                        |
| deepcopy_reduce          | 3.51 us                                                      | 3.38 us: 1.04x faster                                        |
| sqlglot_optimize         | 59.8 ms                                                      | 57.7 ms: 1.04x faster                                        |
| raytrace                 | 317 ms                                                       | 307 ms: 1.03x faster                                         |
| meteor_contest           | 131 ms                                                       | 127 ms: 1.03x faster                                         |
| tomli_loads              | 2.26 sec                                                     | 2.20 sec: 1.03x faster                                       |
| spectral_norm            | 93.3 ms                                                      | 90.9 ms: 1.03x faster                                        |
| regex_effbot             | 3.50 ms                                                      | 3.44 ms: 1.02x faster                                        |
| 2to3                     | 288 ms                                                       | 283 ms: 1.02x faster                                         |
| pyflate                  | 449 ms                                                       | 443 ms: 1.01x faster                                         |
| scimark_sor              | 111 ms                                                       | 110 ms: 1.01x faster                                         |
| regex_dna                | 227 ms                                                       | 228 ms: 1.00x slower                                         |
| docutils                 | 2.86 sec                                                     | 2.87 sec: 1.01x slower                                       |
| pickle_pure_python       | 319 us                                                       | 321 us: 1.01x slower                                         |
| scimark_monte_carlo      | 68.2 ms                                                      | 69.0 ms: 1.01x slower                                        |
| unpickle_list            | 4.53 us                                                      | 4.61 us: 1.02x slower                                        |
| pprint_safe_repr         | 784 ms                                                       | 798 ms: 1.02x slower                                         |
| pathlib                  | 19.1 ms                                                      | 19.5 ms: 1.02x slower                                        |
| telco                    | 6.86 ms                                                      | 7.08 ms: 1.03x slower                                        |
| create_gc_cycles         | 1.61 ms                                                      | 1.66 ms: 1.03x slower                                        |
| pidigits                 | 251 ms                                                       | 261 ms: 1.04x slower                                         |
| xml_etree_process        | 56.5 ms                                                      | 59.1 ms: 1.05x slower                                        |
| python_startup           | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                        |
| gc_traversal             | 3.85 ms                                                      | 4.05 ms: 1.05x slower                                        |
| pickle                   | 9.64 us                                                      | 10.2 us: 1.05x slower                                        |
| sqlite_synth             | 2.50 us                                                      | 2.65 us: 1.06x slower                                        |
| float                    | 74.2 ms                                                      | 79.0 ms: 1.06x slower                                        |
| pickle_dict              | 30.8 us                                                      | 32.8 us: 1.07x slower                                        |
| xml_etree_generate       | 80.5 ms                                                      | 86.0 ms: 1.07x slower                                        |
| python_startup_no_site   | 7.76 ms                                                      | 8.40 ms: 1.08x slower                                        |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 4.41 ms: 1.09x slower                                        |
| scimark_fft              | 285 ms                                                       | 312 ms: 1.10x slower                                         |
| coverage                 | 84.8 ms                                                      | 93.3 ms: 1.10x slower                                        |
| unpickle                 | 13.4 us                                                      | 14.9 us: 1.11x slower                                        |
| pickle_list              | 3.83 us                                                      | 4.29 us: 1.12x slower                                        |
| unpack_sequence          | 45.6 ns                                                      | 51.2 ns: 1.12x slower                                        |
| async_generators         | 316 ms                                                       | 386 ms: 1.22x slower                                         |
| bench_mp_pool            | 4.62 ms                                                      | 5.80 ms: 1.25x slower                                        |
| dask                     | 410 ms                                                       | 555 ms: 1.35x slower                                         |
| Geometric mean           | (ref)                                                        | 1.07x faster                                                 |

Benchmark hidden because not significant (2): pprint_pformat, xml_etree_iterparse
Ignored benchmarks (16) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
