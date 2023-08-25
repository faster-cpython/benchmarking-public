
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: a47c13c
- commit date: 2023-08-19
- overall geometric mean: 1.04x faster
- HPT reliability: 82.54%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-linux-x86_64-python-main-3.13.0a0-a47c13c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 93.1 ms                                                | 90.9 ms: 1.02x faster                                 |
| pidigits       | 198 ms                                                 | 201 ms: 1.01x slower                                  |
| float          | 77.2 ms                                                | 79.7 ms: 1.03x slower                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-linux-x86_64-python-main-3.13.0a0-a47c13c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.55 ms: 1.12x faster                                 |
| regex_compile  | 138 ms                                                 | 136 ms: 1.02x faster                                  |
| regex_dna      | 204 ms                                                 | 215 ms: 1.06x slower                                  |
| regex_v8       | 22.0 ms                                                | 24.7 ms: 1.12x slower                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-linux-x86_64-python-main-3.13.0a0-a47c13c |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.84 ms: 1.28x faster                                 |
| unpickle_pure_python | 228 us                                                 | 215 us: 1.06x faster                                  |
| tomli_loads          | 2.22 sec                                               | 2.10 sec: 1.06x faster                                |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.04x faster                                  |
| json_loads           | 26.5 us                                                | 25.7 us: 1.03x faster                                 |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.01x faster                                  |
| pickle_pure_python   | 306 us                                                 | 303 us: 1.01x faster                                  |
| unpickle_list        | 4.91 us                                                | 4.88 us: 1.01x faster                                 |
| pickle_dict          | 31.1 us                                                | 31.4 us: 1.01x slower                                 |
| unpickle             | 13.7 us                                                | 14.2 us: 1.04x slower                                 |
| pickle               | 10.1 us                                                | 10.6 us: 1.06x slower                                 |
| xml_etree_process    | 53.9 ms                                                | 58.2 ms: 1.08x slower                                 |
| xml_etree_generate   | 76.2 ms                                                | 83.2 ms: 1.09x slower                                 |
| pickle_list          | 4.11 us                                                | 4.62 us: 1.12x slower                                 |
| Geometric mean       | (ref)                                                  | 1.01x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-linux-x86_64-python-main-3.13.0a0-a47c13c |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.34 ms: 1.10x slower                                 |
| python_startup_no_site | 6.01 ms                                                | 6.85 ms: 1.14x slower                                 |
| Geometric mean         | (ref)                                                  | 1.12x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-linux-x86_64-python-main-3.13.0a0-a47c13c |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.8 ms: 1.07x slower                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-linux-x86_64-python-main-3.13.0a0-a47c13c |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 145 us: 3.35x faster                                  |
| generators               | 73.5 ms                                                | 29.2 ms: 2.52x faster                                 |
| asyncio_tcp              | 922 ms                                                 | 487 ms: 1.89x faster                                  |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.78 sec: 1.76x faster                                |
| json_dumps               | 12.6 ms                                                | 9.84 ms: 1.28x faster                                 |
| async_tree_none          | 526 ms                                                 | 439 ms: 1.20x faster                                  |
| coverage                 | 100 ms                                                 | 84.7 ms: 1.18x faster                                 |
| chaos                    | 69.2 ms                                                | 59.8 ms: 1.16x faster                                 |
| coroutines               | 25.5 ms                                                | 22.3 ms: 1.14x faster                                 |
| regex_effbot             | 3.99 ms                                                | 3.55 ms: 1.12x faster                                 |
| async_tree_memoization   | 627 ms                                                 | 560 ms: 1.12x faster                                  |
| deltablue                | 3.67 ms                                                | 3.32 ms: 1.11x faster                                 |
| async_tree_io            | 1.30 sec                                               | 1.19 sec: 1.09x faster                                |
| sqlglot_parse            | 1.40 ms                                                | 1.28 ms: 1.09x faster                                 |
| raytrace                 | 297 ms                                                 | 275 ms: 1.08x faster                                  |
| comprehensions           | 22.4 us                                                | 20.9 us: 1.07x faster                                 |
| sqlglot_transpile        | 1.70 ms                                                | 1.60 ms: 1.07x faster                                 |
| crypto_pyaes             | 74.7 ms                                                | 70.1 ms: 1.07x faster                                 |
| unpickle_pure_python     | 228 us                                                 | 215 us: 1.06x faster                                  |
| tomli_loads              | 2.22 sec                                               | 2.10 sec: 1.06x faster                                |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 701 ms: 1.05x faster                                  |
| nqueens                  | 83.4 ms                                                | 79.5 ms: 1.05x faster                                 |
| richards_super           | 56.8 ms                                                | 54.2 ms: 1.05x faster                                 |
| hexiom                   | 6.37 ms                                                | 6.11 ms: 1.04x faster                                 |
| xml_etree_parse          | 158 ms                                                 | 152 ms: 1.04x faster                                  |
| json_loads               | 26.5 us                                                | 25.7 us: 1.03x faster                                 |
| mdp                      | 2.62 sec                                               | 2.54 sec: 1.03x faster                                |
| nbody                    | 93.1 ms                                                | 90.9 ms: 1.02x faster                                 |
| gc_traversal             | 4.02 ms                                                | 3.93 ms: 1.02x faster                                 |
| logging_format           | 6.68 us                                                | 6.53 us: 1.02x faster                                 |
| logging_simple           | 6.03 us                                                | 5.90 us: 1.02x faster                                 |
| sqlglot_normalize        | 108 ms                                                 | 106 ms: 1.02x faster                                  |
| regex_compile            | 138 ms                                                 | 136 ms: 1.02x faster                                  |
| json                     | 4.94 ms                                                | 4.86 ms: 1.02x faster                                 |
| xml_etree_iterparse      | 104 ms                                                 | 102 ms: 1.01x faster                                  |
| scimark_monte_carlo      | 68.1 ms                                                | 67.2 ms: 1.01x faster                                 |
| pickle_pure_python       | 306 us                                                 | 303 us: 1.01x faster                                  |
| sqlglot_optimize         | 53.1 ms                                                | 52.7 ms: 1.01x faster                                 |
| fannkuch                 | 388 ms                                                 | 385 ms: 1.01x faster                                  |
| unpickle_list            | 4.91 us                                                | 4.88 us: 1.01x faster                                 |
| pickle_dict              | 31.1 us                                                | 31.4 us: 1.01x slower                                 |
| deepcopy_memo            | 37.0 us                                                | 37.4 us: 1.01x slower                                 |
| create_gc_cycles         | 1.49 ms                                                | 1.51 ms: 1.01x slower                                 |
| pidigits                 | 198 ms                                                 | 201 ms: 1.01x slower                                  |
| pycparser                | 1.18 sec                                               | 1.20 sec: 1.02x slower                                |
| pathlib                  | 18.2 ms                                                | 18.5 ms: 1.02x slower                                 |
| go                       | 140 ms                                                 | 142 ms: 1.02x slower                                  |
| unpack_sequence          | 43.1 ns                                                | 43.8 ns: 1.02x slower                                 |
| logging_silent           | 101 ns                                                 | 104 ns: 1.02x slower                                  |
| deepcopy                 | 342 us                                                 | 351 us: 1.03x slower                                  |
| pprint_pformat           | 1.46 sec                                               | 1.50 sec: 1.03x slower                                |
| float                    | 77.2 ms                                                | 79.7 ms: 1.03x slower                                 |
| scimark_sor              | 118 ms                                                 | 122 ms: 1.03x slower                                  |
| unpickle                 | 13.7 us                                                | 14.2 us: 1.04x slower                                 |
| dulwich_log              | 63.7 ms                                                | 66.4 ms: 1.04x slower                                 |
| richards                 | 45.7 ms                                                | 47.7 ms: 1.04x slower                                 |
| pprint_safe_repr         | 701 ms                                                 | 733 ms: 1.04x slower                                  |
| deepcopy_reduce          | 2.94 us                                                | 3.10 us: 1.05x slower                                 |
| regex_dna                | 204 ms                                                 | 215 ms: 1.06x slower                                  |
| pickle                   | 10.1 us                                                | 10.6 us: 1.06x slower                                 |
| spectral_norm            | 100 ms                                                 | 106 ms: 1.06x slower                                  |
| mako                     | 10.1 ms                                                | 10.8 ms: 1.07x slower                                 |
| scimark_fft              | 328 ms                                                 | 354 ms: 1.08x slower                                  |
| xml_etree_process        | 53.9 ms                                                | 58.2 ms: 1.08x slower                                 |
| pyflate                  | 418 ms                                                 | 452 ms: 1.08x slower                                  |
| sqlite_synth             | 2.52 us                                                | 2.75 us: 1.09x slower                                 |
| xml_etree_generate       | 76.2 ms                                                | 83.2 ms: 1.09x slower                                 |
| python_startup           | 8.52 ms                                                | 9.34 ms: 1.10x slower                                 |
| regex_v8                 | 22.0 ms                                                | 24.7 ms: 1.12x slower                                 |
| pickle_list              | 4.11 us                                                | 4.62 us: 1.12x slower                                 |
| python_startup_no_site   | 6.01 ms                                                | 6.85 ms: 1.14x slower                                 |
| telco                    | 6.58 ms                                                | 7.98 ms: 1.21x slower                                 |
| async_generators         | 368 ms                                                 | 447 ms: 1.21x slower                                  |
| dask                     | 360 ms                                                 | 524 ms: 1.46x slower                                  |
| Geometric mean           | (ref)                                                  | 1.04x faster                                          |

Benchmark hidden because not significant (8): meteor_contest, tornado_http, docutils, bench_thread_pool, bench_mp_pool, scimark_lu, scimark_sparse_mat_mult, mypy2
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 82.54% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
