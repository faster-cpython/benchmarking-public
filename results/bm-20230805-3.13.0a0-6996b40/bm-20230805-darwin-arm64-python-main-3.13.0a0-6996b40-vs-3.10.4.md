
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 6996b40
- commit date: 2023-08-05
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-darwin-arm64-python-main-3.13.0a0-6996b40 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 1.78 sec                                               | 1.55 sec: 1.15x faster                                |
| tornado_http   | 91.9 ms                                                | 72.0 ms: 1.28x faster                                 |
| Geometric mean | (ref)                                                  | 1.21x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-darwin-arm64-python-main-3.13.0a0-6996b40 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 94.1 ms                                                | 71.9 ms: 1.31x faster                                 |
| float          | 72.3 ms                                                | 59.6 ms: 1.21x faster                                 |
| Geometric mean | (ref)                                                  | 1.17x faster                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-darwin-arm64-python-main-3.13.0a0-6996b40 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 80.8 ms: 1.20x faster                                 |
| regex_v8       | 17.5 ms                                                | 15.7 ms: 1.12x faster                                 |
| regex_dna      | 160 ms                                                 | 149 ms: 1.07x faster                                  |
| regex_effbot   | 2.45 ms                                                | 2.58 ms: 1.06x slower                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-darwin-arm64-python-main-3.13.0a0-6996b40 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 203 us: 1.40x faster                                  |
| json_dumps           | 8.38 ms                                                | 6.69 ms: 1.25x faster                                 |
| unpickle_pure_python | 203 us                                                 | 166 us: 1.23x faster                                  |
| xml_etree_process    | 45.1 ms                                                | 40.8 ms: 1.10x faster                                 |
| tomli_loads          | 1.76 sec                                               | 1.64 sec: 1.08x faster                                |
| unpickle             | 9.77 us                                                | 9.19 us: 1.06x faster                                 |
| pickle               | 7.36 us                                                | 7.32 us: 1.01x faster                                 |
| pickle_dict          | 17.8 us                                                | 17.9 us: 1.01x slower                                 |
| xml_etree_parse      | 107 ms                                                 | 109 ms: 1.02x slower                                  |
| pickle_list          | 2.83 us                                                | 2.89 us: 1.02x slower                                 |
| json_loads           | 16.9 us                                                | 17.6 us: 1.04x slower                                 |
| xml_etree_iterparse  | 72.6 ms                                                | 76.4 ms: 1.05x slower                                 |
| xml_etree_generate   | 54.3 ms                                                | 58.9 ms: 1.09x slower                                 |
| unpickle_list        | 2.66 us                                                | 3.15 us: 1.18x slower                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-darwin-arm64-python-main-3.13.0a0-6996b40 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 10.6 ms: 1.19x faster                                 |
| python_startup_no_site | 9.73 ms                                                | 8.52 ms: 1.14x faster                                 |
| Geometric mean         | (ref)                                                  | 1.16x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-darwin-arm64-python-main-3.13.0a0-6996b40 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.49 ms: 1.40x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-darwin-arm64-python-main-3.13.0a0-6996b40 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 95.2 us: 3.62x faster                                 |
| deltablue                | 5.15 ms                                                | 2.83 ms: 1.82x faster                                 |
| crypto_pyaes             | 78.0 ms                                                | 47.5 ms: 1.64x faster                                 |
| asyncio_tcp              | 673 ms                                                 | 419 ms: 1.61x faster                                  |
| logging_silent           | 119 ns                                                 | 77.0 ns: 1.55x faster                                 |
| async_tree_memoization   | 493 ms                                                 | 322 ms: 1.53x faster                                  |
| async_tree_io            | 1.02 sec                                               | 677 ms: 1.51x faster                                  |
| richards_super           | 60.7 ms                                                | 40.9 ms: 1.48x faster                                 |
| chaos                    | 66.8 ms                                                | 45.2 ms: 1.48x faster                                 |
| async_tree_none          | 402 ms                                                 | 273 ms: 1.47x faster                                  |
| sqlglot_parse            | 1.33 ms                                                | 923 us: 1.44x faster                                  |
| scimark_lu               | 110 ms                                                 | 76.7 ms: 1.43x faster                                 |
| raytrace                 | 328 ms                                                 | 230 ms: 1.43x faster                                  |
| unpack_sequence          | 38.7 ns                                                | 27.5 ns: 1.41x faster                                 |
| mako                     | 10.5 ms                                                | 7.49 ms: 1.40x faster                                 |
| pickle_pure_python       | 284 us                                                 | 203 us: 1.40x faster                                  |
| richards                 | 51.4 ms                                                | 36.8 ms: 1.40x faster                                 |
| sqlglot_transpile        | 1.54 ms                                                | 1.11 ms: 1.39x faster                                 |
| go                       | 165 ms                                                 | 120 ms: 1.38x faster                                  |
| scimark_monte_carlo      | 72.2 ms                                                | 52.9 ms: 1.37x faster                                 |
| deepcopy_memo            | 34.5 us                                                | 25.6 us: 1.35x faster                                 |
| nbody                    | 94.1 ms                                                | 71.9 ms: 1.31x faster                                 |
| spectral_norm            | 96.4 ms                                                | 74.3 ms: 1.30x faster                                 |
| pycparser                | 915 ms                                                 | 711 ms: 1.29x faster                                  |
| tornado_http             | 91.9 ms                                                | 72.0 ms: 1.28x faster                                 |
| hexiom                   | 6.32 ms                                                | 4.96 ms: 1.27x faster                                 |
| pyflate                  | 453 ms                                                 | 360 ms: 1.26x faster                                  |
| json_dumps               | 8.38 ms                                                | 6.69 ms: 1.25x faster                                 |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 536 ms: 1.25x faster                                  |
| create_gc_cycles         | 876 us                                                 | 702 us: 1.25x faster                                  |
| unpickle_pure_python     | 203 us                                                 | 166 us: 1.23x faster                                  |
| float                    | 72.3 ms                                                | 59.6 ms: 1.21x faster                                 |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.36 sec: 1.21x faster                                |
| logging_format           | 5.01 us                                                | 4.15 us: 1.21x faster                                 |
| deepcopy                 | 278 us                                                 | 230 us: 1.21x faster                                  |
| regex_compile            | 96.6 ms                                                | 80.8 ms: 1.20x faster                                 |
| logging_simple           | 4.63 us                                                | 3.88 us: 1.19x faster                                 |
| python_startup           | 12.6 ms                                                | 10.6 ms: 1.19x faster                                 |
| dulwich_log              | 37.1 ms                                                | 31.4 ms: 1.18x faster                                 |
| pprint_safe_repr         | 609 ms                                                 | 517 ms: 1.18x faster                                  |
| mypy2                    | 308 ms                                                 | 263 ms: 1.17x faster                                  |
| pprint_pformat           | 1.24 sec                                               | 1.06 sec: 1.17x faster                                |
| generators               | 32.9 ms                                                | 28.4 ms: 1.16x faster                                 |
| docutils                 | 1.78 sec                                               | 1.55 sec: 1.15x faster                                |
| scimark_fft              | 232 ms                                                 | 201 ms: 1.15x faster                                  |
| python_startup_no_site   | 9.73 ms                                                | 8.52 ms: 1.14x faster                                 |
| nqueens                  | 68.1 ms                                                | 59.8 ms: 1.14x faster                                 |
| deepcopy_reduce          | 2.38 us                                                | 2.11 us: 1.13x faster                                 |
| regex_v8                 | 17.5 ms                                                | 15.7 ms: 1.12x faster                                 |
| comprehensions           | 17.7 us                                                | 15.8 us: 1.12x faster                                 |
| fannkuch                 | 317 ms                                                 | 286 ms: 1.11x faster                                  |
| bench_thread_pool        | 548 us                                                 | 497 us: 1.10x faster                                  |
| xml_etree_process        | 45.1 ms                                                | 40.8 ms: 1.10x faster                                 |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.15 ms: 1.10x faster                                 |
| tomli_loads              | 1.76 sec                                               | 1.64 sec: 1.08x faster                                |
| regex_dna                | 160 ms                                                 | 149 ms: 1.07x faster                                  |
| scimark_sor              | 127 ms                                                 | 119 ms: 1.07x faster                                  |
| unpickle                 | 9.77 us                                                | 9.19 us: 1.06x faster                                 |
| sqlglot_optimize         | 38.0 ms                                                | 35.8 ms: 1.06x faster                                 |
| meteor_contest           | 78.6 ms                                                | 75.1 ms: 1.05x faster                                 |
| json                     | 3.10 ms                                                | 2.97 ms: 1.04x faster                                 |
| coroutines               | 20.2 ms                                                | 19.6 ms: 1.03x faster                                 |
| sqlglot_normalize        | 197 ms                                                 | 194 ms: 1.01x faster                                  |
| mdp                      | 1.67 sec                                               | 1.65 sec: 1.01x faster                                |
| pickle                   | 7.36 us                                                | 7.32 us: 1.01x faster                                 |
| pickle_dict              | 17.8 us                                                | 17.9 us: 1.01x slower                                 |
| xml_etree_parse          | 107 ms                                                 | 109 ms: 1.02x slower                                  |
| pickle_list              | 2.83 us                                                | 2.89 us: 1.02x slower                                 |
| pathlib                  | 28.8 ms                                                | 29.5 ms: 1.02x slower                                 |
| json_loads               | 16.9 us                                                | 17.6 us: 1.04x slower                                 |
| xml_etree_iterparse      | 72.6 ms                                                | 76.4 ms: 1.05x slower                                 |
| regex_effbot             | 2.45 ms                                                | 2.58 ms: 1.06x slower                                 |
| xml_etree_generate       | 54.3 ms                                                | 58.9 ms: 1.09x slower                                 |
| sqlite_synth             | 1.47 us                                                | 1.60 us: 1.09x slower                                 |
| bench_mp_pool            | 41.0 ms                                                | 44.6 ms: 1.09x slower                                 |
| unpickle_list            | 2.66 us                                                | 3.15 us: 1.18x slower                                 |
| coverage                 | 40.8 ms                                                | 50.8 ms: 1.24x slower                                 |
| telco                    | 3.68 ms                                                | 4.59 ms: 1.25x slower                                 |
| dask                     | 258 ms                                                 | 340 ms: 1.32x slower                                  |
| async_generators         | 233 ms                                                 | 311 ms: 1.33x slower                                  |
| Geometric mean           | (ref)                                                  | 1.18x faster                                          |

Benchmark hidden because not significant (2): pidigits, gc_traversal
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x
