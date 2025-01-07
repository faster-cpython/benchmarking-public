# Results vs. 3.13.0

- fork: kumaraditya303
- ref: fast_state
- machine: windows-amd64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.013x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 225 ms: 1.05x slower                                                      |
| docutils       | 1.53 sec                                                    | 1.66 sec: 1.09x slower                                                    |
| html5lib       | 38.2 ms                                                     | 39.7 ms: 1.04x slower                                                     |
| sphinx         | 617 ms                                                      | 644 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                      |
| async_tree_io              | 513 ms                                                      | 403 ms: 1.27x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 393 ms: 1.26x faster                                                      |
| async_tree_memoization     | 265 ms                                                      | 218 ms: 1.21x faster                                                      |
| async_tree_none            | 219 ms                                                      | 182 ms: 1.20x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.20x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 347 ms: 1.10x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 309 ms: 1.03x slower                                                      |
| async_generators           | 223 ms                                                      | 241 ms: 1.08x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.13x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 146 ms                                                      | 146 ms: 1.00x faster                                                      |
| float          | 50.8 ms                                                     | 52.6 ms: 1.03x slower                                                     |
| nbody          | 66.3 ms                                                     | 77.8 ms: 1.17x slower                                                     |
| Geometric mean | (ref)                                                       | 1.07x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 1.69 ms                                                     | 1.42 ms: 1.20x faster                                                     |
| regex_v8       | 23.8 ms                                                     | 20.1 ms: 1.19x faster                                                     |
| regex_dna      | 115 ms                                                      | 113 ms: 1.02x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 88.0 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                       | 1.07x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 87.9 ms: 1.05x faster                                                     |
| json_loads           | 15.1 us                                                     | 14.6 us: 1.03x faster                                                     |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.8 ms: 1.04x slower                                                     |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                    |
| xml_etree_generate   | 53.5 ms                                                     | 58.0 ms: 1.08x slower                                                     |
| json_dumps           | 6.19 ms                                                     | 6.76 ms: 1.09x slower                                                     |
| xml_etree_process    | 36.5 ms                                                     | 41.2 ms: 1.13x slower                                                     |
| unpickle_pure_python | 130 us                                                      | 148 us: 1.14x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 225 us: 1.21x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 24.1 ms: 1.01x faster                                                     |
| python_startup_no_site | 16.9 ms                                                     | 18.0 ms: 1.06x slower                                                     |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.80 ms: 1.04x slower                                                     |
| genshi_xml      | 33.9 ms                                                     | 35.1 ms: 1.04x slower                                                     |
| genshi_text     | 15.2 ms                                                     | 16.8 ms: 1.10x slower                                                     |
| django_template | 20.3 ms                                                     | 25.6 ms: 1.26x slower                                                     |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 531 us: 15.95x faster                                                     |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                      |
| async_tree_io              | 513 ms                                                      | 403 ms: 1.27x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 393 ms: 1.26x faster                                                      |
| async_tree_memoization     | 265 ms                                                      | 218 ms: 1.21x faster                                                      |
| async_tree_none            | 219 ms                                                      | 182 ms: 1.20x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.20x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.42 ms: 1.20x faster                                                     |
| deepcopy                   | 223 us                                                      | 187 us: 1.19x faster                                                      |
| regex_v8                   | 23.8 ms                                                     | 20.1 ms: 1.19x faster                                                     |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                      |
| json                       | 3.30 ms                                                     | 2.97 ms: 1.11x faster                                                     |
| deepcopy_memo              | 23.1 us                                                     | 20.9 us: 1.10x faster                                                     |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 347 ms: 1.10x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.91 us: 1.06x faster                                                     |
| xml_etree_parse            | 92.2 ms                                                     | 87.9 ms: 1.05x faster                                                     |
| json_loads                 | 15.1 us                                                     | 14.6 us: 1.03x faster                                                     |
| bench_mp_pool              | 84.2 ms                                                     | 82.3 ms: 1.02x faster                                                     |
| regex_dna                  | 115 ms                                                      | 113 ms: 1.02x faster                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.21 ms: 1.01x faster                                                     |
| python_startup             | 24.4 ms                                                     | 24.1 ms: 1.01x faster                                                     |
| shortest_path              | 355 ms                                                      | 353 ms: 1.01x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.82 ms: 1.01x faster                                                     |
| pidigits                   | 146 ms                                                      | 146 ms: 1.00x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 76.1 ms: 1.01x slower                                                     |
| sqlite_synth               | 1.59 us                                                     | 1.61 us: 1.02x slower                                                     |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.68 ms: 1.03x slower                                                     |
| go                         | 84.7 ms                                                     | 87.2 ms: 1.03x slower                                                     |
| asyncio_websockets         | 300 ms                                                      | 309 ms: 1.03x slower                                                      |
| coverage                   | 45.3 ms                                                     | 46.7 ms: 1.03x slower                                                     |
| float                      | 50.8 ms                                                     | 52.6 ms: 1.03x slower                                                     |
| mako                       | 6.56 ms                                                     | 6.80 ms: 1.04x slower                                                     |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.8 ms: 1.04x slower                                                     |
| genshi_xml                 | 33.9 ms                                                     | 35.1 ms: 1.04x slower                                                     |
| html5lib                   | 38.2 ms                                                     | 39.7 ms: 1.04x slower                                                     |
| dulwich_log                | 40.1 ms                                                     | 41.8 ms: 1.04x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                    |
| sphinx                     | 617 ms                                                      | 644 ms: 1.04x slower                                                      |
| 2to3                       | 215 ms                                                      | 225 ms: 1.05x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 66.4 ms: 1.05x slower                                                     |
| bpe_tokeniser              | 2.87 sec                                                    | 3.01 sec: 1.05x slower                                                    |
| mdp                        | 1.43 sec                                                    | 1.52 sec: 1.06x slower                                                    |
| python_startup_no_site     | 16.9 ms                                                     | 18.0 ms: 1.06x slower                                                     |
| sympy_sum                  | 85.2 ms                                                     | 90.7 ms: 1.07x slower                                                     |
| sympy_str                  | 167 ms                                                      | 179 ms: 1.07x slower                                                      |
| sympy_expand               | 286 ms                                                      | 306 ms: 1.07x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 60.9 ms: 1.07x slower                                                     |
| crypto_pyaes               | 45.6 ms                                                     | 49.1 ms: 1.08x slower                                                     |
| pycparser                  | 695 ms                                                      | 750 ms: 1.08x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 77.7 ms: 1.08x slower                                                     |
| async_generators           | 223 ms                                                      | 241 ms: 1.08x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 58.0 ms: 1.08x slower                                                     |
| docutils                   | 1.53 sec                                                    | 1.66 sec: 1.09x slower                                                    |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                     |
| regex_compile              | 80.7 ms                                                     | 88.0 ms: 1.09x slower                                                     |
| json_dumps                 | 6.19 ms                                                     | 6.76 ms: 1.09x slower                                                     |
| typing_runtime_protocols   | 103 us                                                      | 113 us: 1.09x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 13.5 ms: 1.09x slower                                                     |
| logging_simple             | 5.77 us                                                     | 6.32 us: 1.10x slower                                                     |
| fannkuch                   | 252 ms                                                      | 276 ms: 1.10x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 16.8 ms: 1.10x slower                                                     |
| logging_format             | 6.18 us                                                     | 6.84 us: 1.11x slower                                                     |
| sqlglot_optimize           | 32.5 ms                                                     | 36.1 ms: 1.11x slower                                                     |
| generators                 | 19.0 ms                                                     | 21.1 ms: 1.11x slower                                                     |
| pprint_safe_repr           | 485 ms                                                      | 543 ms: 1.12x slower                                                      |
| scimark_fft                | 175 ms                                                      | 196 ms: 1.12x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 41.2 ms: 1.13x slower                                                     |
| pyflate                    | 283 ms                                                      | 320 ms: 1.13x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.11 sec: 1.13x slower                                                    |
| unpickle_pure_python       | 130 us                                                      | 148 us: 1.14x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 62.3 ns: 1.14x slower                                                     |
| chaos                      | 37.9 ms                                                     | 43.5 ms: 1.15x slower                                                     |
| nqueens                    | 56.1 ms                                                     | 64.4 ms: 1.15x slower                                                     |
| sqlglot_normalize          | 172 ms                                                      | 197 ms: 1.15x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.45 ms: 1.16x slower                                                     |
| sqlglot_transpile          | 953 us                                                      | 1.11 ms: 1.16x slower                                                     |
| sqlglot_parse              | 764 us                                                      | 887 us: 1.16x slower                                                      |
| richards                   | 26.3 ms                                                     | 30.5 ms: 1.16x slower                                                     |
| richards_super             | 29.8 ms                                                     | 34.8 ms: 1.17x slower                                                     |
| nbody                      | 66.3 ms                                                     | 77.8 ms: 1.17x slower                                                     |
| comprehensions             | 10.4 us                                                     | 12.3 us: 1.19x slower                                                     |
| deltablue                  | 1.89 ms                                                     | 2.26 ms: 1.19x slower                                                     |
| scimark_sor                | 76.2 ms                                                     | 91.1 ms: 1.20x slower                                                     |
| scimark_monte_carlo        | 40.7 ms                                                     | 48.8 ms: 1.20x slower                                                     |
| pickle_pure_python         | 186 us                                                      | 225 us: 1.21x slower                                                      |
| many_optionals             | 361 us                                                      | 438 us: 1.21x slower                                                      |
| raytrace                   | 153 ms                                                      | 188 ms: 1.23x slower                                                      |
| django_template            | 20.3 ms                                                     | 25.6 ms: 1.26x slower                                                     |
| subparsers                 | 10.9 ms                                                     | 16.5 ms: 1.52x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                              |

Benchmark hidden because not significant (5): pylint, k_core, gc_traversal, connected_components, bench_thread_pool
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20250107-3.14.0a3+-7de6e22/bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: mypy2

- Geometric mean (including insignificant results): 1.013x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown