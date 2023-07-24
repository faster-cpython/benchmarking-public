
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 9a6b278
- commit date: 2023-07-22
- overall geometric mean: 1.04x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230722-darwin-arm64-python-main-3.13.0a0-9a6b278 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 1.47 sec                                               | 1.57 sec: 1.07x slower                                |
| Geometric mean | (ref)                                                  | 1.04x slower                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230722-darwin-arm64-python-main-3.13.0a0-9a6b278 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                  |
| nbody          | 65.6 ms                                                | 72.7 ms: 1.11x slower                                 |
| float          | 53.0 ms                                                | 60.9 ms: 1.15x slower                                 |
| Geometric mean | (ref)                                                  | 1.09x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230722-darwin-arm64-python-main-3.13.0a0-9a6b278 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_v8       | 16.1 ms                                                | 15.7 ms: 1.03x faster                                 |
| regex_effbot   | 2.63 ms                                                | 2.57 ms: 1.02x faster                                 |
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                  |
| regex_compile  | 76.7 ms                                                | 81.5 ms: 1.06x slower                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230722-darwin-arm64-python-main-3.13.0a0-9a6b278 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.75 ms: 1.13x faster                                 |
| unpickle             | 9.67 us                                                | 9.21 us: 1.05x faster                                 |
| pickle_dict          | 18.0 us                                                | 18.1 us: 1.01x slower                                 |
| pickle_pure_python   | 201 us                                                 | 206 us: 1.03x slower                                  |
| xml_etree_parse      | 108 ms                                                 | 111 ms: 1.03x slower                                  |
| pickle_list          | 2.81 us                                                | 2.90 us: 1.03x slower                                 |
| pickle               | 7.15 us                                                | 7.40 us: 1.04x slower                                 |
| unpickle_pure_python | 159 us                                                 | 168 us: 1.06x slower                                  |
| json_loads           | 16.1 us                                                | 17.6 us: 1.09x slower                                 |
| xml_etree_iterparse  | 70.1 ms                                                | 78.4 ms: 1.12x slower                                 |
| tomli_loads          | 1.47 sec                                               | 1.65 sec: 1.13x slower                                |
| xml_etree_process    | 35.1 ms                                                | 41.7 ms: 1.19x slower                                 |
| unpickle_list        | 2.65 us                                                | 3.15 us: 1.19x slower                                 |
| xml_etree_generate   | 48.3 ms                                                | 59.9 ms: 1.24x slower                                 |
| Geometric mean       | (ref)                                                  | 1.07x slower                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230722-darwin-arm64-python-main-3.13.0a0-9a6b278 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 8.45 ms: 1.20x faster                                 |
| python_startup         | 12.4 ms                                                | 10.6 ms: 1.17x faster                                 |
| Geometric mean         | (ref)                                                  | 1.19x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230722-darwin-arm64-python-main-3.13.0a0-9a6b278 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 8.53 ms                                                | 7.74 ms: 1.10x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230722-darwin-arm64-python-main-3.13.0a0-9a6b278 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                 | 96.8 us: 3.47x faster                                 |
| asyncio_tcp              | 651 ms                                                 | 438 ms: 1.49x faster                                  |
| unpack_sequence          | 34.1 ns                                                | 27.4 ns: 1.24x faster                                 |
| python_startup_no_site   | 10.2 ms                                                | 8.45 ms: 1.20x faster                                 |
| python_startup           | 12.4 ms                                                | 10.6 ms: 1.17x faster                                 |
| asyncio_tcp_ssl          | 1.44 sec                                               | 1.26 sec: 1.14x faster                                |
| chaos                    | 49.4 ms                                                | 43.4 ms: 1.14x faster                                 |
| json_dumps               | 7.63 ms                                                | 6.75 ms: 1.13x faster                                 |
| coverage                 | 58.4 ms                                                | 51.9 ms: 1.13x faster                                 |
| mako                     | 8.53 ms                                                | 7.74 ms: 1.10x faster                                 |
| crypto_pyaes             | 51.7 ms                                                | 48.6 ms: 1.07x faster                                 |
| unpickle                 | 9.67 us                                                | 9.21 us: 1.05x faster                                 |
| regex_v8                 | 16.1 ms                                                | 15.7 ms: 1.03x faster                                 |
| create_gc_cycles         | 716 us                                                 | 698 us: 1.03x faster                                  |
| async_tree_none          | 286 ms                                                 | 279 ms: 1.02x faster                                  |
| regex_effbot             | 2.63 ms                                                | 2.57 ms: 1.02x faster                                 |
| sqlglot_parse            | 959 us                                                 | 939 us: 1.02x faster                                  |
| regex_dna                | 152 ms                                                 | 149 ms: 1.02x faster                                  |
| async_tree_io            | 704 ms                                                 | 695 ms: 1.01x faster                                  |
| gc_traversal             | 2.42 ms                                                | 2.40 ms: 1.01x faster                                 |
| pidigits                 | 281 ms                                                 | 282 ms: 1.00x slower                                  |
| scimark_sparse_mat_mult  | 3.19 ms                                                | 3.21 ms: 1.01x slower                                 |
| pickle_dict              | 18.0 us                                                | 18.1 us: 1.01x slower                                 |
| hexiom                   | 4.72 ms                                                | 4.79 ms: 1.02x slower                                 |
| async_tree_cpu_io_mixed  | 533 ms                                                 | 543 ms: 1.02x slower                                  |
| bench_mp_pool            | 43.9 ms                                                | 44.8 ms: 1.02x slower                                 |
| pickle_pure_python       | 201 us                                                 | 206 us: 1.03x slower                                  |
| xml_etree_parse          | 108 ms                                                 | 111 ms: 1.03x slower                                  |
| pickle_list              | 2.81 us                                                | 2.90 us: 1.03x slower                                 |
| meteor_contest           | 73.5 ms                                                | 76.1 ms: 1.03x slower                                 |
| pycparser                | 698 ms                                                 | 722 ms: 1.04x slower                                  |
| scimark_fft              | 200 ms                                                 | 207 ms: 1.04x slower                                  |
| pickle                   | 7.15 us                                                | 7.40 us: 1.04x slower                                 |
| dulwich_log              | 30.3 ms                                                | 31.4 ms: 1.04x slower                                 |
| deltablue                | 2.81 ms                                                | 2.92 ms: 1.04x slower                                 |
| deepcopy_memo            | 26.3 us                                                | 27.3 us: 1.04x slower                                 |
| spectral_norm            | 72.6 ms                                                | 75.8 ms: 1.04x slower                                 |
| comprehensions           | 16.1 us                                                | 17.0 us: 1.05x slower                                 |
| unpickle_pure_python     | 159 us                                                 | 168 us: 1.06x slower                                  |
| richards_super           | 39.2 ms                                                | 41.5 ms: 1.06x slower                                 |
| scimark_lu               | 73.3 ms                                                | 77.8 ms: 1.06x slower                                 |
| regex_compile            | 76.7 ms                                                | 81.5 ms: 1.06x slower                                 |
| nqueens                  | 59.8 ms                                                | 63.7 ms: 1.07x slower                                 |
| docutils                 | 1.47 sec                                               | 1.57 sec: 1.07x slower                                |
| bench_thread_pool        | 474 us                                                 | 509 us: 1.07x slower                                  |
| json                     | 2.78 ms                                                | 3.00 ms: 1.08x slower                                 |
| deepcopy                 | 223 us                                                 | 242 us: 1.09x slower                                  |
| json_loads               | 16.1 us                                                | 17.6 us: 1.09x slower                                 |
| logging_simple           | 3.55 us                                                | 3.90 us: 1.10x slower                                 |
| nbody                    | 65.6 ms                                                | 72.7 ms: 1.11x slower                                 |
| mdp                      | 1.55 sec                                               | 1.71 sec: 1.11x slower                                |
| logging_format           | 3.78 us                                                | 4.21 us: 1.11x slower                                 |
| coroutines               | 17.8 ms                                                | 19.8 ms: 1.11x slower                                 |
| xml_etree_iterparse      | 70.1 ms                                                | 78.4 ms: 1.12x slower                                 |
| deepcopy_reduce          | 1.91 us                                                | 2.15 us: 1.12x slower                                 |
| go                       | 109 ms                                                 | 122 ms: 1.12x slower                                  |
| raytrace                 | 207 ms                                                 | 233 ms: 1.13x slower                                  |
| tomli_loads              | 1.47 sec                                               | 1.65 sec: 1.13x slower                                |
| fannkuch                 | 261 ms                                                 | 295 ms: 1.13x slower                                  |
| pprint_pformat           | 954 ms                                                 | 1.09 sec: 1.15x slower                                |
| pprint_safe_repr         | 466 ms                                                 | 535 ms: 1.15x slower                                  |
| float                    | 53.0 ms                                                | 60.9 ms: 1.15x slower                                 |
| sqlglot_normalize        | 171 ms                                                 | 197 ms: 1.15x slower                                  |
| sqlglot_optimize         | 31.1 ms                                                | 36.4 ms: 1.17x slower                                 |
| scimark_monte_carlo      | 46.5 ms                                                | 54.4 ms: 1.17x slower                                 |
| richards                 | 32.2 ms                                                | 37.9 ms: 1.18x slower                                 |
| logging_silent           | 68.1 ns                                                | 80.5 ns: 1.18x slower                                 |
| pyflate                  | 310 ms                                                 | 368 ms: 1.19x slower                                  |
| xml_etree_process        | 35.1 ms                                                | 41.7 ms: 1.19x slower                                 |
| unpickle_list            | 2.65 us                                                | 3.15 us: 1.19x slower                                 |
| xml_etree_generate       | 48.3 ms                                                | 59.9 ms: 1.24x slower                                 |
| telco                    | 3.41 ms                                                | 4.24 ms: 1.24x slower                                 |
| sqlite_synth             | 1.27 us                                                | 1.61 us: 1.27x slower                                 |
| pathlib                  | 27.2 ms                                                | 35.0 ms: 1.29x slower                                 |
| mypy2                    | 195 ms                                                 | 268 ms: 1.37x slower                                  |
| scimark_sor              | 82.6 ms                                                | 120 ms: 1.45x slower                                  |
| async_generators         | 196 ms                                                 | 320 ms: 1.63x slower                                  |
| Geometric mean           | (ref)                                                  | 1.04x slower                                          |

Benchmark hidden because not significant (4): async_tree_memoization, generators, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
Ignored benchmarks (1) of results/bm-20230722-3.13.0a0-9a6b278/bm-20230722-darwin-arm64-python-main-3.13.0a0-9a6b278.json: dask
