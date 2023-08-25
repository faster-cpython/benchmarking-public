
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: d20d52b
- commit date: 2023-08-11
- overall geometric mean: 1.03x faster
- HPT reliability: 71.92%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 268 ms: 1.04x slower                                    |
| docutils       | 2.63 sec                                               | 2.72 sec: 1.03x slower                                  |
| tornado_http   | 96.3 ms                                                | 99.3 ms: 1.03x slower                                   |
| Geometric mean | (ref)                                                  | 1.03x slower                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                    |
| nbody          | 93.1 ms                                                | 89.7 ms: 1.04x faster                                   |
| float          | 77.2 ms                                                | 79.9 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.46 ms: 1.16x faster                                   |
| regex_dna      | 204 ms                                                 | 202 ms: 1.01x faster                                    |
| regex_v8       | 22.0 ms                                                | 22.5 ms: 1.02x slower                                   |
| regex_compile  | 138 ms                                                 | 145 ms: 1.05x slower                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.76 ms: 1.29x faster                                   |
| unpickle_pure_python | 228 us                                                 | 216 us: 1.06x faster                                    |
| json_loads           | 26.5 us                                                | 25.1 us: 1.05x faster                                   |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                    |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                    |
| pickle_pure_python   | 306 us                                                 | 307 us: 1.00x slower                                    |
| unpickle_list        | 4.91 us                                                | 5.02 us: 1.02x slower                                   |
| pickle_dict          | 31.1 us                                                | 32.3 us: 1.04x slower                                   |
| pickle               | 10.1 us                                                | 10.9 us: 1.08x slower                                   |
| unpickle             | 13.7 us                                                | 15.0 us: 1.09x slower                                   |
| xml_etree_process    | 53.9 ms                                                | 59.8 ms: 1.11x slower                                   |
| xml_etree_generate   | 76.2 ms                                                | 85.8 ms: 1.13x slower                                   |
| pickle_list          | 4.11 us                                                | 4.81 us: 1.17x slower                                   |
| Geometric mean       | (ref)                                                  | 1.02x slower                                            |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.34 ms: 1.10x slower                                   |
| python_startup_no_site | 6.01 ms                                                | 6.78 ms: 1.13x slower                                   |
| Geometric mean         | (ref)                                                  | 1.11x slower                                            |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.6 ms: 1.05x slower                                   |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-python-3.12-3.12.0rc1+-d20d52b |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 149 us: 3.26x faster                                    |
| generators               | 73.5 ms                                                | 30.6 ms: 2.40x faster                                   |
| asyncio_tcp              | 922 ms                                                 | 512 ms: 1.80x faster                                    |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.80 sec: 1.75x faster                                  |
| json_dumps               | 12.6 ms                                                | 9.76 ms: 1.29x faster                                   |
| mypy2                    | 420 ms                                                 | 345 ms: 1.22x faster                                    |
| coroutines               | 25.5 ms                                                | 22.0 ms: 1.16x faster                                   |
| regex_effbot             | 3.99 ms                                                | 3.46 ms: 1.16x faster                                   |
| richards_super           | 56.8 ms                                                | 49.3 ms: 1.15x faster                                   |
| async_tree_none          | 526 ms                                                 | 467 ms: 1.13x faster                                    |
| async_tree_io            | 1.30 sec                                               | 1.15 sec: 1.12x faster                                  |
| async_tree_memoization   | 627 ms                                                 | 572 ms: 1.10x faster                                    |
| chaos                    | 69.2 ms                                                | 63.7 ms: 1.09x faster                                   |
| comprehensions           | 22.4 us                                                | 20.7 us: 1.08x faster                                   |
| coverage                 | 100 ms                                                 | 93.5 ms: 1.07x faster                                   |
| unpickle_pure_python     | 228 us                                                 | 216 us: 1.06x faster                                    |
| json_loads               | 26.5 us                                                | 25.1 us: 1.05x faster                                   |
| sqlglot_parse            | 1.40 ms                                                | 1.33 ms: 1.05x faster                                   |
| hexiom                   | 6.37 ms                                                | 6.07 ms: 1.05x faster                                   |
| deltablue                | 3.67 ms                                                | 3.50 ms: 1.05x faster                                   |
| gc_traversal             | 4.02 ms                                                | 3.84 ms: 1.05x faster                                   |
| pidigits                 | 198 ms                                                 | 189 ms: 1.05x faster                                    |
| richards                 | 45.7 ms                                                | 43.8 ms: 1.04x faster                                   |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 709 ms: 1.04x faster                                    |
| nbody                    | 93.1 ms                                                | 89.7 ms: 1.04x faster                                   |
| go                       | 140 ms                                                 | 135 ms: 1.04x faster                                    |
| pycparser                | 1.18 sec                                               | 1.14 sec: 1.03x faster                                  |
| nqueens                  | 83.4 ms                                                | 80.6 ms: 1.03x faster                                   |
| sqlglot_transpile        | 1.70 ms                                                | 1.65 ms: 1.03x faster                                   |
| logging_silent           | 101 ns                                                 | 98.0 ns: 1.03x faster                                   |
| mdp                      | 2.62 sec                                               | 2.54 sec: 1.03x faster                                  |
| json                     | 4.94 ms                                                | 4.81 ms: 1.03x faster                                   |
| xml_etree_parse          | 158 ms                                                 | 154 ms: 1.03x faster                                    |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.02x faster                                    |
| regex_dna                | 204 ms                                                 | 202 ms: 1.01x faster                                    |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                    |
| pickle_pure_python       | 306 us                                                 | 307 us: 1.00x slower                                    |
| fannkuch                 | 388 ms                                                 | 390 ms: 1.01x slower                                    |
| pathlib                  | 18.2 ms                                                | 18.4 ms: 1.01x slower                                   |
| bench_thread_pool        | 819 us                                                 | 829 us: 1.01x slower                                    |
| sqlglot_optimize         | 53.1 ms                                                | 54.0 ms: 1.02x slower                                   |
| sqlglot_normalize        | 108 ms                                                 | 110 ms: 1.02x slower                                    |
| create_gc_cycles         | 1.49 ms                                                | 1.51 ms: 1.02x slower                                   |
| regex_v8                 | 22.0 ms                                                | 22.5 ms: 1.02x slower                                   |
| pprint_pformat           | 1.46 sec                                               | 1.49 sec: 1.02x slower                                  |
| deepcopy_memo            | 37.0 us                                                | 37.9 us: 1.02x slower                                   |
| unpickle_list            | 4.91 us                                                | 5.02 us: 1.02x slower                                   |
| scimark_sor              | 118 ms                                                 | 121 ms: 1.03x slower                                    |
| scimark_lu               | 110 ms                                                 | 113 ms: 1.03x slower                                    |
| crypto_pyaes             | 74.7 ms                                                | 77.0 ms: 1.03x slower                                   |
| tornado_http             | 96.3 ms                                                | 99.3 ms: 1.03x slower                                   |
| sqlalchemy_imperative    | 17.9 ms                                                | 18.5 ms: 1.03x slower                                   |
| docutils                 | 2.63 sec                                               | 2.72 sec: 1.03x slower                                  |
| spectral_norm            | 100 ms                                                 | 103 ms: 1.03x slower                                    |
| float                    | 77.2 ms                                                | 79.9 ms: 1.04x slower                                   |
| 2to3                     | 259 ms                                                 | 268 ms: 1.04x slower                                    |
| logging_simple           | 6.03 us                                                | 6.25 us: 1.04x slower                                   |
| logging_format           | 6.68 us                                                | 6.93 us: 1.04x slower                                   |
| pickle_dict              | 31.1 us                                                | 32.3 us: 1.04x slower                                   |
| telco                    | 6.58 ms                                                | 6.87 ms: 1.04x slower                                   |
| deepcopy                 | 342 us                                                 | 357 us: 1.04x slower                                    |
| sqlalchemy_declarative   | 138 ms                                                 | 144 ms: 1.04x slower                                    |
| pprint_safe_repr         | 701 ms                                                 | 733 ms: 1.05x slower                                    |
| mako                     | 10.1 ms                                                | 10.6 ms: 1.05x slower                                   |
| regex_compile            | 138 ms                                                 | 145 ms: 1.05x slower                                    |
| scimark_monte_carlo      | 68.1 ms                                                | 71.8 ms: 1.06x slower                                   |
| pyflate                  | 418 ms                                                 | 443 ms: 1.06x slower                                    |
| deepcopy_reduce          | 2.94 us                                                | 3.14 us: 1.07x slower                                   |
| dulwich_log              | 63.7 ms                                                | 68.1 ms: 1.07x slower                                   |
| unpack_sequence          | 43.1 ns                                                | 46.4 ns: 1.08x slower                                   |
| pickle                   | 10.1 us                                                | 10.9 us: 1.08x slower                                   |
| scimark_fft              | 328 ms                                                 | 358 ms: 1.09x slower                                    |
| sqlite_synth             | 2.52 us                                                | 2.76 us: 1.09x slower                                   |
| unpickle                 | 13.7 us                                                | 15.0 us: 1.09x slower                                   |
| python_startup           | 8.52 ms                                                | 9.34 ms: 1.10x slower                                   |
| xml_etree_process        | 53.9 ms                                                | 59.8 ms: 1.11x slower                                   |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 5.01 ms: 1.11x slower                                   |
| xml_etree_generate       | 76.2 ms                                                | 85.8 ms: 1.13x slower                                   |
| python_startup_no_site   | 6.01 ms                                                | 6.78 ms: 1.13x slower                                   |
| pickle_list              | 4.11 us                                                | 4.81 us: 1.17x slower                                   |
| async_generators         | 368 ms                                                 | 449 ms: 1.22x slower                                    |
| dask                     | 360 ms                                                 | 536 ms: 1.49x slower                                    |
| Geometric mean           | (ref)                                                  | 1.03x faster                                            |

Benchmark hidden because not significant (3): tomli_loads, bench_mp_pool, raytrace
Ignored benchmarks (15) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 71.92% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
