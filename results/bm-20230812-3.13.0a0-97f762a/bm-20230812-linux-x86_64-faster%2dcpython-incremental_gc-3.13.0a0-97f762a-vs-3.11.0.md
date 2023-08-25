
# Results vs. 3.11.0

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: 97f762a
- commit date: 2023-08-12
- overall geometric mean: 1.07x faster
- HPT reliability: 76.67%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-97f762a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.44 sec: 1.08x faster                                                    |
| tornado_http   | 96.3 ms                                                | 92.7 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-97f762a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                      |
| nbody          | 93.1 ms                                                | 89.6 ms: 1.04x faster                                                     |
| float          | 77.2 ms                                                | 77.8 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-97f762a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.53 ms: 1.13x faster                                                     |
| regex_v8       | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                     |
| regex_compile  | 138 ms                                                 | 137 ms: 1.01x faster                                                      |
| regex_dna      | 204 ms                                                 | 207 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-97f762a |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.82 ms: 1.28x faster                                                     |
| unpickle_pure_python | 228 us                                                 | 214 us: 1.07x faster                                                      |
| pickle_pure_python   | 306 us                                                 | 294 us: 1.04x faster                                                      |
| json_loads           | 26.5 us                                                | 25.5 us: 1.04x faster                                                     |
| pickle_dict          | 31.1 us                                                | 31.1 us: 1.00x faster                                                     |
| unpickle_list        | 4.91 us                                                | 4.95 us: 1.01x slower                                                     |
| xml_etree_iterparse  | 104 ms                                                 | 105 ms: 1.01x slower                                                      |
| tomli_loads          | 2.22 sec                                               | 2.30 sec: 1.04x slower                                                    |
| xml_etree_parse      | 158 ms                                                 | 166 ms: 1.05x slower                                                      |
| pickle               | 10.1 us                                                | 10.6 us: 1.05x slower                                                     |
| xml_etree_process    | 53.9 ms                                                | 57.6 ms: 1.07x slower                                                     |
| unpickle             | 13.7 us                                                | 14.8 us: 1.08x slower                                                     |
| xml_etree_generate   | 76.2 ms                                                | 83.2 ms: 1.09x slower                                                     |
| pickle_list          | 4.11 us                                                | 4.62 us: 1.12x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-97f762a |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.27 ms: 1.09x slower                                                     |
| python_startup_no_site | 6.01 ms                                                | 6.75 ms: 1.12x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-97f762a |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-97f762a |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 147 us: 3.31x faster                                                      |
| generators               | 73.5 ms                                                | 30.9 ms: 2.37x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 486 ms: 1.90x faster                                                      |
| async_tree_io            | 1.30 sec                                               | 730 ms: 1.77x faster                                                      |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                    |
| async_tree_memoization   | 627 ms                                                 | 406 ms: 1.55x faster                                                      |
| async_tree_none          | 526 ms                                                 | 342 ms: 1.54x faster                                                      |
| json_dumps               | 12.6 ms                                                | 9.82 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 577 ms: 1.28x faster                                                      |
| chaos                    | 69.2 ms                                                | 58.7 ms: 1.18x faster                                                     |
| deltablue                | 3.67 ms                                                | 3.13 ms: 1.17x faster                                                     |
| mypy2                    | 420 ms                                                 | 359 ms: 1.17x faster                                                      |
| coroutines               | 25.5 ms                                                | 22.1 ms: 1.15x faster                                                     |
| regex_effbot             | 3.99 ms                                                | 3.53 ms: 1.13x faster                                                     |
| gc_traversal             | 4.02 ms                                                | 3.61 ms: 1.12x faster                                                     |
| comprehensions           | 22.4 us                                                | 20.2 us: 1.11x faster                                                     |
| crypto_pyaes             | 74.7 ms                                                | 68.3 ms: 1.09x faster                                                     |
| raytrace                 | 297 ms                                                 | 271 ms: 1.09x faster                                                      |
| sqlglot_parse            | 1.40 ms                                                | 1.28 ms: 1.09x faster                                                     |
| coverage                 | 100 ms                                                 | 92.8 ms: 1.08x faster                                                     |
| docutils                 | 2.63 sec                                               | 2.44 sec: 1.08x faster                                                    |
| richards_super           | 56.8 ms                                                | 52.8 ms: 1.07x faster                                                     |
| sqlglot_transpile        | 1.70 ms                                                | 1.59 ms: 1.07x faster                                                     |
| unpickle_pure_python     | 228 us                                                 | 214 us: 1.07x faster                                                      |
| hexiom                   | 6.37 ms                                                | 6.05 ms: 1.05x faster                                                     |
| pidigits                 | 198 ms                                                 | 189 ms: 1.05x faster                                                      |
| pickle_pure_python       | 306 us                                                 | 294 us: 1.04x faster                                                      |
| nbody                    | 93.1 ms                                                | 89.6 ms: 1.04x faster                                                     |
| tornado_http             | 96.3 ms                                                | 92.7 ms: 1.04x faster                                                     |
| json_loads               | 26.5 us                                                | 25.5 us: 1.04x faster                                                     |
| mdp                      | 2.62 sec                                               | 2.53 sec: 1.03x faster                                                    |
| logging_format           | 6.68 us                                                | 6.47 us: 1.03x faster                                                     |
| create_gc_cycles         | 1.49 ms                                                | 1.45 ms: 1.03x faster                                                     |
| nqueens                  | 83.4 ms                                                | 81.3 ms: 1.03x faster                                                     |
| logging_simple           | 6.03 us                                                | 5.91 us: 1.02x faster                                                     |
| sqlglot_normalize        | 108 ms                                                 | 106 ms: 1.02x faster                                                      |
| scimark_monte_carlo      | 68.1 ms                                                | 66.9 ms: 1.02x faster                                                     |
| json                     | 4.94 ms                                                | 4.87 ms: 1.01x faster                                                     |
| logging_silent           | 101 ns                                                 | 99.7 ns: 1.01x faster                                                     |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.01x faster                                                      |
| regex_v8                 | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                     |
| regex_compile            | 138 ms                                                 | 137 ms: 1.01x faster                                                      |
| unpack_sequence          | 43.1 ns                                                | 42.7 ns: 1.01x faster                                                     |
| go                       | 140 ms                                                 | 139 ms: 1.00x faster                                                      |
| pickle_dict              | 31.1 us                                                | 31.1 us: 1.00x faster                                                     |
| pprint_pformat           | 1.46 sec                                               | 1.47 sec: 1.01x slower                                                    |
| float                    | 77.2 ms                                                | 77.8 ms: 1.01x slower                                                     |
| unpickle_list            | 4.91 us                                                | 4.95 us: 1.01x slower                                                     |
| bench_thread_pool        | 819 us                                                 | 826 us: 1.01x slower                                                      |
| xml_etree_iterparse      | 104 ms                                                 | 105 ms: 1.01x slower                                                      |
| richards                 | 45.7 ms                                                | 46.2 ms: 1.01x slower                                                     |
| scimark_lu               | 110 ms                                                 | 111 ms: 1.01x slower                                                      |
| fannkuch                 | 388 ms                                                 | 392 ms: 1.01x slower                                                      |
| deepcopy_memo            | 37.0 us                                                | 37.5 us: 1.01x slower                                                     |
| regex_dna                | 204 ms                                                 | 207 ms: 1.02x slower                                                      |
| pprint_safe_repr         | 701 ms                                                 | 717 ms: 1.02x slower                                                      |
| pathlib                  | 18.2 ms                                                | 18.7 ms: 1.02x slower                                                     |
| deepcopy                 | 342 us                                                 | 354 us: 1.03x slower                                                      |
| tomli_loads              | 2.22 sec                                               | 2.30 sec: 1.04x slower                                                    |
| dulwich_log              | 63.7 ms                                                | 66.0 ms: 1.04x slower                                                     |
| xml_etree_parse          | 158 ms                                                 | 166 ms: 1.05x slower                                                      |
| pickle                   | 10.1 us                                                | 10.6 us: 1.05x slower                                                     |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.74 ms: 1.05x slower                                                     |
| pyflate                  | 418 ms                                                 | 441 ms: 1.05x slower                                                      |
| spectral_norm            | 100 ms                                                 | 106 ms: 1.06x slower                                                      |
| deepcopy_reduce          | 2.94 us                                                | 3.14 us: 1.07x slower                                                     |
| xml_etree_process        | 53.9 ms                                                | 57.6 ms: 1.07x slower                                                     |
| mako                     | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                     |
| scimark_fft              | 328 ms                                                 | 354 ms: 1.08x slower                                                      |
| unpickle                 | 13.7 us                                                | 14.8 us: 1.08x slower                                                     |
| python_startup           | 8.52 ms                                                | 9.27 ms: 1.09x slower                                                     |
| xml_etree_generate       | 76.2 ms                                                | 83.2 ms: 1.09x slower                                                     |
| sqlite_synth             | 2.52 us                                                | 2.78 us: 1.10x slower                                                     |
| python_startup_no_site   | 6.01 ms                                                | 6.75 ms: 1.12x slower                                                     |
| pickle_list              | 4.11 us                                                | 4.62 us: 1.12x slower                                                     |
| async_generators         | 368 ms                                                 | 434 ms: 1.18x slower                                                      |
| telco                    | 6.58 ms                                                | 7.98 ms: 1.21x slower                                                     |
| dask                     | 360 ms                                                 | 495 ms: 1.38x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.07x faster                                                              |

Benchmark hidden because not significant (4): bench_mp_pool, pycparser, scimark_sor, sqlglot_optimize
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 76.67% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
