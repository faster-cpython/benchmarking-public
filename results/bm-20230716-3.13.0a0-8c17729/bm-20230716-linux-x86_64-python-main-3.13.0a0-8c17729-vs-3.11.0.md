
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 8c17729
- commit date: 2023-07-16
- overall geometric mean: 1.04x faster
- HPT reliability: 63.12%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-linux-x86_64-python-main-3.13.0a0-8c17729 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.65 sec: 1.01x slower                                |
| tornado_http   | 96.3 ms                                                | 96.8 ms: 1.01x slower                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-linux-x86_64-python-main-3.13.0a0-8c17729 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 93.1 ms                                                | 89.3 ms: 1.04x faster                                 |
| pidigits       | 198 ms                                                 | 196 ms: 1.01x faster                                  |
| float          | 77.2 ms                                                | 80.7 ms: 1.04x slower                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-linux-x86_64-python-main-3.13.0a0-8c17729 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.67 ms: 1.09x faster                                 |
| regex_v8       | 22.0 ms                                                | 22.3 ms: 1.01x slower                                 |
| regex_dna      | 204 ms                                                 | 207 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-linux-x86_64-python-main-3.13.0a0-8c17729 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.77 ms: 1.29x faster                                 |
| unpickle_pure_python | 228 us                                                 | 214 us: 1.06x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                  |
| pickle_pure_python   | 306 us                                                 | 298 us: 1.03x faster                                  |
| json_loads           | 26.5 us                                                | 26.1 us: 1.01x faster                                 |
| pickle_dict          | 31.1 us                                                | 31.7 us: 1.02x slower                                 |
| unpickle_list        | 4.91 us                                                | 5.14 us: 1.05x slower                                 |
| pickle               | 10.1 us                                                | 10.6 us: 1.05x slower                                 |
| tomli_loads          | 2.22 sec                                               | 2.33 sec: 1.05x slower                                |
| xml_etree_process    | 53.9 ms                                                | 58.5 ms: 1.09x slower                                 |
| unpickle             | 13.7 us                                                | 14.9 us: 1.09x slower                                 |
| xml_etree_generate   | 76.2 ms                                                | 84.6 ms: 1.11x slower                                 |
| pickle_list          | 4.11 us                                                | 4.70 us: 1.14x slower                                 |
| Geometric mean       | (ref)                                                  | 1.01x slower                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-linux-x86_64-python-main-3.13.0a0-8c17729 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.25 ms: 1.08x slower                                 |
| python_startup_no_site | 6.01 ms                                                | 6.71 ms: 1.12x slower                                 |
| Geometric mean         | (ref)                                                  | 1.10x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-linux-x86_64-python-main-3.13.0a0-8c17729 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.9 ms: 1.08x slower                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-linux-x86_64-python-main-3.13.0a0-8c17729 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 148 us: 3.28x faster                                  |
| generators               | 73.5 ms                                                | 28.7 ms: 2.56x faster                                 |
| asyncio_tcp              | 922 ms                                                 | 508 ms: 1.81x faster                                  |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                |
| json_dumps               | 12.6 ms                                                | 9.77 ms: 1.29x faster                                 |
| mypy2                    | 420 ms                                                 | 336 ms: 1.25x faster                                  |
| chaos                    | 69.2 ms                                                | 59.8 ms: 1.16x faster                                 |
| coroutines               | 25.5 ms                                                | 22.6 ms: 1.13x faster                                 |
| deltablue                | 3.67 ms                                                | 3.26 ms: 1.13x faster                                 |
| raytrace                 | 297 ms                                                 | 268 ms: 1.11x faster                                  |
| async_tree_io            | 1.30 sec                                               | 1.18 sec: 1.10x faster                                |
| async_tree_none          | 526 ms                                                 | 481 ms: 1.10x faster                                  |
| comprehensions           | 22.4 us                                                | 20.5 us: 1.09x faster                                 |
| regex_effbot             | 3.99 ms                                                | 3.67 ms: 1.09x faster                                 |
| sqlglot_parse            | 1.40 ms                                                | 1.29 ms: 1.09x faster                                 |
| async_tree_memoization   | 627 ms                                                 | 583 ms: 1.08x faster                                  |
| unpickle_pure_python     | 228 us                                                 | 214 us: 1.06x faster                                  |
| coverage                 | 100 ms                                                 | 94.1 ms: 1.06x faster                                 |
| sqlglot_transpile        | 1.70 ms                                                | 1.61 ms: 1.06x faster                                 |
| richards_super           | 56.8 ms                                                | 54.0 ms: 1.05x faster                                 |
| crypto_pyaes             | 74.7 ms                                                | 71.1 ms: 1.05x faster                                 |
| hexiom                   | 6.37 ms                                                | 6.11 ms: 1.04x faster                                 |
| nbody                    | 93.1 ms                                                | 89.3 ms: 1.04x faster                                 |
| nqueens                  | 83.4 ms                                                | 80.2 ms: 1.04x faster                                 |
| sqlglot_normalize        | 108 ms                                                 | 105 ms: 1.03x faster                                  |
| xml_etree_parse          | 158 ms                                                 | 154 ms: 1.03x faster                                  |
| pickle_pure_python       | 306 us                                                 | 298 us: 1.03x faster                                  |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 721 ms: 1.03x faster                                  |
| logging_simple           | 6.03 us                                                | 5.90 us: 1.02x faster                                 |
| gc_traversal             | 4.02 ms                                                | 3.94 ms: 1.02x faster                                 |
| logging_format           | 6.68 us                                                | 6.54 us: 1.02x faster                                 |
| mdp                      | 2.62 sec                                               | 2.56 sec: 1.02x faster                                |
| unpack_sequence          | 43.1 ns                                                | 42.3 ns: 1.02x faster                                 |
| pycparser                | 1.18 sec                                               | 1.16 sec: 1.02x faster                                |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.02x faster                                  |
| go                       | 140 ms                                                 | 138 ms: 1.01x faster                                  |
| json_loads               | 26.5 us                                                | 26.1 us: 1.01x faster                                 |
| sqlglot_optimize         | 53.1 ms                                                | 52.5 ms: 1.01x faster                                 |
| pidigits                 | 198 ms                                                 | 196 ms: 1.01x faster                                  |
| tornado_http             | 96.3 ms                                                | 96.8 ms: 1.01x slower                                 |
| docutils                 | 2.63 sec                                               | 2.65 sec: 1.01x slower                                |
| regex_v8                 | 22.0 ms                                                | 22.3 ms: 1.01x slower                                 |
| logging_silent           | 101 ns                                                 | 103 ns: 1.01x slower                                  |
| scimark_lu               | 110 ms                                                 | 111 ms: 1.01x slower                                  |
| regex_dna                | 204 ms                                                 | 207 ms: 1.02x slower                                  |
| pickle_dict              | 31.1 us                                                | 31.7 us: 1.02x slower                                 |
| deepcopy_memo            | 37.0 us                                                | 37.7 us: 1.02x slower                                 |
| create_gc_cycles         | 1.49 ms                                                | 1.52 ms: 1.02x slower                                 |
| fannkuch                 | 388 ms                                                 | 397 ms: 1.02x slower                                  |
| scimark_sor              | 118 ms                                                 | 121 ms: 1.03x slower                                  |
| pathlib                  | 18.2 ms                                                | 18.8 ms: 1.03x slower                                 |
| pprint_pformat           | 1.46 sec                                               | 1.51 sec: 1.04x slower                                |
| deepcopy                 | 342 us                                                 | 356 us: 1.04x slower                                  |
| dulwich_log              | 63.7 ms                                                | 66.4 ms: 1.04x slower                                 |
| float                    | 77.2 ms                                                | 80.7 ms: 1.04x slower                                 |
| unpickle_list            | 4.91 us                                                | 5.14 us: 1.05x slower                                 |
| pprint_safe_repr         | 701 ms                                                 | 736 ms: 1.05x slower                                  |
| pickle                   | 10.1 us                                                | 10.6 us: 1.05x slower                                 |
| tomli_loads              | 2.22 sec                                               | 2.33 sec: 1.05x slower                                |
| richards                 | 45.7 ms                                                | 48.1 ms: 1.05x slower                                 |
| deepcopy_reduce          | 2.94 us                                                | 3.15 us: 1.07x slower                                 |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.82 ms: 1.07x slower                                 |
| pyflate                  | 418 ms                                                 | 449 ms: 1.07x slower                                  |
| mako                     | 10.1 ms                                                | 10.9 ms: 1.08x slower                                 |
| python_startup           | 8.52 ms                                                | 9.25 ms: 1.08x slower                                 |
| spectral_norm            | 100 ms                                                 | 109 ms: 1.09x slower                                  |
| xml_etree_process        | 53.9 ms                                                | 58.5 ms: 1.09x slower                                 |
| unpickle                 | 13.7 us                                                | 14.9 us: 1.09x slower                                 |
| sqlite_synth             | 2.52 us                                                | 2.75 us: 1.09x slower                                 |
| scimark_fft              | 328 ms                                                 | 360 ms: 1.10x slower                                  |
| telco                    | 6.58 ms                                                | 7.28 ms: 1.11x slower                                 |
| xml_etree_generate       | 76.2 ms                                                | 84.6 ms: 1.11x slower                                 |
| python_startup_no_site   | 6.01 ms                                                | 6.71 ms: 1.12x slower                                 |
| pickle_list              | 4.11 us                                                | 4.70 us: 1.14x slower                                 |
| async_generators         | 368 ms                                                 | 454 ms: 1.23x slower                                  |
| dask                     | 360 ms                                                 | 523 ms: 1.45x slower                                  |
| Geometric mean           | (ref)                                                  | 1.04x faster                                          |

Benchmark hidden because not significant (6): xml_etree_iterparse, bench_mp_pool, bench_thread_pool, regex_compile, json, scimark_monte_carlo
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 63.12% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
