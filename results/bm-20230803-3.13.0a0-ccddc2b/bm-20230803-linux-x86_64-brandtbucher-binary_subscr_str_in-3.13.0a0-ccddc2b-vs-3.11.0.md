
# Results vs. 3.11.0

- fork: brandtbucher
- ref: binary_subscr_str_in
- machine: linux-x86_64
- commit hash: ccddc2b
- commit date: 2023-08-03
- overall geometric mean: 1.04x faster
- HPT reliability: 61.55%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230803-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-ccddc2b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.66 sec: 1.01x slower                                                      |
| tornado_http   | 96.3 ms                                                | 95.7 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230803-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-ccddc2b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 94.3 ms: 1.01x slower                                                       |
| pidigits       | 198 ms                                                 | 201 ms: 1.01x slower                                                        |
| float          | 77.2 ms                                                | 80.1 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230803-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-ccddc2b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.55 ms: 1.12x faster                                                       |
| regex_compile  | 138 ms                                                 | 138 ms: 1.00x faster                                                        |
| regex_v8       | 22.0 ms                                                | 23.0 ms: 1.04x slower                                                       |
| regex_dna      | 204 ms                                                 | 216 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230803-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-ccddc2b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.79 ms: 1.29x faster                                                       |
| unpickle_pure_python | 228 us                                                 | 215 us: 1.06x faster                                                        |
| tomli_loads          | 2.22 sec                                               | 2.13 sec: 1.04x faster                                                      |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.04x faster                                                        |
| pickle_pure_python   | 306 us                                                 | 295 us: 1.04x faster                                                        |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                        |
| pickle_dict          | 31.1 us                                                | 31.5 us: 1.01x slower                                                       |
| unpickle_list        | 4.91 us                                                | 5.11 us: 1.04x slower                                                       |
| pickle               | 10.1 us                                                | 10.5 us: 1.05x slower                                                       |
| xml_etree_process    | 53.9 ms                                                | 58.3 ms: 1.08x slower                                                       |
| unpickle             | 13.7 us                                                | 15.0 us: 1.10x slower                                                       |
| pickle_list          | 4.11 us                                                | 4.51 us: 1.10x slower                                                       |
| xml_etree_generate   | 76.2 ms                                                | 84.6 ms: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230803-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-ccddc2b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.40 ms: 1.10x slower                                                       |
| python_startup_no_site | 6.01 ms                                                | 6.87 ms: 1.14x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230803-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-ccddc2b |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230803-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-ccddc2b |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 143 us: 3.39x faster                                                        |
| generators               | 73.5 ms                                                | 29.6 ms: 2.48x faster                                                       |
| asyncio_tcp              | 922 ms                                                 | 485 ms: 1.90x faster                                                        |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.76x faster                                                      |
| json_dumps               | 12.6 ms                                                | 9.79 ms: 1.29x faster                                                       |
| mypy2                    | 420 ms                                                 | 337 ms: 1.25x faster                                                        |
| chaos                    | 69.2 ms                                                | 60.3 ms: 1.15x faster                                                       |
| deltablue                | 3.67 ms                                                | 3.21 ms: 1.15x faster                                                       |
| coroutines               | 25.5 ms                                                | 22.4 ms: 1.14x faster                                                       |
| regex_effbot             | 3.99 ms                                                | 3.55 ms: 1.12x faster                                                       |
| comprehensions           | 22.4 us                                                | 20.4 us: 1.10x faster                                                       |
| sqlglot_parse            | 1.40 ms                                                | 1.28 ms: 1.10x faster                                                       |
| raytrace                 | 297 ms                                                 | 272 ms: 1.09x faster                                                        |
| async_tree_none          | 526 ms                                                 | 484 ms: 1.09x faster                                                        |
| async_tree_io            | 1.30 sec                                               | 1.19 sec: 1.09x faster                                                      |
| async_tree_memoization   | 627 ms                                                 | 587 ms: 1.07x faster                                                        |
| sqlglot_transpile        | 1.70 ms                                                | 1.59 ms: 1.07x faster                                                       |
| coverage                 | 100 ms                                                 | 93.9 ms: 1.07x faster                                                       |
| unpickle_pure_python     | 228 us                                                 | 215 us: 1.06x faster                                                        |
| crypto_pyaes             | 74.7 ms                                                | 70.5 ms: 1.06x faster                                                       |
| tomli_loads              | 2.22 sec                                               | 2.13 sec: 1.04x faster                                                      |
| richards_super           | 56.8 ms                                                | 54.5 ms: 1.04x faster                                                       |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.04x faster                                                        |
| pickle_pure_python       | 306 us                                                 | 295 us: 1.04x faster                                                        |
| nqueens                  | 83.4 ms                                                | 80.7 ms: 1.03x faster                                                       |
| sqlglot_normalize        | 108 ms                                                 | 105 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 721 ms: 1.03x faster                                                        |
| mdp                      | 2.62 sec                                               | 2.55 sec: 1.02x faster                                                      |
| hexiom                   | 6.37 ms                                                | 6.23 ms: 1.02x faster                                                       |
| logging_format           | 6.68 us                                                | 6.56 us: 1.02x faster                                                       |
| pycparser                | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                      |
| gc_traversal             | 4.02 ms                                                | 3.99 ms: 1.01x faster                                                       |
| logging_simple           | 6.03 us                                                | 5.99 us: 1.01x faster                                                       |
| go                       | 140 ms                                                 | 139 ms: 1.01x faster                                                        |
| tornado_http             | 96.3 ms                                                | 95.7 ms: 1.01x faster                                                       |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                                        |
| sqlglot_optimize         | 53.1 ms                                                | 52.8 ms: 1.01x faster                                                       |
| regex_compile            | 138 ms                                                 | 138 ms: 1.00x faster                                                        |
| bench_thread_pool        | 819 us                                                 | 826 us: 1.01x slower                                                        |
| docutils                 | 2.63 sec                                               | 2.66 sec: 1.01x slower                                                      |
| pickle_dict              | 31.1 us                                                | 31.5 us: 1.01x slower                                                       |
| pprint_pformat           | 1.46 sec                                               | 1.47 sec: 1.01x slower                                                      |
| nbody                    | 93.1 ms                                                | 94.3 ms: 1.01x slower                                                       |
| pidigits                 | 198 ms                                                 | 201 ms: 1.01x slower                                                        |
| pathlib                  | 18.2 ms                                                | 18.5 ms: 1.01x slower                                                       |
| create_gc_cycles         | 1.49 ms                                                | 1.51 ms: 1.02x slower                                                       |
| scimark_monte_carlo      | 68.1 ms                                                | 69.3 ms: 1.02x slower                                                       |
| pprint_safe_repr         | 701 ms                                                 | 719 ms: 1.02x slower                                                        |
| deepcopy_memo            | 37.0 us                                                | 38.2 us: 1.03x slower                                                       |
| scimark_sor              | 118 ms                                                 | 122 ms: 1.03x slower                                                        |
| deepcopy                 | 342 us                                                 | 354 us: 1.04x slower                                                        |
| float                    | 77.2 ms                                                | 80.1 ms: 1.04x slower                                                       |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.66 ms: 1.04x slower                                                       |
| fannkuch                 | 388 ms                                                 | 402 ms: 1.04x slower                                                        |
| unpickle_list            | 4.91 us                                                | 5.11 us: 1.04x slower                                                       |
| regex_v8                 | 22.0 ms                                                | 23.0 ms: 1.04x slower                                                       |
| dulwich_log              | 63.7 ms                                                | 66.4 ms: 1.04x slower                                                       |
| pickle                   | 10.1 us                                                | 10.5 us: 1.05x slower                                                       |
| richards                 | 45.7 ms                                                | 48.3 ms: 1.06x slower                                                       |
| regex_dna                | 204 ms                                                 | 216 ms: 1.06x slower                                                        |
| logging_silent           | 101 ns                                                 | 108 ns: 1.07x slower                                                        |
| scimark_fft              | 328 ms                                                 | 354 ms: 1.08x slower                                                        |
| pyflate                  | 418 ms                                                 | 452 ms: 1.08x slower                                                        |
| xml_etree_process        | 53.9 ms                                                | 58.3 ms: 1.08x slower                                                       |
| mako                     | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                       |
| unpack_sequence          | 43.1 ns                                                | 46.9 ns: 1.09x slower                                                       |
| deepcopy_reduce          | 2.94 us                                                | 3.22 us: 1.09x slower                                                       |
| unpickle                 | 13.7 us                                                | 15.0 us: 1.10x slower                                                       |
| pickle_list              | 4.11 us                                                | 4.51 us: 1.10x slower                                                       |
| sqlite_synth             | 2.52 us                                                | 2.76 us: 1.10x slower                                                       |
| spectral_norm            | 100 ms                                                 | 110 ms: 1.10x slower                                                        |
| python_startup           | 8.52 ms                                                | 9.40 ms: 1.10x slower                                                       |
| xml_etree_generate       | 76.2 ms                                                | 84.6 ms: 1.11x slower                                                       |
| python_startup_no_site   | 6.01 ms                                                | 6.87 ms: 1.14x slower                                                       |
| telco                    | 6.58 ms                                                | 7.77 ms: 1.18x slower                                                       |
| async_generators         | 368 ms                                                 | 446 ms: 1.21x slower                                                        |
| dask                     | 360 ms                                                 | 523 ms: 1.45x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (5): meteor_contest, scimark_lu, json_loads, json, bench_mp_pool
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 61.55% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
