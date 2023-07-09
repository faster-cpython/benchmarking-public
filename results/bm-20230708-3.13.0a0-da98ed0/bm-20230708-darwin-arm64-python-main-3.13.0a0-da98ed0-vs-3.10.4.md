
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: da98ed0
- commit date: 2023-07-08
- overall geometric mean: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-darwin-arm64-python-main-3.13.0a0-da98ed0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 1.78 sec                                               | 1.57 sec: 1.14x faster                                |
| tornado_http   | 91.9 ms                                                | 72.3 ms: 1.27x faster                                 |
| Geometric mean | (ref)                                                  | 1.20x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-darwin-arm64-python-main-3.13.0a0-da98ed0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 94.1 ms                                                | 71.6 ms: 1.31x faster                                 |
| float          | 72.3 ms                                                | 59.8 ms: 1.21x faster                                 |
| Geometric mean | (ref)                                                  | 1.17x faster                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-darwin-arm64-python-main-3.13.0a0-da98ed0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 79.9 ms: 1.21x faster                                 |
| regex_v8       | 17.5 ms                                                | 15.7 ms: 1.12x faster                                 |
| regex_dna      | 160 ms                                                 | 149 ms: 1.07x faster                                  |
| regex_effbot   | 2.45 ms                                                | 2.56 ms: 1.05x slower                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-darwin-arm64-python-main-3.13.0a0-da98ed0 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 203 us: 1.40x faster                                  |
| unpickle_pure_python | 203 us                                                 | 160 us: 1.27x faster                                  |
| json_dumps           | 8.38 ms                                                | 6.63 ms: 1.26x faster                                 |
| xml_etree_process    | 45.1 ms                                                | 40.7 ms: 1.11x faster                                 |
| tomli_loads          | 1.76 sec                                               | 1.65 sec: 1.07x faster                                |
| unpickle             | 9.77 us                                                | 9.31 us: 1.05x faster                                 |
| pickle               | 7.36 us                                                | 7.41 us: 1.01x slower                                 |
| pickle_dict          | 17.8 us                                                | 17.9 us: 1.01x slower                                 |
| pickle_list          | 2.83 us                                                | 2.92 us: 1.03x slower                                 |
| xml_etree_parse      | 107 ms                                                 | 111 ms: 1.03x slower                                  |
| json_loads           | 16.9 us                                                | 17.6 us: 1.04x slower                                 |
| xml_etree_iterparse  | 72.6 ms                                                | 77.4 ms: 1.07x slower                                 |
| xml_etree_generate   | 54.3 ms                                                | 58.3 ms: 1.07x slower                                 |
| unpickle_list        | 2.66 us                                                | 3.20 us: 1.20x slower                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-darwin-arm64-python-main-3.13.0a0-da98ed0 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 11.5 ms: 1.09x faster                                 |
| python_startup_no_site | 9.73 ms                                                | 9.36 ms: 1.04x faster                                 |
| Geometric mean         | (ref)                                                  | 1.07x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-darwin-arm64-python-main-3.13.0a0-da98ed0 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.43 ms: 1.41x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-darwin-arm64-python-main-3.13.0a0-da98ed0 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 94.4 us: 3.65x faster                                 |
| deltablue                | 5.15 ms                                                | 2.85 ms: 1.81x faster                                 |
| chaos                    | 66.8 ms                                                | 42.4 ms: 1.58x faster                                 |
| logging_silent           | 119 ns                                                 | 77.7 ns: 1.53x faster                                 |
| async_tree_memoization   | 493 ms                                                 | 326 ms: 1.51x faster                                  |
| crypto_pyaes             | 78.0 ms                                                | 52.2 ms: 1.50x faster                                 |
| async_tree_io            | 1.02 sec                                               | 694 ms: 1.47x faster                                  |
| scimark_lu               | 110 ms                                                 | 74.9 ms: 1.47x faster                                 |
| richards_super           | 60.7 ms                                                | 41.7 ms: 1.46x faster                                 |
| raytrace                 | 328 ms                                                 | 225 ms: 1.45x faster                                  |
| async_tree_none          | 402 ms                                                 | 277 ms: 1.45x faster                                  |
| asyncio_tcp              | 673 ms                                                 | 465 ms: 1.45x faster                                  |
| mako                     | 10.5 ms                                                | 7.43 ms: 1.41x faster                                 |
| sqlglot_parse            | 1.33 ms                                                | 952 us: 1.40x faster                                  |
| pickle_pure_python       | 284 us                                                 | 203 us: 1.40x faster                                  |
| unpack_sequence          | 38.7 ns                                                | 27.8 ns: 1.39x faster                                 |
| hexiom                   | 6.32 ms                                                | 4.62 ms: 1.37x faster                                 |
| richards                 | 51.4 ms                                                | 37.6 ms: 1.37x faster                                 |
| go                       | 165 ms                                                 | 121 ms: 1.36x faster                                  |
| sqlglot_transpile        | 1.54 ms                                                | 1.14 ms: 1.35x faster                                 |
| deepcopy_memo            | 34.5 us                                                | 25.9 us: 1.33x faster                                 |
| nbody                    | 94.1 ms                                                | 71.6 ms: 1.31x faster                                 |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.26 sec: 1.31x faster                                |
| pycparser                | 915 ms                                                 | 710 ms: 1.29x faster                                  |
| scimark_monte_carlo      | 72.2 ms                                                | 56.2 ms: 1.28x faster                                 |
| spectral_norm            | 96.4 ms                                                | 75.1 ms: 1.28x faster                                 |
| tornado_http             | 91.9 ms                                                | 72.3 ms: 1.27x faster                                 |
| unpickle_pure_python     | 203 us                                                 | 160 us: 1.27x faster                                  |
| json_dumps               | 8.38 ms                                                | 6.63 ms: 1.26x faster                                 |
| create_gc_cycles         | 876 us                                                 | 701 us: 1.25x faster                                  |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 541 ms: 1.24x faster                                  |
| pyflate                  | 453 ms                                                 | 369 ms: 1.23x faster                                  |
| regex_compile            | 96.6 ms                                                | 79.9 ms: 1.21x faster                                 |
| float                    | 72.3 ms                                                | 59.8 ms: 1.21x faster                                 |
| dulwich_log              | 37.1 ms                                                | 30.8 ms: 1.20x faster                                 |
| logging_format           | 5.01 us                                                | 4.18 us: 1.20x faster                                 |
| deepcopy                 | 278 us                                                 | 233 us: 1.19x faster                                  |
| logging_simple           | 4.63 us                                                | 3.90 us: 1.19x faster                                 |
| pprint_pformat           | 1.24 sec                                               | 1.06 sec: 1.17x faster                                |
| pprint_safe_repr         | 609 ms                                                 | 519 ms: 1.17x faster                                  |
| mypy2                    | 308 ms                                                 | 266 ms: 1.16x faster                                  |
| generators               | 32.9 ms                                                | 28.9 ms: 1.14x faster                                 |
| docutils                 | 1.78 sec                                               | 1.57 sec: 1.14x faster                                |
| scimark_fft              | 232 ms                                                 | 204 ms: 1.14x faster                                  |
| deepcopy_reduce          | 2.38 us                                                | 2.10 us: 1.13x faster                                 |
| nqueens                  | 68.1 ms                                                | 60.7 ms: 1.12x faster                                 |
| regex_v8                 | 17.5 ms                                                | 15.7 ms: 1.12x faster                                 |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.13 ms: 1.11x faster                                 |
| fannkuch                 | 317 ms                                                 | 287 ms: 1.11x faster                                  |
| xml_etree_process        | 45.1 ms                                                | 40.7 ms: 1.11x faster                                 |
| bench_thread_pool        | 548 us                                                 | 497 us: 1.10x faster                                  |
| python_startup           | 12.6 ms                                                | 11.5 ms: 1.09x faster                                 |
| comprehensions           | 17.7 us                                                | 16.3 us: 1.08x faster                                 |
| sqlglot_optimize         | 38.0 ms                                                | 35.3 ms: 1.08x faster                                 |
| regex_dna                | 160 ms                                                 | 149 ms: 1.07x faster                                  |
| tomli_loads              | 1.76 sec                                               | 1.65 sec: 1.07x faster                                |
| scimark_sor              | 127 ms                                                 | 119 ms: 1.07x faster                                  |
| unpickle                 | 9.77 us                                                | 9.31 us: 1.05x faster                                 |
| meteor_contest           | 78.6 ms                                                | 75.0 ms: 1.05x faster                                 |
| python_startup_no_site   | 9.73 ms                                                | 9.36 ms: 1.04x faster                                 |
| json                     | 3.10 ms                                                | 3.00 ms: 1.03x faster                                 |
| sqlglot_normalize        | 197 ms                                                 | 190 ms: 1.03x faster                                  |
| coroutines               | 20.2 ms                                                | 20.1 ms: 1.01x faster                                 |
| pickle                   | 7.36 us                                                | 7.41 us: 1.01x slower                                 |
| pickle_dict              | 17.8 us                                                | 17.9 us: 1.01x slower                                 |
| pickle_list              | 2.83 us                                                | 2.92 us: 1.03x slower                                 |
| xml_etree_parse          | 107 ms                                                 | 111 ms: 1.03x slower                                  |
| json_loads               | 16.9 us                                                | 17.6 us: 1.04x slower                                 |
| regex_effbot             | 2.45 ms                                                | 2.56 ms: 1.05x slower                                 |
| xml_etree_iterparse      | 72.6 ms                                                | 77.4 ms: 1.07x slower                                 |
| xml_etree_generate       | 54.3 ms                                                | 58.3 ms: 1.07x slower                                 |
| sqlite_synth             | 1.47 us                                                | 1.62 us: 1.10x slower                                 |
| telco                    | 3.68 ms                                                | 4.09 ms: 1.11x slower                                 |
| bench_mp_pool            | 41.0 ms                                                | 45.7 ms: 1.11x slower                                 |
| unpickle_list            | 2.66 us                                                | 3.20 us: 1.20x slower                                 |
| pathlib                  | 28.8 ms                                                | 34.7 ms: 1.20x slower                                 |
| coverage                 | 40.8 ms                                                | 51.1 ms: 1.25x slower                                 |
| dask                     | 258 ms                                                 | 344 ms: 1.34x slower                                  |
| async_generators         | 233 ms                                                 | 312 ms: 1.34x slower                                  |
| Geometric mean           | (ref)                                                  | 1.17x faster                                          |

Benchmark hidden because not significant (3): mdp, pidigits, gc_traversal
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
