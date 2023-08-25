
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 5113ed7
- commit date: 2023-07-29
- overall geometric mean: 1.04x faster
- HPT reliability: 70.81%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-python-main-3.13.0a0-5113ed7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.66 sec: 1.01x slower                                |
| tornado_http   | 96.3 ms                                                | 95.6 ms: 1.01x faster                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-python-main-3.13.0a0-5113ed7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 198 ms                                                 | 201 ms: 1.01x slower                                  |
| float          | 77.2 ms                                                | 80.4 ms: 1.04x slower                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-python-main-3.13.0a0-5113ed7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.49 ms: 1.14x faster                                 |
| regex_compile  | 138 ms                                                 | 139 ms: 1.00x slower                                  |
| regex_dna      | 204 ms                                                 | 208 ms: 1.02x slower                                  |
| regex_v8       | 22.0 ms                                                | 22.9 ms: 1.04x slower                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-python-main-3.13.0a0-5113ed7 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.75 ms: 1.29x faster                                 |
| unpickle_pure_python | 228 us                                                 | 216 us: 1.06x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.04x faster                                  |
| json_loads           | 26.5 us                                                | 25.7 us: 1.03x faster                                 |
| pickle_pure_python   | 306 us                                                 | 298 us: 1.03x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                  |
| pickle_dict          | 31.1 us                                                | 31.5 us: 1.01x slower                                 |
| unpickle_list        | 4.91 us                                                | 5.01 us: 1.02x slower                                 |
| pickle               | 10.1 us                                                | 10.6 us: 1.05x slower                                 |
| tomli_loads          | 2.22 sec                                               | 2.34 sec: 1.05x slower                                |
| xml_etree_process    | 53.9 ms                                                | 58.4 ms: 1.09x slower                                 |
| xml_etree_generate   | 76.2 ms                                                | 84.2 ms: 1.10x slower                                 |
| unpickle             | 13.7 us                                                | 15.4 us: 1.13x slower                                 |
| pickle_list          | 4.11 us                                                | 4.77 us: 1.16x slower                                 |
| Geometric mean       | (ref)                                                  | 1.01x slower                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-python-main-3.13.0a0-5113ed7 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.31 ms: 1.09x slower                                 |
| python_startup_no_site | 6.01 ms                                                | 6.80 ms: 1.13x slower                                 |
| Geometric mean         | (ref)                                                  | 1.11x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-python-main-3.13.0a0-5113ed7 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.8 ms: 1.07x slower                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-python-main-3.13.0a0-5113ed7 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 141 us: 3.45x faster                                  |
| generators               | 73.5 ms                                                | 28.5 ms: 2.58x faster                                 |
| asyncio_tcp              | 922 ms                                                 | 491 ms: 1.88x faster                                  |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.78 sec: 1.76x faster                                |
| json_dumps               | 12.6 ms                                                | 9.75 ms: 1.29x faster                                 |
| mypy2                    | 420 ms                                                 | 338 ms: 1.24x faster                                  |
| coroutines               | 25.5 ms                                                | 21.6 ms: 1.18x faster                                 |
| chaos                    | 69.2 ms                                                | 59.8 ms: 1.16x faster                                 |
| regex_effbot             | 3.99 ms                                                | 3.49 ms: 1.14x faster                                 |
| deltablue                | 3.67 ms                                                | 3.22 ms: 1.14x faster                                 |
| gc_traversal             | 4.02 ms                                                | 3.66 ms: 1.10x faster                                 |
| raytrace                 | 297 ms                                                 | 271 ms: 1.09x faster                                  |
| async_tree_none          | 526 ms                                                 | 482 ms: 1.09x faster                                  |
| async_tree_io            | 1.30 sec                                               | 1.19 sec: 1.09x faster                                |
| comprehensions           | 22.4 us                                                | 20.6 us: 1.09x faster                                 |
| sqlglot_parse            | 1.40 ms                                                | 1.30 ms: 1.08x faster                                 |
| coverage                 | 100 ms                                                 | 93.2 ms: 1.07x faster                                 |
| async_tree_memoization   | 627 ms                                                 | 587 ms: 1.07x faster                                  |
| richards_super           | 56.8 ms                                                | 53.2 ms: 1.07x faster                                 |
| unpickle_pure_python     | 228 us                                                 | 216 us: 1.06x faster                                  |
| sqlglot_transpile        | 1.70 ms                                                | 1.62 ms: 1.05x faster                                 |
| nqueens                  | 83.4 ms                                                | 79.8 ms: 1.04x faster                                 |
| xml_etree_parse          | 158 ms                                                 | 152 ms: 1.04x faster                                  |
| hexiom                   | 6.37 ms                                                | 6.12 ms: 1.04x faster                                 |
| crypto_pyaes             | 74.7 ms                                                | 71.8 ms: 1.04x faster                                 |
| json_loads               | 26.5 us                                                | 25.7 us: 1.03x faster                                 |
| pickle_pure_python       | 306 us                                                 | 298 us: 1.03x faster                                  |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 722 ms: 1.02x faster                                  |
| pycparser                | 1.18 sec                                               | 1.16 sec: 1.02x faster                                |
| logging_format           | 6.68 us                                                | 6.55 us: 1.02x faster                                 |
| logging_simple           | 6.03 us                                                | 5.92 us: 1.02x faster                                 |
| sqlglot_normalize        | 108 ms                                                 | 106 ms: 1.02x faster                                  |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.02x faster                                  |
| json                     | 4.94 ms                                                | 4.89 ms: 1.01x faster                                 |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                  |
| tornado_http             | 96.3 ms                                                | 95.6 ms: 1.01x faster                                 |
| create_gc_cycles         | 1.49 ms                                                | 1.48 ms: 1.00x faster                                 |
| regex_compile            | 138 ms                                                 | 139 ms: 1.00x slower                                  |
| scimark_monte_carlo      | 68.1 ms                                                | 68.4 ms: 1.01x slower                                 |
| docutils                 | 2.63 sec                                               | 2.66 sec: 1.01x slower                                |
| pickle_dict              | 31.1 us                                                | 31.5 us: 1.01x slower                                 |
| pathlib                  | 18.2 ms                                                | 18.5 ms: 1.01x slower                                 |
| pprint_pformat           | 1.46 sec                                               | 1.48 sec: 1.01x slower                                |
| pidigits                 | 198 ms                                                 | 201 ms: 1.01x slower                                  |
| richards                 | 45.7 ms                                                | 46.4 ms: 1.01x slower                                 |
| regex_dna                | 204 ms                                                 | 208 ms: 1.02x slower                                  |
| deepcopy_memo            | 37.0 us                                                | 37.8 us: 1.02x slower                                 |
| unpickle_list            | 4.91 us                                                | 5.01 us: 1.02x slower                                 |
| scimark_lu               | 110 ms                                                 | 112 ms: 1.02x slower                                  |
| pprint_safe_repr         | 701 ms                                                 | 722 ms: 1.03x slower                                  |
| unpack_sequence          | 43.1 ns                                                | 44.4 ns: 1.03x slower                                 |
| fannkuch                 | 388 ms                                                 | 402 ms: 1.04x slower                                  |
| logging_silent           | 101 ns                                                 | 105 ns: 1.04x slower                                  |
| scimark_sor              | 118 ms                                                 | 122 ms: 1.04x slower                                  |
| regex_v8                 | 22.0 ms                                                | 22.9 ms: 1.04x slower                                 |
| float                    | 77.2 ms                                                | 80.4 ms: 1.04x slower                                 |
| dulwich_log              | 63.7 ms                                                | 66.3 ms: 1.04x slower                                 |
| mdp                      | 2.62 sec                                               | 2.74 sec: 1.05x slower                                |
| pickle                   | 10.1 us                                                | 10.6 us: 1.05x slower                                 |
| tomli_loads              | 2.22 sec                                               | 2.34 sec: 1.05x slower                                |
| deepcopy                 | 342 us                                                 | 362 us: 1.06x slower                                  |
| mako                     | 10.1 ms                                                | 10.8 ms: 1.07x slower                                 |
| spectral_norm            | 100 ms                                                 | 107 ms: 1.07x slower                                  |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.83 ms: 1.07x slower                                 |
| sqlite_synth             | 2.52 us                                                | 2.73 us: 1.08x slower                                 |
| xml_etree_process        | 53.9 ms                                                | 58.4 ms: 1.09x slower                                 |
| python_startup           | 8.52 ms                                                | 9.31 ms: 1.09x slower                                 |
| pyflate                  | 418 ms                                                 | 457 ms: 1.09x slower                                  |
| xml_etree_generate       | 76.2 ms                                                | 84.2 ms: 1.10x slower                                 |
| deepcopy_reduce          | 2.94 us                                                | 3.26 us: 1.11x slower                                 |
| scimark_fft              | 328 ms                                                 | 366 ms: 1.12x slower                                  |
| unpickle                 | 13.7 us                                                | 15.4 us: 1.13x slower                                 |
| python_startup_no_site   | 6.01 ms                                                | 6.80 ms: 1.13x slower                                 |
| pickle_list              | 4.11 us                                                | 4.77 us: 1.16x slower                                 |
| telco                    | 6.58 ms                                                | 7.95 ms: 1.21x slower                                 |
| async_generators         | 368 ms                                                 | 449 ms: 1.22x slower                                  |
| dask                     | 360 ms                                                 | 521 ms: 1.45x slower                                  |
| Geometric mean           | (ref)                                                  | 1.04x faster                                          |

Benchmark hidden because not significant (5): go, sqlglot_optimize, bench_thread_pool, bench_mp_pool, nbody
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 70.81% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
