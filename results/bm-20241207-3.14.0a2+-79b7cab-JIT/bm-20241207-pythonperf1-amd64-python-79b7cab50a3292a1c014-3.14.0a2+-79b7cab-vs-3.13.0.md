# Results vs. 3.13.0

- fork: python
- ref: 79b7cab50a3292a1c014
- machine: windows-amd64
- commit hash: 79b7cab
- commit date: 2024-12-07
- overall geometric mean: 1.031x faster
- HPT reliability: 79.01%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 217 ms: 1.01x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.71 sec: 1.11x slower                                                      |
| sphinx         | 617 ms                                                      | 667 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 513 ms                                                      | 396 ms: 1.29x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 221 ms: 1.27x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 397 ms: 1.25x faster                                                        |
| async_tree_none            | 219 ms                                                      | 182 ms: 1.20x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 221 ms: 1.20x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 174 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 359 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 364 ms: 1.05x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                       |
| async_generators           | 223 ms                                                      | 262 ms: 1.17x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.10x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 53.5 ms: 1.24x faster                                                       |
| float          | 50.8 ms                                                     | 48.8 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 18.4 ms: 1.30x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.43 ms: 1.19x faster                                                       |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                        |
| regex_compile  | 80.7 ms                                                     | 81.3 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 111 us: 1.17x faster                                                        |
| xml_etree_parse      | 92.2 ms                                                     | 84.4 ms: 1.09x faster                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 50.4 ms: 1.06x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.30 sec: 1.06x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 57.5 ms: 1.05x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.5 us: 1.04x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 35.3 ms: 1.03x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 6.50 ms: 1.05x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 203 us: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 23.5 ms: 1.04x faster                                                       |
| python_startup_no_site | 16.9 ms                                                     | 17.8 ms: 1.05x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.17 ms: 1.27x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 18.1 ms: 1.19x slower                                                       |
| django_template | 20.3 ms                                                     | 26.1 ms: 1.29x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 45.9 ms: 1.35x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.13x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 517 us: 16.39x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 16.7 us: 1.39x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 18.4 ms: 1.30x faster                                                       |
| async_tree_io              | 513 ms                                                      | 396 ms: 1.29x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 221 ms: 1.27x faster                                                        |
| mako                       | 6.56 ms                                                     | 5.17 ms: 1.27x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 397 ms: 1.25x faster                                                        |
| nbody                      | 66.3 ms                                                     | 53.5 ms: 1.24x faster                                                       |
| async_tree_none            | 219 ms                                                      | 182 ms: 1.20x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 221 ms: 1.20x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.43 ms: 1.19x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 64.1 ms: 1.19x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.21 ms: 1.18x faster                                                       |
| unpickle_pure_python       | 130 us                                                      | 111 us: 1.17x faster                                                        |
| deepcopy                   | 223 us                                                      | 191 us: 1.17x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 54.7 ms: 1.16x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 174 ms: 1.15x faster                                                        |
| scimark_fft                | 175 ms                                                      | 153 ms: 1.14x faster                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 36.2 ms: 1.13x faster                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.09 ms: 1.12x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.34 ms: 1.12x faster                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 41.1 ms: 1.11x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 84.4 ms: 1.09x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.65 sec: 1.09x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.57 sec: 1.08x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.88 us: 1.08x faster                                                       |
| json                       | 3.30 ms                                                     | 3.09 ms: 1.07x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 50.4 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 359 ms: 1.06x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.30 sec: 1.06x faster                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 57.5 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 364 ms: 1.05x faster                                                        |
| scimark_lu                 | 56.7 ms                                                     | 54.1 ms: 1.05x faster                                                       |
| pprint_safe_repr           | 485 ms                                                      | 462 ms: 1.05x faster                                                        |
| fannkuch                   | 252 ms                                                      | 240 ms: 1.05x faster                                                        |
| pprint_pformat             | 977 ms                                                      | 933 ms: 1.05x faster                                                        |
| float                      | 50.8 ms                                                     | 48.8 ms: 1.04x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.5 us: 1.04x faster                                                       |
| shortest_path              | 355 ms                                                      | 342 ms: 1.04x faster                                                        |
| python_startup             | 24.4 ms                                                     | 23.5 ms: 1.04x faster                                                       |
| xml_etree_process          | 36.5 ms                                                     | 35.3 ms: 1.03x faster                                                       |
| gc_traversal               | 1.96 ms                                                     | 1.90 ms: 1.03x faster                                                       |
| connected_components       | 320 ms                                                      | 310 ms: 1.03x faster                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 81.8 ms: 1.03x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 74.3 ms: 1.01x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.57 us: 1.01x faster                                                       |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                        |
| regex_compile              | 80.7 ms                                                     | 81.3 ms: 1.01x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 72.6 ms: 1.01x slower                                                       |
| 2to3                       | 215 ms                                                      | 217 ms: 1.01x slower                                                        |
| pyflate                    | 283 ms                                                      | 287 ms: 1.01x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 40.7 ms: 1.01x slower                                                       |
| coverage                   | 45.3 ms                                                     | 46.8 ms: 1.03x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 56.4 ns: 1.03x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.50 ms: 1.05x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 17.8 ms: 1.05x slower                                                       |
| go                         | 84.7 ms                                                     | 89.7 ms: 1.06x slower                                                       |
| sympy_str                  | 167 ms                                                      | 177 ms: 1.06x slower                                                        |
| sympy_expand               | 286 ms                                                      | 303 ms: 1.06x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 90.7 ms: 1.06x slower                                                       |
| chaos                      | 37.9 ms                                                     | 40.8 ms: 1.08x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.66 us: 1.08x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 111 us: 1.08x slower                                                        |
| sphinx                     | 617 ms                                                      | 667 ms: 1.08x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.27 us: 1.09x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 203 us: 1.09x slower                                                        |
| sympy_integrate            | 12.3 ms                                                     | 13.5 ms: 1.10x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.59 sec: 1.11x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 62.6 ms: 1.11x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.71 sec: 1.11x slower                                                      |
| comprehensions             | 10.4 us                                                     | 11.7 us: 1.13x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 864 us: 1.13x slower                                                        |
| sqlglot_transpile          | 953 us                                                      | 1.10 ms: 1.15x slower                                                       |
| async_generators           | 223 ms                                                      | 262 ms: 1.17x slower                                                        |
| sqlglot_optimize           | 32.5 ms                                                     | 38.3 ms: 1.18x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 18.1 ms: 1.19x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 206 ms: 1.20x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.29 ms: 1.21x slower                                                       |
| generators                 | 19.0 ms                                                     | 23.7 ms: 1.25x slower                                                       |
| many_optionals             | 361 us                                                      | 458 us: 1.27x slower                                                        |
| django_template            | 20.3 ms                                                     | 26.1 ms: 1.29x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.95 ms: 1.29x slower                                                       |
| richards_super             | 29.8 ms                                                     | 39.4 ms: 1.32x slower                                                       |
| raytrace                   | 153 ms                                                      | 204 ms: 1.33x slower                                                        |
| richards                   | 26.3 ms                                                     | 35.2 ms: 1.34x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 45.9 ms: 1.35x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 15.7 ms: 1.45x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (6): pylint, pycparser, pidigits, bench_thread_pool, html5lib, asyncio_websockets
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.031x faster

# HPT report

- Reliability score: 79.01% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown