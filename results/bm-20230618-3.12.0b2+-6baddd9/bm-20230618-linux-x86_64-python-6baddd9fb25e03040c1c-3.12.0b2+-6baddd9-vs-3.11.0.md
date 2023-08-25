
# Results vs. 3.11.0

- fork: python
- ref: 6baddd9fb25e03040c1c
- machine: linux-x86_64
- commit hash: 6baddd9
- commit date: 2023-06-18
- overall geometric mean: 1.03x faster
- HPT reliability: 54.10%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230618-linux-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 268 ms: 1.03x slower                                                   |
| docutils       | 2.63 sec                                               | 2.71 sec: 1.03x slower                                                 |
| tornado_http   | 96.3 ms                                                | 99.1 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230618-linux-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 88.9 ms: 1.05x faster                                                  |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                   |
| float          | 77.2 ms                                                | 79.6 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230618-linux-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.66 ms: 1.09x faster                                                  |
| regex_dna      | 204 ms                                                 | 211 ms: 1.03x slower                                                   |
| regex_compile  | 138 ms                                                 | 143 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230618-linux-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.74 ms: 1.29x faster                                                  |
| unpickle_pure_python | 228 us                                                 | 215 us: 1.06x faster                                                   |
| json_loads           | 26.5 us                                                | 25.0 us: 1.06x faster                                                  |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.04x faster                                                   |
| tomli_loads          | 2.22 sec                                               | 2.18 sec: 1.02x faster                                                 |
| pickle_dict          | 31.1 us                                                | 30.7 us: 1.01x faster                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                   |
| pickle_pure_python   | 306 us                                                 | 310 us: 1.01x slower                                                   |
| unpickle_list        | 4.91 us                                                | 5.02 us: 1.02x slower                                                  |
| pickle               | 10.1 us                                                | 10.8 us: 1.07x slower                                                  |
| xml_etree_process    | 53.9 ms                                                | 58.7 ms: 1.09x slower                                                  |
| xml_etree_generate   | 76.2 ms                                                | 84.6 ms: 1.11x slower                                                  |
| unpickle             | 13.7 us                                                | 15.2 us: 1.11x slower                                                  |
| pickle_list          | 4.11 us                                                | 4.57 us: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230618-linux-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.31 ms: 1.09x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.75 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230618-linux-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                  |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230618-linux-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 145 us: 3.36x faster                                                   |
| generators               | 73.5 ms                                                | 32.2 ms: 2.28x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 512 ms: 1.80x faster                                                   |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                 |
| json_dumps               | 12.6 ms                                                | 9.74 ms: 1.29x faster                                                  |
| coroutines               | 25.5 ms                                                | 22.0 ms: 1.16x faster                                                  |
| richards_super           | 56.8 ms                                                | 49.5 ms: 1.15x faster                                                  |
| gc_traversal             | 4.02 ms                                                | 3.55 ms: 1.13x faster                                                  |
| async_tree_none          | 526 ms                                                 | 468 ms: 1.12x faster                                                   |
| async_tree_io            | 1.30 sec                                               | 1.15 sec: 1.12x faster                                                 |
| chaos                    | 69.2 ms                                                | 62.8 ms: 1.10x faster                                                  |
| async_tree_memoization   | 627 ms                                                 | 573 ms: 1.10x faster                                                   |
| regex_effbot             | 3.99 ms                                                | 3.66 ms: 1.09x faster                                                  |
| comprehensions           | 22.4 us                                                | 20.7 us: 1.08x faster                                                  |
| deltablue                | 3.67 ms                                                | 3.45 ms: 1.06x faster                                                  |
| unpickle_pure_python     | 228 us                                                 | 215 us: 1.06x faster                                                   |
| json_loads               | 26.5 us                                                | 25.0 us: 1.06x faster                                                  |
| sqlglot_parse            | 1.40 ms                                                | 1.33 ms: 1.06x faster                                                  |
| coverage                 | 100 ms                                                 | 95.0 ms: 1.05x faster                                                  |
| hexiom                   | 6.37 ms                                                | 6.06 ms: 1.05x faster                                                  |
| nbody                    | 93.1 ms                                                | 88.9 ms: 1.05x faster                                                  |
| nqueens                  | 83.4 ms                                                | 79.7 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 708 ms: 1.04x faster                                                   |
| xml_etree_parse          | 158 ms                                                 | 152 ms: 1.04x faster                                                   |
| logging_silent           | 101 ns                                                 | 97.2 ns: 1.04x faster                                                  |
| richards                 | 45.7 ms                                                | 44.0 ms: 1.04x faster                                                  |
| json                     | 4.94 ms                                                | 4.76 ms: 1.04x faster                                                  |
| sqlglot_transpile        | 1.70 ms                                                | 1.64 ms: 1.04x faster                                                  |
| pycparser                | 1.18 sec                                               | 1.14 sec: 1.03x faster                                                 |
| go                       | 140 ms                                                 | 136 ms: 1.03x faster                                                   |
| mdp                      | 2.62 sec                                               | 2.55 sec: 1.03x faster                                                 |
| fannkuch                 | 388 ms                                                 | 379 ms: 1.02x faster                                                   |
| tomli_loads              | 2.22 sec                                               | 2.18 sec: 1.02x faster                                                 |
| raytrace                 | 297 ms                                                 | 292 ms: 1.02x faster                                                   |
| pickle_dict              | 31.1 us                                                | 30.7 us: 1.01x faster                                                  |
| pathlib                  | 18.2 ms                                                | 18.1 ms: 1.01x faster                                                  |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                                   |
| pidigits                 | 198 ms                                                 | 197 ms: 1.00x faster                                                   |
| create_gc_cycles         | 1.49 ms                                                | 1.50 ms: 1.01x slower                                                  |
| sqlglot_optimize         | 53.1 ms                                                | 53.6 ms: 1.01x slower                                                  |
| bench_thread_pool        | 819 us                                                 | 828 us: 1.01x slower                                                   |
| deepcopy_memo            | 37.0 us                                                | 37.5 us: 1.01x slower                                                  |
| pickle_pure_python       | 306 us                                                 | 310 us: 1.01x slower                                                   |
| unpickle_list            | 4.91 us                                                | 5.02 us: 1.02x slower                                                  |
| scimark_lu               | 110 ms                                                 | 113 ms: 1.03x slower                                                   |
| tornado_http             | 96.3 ms                                                | 99.1 ms: 1.03x slower                                                  |
| docutils                 | 2.63 sec                                               | 2.71 sec: 1.03x slower                                                 |
| float                    | 77.2 ms                                                | 79.6 ms: 1.03x slower                                                  |
| 2to3                     | 259 ms                                                 | 268 ms: 1.03x slower                                                   |
| regex_dna                | 204 ms                                                 | 211 ms: 1.03x slower                                                   |
| sqlalchemy_imperative    | 17.9 ms                                                | 18.5 ms: 1.03x slower                                                  |
| crypto_pyaes             | 74.7 ms                                                | 77.3 ms: 1.04x slower                                                  |
| logging_format           | 6.68 us                                                | 6.92 us: 1.04x slower                                                  |
| deepcopy                 | 342 us                                                 | 355 us: 1.04x slower                                                   |
| regex_compile            | 138 ms                                                 | 143 ms: 1.04x slower                                                   |
| pprint_pformat           | 1.46 sec                                               | 1.52 sec: 1.04x slower                                                 |
| scimark_monte_carlo      | 68.1 ms                                                | 71.0 ms: 1.04x slower                                                  |
| sqlalchemy_declarative   | 138 ms                                                 | 144 ms: 1.04x slower                                                   |
| logging_simple           | 6.03 us                                                | 6.31 us: 1.05x slower                                                  |
| telco                    | 6.58 ms                                                | 6.93 ms: 1.05x slower                                                  |
| pprint_safe_repr         | 701 ms                                                 | 739 ms: 1.05x slower                                                   |
| spectral_norm            | 100 ms                                                 | 106 ms: 1.06x slower                                                   |
| pyflate                  | 418 ms                                                 | 442 ms: 1.06x slower                                                   |
| mako                     | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                  |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.76 ms: 1.06x slower                                                  |
| deepcopy_reduce          | 2.94 us                                                | 3.14 us: 1.07x slower                                                  |
| dulwich_log              | 63.7 ms                                                | 68.1 ms: 1.07x slower                                                  |
| pickle                   | 10.1 us                                                | 10.8 us: 1.07x slower                                                  |
| sqlite_synth             | 2.52 us                                                | 2.73 us: 1.08x slower                                                  |
| xml_etree_process        | 53.9 ms                                                | 58.7 ms: 1.09x slower                                                  |
| python_startup           | 8.52 ms                                                | 9.31 ms: 1.09x slower                                                  |
| scimark_fft              | 328 ms                                                 | 361 ms: 1.10x slower                                                   |
| xml_etree_generate       | 76.2 ms                                                | 84.6 ms: 1.11x slower                                                  |
| unpickle                 | 13.7 us                                                | 15.2 us: 1.11x slower                                                  |
| pickle_list              | 4.11 us                                                | 4.57 us: 1.11x slower                                                  |
| python_startup_no_site   | 6.01 ms                                                | 6.75 ms: 1.12x slower                                                  |
| async_generators         | 368 ms                                                 | 439 ms: 1.19x slower                                                   |
| unpack_sequence          | 43.1 ns                                                | 54.8 ns: 1.27x slower                                                  |
| dask                     | 360 ms                                                 | 534 ms: 1.48x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (6): meteor_contest, bench_mp_pool, regex_v8, sqlglot_normalize, scimark_sor, mypy2
Ignored benchmarks (15) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 54.10% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
