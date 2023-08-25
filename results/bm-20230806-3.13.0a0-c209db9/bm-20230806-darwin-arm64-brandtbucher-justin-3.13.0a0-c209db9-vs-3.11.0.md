
# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin
- machine: darwin-arm64
- commit hash: c209db9
- commit date: 2023-08-06
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 1.47 sec                                               | 1.58 sec: 1.07x slower                                        |
| Geometric mean | (ref)                                                  | 1.05x slower                                                  |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                          |
| nbody          | 65.6 ms                                                | 76.2 ms: 1.16x slower                                         |
| float          | 53.0 ms                                                | 62.0 ms: 1.17x slower                                         |
| Geometric mean | (ref)                                                  | 1.11x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.56 ms: 1.03x faster                                         |
| regex_v8       | 16.1 ms                                                | 15.8 ms: 1.02x faster                                         |
| regex_dna      | 152 ms                                                 | 150 ms: 1.01x faster                                          |
| regex_compile  | 76.7 ms                                                | 85.8 ms: 1.12x slower                                         |
| Geometric mean | (ref)                                                  | 1.01x slower                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.67 ms: 1.14x faster                                         |
| unpickle             | 9.67 us                                                | 9.39 us: 1.03x faster                                         |
| pickle_dict          | 18.0 us                                                | 17.8 us: 1.01x faster                                         |
| pickle_pure_python   | 201 us                                                 | 205 us: 1.02x slower                                          |
| pickle_list          | 2.81 us                                                | 2.90 us: 1.03x slower                                         |
| xml_etree_parse      | 108 ms                                                 | 112 ms: 1.03x slower                                          |
| pickle               | 7.15 us                                                | 7.50 us: 1.05x slower                                         |
| json_loads           | 16.1 us                                                | 17.4 us: 1.08x slower                                         |
| unpickle_pure_python | 159 us                                                 | 173 us: 1.09x slower                                          |
| xml_etree_iterparse  | 70.1 ms                                                | 78.6 ms: 1.12x slower                                         |
| tomli_loads          | 1.47 sec                                               | 1.67 sec: 1.14x slower                                        |
| xml_etree_process    | 35.1 ms                                                | 41.7 ms: 1.19x slower                                         |
| unpickle_list        | 2.65 us                                                | 3.19 us: 1.21x slower                                         |
| xml_etree_generate   | 48.3 ms                                                | 60.2 ms: 1.25x slower                                         |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 9.05 ms: 1.12x faster                                         |
| python_startup         | 12.4 ms                                                | 11.1 ms: 1.12x faster                                         |
| Geometric mean         | (ref)                                                  | 1.12x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 8.53 ms                                                | 8.08 ms: 1.06x faster                                         |

All benchmarks:
===============

