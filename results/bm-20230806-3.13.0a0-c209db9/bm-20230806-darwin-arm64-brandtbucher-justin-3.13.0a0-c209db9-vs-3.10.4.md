
# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin
- machine: darwin-arm64
- commit hash: c209db9
- commit date: 2023-08-06
- overall geometric mean: 1.15x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 1.78 sec                                               | 1.58 sec: 1.13x faster                                        |
| tornado_http   | 91.9 ms                                                | 73.0 ms: 1.26x faster                                         |
| Geometric mean | (ref)                                                  | 1.19x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 76.2 ms: 1.24x faster                                         |
| float          | 72.3 ms                                                | 62.0 ms: 1.17x faster                                         |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                          |
| Geometric mean | (ref)                                                  | 1.13x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 85.8 ms: 1.13x faster                                         |
| regex_v8       | 17.5 ms                                                | 15.8 ms: 1.11x faster                                         |
| regex_dna      | 160 ms                                                 | 150 ms: 1.06x faster                                          |
| regex_effbot   | 2.45 ms                                                | 2.56 ms: 1.05x slower                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 205 us: 1.38x faster                                          |
| json_dumps           | 8.38 ms                                                | 6.67 ms: 1.26x faster                                         |
| unpickle_pure_python | 203 us                                                 | 173 us: 1.18x faster                                          |
| xml_etree_process    | 45.1 ms                                                | 41.7 ms: 1.08x faster                                         |
| tomli_loads          | 1.76 sec                                               | 1.67 sec: 1.05x faster                                        |
| unpickle             | 9.77 us                                                | 9.39 us: 1.04x faster                                         |
| pickle               | 7.36 us                                                | 7.50 us: 1.02x slower                                         |
| pickle_list          | 2.83 us                                                | 2.90 us: 1.02x slower                                         |
| json_loads           | 16.9 us                                                | 17.4 us: 1.03x slower                                         |
| xml_etree_parse      | 107 ms                                                 | 112 ms: 1.04x slower                                          |
| xml_etree_iterparse  | 72.6 ms                                                | 78.6 ms: 1.08x slower                                         |
| xml_etree_generate   | 54.3 ms                                                | 60.2 ms: 1.11x slower                                         |
| unpickle_list        | 2.66 us                                                | 3.19 us: 1.20x slower                                         |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                  |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 11.1 ms: 1.13x faster                                         |
| python_startup_no_site | 9.73 ms                                                | 9.05 ms: 1.07x faster                                         |
| Geometric mean         | (ref)                                                  | 1.10x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 10.5 ms                                                | 8.08 ms: 1.30x faster                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 97.2 us: 3.54x faster                                         |
| deltablue                | 5.15 ms                                                | 2.93 ms: 1.76x faster                                         |
| asyncio_tcp              | 673 ms                                                 | 421 ms: 1.60x faster                                          |
| crypto_pyaes             | 78.0 ms                                                | 49.5 ms: 1.58x faster                                         |
| logging_silent           | 119 ns                                                 | 77.8 ns: 1.53x faster                                         |
| async_tree_memoization   | 493 ms                                                 | 325 ms: 1.52x faster                                          |
| async_tree_io            | 1.02 sec                                               | 683 ms: 1.49x faster                                          |
| richards_super           | 60.7 ms                                                | 41.5 ms: 1.46x faster                                         |
| async_tree_none          | 402 ms                                                 | 276 ms: 1.46x faster                                          |
| chaos                    | 66.8 ms                                                | 46.9 ms: 1.42x faster                                         |
| sqlglot_parse            | 1.33 ms                                                | 945 us: 1.41x faster                                          |
| raytrace                 | 328 ms                                                 | 233 ms: 1.40x faster                                          |
| unpack_sequence          | 38.7 ns                                                | 27.9 ns: 1.39x faster                                         |
| pickle_pure_python       | 284 us                                                 | 205 us: 1.38x faster                                          |
| scimark_lu               | 110 ms                                                 | 79.4 ms: 1.38x faster                                         |
| sqlglot_transpile        | 1.54 ms                                                | 1.13 ms: 1.36x faster                                         |
| richards                 | 51.4 ms                                                | 37.8 ms: 1.36x faster                                         |
| go                       | 165 ms                                                 | 125 ms: 1.32x faster                                          |
| scimark_monte_carlo      | 72.2 ms                                                | 54.7 ms: 1.32x faster                                         |
| mako                     | 10.5 ms                                                | 8.08 ms: 1.30x faster                                         |
| pycparser                | 915 ms                                                 | 722 ms: 1.27x faster                                          |
| tornado_http             | 91.9 ms                                                | 73.0 ms: 1.26x faster                                         |
| json_dumps               | 8.38 ms                                                | 6.67 ms: 1.26x faster                                         |
| create_gc_cycles         | 876 us                                                 | 699 us: 1.25x faster                                          |
| deepcopy_memo            | 34.5 us                                                | 27.6 us: 1.25x faster                                         |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 538 ms: 1.25x faster                                          |
| spectral_norm            | 96.4 ms                                                | 78.0 ms: 1.24x faster                                         |
| nbody                    | 94.1 ms                                                | 76.2 ms: 1.24x faster                                         |
| pyflate                  | 453 ms                                                 | 368 ms: 1.23x faster                                          |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.35 sec: 1.21x faster                                        |
| logging_format           | 5.01 us                                                | 4.16 us: 1.21x faster                                         |
| logging_simple           | 4.63 us                                                | 3.87 us: 1.20x faster                                         |
| unpickle_pure_python     | 203 us                                                 | 173 us: 1.18x faster                                          |
| deepcopy                 | 278 us                                                 | 237 us: 1.17x faster                                          |
| dulwich_log              | 37.1 ms                                                | 31.8 ms: 1.17x faster                                         |
| float                    | 72.3 ms                                                | 62.0 ms: 1.17x faster                                         |
| pprint_safe_repr         | 609 ms                                                 | 522 ms: 1.16x faster                                          |
| pprint_pformat           | 1.24 sec                                               | 1.07 sec: 1.16x faster                                        |
| mypy2                    | 308 ms                                                 | 269 ms: 1.15x faster                                          |
| generators               | 32.9 ms                                                | 29.0 ms: 1.14x faster                                         |
| python_startup           | 12.6 ms                                                | 11.1 ms: 1.13x faster                                         |
| deepcopy_reduce          | 2.38 us                                                | 2.11 us: 1.13x faster                                         |
| docutils                 | 1.78 sec                                               | 1.58 sec: 1.13x faster                                        |
| regex_compile            | 96.6 ms                                                | 85.8 ms: 1.13x faster                                         |
| hexiom                   | 6.32 ms                                                | 5.67 ms: 1.12x faster                                         |
| regex_v8                 | 17.5 ms                                                | 15.8 ms: 1.11x faster                                         |
| scimark_fft              | 232 ms                                                 | 213 ms: 1.09x faster                                          |
| xml_etree_process        | 45.1 ms                                                | 41.7 ms: 1.08x faster                                         |
| python_startup_no_site   | 9.73 ms                                                | 9.05 ms: 1.07x faster                                         |
| regex_dna                | 160 ms                                                 | 150 ms: 1.06x faster                                          |
| pathlib                  | 28.8 ms                                                | 27.3 ms: 1.06x faster                                         |
| tomli_loads              | 1.76 sec                                               | 1.67 sec: 1.05x faster                                        |
| scimark_sor              | 127 ms                                                 | 120 ms: 1.05x faster                                          |
| bench_thread_pool        | 548 us                                                 | 523 us: 1.05x faster                                          |
| unpickle                 | 9.77 us                                                | 9.39 us: 1.04x faster                                         |
| json                     | 3.10 ms                                                | 2.98 ms: 1.04x faster                                         |
| sqlglot_optimize         | 38.0 ms                                                | 36.7 ms: 1.03x faster                                         |
| fannkuch                 | 317 ms                                                 | 308 ms: 1.03x faster                                          |
| gc_traversal             | 2.40 ms                                                | 2.39 ms: 1.00x faster                                         |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                          |
| nqueens                  | 68.1 ms                                                | 68.8 ms: 1.01x slower                                         |
| sqlglot_normalize        | 197 ms                                                 | 200 ms: 1.02x slower                                          |
| coroutines               | 20.2 ms                                                | 20.5 ms: 1.02x slower                                         |
| pickle                   | 7.36 us                                                | 7.50 us: 1.02x slower                                         |
| meteor_contest           | 78.6 ms                                                | 80.3 ms: 1.02x slower                                         |
| pickle_list              | 2.83 us                                                | 2.90 us: 1.02x slower                                         |
| json_loads               | 16.9 us                                                | 17.4 us: 1.03x slower                                         |
| xml_etree_parse          | 107 ms                                                 | 112 ms: 1.04x slower                                          |
| comprehensions           | 17.7 us                                                | 18.4 us: 1.04x slower                                         |
| regex_effbot             | 2.45 ms                                                | 2.56 ms: 1.05x slower                                         |
| mdp                      | 1.67 sec                                               | 1.76 sec: 1.05x slower                                        |
| xml_etree_iterparse      | 72.6 ms                                                | 78.6 ms: 1.08x slower                                         |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.77 ms: 1.08x slower                                         |
| sqlite_synth             | 1.47 us                                                | 1.61 us: 1.10x slower                                         |
| xml_etree_generate       | 54.3 ms                                                | 60.2 ms: 1.11x slower                                         |
| bench_mp_pool            | 41.0 ms                                                | 46.7 ms: 1.14x slower                                         |
| unpickle_list            | 2.66 us                                                | 3.19 us: 1.20x slower                                         |
| telco                    | 3.68 ms                                                | 4.57 ms: 1.24x slower                                         |
| coverage                 | 40.8 ms                                                | 51.1 ms: 1.25x slower                                         |
| dask                     | 258 ms                                                 | 344 ms: 1.34x slower                                          |
| async_generators         | 233 ms                                                 | 323 ms: 1.39x slower                                          |
| Geometric mean           | (ref)                                                  | 1.15x faster                                                  |

Benchmark hidden because not significant (1): pickle_dict
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x
