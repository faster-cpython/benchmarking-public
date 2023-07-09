
# Results vs. 3.11.0

- fork: brandtbucher
- ref: un_materialize_alt
- machine: linux-x86_64
- commit hash: d00eefe
- commit date: 2023-07-07
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.64 sec: 1.01x slower                                                    |
| Geometric mean | (ref)                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 89.4 ms: 1.04x faster                                                     |
| pidigits       | 198 ms                                                 | 197 ms: 1.01x faster                                                      |
| float          | 77.2 ms                                                | 79.3 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.51 ms: 1.14x faster                                                     |
| regex_compile  | 138 ms                                                 | 136 ms: 1.02x faster                                                      |
| regex_v8       | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                     |
| regex_dna      | 204 ms                                                 | 213 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.75 ms: 1.29x faster                                                     |
| unpickle_pure_python | 228 us                                                 | 213 us: 1.07x faster                                                      |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.04x faster                                                      |
| json_loads           | 26.5 us                                                | 25.7 us: 1.03x faster                                                     |
| pickle_dict          | 31.1 us                                                | 30.8 us: 1.01x faster                                                     |
| pickle_pure_python   | 306 us                                                 | 302 us: 1.01x faster                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                      |
| unpickle_list        | 4.91 us                                                | 5.00 us: 1.02x slower                                                     |
| tomli_loads          | 2.22 sec                                               | 2.30 sec: 1.04x slower                                                    |
| pickle               | 10.1 us                                                | 10.6 us: 1.06x slower                                                     |
| xml_etree_process    | 53.9 ms                                                | 57.5 ms: 1.07x slower                                                     |
| xml_etree_generate   | 76.2 ms                                                | 83.3 ms: 1.09x slower                                                     |
| unpickle             | 13.7 us                                                | 15.1 us: 1.11x slower                                                     |
| pickle_list          | 4.11 us                                                | 4.55 us: 1.11x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.26 ms: 1.09x slower                                                     |
| python_startup_no_site | 6.01 ms                                                | 6.73 ms: 1.12x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.5 ms: 1.04x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 144 us: 3.37x faster                                                      |
| generators               | 73.5 ms                                                | 28.6 ms: 2.57x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 508 ms: 1.81x faster                                                      |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                    |
| json_dumps               | 12.6 ms                                                | 9.75 ms: 1.29x faster                                                     |
| chaos                    | 69.2 ms                                                | 58.9 ms: 1.18x faster                                                     |
| regex_effbot             | 3.99 ms                                                | 3.51 ms: 1.14x faster                                                     |
| coroutines               | 25.5 ms                                                | 22.5 ms: 1.13x faster                                                     |
| gc_traversal             | 4.02 ms                                                | 3.56 ms: 1.13x faster                                                     |
| deltablue                | 3.67 ms                                                | 3.29 ms: 1.12x faster                                                     |
| raytrace                 | 297 ms                                                 | 271 ms: 1.09x faster                                                      |
| comprehensions           | 22.4 us                                                | 20.6 us: 1.09x faster                                                     |
| async_tree_none          | 526 ms                                                 | 484 ms: 1.09x faster                                                      |
| async_tree_io            | 1.30 sec                                               | 1.20 sec: 1.08x faster                                                    |
| richards_super           | 56.8 ms                                                | 52.5 ms: 1.08x faster                                                     |
| unpickle_pure_python     | 228 us                                                 | 213 us: 1.07x faster                                                      |
| async_tree_memoization   | 627 ms                                                 | 588 ms: 1.07x faster                                                      |
| sqlglot_parse            | 1.40 ms                                                | 1.33 ms: 1.06x faster                                                     |
| hexiom                   | 6.37 ms                                                | 6.06 ms: 1.05x faster                                                     |
| coverage                 | 100 ms                                                 | 95.6 ms: 1.05x faster                                                     |
| nbody                    | 93.1 ms                                                | 89.4 ms: 1.04x faster                                                     |
| xml_etree_parse          | 158 ms                                                 | 152 ms: 1.04x faster                                                      |
| sqlglot_transpile        | 1.70 ms                                                | 1.65 ms: 1.03x faster                                                     |
| json_loads               | 26.5 us                                                | 25.7 us: 1.03x faster                                                     |
| logging_format           | 6.68 us                                                | 6.50 us: 1.03x faster                                                     |
| meteor_contest           | 107 ms                                                 | 104 ms: 1.02x faster                                                      |
| logging_simple           | 6.03 us                                                | 5.90 us: 1.02x faster                                                     |
| nqueens                  | 83.4 ms                                                | 81.6 ms: 1.02x faster                                                     |
| sqlglot_normalize        | 108 ms                                                 | 106 ms: 1.02x faster                                                      |
| regex_compile            | 138 ms                                                 | 136 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 729 ms: 1.01x faster                                                      |
| pickle_dict              | 31.1 us                                                | 30.8 us: 1.01x faster                                                     |
| pickle_pure_python       | 306 us                                                 | 302 us: 1.01x faster                                                      |
| go                       | 140 ms                                                 | 139 ms: 1.01x faster                                                      |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                                      |
| pidigits                 | 198 ms                                                 | 197 ms: 1.01x faster                                                      |
| regex_v8                 | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                     |
| bench_thread_pool        | 819 us                                                 | 817 us: 1.00x faster                                                      |
| sqlglot_optimize         | 53.1 ms                                                | 53.3 ms: 1.00x slower                                                     |
| docutils                 | 2.63 sec                                               | 2.64 sec: 1.01x slower                                                    |
| fannkuch                 | 388 ms                                                 | 391 ms: 1.01x slower                                                      |
| deepcopy_memo            | 37.0 us                                                | 37.3 us: 1.01x slower                                                     |
| pycparser                | 1.18 sec                                               | 1.19 sec: 1.01x slower                                                    |
| create_gc_cycles         | 1.49 ms                                                | 1.50 ms: 1.01x slower                                                     |
| pprint_pformat           | 1.46 sec                                               | 1.48 sec: 1.02x slower                                                    |
| scimark_sor              | 118 ms                                                 | 120 ms: 1.02x slower                                                      |
| unpickle_list            | 4.91 us                                                | 5.00 us: 1.02x slower                                                     |
| deepcopy                 | 342 us                                                 | 351 us: 1.03x slower                                                      |
| pprint_safe_repr         | 701 ms                                                 | 720 ms: 1.03x slower                                                      |
| float                    | 77.2 ms                                                | 79.3 ms: 1.03x slower                                                     |
| richards                 | 45.7 ms                                                | 47.1 ms: 1.03x slower                                                     |
| logging_silent           | 101 ns                                                 | 104 ns: 1.03x slower                                                      |
| dulwich_log              | 63.7 ms                                                | 65.6 ms: 1.03x slower                                                     |
| mdp                      | 2.62 sec                                               | 2.70 sec: 1.03x slower                                                    |
| pathlib                  | 18.2 ms                                                | 18.9 ms: 1.04x slower                                                     |
| tomli_loads              | 2.22 sec                                               | 2.30 sec: 1.04x slower                                                    |
| mako                     | 10.1 ms                                                | 10.5 ms: 1.04x slower                                                     |
| crypto_pyaes             | 74.7 ms                                                | 77.9 ms: 1.04x slower                                                     |
| regex_dna                | 204 ms                                                 | 213 ms: 1.04x slower                                                      |
| spectral_norm            | 100 ms                                                 | 104 ms: 1.04x slower                                                      |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.70 ms: 1.04x slower                                                     |
| pickle                   | 10.1 us                                                | 10.6 us: 1.06x slower                                                     |
| scimark_monte_carlo      | 68.1 ms                                                | 72.1 ms: 1.06x slower                                                     |
| pyflate                  | 418 ms                                                 | 446 ms: 1.07x slower                                                      |
| scimark_fft              | 328 ms                                                 | 351 ms: 1.07x slower                                                      |
| xml_etree_process        | 53.9 ms                                                | 57.5 ms: 1.07x slower                                                     |
| telco                    | 6.58 ms                                                | 7.10 ms: 1.08x slower                                                     |
| python_startup           | 8.52 ms                                                | 9.26 ms: 1.09x slower                                                     |
| sqlite_synth             | 2.52 us                                                | 2.74 us: 1.09x slower                                                     |
| deepcopy_reduce          | 2.94 us                                                | 3.21 us: 1.09x slower                                                     |
| xml_etree_generate       | 76.2 ms                                                | 83.3 ms: 1.09x slower                                                     |
| unpickle                 | 13.7 us                                                | 15.1 us: 1.11x slower                                                     |
| pickle_list              | 4.11 us                                                | 4.55 us: 1.11x slower                                                     |
| python_startup_no_site   | 6.01 ms                                                | 6.73 ms: 1.12x slower                                                     |
| async_generators         | 368 ms                                                 | 447 ms: 1.21x slower                                                      |
| dask                     | 360 ms                                                 | 517 ms: 1.44x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (6): json, tornado_http, bench_mp_pool, unpack_sequence, scimark_lu, mypy2
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