| Benchmark                | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                 | 97.2 us: 3.46x faster                                         |
| asyncio_tcp              | 651 ms                                                 | 421 ms: 1.55x faster                                          |
| unpack_sequence          | 34.1 ns                                                | 27.9 ns: 1.22x faster                                         |
| json_dumps               | 7.63 ms                                                | 6.67 ms: 1.14x faster                                         |
| coverage                 | 58.4 ms                                                | 51.1 ms: 1.14x faster                                         |
| python_startup_no_site   | 10.2 ms                                                | 9.05 ms: 1.12x faster                                         |
| python_startup           | 12.4 ms                                                | 11.1 ms: 1.12x faster                                         |
| asyncio_tcp_ssl          | 1.44 sec                                               | 1.35 sec: 1.06x faster                                        |
| mako                     | 8.53 ms                                                | 8.08 ms: 1.06x faster                                         |
| chaos                    | 49.4 ms                                                | 46.9 ms: 1.05x faster                                         |
| crypto_pyaes             | 51.7 ms                                                | 49.5 ms: 1.05x faster                                         |
| async_tree_none          | 286 ms                                                 | 276 ms: 1.03x faster                                          |
| async_tree_memoization   | 336 ms                                                 | 325 ms: 1.03x faster                                          |
| async_tree_io            | 704 ms                                                 | 683 ms: 1.03x faster                                          |
| unpickle                 | 9.67 us                                                | 9.39 us: 1.03x faster                                         |
| regex_effbot             | 2.63 ms                                                | 2.56 ms: 1.03x faster                                         |
| create_gc_cycles         | 716 us                                                 | 699 us: 1.02x faster                                          |
| regex_v8                 | 16.1 ms                                                | 15.8 ms: 1.02x faster                                         |
| sqlglot_parse            | 959 us                                                 | 945 us: 1.02x faster                                          |
| regex_dna                | 152 ms                                                 | 150 ms: 1.01x faster                                          |
| gc_traversal             | 2.42 ms                                                | 2.39 ms: 1.01x faster                                         |
| pickle_dict              | 18.0 us                                                | 17.8 us: 1.01x faster                                         |
| pidigits                 | 281 ms                                                 | 282 ms: 1.00x slower                                          |
| sqlglot_transpile        | 1.12 ms                                                | 1.13 ms: 1.01x slower                                         |
| generators               | 28.8 ms                                                | 29.0 ms: 1.01x slower                                         |
| async_tree_cpu_io_mixed  | 533 ms                                                 | 538 ms: 1.01x slower                                          |
| pickle_pure_python       | 201 us                                                 | 205 us: 1.02x slower                                          |
| pickle_list              | 2.81 us                                                | 2.90 us: 1.03x slower                                         |
| xml_etree_parse          | 108 ms                                                 | 112 ms: 1.03x slower                                          |
| pycparser                | 698 ms                                                 | 722 ms: 1.04x slower                                          |
| deltablue                | 2.81 ms                                                | 2.93 ms: 1.04x slower                                         |
| dulwich_log              | 30.3 ms                                                | 31.8 ms: 1.05x slower                                         |
| pickle                   | 7.15 us                                                | 7.50 us: 1.05x slower                                         |
| deepcopy_memo            | 26.3 us                                                | 27.6 us: 1.05x slower                                         |
| richards_super           | 39.2 ms                                                | 41.5 ms: 1.06x slower                                         |
| deepcopy                 | 223 us                                                 | 237 us: 1.06x slower                                          |
| bench_mp_pool            | 43.9 ms                                                | 46.7 ms: 1.06x slower                                         |
| scimark_fft              | 200 ms                                                 | 213 ms: 1.07x slower                                          |
| json                     | 2.78 ms                                                | 2.98 ms: 1.07x slower                                         |
| docutils                 | 1.47 sec                                               | 1.58 sec: 1.07x slower                                        |
| spectral_norm            | 72.6 ms                                                | 78.0 ms: 1.07x slower                                         |
| json_loads               | 16.1 us                                                | 17.4 us: 1.08x slower                                         |
| scimark_lu               | 73.3 ms                                                | 79.4 ms: 1.08x slower                                         |
| unpickle_pure_python     | 159 us                                                 | 173 us: 1.09x slower                                          |
| logging_simple           | 3.55 us                                                | 3.87 us: 1.09x slower                                         |
| meteor_contest           | 73.5 ms                                                | 80.3 ms: 1.09x slower                                         |
| logging_format           | 3.78 us                                                | 4.16 us: 1.10x slower                                         |
| bench_thread_pool        | 474 us                                                 | 523 us: 1.10x slower                                          |
| deepcopy_reduce          | 1.91 us                                                | 2.11 us: 1.10x slower                                         |
| regex_compile            | 76.7 ms                                                | 85.8 ms: 1.12x slower                                         |
| pprint_pformat           | 954 ms                                                 | 1.07 sec: 1.12x slower                                        |
| pprint_safe_repr         | 466 ms                                                 | 522 ms: 1.12x slower                                          |
| xml_etree_iterparse      | 70.1 ms                                                | 78.6 ms: 1.12x slower                                         |
| raytrace                 | 207 ms                                                 | 233 ms: 1.13x slower                                          |
| mdp                      | 1.55 sec                                               | 1.76 sec: 1.14x slower                                        |
| comprehensions           | 16.1 us                                                | 18.4 us: 1.14x slower                                         |
| logging_silent           | 68.1 ns                                                | 77.8 ns: 1.14x slower                                         |
| tomli_loads              | 1.47 sec                                               | 1.67 sec: 1.14x slower                                        |
| go                       | 109 ms                                                 | 125 ms: 1.15x slower                                          |
| nqueens                  | 59.8 ms                                                | 68.8 ms: 1.15x slower                                         |
| coroutines               | 17.8 ms                                                | 20.5 ms: 1.16x slower                                         |
| nbody                    | 65.6 ms                                                | 76.2 ms: 1.16x slower                                         |
| sqlglot_normalize        | 171 ms                                                 | 200 ms: 1.17x slower                                          |
| float                    | 53.0 ms                                                | 62.0 ms: 1.17x slower                                         |
| richards                 | 32.2 ms                                                | 37.8 ms: 1.17x slower                                         |
| scimark_monte_carlo      | 46.5 ms                                                | 54.7 ms: 1.18x slower                                         |
| fannkuch                 | 261 ms                                                 | 308 ms: 1.18x slower                                          |
| scimark_sparse_mat_mult  | 3.19 ms                                                | 3.77 ms: 1.18x slower                                         |
| sqlglot_optimize         | 31.1 ms                                                | 36.7 ms: 1.18x slower                                         |
| pyflate                  | 310 ms                                                 | 368 ms: 1.19x slower                                          |
| xml_etree_process        | 35.1 ms                                                | 41.7 ms: 1.19x slower                                         |
| hexiom                   | 4.72 ms                                                | 5.67 ms: 1.20x slower                                         |
| unpickle_list            | 2.65 us                                                | 3.19 us: 1.21x slower                                         |
| xml_etree_generate       | 48.3 ms                                                | 60.2 ms: 1.25x slower                                         |
| sqlite_synth             | 1.27 us                                                | 1.61 us: 1.27x slower                                         |
| telco                    | 3.41 ms                                                | 4.57 ms: 1.34x slower                                         |
| mypy2                    | 195 ms                                                 | 269 ms: 1.38x slower                                          |
| scimark_sor              | 82.6 ms                                                | 120 ms: 1.46x slower                                          |
| async_generators         | 196 ms                                                 | 323 ms: 1.65x slower                                          |
| Geometric mean           | (ref)                                                  | 1.05x slower                                                  |

Benchmark hidden because not significant (2): pathlib, tornado_http
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
Ignored benchmarks (1) of results/bm-20230806-3.13.0a0-c209db9/bm-20230806-darwin-arm64-brandtbucher-justin-3.13.0a0-c209db9.json: dask


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x
