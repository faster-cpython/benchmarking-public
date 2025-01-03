# Results vs. 3.13.0

- fork: eendebakpt
- ref: iter_freelists
- machine: windows-amd64
- commit hash: 05f479c
- commit date: 2025-01-02
- overall geometric mean: 1.013x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 224 ms: 1.04x slower                                                      |
| docutils       | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                    |
| html5lib       | 38.2 ms                                                     | 39.3 ms: 1.03x slower                                                     |
| sphinx         | 617 ms                                                      | 641 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                      |
| async_tree_io              | 513 ms                                                      | 403 ms: 1.27x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 398 ms: 1.25x faster                                                      |
| async_tree_memoization     | 265 ms                                                      | 221 ms: 1.20x faster                                                      |
| async_tree_none            | 219 ms                                                      | 184 ms: 1.19x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.18x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 347 ms: 1.10x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 304 ms: 1.01x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                                     |
| async_generators           | 223 ms                                                      | 240 ms: 1.08x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.13x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                      |
| float          | 50.8 ms                                                     | 52.7 ms: 1.04x slower                                                     |
| nbody          | 66.3 ms                                                     | 77.4 ms: 1.17x slower                                                     |
| Geometric mean | (ref)                                                       | 1.07x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 1.69 ms                                                     | 1.44 ms: 1.18x faster                                                     |
| regex_dna      | 115 ms                                                      | 118 ms: 1.02x slower                                                      |
| regex_compile  | 80.7 ms                                                     | 86.5 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                       | 1.05x faster                                                              |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.0 us: 1.08x faster                                                     |
| xml_etree_parse      | 92.2 ms                                                     | 88.8 ms: 1.04x faster                                                     |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.6 ms: 1.03x slower                                                     |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.05x slower                                                    |
| xml_etree_generate   | 53.5 ms                                                     | 56.4 ms: 1.06x slower                                                     |
| json_dumps           | 6.19 ms                                                     | 6.73 ms: 1.09x slower                                                     |
| xml_etree_process    | 36.5 ms                                                     | 40.0 ms: 1.10x slower                                                     |
| unpickle_pure_python | 130 us                                                      | 157 us: 1.21x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 228 us: 1.22x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 23.4 ms: 1.04x faster                                                     |
| python_startup_no_site | 16.9 ms                                                     | 17.4 ms: 1.03x slower                                                     |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                     |
| mako            | 6.56 ms                                                     | 6.94 ms: 1.06x slower                                                     |
| django_template | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                     |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                              |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 533 us: 15.89x faster                                                     |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                      |
| async_tree_io              | 513 ms                                                      | 403 ms: 1.27x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 398 ms: 1.25x faster                                                      |
| deepcopy                   | 223 us                                                      | 184 us: 1.22x faster                                                      |
| async_tree_memoization     | 265 ms                                                      | 221 ms: 1.20x faster                                                      |
| async_tree_none            | 219 ms                                                      | 184 ms: 1.19x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.18x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.44 ms: 1.18x faster                                                     |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 347 ms: 1.10x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.0 us: 1.08x faster                                                     |
| deepcopy_memo              | 23.1 us                                                     | 21.4 us: 1.08x faster                                                     |
| deepcopy_reduce            | 2.02 us                                                     | 1.89 us: 1.07x faster                                                     |
| telco                      | 4.85 ms                                                     | 4.58 ms: 1.06x faster                                                     |
| python_startup             | 24.4 ms                                                     | 23.4 ms: 1.04x faster                                                     |
| xml_etree_parse            | 92.2 ms                                                     | 88.8 ms: 1.04x faster                                                     |
| bench_mp_pool              | 84.2 ms                                                     | 82.1 ms: 1.03x faster                                                     |
| create_gc_cycles           | 1.22 ms                                                     | 1.21 ms: 1.01x faster                                                     |
| shortest_path              | 355 ms                                                      | 351 ms: 1.01x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 62.8 ms: 1.01x faster                                                     |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                      |
| asyncio_websockets         | 300 ms                                                      | 304 ms: 1.01x slower                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.62 us: 1.02x slower                                                     |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.02x slower                                                      |
| coverage                   | 45.3 ms                                                     | 46.3 ms: 1.02x slower                                                     |
| mdp                        | 1.43 sec                                                    | 1.46 sec: 1.02x slower                                                    |
| bpe_tokeniser              | 2.87 sec                                                    | 2.96 sec: 1.03x slower                                                    |
| python_startup_no_site     | 16.9 ms                                                     | 17.4 ms: 1.03x slower                                                     |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.68 ms: 1.03x slower                                                     |
| html5lib                   | 38.2 ms                                                     | 39.3 ms: 1.03x slower                                                     |
| genshi_text                | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                     |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.6 ms: 1.03x slower                                                     |
| float                      | 50.8 ms                                                     | 52.7 ms: 1.04x slower                                                     |
| sphinx                     | 617 ms                                                      | 641 ms: 1.04x slower                                                      |
| 2to3                       | 215 ms                                                      | 224 ms: 1.04x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.05x slower                                                    |
| go                         | 84.7 ms                                                     | 88.9 ms: 1.05x slower                                                     |
| sympy_expand               | 286 ms                                                      | 301 ms: 1.05x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 42.3 ms: 1.05x slower                                                     |
| sympy_sum                  | 85.2 ms                                                     | 89.9 ms: 1.06x slower                                                     |
| xml_etree_generate         | 53.5 ms                                                     | 56.4 ms: 1.06x slower                                                     |
| mako                       | 6.56 ms                                                     | 6.94 ms: 1.06x slower                                                     |
| sympy_str                  | 167 ms                                                      | 177 ms: 1.06x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 109 us: 1.06x slower                                                      |
| pycparser                  | 695 ms                                                      | 738 ms: 1.06x slower                                                      |
| sqlglot_optimize           | 32.5 ms                                                     | 34.6 ms: 1.06x slower                                                     |
| crypto_pyaes               | 45.6 ms                                                     | 48.8 ms: 1.07x slower                                                     |
| meteor_contest             | 72.0 ms                                                     | 77.1 ms: 1.07x slower                                                     |
| regex_compile              | 80.7 ms                                                     | 86.5 ms: 1.07x slower                                                     |
| sympy_integrate            | 12.3 ms                                                     | 13.2 ms: 1.07x slower                                                     |
| coroutines                 | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                                     |
| async_generators           | 223 ms                                                      | 240 ms: 1.08x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                    |
| json_dumps                 | 6.19 ms                                                     | 6.73 ms: 1.09x slower                                                     |
| scimark_fft                | 175 ms                                                      | 191 ms: 1.09x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 40.0 ms: 1.10x slower                                                     |
| sqlglot_normalize          | 172 ms                                                      | 190 ms: 1.11x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.83 us: 1.11x slower                                                     |
| logging_simple             | 5.77 us                                                     | 6.43 us: 1.11x slower                                                     |
| fannkuch                   | 252 ms                                                      | 281 ms: 1.12x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 62.9 ms: 1.12x slower                                                     |
| pyflate                    | 283 ms                                                      | 318 ms: 1.13x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 550 ms: 1.14x slower                                                      |
| chaos                      | 37.9 ms                                                     | 43.2 ms: 1.14x slower                                                     |
| scimark_lu                 | 56.7 ms                                                     | 65.0 ms: 1.15x slower                                                     |
| generators                 | 19.0 ms                                                     | 21.7 ms: 1.15x slower                                                     |
| sqlglot_transpile          | 953 us                                                      | 1.10 ms: 1.16x slower                                                     |
| scimark_monte_carlo        | 40.7 ms                                                     | 47.3 ms: 1.16x slower                                                     |
| pprint_pformat             | 977 ms                                                      | 1.14 sec: 1.17x slower                                                    |
| nbody                      | 66.3 ms                                                     | 77.4 ms: 1.17x slower                                                     |
| comprehensions             | 10.4 us                                                     | 12.1 us: 1.17x slower                                                     |
| sqlglot_parse              | 764 us                                                      | 896 us: 1.17x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.22 ms: 1.17x slower                                                     |
| hexiom                     | 3.84 ms                                                     | 4.53 ms: 1.18x slower                                                     |
| scimark_sor                | 76.2 ms                                                     | 90.7 ms: 1.19x slower                                                     |
| many_optionals             | 361 us                                                      | 431 us: 1.19x slower                                                      |
| richards_super             | 29.8 ms                                                     | 35.8 ms: 1.20x slower                                                     |
| django_template            | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                     |
| unpickle_pure_python       | 130 us                                                      | 157 us: 1.21x slower                                                      |
| richards                   | 26.3 ms                                                     | 31.8 ms: 1.21x slower                                                     |
| logging_silent             | 54.6 ns                                                     | 66.4 ns: 1.22x slower                                                     |
| pickle_pure_python         | 186 us                                                      | 228 us: 1.22x slower                                                      |
| raytrace                   | 153 ms                                                      | 202 ms: 1.32x slower                                                      |
| subparsers                 | 10.9 ms                                                     | 16.2 ms: 1.49x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                              |

Benchmark hidden because not significant (9): regex_v8, json, pylint, gc_traversal, k_core, pathlib, connected_components, bench_thread_pool, genshi_xml
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20250102-3.14.0a3+-05f479c/bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c.json: mypy2

- Geometric mean (including insignificant results): 1.013x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown