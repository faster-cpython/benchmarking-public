
# Results vs. 3.11.0

- fork: brandtbucher
- ref: not_none
- machine: linux-x86_64
- commit hash: 806df38
- commit date: 2023-07-10
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.67 sec: 1.02x slower                                          |
| tornado_http   | 96.3 ms                                                | 97.4 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 89.4 ms: 1.04x faster                                           |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                            |
| float          | 77.2 ms                                                | 78.7 ms: 1.02x slower                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.57 ms: 1.12x faster                                           |
| regex_dna      | 204 ms                                                 | 210 ms: 1.03x slower                                            |
| regex_v8       | 22.0 ms                                                | 23.0 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.88 ms: 1.27x faster                                           |
| unpickle_pure_python | 228 us                                                 | 211 us: 1.08x faster                                            |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.04x faster                                            |
| pickle_pure_python   | 306 us                                                 | 296 us: 1.03x faster                                            |
| json_loads           | 26.5 us                                                | 25.7 us: 1.03x faster                                           |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                            |
| pickle_dict          | 31.1 us                                                | 31.9 us: 1.03x slower                                           |
| tomli_loads          | 2.22 sec                                               | 2.28 sec: 1.03x slower                                          |
| unpickle_list        | 4.91 us                                                | 5.12 us: 1.04x slower                                           |
| pickle               | 10.1 us                                                | 10.6 us: 1.05x slower                                           |
| xml_etree_process    | 53.9 ms                                                | 57.4 ms: 1.07x slower                                           |
| unpickle             | 13.7 us                                                | 14.8 us: 1.08x slower                                           |
| pickle_list          | 4.11 us                                                | 4.49 us: 1.09x slower                                           |
| xml_etree_generate   | 76.2 ms                                                | 84.6 ms: 1.11x slower                                           |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.17 ms: 1.08x slower                                           |
| python_startup_no_site | 6.01 ms                                                | 6.67 ms: 1.11x slower                                           |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.7 ms: 1.06x slower                                           |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-linux-x86_64-brandtbucher-not_none-3.13.0a0-806df38 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 146 us: 3.33x faster                                            |
| generators               | 73.5 ms                                                | 29.0 ms: 2.53x faster                                           |
| asyncio_tcp              | 922 ms                                                 | 507 ms: 1.82x faster                                            |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.78 sec: 1.76x faster                                          |
| json_dumps               | 12.6 ms                                                | 9.88 ms: 1.27x faster                                           |
| mypy2                    | 420 ms                                                 | 338 ms: 1.24x faster                                            |
| chaos                    | 69.2 ms                                                | 59.7 ms: 1.16x faster                                           |
| coroutines               | 25.5 ms                                                | 22.6 ms: 1.13x faster                                           |
| deltablue                | 3.67 ms                                                | 3.26 ms: 1.13x faster                                           |
| regex_effbot             | 3.99 ms                                                | 3.57 ms: 1.12x faster                                           |
| comprehensions           | 22.4 us                                                | 20.2 us: 1.11x faster                                           |
| async_tree_none          | 526 ms                                                 | 479 ms: 1.10x faster                                            |
| raytrace                 | 297 ms                                                 | 271 ms: 1.10x faster                                            |
| async_tree_io            | 1.30 sec                                               | 1.18 sec: 1.10x faster                                          |
| unpickle_pure_python     | 228 us                                                 | 211 us: 1.08x faster                                            |
| sqlglot_parse            | 1.40 ms                                                | 1.30 ms: 1.08x faster                                           |
| async_tree_memoization   | 627 ms                                                 | 584 ms: 1.08x faster                                            |
| crypto_pyaes             | 74.7 ms                                                | 69.6 ms: 1.07x faster                                           |
| hexiom                   | 6.37 ms                                                | 5.95 ms: 1.07x faster                                           |
| coverage                 | 100 ms                                                 | 94.0 ms: 1.06x faster                                           |
| sqlglot_transpile        | 1.70 ms                                                | 1.61 ms: 1.06x faster                                           |
| nqueens                  | 83.4 ms                                                | 79.2 ms: 1.05x faster                                           |
| richards_super           | 56.8 ms                                                | 54.3 ms: 1.05x faster                                           |
| nbody                    | 93.1 ms                                                | 89.4 ms: 1.04x faster                                           |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.04x faster                                            |
| pickle_pure_python       | 306 us                                                 | 296 us: 1.03x faster                                            |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 717 ms: 1.03x faster                                            |
| json_loads               | 26.5 us                                                | 25.7 us: 1.03x faster                                           |
| logging_format           | 6.68 us                                                | 6.54 us: 1.02x faster                                           |
| go                       | 140 ms                                                 | 137 ms: 1.02x faster                                            |
| pycparser                | 1.18 sec                                               | 1.16 sec: 1.02x faster                                          |
| mdp                      | 2.62 sec                                               | 2.58 sec: 1.02x faster                                          |
| sqlglot_normalize        | 108 ms                                                 | 106 ms: 1.02x faster                                            |
| logging_simple           | 6.03 us                                                | 5.96 us: 1.01x faster                                           |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                            |
| scimark_monte_carlo      | 68.1 ms                                                | 67.4 ms: 1.01x faster                                           |
| create_gc_cycles         | 1.49 ms                                                | 1.48 ms: 1.00x faster                                           |
| pidigits                 | 198 ms                                                 | 197 ms: 1.00x faster                                            |
| bench_thread_pool        | 819 us                                                 | 816 us: 1.00x faster                                            |
| sqlglot_optimize         | 53.1 ms                                                | 53.0 ms: 1.00x faster                                           |
| logging_silent           | 101 ns                                                 | 102 ns: 1.01x slower                                            |
| deepcopy_memo            | 37.0 us                                                | 37.4 us: 1.01x slower                                           |
| tornado_http             | 96.3 ms                                                | 97.4 ms: 1.01x slower                                           |
| gc_traversal             | 4.02 ms                                                | 4.07 ms: 1.01x slower                                           |
| scimark_sor              | 118 ms                                                 | 120 ms: 1.01x slower                                            |
| docutils                 | 2.63 sec                                               | 2.67 sec: 1.02x slower                                          |
| pathlib                  | 18.2 ms                                                | 18.5 ms: 1.02x slower                                           |
| float                    | 77.2 ms                                                | 78.7 ms: 1.02x slower                                           |
| pprint_pformat           | 1.46 sec                                               | 1.49 sec: 1.02x slower                                          |
| pickle_dict              | 31.1 us                                                | 31.9 us: 1.03x slower                                           |
| tomli_loads              | 2.22 sec                                               | 2.28 sec: 1.03x slower                                          |
| deepcopy                 | 342 us                                                 | 352 us: 1.03x slower                                            |
| regex_dna                | 204 ms                                                 | 210 ms: 1.03x slower                                            |
| pprint_safe_repr         | 701 ms                                                 | 725 ms: 1.03x slower                                            |
| spectral_norm            | 100 ms                                                 | 104 ms: 1.04x slower                                            |
| dulwich_log              | 63.7 ms                                                | 66.4 ms: 1.04x slower                                           |
| unpickle_list            | 4.91 us                                                | 5.12 us: 1.04x slower                                           |
| regex_v8                 | 22.0 ms                                                | 23.0 ms: 1.04x slower                                           |
| richards                 | 45.7 ms                                                | 47.8 ms: 1.04x slower                                           |
| pickle                   | 10.1 us                                                | 10.6 us: 1.05x slower                                           |
| mako                     | 10.1 ms                                                | 10.7 ms: 1.06x slower                                           |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.79 ms: 1.07x slower                                           |
| xml_etree_process        | 53.9 ms                                                | 57.4 ms: 1.07x slower                                           |
| pyflate                  | 418 ms                                                 | 446 ms: 1.07x slower                                            |
| python_startup           | 8.52 ms                                                | 9.17 ms: 1.08x slower                                           |
| scimark_fft              | 328 ms                                                 | 354 ms: 1.08x slower                                            |
| unpickle                 | 13.7 us                                                | 14.8 us: 1.08x slower                                           |
| sqlite_synth             | 2.52 us                                                | 2.73 us: 1.09x slower                                           |
| pickle_list              | 4.11 us                                                | 4.49 us: 1.09x slower                                           |
| deepcopy_reduce          | 2.94 us                                                | 3.21 us: 1.09x slower                                           |
| unpack_sequence          | 43.1 ns                                                | 47.0 ns: 1.09x slower                                           |
| telco                    | 6.58 ms                                                | 7.30 ms: 1.11x slower                                           |
| python_startup_no_site   | 6.01 ms                                                | 6.67 ms: 1.11x slower                                           |
| xml_etree_generate       | 76.2 ms                                                | 84.6 ms: 1.11x slower                                           |
| async_generators         | 368 ms                                                 | 443 ms: 1.20x slower                                            |
| dask                     | 360 ms                                                 | 523 ms: 1.45x slower                                            |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                    |

Benchmark hidden because not significant (6): meteor_contest, json, regex_compile, bench_mp_pool, scimark_lu, fannkuch
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
