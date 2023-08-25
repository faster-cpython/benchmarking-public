
# Results vs. 3.11.0

- fork: brandtbucher
- ref: un_materialize_alt
- machine: linux-x86_64
- commit hash: b2495de
- commit date: 2023-08-05
- overall geometric mean: 1.04x faster
- HPT reliability: 82.42%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.65 sec: 1.01x slower                                                    |
| tornado_http   | 96.3 ms                                                | 95.0 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.00x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                      |
| nbody          | 93.1 ms                                                | 89.2 ms: 1.04x faster                                                     |
| float          | 77.2 ms                                                | 80.2 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.53 ms: 1.13x faster                                                     |
| regex_compile  | 138 ms                                                 | 136 ms: 1.01x faster                                                      |
| regex_dna      | 204 ms                                                 | 203 ms: 1.00x faster                                                      |
| regex_v8       | 22.0 ms                                                | 22.5 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.78 ms: 1.29x faster                                                     |
| unpickle_pure_python | 228 us                                                 | 215 us: 1.06x faster                                                      |
| json_loads           | 26.5 us                                                | 25.6 us: 1.03x faster                                                     |
| pickle_pure_python   | 306 us                                                 | 296 us: 1.03x faster                                                      |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                      |
| pickle_dict          | 31.1 us                                                | 31.6 us: 1.01x slower                                                     |
| tomli_loads          | 2.22 sec                                               | 2.31 sec: 1.04x slower                                                    |
| pickle               | 10.1 us                                                | 10.8 us: 1.07x slower                                                     |
| xml_etree_process    | 53.9 ms                                                | 58.0 ms: 1.08x slower                                                     |
| xml_etree_generate   | 76.2 ms                                                | 83.4 ms: 1.09x slower                                                     |
| unpickle             | 13.7 us                                                | 15.3 us: 1.12x slower                                                     |
| pickle_list          | 4.11 us                                                | 4.66 us: 1.13x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.43 ms: 1.11x slower                                                     |
| python_startup_no_site | 6.01 ms                                                | 6.89 ms: 1.15x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.7 ms: 1.07x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 143 us: 3.40x faster                                                      |
| generators               | 73.5 ms                                                | 28.1 ms: 2.62x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 485 ms: 1.90x faster                                                      |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                    |
| json_dumps               | 12.6 ms                                                | 9.78 ms: 1.29x faster                                                     |
| coroutines               | 25.5 ms                                                | 21.3 ms: 1.20x faster                                                     |
| chaos                    | 69.2 ms                                                | 59.3 ms: 1.17x faster                                                     |
| deltablue                | 3.67 ms                                                | 3.23 ms: 1.14x faster                                                     |
| regex_effbot             | 3.99 ms                                                | 3.53 ms: 1.13x faster                                                     |
| comprehensions           | 22.4 us                                                | 20.2 us: 1.11x faster                                                     |
| async_tree_none          | 526 ms                                                 | 483 ms: 1.09x faster                                                      |
| sqlglot_parse            | 1.40 ms                                                | 1.29 ms: 1.08x faster                                                     |
| async_tree_io            | 1.30 sec                                               | 1.20 sec: 1.08x faster                                                    |
| raytrace                 | 297 ms                                                 | 275 ms: 1.08x faster                                                      |
| coverage                 | 100 ms                                                 | 93.3 ms: 1.07x faster                                                     |
| async_tree_memoization   | 627 ms                                                 | 585 ms: 1.07x faster                                                      |
| crypto_pyaes             | 74.7 ms                                                | 69.9 ms: 1.07x faster                                                     |
| unpickle_pure_python     | 228 us                                                 | 215 us: 1.06x faster                                                      |
| sqlglot_transpile        | 1.70 ms                                                | 1.61 ms: 1.06x faster                                                     |
| hexiom                   | 6.37 ms                                                | 6.03 ms: 1.06x faster                                                     |
| nqueens                  | 83.4 ms                                                | 79.2 ms: 1.05x faster                                                     |
| richards_super           | 56.8 ms                                                | 53.9 ms: 1.05x faster                                                     |
| pidigits                 | 198 ms                                                 | 189 ms: 1.05x faster                                                      |
| nbody                    | 93.1 ms                                                | 89.2 ms: 1.04x faster                                                     |
| logging_format           | 6.68 us                                                | 6.44 us: 1.04x faster                                                     |
| sqlglot_normalize        | 108 ms                                                 | 104 ms: 1.04x faster                                                      |
| json_loads               | 26.5 us                                                | 25.6 us: 1.03x faster                                                     |
| pickle_pure_python       | 306 us                                                 | 296 us: 1.03x faster                                                      |
| xml_etree_parse          | 158 ms                                                 | 154 ms: 1.03x faster                                                      |
| pycparser                | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                    |
| logging_simple           | 6.03 us                                                | 5.86 us: 1.03x faster                                                     |
| mdp                      | 2.62 sec                                               | 2.54 sec: 1.03x faster                                                    |
| json                     | 4.94 ms                                                | 4.83 ms: 1.02x faster                                                     |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 723 ms: 1.02x faster                                                      |
| tornado_http             | 96.3 ms                                                | 95.0 ms: 1.01x faster                                                     |
| regex_compile            | 138 ms                                                 | 136 ms: 1.01x faster                                                      |
| go                       | 140 ms                                                 | 138 ms: 1.01x faster                                                      |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                                      |
| sqlglot_optimize         | 53.1 ms                                                | 52.6 ms: 1.01x faster                                                     |
| fannkuch                 | 388 ms                                                 | 386 ms: 1.00x faster                                                      |
| regex_dna                | 204 ms                                                 | 203 ms: 1.00x faster                                                      |
| bench_thread_pool        | 819 us                                                 | 820 us: 1.00x slower                                                      |
| scimark_monte_carlo      | 68.1 ms                                                | 68.5 ms: 1.01x slower                                                     |
| pprint_pformat           | 1.46 sec                                               | 1.47 sec: 1.01x slower                                                    |
| docutils                 | 2.63 sec                                               | 2.65 sec: 1.01x slower                                                    |
| pickle_dict              | 31.1 us                                                | 31.6 us: 1.01x slower                                                     |
| deepcopy_memo            | 37.0 us                                                | 37.6 us: 1.02x slower                                                     |
| scimark_lu               | 110 ms                                                 | 112 ms: 1.02x slower                                                      |
| scimark_sor              | 118 ms                                                 | 120 ms: 1.02x slower                                                      |
| pprint_safe_repr         | 701 ms                                                 | 715 ms: 1.02x slower                                                      |
| create_gc_cycles         | 1.49 ms                                                | 1.52 ms: 1.02x slower                                                     |
| regex_v8                 | 22.0 ms                                                | 22.5 ms: 1.02x slower                                                     |
| pathlib                  | 18.2 ms                                                | 18.8 ms: 1.03x slower                                                     |
| float                    | 77.2 ms                                                | 80.2 ms: 1.04x slower                                                     |
| dulwich_log              | 63.7 ms                                                | 66.2 ms: 1.04x slower                                                     |
| tomli_loads              | 2.22 sec                                               | 2.31 sec: 1.04x slower                                                    |
| deepcopy                 | 342 us                                                 | 358 us: 1.05x slower                                                      |
| richards                 | 45.7 ms                                                | 48.2 ms: 1.05x slower                                                     |
| pyflate                  | 418 ms                                                 | 443 ms: 1.06x slower                                                      |
| spectral_norm            | 100 ms                                                 | 106 ms: 1.06x slower                                                      |
| mako                     | 10.1 ms                                                | 10.7 ms: 1.07x slower                                                     |
| pickle                   | 10.1 us                                                | 10.8 us: 1.07x slower                                                     |
| sqlite_synth             | 2.52 us                                                | 2.71 us: 1.08x slower                                                     |
| xml_etree_process        | 53.9 ms                                                | 58.0 ms: 1.08x slower                                                     |
| gc_traversal             | 4.02 ms                                                | 4.34 ms: 1.08x slower                                                     |
| scimark_fft              | 328 ms                                                 | 356 ms: 1.08x slower                                                      |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.91 ms: 1.09x slower                                                     |
| deepcopy_reduce          | 2.94 us                                                | 3.21 us: 1.09x slower                                                     |
| xml_etree_generate       | 76.2 ms                                                | 83.4 ms: 1.09x slower                                                     |
| unpack_sequence          | 43.1 ns                                                | 47.6 ns: 1.10x slower                                                     |
| python_startup           | 8.52 ms                                                | 9.43 ms: 1.11x slower                                                     |
| unpickle                 | 13.7 us                                                | 15.3 us: 1.12x slower                                                     |
| pickle_list              | 4.11 us                                                | 4.66 us: 1.13x slower                                                     |
| python_startup_no_site   | 6.01 ms                                                | 6.89 ms: 1.15x slower                                                     |
| telco                    | 6.58 ms                                                | 7.97 ms: 1.21x slower                                                     |
| async_generators         | 368 ms                                                 | 447 ms: 1.21x slower                                                      |
| dask                     | 360 ms                                                 | 516 ms: 1.43x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (5): meteor_contest, logging_silent, bench_mp_pool, unpickle_list, mypy2
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 82.42% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
