
# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin
- machine: darwin-arm64
- commit hash: a4921c7
- commit date: 2023-07-16
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 1.47 sec                                               | 1.52 sec: 1.04x slower                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                  |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                          |
| nbody          | 65.6 ms                                                | 69.8 ms: 1.06x slower                                         |
| float          | 53.0 ms                                                | 59.7 ms: 1.13x slower                                         |
| Geometric mean | (ref)                                                  | 1.06x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.56 ms: 1.03x faster                                         |
| regex_v8       | 16.1 ms                                                | 15.8 ms: 1.02x faster                                         |
| regex_compile  | 76.7 ms                                                | 75.3 ms: 1.02x faster                                         |
| regex_dna      | 152 ms                                                 | 150 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                  | 1.02x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.48 ms: 1.18x faster                                         |
| unpickle_pure_python | 159 us                                                 | 140 us: 1.13x faster                                          |
| pickle_pure_python   | 201 us                                                 | 180 us: 1.12x faster                                          |
| unpickle             | 9.67 us                                                | 9.38 us: 1.03x faster                                         |
| pickle_dict          | 18.0 us                                                | 17.9 us: 1.00x faster                                         |
| xml_etree_parse      | 108 ms                                                 | 109 ms: 1.01x slower                                          |
| pickle_list          | 2.81 us                                                | 2.89 us: 1.03x slower                                         |
| pickle               | 7.15 us                                                | 7.47 us: 1.04x slower                                         |
| xml_etree_iterparse  | 70.1 ms                                                | 73.7 ms: 1.05x slower                                         |
| tomli_loads          | 1.47 sec                                               | 1.54 sec: 1.05x slower                                        |
| xml_etree_process    | 35.1 ms                                                | 37.8 ms: 1.08x slower                                         |
| json_loads           | 16.1 us                                                | 17.7 us: 1.10x slower                                         |
| xml_etree_generate   | 48.3 ms                                                | 55.9 ms: 1.16x slower                                         |
| unpickle_list        | 2.65 us                                                | 3.27 us: 1.23x slower                                         |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 12.7 ms: 1.02x slower                                         |
| python_startup_no_site | 10.2 ms                                                | 10.6 ms: 1.04x slower                                         |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 8.53 ms                                                | 8.57 ms: 1.00x slower                                         |

All benchmarks:
===============

