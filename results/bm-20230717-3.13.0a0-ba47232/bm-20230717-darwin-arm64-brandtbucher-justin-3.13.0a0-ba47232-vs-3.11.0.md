
# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin
- machine: darwin-arm64
- commit hash: ba47232
- commit date: 2023-07-17
- overall geometric mean: 1.00x faster
- HPT reliability: 98.36%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 1.47 sec                                               | 1.54 sec: 1.04x slower                                        |
| Geometric mean | (ref)                                                  | 1.02x slower                                                  |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                          |
| nbody          | 65.6 ms                                                | 69.4 ms: 1.06x slower                                         |
| float          | 53.0 ms                                                | 57.6 ms: 1.09x slower                                         |
| Geometric mean | (ref)                                                  | 1.05x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.56 ms: 1.03x faster                                         |
| regex_dna      | 152 ms                                                 | 150 ms: 1.01x faster                                          |
| regex_v8       | 16.1 ms                                                | 15.9 ms: 1.01x faster                                         |
| regex_compile  | 76.7 ms                                                | 75.9 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.44 ms: 1.18x faster                                         |
| unpickle_pure_python | 159 us                                                 | 143 us: 1.11x faster                                          |
| pickle_pure_python   | 201 us                                                 | 183 us: 1.09x faster                                          |
| unpickle             | 9.67 us                                                | 9.31 us: 1.04x faster                                         |
| pickle_dict          | 18.0 us                                                | 18.1 us: 1.01x slower                                         |
| pickle_list          | 2.81 us                                                | 2.88 us: 1.02x slower                                         |
| xml_etree_parse      | 108 ms                                                 | 111 ms: 1.03x slower                                          |
| tomli_loads          | 1.47 sec                                               | 1.52 sec: 1.04x slower                                        |
| pickle               | 7.15 us                                                | 7.44 us: 1.04x slower                                         |
| xml_etree_iterparse  | 70.1 ms                                                | 74.4 ms: 1.06x slower                                         |
| xml_etree_process    | 35.1 ms                                                | 38.2 ms: 1.09x slower                                         |
| json_loads           | 16.1 us                                                | 17.6 us: 1.09x slower                                         |
| xml_etree_generate   | 48.3 ms                                                | 56.0 ms: 1.16x slower                                         |
| unpickle_list        | 2.65 us                                                | 3.25 us: 1.22x slower                                         |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 12.7 ms: 1.02x slower                                         |
| python_startup_no_site | 10.2 ms                                                | 10.5 ms: 1.04x slower                                         |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 8.53 ms                                                | 8.10 ms: 1.05x faster                                         |

All benchmarks:
===============

| Benchmark                | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                 | 88.8 us: 3.78x faster                                         |
| asyncio_tcp              | 651 ms                                                 | 431 ms: 1.51x faster                                          |
| unpack_sequence          | 34.1 ns                                                | 27.2 ns: 1.25x faster                                         |
| json_dumps               | 7.63 ms                                                | 6.44 ms: 1.18x faster                                         |
| richards_super           | 39.2 ms                                                | 33.5 ms: 1.17x faster                                         |
| generators               | 28.8 ms                                                | 24.8 ms: 1.16x faster                                         |
| coverage                 | 58.4 ms                                                | 50.4 ms: 1.16x faster                                         |
| asyncio_tcp_ssl          | 1.44 sec                                               | 1.27 sec: 1.14x faster                                        |
| deltablue                | 2.81 ms                                                | 2.50 ms: 1.13x faster                                         |
| hexiom                   | 4.72 ms                                                | 4.23 ms: 1.12x faster                                         |
| chaos                    | 49.4 ms                                                | 44.3 ms: 1.11x faster                                         |
| unpickle_pure_python     | 159 us                                                 | 143 us: 1.11x faster                                          |
| pickle_pure_python       | 201 us                                                 | 183 us: 1.09x faster                                          |
| richards                 | 32.2 ms                                                | 29.8 ms: 1.08x faster                                         |
| sqlglot_parse            | 959 us                                                 | 888 us: 1.08x faster                                          |
| sqlglot_transpile        | 1.12 ms                                                | 1.07 ms: 1.05x faster                                         |
| mako                     | 8.53 ms                                                | 8.10 ms: 1.05x faster                                         |
| pycparser                | 698 ms                                                 | 664 ms: 1.05x faster                                          |
| unpickle                 | 9.67 us                                                | 9.31 us: 1.04x faster                                         |
| go                       | 109 ms                                                 | 105 ms: 1.04x faster                                          |
| logging_silent           | 68.1 ns                                                | 65.8 ns: 1.04x faster                                         |
| coroutines               | 17.8 ms                                                | 17.2 ms: 1.04x faster                                         |
| async_tree_none          | 286 ms                                                 | 276 ms: 1.03x faster                                          |
| async_tree_memoization   | 336 ms                                                 | 326 ms: 1.03x faster                                          |
| create_gc_cycles         | 716 us                                                 | 696 us: 1.03x faster                                          |
| regex_effbot             | 2.63 ms                                                | 2.56 ms: 1.03x faster                                         |
| regex_dna                | 152 ms                                                 | 150 ms: 1.01x faster                                          |
| regex_v8                 | 16.1 ms                                                | 15.9 ms: 1.01x faster                                         |
| regex_compile            | 76.7 ms                                                | 75.9 ms: 1.01x faster                                         |
| gc_traversal             | 2.42 ms                                                | 2.40 ms: 1.01x faster                                         |
| meteor_contest           | 73.5 ms                                                | 73.3 ms: 1.00x faster                                         |
| scimark_lu               | 73.3 ms                                                | 73.5 ms: 1.00x slower                                         |
| pidigits                 | 281 ms                                                 | 282 ms: 1.00x slower                                          |
| pickle_dict              | 18.0 us                                                | 18.1 us: 1.01x slower                                         |
| nqueens                  | 59.8 ms                                                | 60.4 ms: 1.01x slower                                         |
| async_tree_cpu_io_mixed  | 533 ms                                                 | 541 ms: 1.01x slower                                          |
| spectral_norm            | 72.6 ms                                                | 73.8 ms: 1.02x slower                                         |
| bench_thread_pool        | 474 us                                                 | 484 us: 1.02x slower                                          |
| python_startup           | 12.4 ms                                                | 12.7 ms: 1.02x slower                                         |
| pickle_list              | 2.81 us                                                | 2.88 us: 1.02x slower                                         |
| deepcopy                 | 223 us                                                 | 228 us: 1.02x slower                                          |
| xml_etree_parse          | 108 ms                                                 | 111 ms: 1.03x slower                                          |
| crypto_pyaes             | 51.7 ms                                                | 53.2 ms: 1.03x slower                                         |
| scimark_fft              | 200 ms                                                 | 205 ms: 1.03x slower                                          |
| logging_simple           | 3.55 us                                                | 3.67 us: 1.04x slower                                         |
| python_startup_no_site   | 10.2 ms                                                | 10.5 ms: 1.04x slower                                         |
| pprint_pformat           | 954 ms                                                 | 989 ms: 1.04x slower                                          |
| tomli_loads              | 1.47 sec                                               | 1.52 sec: 1.04x slower                                        |
| pickle                   | 7.15 us                                                | 7.44 us: 1.04x slower                                         |
| logging_format           | 3.78 us                                                | 3.95 us: 1.04x slower                                         |
| docutils                 | 1.47 sec                                               | 1.54 sec: 1.04x slower                                        |
| pprint_safe_repr         | 466 ms                                                 | 488 ms: 1.05x slower                                          |
| nbody                    | 65.6 ms                                                | 69.4 ms: 1.06x slower                                         |
| xml_etree_iterparse      | 70.1 ms                                                | 74.4 ms: 1.06x slower                                         |
| scimark_monte_carlo      | 46.5 ms                                                | 49.4 ms: 1.06x slower                                         |
| mdp                      | 1.55 sec                                               | 1.64 sec: 1.06x slower                                        |
| fannkuch                 | 261 ms                                                 | 279 ms: 1.07x slower                                          |
| deepcopy_memo            | 26.3 us                                                | 28.2 us: 1.07x slower                                         |
| deepcopy_reduce          | 1.91 us                                                | 2.05 us: 1.07x slower                                         |
| sqlglot_normalize        | 171 ms                                                 | 183 ms: 1.07x slower                                          |
| bench_mp_pool            | 43.9 ms                                                | 47.3 ms: 1.08x slower                                         |
| json                     | 2.78 ms                                                | 3.00 ms: 1.08x slower                                         |
| pyflate                  | 310 ms                                                 | 336 ms: 1.08x slower                                          |
| float                    | 53.0 ms                                                | 57.6 ms: 1.09x slower                                         |
| xml_etree_process        | 35.1 ms                                                | 38.2 ms: 1.09x slower                                         |
| json_loads               | 16.1 us                                                | 17.6 us: 1.09x slower                                         |
| sqlglot_optimize         | 31.1 ms                                                | 34.0 ms: 1.09x slower                                         |
| scimark_sparse_mat_mult  | 3.19 ms                                                | 3.54 ms: 1.11x slower                                         |
| scimark_sor              | 82.6 ms                                                | 92.0 ms: 1.11x slower                                         |
| telco                    | 3.41 ms                                                | 3.84 ms: 1.13x slower                                         |
| xml_etree_generate       | 48.3 ms                                                | 56.0 ms: 1.16x slower                                         |
| raytrace                 | 207 ms                                                 | 242 ms: 1.17x slower                                          |
| unpickle_list            | 2.65 us                                                | 3.25 us: 1.22x slower                                         |
| sqlite_synth             | 1.27 us                                                | 1.57 us: 1.24x slower                                         |
| pathlib                  | 27.2 ms                                                | 33.9 ms: 1.25x slower                                         |
| mypy2                    | 195 ms                                                 | 259 ms: 1.33x slower                                          |
| async_generators         | 196 ms                                                 | 307 ms: 1.56x slower                                          |
| Geometric mean           | (ref)                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (4): async_tree_io, tornado_http, comprehensions, dulwich_log
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
Ignored benchmarks (1) of results/bm-20230717-3.13.0a0-ba47232/bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232.json: dask


# HPT report

- Reliability score: 98.36% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
