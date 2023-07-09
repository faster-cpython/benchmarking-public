
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: da98ed0
- commit date: 2023-07-08
- overall geometric mean: 1.03x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-darwin-arm64-python-main-3.13.0a0-da98ed0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 1.47 sec                                               | 1.57 sec: 1.06x slower                                |
| Geometric mean | (ref)                                                  | 1.04x slower                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-darwin-arm64-python-main-3.13.0a0-da98ed0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                  |
| nbody          | 65.6 ms                                                | 71.6 ms: 1.09x slower                                 |
| float          | 53.0 ms                                                | 59.8 ms: 1.13x slower                                 |
| Geometric mean | (ref)                                                  | 1.07x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-darwin-arm64-python-main-3.13.0a0-da98ed0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_v8       | 16.1 ms                                                | 15.7 ms: 1.03x faster                                 |
| regex_effbot   | 2.63 ms                                                | 2.56 ms: 1.03x faster                                 |
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                  |
| regex_compile  | 76.7 ms                                                | 79.9 ms: 1.04x slower                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-darwin-arm64-python-main-3.13.0a0-da98ed0 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.63 ms: 1.15x faster                                 |
| unpickle             | 9.67 us                                                | 9.31 us: 1.04x faster                                 |
| unpickle_pure_python | 159 us                                                 | 160 us: 1.01x slower                                  |
| pickle_pure_python   | 201 us                                                 | 203 us: 1.01x slower                                  |
| xml_etree_parse      | 108 ms                                                 | 111 ms: 1.03x slower                                  |
| pickle               | 7.15 us                                                | 7.41 us: 1.04x slower                                 |
| pickle_list          | 2.81 us                                                | 2.92 us: 1.04x slower                                 |
| json_loads           | 16.1 us                                                | 17.6 us: 1.09x slower                                 |
| xml_etree_iterparse  | 70.1 ms                                                | 77.4 ms: 1.10x slower                                 |
| tomli_loads          | 1.47 sec                                               | 1.65 sec: 1.13x slower                                |
| xml_etree_process    | 35.1 ms                                                | 40.7 ms: 1.16x slower                                 |
| unpickle_list        | 2.65 us                                                | 3.20 us: 1.21x slower                                 |
| xml_etree_generate   | 48.3 ms                                                | 58.3 ms: 1.21x slower                                 |
| Geometric mean       | (ref)                                                  | 1.06x slower                                          |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-darwin-arm64-python-main-3.13.0a0-da98ed0 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 9.36 ms: 1.09x faster                                 |
| python_startup         | 12.4 ms                                                | 11.5 ms: 1.08x faster                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-darwin-arm64-python-main-3.13.0a0-da98ed0 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 8.53 ms                                                | 7.43 ms: 1.15x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230708-darwin-arm64-python-main-3.13.0a0-da98ed0 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                 | 94.4 us: 3.56x faster                                 |
| asyncio_tcp              | 651 ms                                                 | 465 ms: 1.40x faster                                  |
| unpack_sequence          | 34.1 ns                                                | 27.8 ns: 1.23x faster                                 |
| chaos                    | 49.4 ms                                                | 42.4 ms: 1.17x faster                                 |
| json_dumps               | 7.63 ms                                                | 6.63 ms: 1.15x faster                                 |
| mako                     | 8.53 ms                                                | 7.43 ms: 1.15x faster                                 |
| asyncio_tcp_ssl          | 1.44 sec                                               | 1.26 sec: 1.15x faster                                |
| coverage                 | 58.4 ms                                                | 51.1 ms: 1.14x faster                                 |
| python_startup_no_site   | 10.2 ms                                                | 9.36 ms: 1.09x faster                                 |
| python_startup           | 12.4 ms                                                | 11.5 ms: 1.08x faster                                 |
| unpickle                 | 9.67 us                                                | 9.31 us: 1.04x faster                                 |
| async_tree_none          | 286 ms                                                 | 277 ms: 1.03x faster                                  |
| async_tree_memoization   | 336 ms                                                 | 326 ms: 1.03x faster                                  |
| regex_v8                 | 16.1 ms                                                | 15.7 ms: 1.03x faster                                 |
| regex_effbot             | 2.63 ms                                                | 2.56 ms: 1.03x faster                                 |
| hexiom                   | 4.72 ms                                                | 4.62 ms: 1.02x faster                                 |
| create_gc_cycles         | 716 us                                                 | 701 us: 1.02x faster                                  |
| regex_dna                | 152 ms                                                 | 149 ms: 1.02x faster                                  |
| scimark_sparse_mat_mult  | 3.19 ms                                                | 3.13 ms: 1.02x faster                                 |
| deepcopy_memo            | 26.3 us                                                | 25.9 us: 1.02x faster                                 |
| async_tree_io            | 704 ms                                                 | 694 ms: 1.02x faster                                  |
| sqlglot_parse            | 959 us                                                 | 952 us: 1.01x faster                                  |
| gc_traversal             | 2.42 ms                                                | 2.40 ms: 1.01x faster                                 |
| pidigits                 | 281 ms                                                 | 282 ms: 1.00x slower                                  |
| generators               | 28.8 ms                                                | 28.9 ms: 1.00x slower                                 |
| unpickle_pure_python     | 159 us                                                 | 160 us: 1.01x slower                                  |
| crypto_pyaes             | 51.7 ms                                                | 52.2 ms: 1.01x slower                                 |
| pickle_pure_python       | 201 us                                                 | 203 us: 1.01x slower                                  |
| deltablue                | 2.81 ms                                                | 2.85 ms: 1.01x slower                                 |
| sqlglot_transpile        | 1.12 ms                                                | 1.14 ms: 1.01x slower                                 |
| comprehensions           | 16.1 us                                                | 16.3 us: 1.01x slower                                 |
| async_tree_cpu_io_mixed  | 533 ms                                                 | 541 ms: 1.01x slower                                  |
| nqueens                  | 59.8 ms                                                | 60.7 ms: 1.02x slower                                 |
| dulwich_log              | 30.3 ms                                                | 30.8 ms: 1.02x slower                                 |
| pycparser                | 698 ms                                                 | 710 ms: 1.02x slower                                  |
| meteor_contest           | 73.5 ms                                                | 75.0 ms: 1.02x slower                                 |
| scimark_fft              | 200 ms                                                 | 204 ms: 1.02x slower                                  |
| scimark_lu               | 73.3 ms                                                | 74.9 ms: 1.02x slower                                 |
| xml_etree_parse          | 108 ms                                                 | 111 ms: 1.03x slower                                  |
| spectral_norm            | 72.6 ms                                                | 75.1 ms: 1.03x slower                                 |
| pickle                   | 7.15 us                                                | 7.41 us: 1.04x slower                                 |
| bench_mp_pool            | 43.9 ms                                                | 45.7 ms: 1.04x slower                                 |
| pickle_list              | 2.81 us                                                | 2.92 us: 1.04x slower                                 |
| regex_compile            | 76.7 ms                                                | 79.9 ms: 1.04x slower                                 |
| deepcopy                 | 223 us                                                 | 233 us: 1.05x slower                                  |
| bench_thread_pool        | 474 us                                                 | 497 us: 1.05x slower                                  |
| richards_super           | 39.2 ms                                                | 41.7 ms: 1.06x slower                                 |
| docutils                 | 1.47 sec                                               | 1.57 sec: 1.06x slower                                |
| mdp                      | 1.55 sec                                               | 1.66 sec: 1.08x slower                                |
| json                     | 2.78 ms                                                | 3.00 ms: 1.08x slower                                 |
| raytrace                 | 207 ms                                                 | 225 ms: 1.09x slower                                  |
| json_loads               | 16.1 us                                                | 17.6 us: 1.09x slower                                 |
| nbody                    | 65.6 ms                                                | 71.6 ms: 1.09x slower                                 |
| fannkuch                 | 261 ms                                                 | 287 ms: 1.10x slower                                  |
| logging_simple           | 3.55 us                                                | 3.90 us: 1.10x slower                                 |
| deepcopy_reduce          | 1.91 us                                                | 2.10 us: 1.10x slower                                 |
| xml_etree_iterparse      | 70.1 ms                                                | 77.4 ms: 1.10x slower                                 |
| logging_format           | 3.78 us                                                | 4.18 us: 1.11x slower                                 |
| pprint_pformat           | 954 ms                                                 | 1.06 sec: 1.11x slower                                |
| go                       | 109 ms                                                 | 121 ms: 1.11x slower                                  |
| pprint_safe_repr         | 466 ms                                                 | 519 ms: 1.11x slower                                  |
| sqlglot_normalize        | 171 ms                                                 | 190 ms: 1.11x slower                                  |
| tomli_loads              | 1.47 sec                                               | 1.65 sec: 1.13x slower                                |
| coroutines               | 17.8 ms                                                | 20.1 ms: 1.13x slower                                 |
| float                    | 53.0 ms                                                | 59.8 ms: 1.13x slower                                 |
| sqlglot_optimize         | 31.1 ms                                                | 35.3 ms: 1.14x slower                                 |
| logging_silent           | 68.1 ns                                                | 77.7 ns: 1.14x slower                                 |
| xml_etree_process        | 35.1 ms                                                | 40.7 ms: 1.16x slower                                 |
| richards                 | 32.2 ms                                                | 37.6 ms: 1.17x slower                                 |
| pyflate                  | 310 ms                                                 | 369 ms: 1.19x slower                                  |
| telco                    | 3.41 ms                                                | 4.09 ms: 1.20x slower                                 |
| unpickle_list            | 2.65 us                                                | 3.20 us: 1.21x slower                                 |
| xml_etree_generate       | 48.3 ms                                                | 58.3 ms: 1.21x slower                                 |
| scimark_monte_carlo      | 46.5 ms                                                | 56.2 ms: 1.21x slower                                 |
| sqlite_synth             | 1.27 us                                                | 1.62 us: 1.27x slower                                 |
| pathlib                  | 27.2 ms                                                | 34.7 ms: 1.27x slower                                 |
| mypy2                    | 195 ms                                                 | 266 ms: 1.36x slower                                  |
| scimark_sor              | 82.6 ms                                                | 119 ms: 1.44x slower                                  |
| async_generators         | 196 ms                                                 | 312 ms: 1.59x slower                                  |
| Geometric mean           | (ref)                                                  | 1.03x slower                                          |

Benchmark hidden because not significant (2): pickle_dict, tornado_http
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
Ignored benchmarks (1) of results/bm-20230708-3.13.0a0-da98ed0/bm-20230708-darwin-arm64-python-main-3.13.0a0-da98ed0.json: dask
