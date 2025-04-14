# Results vs. 3.13.0

- fork: python
- ref: 295b53df2aa18deb625a
- machine: windows-amd64
- commit hash: 295b53d
- commit date: 2025-03-18
- overall geometric mean: 1.018x faster
- HPT reliability: 96.84%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 227 ms: 1.05x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.75 sec: 1.14x slower                                                      |
| html5lib       | 38.2 ms                                                     | 41.3 ms: 1.08x slower                                                       |
| sphinx         | 617 ms                                                      | 670 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                       | 1.09x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                        |
| async_tree_io              | 513 ms                                                      | 418 ms: 1.23x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 411 ms: 1.21x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 221 ms: 1.20x faster                                                        |
| async_tree_none            | 219 ms                                                      | 186 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 175 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 338 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 341 ms: 1.12x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 307 ms: 1.02x slower                                                        |
| async_generators           | 223 ms                                                      | 246 ms: 1.11x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 58.6 ms: 1.13x faster                                                       |
| float          | 50.8 ms                                                     | 47.3 ms: 1.08x faster                                                       |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.2 ms: 1.67x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.01x slower                                                        |
| regex_compile  | 80.7 ms                                                     | 86.2 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.22 sec: 1.12x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 87.6 ms: 1.05x faster                                                       |
| unpickle_pure_python | 130 us                                                      | 126 us: 1.03x faster                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 53.0 ms: 1.01x faster                                                       |
| json_loads           | 15.1 us                                                     | 15.3 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.1 ms: 1.04x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 38.9 ms: 1.07x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.98 ms: 1.13x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 222 us: 1.19x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 20.6 ms: 1.22x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.81 ms: 1.13x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 16.9 ms: 1.11x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 38.3 ms: 1.13x slower                                                       |
| django_template | 20.3 ms                                                     | 26.2 ms: 1.29x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.09x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 537 us: 15.77x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 32.7 ms: 2.30x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.2 ms: 1.67x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 18.0 us: 1.28x faster                                                       |
| async_tree_io              | 513 ms                                                      | 418 ms: 1.23x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 411 ms: 1.21x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 221 ms: 1.20x faster                                                        |
| async_tree_none            | 219 ms                                                      | 186 ms: 1.18x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                       |
| deepcopy                   | 223 us                                                      | 193 us: 1.16x faster                                                        |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.27 ms: 1.14x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 175 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 338 ms: 1.13x faster                                                        |
| mako                       | 6.56 ms                                                     | 5.81 ms: 1.13x faster                                                       |
| nbody                      | 66.3 ms                                                     | 58.6 ms: 1.13x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.22 sec: 1.12x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 341 ms: 1.12x faster                                                        |
| scimark_fft                | 175 ms                                                      | 158 ms: 1.11x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 58.8 ms: 1.08x faster                                                       |
| float                      | 50.8 ms                                                     | 47.3 ms: 1.08x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.58 ms: 1.06x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 87.6 ms: 1.05x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.74 sec: 1.05x faster                                                      |
| json                       | 3.30 ms                                                     | 3.16 ms: 1.04x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.53 us: 1.04x faster                                                       |
| unpickle_pure_python       | 130 us                                                      | 126 us: 1.03x faster                                                        |
| fannkuch                   | 252 ms                                                      | 246 ms: 1.02x faster                                                        |
| k_core                     | 1.70 sec                                                    | 1.67 sec: 1.02x faster                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 53.0 ms: 1.01x faster                                                       |
| json_loads                 | 15.1 us                                                     | 15.3 us: 1.01x slower                                                       |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                        |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.01x slower                                                        |
| connected_components       | 320 ms                                                      | 326 ms: 1.02x slower                                                        |
| asyncio_websockets         | 300 ms                                                      | 307 ms: 1.02x slower                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.25 ms: 1.02x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.04 ms: 1.04x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.1 ms: 1.04x slower                                                       |
| coverage                   | 45.3 ms                                                     | 47.4 ms: 1.05x slower                                                       |
| go                         | 84.7 ms                                                     | 88.7 ms: 1.05x slower                                                       |
| 2to3                       | 215 ms                                                      | 227 ms: 1.05x slower                                                        |
| meteor_contest             | 72.0 ms                                                     | 75.9 ms: 1.05x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 89.1 ms: 1.06x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 38.9 ms: 1.07x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 86.2 ms: 1.07x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 519 ms: 1.07x slower                                                        |
| scimark_sor                | 76.2 ms                                                     | 81.8 ms: 1.07x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 91.7 ms: 1.08x slower                                                       |
| sympy_str                  | 167 ms                                                      | 180 ms: 1.08x slower                                                        |
| pycparser                  | 695 ms                                                      | 750 ms: 1.08x slower                                                        |
| bench_thread_pool          | 810 us                                                      | 874 us: 1.08x slower                                                        |
| html5lib                   | 38.2 ms                                                     | 41.3 ms: 1.08x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 44.1 ms: 1.08x slower                                                       |
| generators                 | 19.0 ms                                                     | 20.6 ms: 1.08x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 43.5 ms: 1.09x slower                                                       |
| sphinx                     | 617 ms                                                      | 670 ms: 1.09x slower                                                        |
| typing_runtime_protocols   | 103 us                                                      | 112 us: 1.09x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 59.5 ns: 1.09x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.5 ms: 1.10x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 61.6 ms: 1.10x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 62.3 ms: 1.10x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 50.1 ms: 1.10x slower                                                       |
| sympy_expand               | 286 ms                                                      | 315 ms: 1.10x slower                                                        |
| async_generators           | 223 ms                                                      | 246 ms: 1.11x slower                                                        |
| mdp                        | 1.43 sec                                                    | 1.58 sec: 1.11x slower                                                      |
| richards_super             | 29.8 ms                                                     | 33.0 ms: 1.11x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 16.9 ms: 1.11x slower                                                       |
| richards                   | 26.3 ms                                                     | 29.4 ms: 1.12x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.10 sec: 1.12x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.98 ms: 1.13x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.7 us: 1.13x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 38.3 ms: 1.13x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.75 sec: 1.14x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.63 us: 1.15x slower                                                       |
| logging_format             | 6.18 us                                                     | 7.17 us: 1.16x slower                                                       |
| chaos                      | 37.9 ms                                                     | 44.1 ms: 1.16x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.53 ms: 1.18x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 222 us: 1.19x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 20.6 ms: 1.22x slower                                                       |
| raytrace                   | 153 ms                                                      | 194 ms: 1.26x slower                                                        |
| many_optionals             | 361 us                                                      | 457 us: 1.27x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.40 ms: 1.27x slower                                                       |
| django_template            | 20.3 ms                                                     | 26.2 ms: 1.29x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.6 ms: 1.53x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (4): pylint, pyflate, shortest_path, deepcopy_reduce
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250318-3.14.0a6+-295b53d-JIT/bm-20250318-pythonperf1-amd64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.018x faster

# HPT report

- Reliability score: 96.84% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown