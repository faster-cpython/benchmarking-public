
# Results vs. 3.11.0

- fork: brandtbucher
- ref: tracing
- machine: linux-x86_64
- commit hash: 930262f
- commit date: 2023-08-05
- overall geometric mean: 1.01x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.79 sec: 1.06x slower                                         |
| tornado_http   | 96.3 ms                                                | 98.2 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                  | 1.04x slower                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 201 ms: 1.01x slower                                           |
| float          | 77.2 ms                                                | 85.2 ms: 1.10x slower                                          |
| nbody          | 93.1 ms                                                | 112 ms: 1.20x slower                                           |
| Geometric mean | (ref)                                                  | 1.10x slower                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.54 ms: 1.13x faster                                          |
| regex_v8       | 22.0 ms                                                | 21.6 ms: 1.02x faster                                          |
| regex_dna      | 204 ms                                                 | 208 ms: 1.02x slower                                           |
| regex_compile  | 138 ms                                                 | 156 ms: 1.13x slower                                           |
| Geometric mean | (ref)                                                  | 1.00x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 10.1 ms: 1.25x faster                                          |
| json_loads           | 26.5 us                                                | 25.4 us: 1.04x faster                                          |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.04x faster                                           |
| unpickle_pure_python | 228 us                                                 | 225 us: 1.02x faster                                           |
| pickle_pure_python   | 306 us                                                 | 303 us: 1.01x faster                                           |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                           |
| pickle_dict          | 31.1 us                                                | 32.8 us: 1.05x slower                                          |
| pickle               | 10.1 us                                                | 10.8 us: 1.07x slower                                          |
| unpickle_list        | 4.91 us                                                | 5.30 us: 1.08x slower                                          |
| unpickle             | 13.7 us                                                | 15.0 us: 1.10x slower                                          |
| xml_etree_process    | 53.9 ms                                                | 59.7 ms: 1.11x slower                                          |
| pickle_list          | 4.11 us                                                | 4.64 us: 1.13x slower                                          |
| xml_etree_generate   | 76.2 ms                                                | 86.1 ms: 1.13x slower                                          |
| tomli_loads          | 2.22 sec                                               | 2.66 sec: 1.20x slower                                         |
| Geometric mean       | (ref)                                                  | 1.04x slower                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.34 ms: 1.10x slower                                          |
| python_startup_no_site | 6.01 ms                                                | 6.83 ms: 1.14x slower                                          |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f |
|-----------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 12.4 ms: 1.23x slower                                          |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 154 us: 3.15x faster                                           |
| generators               | 73.5 ms                                                | 28.9 ms: 2.54x faster                                          |
| asyncio_tcp              | 922 ms                                                 | 492 ms: 1.87x faster                                           |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.81 sec: 1.74x faster                                         |
| json_dumps               | 12.6 ms                                                | 10.1 ms: 1.25x faster                                          |
| coroutines               | 25.5 ms                                                | 21.5 ms: 1.19x faster                                          |
| mypy2                    | 420 ms                                                 | 354 ms: 1.19x faster                                           |
| regex_effbot             | 3.99 ms                                                | 3.54 ms: 1.13x faster                                          |
| async_tree_io            | 1.30 sec                                               | 1.20 sec: 1.08x faster                                         |
| async_tree_none          | 526 ms                                                 | 493 ms: 1.07x faster                                           |
| coverage                 | 100 ms                                                 | 94.5 ms: 1.06x faster                                          |
| deltablue                | 3.67 ms                                                | 3.47 ms: 1.06x faster                                          |
| sqlglot_parse            | 1.40 ms                                                | 1.34 ms: 1.05x faster                                          |
| json_loads               | 26.5 us                                                | 25.4 us: 1.04x faster                                          |
| async_tree_memoization   | 627 ms                                                 | 602 ms: 1.04x faster                                           |
| xml_etree_parse          | 158 ms                                                 | 152 ms: 1.04x faster                                           |
| json                     | 4.94 ms                                                | 4.80 ms: 1.03x faster                                          |
| raytrace                 | 297 ms                                                 | 288 ms: 1.03x faster                                           |
| sqlglot_transpile        | 1.70 ms                                                | 1.66 ms: 1.03x faster                                          |
| regex_v8                 | 22.0 ms                                                | 21.6 ms: 1.02x faster                                          |
| richards_super           | 56.8 ms                                                | 55.7 ms: 1.02x faster                                          |
| unpickle_pure_python     | 228 us                                                 | 225 us: 1.02x faster                                           |
| pickle_pure_python       | 306 us                                                 | 303 us: 1.01x faster                                           |
| gc_traversal             | 4.02 ms                                                | 4.06 ms: 1.01x slower                                          |
| pycparser                | 1.18 sec                                               | 1.20 sec: 1.01x slower                                         |
| pidigits                 | 198 ms                                                 | 201 ms: 1.01x slower                                           |
| sqlglot_normalize        | 108 ms                                                 | 110 ms: 1.02x slower                                           |
| tornado_http             | 96.3 ms                                                | 98.2 ms: 1.02x slower                                          |
| regex_dna                | 204 ms                                                 | 208 ms: 1.02x slower                                           |
| xml_etree_iterparse      | 104 ms                                                 | 106 ms: 1.02x slower                                           |
| scimark_monte_carlo      | 68.1 ms                                                | 69.5 ms: 1.02x slower                                          |
| logging_simple           | 6.03 us                                                | 6.18 us: 1.02x slower                                          |
| chaos                    | 69.2 ms                                                | 71.2 ms: 1.03x slower                                          |
| crypto_pyaes             | 74.7 ms                                                | 77.0 ms: 1.03x slower                                          |
| logging_format           | 6.68 us                                                | 6.89 us: 1.03x slower                                          |
| pathlib                  | 18.2 ms                                                | 18.9 ms: 1.04x slower                                          |
| mdp                      | 2.62 sec                                               | 2.71 sec: 1.04x slower                                         |
| sqlglot_optimize         | 53.1 ms                                                | 55.4 ms: 1.04x slower                                          |
| logging_silent           | 101 ns                                                 | 106 ns: 1.05x slower                                           |
| pickle_dict              | 31.1 us                                                | 32.8 us: 1.05x slower                                          |
| bench_thread_pool        | 819 us                                                 | 866 us: 1.06x slower                                           |
| docutils                 | 2.63 sec                                               | 2.79 sec: 1.06x slower                                         |
| scimark_sor              | 118 ms                                                 | 126 ms: 1.06x slower                                           |
| go                       | 140 ms                                                 | 149 ms: 1.07x slower                                           |
| pickle                   | 10.1 us                                                | 10.8 us: 1.07x slower                                          |
| unpack_sequence          | 43.1 ns                                                | 46.1 ns: 1.07x slower                                          |
| deepcopy                 | 342 us                                                 | 367 us: 1.07x slower                                           |
| richards                 | 45.7 ms                                                | 49.1 ms: 1.07x slower                                          |
| unpickle_list            | 4.91 us                                                | 5.30 us: 1.08x slower                                          |
| dulwich_log              | 63.7 ms                                                | 69.0 ms: 1.08x slower                                          |
| pprint_pformat           | 1.46 sec                                               | 1.58 sec: 1.09x slower                                         |
| scimark_lu               | 110 ms                                                 | 119 ms: 1.09x slower                                           |
| deepcopy_reduce          | 2.94 us                                                | 3.21 us: 1.09x slower                                          |
| unpickle                 | 13.7 us                                                | 15.0 us: 1.10x slower                                          |
| python_startup           | 8.52 ms                                                | 9.34 ms: 1.10x slower                                          |
| pprint_safe_repr         | 701 ms                                                 | 771 ms: 1.10x slower                                           |
| float                    | 77.2 ms                                                | 85.2 ms: 1.10x slower                                          |
| sqlite_synth             | 2.52 us                                                | 2.79 us: 1.11x slower                                          |
| xml_etree_process        | 53.9 ms                                                | 59.7 ms: 1.11x slower                                          |
| spectral_norm            | 100 ms                                                 | 111 ms: 1.11x slower                                           |
| comprehensions           | 22.4 us                                                | 25.3 us: 1.13x slower                                          |
| pickle_list              | 4.11 us                                                | 4.64 us: 1.13x slower                                          |
| meteor_contest           | 107 ms                                                 | 120 ms: 1.13x slower                                           |
| xml_etree_generate       | 76.2 ms                                                | 86.1 ms: 1.13x slower                                          |
| regex_compile            | 138 ms                                                 | 156 ms: 1.13x slower                                           |
| python_startup_no_site   | 6.01 ms                                                | 6.83 ms: 1.14x slower                                          |
| deepcopy_memo            | 37.0 us                                                | 42.9 us: 1.16x slower                                          |
| telco                    | 6.58 ms                                                | 7.80 ms: 1.18x slower                                          |
| tomli_loads              | 2.22 sec                                               | 2.66 sec: 1.20x slower                                         |
| nbody                    | 93.1 ms                                                | 112 ms: 1.20x slower                                           |
| nqueens                  | 83.4 ms                                                | 101 ms: 1.21x slower                                           |
| scimark_fft              | 328 ms                                                 | 404 ms: 1.23x slower                                           |
| mako                     | 10.1 ms                                                | 12.4 ms: 1.23x slower                                          |
| hexiom                   | 6.37 ms                                                | 7.93 ms: 1.24x slower                                          |
| fannkuch                 | 388 ms                                                 | 490 ms: 1.26x slower                                           |
| async_generators         | 368 ms                                                 | 466 ms: 1.26x slower                                           |
| pyflate                  | 418 ms                                                 | 533 ms: 1.28x slower                                           |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 5.79 ms: 1.29x slower                                          |
| dask                     | 360 ms                                                 | 538 ms: 1.49x slower                                           |
| Geometric mean           | (ref)                                                  | 1.01x slower                                                   |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, create_gc_cycles, bench_mp_pool
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x
