
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: 236cdad
- commit date: 2023-08-05
- overall geometric mean: 1.03x faster
- HPT reliability: 79.31%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-python-3.12-3.12.0b4+-236cdad |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 268 ms: 1.03x slower                                   |
| docutils       | 2.63 sec                                               | 2.71 sec: 1.03x slower                                 |
| tornado_http   | 96.3 ms                                                | 99.3 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-python-3.12-3.12.0b4+-236cdad |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 89.9 ms: 1.04x faster                                  |
| pidigits       | 198 ms                                                 | 200 ms: 1.01x slower                                   |
| float          | 77.2 ms                                                | 80.6 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-python-3.12-3.12.0b4+-236cdad |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.54 ms: 1.13x faster                                  |
| regex_dna      | 204 ms                                                 | 211 ms: 1.04x slower                                   |
| regex_compile  | 138 ms                                                 | 145 ms: 1.05x slower                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-python-3.12-3.12.0b4+-236cdad |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.84 ms: 1.28x faster                                  |
| unpickle_pure_python | 228 us                                                 | 215 us: 1.06x faster                                   |
| json_loads           | 26.5 us                                                | 25.0 us: 1.06x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                   |
| tomli_loads          | 2.22 sec                                               | 2.20 sec: 1.01x faster                                 |
| pickle_pure_python   | 306 us                                                 | 309 us: 1.01x slower                                   |
| unpickle_list        | 4.91 us                                                | 4.96 us: 1.01x slower                                  |
| pickle_dict          | 31.1 us                                                | 31.9 us: 1.03x slower                                  |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                  |
| xml_etree_process    | 53.9 ms                                                | 59.3 ms: 1.10x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 85.2 ms: 1.12x slower                                  |
| pickle_list          | 4.11 us                                                | 4.61 us: 1.12x slower                                  |
| unpickle             | 13.7 us                                                | 15.8 us: 1.16x slower                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-python-3.12-3.12.0b4+-236cdad |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.33 ms: 1.09x slower                                  |
| python_startup_no_site | 6.01 ms                                                | 6.78 ms: 1.13x slower                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-python-3.12-3.12.0b4+-236cdad |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.8 ms: 1.07x slower                                  |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-python-3.12-3.12.0b4+-236cdad |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 150 us: 3.25x faster                                   |
| generators               | 73.5 ms                                                | 31.2 ms: 2.36x faster                                  |
| asyncio_tcp              | 922 ms                                                 | 514 ms: 1.79x faster                                   |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                 |
| json_dumps               | 12.6 ms                                                | 9.84 ms: 1.28x faster                                  |
| mypy2                    | 420 ms                                                 | 344 ms: 1.22x faster                                   |
| coroutines               | 25.5 ms                                                | 22.2 ms: 1.15x faster                                  |
| richards_super           | 56.8 ms                                                | 49.6 ms: 1.14x faster                                  |
| regex_effbot             | 3.99 ms                                                | 3.54 ms: 1.13x faster                                  |
| async_tree_none          | 526 ms                                                 | 471 ms: 1.12x faster                                   |
| async_tree_io            | 1.30 sec                                               | 1.16 sec: 1.11x faster                                 |
| chaos                    | 69.2 ms                                                | 63.3 ms: 1.09x faster                                  |
| async_tree_memoization   | 627 ms                                                 | 576 ms: 1.09x faster                                   |
| comprehensions           | 22.4 us                                                | 20.8 us: 1.08x faster                                  |
| unpickle_pure_python     | 228 us                                                 | 215 us: 1.06x faster                                   |
| json_loads               | 26.5 us                                                | 25.0 us: 1.06x faster                                  |
| deltablue                | 3.67 ms                                                | 3.50 ms: 1.05x faster                                  |
| sqlglot_parse            | 1.40 ms                                                | 1.34 ms: 1.05x faster                                  |
| coverage                 | 100 ms                                                 | 95.7 ms: 1.05x faster                                  |
| pycparser                | 1.18 sec                                               | 1.13 sec: 1.04x faster                                 |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 710 ms: 1.04x faster                                   |
| richards                 | 45.7 ms                                                | 44.0 ms: 1.04x faster                                  |
| hexiom                   | 6.37 ms                                                | 6.13 ms: 1.04x faster                                  |
| go                       | 140 ms                                                 | 135 ms: 1.04x faster                                   |
| nbody                    | 93.1 ms                                                | 89.9 ms: 1.04x faster                                  |
| json                     | 4.94 ms                                                | 4.78 ms: 1.03x faster                                  |
| nqueens                  | 83.4 ms                                                | 80.8 ms: 1.03x faster                                  |
| xml_etree_parse          | 158 ms                                                 | 154 ms: 1.03x faster                                   |
| sqlglot_transpile        | 1.70 ms                                                | 1.66 ms: 1.03x faster                                  |
| mdp                      | 2.62 sec                                               | 2.55 sec: 1.03x faster                                 |
| pathlib                  | 18.2 ms                                                | 18.0 ms: 1.01x faster                                  |
| logging_silent           | 101 ns                                                 | 100.0 ns: 1.01x faster                                 |
| gc_traversal             | 4.02 ms                                                | 3.98 ms: 1.01x faster                                  |
| tomli_loads              | 2.22 sec                                               | 2.20 sec: 1.01x faster                                 |
| pickle_pure_python       | 306 us                                                 | 309 us: 1.01x slower                                   |
| scimark_lu               | 110 ms                                                 | 111 ms: 1.01x slower                                   |
| unpickle_list            | 4.91 us                                                | 4.96 us: 1.01x slower                                  |
| pidigits                 | 198 ms                                                 | 200 ms: 1.01x slower                                   |
| fannkuch                 | 388 ms                                                 | 394 ms: 1.02x slower                                   |
| sqlglot_optimize         | 53.1 ms                                                | 54.1 ms: 1.02x slower                                  |
| sqlglot_normalize        | 108 ms                                                 | 110 ms: 1.02x slower                                   |
| bench_thread_pool        | 819 us                                                 | 834 us: 1.02x slower                                   |
| create_gc_cycles         | 1.49 ms                                                | 1.52 ms: 1.02x slower                                  |
| pickle_dict              | 31.1 us                                                | 31.9 us: 1.03x slower                                  |
| pprint_pformat           | 1.46 sec                                               | 1.50 sec: 1.03x slower                                 |
| docutils                 | 2.63 sec                                               | 2.71 sec: 1.03x slower                                 |
| tornado_http             | 96.3 ms                                                | 99.3 ms: 1.03x slower                                  |
| logging_simple           | 6.03 us                                                | 6.23 us: 1.03x slower                                  |
| deepcopy                 | 342 us                                                 | 353 us: 1.03x slower                                   |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.65 ms: 1.03x slower                                  |
| 2to3                     | 259 ms                                                 | 268 ms: 1.03x slower                                   |
| regex_dna                | 204 ms                                                 | 211 ms: 1.04x slower                                   |
| scimark_sor              | 118 ms                                                 | 123 ms: 1.04x slower                                   |
| sqlalchemy_declarative   | 138 ms                                                 | 144 ms: 1.04x slower                                   |
| float                    | 77.2 ms                                                | 80.6 ms: 1.04x slower                                  |
| pickle                   | 10.1 us                                                | 10.5 us: 1.04x slower                                  |
| scimark_monte_carlo      | 68.1 ms                                                | 71.0 ms: 1.04x slower                                  |
| logging_format           | 6.68 us                                                | 6.98 us: 1.04x slower                                  |
| crypto_pyaes             | 74.7 ms                                                | 78.0 ms: 1.04x slower                                  |
| regex_compile            | 138 ms                                                 | 145 ms: 1.05x slower                                   |
| sqlalchemy_imperative    | 17.9 ms                                                | 18.8 ms: 1.05x slower                                  |
| telco                    | 6.58 ms                                                | 6.92 ms: 1.05x slower                                  |
| spectral_norm            | 100 ms                                                 | 105 ms: 1.05x slower                                   |
| pprint_safe_repr         | 701 ms                                                 | 739 ms: 1.05x slower                                   |
| deepcopy_reduce          | 2.94 us                                                | 3.13 us: 1.06x slower                                  |
| mako                     | 10.1 ms                                                | 10.8 ms: 1.07x slower                                  |
| dulwich_log              | 63.7 ms                                                | 67.9 ms: 1.07x slower                                  |
| pyflate                  | 418 ms                                                 | 450 ms: 1.08x slower                                   |
| sqlite_synth             | 2.52 us                                                | 2.76 us: 1.09x slower                                  |
| python_startup           | 8.52 ms                                                | 9.33 ms: 1.09x slower                                  |
| scimark_fft              | 328 ms                                                 | 360 ms: 1.10x slower                                   |
| xml_etree_process        | 53.9 ms                                                | 59.3 ms: 1.10x slower                                  |
| xml_etree_generate       | 76.2 ms                                                | 85.2 ms: 1.12x slower                                  |
| pickle_list              | 4.11 us                                                | 4.61 us: 1.12x slower                                  |
| python_startup_no_site   | 6.01 ms                                                | 6.78 ms: 1.13x slower                                  |
| unpickle                 | 13.7 us                                                | 15.8 us: 1.16x slower                                  |
| unpack_sequence          | 43.1 ns                                                | 51.9 ns: 1.21x slower                                  |
| async_generators         | 368 ms                                                 | 448 ms: 1.22x slower                                   |
| dask                     | 360 ms                                                 | 536 ms: 1.49x slower                                   |
| Geometric mean           | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (6): bench_mp_pool, raytrace, deepcopy_memo, regex_v8, xml_etree_iterparse, meteor_contest
Ignored benchmarks (15) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 79.31% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
