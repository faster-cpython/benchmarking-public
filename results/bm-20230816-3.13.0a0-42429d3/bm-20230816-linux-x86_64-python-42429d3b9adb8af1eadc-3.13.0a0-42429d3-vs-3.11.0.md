
# Results vs. 3.11.0

- fork: python
- ref: 42429d3b9adb8af1eadc
- machine: linux-x86_64
- commit hash: 42429d3
- commit date: 2023-08-16
- overall geometric mean: 1.04x faster
- HPT reliability: 67.39%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230816-linux-x86_64-python-42429d3b9adb8af1eadc-3.13.0a0-42429d3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tornado_http   | 96.3 ms                                                | 95.3 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230816-linux-x86_64-python-42429d3b9adb8af1eadc-3.13.0a0-42429d3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 91.7 ms: 1.02x faster                                                 |
| pidigits       | 198 ms                                                 | 201 ms: 1.01x slower                                                  |
| float          | 77.2 ms                                                | 80.6 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230816-linux-x86_64-python-42429d3b9adb8af1eadc-3.13.0a0-42429d3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.66 ms: 1.09x faster                                                 |
| regex_compile  | 138 ms                                                 | 137 ms: 1.01x faster                                                  |
| regex_v8       | 22.0 ms                                                | 22.9 ms: 1.04x slower                                                 |
| regex_dna      | 204 ms                                                 | 217 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230816-linux-x86_64-python-42429d3b9adb8af1eadc-3.13.0a0-42429d3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.69 ms: 1.30x faster                                                 |
| unpickle_pure_python | 228 us                                                 | 213 us: 1.07x faster                                                  |
| tomli_loads          | 2.22 sec                                               | 2.11 sec: 1.05x faster                                                |
| json_loads           | 26.5 us                                                | 25.3 us: 1.05x faster                                                 |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.04x faster                                                  |
| pickle_pure_python   | 306 us                                                 | 298 us: 1.03x faster                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                  |
| pickle_dict          | 31.1 us                                                | 33.0 us: 1.06x slower                                                 |
| pickle               | 10.1 us                                                | 10.8 us: 1.07x slower                                                 |
| xml_etree_process    | 53.9 ms                                                | 58.5 ms: 1.09x slower                                                 |
| unpickle             | 13.7 us                                                | 14.9 us: 1.09x slower                                                 |
| xml_etree_generate   | 76.2 ms                                                | 84.6 ms: 1.11x slower                                                 |
| pickle_list          | 4.11 us                                                | 4.63 us: 1.13x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230816-linux-x86_64-python-42429d3b9adb8af1eadc-3.13.0a0-42429d3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.35 ms: 1.10x slower                                                 |
| python_startup_no_site | 6.01 ms                                                | 6.84 ms: 1.14x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230816-linux-x86_64-python-42429d3b9adb8af1eadc-3.13.0a0-42429d3 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230816-linux-x86_64-python-42429d3b9adb8af1eadc-3.13.0a0-42429d3 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 143 us: 3.40x faster                                                  |
| generators               | 73.5 ms                                                | 29.0 ms: 2.53x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 486 ms: 1.89x faster                                                  |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                |
| json_dumps               | 12.6 ms                                                | 9.69 ms: 1.30x faster                                                 |
| async_tree_none          | 526 ms                                                 | 435 ms: 1.21x faster                                                  |
| coverage                 | 100 ms                                                 | 85.1 ms: 1.18x faster                                                 |
| chaos                    | 69.2 ms                                                | 59.8 ms: 1.16x faster                                                 |
| coroutines               | 25.5 ms                                                | 22.2 ms: 1.15x faster                                                 |
| deltablue                | 3.67 ms                                                | 3.27 ms: 1.12x faster                                                 |
| async_tree_memoization   | 627 ms                                                 | 563 ms: 1.11x faster                                                  |
| regex_effbot             | 3.99 ms                                                | 3.66 ms: 1.09x faster                                                 |
| sqlglot_parse            | 1.40 ms                                                | 1.28 ms: 1.09x faster                                                 |
| async_tree_io            | 1.30 sec                                               | 1.19 sec: 1.09x faster                                                |
| crypto_pyaes             | 74.7 ms                                                | 68.5 ms: 1.09x faster                                                 |
| raytrace                 | 297 ms                                                 | 274 ms: 1.08x faster                                                  |
| comprehensions           | 22.4 us                                                | 20.8 us: 1.08x faster                                                 |
| unpickle_pure_python     | 228 us                                                 | 213 us: 1.07x faster                                                  |
| sqlglot_transpile        | 1.70 ms                                                | 1.60 ms: 1.06x faster                                                 |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 701 ms: 1.05x faster                                                  |
| tomli_loads              | 2.22 sec                                               | 2.11 sec: 1.05x faster                                                |
| hexiom                   | 6.37 ms                                                | 6.08 ms: 1.05x faster                                                 |
| richards_super           | 56.8 ms                                                | 54.2 ms: 1.05x faster                                                 |
| json_loads               | 26.5 us                                                | 25.3 us: 1.05x faster                                                 |
| nqueens                  | 83.4 ms                                                | 80.3 ms: 1.04x faster                                                 |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.04x faster                                                  |
| gc_traversal             | 4.02 ms                                                | 3.89 ms: 1.03x faster                                                 |
| scimark_monte_carlo      | 68.1 ms                                                | 66.2 ms: 1.03x faster                                                 |
| pickle_pure_python       | 306 us                                                 | 298 us: 1.03x faster                                                  |
| sqlglot_normalize        | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| logging_simple           | 6.03 us                                                | 5.91 us: 1.02x faster                                                 |
| json                     | 4.94 ms                                                | 4.85 ms: 1.02x faster                                                 |
| logging_format           | 6.68 us                                                | 6.57 us: 1.02x faster                                                 |
| nbody                    | 93.1 ms                                                | 91.7 ms: 1.02x faster                                                 |
| regex_compile            | 138 ms                                                 | 137 ms: 1.01x faster                                                  |
| go                       | 140 ms                                                 | 138 ms: 1.01x faster                                                  |
| meteor_contest           | 107 ms                                                 | 106 ms: 1.01x faster                                                  |
| tornado_http             | 96.3 ms                                                | 95.3 ms: 1.01x faster                                                 |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                                  |
| create_gc_cycles         | 1.49 ms                                                | 1.49 ms: 1.00x slower                                                 |
| fannkuch                 | 388 ms                                                 | 392 ms: 1.01x slower                                                  |
| logging_silent           | 101 ns                                                 | 102 ns: 1.01x slower                                                  |
| pathlib                  | 18.2 ms                                                | 18.5 ms: 1.01x slower                                                 |
| pidigits                 | 198 ms                                                 | 201 ms: 1.01x slower                                                  |
| pycparser                | 1.18 sec                                               | 1.20 sec: 1.02x slower                                                |
| unpack_sequence          | 43.1 ns                                                | 43.9 ns: 1.02x slower                                                 |
| deepcopy_memo            | 37.0 us                                                | 37.7 us: 1.02x slower                                                 |
| pprint_pformat           | 1.46 sec                                               | 1.49 sec: 1.02x slower                                                |
| deepcopy                 | 342 us                                                 | 352 us: 1.03x slower                                                  |
| richards                 | 45.7 ms                                                | 47.1 ms: 1.03x slower                                                 |
| dulwich_log              | 63.7 ms                                                | 65.6 ms: 1.03x slower                                                 |
| regex_v8                 | 22.0 ms                                                | 22.9 ms: 1.04x slower                                                 |
| float                    | 77.2 ms                                                | 80.6 ms: 1.04x slower                                                 |
| pprint_safe_repr         | 701 ms                                                 | 732 ms: 1.04x slower                                                  |
| scimark_sor              | 118 ms                                                 | 123 ms: 1.04x slower                                                  |
| mdp                      | 2.62 sec                                               | 2.73 sec: 1.04x slower                                                |
| spectral_norm            | 100 ms                                                 | 105 ms: 1.05x slower                                                  |
| pyflate                  | 418 ms                                                 | 444 ms: 1.06x slower                                                  |
| scimark_fft              | 328 ms                                                 | 349 ms: 1.06x slower                                                  |
| pickle_dict              | 31.1 us                                                | 33.0 us: 1.06x slower                                                 |
| regex_dna                | 204 ms                                                 | 217 ms: 1.06x slower                                                  |
| pickle                   | 10.1 us                                                | 10.8 us: 1.07x slower                                                 |
| mako                     | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                 |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.85 ms: 1.08x slower                                                 |
| deepcopy_reduce          | 2.94 us                                                | 3.17 us: 1.08x slower                                                 |
| xml_etree_process        | 53.9 ms                                                | 58.5 ms: 1.09x slower                                                 |
| sqlite_synth             | 2.52 us                                                | 2.74 us: 1.09x slower                                                 |
| unpickle                 | 13.7 us                                                | 14.9 us: 1.09x slower                                                 |
| python_startup           | 8.52 ms                                                | 9.35 ms: 1.10x slower                                                 |
| xml_etree_generate       | 76.2 ms                                                | 84.6 ms: 1.11x slower                                                 |
| pickle_list              | 4.11 us                                                | 4.63 us: 1.13x slower                                                 |
| python_startup_no_site   | 6.01 ms                                                | 6.84 ms: 1.14x slower                                                 |
| telco                    | 6.58 ms                                                | 8.05 ms: 1.22x slower                                                 |
| async_generators         | 368 ms                                                 | 457 ms: 1.24x slower                                                  |
| dask                     | 360 ms                                                 | 520 ms: 1.45x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (7): scimark_lu, docutils, bench_thread_pool, bench_mp_pool, sqlglot_optimize, unpickle_list, mypy2
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 67.39% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
