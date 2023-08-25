
# Results vs. 3.11.0

- fork: python
- ref: 14fbd4e6b16dcbcbff44
- machine: linux-x86_64
- commit hash: 14fbd4e
- commit date: 2023-08-03
- overall geometric mean: 1.04x faster
- HPT reliability: 59.77%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.65 sec: 1.01x slower                                                |
| tornado_http   | 96.3 ms                                                | 95.3 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 92.4 ms: 1.01x faster                                                 |
| pidigits       | 198 ms                                                 | 201 ms: 1.02x slower                                                  |
| float          | 77.2 ms                                                | 80.5 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.51 ms: 1.14x faster                                                 |
| regex_compile  | 138 ms                                                 | 137 ms: 1.01x faster                                                  |
| regex_v8       | 22.0 ms                                                | 22.4 ms: 1.01x slower                                                 |
| regex_dna      | 204 ms                                                 | 211 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.87 ms: 1.28x faster                                                 |
| unpickle_pure_python | 228 us                                                 | 212 us: 1.07x faster                                                  |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.04x faster                                                  |
| pickle_pure_python   | 306 us                                                 | 294 us: 1.04x faster                                                  |
| json_loads           | 26.5 us                                                | 26.1 us: 1.02x faster                                                 |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                  |
| unpickle_list        | 4.91 us                                                | 4.99 us: 1.02x slower                                                 |
| pickle_dict          | 31.1 us                                                | 31.6 us: 1.02x slower                                                 |
| pickle               | 10.1 us                                                | 10.4 us: 1.03x slower                                                 |
| tomli_loads          | 2.22 sec                                               | 2.33 sec: 1.05x slower                                                |
| xml_etree_process    | 53.9 ms                                                | 57.7 ms: 1.07x slower                                                 |
| xml_etree_generate   | 76.2 ms                                                | 83.3 ms: 1.09x slower                                                 |
| unpickle             | 13.7 us                                                | 15.0 us: 1.10x slower                                                 |
| pickle_list          | 4.11 us                                                | 4.57 us: 1.11x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.33 ms: 1.09x slower                                                 |
| python_startup_no_site | 6.01 ms                                                | 6.83 ms: 1.14x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230803-linux-x86_64-python-14fbd4e6b16dcbcbff44-3.13.0a0-14fbd4e |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 144 us: 3.38x faster                                                  |
| generators               | 73.5 ms                                                | 28.2 ms: 2.61x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 484 ms: 1.90x faster                                                  |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                |
| json_dumps               | 12.6 ms                                                | 9.87 ms: 1.28x faster                                                 |
| mypy2                    | 420 ms                                                 | 336 ms: 1.25x faster                                                  |
| coroutines               | 25.5 ms                                                | 21.7 ms: 1.18x faster                                                 |
| chaos                    | 69.2 ms                                                | 59.2 ms: 1.17x faster                                                 |
| regex_effbot             | 3.99 ms                                                | 3.51 ms: 1.14x faster                                                 |
| deltablue                | 3.67 ms                                                | 3.28 ms: 1.12x faster                                                 |
| comprehensions           | 22.4 us                                                | 20.3 us: 1.11x faster                                                 |
| gc_traversal             | 4.02 ms                                                | 3.66 ms: 1.10x faster                                                 |
| async_tree_none          | 526 ms                                                 | 480 ms: 1.10x faster                                                  |
| async_tree_io            | 1.30 sec                                               | 1.19 sec: 1.09x faster                                                |
| raytrace                 | 297 ms                                                 | 272 ms: 1.09x faster                                                  |
| sqlglot_parse            | 1.40 ms                                                | 1.29 ms: 1.09x faster                                                 |
| crypto_pyaes             | 74.7 ms                                                | 68.7 ms: 1.09x faster                                                 |
| coverage                 | 100 ms                                                 | 92.9 ms: 1.08x faster                                                 |
| unpickle_pure_python     | 228 us                                                 | 212 us: 1.07x faster                                                  |
| async_tree_memoization   | 627 ms                                                 | 584 ms: 1.07x faster                                                  |
| sqlglot_transpile        | 1.70 ms                                                | 1.60 ms: 1.06x faster                                                 |
| hexiom                   | 6.37 ms                                                | 6.01 ms: 1.06x faster                                                 |
| richards_super           | 56.8 ms                                                | 54.1 ms: 1.05x faster                                                 |
| nqueens                  | 83.4 ms                                                | 79.5 ms: 1.05x faster                                                 |
| xml_etree_parse          | 158 ms                                                 | 152 ms: 1.04x faster                                                  |
| pickle_pure_python       | 306 us                                                 | 294 us: 1.04x faster                                                  |
| sqlglot_normalize        | 108 ms                                                 | 104 ms: 1.03x faster                                                  |
| logging_format           | 6.68 us                                                | 6.48 us: 1.03x faster                                                 |
| pycparser                | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 719 ms: 1.03x faster                                                  |
| go                       | 140 ms                                                 | 137 ms: 1.03x faster                                                  |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.02x faster                                                  |
| json_loads               | 26.5 us                                                | 26.1 us: 1.02x faster                                                 |
| logging_simple           | 6.03 us                                                | 5.96 us: 1.01x faster                                                 |
| sqlglot_optimize         | 53.1 ms                                                | 52.6 ms: 1.01x faster                                                 |
| tornado_http             | 96.3 ms                                                | 95.3 ms: 1.01x faster                                                 |
| regex_compile            | 138 ms                                                 | 137 ms: 1.01x faster                                                  |
| json                     | 4.94 ms                                                | 4.90 ms: 1.01x faster                                                 |
| nbody                    | 93.1 ms                                                | 92.4 ms: 1.01x faster                                                 |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                                  |
| create_gc_cycles         | 1.49 ms                                                | 1.48 ms: 1.00x faster                                                 |
| bench_thread_pool        | 819 us                                                 | 825 us: 1.01x slower                                                  |
| docutils                 | 2.63 sec                                               | 2.65 sec: 1.01x slower                                                |
| scimark_lu               | 110 ms                                                 | 111 ms: 1.01x slower                                                  |
| pathlib                  | 18.2 ms                                                | 18.5 ms: 1.01x slower                                                 |
| regex_v8                 | 22.0 ms                                                | 22.4 ms: 1.01x slower                                                 |
| pidigits                 | 198 ms                                                 | 201 ms: 1.02x slower                                                  |
| mdp                      | 2.62 sec                                               | 2.66 sec: 1.02x slower                                                |
| unpickle_list            | 4.91 us                                                | 4.99 us: 1.02x slower                                                 |
| pickle_dict              | 31.1 us                                                | 31.6 us: 1.02x slower                                                 |
| fannkuch                 | 388 ms                                                 | 394 ms: 1.02x slower                                                  |
| pprint_pformat           | 1.46 sec                                               | 1.48 sec: 1.02x slower                                                |
| scimark_sor              | 118 ms                                                 | 121 ms: 1.03x slower                                                  |
| pprint_safe_repr         | 701 ms                                                 | 724 ms: 1.03x slower                                                  |
| pickle                   | 10.1 us                                                | 10.4 us: 1.03x slower                                                 |
| dulwich_log              | 63.7 ms                                                | 65.9 ms: 1.03x slower                                                 |
| regex_dna                | 204 ms                                                 | 211 ms: 1.03x slower                                                  |
| deepcopy                 | 342 us                                                 | 355 us: 1.04x slower                                                  |
| richards                 | 45.7 ms                                                | 47.5 ms: 1.04x slower                                                 |
| deepcopy_memo            | 37.0 us                                                | 38.5 us: 1.04x slower                                                 |
| float                    | 77.2 ms                                                | 80.5 ms: 1.04x slower                                                 |
| logging_silent           | 101 ns                                                 | 106 ns: 1.04x slower                                                  |
| tomli_loads              | 2.22 sec                                               | 2.33 sec: 1.05x slower                                                |
| spectral_norm            | 100 ms                                                 | 106 ms: 1.06x slower                                                  |
| xml_etree_process        | 53.9 ms                                                | 57.7 ms: 1.07x slower                                                 |
| pyflate                  | 418 ms                                                 | 450 ms: 1.08x slower                                                  |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.85 ms: 1.08x slower                                                 |
| deepcopy_reduce          | 2.94 us                                                | 3.19 us: 1.09x slower                                                 |
| sqlite_synth             | 2.52 us                                                | 2.74 us: 1.09x slower                                                 |
| xml_etree_generate       | 76.2 ms                                                | 83.3 ms: 1.09x slower                                                 |
| mako                     | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                 |
| python_startup           | 8.52 ms                                                | 9.33 ms: 1.09x slower                                                 |
| unpickle                 | 13.7 us                                                | 15.0 us: 1.10x slower                                                 |
| pickle_list              | 4.11 us                                                | 4.57 us: 1.11x slower                                                 |
| unpack_sequence          | 43.1 ns                                                | 48.0 ns: 1.11x slower                                                 |
| scimark_fft              | 328 ms                                                 | 366 ms: 1.11x slower                                                  |
| python_startup_no_site   | 6.01 ms                                                | 6.83 ms: 1.14x slower                                                 |
| telco                    | 6.58 ms                                                | 7.84 ms: 1.19x slower                                                 |
| async_generators         | 368 ms                                                 | 444 ms: 1.20x slower                                                  |
| dask                     | 360 ms                                                 | 520 ms: 1.44x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (2): bench_mp_pool, scimark_monte_carlo
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 59.77% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
