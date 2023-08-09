
# Results vs. 3.11.0

- fork: brandtbucher
- ref: un_materialize_alt
- machine: linux-x86_64
- commit hash: d42d2e6
- commit date: 2023-08-05
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.64 sec: 1.00x slower                                                    |
| tornado_http   | 96.3 ms                                                | 95.0 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.00x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 87.6 ms: 1.06x faster                                                     |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                      |
| float          | 77.2 ms                                                | 79.8 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.43 ms: 1.16x faster                                                     |
| regex_compile  | 138 ms                                                 | 136 ms: 1.02x faster                                                      |
| regex_v8       | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.77 ms: 1.29x faster                                                     |
| unpickle_pure_python | 228 us                                                 | 213 us: 1.07x faster                                                      |
| json_loads           | 26.5 us                                                | 25.3 us: 1.04x faster                                                     |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                                      |
| pickle_pure_python   | 306 us                                                 | 298 us: 1.03x faster                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.01x faster                                                      |
| pickle_dict          | 31.1 us                                                | 31.5 us: 1.01x slower                                                     |
| unpickle_list        | 4.91 us                                                | 5.04 us: 1.03x slower                                                     |
| pickle               | 10.1 us                                                | 10.4 us: 1.03x slower                                                     |
| tomli_loads          | 2.22 sec                                               | 2.31 sec: 1.04x slower                                                    |
| xml_etree_process    | 53.9 ms                                                | 57.3 ms: 1.06x slower                                                     |
| xml_etree_generate   | 76.2 ms                                                | 82.9 ms: 1.09x slower                                                     |
| pickle_list          | 4.11 us                                                | 4.59 us: 1.12x slower                                                     |
| unpickle             | 13.7 us                                                | 15.5 us: 1.13x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.37 ms: 1.10x slower                                                     |
| python_startup_no_site | 6.01 ms                                                | 6.85 ms: 1.14x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 145 us: 3.34x faster                                                      |
| generators               | 73.5 ms                                                | 28.5 ms: 2.58x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 484 ms: 1.90x faster                                                      |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                    |
| json_dumps               | 12.6 ms                                                | 9.77 ms: 1.29x faster                                                     |
| coroutines               | 25.5 ms                                                | 21.9 ms: 1.16x faster                                                     |
| regex_effbot             | 3.99 ms                                                | 3.43 ms: 1.16x faster                                                     |
| chaos                    | 69.2 ms                                                | 59.7 ms: 1.16x faster                                                     |
| deltablue                | 3.67 ms                                                | 3.23 ms: 1.14x faster                                                     |
| async_tree_none          | 526 ms                                                 | 476 ms: 1.11x faster                                                      |
| async_tree_io            | 1.30 sec                                               | 1.18 sec: 1.10x faster                                                    |
| comprehensions           | 22.4 us                                                | 20.5 us: 1.09x faster                                                     |
| async_tree_memoization   | 627 ms                                                 | 574 ms: 1.09x faster                                                      |
| raytrace                 | 297 ms                                                 | 273 ms: 1.09x faster                                                      |
| sqlglot_parse            | 1.40 ms                                                | 1.29 ms: 1.08x faster                                                     |
| unpickle_pure_python     | 228 us                                                 | 213 us: 1.07x faster                                                      |
| crypto_pyaes             | 74.7 ms                                                | 69.7 ms: 1.07x faster                                                     |
| coverage                 | 100 ms                                                 | 93.5 ms: 1.07x faster                                                     |
| nbody                    | 93.1 ms                                                | 87.6 ms: 1.06x faster                                                     |
| sqlglot_transpile        | 1.70 ms                                                | 1.61 ms: 1.06x faster                                                     |
| richards_super           | 56.8 ms                                                | 53.7 ms: 1.06x faster                                                     |
| hexiom                   | 6.37 ms                                                | 6.03 ms: 1.06x faster                                                     |
| pidigits                 | 198 ms                                                 | 189 ms: 1.05x faster                                                      |
| gc_traversal             | 4.02 ms                                                | 3.84 ms: 1.05x faster                                                     |
| json_loads               | 26.5 us                                                | 25.3 us: 1.04x faster                                                     |
| nqueens                  | 83.4 ms                                                | 79.9 ms: 1.04x faster                                                     |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 714 ms: 1.04x faster                                                      |
| logging_format           | 6.68 us                                                | 6.48 us: 1.03x faster                                                     |
| xml_etree_parse          | 158 ms                                                 | 154 ms: 1.03x faster                                                      |
| sqlglot_normalize        | 108 ms                                                 | 105 ms: 1.03x faster                                                      |
| pickle_pure_python       | 306 us                                                 | 298 us: 1.03x faster                                                      |
| logging_simple           | 6.03 us                                                | 5.88 us: 1.03x faster                                                     |
| pycparser                | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                    |
| json                     | 4.94 ms                                                | 4.83 ms: 1.02x faster                                                     |
| regex_compile            | 138 ms                                                 | 136 ms: 1.02x faster                                                      |
| xml_etree_iterparse      | 104 ms                                                 | 102 ms: 1.01x faster                                                      |
| go                       | 140 ms                                                 | 138 ms: 1.01x faster                                                      |
| tornado_http             | 96.3 ms                                                | 95.0 ms: 1.01x faster                                                     |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.01x faster                                                      |
| regex_v8                 | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                     |
| sqlglot_optimize         | 53.1 ms                                                | 52.9 ms: 1.00x faster                                                     |
| create_gc_cycles         | 1.49 ms                                                | 1.48 ms: 1.00x faster                                                     |
| pathlib                  | 18.2 ms                                                | 18.3 ms: 1.00x slower                                                     |
| docutils                 | 2.63 sec                                               | 2.64 sec: 1.00x slower                                                    |
| bench_thread_pool        | 819 us                                                 | 826 us: 1.01x slower                                                      |
| fannkuch                 | 388 ms                                                 | 392 ms: 1.01x slower                                                      |
| logging_silent           | 101 ns                                                 | 102 ns: 1.01x slower                                                      |
| pickle_dict              | 31.1 us                                                | 31.5 us: 1.01x slower                                                     |
| pprint_pformat           | 1.46 sec                                               | 1.48 sec: 1.02x slower                                                    |
| scimark_lu               | 110 ms                                                 | 112 ms: 1.02x slower                                                      |
| unpickle_list            | 4.91 us                                                | 5.04 us: 1.03x slower                                                     |
| pprint_safe_repr         | 701 ms                                                 | 720 ms: 1.03x slower                                                      |
| dulwich_log              | 63.7 ms                                                | 65.6 ms: 1.03x slower                                                     |
| pickle                   | 10.1 us                                                | 10.4 us: 1.03x slower                                                     |
| spectral_norm            | 100 ms                                                 | 103 ms: 1.03x slower                                                      |
| deepcopy_memo            | 37.0 us                                                | 38.2 us: 1.03x slower                                                     |
| float                    | 77.2 ms                                                | 79.8 ms: 1.03x slower                                                     |
| deepcopy                 | 342 us                                                 | 355 us: 1.04x slower                                                      |
| tomli_loads              | 2.22 sec                                               | 2.31 sec: 1.04x slower                                                    |
| richards                 | 45.7 ms                                                | 47.6 ms: 1.04x slower                                                     |
| mdp                      | 2.62 sec                                               | 2.73 sec: 1.04x slower                                                    |
| mako                     | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                     |
| xml_etree_process        | 53.9 ms                                                | 57.3 ms: 1.06x slower                                                     |
| deepcopy_reduce          | 2.94 us                                                | 3.13 us: 1.06x slower                                                     |
| pyflate                  | 418 ms                                                 | 445 ms: 1.06x slower                                                      |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.80 ms: 1.07x slower                                                     |
| sqlite_synth             | 2.52 us                                                | 2.72 us: 1.08x slower                                                     |
| scimark_fft              | 328 ms                                                 | 356 ms: 1.08x slower                                                      |
| xml_etree_generate       | 76.2 ms                                                | 82.9 ms: 1.09x slower                                                     |
| python_startup           | 8.52 ms                                                | 9.37 ms: 1.10x slower                                                     |
| pickle_list              | 4.11 us                                                | 4.59 us: 1.12x slower                                                     |
| unpickle                 | 13.7 us                                                | 15.5 us: 1.13x slower                                                     |
| python_startup_no_site   | 6.01 ms                                                | 6.85 ms: 1.14x slower                                                     |
| telco                    | 6.58 ms                                                | 7.79 ms: 1.18x slower                                                     |
| async_generators         | 368 ms                                                 | 448 ms: 1.22x slower                                                      |
| dask                     | 360 ms                                                 | 515 ms: 1.43x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (6): bench_mp_pool, regex_dna, unpack_sequence, scimark_monte_carlo, scimark_sor, mypy2
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
