# Results vs. 3.13.0

- fork: python
- ref: 79b7cab50a3292a1c014
- machine: windows-amd64
- commit hash: 79b7cab
- commit date: 2024-12-07
- overall geometric mean: 1.031x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 224 ms: 1.04x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                      |
| html5lib       | 38.2 ms                                                     | 40.4 ms: 1.06x slower                                                       |
| sphinx         | 617 ms                                                      | 650 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 513 ms                                                      | 407 ms: 1.26x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 226 ms: 1.24x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 413 ms: 1.20x faster                                                        |
| async_tree_none            | 219 ms                                                      | 185 ms: 1.19x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 230 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 182 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 361 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 371 ms: 1.03x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 310 ms: 1.03x slower                                                        |
| async_generators           | 223 ms                                                      | 244 ms: 1.10x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.12x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 146 ms                                                      | 147 ms: 1.00x slower                                                        |
| float          | 50.8 ms                                                     | 54.8 ms: 1.08x slower                                                       |
| nbody          | 66.3 ms                                                     | 76.5 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.69 ms                                                     | 1.53 ms: 1.10x faster                                                       |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                                        |
| regex_compile  | 80.7 ms                                                     | 89.9 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 90.6 ms: 1.02x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.6 ms: 1.05x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 58.5 ms: 1.09x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 41.5 ms: 1.14x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 7.18 ms: 1.16x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.59 sec: 1.16x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 157 us: 1.21x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 227 us: 1.22x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.11x slower                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 23.4 ms: 1.04x faster                                                       |
| python_startup_no_site | 16.9 ms                                                     | 17.5 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 36.3 ms: 1.07x slower                                                       |
| mako            | 6.56 ms                                                     | 7.15 ms: 1.09x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 16.9 ms: 1.11x slower                                                       |
| django_template | 20.3 ms                                                     | 25.7 ms: 1.27x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.13x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 526 us: 16.11x faster                                                       |
| async_tree_io              | 513 ms                                                      | 407 ms: 1.26x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 226 ms: 1.24x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 413 ms: 1.20x faster                                                        |
| async_tree_none            | 219 ms                                                      | 185 ms: 1.19x faster                                                        |
| deepcopy                   | 223 us                                                      | 192 us: 1.17x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 230 ms: 1.15x faster                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.09 ms: 1.12x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.53 ms: 1.10x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 20.9 us: 1.10x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 182 ms: 1.10x faster                                                        |
| pylint                     | 205 ms                                                      | 191 ms: 1.08x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.90 us: 1.06x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 361 ms: 1.05x faster                                                        |
| python_startup             | 24.4 ms                                                     | 23.4 ms: 1.04x faster                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 81.6 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 371 ms: 1.03x faster                                                        |
| gc_traversal               | 1.96 ms                                                     | 1.92 ms: 1.02x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.66 sec: 1.02x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.75 ms: 1.02x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 90.6 ms: 1.02x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 74.6 ms: 1.01x faster                                                       |
| pidigits                   | 146 ms                                                      | 147 ms: 1.00x slower                                                        |
| coverage                   | 45.3 ms                                                     | 45.5 ms: 1.01x slower                                                       |
| shortest_path              | 355 ms                                                      | 359 ms: 1.01x slower                                                        |
| connected_components       | 320 ms                                                      | 325 ms: 1.02x slower                                                        |
| mdp                        | 1.43 sec                                                    | 1.47 sec: 1.02x slower                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.63 us: 1.03x slower                                                       |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.03x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 17.5 ms: 1.03x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 310 ms: 1.03x slower                                                        |
| go                         | 84.7 ms                                                     | 87.6 ms: 1.03x slower                                                       |
| pycparser                  | 695 ms                                                      | 722 ms: 1.04x slower                                                        |
| 2to3                       | 215 ms                                                      | 224 ms: 1.04x slower                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 47.8 ms: 1.05x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.6 ms: 1.05x slower                                                       |
| sphinx                     | 617 ms                                                      | 650 ms: 1.05x slower                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 3.03 sec: 1.06x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 90.0 ms: 1.06x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 40.4 ms: 1.06x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 77.2 ms: 1.07x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 36.3 ms: 1.07x slower                                                       |
| sympy_str                  | 167 ms                                                      | 179 ms: 1.07x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 43.0 ms: 1.07x slower                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.80 ms: 1.07x slower                                                       |
| sympy_expand               | 286 ms                                                      | 307 ms: 1.08x slower                                                        |
| float                      | 50.8 ms                                                     | 54.8 ms: 1.08x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 112 us: 1.08x slower                                                        |
| docutils                   | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 13.4 ms: 1.09x slower                                                       |
| spectral_norm              | 63.4 ms                                                     | 69.1 ms: 1.09x slower                                                       |
| mako                       | 6.56 ms                                                     | 7.15 ms: 1.09x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.74 us: 1.09x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 58.5 ms: 1.09x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.32 us: 1.09x slower                                                       |
| async_generators           | 223 ms                                                      | 244 ms: 1.10x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 16.9 ms: 1.11x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 89.9 ms: 1.11x slower                                                       |
| fannkuch                   | 252 ms                                                      | 282 ms: 1.12x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.12x slower                                                       |
| chaos                      | 37.9 ms                                                     | 42.9 ms: 1.13x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.11 sec: 1.13x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 41.5 ms: 1.14x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 553 ms: 1.14x slower                                                        |
| pyflate                    | 283 ms                                                      | 323 ms: 1.14x slower                                                        |
| sqlglot_optimize           | 32.5 ms                                                     | 37.3 ms: 1.15x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 64.3 ms: 1.15x slower                                                       |
| generators                 | 19.0 ms                                                     | 21.9 ms: 1.15x slower                                                       |
| nbody                      | 66.3 ms                                                     | 76.5 ms: 1.16x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 7.18 ms: 1.16x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.59 sec: 1.16x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 66.2 ms: 1.17x slower                                                       |
| comprehensions             | 10.4 us                                                     | 12.1 us: 1.17x slower                                                       |
| scimark_fft                | 175 ms                                                      | 205 ms: 1.17x slower                                                        |
| hexiom                     | 3.84 ms                                                     | 4.52 ms: 1.18x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.12 ms: 1.18x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 903 us: 1.18x slower                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 48.1 ms: 1.18x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 205 ms: 1.19x slower                                                        |
| scimark_sor                | 76.2 ms                                                     | 91.8 ms: 1.20x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 157 us: 1.21x slower                                                        |
| richards_super             | 29.8 ms                                                     | 36.1 ms: 1.21x slower                                                       |
| many_optionals             | 361 us                                                      | 441 us: 1.22x slower                                                        |
| pickle_pure_python         | 186 us                                                      | 227 us: 1.22x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.32 ms: 1.23x slower                                                       |
| richards                   | 26.3 ms                                                     | 32.4 ms: 1.23x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 67.3 ns: 1.23x slower                                                       |
| raytrace                   | 153 ms                                                      | 193 ms: 1.26x slower                                                        |
| django_template            | 20.3 ms                                                     | 25.7 ms: 1.27x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.2 ms: 1.50x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (4): json, bench_thread_pool, json_loads, regex_v8
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.031x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown