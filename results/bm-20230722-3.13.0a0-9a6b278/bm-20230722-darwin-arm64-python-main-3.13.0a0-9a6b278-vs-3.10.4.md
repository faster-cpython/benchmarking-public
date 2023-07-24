
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 9a6b278
- commit date: 2023-07-22
- overall geometric mean: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230722-darwin-arm64-python-main-3.13.0a0-9a6b278 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 1.78 sec                                               | 1.57 sec: 1.13x faster                                |
| tornado_http   | 91.9 ms                                                | 72.1 ms: 1.28x faster                                 |
| Geometric mean | (ref)                                                  | 1.20x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230722-darwin-arm64-python-main-3.13.0a0-9a6b278 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 94.1 ms                                                | 72.7 ms: 1.29x faster                                 |
| float          | 72.3 ms                                                | 60.9 ms: 1.19x faster                                 |
| Geometric mean | (ref)                                                  | 1.15x faster                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230722-darwin-arm64-python-main-3.13.0a0-9a6b278 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 81.5 ms: 1.19x faster                                 |
| regex_v8       | 17.5 ms                                                | 15.7 ms: 1.12x faster                                 |
| regex_dna      | 160 ms                                                 | 149 ms: 1.07x faster                                  |
| regex_effbot   | 2.45 ms                                                | 2.57 ms: 1.05x slower                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230722-darwin-arm64-python-main-3.13.0a0-9a6b278 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 206 us: 1.38x faster                                  |
| json_dumps           | 8.38 ms                                                | 6.75 ms: 1.24x faster                                 |
| unpickle_pure_python | 203 us                                                 | 168 us: 1.21x faster                                  |
| xml_etree_process    | 45.1 ms                                                | 41.7 ms: 1.08x faster                                 |
| tomli_loads          | 1.76 sec                                               | 1.65 sec: 1.07x faster                                |
| unpickle             | 9.77 us                                                | 9.21 us: 1.06x faster                                 |
| pickle               | 7.36 us                                                | 7.40 us: 1.01x slower                                 |
| pickle_dict          | 17.8 us                                                | 18.1 us: 1.02x slower                                 |
| pickle_list          | 2.83 us                                                | 2.90 us: 1.03x slower                                 |
| xml_etree_parse      | 107 ms                                                 | 111 ms: 1.04x slower                                  |
| json_loads           | 16.9 us                                                | 17.6 us: 1.04x slower                                 |
| xml_etree_iterparse  | 72.6 ms                                                | 78.4 ms: 1.08x slower                                 |
| xml_etree_generate   | 54.3 ms                                                | 59.9 ms: 1.10x slower                                 |
| unpickle_list        | 2.66 us                                                | 3.15 us: 1.18x slower                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230722-darwin-arm64-python-main-3.13.0a0-9a6b278 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 10.6 ms: 1.19x faster                                 |
| python_startup_no_site | 9.73 ms                                                | 8.45 ms: 1.15x faster                                 |
| Geometric mean         | (ref)                                                  | 1.17x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230722-darwin-arm64-python-main-3.13.0a0-9a6b278 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.74 ms: 1.35x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230722-darwin-arm64-python-main-3.13.0a0-9a6b278 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 96.8 us: 3.56x faster                                 |
| deltablue                | 5.15 ms                                                | 2.92 ms: 1.76x faster                                 |
| crypto_pyaes             | 78.0 ms                                                | 48.6 ms: 1.61x faster                                 |
| chaos                    | 66.8 ms                                                | 43.4 ms: 1.54x faster                                 |
| asyncio_tcp              | 673 ms                                                 | 438 ms: 1.54x faster                                  |
| async_tree_memoization   | 493 ms                                                 | 330 ms: 1.50x faster                                  |
| logging_silent           | 119 ns                                                 | 80.5 ns: 1.48x faster                                 |
| async_tree_io            | 1.02 sec                                               | 695 ms: 1.47x faster                                  |
| richards_super           | 60.7 ms                                                | 41.5 ms: 1.46x faster                                 |
| async_tree_none          | 402 ms                                                 | 279 ms: 1.44x faster                                  |
| sqlglot_parse            | 1.33 ms                                                | 939 us: 1.42x faster                                  |
| scimark_lu               | 110 ms                                                 | 77.8 ms: 1.41x faster                                 |
| unpack_sequence          | 38.7 ns                                                | 27.4 ns: 1.41x faster                                 |
| raytrace                 | 328 ms                                                 | 233 ms: 1.41x faster                                  |
| pickle_pure_python       | 284 us                                                 | 206 us: 1.38x faster                                  |
| sqlglot_transpile        | 1.54 ms                                                | 1.12 ms: 1.37x faster                                 |
| richards                 | 51.4 ms                                                | 37.9 ms: 1.36x faster                                 |
| mako                     | 10.5 ms                                                | 7.74 ms: 1.35x faster                                 |
| go                       | 165 ms                                                 | 122 ms: 1.35x faster                                  |
| scimark_monte_carlo      | 72.2 ms                                                | 54.4 ms: 1.33x faster                                 |
| hexiom                   | 6.32 ms                                                | 4.79 ms: 1.32x faster                                 |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.26 sec: 1.31x faster                                |
| nbody                    | 94.1 ms                                                | 72.7 ms: 1.29x faster                                 |
| tornado_http             | 91.9 ms                                                | 72.1 ms: 1.28x faster                                 |
| spectral_norm            | 96.4 ms                                                | 75.8 ms: 1.27x faster                                 |
| pycparser                | 915 ms                                                 | 722 ms: 1.27x faster                                  |
| deepcopy_memo            | 34.5 us                                                | 27.3 us: 1.26x faster                                 |
| create_gc_cycles         | 876 us                                                 | 698 us: 1.26x faster                                  |
| json_dumps               | 8.38 ms                                                | 6.75 ms: 1.24x faster                                 |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 543 ms: 1.23x faster                                  |
| pyflate                  | 453 ms                                                 | 368 ms: 1.23x faster                                  |
| unpickle_pure_python     | 203 us                                                 | 168 us: 1.21x faster                                  |
| logging_format           | 5.01 us                                                | 4.21 us: 1.19x faster                                 |
| python_startup           | 12.6 ms                                                | 10.6 ms: 1.19x faster                                 |
| float                    | 72.3 ms                                                | 60.9 ms: 1.19x faster                                 |
| logging_simple           | 4.63 us                                                | 3.90 us: 1.19x faster                                 |
| regex_compile            | 96.6 ms                                                | 81.5 ms: 1.19x faster                                 |
| dulwich_log              | 37.1 ms                                                | 31.4 ms: 1.18x faster                                 |
| mypy2                    | 308 ms                                                 | 268 ms: 1.15x faster                                  |
| python_startup_no_site   | 9.73 ms                                                | 8.45 ms: 1.15x faster                                 |
| deepcopy                 | 278 us                                                 | 242 us: 1.15x faster                                  |
| generators               | 32.9 ms                                                | 28.8 ms: 1.14x faster                                 |
| pprint_safe_repr         | 609 ms                                                 | 535 ms: 1.14x faster                                  |
| docutils                 | 1.78 sec                                               | 1.57 sec: 1.13x faster                                |
| pprint_pformat           | 1.24 sec                                               | 1.09 sec: 1.13x faster                                |
| scimark_fft              | 232 ms                                                 | 207 ms: 1.12x faster                                  |
| regex_v8                 | 17.5 ms                                                | 15.7 ms: 1.12x faster                                 |
| deepcopy_reduce          | 2.38 us                                                | 2.15 us: 1.11x faster                                 |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.21 ms: 1.08x faster                                 |
| xml_etree_process        | 45.1 ms                                                | 41.7 ms: 1.08x faster                                 |
| bench_thread_pool        | 548 us                                                 | 509 us: 1.08x faster                                  |
| fannkuch                 | 317 ms                                                 | 295 ms: 1.08x faster                                  |
| regex_dna                | 160 ms                                                 | 149 ms: 1.07x faster                                  |
| nqueens                  | 68.1 ms                                                | 63.7 ms: 1.07x faster                                 |
| tomli_loads              | 1.76 sec                                               | 1.65 sec: 1.07x faster                                |
| unpickle                 | 9.77 us                                                | 9.21 us: 1.06x faster                                 |
| scimark_sor              | 127 ms                                                 | 120 ms: 1.06x faster                                  |
| sqlglot_optimize         | 38.0 ms                                                | 36.4 ms: 1.04x faster                                 |
| comprehensions           | 17.7 us                                                | 17.0 us: 1.04x faster                                 |
| meteor_contest           | 78.6 ms                                                | 76.1 ms: 1.03x faster                                 |
| json                     | 3.10 ms                                                | 3.00 ms: 1.03x faster                                 |
| coroutines               | 20.2 ms                                                | 19.8 ms: 1.02x faster                                 |
| pickle                   | 7.36 us                                                | 7.40 us: 1.01x slower                                 |
| pickle_dict              | 17.8 us                                                | 18.1 us: 1.02x slower                                 |
| pickle_list              | 2.83 us                                                | 2.90 us: 1.03x slower                                 |
| mdp                      | 1.67 sec                                               | 1.71 sec: 1.03x slower                                |
| xml_etree_parse          | 107 ms                                                 | 111 ms: 1.04x slower                                  |
| json_loads               | 16.9 us                                                | 17.6 us: 1.04x slower                                 |
| regex_effbot             | 2.45 ms                                                | 2.57 ms: 1.05x slower                                 |
| xml_etree_iterparse      | 72.6 ms                                                | 78.4 ms: 1.08x slower                                 |
| bench_mp_pool            | 41.0 ms                                                | 44.8 ms: 1.09x slower                                 |
| sqlite_synth             | 1.47 us                                                | 1.61 us: 1.09x slower                                 |
| xml_etree_generate       | 54.3 ms                                                | 59.9 ms: 1.10x slower                                 |
| telco                    | 3.68 ms                                                | 4.24 ms: 1.15x slower                                 |
| unpickle_list            | 2.66 us                                                | 3.15 us: 1.18x slower                                 |
| pathlib                  | 28.8 ms                                                | 35.0 ms: 1.22x slower                                 |
| coverage                 | 40.8 ms                                                | 51.9 ms: 1.27x slower                                 |
| dask                     | 258 ms                                                 | 346 ms: 1.34x slower                                  |
| async_generators         | 233 ms                                                 | 320 ms: 1.37x slower                                  |
| Geometric mean           | (ref)                                                  | 1.16x faster                                          |

Benchmark hidden because not significant (3): pidigits, gc_traversal, sqlglot_normalize
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
