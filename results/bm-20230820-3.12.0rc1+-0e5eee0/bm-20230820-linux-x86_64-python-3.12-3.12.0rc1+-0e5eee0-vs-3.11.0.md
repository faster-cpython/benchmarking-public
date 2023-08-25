
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: 0e5eee0
- commit date: 2023-08-20
- overall geometric mean: 1.02x faster
- HPT reliability: 89.85%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230820-linux-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 269 ms: 1.04x slower                                    |
| docutils       | 2.63 sec                                               | 2.73 sec: 1.04x slower                                  |
| tornado_http   | 96.3 ms                                                | 99.4 ms: 1.03x slower                                   |
| Geometric mean | (ref)                                                  | 1.04x slower                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230820-linux-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 88.0 ms: 1.06x faster                                   |
| pidigits       | 198 ms                                                 | 200 ms: 1.01x slower                                    |
| float          | 77.2 ms                                                | 80.8 ms: 1.05x slower                                   |
| Geometric mean | (ref)                                                  | 1.00x slower                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230820-linux-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.70 ms: 1.08x faster                                   |
| regex_v8       | 22.0 ms                                                | 22.8 ms: 1.04x slower                                   |
| regex_compile  | 138 ms                                                 | 146 ms: 1.06x slower                                    |
| Geometric mean | (ref)                                                  | 1.00x slower                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230820-linux-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.66 ms: 1.30x faster                                   |
| json_loads           | 26.5 us                                                | 25.2 us: 1.05x faster                                   |
| unpickle_pure_python | 228 us                                                 | 219 us: 1.04x faster                                    |
| pickle_dict          | 31.1 us                                                | 30.2 us: 1.03x faster                                   |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                    |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                    |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                   |
| pickle_pure_python   | 306 us                                                 | 312 us: 1.02x slower                                    |
| unpickle_list        | 4.91 us                                                | 5.05 us: 1.03x slower                                   |
| xml_etree_process    | 53.9 ms                                                | 59.2 ms: 1.10x slower                                   |
| unpickle             | 13.7 us                                                | 15.2 us: 1.11x slower                                   |
| xml_etree_generate   | 76.2 ms                                                | 85.1 ms: 1.12x slower                                   |
| pickle_list          | 4.11 us                                                | 4.62 us: 1.12x slower                                   |
| Geometric mean       | (ref)                                                  | 1.00x slower                                            |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230820-linux-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.31 ms: 1.09x slower                                   |
| python_startup_no_site | 6.01 ms                                                | 6.77 ms: 1.13x slower                                   |
| Geometric mean         | (ref)                                                  | 1.11x slower                                            |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230820-linux-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.8 ms: 1.08x slower                                   |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230820-linux-x86_64-python-3.12-3.12.0rc1+-0e5eee0 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 145 us: 3.35x faster                                    |
| generators               | 73.5 ms                                                | 30.2 ms: 2.43x faster                                   |
| asyncio_tcp              | 922 ms                                                 | 516 ms: 1.79x faster                                    |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.80 sec: 1.75x faster                                  |
| json_dumps               | 12.6 ms                                                | 9.66 ms: 1.30x faster                                   |
| mypy2                    | 420 ms                                                 | 344 ms: 1.22x faster                                    |
| coroutines               | 25.5 ms                                                | 22.3 ms: 1.14x faster                                   |
| richards_super           | 56.8 ms                                                | 50.8 ms: 1.12x faster                                   |
| async_tree_none          | 526 ms                                                 | 472 ms: 1.12x faster                                    |
| async_tree_io            | 1.30 sec                                               | 1.17 sec: 1.11x faster                                  |
| async_tree_memoization   | 627 ms                                                 | 574 ms: 1.09x faster                                    |
| comprehensions           | 22.4 us                                                | 20.7 us: 1.08x faster                                   |
| regex_effbot             | 3.99 ms                                                | 3.70 ms: 1.08x faster                                   |
| chaos                    | 69.2 ms                                                | 64.3 ms: 1.08x faster                                   |
| nbody                    | 93.1 ms                                                | 88.0 ms: 1.06x faster                                   |
| coverage                 | 100 ms                                                 | 94.9 ms: 1.05x faster                                   |
| json_loads               | 26.5 us                                                | 25.2 us: 1.05x faster                                   |
| sqlglot_parse            | 1.40 ms                                                | 1.33 ms: 1.05x faster                                   |
| unpickle_pure_python     | 228 us                                                 | 219 us: 1.04x faster                                    |
| richards                 | 45.7 ms                                                | 44.1 ms: 1.04x faster                                   |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 713 ms: 1.04x faster                                    |
| pickle_dict              | 31.1 us                                                | 30.2 us: 1.03x faster                                   |
| deltablue                | 3.67 ms                                                | 3.56 ms: 1.03x faster                                   |
| xml_etree_parse          | 158 ms                                                 | 154 ms: 1.03x faster                                    |
| json                     | 4.94 ms                                                | 4.81 ms: 1.03x faster                                   |
| go                       | 140 ms                                                 | 136 ms: 1.03x faster                                    |
| sqlglot_transpile        | 1.70 ms                                                | 1.66 ms: 1.03x faster                                   |
| nqueens                  | 83.4 ms                                                | 81.3 ms: 1.02x faster                                   |
| pycparser                | 1.18 sec                                               | 1.16 sec: 1.02x faster                                  |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.02x faster                                    |
| hexiom                   | 6.37 ms                                                | 6.28 ms: 1.01x faster                                   |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                    |
| scimark_lu               | 110 ms                                                 | 111 ms: 1.01x slower                                    |
| pidigits                 | 198 ms                                                 | 200 ms: 1.01x slower                                    |
| deepcopy_memo            | 37.0 us                                                | 37.5 us: 1.01x slower                                   |
| create_gc_cycles         | 1.49 ms                                                | 1.51 ms: 1.02x slower                                   |
| mdp                      | 2.62 sec                                               | 2.66 sec: 1.02x slower                                  |
| bench_thread_pool        | 819 us                                                 | 832 us: 1.02x slower                                    |
| sqlglot_optimize         | 53.1 ms                                                | 54.0 ms: 1.02x slower                                   |
| pickle                   | 10.1 us                                                | 10.3 us: 1.02x slower                                   |
| fannkuch                 | 388 ms                                                 | 395 ms: 1.02x slower                                    |
| pickle_pure_python       | 306 us                                                 | 312 us: 1.02x slower                                    |
| raytrace                 | 297 ms                                                 | 302 ms: 1.02x slower                                    |
| sqlglot_normalize        | 108 ms                                                 | 110 ms: 1.02x slower                                    |
| sqlalchemy_imperative    | 17.9 ms                                                | 18.3 ms: 1.02x slower                                   |
| unpickle_list            | 4.91 us                                                | 5.05 us: 1.03x slower                                   |
| pprint_pformat           | 1.46 sec                                               | 1.50 sec: 1.03x slower                                  |
| tornado_http             | 96.3 ms                                                | 99.4 ms: 1.03x slower                                   |
| logging_silent           | 101 ns                                                 | 104 ns: 1.03x slower                                    |
| deepcopy                 | 342 us                                                 | 354 us: 1.03x slower                                    |
| regex_v8                 | 22.0 ms                                                | 22.8 ms: 1.04x slower                                   |
| 2to3                     | 259 ms                                                 | 269 ms: 1.04x slower                                    |
| logging_simple           | 6.03 us                                                | 6.26 us: 1.04x slower                                   |
| docutils                 | 2.63 sec                                               | 2.73 sec: 1.04x slower                                  |
| telco                    | 6.58 ms                                                | 6.84 ms: 1.04x slower                                   |
| logging_format           | 6.68 us                                                | 6.96 us: 1.04x slower                                   |
| sqlalchemy_declarative   | 138 ms                                                 | 145 ms: 1.05x slower                                    |
| float                    | 77.2 ms                                                | 80.8 ms: 1.05x slower                                   |
| crypto_pyaes             | 74.7 ms                                                | 78.5 ms: 1.05x slower                                   |
| pprint_safe_repr         | 701 ms                                                 | 738 ms: 1.05x slower                                    |
| deepcopy_reduce          | 2.94 us                                                | 3.09 us: 1.05x slower                                   |
| scimark_monte_carlo      | 68.1 ms                                                | 71.8 ms: 1.05x slower                                   |
| regex_compile            | 138 ms                                                 | 146 ms: 1.06x slower                                    |
| scimark_sor              | 118 ms                                                 | 126 ms: 1.06x slower                                    |
| spectral_norm            | 100 ms                                                 | 107 ms: 1.07x slower                                    |
| dulwich_log              | 63.7 ms                                                | 68.3 ms: 1.07x slower                                   |
| mako                     | 10.1 ms                                                | 10.8 ms: 1.08x slower                                   |
| pyflate                  | 418 ms                                                 | 450 ms: 1.08x slower                                    |
| sqlite_synth             | 2.52 us                                                | 2.73 us: 1.08x slower                                   |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.90 ms: 1.09x slower                                   |
| scimark_fft              | 328 ms                                                 | 358 ms: 1.09x slower                                    |
| python_startup           | 8.52 ms                                                | 9.31 ms: 1.09x slower                                   |
| xml_etree_process        | 53.9 ms                                                | 59.2 ms: 1.10x slower                                   |
| gc_traversal             | 4.02 ms                                                | 4.46 ms: 1.11x slower                                   |
| unpickle                 | 13.7 us                                                | 15.2 us: 1.11x slower                                   |
| xml_etree_generate       | 76.2 ms                                                | 85.1 ms: 1.12x slower                                   |
| pickle_list              | 4.11 us                                                | 4.62 us: 1.12x slower                                   |
| python_startup_no_site   | 6.01 ms                                                | 6.77 ms: 1.13x slower                                   |
| async_generators         | 368 ms                                                 | 452 ms: 1.23x slower                                    |
| unpack_sequence          | 43.1 ns                                                | 53.7 ns: 1.25x slower                                   |
| dask                     | 360 ms                                                 | 538 ms: 1.49x slower                                    |
| Geometric mean           | (ref)                                                  | 1.02x faster                                            |

Benchmark hidden because not significant (4): regex_dna, tomli_loads, pathlib, bench_mp_pool
Ignored benchmarks (15) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 89.85% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
