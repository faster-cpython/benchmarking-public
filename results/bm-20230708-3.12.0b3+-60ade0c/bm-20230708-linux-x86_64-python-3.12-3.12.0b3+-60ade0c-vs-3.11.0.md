
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: 60ade0c
- commit date: 2023-07-08
- overall geometric mean: 1.03x faster
- HPT reliability: 62.63%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-linux-x86_64-python-3.12-3.12.0b3+-60ade0c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 267 ms: 1.03x slower                                   |
| docutils       | 2.63 sec                                               | 2.71 sec: 1.03x slower                                 |
| tornado_http   | 96.3 ms                                                | 99.3 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-linux-x86_64-python-3.12-3.12.0b3+-60ade0c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 88.9 ms: 1.05x faster                                  |
| pidigits       | 198 ms                                                 | 196 ms: 1.01x faster                                   |
| float          | 77.2 ms                                                | 80.3 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-linux-x86_64-python-3.12-3.12.0b3+-60ade0c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.66 ms: 1.09x faster                                  |
| regex_dna      | 204 ms                                                 | 202 ms: 1.01x faster                                   |
| regex_v8       | 22.0 ms                                                | 22.8 ms: 1.04x slower                                  |
| regex_compile  | 138 ms                                                 | 145 ms: 1.05x slower                                   |
| Geometric mean | (ref)                                                  | 1.00x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-linux-x86_64-python-3.12-3.12.0b3+-60ade0c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.69 ms: 1.30x faster                                  |
| unpickle_pure_python | 228 us                                                 | 217 us: 1.05x faster                                   |
| json_loads           | 26.5 us                                                | 25.6 us: 1.03x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.03x faster                                   |
| pickle_dict          | 31.1 us                                                | 30.5 us: 1.02x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| pickle_pure_python   | 306 us                                                 | 310 us: 1.02x slower                                   |
| unpickle_list        | 4.91 us                                                | 5.05 us: 1.03x slower                                  |
| pickle               | 10.1 us                                                | 10.6 us: 1.05x slower                                  |
| xml_etree_process    | 53.9 ms                                                | 59.2 ms: 1.10x slower                                  |
| pickle_list          | 4.11 us                                                | 4.57 us: 1.11x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 84.9 ms: 1.11x slower                                  |
| unpickle             | 13.7 us                                                | 15.2 us: 1.11x slower                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-linux-x86_64-python-3.12-3.12.0b3+-60ade0c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.30 ms: 1.09x slower                                  |
| python_startup_no_site | 6.01 ms                                                | 6.76 ms: 1.12x slower                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-linux-x86_64-python-3.12-3.12.0b3+-60ade0c |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.8 ms: 1.07x slower                                  |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-linux-x86_64-python-3.12-3.12.0b3+-60ade0c |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 150 us: 3.25x faster                                   |
| generators               | 73.5 ms                                                | 30.7 ms: 2.39x faster                                  |
| asyncio_tcp              | 922 ms                                                 | 513 ms: 1.80x faster                                   |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.80 sec: 1.74x faster                                 |
| json_dumps               | 12.6 ms                                                | 9.69 ms: 1.30x faster                                  |
| mypy2                    | 420 ms                                                 | 344 ms: 1.22x faster                                   |
| richards_super           | 56.8 ms                                                | 49.8 ms: 1.14x faster                                  |
| coroutines               | 25.5 ms                                                | 22.7 ms: 1.13x faster                                  |
| async_tree_io            | 1.30 sec                                               | 1.16 sec: 1.12x faster                                 |
| async_tree_none          | 526 ms                                                 | 472 ms: 1.11x faster                                   |
| async_tree_memoization   | 627 ms                                                 | 574 ms: 1.09x faster                                   |
| chaos                    | 69.2 ms                                                | 63.4 ms: 1.09x faster                                  |
| regex_effbot             | 3.99 ms                                                | 3.66 ms: 1.09x faster                                  |
| comprehensions           | 22.4 us                                                | 20.8 us: 1.08x faster                                  |
| sqlglot_parse            | 1.40 ms                                                | 1.33 ms: 1.06x faster                                  |
| coverage                 | 100 ms                                                 | 95.2 ms: 1.05x faster                                  |
| deltablue                | 3.67 ms                                                | 3.50 ms: 1.05x faster                                  |
| unpickle_pure_python     | 228 us                                                 | 217 us: 1.05x faster                                   |
| nbody                    | 93.1 ms                                                | 88.9 ms: 1.05x faster                                  |
| gc_traversal             | 4.02 ms                                                | 3.86 ms: 1.04x faster                                  |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 713 ms: 1.04x faster                                   |
| json_loads               | 26.5 us                                                | 25.6 us: 1.03x faster                                  |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.03x faster                                   |
| sqlglot_transpile        | 1.70 ms                                                | 1.65 ms: 1.03x faster                                  |
| go                       | 140 ms                                                 | 136 ms: 1.03x faster                                   |
| mdp                      | 2.62 sec                                               | 2.55 sec: 1.03x faster                                 |
| richards                 | 45.7 ms                                                | 44.6 ms: 1.03x faster                                  |
| pycparser                | 1.18 sec                                               | 1.15 sec: 1.02x faster                                 |
| hexiom                   | 6.37 ms                                                | 6.23 ms: 1.02x faster                                  |
| pickle_dict              | 31.1 us                                                | 30.5 us: 1.02x faster                                  |
| nqueens                  | 83.4 ms                                                | 82.3 ms: 1.01x faster                                  |
| json                     | 4.94 ms                                                | 4.89 ms: 1.01x faster                                  |
| regex_dna                | 204 ms                                                 | 202 ms: 1.01x faster                                   |
| pidigits                 | 198 ms                                                 | 196 ms: 1.01x faster                                   |
| fannkuch                 | 388 ms                                                 | 385 ms: 1.01x faster                                   |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| sqlglot_normalize        | 108 ms                                                 | 108 ms: 1.00x slower                                   |
| sqlglot_optimize         | 53.1 ms                                                | 53.6 ms: 1.01x slower                                  |
| scimark_lu               | 110 ms                                                 | 111 ms: 1.01x slower                                   |
| create_gc_cycles         | 1.49 ms                                                | 1.51 ms: 1.02x slower                                  |
| pickle_pure_python       | 306 us                                                 | 310 us: 1.02x slower                                   |
| deepcopy_memo            | 37.0 us                                                | 37.6 us: 1.02x slower                                  |
| bench_thread_pool        | 819 us                                                 | 833 us: 1.02x slower                                   |
| logging_simple           | 6.03 us                                                | 6.17 us: 1.02x slower                                  |
| scimark_sor              | 118 ms                                                 | 121 ms: 1.02x slower                                   |
| unpickle_list            | 4.91 us                                                | 5.05 us: 1.03x slower                                  |
| docutils                 | 2.63 sec                                               | 2.71 sec: 1.03x slower                                 |
| tornado_http             | 96.3 ms                                                | 99.3 ms: 1.03x slower                                  |
| telco                    | 6.58 ms                                                | 6.80 ms: 1.03x slower                                  |
| deepcopy                 | 342 us                                                 | 353 us: 1.03x slower                                   |
| 2to3                     | 259 ms                                                 | 267 ms: 1.03x slower                                   |
| pprint_pformat           | 1.46 sec                                               | 1.51 sec: 1.03x slower                                 |
| logging_silent           | 101 ns                                                 | 105 ns: 1.03x slower                                   |
| logging_format           | 6.68 us                                                | 6.92 us: 1.04x slower                                  |
| regex_v8                 | 22.0 ms                                                | 22.8 ms: 1.04x slower                                  |
| scimark_monte_carlo      | 68.1 ms                                                | 70.6 ms: 1.04x slower                                  |
| sqlalchemy_imperative    | 17.9 ms                                                | 18.6 ms: 1.04x slower                                  |
| float                    | 77.2 ms                                                | 80.3 ms: 1.04x slower                                  |
| sqlalchemy_declarative   | 138 ms                                                 | 144 ms: 1.04x slower                                   |
| crypto_pyaes             | 74.7 ms                                                | 78.0 ms: 1.04x slower                                  |
| regex_compile            | 138 ms                                                 | 145 ms: 1.05x slower                                   |
| spectral_norm            | 100 ms                                                 | 105 ms: 1.05x slower                                   |
| pprint_safe_repr         | 701 ms                                                 | 740 ms: 1.05x slower                                   |
| pickle                   | 10.1 us                                                | 10.6 us: 1.05x slower                                  |
| pyflate                  | 418 ms                                                 | 442 ms: 1.06x slower                                   |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.78 ms: 1.06x slower                                  |
| mako                     | 10.1 ms                                                | 10.8 ms: 1.07x slower                                  |
| scimark_fft              | 328 ms                                                 | 352 ms: 1.07x slower                                   |
| deepcopy_reduce          | 2.94 us                                                | 3.16 us: 1.07x slower                                  |
| dulwich_log              | 63.7 ms                                                | 68.4 ms: 1.07x slower                                  |
| sqlite_synth             | 2.52 us                                                | 2.74 us: 1.09x slower                                  |
| python_startup           | 8.52 ms                                                | 9.30 ms: 1.09x slower                                  |
| xml_etree_process        | 53.9 ms                                                | 59.2 ms: 1.10x slower                                  |
| pickle_list              | 4.11 us                                                | 4.57 us: 1.11x slower                                  |
| xml_etree_generate       | 76.2 ms                                                | 84.9 ms: 1.11x slower                                  |
| unpickle                 | 13.7 us                                                | 15.2 us: 1.11x slower                                  |
| python_startup_no_site   | 6.01 ms                                                | 6.76 ms: 1.12x slower                                  |
| unpack_sequence          | 43.1 ns                                                | 51.9 ns: 1.20x slower                                  |
| async_generators         | 368 ms                                                 | 445 ms: 1.21x slower                                   |
| dask                     | 360 ms                                                 | 535 ms: 1.49x slower                                   |
| Geometric mean           | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (5): meteor_contest, pathlib, tomli_loads, bench_mp_pool, raytrace
Ignored benchmarks (15) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 62.63% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
