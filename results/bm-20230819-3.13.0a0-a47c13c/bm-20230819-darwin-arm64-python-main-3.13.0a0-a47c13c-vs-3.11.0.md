
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: a47c13c
- commit date: 2023-08-19
- overall geometric mean: 1.01x slower
- HPT reliability: 99.24%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-darwin-arm64-python-main-3.13.0a0-a47c13c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 1.47 sec                                               | 1.53 sec: 1.04x slower                                |
| Geometric mean | (ref)                                                  | 1.02x slower                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-darwin-arm64-python-main-3.13.0a0-a47c13c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 281 ms                                                 | 281 ms: 1.00x slower                                  |
| float          | 53.0 ms                                                | 56.4 ms: 1.07x slower                                 |
| nbody          | 65.6 ms                                                | 72.3 ms: 1.10x slower                                 |
| Geometric mean | (ref)                                                  | 1.06x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-darwin-arm64-python-main-3.13.0a0-a47c13c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.57 ms: 1.02x faster                                 |
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                  |
| regex_compile  | 76.7 ms                                                | 79.1 ms: 1.03x slower                                 |
| regex_v8       | 16.1 ms                                                | 17.0 ms: 1.05x slower                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-darwin-arm64-python-main-3.13.0a0-a47c13c |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.58 ms: 1.16x faster                                 |
| unpickle             | 9.67 us                                                | 9.17 us: 1.05x faster                                 |
| pickle_pure_python   | 201 us                                                 | 198 us: 1.01x faster                                  |
| xml_etree_parse      | 108 ms                                                 | 110 ms: 1.01x slower                                  |
| unpickle_pure_python | 159 us                                                 | 163 us: 1.02x slower                                  |
| pickle_list          | 2.81 us                                                | 2.90 us: 1.03x slower                                 |
| pickle               | 7.15 us                                                | 7.41 us: 1.04x slower                                 |
| tomli_loads          | 1.47 sec                                               | 1.57 sec: 1.07x slower                                |
| json_loads           | 16.1 us                                                | 17.4 us: 1.08x slower                                 |
| xml_etree_iterparse  | 70.1 ms                                                | 76.5 ms: 1.09x slower                                 |
| xml_etree_process    | 35.1 ms                                                | 40.7 ms: 1.16x slower                                 |
| unpickle_list        | 2.65 us                                                | 3.14 us: 1.19x slower                                 |
| xml_etree_generate   | 48.3 ms                                                | 59.0 ms: 1.22x slower                                 |
| Geometric mean       | (ref)                                                  | 1.05x slower                                          |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-darwin-arm64-python-main-3.13.0a0-a47c13c |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 9.18 ms: 1.11x faster                                 |
| python_startup         | 12.4 ms                                                | 11.3 ms: 1.10x faster                                 |
| Geometric mean         | (ref)                                                  | 1.10x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-darwin-arm64-python-main-3.13.0a0-a47c13c |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 8.53 ms                                                | 7.54 ms: 1.13x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230819-darwin-arm64-python-main-3.13.0a0-a47c13c |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                 | 94.1 us: 3.57x faster                                 |
| asyncio_tcp              | 651 ms                                                 | 405 ms: 1.61x faster                                  |
| unpack_sequence          | 34.1 ns                                                | 27.5 ns: 1.24x faster                                 |
| coverage                 | 58.4 ms                                                | 47.5 ms: 1.23x faster                                 |
| chaos                    | 49.4 ms                                                | 42.2 ms: 1.17x faster                                 |
| json_dumps               | 7.63 ms                                                | 6.58 ms: 1.16x faster                                 |
| sqlglot_parse            | 959 us                                                 | 827 us: 1.16x faster                                  |
| mako                     | 8.53 ms                                                | 7.54 ms: 1.13x faster                                 |
| sqlglot_transpile        | 1.12 ms                                                | 1.01 ms: 1.12x faster                                 |
| async_tree_none          | 286 ms                                                 | 257 ms: 1.11x faster                                  |
| python_startup_no_site   | 10.2 ms                                                | 9.18 ms: 1.11x faster                                 |
| deltablue                | 2.81 ms                                                | 2.54 ms: 1.11x faster                                 |
| python_startup           | 12.4 ms                                                | 11.3 ms: 1.10x faster                                 |
| raytrace                 | 207 ms                                                 | 189 ms: 1.09x faster                                  |
| crypto_pyaes             | 51.7 ms                                                | 47.9 ms: 1.08x faster                                 |
| comprehensions           | 16.1 us                                                | 15.0 us: 1.07x faster                                 |
| asyncio_tcp_ssl          | 1.44 sec                                               | 1.36 sec: 1.06x faster                                |
| deepcopy_memo            | 26.3 us                                                | 24.9 us: 1.06x faster                                 |
| unpickle                 | 9.67 us                                                | 9.17 us: 1.05x faster                                 |
| create_gc_cycles         | 716 us                                                 | 698 us: 1.02x faster                                  |
| regex_effbot             | 2.63 ms                                                | 2.57 ms: 1.02x faster                                 |
| regex_dna                | 152 ms                                                 | 149 ms: 1.02x faster                                  |
| generators               | 28.8 ms                                                | 28.2 ms: 1.02x faster                                 |
| scimark_sparse_mat_mult  | 3.19 ms                                                | 3.13 ms: 1.02x faster                                 |
| nqueens                  | 59.8 ms                                                | 59.0 ms: 1.01x faster                                 |
| pickle_pure_python       | 201 us                                                 | 198 us: 1.01x faster                                  |
| async_tree_cpu_io_mixed  | 533 ms                                                 | 528 ms: 1.01x faster                                  |
| gc_traversal             | 2.42 ms                                                | 2.39 ms: 1.01x faster                                 |
| go                       | 109 ms                                                 | 108 ms: 1.01x faster                                  |
| pidigits                 | 281 ms                                                 | 281 ms: 1.00x slower                                  |
| richards_super           | 39.2 ms                                                | 39.5 ms: 1.01x slower                                 |
| async_tree_io            | 704 ms                                                 | 709 ms: 1.01x slower                                  |
| scimark_fft              | 200 ms                                                 | 202 ms: 1.01x slower                                  |
| meteor_contest           | 73.5 ms                                                | 74.5 ms: 1.01x slower                                 |
| xml_etree_parse          | 108 ms                                                 | 110 ms: 1.01x slower                                  |
| spectral_norm            | 72.6 ms                                                | 74.2 ms: 1.02x slower                                 |
| unpickle_pure_python     | 159 us                                                 | 163 us: 1.02x slower                                  |
| dulwich_log              | 30.3 ms                                                | 31.1 ms: 1.03x slower                                 |
| regex_compile            | 76.7 ms                                                | 79.1 ms: 1.03x slower                                 |
| hexiom                   | 4.72 ms                                                | 4.87 ms: 1.03x slower                                 |
| deepcopy                 | 223 us                                                 | 230 us: 1.03x slower                                  |
| pickle_list              | 2.81 us                                                | 2.90 us: 1.03x slower                                 |
| bench_mp_pool            | 43.9 ms                                                | 45.4 ms: 1.03x slower                                 |
| pathlib                  | 27.2 ms                                                | 28.2 ms: 1.03x slower                                 |
| bench_thread_pool        | 474 us                                                 | 491 us: 1.04x slower                                  |
| pickle                   | 7.15 us                                                | 7.41 us: 1.04x slower                                 |
| scimark_lu               | 73.3 ms                                                | 76.2 ms: 1.04x slower                                 |
| docutils                 | 1.47 sec                                               | 1.53 sec: 1.04x slower                                |
| regex_v8                 | 16.1 ms                                                | 17.0 ms: 1.05x slower                                 |
| mdp                      | 1.55 sec                                               | 1.64 sec: 1.06x slower                                |
| float                    | 53.0 ms                                                | 56.4 ms: 1.07x slower                                 |
| logging_simple           | 3.55 us                                                | 3.80 us: 1.07x slower                                 |
| tomli_loads              | 1.47 sec                                               | 1.57 sec: 1.07x slower                                |
| deepcopy_reduce          | 1.91 us                                                | 2.06 us: 1.08x slower                                 |
| logging_silent           | 68.1 ns                                                | 73.6 ns: 1.08x slower                                 |
| json_loads               | 16.1 us                                                | 17.4 us: 1.08x slower                                 |
| json                     | 2.78 ms                                                | 3.01 ms: 1.09x slower                                 |
| logging_format           | 3.78 us                                                | 4.12 us: 1.09x slower                                 |
| xml_etree_iterparse      | 70.1 ms                                                | 76.5 ms: 1.09x slower                                 |
| pprint_pformat           | 954 ms                                                 | 1.04 sec: 1.09x slower                                |
| coroutines               | 17.8 ms                                                | 19.4 ms: 1.09x slower                                 |
| fannkuch                 | 261 ms                                                 | 286 ms: 1.09x slower                                  |
| pprint_safe_repr         | 466 ms                                                 | 514 ms: 1.10x slower                                  |
| nbody                    | 65.6 ms                                                | 72.3 ms: 1.10x slower                                 |
| sqlglot_normalize        | 171 ms                                                 | 191 ms: 1.12x slower                                  |
| richards                 | 32.2 ms                                                | 36.1 ms: 1.12x slower                                 |
| pyflate                  | 310 ms                                                 | 348 ms: 1.12x slower                                  |
| sqlglot_optimize         | 31.1 ms                                                | 35.2 ms: 1.13x slower                                 |
| xml_etree_process        | 35.1 ms                                                | 40.7 ms: 1.16x slower                                 |
| unpickle_list            | 2.65 us                                                | 3.14 us: 1.19x slower                                 |
| xml_etree_generate       | 48.3 ms                                                | 59.0 ms: 1.22x slower                                 |
| sqlite_synth             | 1.27 us                                                | 1.62 us: 1.27x slower                                 |
| scimark_sor              | 82.6 ms                                                | 108 ms: 1.31x slower                                  |
| mypy2                    | 195 ms                                                 | 261 ms: 1.34x slower                                  |
| telco                    | 3.41 ms                                                | 4.57 ms: 1.34x slower                                 |
| async_generators         | 196 ms                                                 | 308 ms: 1.57x slower                                  |
| Geometric mean           | (ref)                                                  | 1.01x slower                                          |

Benchmark hidden because not significant (5): async_tree_memoization, pickle_dict, scimark_monte_carlo, tornado_http, pycparser
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
Ignored benchmarks (1) of results/bm-20230819-3.13.0a0-a47c13c/bm-20230819-darwin-arm64-python-main-3.13.0a0-a47c13c.json: dask


# HPT report

- Reliability score: 99.24% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x
