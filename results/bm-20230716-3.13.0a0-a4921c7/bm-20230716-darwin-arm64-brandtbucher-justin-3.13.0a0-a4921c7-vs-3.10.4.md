
# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin
- machine: darwin-arm64
- commit hash: a4921c7
- commit date: 2023-07-16
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 1.78 sec                                               | 1.52 sec: 1.17x faster                                        |
| tornado_http   | 91.9 ms                                                | 70.1 ms: 1.31x faster                                         |
| Geometric mean | (ref)                                                  | 1.24x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 69.8 ms: 1.35x faster                                         |
| float          | 72.3 ms                                                | 59.7 ms: 1.21x faster                                         |
| Geometric mean | (ref)                                                  | 1.18x faster                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 75.3 ms: 1.28x faster                                         |
| regex_v8       | 17.5 ms                                                | 15.8 ms: 1.11x faster                                         |
| regex_dna      | 160 ms                                                 | 150 ms: 1.07x faster                                          |
| regex_effbot   | 2.45 ms                                                | 2.56 ms: 1.05x slower                                         |
| Geometric mean | (ref)                                                  | 1.10x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 180 us: 1.58x faster                                          |
| unpickle_pure_python | 203 us                                                 | 140 us: 1.45x faster                                          |
| json_dumps           | 8.38 ms                                                | 6.48 ms: 1.29x faster                                         |
| xml_etree_process    | 45.1 ms                                                | 37.8 ms: 1.19x faster                                         |
| tomli_loads          | 1.76 sec                                               | 1.54 sec: 1.14x faster                                        |
| unpickle             | 9.77 us                                                | 9.38 us: 1.04x faster                                         |
| pickle_dict          | 17.8 us                                                | 17.9 us: 1.01x slower                                         |
| xml_etree_iterparse  | 72.6 ms                                                | 73.7 ms: 1.01x slower                                         |
| pickle               | 7.36 us                                                | 7.47 us: 1.01x slower                                         |
| xml_etree_parse      | 107 ms                                                 | 109 ms: 1.02x slower                                          |
| pickle_list          | 2.83 us                                                | 2.89 us: 1.02x slower                                         |
| xml_etree_generate   | 54.3 ms                                                | 55.9 ms: 1.03x slower                                         |
| json_loads           | 16.9 us                                                | 17.7 us: 1.05x slower                                         |
| unpickle_list        | 2.66 us                                                | 3.27 us: 1.23x slower                                         |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 12.7 ms: 1.01x slower                                         |
| python_startup_no_site | 9.73 ms                                                | 10.6 ms: 1.09x slower                                         |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 10.5 ms                                                | 8.57 ms: 1.22x faster                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 87.9 us: 3.92x faster                                         |
| deltablue                | 5.15 ms                                                | 2.43 ms: 2.12x faster                                         |
| richards_super           | 60.7 ms                                                | 33.1 ms: 1.83x faster                                         |
| logging_silent           | 119 ns                                                 | 65.2 ns: 1.83x faster                                         |
| richards                 | 51.4 ms                                                | 29.7 ms: 1.73x faster                                         |
| go                       | 165 ms                                                 | 104 ms: 1.58x faster                                          |
| pickle_pure_python       | 284 us                                                 | 180 us: 1.58x faster                                          |
| scimark_sor              | 127 ms                                                 | 80.4 ms: 1.58x faster                                         |
| sqlglot_parse            | 1.33 ms                                                | 872 us: 1.53x faster                                          |
| hexiom                   | 6.32 ms                                                | 4.18 ms: 1.51x faster                                         |
| chaos                    | 66.8 ms                                                | 44.3 ms: 1.51x faster                                         |
| async_tree_memoization   | 493 ms                                                 | 327 ms: 1.51x faster                                          |
| asyncio_tcp              | 673 ms                                                 | 452 ms: 1.49x faster                                          |
| scimark_monte_carlo      | 72.2 ms                                                | 48.8 ms: 1.48x faster                                         |
| sqlglot_transpile        | 1.54 ms                                                | 1.04 ms: 1.47x faster                                         |
| crypto_pyaes             | 78.0 ms                                                | 53.3 ms: 1.46x faster                                         |
| unpickle_pure_python     | 203 us                                                 | 140 us: 1.45x faster                                          |
| async_tree_io            | 1.02 sec                                               | 705 ms: 1.45x faster                                          |
| async_tree_none          | 402 ms                                                 | 278 ms: 1.45x faster                                          |
| unpack_sequence          | 38.7 ns                                                | 27.4 ns: 1.41x faster                                         |
| scimark_lu               | 110 ms                                                 | 78.1 ms: 1.41x faster                                         |
| pycparser                | 915 ms                                                 | 662 ms: 1.38x faster                                          |
| raytrace                 | 328 ms                                                 | 239 ms: 1.37x faster                                          |
| nbody                    | 94.1 ms                                                | 69.8 ms: 1.35x faster                                         |
| pyflate                  | 453 ms                                                 | 339 ms: 1.34x faster                                          |
| logging_format           | 5.01 us                                                | 3.77 us: 1.33x faster                                         |
| logging_simple           | 4.63 us                                                | 3.50 us: 1.32x faster                                         |
| spectral_norm            | 96.4 ms                                                | 73.1 ms: 1.32x faster                                         |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.25 sec: 1.31x faster                                        |
| tornado_http             | 91.9 ms                                                | 70.1 ms: 1.31x faster                                         |
| generators               | 32.9 ms                                                | 25.3 ms: 1.30x faster                                         |
| json_dumps               | 8.38 ms                                                | 6.48 ms: 1.29x faster                                         |
| regex_compile            | 96.6 ms                                                | 75.3 ms: 1.28x faster                                         |
| pprint_pformat           | 1.24 sec                                               | 981 ms: 1.26x faster                                          |
| create_gc_cycles         | 876 us                                                 | 695 us: 1.26x faster                                          |
| deepcopy                 | 278 us                                                 | 223 us: 1.25x faster                                          |
| dulwich_log              | 37.1 ms                                                | 29.8 ms: 1.25x faster                                         |
| pprint_safe_repr         | 609 ms                                                 | 489 ms: 1.24x faster                                          |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 543 ms: 1.23x faster                                          |
| mako                     | 10.5 ms                                                | 8.57 ms: 1.22x faster                                         |
| float                    | 72.3 ms                                                | 59.7 ms: 1.21x faster                                         |
| coroutines               | 20.2 ms                                                | 16.7 ms: 1.21x faster                                         |
| mypy2                    | 308 ms                                                 | 258 ms: 1.19x faster                                          |
| xml_etree_process        | 45.1 ms                                                | 37.8 ms: 1.19x faster                                         |
| deepcopy_reduce          | 2.38 us                                                | 2.03 us: 1.17x faster                                         |
| docutils                 | 1.78 sec                                               | 1.52 sec: 1.17x faster                                        |
| deepcopy_memo            | 34.5 us                                                | 29.7 us: 1.16x faster                                         |
| tomli_loads              | 1.76 sec                                               | 1.54 sec: 1.14x faster                                        |
| sqlglot_optimize         | 38.0 ms                                                | 33.5 ms: 1.14x faster                                         |
| bench_thread_pool        | 548 us                                                 | 484 us: 1.13x faster                                          |
| nqueens                  | 68.1 ms                                                | 60.2 ms: 1.13x faster                                         |
| scimark_fft              | 232 ms                                                 | 205 ms: 1.13x faster                                          |
| regex_v8                 | 17.5 ms                                                | 15.8 ms: 1.11x faster                                         |
| sqlglot_normalize        | 197 ms                                                 | 181 ms: 1.09x faster                                          |
| fannkuch                 | 317 ms                                                 | 292 ms: 1.09x faster                                          |
| meteor_contest           | 78.6 ms                                                | 72.7 ms: 1.08x faster                                         |
| regex_dna                | 160 ms                                                 | 150 ms: 1.07x faster                                          |
| comprehensions           | 17.7 us                                                | 16.6 us: 1.06x faster                                         |
| unpickle                 | 9.77 us                                                | 9.38 us: 1.04x faster                                         |
| json                     | 3.10 ms                                                | 2.98 ms: 1.04x faster                                         |
| mdp                      | 1.67 sec                                               | 1.64 sec: 1.02x faster                                        |
| python_startup           | 12.6 ms                                                | 12.7 ms: 1.01x slower                                         |
| pickle_dict              | 17.8 us                                                | 17.9 us: 1.01x slower                                         |
| xml_etree_iterparse      | 72.6 ms                                                | 73.7 ms: 1.01x slower                                         |
| pickle                   | 7.36 us                                                | 7.47 us: 1.01x slower                                         |
| xml_etree_parse          | 107 ms                                                 | 109 ms: 1.02x slower                                          |
| pickle_list              | 2.83 us                                                | 2.89 us: 1.02x slower                                         |
| xml_etree_generate       | 54.3 ms                                                | 55.9 ms: 1.03x slower                                         |
| telco                    | 3.68 ms                                                | 3.85 ms: 1.05x slower                                         |
| json_loads               | 16.9 us                                                | 17.7 us: 1.05x slower                                         |
| regex_effbot             | 2.45 ms                                                | 2.56 ms: 1.05x slower                                         |
| sqlite_synth             | 1.47 us                                                | 1.57 us: 1.06x slower                                         |
| python_startup_no_site   | 9.73 ms                                                | 10.6 ms: 1.09x slower                                         |
| bench_mp_pool            | 41.0 ms                                                | 47.1 ms: 1.15x slower                                         |
| pathlib                  | 28.8 ms                                                | 33.7 ms: 1.17x slower                                         |
| coverage                 | 40.8 ms                                                | 50.0 ms: 1.22x slower                                         |
| unpickle_list            | 2.66 us                                                | 3.27 us: 1.23x slower                                         |
| dask                     | 258 ms                                                 | 323 ms: 1.25x slower                                          |
| async_generators         | 233 ms                                                 | 306 ms: 1.31x slower                                          |
| Geometric mean           | (ref)                                                  | 1.22x faster                                                  |

Benchmark hidden because not significant (3): gc_traversal, pidigits, scimark_sparse_mat_mult
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x
