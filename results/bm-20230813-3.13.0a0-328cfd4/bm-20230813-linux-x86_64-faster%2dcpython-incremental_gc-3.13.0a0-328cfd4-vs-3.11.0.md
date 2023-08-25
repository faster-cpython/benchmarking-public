
# Results vs. 3.11.0

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: 328cfd4
- commit date: 2023-08-13
- overall geometric mean: 1.07x faster
- HPT reliability: 82.78%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-328cfd4 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.42 sec: 1.09x faster                                                    |
| tornado_http   | 96.3 ms                                                | 93.6 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-328cfd4 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 88.7 ms: 1.05x faster                                                     |
| float          | 77.2 ms                                                | 75.0 ms: 1.03x faster                                                     |
| pidigits       | 198 ms                                                 | 201 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-328cfd4 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.53 ms: 1.13x faster                                                     |
| regex_compile  | 138 ms                                                 | 137 ms: 1.01x faster                                                      |
| regex_dna      | 204 ms                                                 | 213 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-328cfd4 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.72 ms: 1.29x faster                                                     |
| unpickle_pure_python | 228 us                                                 | 213 us: 1.07x faster                                                      |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.04x faster                                                      |
| json_loads           | 26.5 us                                                | 25.6 us: 1.03x faster                                                     |
| xml_etree_iterparse  | 104 ms                                                 | 101 ms: 1.03x faster                                                      |
| pickle_pure_python   | 306 us                                                 | 299 us: 1.02x faster                                                      |
| pickle_dict          | 31.1 us                                                | 32.2 us: 1.03x slower                                                     |
| pickle               | 10.1 us                                                | 10.4 us: 1.04x slower                                                     |
| tomli_loads          | 2.22 sec                                               | 2.32 sec: 1.05x slower                                                    |
| unpickle_list        | 4.91 us                                                | 5.16 us: 1.05x slower                                                     |
| xml_etree_process    | 53.9 ms                                                | 58.0 ms: 1.08x slower                                                     |
| unpickle             | 13.7 us                                                | 15.0 us: 1.10x slower                                                     |
| xml_etree_generate   | 76.2 ms                                                | 84.1 ms: 1.10x slower                                                     |
| pickle_list          | 4.11 us                                                | 4.63 us: 1.13x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-328cfd4 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.27 ms: 1.09x slower                                                     |
| python_startup_no_site | 6.01 ms                                                | 6.74 ms: 1.12x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-328cfd4 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.8 ms: 1.08x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230813-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-328cfd4 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 145 us: 3.36x faster                                                      |
| generators               | 73.5 ms                                                | 28.4 ms: 2.59x faster                                                     |
| async_tree_io            | 1.30 sec                                               | 676 ms: 1.92x faster                                                      |
| asyncio_tcp              | 922 ms                                                 | 487 ms: 1.89x faster                                                      |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                    |
| async_tree_none          | 526 ms                                                 | 308 ms: 1.71x faster                                                      |
| async_tree_memoization   | 627 ms                                                 | 393 ms: 1.60x faster                                                      |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 560 ms: 1.32x faster                                                      |
| json_dumps               | 12.6 ms                                                | 9.72 ms: 1.29x faster                                                     |
| mypy2                    | 420 ms                                                 | 347 ms: 1.21x faster                                                      |
| chaos                    | 69.2 ms                                                | 59.6 ms: 1.16x faster                                                     |
| coroutines               | 25.5 ms                                                | 22.2 ms: 1.15x faster                                                     |
| deltablue                | 3.67 ms                                                | 3.20 ms: 1.15x faster                                                     |
| regex_effbot             | 3.99 ms                                                | 3.53 ms: 1.13x faster                                                     |
| comprehensions           | 22.4 us                                                | 20.6 us: 1.09x faster                                                     |
| raytrace                 | 297 ms                                                 | 272 ms: 1.09x faster                                                      |
| sqlglot_parse            | 1.40 ms                                                | 1.29 ms: 1.09x faster                                                     |
| docutils                 | 2.63 sec                                               | 2.42 sec: 1.09x faster                                                    |
| richards_super           | 56.8 ms                                                | 52.5 ms: 1.08x faster                                                     |
| coverage                 | 100 ms                                                 | 92.5 ms: 1.08x faster                                                     |
| unpickle_pure_python     | 228 us                                                 | 213 us: 1.07x faster                                                      |
| crypto_pyaes             | 74.7 ms                                                | 70.2 ms: 1.06x faster                                                     |
| gc_traversal             | 4.02 ms                                                | 3.79 ms: 1.06x faster                                                     |
| sqlglot_transpile        | 1.70 ms                                                | 1.61 ms: 1.06x faster                                                     |
| pycparser                | 1.18 sec                                               | 1.12 sec: 1.06x faster                                                    |
| nbody                    | 93.1 ms                                                | 88.7 ms: 1.05x faster                                                     |
| logging_format           | 6.68 us                                                | 6.41 us: 1.04x faster                                                     |
| xml_etree_parse          | 158 ms                                                 | 152 ms: 1.04x faster                                                      |
| logging_simple           | 6.03 us                                                | 5.84 us: 1.03x faster                                                     |
| json_loads               | 26.5 us                                                | 25.6 us: 1.03x faster                                                     |
| xml_etree_iterparse      | 104 ms                                                 | 101 ms: 1.03x faster                                                      |
| hexiom                   | 6.37 ms                                                | 6.18 ms: 1.03x faster                                                     |
| float                    | 77.2 ms                                                | 75.0 ms: 1.03x faster                                                     |
| tornado_http             | 96.3 ms                                                | 93.6 ms: 1.03x faster                                                     |
| create_gc_cycles         | 1.49 ms                                                | 1.45 ms: 1.02x faster                                                     |
| json                     | 4.94 ms                                                | 4.83 ms: 1.02x faster                                                     |
| pickle_pure_python       | 306 us                                                 | 299 us: 1.02x faster                                                      |
| mdp                      | 2.62 sec                                               | 2.56 sec: 1.02x faster                                                    |
| sqlglot_normalize        | 108 ms                                                 | 106 ms: 1.02x faster                                                      |
| logging_silent           | 101 ns                                                 | 99.7 ns: 1.01x faster                                                     |
| go                       | 140 ms                                                 | 138 ms: 1.01x faster                                                      |
| nqueens                  | 83.4 ms                                                | 82.7 ms: 1.01x faster                                                     |
| regex_compile            | 138 ms                                                 | 137 ms: 1.01x faster                                                      |
| sqlglot_optimize         | 53.1 ms                                                | 53.0 ms: 1.00x faster                                                     |
| pprint_pformat           | 1.46 sec                                               | 1.46 sec: 1.01x slower                                                    |
| pidigits                 | 198 ms                                                 | 201 ms: 1.01x slower                                                      |
| bench_thread_pool        | 819 us                                                 | 830 us: 1.01x slower                                                      |
| pathlib                  | 18.2 ms                                                | 18.6 ms: 1.02x slower                                                     |
| richards                 | 45.7 ms                                                | 46.6 ms: 1.02x slower                                                     |
| pprint_safe_repr         | 701 ms                                                 | 718 ms: 1.02x slower                                                      |
| fannkuch                 | 388 ms                                                 | 398 ms: 1.03x slower                                                      |
| deepcopy_memo            | 37.0 us                                                | 38.0 us: 1.03x slower                                                     |
| scimark_lu               | 110 ms                                                 | 113 ms: 1.03x slower                                                      |
| scimark_sor              | 118 ms                                                 | 122 ms: 1.03x slower                                                      |
| pickle_dict              | 31.1 us                                                | 32.2 us: 1.03x slower                                                     |
| pickle                   | 10.1 us                                                | 10.4 us: 1.04x slower                                                     |
| deepcopy                 | 342 us                                                 | 356 us: 1.04x slower                                                      |
| dulwich_log              | 63.7 ms                                                | 66.3 ms: 1.04x slower                                                     |
| regex_dna                | 204 ms                                                 | 213 ms: 1.04x slower                                                      |
| tomli_loads              | 2.22 sec                                               | 2.32 sec: 1.05x slower                                                    |
| unpickle_list            | 4.91 us                                                | 5.16 us: 1.05x slower                                                     |
| spectral_norm            | 100 ms                                                 | 105 ms: 1.05x slower                                                      |
| unpack_sequence          | 43.1 ns                                                | 45.7 ns: 1.06x slower                                                     |
| pyflate                  | 418 ms                                                 | 446 ms: 1.07x slower                                                      |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.80 ms: 1.07x slower                                                     |
| mako                     | 10.1 ms                                                | 10.8 ms: 1.08x slower                                                     |
| xml_etree_process        | 53.9 ms                                                | 58.0 ms: 1.08x slower                                                     |
| python_startup           | 8.52 ms                                                | 9.27 ms: 1.09x slower                                                     |
| sqlite_synth             | 2.52 us                                                | 2.76 us: 1.10x slower                                                     |
| unpickle                 | 13.7 us                                                | 15.0 us: 1.10x slower                                                     |
| deepcopy_reduce          | 2.94 us                                                | 3.23 us: 1.10x slower                                                     |
| xml_etree_generate       | 76.2 ms                                                | 84.1 ms: 1.10x slower                                                     |
| scimark_fft              | 328 ms                                                 | 364 ms: 1.11x slower                                                      |
| python_startup_no_site   | 6.01 ms                                                | 6.74 ms: 1.12x slower                                                     |
| pickle_list              | 4.11 us                                                | 4.63 us: 1.13x slower                                                     |
| async_generators         | 368 ms                                                 | 430 ms: 1.17x slower                                                      |
| telco                    | 6.58 ms                                                | 8.16 ms: 1.24x slower                                                     |
| dask                     | 360 ms                                                 | 492 ms: 1.37x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.07x faster                                                              |

Benchmark hidden because not significant (4): meteor_contest, bench_mp_pool, scimark_monte_carlo, regex_v8
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 82.78% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
