
# Results vs. 3.11.0

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: a8834d3
- commit date: 2023-08-12
- overall geometric mean: 1.08x faster
- HPT reliability: 95.87%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-a8834d3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.37 sec: 1.11x faster                                                    |
| tornado_http   | 96.3 ms                                                | 94.0 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-a8834d3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 70.9 ms: 1.09x faster                                                     |
| nbody          | 93.1 ms                                                | 88.3 ms: 1.06x faster                                                     |
| pidigits       | 198 ms                                                 | 201 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-a8834d3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.43 ms: 1.17x faster                                                     |
| regex_v8       | 22.0 ms                                                | 21.7 ms: 1.01x faster                                                     |
| regex_compile  | 138 ms                                                 | 136 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-a8834d3 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.76 ms: 1.29x faster                                                     |
| xml_etree_parse      | 158 ms                                                 | 139 ms: 1.14x faster                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 94.1 ms: 1.10x faster                                                     |
| unpickle_pure_python | 228 us                                                 | 212 us: 1.07x faster                                                      |
| json_loads           | 26.5 us                                                | 25.7 us: 1.03x faster                                                     |
| pickle_pure_python   | 306 us                                                 | 297 us: 1.03x faster                                                      |
| unpickle_list        | 4.91 us                                                | 4.97 us: 1.01x slower                                                     |
| pickle_dict          | 31.1 us                                                | 31.6 us: 1.01x slower                                                     |
| xml_etree_process    | 53.9 ms                                                | 56.0 ms: 1.04x slower                                                     |
| tomli_loads          | 2.22 sec                                               | 2.31 sec: 1.04x slower                                                    |
| xml_etree_generate   | 76.2 ms                                                | 80.5 ms: 1.06x slower                                                     |
| unpickle             | 13.7 us                                                | 14.7 us: 1.07x slower                                                     |
| pickle               | 10.1 us                                                | 10.8 us: 1.08x slower                                                     |
| pickle_list          | 4.11 us                                                | 4.52 us: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-a8834d3 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.27 ms: 1.09x slower                                                     |
| python_startup_no_site | 6.01 ms                                                | 6.80 ms: 1.13x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-a8834d3 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-a8834d3 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 146 us: 3.34x faster                                                      |
| generators               | 73.5 ms                                                | 28.2 ms: 2.61x faster                                                     |
| async_tree_io            | 1.30 sec                                               | 565 ms: 2.29x faster                                                      |
| async_tree_none          | 526 ms                                                 | 276 ms: 1.91x faster                                                      |
| asyncio_tcp              | 922 ms                                                 | 486 ms: 1.90x faster                                                      |
| async_tree_memoization   | 627 ms                                                 | 343 ms: 1.83x faster                                                      |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.78 sec: 1.76x faster                                                    |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 505 ms: 1.46x faster                                                      |
| json_dumps               | 12.6 ms                                                | 9.76 ms: 1.29x faster                                                     |
| mypy2                    | 420 ms                                                 | 338 ms: 1.24x faster                                                      |
| chaos                    | 69.2 ms                                                | 58.7 ms: 1.18x faster                                                     |
| deltablue                | 3.67 ms                                                | 3.13 ms: 1.17x faster                                                     |
| regex_effbot             | 3.99 ms                                                | 3.43 ms: 1.17x faster                                                     |
| coroutines               | 25.5 ms                                                | 22.2 ms: 1.15x faster                                                     |
| xml_etree_parse          | 158 ms                                                 | 139 ms: 1.14x faster                                                      |
| raytrace                 | 297 ms                                                 | 267 ms: 1.11x faster                                                      |
| docutils                 | 2.63 sec                                               | 2.37 sec: 1.11x faster                                                    |
| xml_etree_iterparse      | 104 ms                                                 | 94.1 ms: 1.10x faster                                                     |
| sqlglot_parse            | 1.40 ms                                                | 1.27 ms: 1.10x faster                                                     |
| comprehensions           | 22.4 us                                                | 20.4 us: 1.10x faster                                                     |
| gc_traversal             | 4.02 ms                                                | 3.68 ms: 1.09x faster                                                     |
| float                    | 77.2 ms                                                | 70.9 ms: 1.09x faster                                                     |
| crypto_pyaes             | 74.7 ms                                                | 69.3 ms: 1.08x faster                                                     |
| coverage                 | 100 ms                                                 | 92.9 ms: 1.08x faster                                                     |
| unpickle_pure_python     | 228 us                                                 | 212 us: 1.07x faster                                                      |
| sqlglot_transpile        | 1.70 ms                                                | 1.59 ms: 1.07x faster                                                     |
| richards_super           | 56.8 ms                                                | 53.2 ms: 1.07x faster                                                     |
| hexiom                   | 6.37 ms                                                | 6.02 ms: 1.06x faster                                                     |
| nbody                    | 93.1 ms                                                | 88.3 ms: 1.06x faster                                                     |
| pycparser                | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                    |
| create_gc_cycles         | 1.49 ms                                                | 1.42 ms: 1.04x faster                                                     |
| logging_format           | 6.68 us                                                | 6.44 us: 1.04x faster                                                     |
| sqlglot_normalize        | 108 ms                                                 | 104 ms: 1.03x faster                                                      |
| nqueens                  | 83.4 ms                                                | 80.7 ms: 1.03x faster                                                     |
| json_loads               | 26.5 us                                                | 25.7 us: 1.03x faster                                                     |
| pickle_pure_python       | 306 us                                                 | 297 us: 1.03x faster                                                      |
| logging_simple           | 6.03 us                                                | 5.88 us: 1.03x faster                                                     |
| scimark_monte_carlo      | 68.1 ms                                                | 66.4 ms: 1.02x faster                                                     |
| tornado_http             | 96.3 ms                                                | 94.0 ms: 1.02x faster                                                     |
| go                       | 140 ms                                                 | 137 ms: 1.02x faster                                                      |
| json                     | 4.94 ms                                                | 4.86 ms: 1.02x faster                                                     |
| regex_v8                 | 22.0 ms                                                | 21.7 ms: 1.01x faster                                                     |
| regex_compile            | 138 ms                                                 | 136 ms: 1.01x faster                                                      |
| sqlglot_optimize         | 53.1 ms                                                | 52.5 ms: 1.01x faster                                                     |
| pprint_pformat           | 1.46 sec                                               | 1.47 sec: 1.01x slower                                                    |
| bench_thread_pool        | 819 us                                                 | 826 us: 1.01x slower                                                      |
| pathlib                  | 18.2 ms                                                | 18.4 ms: 1.01x slower                                                     |
| deepcopy_memo            | 37.0 us                                                | 37.4 us: 1.01x slower                                                     |
| unpickle_list            | 4.91 us                                                | 4.97 us: 1.01x slower                                                     |
| pidigits                 | 198 ms                                                 | 201 ms: 1.01x slower                                                      |
| pickle_dict              | 31.1 us                                                | 31.6 us: 1.01x slower                                                     |
| scimark_lu               | 110 ms                                                 | 112 ms: 1.02x slower                                                      |
| pprint_safe_repr         | 701 ms                                                 | 722 ms: 1.03x slower                                                      |
| dulwich_log              | 63.7 ms                                                | 65.7 ms: 1.03x slower                                                     |
| richards                 | 45.7 ms                                                | 47.4 ms: 1.04x slower                                                     |
| mdp                      | 2.62 sec                                               | 2.72 sec: 1.04x slower                                                    |
| deepcopy                 | 342 us                                                 | 355 us: 1.04x slower                                                      |
| xml_etree_process        | 53.9 ms                                                | 56.0 ms: 1.04x slower                                                     |
| tomli_loads              | 2.22 sec                                               | 2.31 sec: 1.04x slower                                                    |
| xml_etree_generate       | 76.2 ms                                                | 80.5 ms: 1.06x slower                                                     |
| mako                     | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                     |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.79 ms: 1.07x slower                                                     |
| unpack_sequence          | 43.1 ns                                                | 46.1 ns: 1.07x slower                                                     |
| deepcopy_reduce          | 2.94 us                                                | 3.15 us: 1.07x slower                                                     |
| unpickle                 | 13.7 us                                                | 14.7 us: 1.07x slower                                                     |
| spectral_norm            | 100 ms                                                 | 107 ms: 1.07x slower                                                      |
| pickle                   | 10.1 us                                                | 10.8 us: 1.08x slower                                                     |
| pyflate                  | 418 ms                                                 | 453 ms: 1.08x slower                                                      |
| python_startup           | 8.52 ms                                                | 9.27 ms: 1.09x slower                                                     |
| scimark_fft              | 328 ms                                                 | 359 ms: 1.09x slower                                                      |
| pickle_list              | 4.11 us                                                | 4.52 us: 1.10x slower                                                     |
| sqlite_synth             | 2.52 us                                                | 2.80 us: 1.11x slower                                                     |
| python_startup_no_site   | 6.01 ms                                                | 6.80 ms: 1.13x slower                                                     |
| async_generators         | 368 ms                                                 | 426 ms: 1.15x slower                                                      |
| telco                    | 6.58 ms                                                | 7.94 ms: 1.21x slower                                                     |
| dask                     | 360 ms                                                 | 486 ms: 1.35x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.08x faster                                                              |

Benchmark hidden because not significant (6): meteor_contest, fannkuch, bench_mp_pool, logging_silent, regex_dna, scimark_sor
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 95.87% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
