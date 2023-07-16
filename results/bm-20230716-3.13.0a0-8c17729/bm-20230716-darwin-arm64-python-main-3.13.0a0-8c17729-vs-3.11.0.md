
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 8c17729
- commit date: 2023-07-16
- overall geometric mean: 1.04x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-darwin-arm64-python-main-3.13.0a0-8c17729 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 1.47 sec                                               | 1.57 sec: 1.07x slower                                |
| Geometric mean | (ref)                                                  | 1.04x slower                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-darwin-arm64-python-main-3.13.0a0-8c17729 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                  |
| nbody          | 65.6 ms                                                | 73.0 ms: 1.11x slower                                 |
| float          | 53.0 ms                                                | 60.6 ms: 1.14x slower                                 |
| Geometric mean | (ref)                                                  | 1.08x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-darwin-arm64-python-main-3.13.0a0-8c17729 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.56 ms: 1.03x faster                                 |
| regex_v8       | 16.1 ms                                                | 15.7 ms: 1.03x faster                                 |
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                  |
| regex_compile  | 76.7 ms                                                | 81.7 ms: 1.06x slower                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-darwin-arm64-python-main-3.13.0a0-8c17729 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.80 ms: 1.12x faster                                 |
| unpickle             | 9.67 us                                                | 9.30 us: 1.04x faster                                 |
| pickle_dict          | 18.0 us                                                | 17.9 us: 1.00x faster                                 |
| pickle_list          | 2.81 us                                                | 2.90 us: 1.03x slower                                 |
| xml_etree_parse      | 108 ms                                                 | 112 ms: 1.03x slower                                  |
| pickle_pure_python   | 201 us                                                 | 207 us: 1.03x slower                                  |
| unpickle_pure_python | 159 us                                                 | 166 us: 1.04x slower                                  |
| pickle               | 7.15 us                                                | 7.47 us: 1.04x slower                                 |
| json_loads           | 16.1 us                                                | 17.5 us: 1.09x slower                                 |
| xml_etree_iterparse  | 70.1 ms                                                | 78.1 ms: 1.11x slower                                 |
| tomli_loads          | 1.47 sec                                               | 1.65 sec: 1.13x slower                                |
| xml_etree_process    | 35.1 ms                                                | 41.6 ms: 1.19x slower                                 |
| xml_etree_generate   | 48.3 ms                                                | 59.4 ms: 1.23x slower                                 |
| unpickle_list        | 2.65 us                                                | 3.28 us: 1.24x slower                                 |
| Geometric mean       | (ref)                                                  | 1.07x slower                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-darwin-arm64-python-main-3.13.0a0-8c17729 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 11.9 ms: 1.04x faster                                 |
| python_startup_no_site | 10.2 ms                                                | 9.77 ms: 1.04x faster                                 |
| Geometric mean         | (ref)                                                  | 1.04x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-darwin-arm64-python-main-3.13.0a0-8c17729 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 8.53 ms                                                | 7.84 ms: 1.09x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230716-darwin-arm64-python-main-3.13.0a0-8c17729 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                 | 96.3 us: 3.49x faster                                 |
| asyncio_tcp              | 651 ms                                                 | 462 ms: 1.41x faster                                  |
| unpack_sequence          | 34.1 ns                                                | 27.5 ns: 1.24x faster                                 |
| asyncio_tcp_ssl          | 1.44 sec                                               | 1.26 sec: 1.14x faster                                |
| chaos                    | 49.4 ms                                                | 43.2 ms: 1.14x faster                                 |
| coverage                 | 58.4 ms                                                | 51.5 ms: 1.14x faster                                 |
| json_dumps               | 7.63 ms                                                | 6.80 ms: 1.12x faster                                 |
| mako                     | 8.53 ms                                                | 7.84 ms: 1.09x faster                                 |
| crypto_pyaes             | 51.7 ms                                                | 48.6 ms: 1.06x faster                                 |
| python_startup           | 12.4 ms                                                | 11.9 ms: 1.04x faster                                 |
| python_startup_no_site   | 10.2 ms                                                | 9.77 ms: 1.04x faster                                 |
| unpickle                 | 9.67 us                                                | 9.30 us: 1.04x faster                                 |
| regex_effbot             | 2.63 ms                                                | 2.56 ms: 1.03x faster                                 |
| regex_v8                 | 16.1 ms                                                | 15.7 ms: 1.03x faster                                 |
| sqlglot_parse            | 959 us                                                 | 936 us: 1.02x faster                                  |
| async_tree_none          | 286 ms                                                 | 279 ms: 1.02x faster                                  |
| regex_dna                | 152 ms                                                 | 149 ms: 1.02x faster                                  |
| create_gc_cycles         | 716 us                                                 | 705 us: 1.02x faster                                  |
| async_tree_io            | 704 ms                                                 | 697 ms: 1.01x faster                                  |
| pickle_dict              | 18.0 us                                                | 17.9 us: 1.00x faster                                 |
| pidigits                 | 281 ms                                                 | 282 ms: 1.00x slower                                  |
| hexiom                   | 4.72 ms                                                | 4.80 ms: 1.02x slower                                 |
| async_tree_cpu_io_mixed  | 533 ms                                                 | 543 ms: 1.02x slower                                  |
| scimark_sparse_mat_mult  | 3.19 ms                                                | 3.25 ms: 1.02x slower                                 |
| dulwich_log              | 30.3 ms                                                | 31.1 ms: 1.03x slower                                 |
| deepcopy_memo            | 26.3 us                                                | 27.1 us: 1.03x slower                                 |
| pycparser                | 698 ms                                                 | 718 ms: 1.03x slower                                  |
| pickle_list              | 2.81 us                                                | 2.90 us: 1.03x slower                                 |
| xml_etree_parse          | 108 ms                                                 | 112 ms: 1.03x slower                                  |
| deltablue                | 2.81 ms                                                | 2.91 ms: 1.03x slower                                 |
| pickle_pure_python       | 201 us                                                 | 207 us: 1.03x slower                                  |
| meteor_contest           | 73.5 ms                                                | 76.2 ms: 1.04x slower                                 |
| scimark_fft              | 200 ms                                                 | 207 ms: 1.04x slower                                  |
| unpickle_pure_python     | 159 us                                                 | 166 us: 1.04x slower                                  |
| spectral_norm            | 72.6 ms                                                | 75.8 ms: 1.04x slower                                 |
| pickle                   | 7.15 us                                                | 7.47 us: 1.04x slower                                 |
| bench_mp_pool            | 43.9 ms                                                | 45.9 ms: 1.04x slower                                 |
| gc_traversal             | 2.42 ms                                                | 2.54 ms: 1.05x slower                                 |
| scimark_lu               | 73.3 ms                                                | 77.3 ms: 1.05x slower                                 |
| richards_super           | 39.2 ms                                                | 41.7 ms: 1.06x slower                                 |
| bench_thread_pool        | 474 us                                                 | 505 us: 1.06x slower                                  |
| regex_compile            | 76.7 ms                                                | 81.7 ms: 1.06x slower                                 |
| comprehensions           | 16.1 us                                                | 17.2 us: 1.07x slower                                 |
| docutils                 | 1.47 sec                                               | 1.57 sec: 1.07x slower                                |
| nqueens                  | 59.8 ms                                                | 64.0 ms: 1.07x slower                                 |
| json                     | 2.78 ms                                                | 2.99 ms: 1.08x slower                                 |
| deepcopy                 | 223 us                                                 | 241 us: 1.08x slower                                  |
| json_loads               | 16.1 us                                                | 17.5 us: 1.09x slower                                 |
| mdp                      | 1.55 sec                                               | 1.70 sec: 1.10x slower                                |
| logging_simple           | 3.55 us                                                | 3.90 us: 1.10x slower                                 |
| nbody                    | 65.6 ms                                                | 73.0 ms: 1.11x slower                                 |
| xml_etree_iterparse      | 70.1 ms                                                | 78.1 ms: 1.11x slower                                 |
| logging_format           | 3.78 us                                                | 4.21 us: 1.11x slower                                 |
| coroutines               | 17.8 ms                                                | 19.8 ms: 1.12x slower                                 |
| fannkuch                 | 261 ms                                                 | 293 ms: 1.12x slower                                  |
| deepcopy_reduce          | 1.91 us                                                | 2.15 us: 1.12x slower                                 |
| raytrace                 | 207 ms                                                 | 233 ms: 1.13x slower                                  |
| tomli_loads              | 1.47 sec                                               | 1.65 sec: 1.13x slower                                |
| go                       | 109 ms                                                 | 123 ms: 1.13x slower                                  |
| sqlglot_normalize        | 171 ms                                                 | 195 ms: 1.14x slower                                  |
| pprint_pformat           | 954 ms                                                 | 1.09 sec: 1.14x slower                                |
| pprint_safe_repr         | 466 ms                                                 | 533 ms: 1.14x slower                                  |
| float                    | 53.0 ms                                                | 60.6 ms: 1.14x slower                                 |
| sqlglot_optimize         | 31.1 ms                                                | 36.3 ms: 1.17x slower                                 |
| scimark_monte_carlo      | 46.5 ms                                                | 54.3 ms: 1.17x slower                                 |
| richards                 | 32.2 ms                                                | 37.8 ms: 1.17x slower                                 |
| logging_silent           | 68.1 ns                                                | 80.6 ns: 1.18x slower                                 |
| pyflate                  | 310 ms                                                 | 368 ms: 1.19x slower                                  |
| xml_etree_process        | 35.1 ms                                                | 41.6 ms: 1.19x slower                                 |
| xml_etree_generate       | 48.3 ms                                                | 59.4 ms: 1.23x slower                                 |
| unpickle_list            | 2.65 us                                                | 3.28 us: 1.24x slower                                 |
| telco                    | 3.41 ms                                                | 4.24 ms: 1.25x slower                                 |
| pathlib                  | 27.2 ms                                                | 34.7 ms: 1.28x slower                                 |
| sqlite_synth             | 1.27 us                                                | 1.62 us: 1.28x slower                                 |
| mypy2                    | 195 ms                                                 | 267 ms: 1.37x slower                                  |
| scimark_sor              | 82.6 ms                                                | 120 ms: 1.46x slower                                  |
| async_generators         | 196 ms                                                 | 317 ms: 1.61x slower                                  |
| Geometric mean           | (ref)                                                  | 1.04x slower                                          |

Benchmark hidden because not significant (4): async_tree_memoization, sqlglot_transpile, generators, tornado_http
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
Ignored benchmarks (1) of results/bm-20230716-3.13.0a0-8c17729/bm-20230716-darwin-arm64-python-main-3.13.0a0-8c17729.json: dask