| Benchmark                | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                 | 87.9 us: 3.82x faster                                         |
| asyncio_tcp              | 651 ms                                                 | 452 ms: 1.44x faster                                          |
| unpack_sequence          | 34.1 ns                                                | 27.4 ns: 1.25x faster                                         |
| richards_super           | 39.2 ms                                                | 33.1 ms: 1.18x faster                                         |
| json_dumps               | 7.63 ms                                                | 6.48 ms: 1.18x faster                                         |
| coverage                 | 58.4 ms                                                | 50.0 ms: 1.17x faster                                         |
| deltablue                | 2.81 ms                                                | 2.43 ms: 1.16x faster                                         |
| asyncio_tcp_ssl          | 1.44 sec                                               | 1.25 sec: 1.15x faster                                        |
| generators               | 28.8 ms                                                | 25.3 ms: 1.14x faster                                         |
| unpickle_pure_python     | 159 us                                                 | 140 us: 1.13x faster                                          |
| hexiom                   | 4.72 ms                                                | 4.18 ms: 1.13x faster                                         |
| pickle_pure_python       | 201 us                                                 | 180 us: 1.12x faster                                          |
| chaos                    | 49.4 ms                                                | 44.3 ms: 1.12x faster                                         |
| sqlglot_parse            | 959 us                                                 | 872 us: 1.10x faster                                          |
| richards                 | 32.2 ms                                                | 29.7 ms: 1.09x faster                                         |
| sqlglot_transpile        | 1.12 ms                                                | 1.04 ms: 1.08x faster                                         |
| coroutines               | 17.8 ms                                                | 16.7 ms: 1.06x faster                                         |
| pycparser                | 698 ms                                                 | 662 ms: 1.05x faster                                          |
| logging_silent           | 68.1 ns                                                | 65.2 ns: 1.04x faster                                         |
| go                       | 109 ms                                                 | 104 ms: 1.04x faster                                          |
| unpickle                 | 9.67 us                                                | 9.38 us: 1.03x faster                                         |
| create_gc_cycles         | 716 us                                                 | 695 us: 1.03x faster                                          |
| scimark_sor              | 82.6 ms                                                | 80.4 ms: 1.03x faster                                         |
| async_tree_none          | 286 ms                                                 | 278 ms: 1.03x faster                                          |
| regex_effbot             | 2.63 ms                                                | 2.56 ms: 1.03x faster                                         |
| async_tree_memoization   | 336 ms                                                 | 327 ms: 1.03x faster                                          |
| regex_v8                 | 16.1 ms                                                | 15.8 ms: 1.02x faster                                         |
| regex_compile            | 76.7 ms                                                | 75.3 ms: 1.02x faster                                         |
| dulwich_log              | 30.3 ms                                                | 29.8 ms: 1.02x faster                                         |
| logging_simple           | 3.55 us                                                | 3.50 us: 1.01x faster                                         |
| regex_dna                | 152 ms                                                 | 150 ms: 1.01x faster                                          |
| meteor_contest           | 73.5 ms                                                | 72.7 ms: 1.01x faster                                         |
| gc_traversal             | 2.42 ms                                                | 2.39 ms: 1.01x faster                                         |
| pickle_dict              | 18.0 us                                                | 17.9 us: 1.00x faster                                         |
| logging_format           | 3.78 us                                                | 3.77 us: 1.00x faster                                         |
| pidigits                 | 281 ms                                                 | 282 ms: 1.00x slower                                          |
| mako                     | 8.53 ms                                                | 8.57 ms: 1.00x slower                                         |
| nqueens                  | 59.8 ms                                                | 60.2 ms: 1.01x slower                                         |
| spectral_norm            | 72.6 ms                                                | 73.1 ms: 1.01x slower                                         |
| xml_etree_parse          | 108 ms                                                 | 109 ms: 1.01x slower                                          |
| async_tree_cpu_io_mixed  | 533 ms                                                 | 543 ms: 1.02x slower                                          |
| python_startup           | 12.4 ms                                                | 12.7 ms: 1.02x slower                                         |
| bench_thread_pool        | 474 us                                                 | 484 us: 1.02x slower                                          |
| scimark_fft              | 200 ms                                                 | 205 ms: 1.03x slower                                          |
| pickle_list              | 2.81 us                                                | 2.89 us: 1.03x slower                                         |
| pprint_pformat           | 954 ms                                                 | 981 ms: 1.03x slower                                          |
| crypto_pyaes             | 51.7 ms                                                | 53.3 ms: 1.03x slower                                         |
| comprehensions           | 16.1 us                                                | 16.6 us: 1.03x slower                                         |
| docutils                 | 1.47 sec                                               | 1.52 sec: 1.04x slower                                        |
| python_startup_no_site   | 10.2 ms                                                | 10.6 ms: 1.04x slower                                         |
| pickle                   | 7.15 us                                                | 7.47 us: 1.04x slower                                         |
| pprint_safe_repr         | 466 ms                                                 | 489 ms: 1.05x slower                                          |
| xml_etree_iterparse      | 70.1 ms                                                | 73.7 ms: 1.05x slower                                         |
| scimark_monte_carlo      | 46.5 ms                                                | 48.8 ms: 1.05x slower                                         |
| tomli_loads              | 1.47 sec                                               | 1.54 sec: 1.05x slower                                        |
| sqlglot_normalize        | 171 ms                                                 | 181 ms: 1.06x slower                                          |
| mdp                      | 1.55 sec                                               | 1.64 sec: 1.06x slower                                        |
| nbody                    | 65.6 ms                                                | 69.8 ms: 1.06x slower                                         |
| scimark_lu               | 73.3 ms                                                | 78.1 ms: 1.06x slower                                         |
| deepcopy_reduce          | 1.91 us                                                | 2.03 us: 1.06x slower                                         |
| bench_mp_pool            | 43.9 ms                                                | 47.1 ms: 1.07x slower                                         |
| json                     | 2.78 ms                                                | 2.98 ms: 1.07x slower                                         |
| sqlglot_optimize         | 31.1 ms                                                | 33.5 ms: 1.08x slower                                         |
| xml_etree_process        | 35.1 ms                                                | 37.8 ms: 1.08x slower                                         |
| scimark_sparse_mat_mult  | 3.19 ms                                                | 3.48 ms: 1.09x slower                                         |
| pyflate                  | 310 ms                                                 | 339 ms: 1.09x slower                                          |
| json_loads               | 16.1 us                                                | 17.7 us: 1.10x slower                                         |
| fannkuch                 | 261 ms                                                 | 292 ms: 1.12x slower                                          |
| float                    | 53.0 ms                                                | 59.7 ms: 1.13x slower                                         |
| deepcopy_memo            | 26.3 us                                                | 29.7 us: 1.13x slower                                         |
| telco                    | 3.41 ms                                                | 3.85 ms: 1.13x slower                                         |
| raytrace                 | 207 ms                                                 | 239 ms: 1.16x slower                                          |
| xml_etree_generate       | 48.3 ms                                                | 55.9 ms: 1.16x slower                                         |
| sqlite_synth             | 1.27 us                                                | 1.57 us: 1.23x slower                                         |
| unpickle_list            | 2.65 us                                                | 3.27 us: 1.23x slower                                         |
| pathlib                  | 27.2 ms                                                | 33.7 ms: 1.24x slower                                         |
| mypy2                    | 195 ms                                                 | 258 ms: 1.32x slower                                          |
| async_generators         | 196 ms                                                 | 306 ms: 1.56x slower                                          |
| Geometric mean           | (ref)                                                  | 1.01x faster                                                  |

Benchmark hidden because not significant (3): tornado_http, async_tree_io, deepcopy
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
Ignored benchmarks (1) of results/bm-20230716-3.13.0a0-a4921c7/bm-20230716-darwin-arm64-brandtbucher-justin-3.13.0a0-a4921c7.json: dask
