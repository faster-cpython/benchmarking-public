
# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin
- machine: linux-x86_64
- commit hash: 3346d48
- commit date: 2023-07-05
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.71 sec: 1.03x slower                                        |
| tornado_http   | 96.3 ms                                                | 99.1 ms: 1.03x slower                                         |
| Geometric mean | (ref)                                                  | 1.03x slower                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 198 ms: 1.00x faster                                          |
| float          | 77.2 ms                                                | 88.9 ms: 1.15x slower                                         |
| Geometric mean | (ref)                                                  | 1.05x slower                                                  |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.69 ms: 1.08x faster                                         |
| regex_compile  | 138 ms                                                 | 142 ms: 1.03x slower                                          |
| regex_dna      | 204 ms                                                 | 212 ms: 1.04x slower                                          |
| regex_v8       | 22.0 ms                                                | 23.4 ms: 1.06x slower                                         |
| Geometric mean | (ref)                                                  | 1.01x slower                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.83 ms: 1.28x faster                                         |
| json_loads           | 26.5 us                                                | 25.0 us: 1.06x faster                                         |
| unpickle_pure_python | 228 us                                                 | 219 us: 1.04x faster                                          |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                          |
| unpickle_list        | 4.91 us                                                | 4.87 us: 1.01x faster                                         |
| pickle               | 10.1 us                                                | 10.3 us: 1.03x slower                                         |
| pickle_pure_python   | 306 us                                                 | 315 us: 1.03x slower                                          |
| pickle_dict          | 31.1 us                                                | 32.5 us: 1.04x slower                                         |
| tomli_loads          | 2.22 sec                                               | 2.37 sec: 1.07x slower                                        |
| unpickle             | 13.7 us                                                | 14.8 us: 1.09x slower                                         |
| xml_etree_process    | 53.9 ms                                                | 58.9 ms: 1.09x slower                                         |
| pickle_list          | 4.11 us                                                | 4.57 us: 1.11x slower                                         |
| xml_etree_generate   | 76.2 ms                                                | 86.9 ms: 1.14x slower                                         |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                  |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.43 ms: 1.11x slower                                         |
| python_startup_no_site | 6.01 ms                                                | 6.83 ms: 1.14x slower                                         |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 12.6 ms: 1.25x slower                                         |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230705-linux-x86_64-brandtbucher-justin-3.13.0a0-3346d48 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 145 us: 3.34x faster                                          |
| generators               | 73.5 ms                                                | 29.1 ms: 2.52x faster                                         |
| asyncio_tcp              | 922 ms                                                 | 516 ms: 1.79x faster                                          |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                        |
| json_dumps               | 12.6 ms                                                | 9.83 ms: 1.28x faster                                         |
| mypy2                    | 420 ms                                                 | 343 ms: 1.22x faster                                          |
| coroutines               | 25.5 ms                                                | 22.5 ms: 1.13x faster                                         |
| richards_super           | 56.8 ms                                                | 50.8 ms: 1.12x faster                                         |
| regex_effbot             | 3.99 ms                                                | 3.69 ms: 1.08x faster                                         |
| chaos                    | 69.2 ms                                                | 64.8 ms: 1.07x faster                                         |
| coverage                 | 100 ms                                                 | 94.2 ms: 1.06x faster                                         |
| json_loads               | 26.5 us                                                | 25.0 us: 1.06x faster                                         |
| async_tree_none          | 526 ms                                                 | 500 ms: 1.05x faster                                          |
| gc_traversal             | 4.02 ms                                                | 3.84 ms: 1.05x faster                                         |
| unpickle_pure_python     | 228 us                                                 | 219 us: 1.04x faster                                          |
| async_tree_io            | 1.30 sec                                               | 1.25 sec: 1.04x faster                                        |
| pycparser                | 1.18 sec                                               | 1.14 sec: 1.04x faster                                        |
| json                     | 4.94 ms                                                | 4.79 ms: 1.03x faster                                         |
| async_tree_memoization   | 627 ms                                                 | 608 ms: 1.03x faster                                          |
| xml_etree_parse          | 158 ms                                                 | 154 ms: 1.03x faster                                          |
| logging_format           | 6.68 us                                                | 6.51 us: 1.03x faster                                         |
| sqlglot_parse            | 1.40 ms                                                | 1.37 ms: 1.03x faster                                         |
| mdp                      | 2.62 sec                                               | 2.56 sec: 1.02x faster                                        |
| richards                 | 45.7 ms                                                | 44.8 ms: 1.02x faster                                         |
| logging_simple           | 6.03 us                                                | 5.97 us: 1.01x faster                                         |
| deltablue                | 3.67 ms                                                | 3.64 ms: 1.01x faster                                         |
| sqlglot_transpile        | 1.70 ms                                                | 1.69 ms: 1.01x faster                                         |
| unpickle_list            | 4.91 us                                                | 4.87 us: 1.01x faster                                         |
| sqlglot_normalize        | 108 ms                                                 | 107 ms: 1.01x faster                                          |
| pidigits                 | 198 ms                                                 | 198 ms: 1.00x faster                                          |
| sqlglot_optimize         | 53.1 ms                                                | 53.6 ms: 1.01x slower                                         |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 746 ms: 1.01x slower                                          |
| create_gc_cycles         | 1.49 ms                                                | 1.51 ms: 1.01x slower                                         |
| bench_thread_pool        | 819 us                                                 | 832 us: 1.02x slower                                          |
| go                       | 140 ms                                                 | 143 ms: 1.02x slower                                          |
| dulwich_log              | 63.7 ms                                                | 65.2 ms: 1.02x slower                                         |
| pickle                   | 10.1 us                                                | 10.3 us: 1.03x slower                                         |
| tornado_http             | 96.3 ms                                                | 99.1 ms: 1.03x slower                                         |
| pickle_pure_python       | 306 us                                                 | 315 us: 1.03x slower                                          |
| regex_compile            | 138 ms                                                 | 142 ms: 1.03x slower                                          |
| docutils                 | 2.63 sec                                               | 2.71 sec: 1.03x slower                                        |
| pprint_pformat           | 1.46 sec                                               | 1.51 sec: 1.04x slower                                        |
| regex_dna                | 204 ms                                                 | 212 ms: 1.04x slower                                          |
| pathlib                  | 18.2 ms                                                | 19.0 ms: 1.04x slower                                         |
| logging_silent           | 101 ns                                                 | 105 ns: 1.04x slower                                          |
| comprehensions           | 22.4 us                                                | 23.4 us: 1.04x slower                                         |
| pickle_dict              | 31.1 us                                                | 32.5 us: 1.04x slower                                         |
| telco                    | 6.58 ms                                                | 6.87 ms: 1.04x slower                                         |
| hexiom                   | 6.37 ms                                                | 6.66 ms: 1.04x slower                                         |
| deepcopy                 | 342 us                                                 | 360 us: 1.05x slower                                          |
| pprint_safe_repr         | 701 ms                                                 | 741 ms: 1.06x slower                                          |
| unpack_sequence          | 43.1 ns                                                | 45.7 ns: 1.06x slower                                         |
| regex_v8                 | 22.0 ms                                                | 23.4 ms: 1.06x slower                                         |
| scimark_monte_carlo      | 68.1 ms                                                | 72.3 ms: 1.06x slower                                         |
| tomli_loads              | 2.22 sec                                               | 2.37 sec: 1.07x slower                                        |
| scimark_sor              | 118 ms                                                 | 127 ms: 1.08x slower                                          |
| sqlite_synth             | 2.52 us                                                | 2.73 us: 1.08x slower                                         |
| unpickle                 | 13.7 us                                                | 14.8 us: 1.09x slower                                         |
| xml_etree_process        | 53.9 ms                                                | 58.9 ms: 1.09x slower                                         |
| python_startup           | 8.52 ms                                                | 9.43 ms: 1.11x slower                                         |
| deepcopy_reduce          | 2.94 us                                                | 3.26 us: 1.11x slower                                         |
| pickle_list              | 4.11 us                                                | 4.57 us: 1.11x slower                                         |
| spectral_norm            | 100 ms                                                 | 111 ms: 1.11x slower                                          |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 5.06 ms: 1.12x slower                                         |
| fannkuch                 | 388 ms                                                 | 437 ms: 1.13x slower                                          |
| python_startup_no_site   | 6.01 ms                                                | 6.83 ms: 1.14x slower                                         |
| xml_etree_generate       | 76.2 ms                                                | 86.9 ms: 1.14x slower                                         |
| scimark_fft              | 328 ms                                                 | 375 ms: 1.14x slower                                          |
| crypto_pyaes             | 74.7 ms                                                | 86.0 ms: 1.15x slower                                         |
| float                    | 77.2 ms                                                | 88.9 ms: 1.15x slower                                         |
| pyflate                  | 418 ms                                                 | 485 ms: 1.16x slower                                          |
| scimark_lu               | 110 ms                                                 | 133 ms: 1.21x slower                                          |
| async_generators         | 368 ms                                                 | 459 ms: 1.24x slower                                          |
| mako                     | 10.1 ms                                                | 12.6 ms: 1.25x slower                                         |
| deepcopy_memo            | 37.0 us                                                | 49.5 us: 1.34x slower                                         |
| dask                     | 360 ms                                                 | 529 ms: 1.47x slower                                          |
| Geometric mean           | (ref)                                                  | 1.01x faster                                                  |

Benchmark hidden because not significant (6): meteor_contest, xml_etree_iterparse, nbody, bench_mp_pool, raytrace, nqueens
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
