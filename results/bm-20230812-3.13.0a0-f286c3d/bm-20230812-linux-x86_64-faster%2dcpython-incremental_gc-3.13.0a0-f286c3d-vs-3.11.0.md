
# Results vs. 3.11.0

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: f286c3d
- commit date: 2023-08-12
- overall geometric mean: 1.08x faster
- HPT reliability: 95.91%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-f286c3d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.37 sec: 1.11x faster                                                    |
| tornado_http   | 96.3 ms                                                | 93.4 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-f286c3d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 71.7 ms: 1.08x faster                                                     |
| nbody          | 93.1 ms                                                | 88.1 ms: 1.06x faster                                                     |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-f286c3d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.42 ms: 1.17x faster                                                     |
| regex_compile  | 138 ms                                                 | 136 ms: 1.02x faster                                                      |
| regex_v8       | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                     |
| regex_dna      | 204 ms                                                 | 210 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-f286c3d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.88 ms: 1.27x faster                                                     |
| xml_etree_parse      | 158 ms                                                 | 141 ms: 1.13x faster                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 94.2 ms: 1.10x faster                                                     |
| unpickle_pure_python | 228 us                                                 | 213 us: 1.07x faster                                                      |
| pickle_pure_python   | 306 us                                                 | 295 us: 1.04x faster                                                      |
| json_loads           | 26.5 us                                                | 25.7 us: 1.03x faster                                                     |
| pickle_dict          | 31.1 us                                                | 32.6 us: 1.05x slower                                                     |
| tomli_loads          | 2.22 sec                                               | 2.34 sec: 1.06x slower                                                    |
| xml_etree_process    | 53.9 ms                                                | 56.9 ms: 1.06x slower                                                     |
| pickle               | 10.1 us                                                | 10.7 us: 1.06x slower                                                     |
| xml_etree_generate   | 76.2 ms                                                | 81.3 ms: 1.07x slower                                                     |
| unpickle             | 13.7 us                                                | 15.4 us: 1.13x slower                                                     |
| pickle_list          | 4.11 us                                                | 4.64 us: 1.13x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-f286c3d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.27 ms: 1.09x slower                                                     |
| python_startup_no_site | 6.01 ms                                                | 6.79 ms: 1.13x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-f286c3d |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-f286c3d |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 147 us: 3.31x faster                                                      |
| generators               | 73.5 ms                                                | 28.5 ms: 2.58x faster                                                     |
| async_tree_io            | 1.30 sec                                               | 565 ms: 2.30x faster                                                      |
| async_tree_none          | 526 ms                                                 | 278 ms: 1.89x faster                                                      |
| asyncio_tcp              | 922 ms                                                 | 487 ms: 1.89x faster                                                      |
| async_tree_memoization   | 627 ms                                                 | 344 ms: 1.82x faster                                                      |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.78 sec: 1.76x faster                                                    |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 506 ms: 1.46x faster                                                      |
| json_dumps               | 12.6 ms                                                | 9.88 ms: 1.27x faster                                                     |
| mypy2                    | 420 ms                                                 | 339 ms: 1.24x faster                                                      |
| gc_traversal             | 4.02 ms                                                | 3.40 ms: 1.18x faster                                                     |
| regex_effbot             | 3.99 ms                                                | 3.42 ms: 1.17x faster                                                     |
| deltablue                | 3.67 ms                                                | 3.15 ms: 1.17x faster                                                     |
| chaos                    | 69.2 ms                                                | 59.5 ms: 1.16x faster                                                     |
| coroutines               | 25.5 ms                                                | 22.3 ms: 1.14x faster                                                     |
| xml_etree_parse          | 158 ms                                                 | 141 ms: 1.13x faster                                                      |
| docutils                 | 2.63 sec                                               | 2.37 sec: 1.11x faster                                                    |
| sqlglot_parse            | 1.40 ms                                                | 1.26 ms: 1.11x faster                                                     |
| comprehensions           | 22.4 us                                                | 20.3 us: 1.11x faster                                                     |
| xml_etree_iterparse      | 104 ms                                                 | 94.2 ms: 1.10x faster                                                     |
| raytrace                 | 297 ms                                                 | 270 ms: 1.10x faster                                                      |
| crypto_pyaes             | 74.7 ms                                                | 69.0 ms: 1.08x faster                                                     |
| sqlglot_transpile        | 1.70 ms                                                | 1.58 ms: 1.08x faster                                                     |
| float                    | 77.2 ms                                                | 71.7 ms: 1.08x faster                                                     |
| coverage                 | 100 ms                                                 | 93.0 ms: 1.08x faster                                                     |
| unpickle_pure_python     | 228 us                                                 | 213 us: 1.07x faster                                                      |
| richards_super           | 56.8 ms                                                | 53.6 ms: 1.06x faster                                                     |
| pycparser                | 1.18 sec                                               | 1.12 sec: 1.06x faster                                                    |
| nbody                    | 93.1 ms                                                | 88.1 ms: 1.06x faster                                                     |
| create_gc_cycles         | 1.49 ms                                                | 1.41 ms: 1.05x faster                                                     |
| hexiom                   | 6.37 ms                                                | 6.08 ms: 1.05x faster                                                     |
| pidigits                 | 198 ms                                                 | 189 ms: 1.05x faster                                                      |
| logging_format           | 6.68 us                                                | 6.44 us: 1.04x faster                                                     |
| pickle_pure_python       | 306 us                                                 | 295 us: 1.04x faster                                                      |
| mdp                      | 2.62 sec                                               | 2.53 sec: 1.03x faster                                                    |
| tornado_http             | 96.3 ms                                                | 93.4 ms: 1.03x faster                                                     |
| json_loads               | 26.5 us                                                | 25.7 us: 1.03x faster                                                     |
| go                       | 140 ms                                                 | 136 ms: 1.03x faster                                                      |
| logging_simple           | 6.03 us                                                | 5.88 us: 1.03x faster                                                     |
| json                     | 4.94 ms                                                | 4.84 ms: 1.02x faster                                                     |
| regex_compile            | 138 ms                                                 | 136 ms: 1.02x faster                                                      |
| sqlglot_normalize        | 108 ms                                                 | 106 ms: 1.02x faster                                                      |
| nqueens                  | 83.4 ms                                                | 81.9 ms: 1.02x faster                                                     |
| regex_v8                 | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                     |
| scimark_monte_carlo      | 68.1 ms                                                | 67.4 ms: 1.01x faster                                                     |
| sqlglot_optimize         | 53.1 ms                                                | 52.9 ms: 1.00x faster                                                     |
| bench_thread_pool        | 819 us                                                 | 826 us: 1.01x slower                                                      |
| pathlib                  | 18.2 ms                                                | 18.4 ms: 1.01x slower                                                     |
| fannkuch                 | 388 ms                                                 | 392 ms: 1.01x slower                                                      |
| deepcopy_memo            | 37.0 us                                                | 37.5 us: 1.01x slower                                                     |
| pprint_pformat           | 1.46 sec                                               | 1.48 sec: 1.01x slower                                                    |
| scimark_sor              | 118 ms                                                 | 120 ms: 1.02x slower                                                      |
| scimark_lu               | 110 ms                                                 | 113 ms: 1.03x slower                                                      |
| deepcopy                 | 342 us                                                 | 352 us: 1.03x slower                                                      |
| pprint_safe_repr         | 701 ms                                                 | 723 ms: 1.03x slower                                                      |
| spectral_norm            | 100 ms                                                 | 103 ms: 1.03x slower                                                      |
| regex_dna                | 204 ms                                                 | 210 ms: 1.03x slower                                                      |
| dulwich_log              | 63.7 ms                                                | 66.0 ms: 1.04x slower                                                     |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.68 ms: 1.04x slower                                                     |
| pickle_dict              | 31.1 us                                                | 32.6 us: 1.05x slower                                                     |
| unpack_sequence          | 43.1 ns                                                | 45.1 ns: 1.05x slower                                                     |
| richards                 | 45.7 ms                                                | 48.0 ms: 1.05x slower                                                     |
| tomli_loads              | 2.22 sec                                               | 2.34 sec: 1.06x slower                                                    |
| xml_etree_process        | 53.9 ms                                                | 56.9 ms: 1.06x slower                                                     |
| pickle                   | 10.1 us                                                | 10.7 us: 1.06x slower                                                     |
| mako                     | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                     |
| xml_etree_generate       | 76.2 ms                                                | 81.3 ms: 1.07x slower                                                     |
| scimark_fft              | 328 ms                                                 | 352 ms: 1.07x slower                                                      |
| deepcopy_reduce          | 2.94 us                                                | 3.16 us: 1.08x slower                                                     |
| pyflate                  | 418 ms                                                 | 451 ms: 1.08x slower                                                      |
| python_startup           | 8.52 ms                                                | 9.27 ms: 1.09x slower                                                     |
| sqlite_synth             | 2.52 us                                                | 2.79 us: 1.11x slower                                                     |
| unpickle                 | 13.7 us                                                | 15.4 us: 1.13x slower                                                     |
| pickle_list              | 4.11 us                                                | 4.64 us: 1.13x slower                                                     |
| python_startup_no_site   | 6.01 ms                                                | 6.79 ms: 1.13x slower                                                     |
| async_generators         | 368 ms                                                 | 425 ms: 1.15x slower                                                      |
| telco                    | 6.58 ms                                                | 7.90 ms: 1.20x slower                                                     |
| dask                     | 360 ms                                                 | 485 ms: 1.35x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.08x faster                                                              |

Benchmark hidden because not significant (4): meteor_contest, bench_mp_pool, unpickle_list, logging_silent
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 95.91% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
