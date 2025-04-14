# Results vs. 3.13.0

- fork: brandtbucher
- ref: msvc_musttail
- machine: windows-amd64
- commit hash: 06bc3bd
- commit date: 2025-03-07
- overall geometric mean: 1.006x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 229 ms: 1.07x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.71 sec: 1.12x slower                                                     |
| html5lib       | 38.2 ms                                                     | 40.1 ms: 1.05x slower                                                      |
| sphinx         | 617 ms                                                      | 669 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 218 ms: 1.29x faster                                                       |
| async_tree_io              | 513 ms                                                      | 426 ms: 1.20x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 417 ms: 1.19x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 225 ms: 1.18x faster                                                       |
| async_tree_none            | 219 ms                                                      | 187 ms: 1.17x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 178 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 343 ms: 1.11x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                                       |
| async_generators           | 223 ms                                                      | 221 ms: 1.01x faster                                                       |
| coroutines                 | 12.5 ms                                                     | 13.1 ms: 1.05x slower                                                      |
| asyncio_websockets         | 300 ms                                                      | 315 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.8 ms: 1.13x faster                                                      |
| nbody          | 66.3 ms                                                     | 67.9 ms: 1.03x slower                                                      |
| pidigits       | 146 ms                                                      | 151 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.2 ms: 1.81x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.42 ms: 1.20x faster                                                      |
| regex_dna      | 115 ms                                                      | 113 ms: 1.02x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 87.2 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.4 ms: 1.05x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 56.7 ms: 1.06x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 39.9 ms: 1.09x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 6.86 ms: 1.11x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 150 us: 1.16x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 230 us: 1.23x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                               |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.9 ms: 1.06x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.79 ms: 1.03x slower                                                      |
| genshi_xml      | 33.9 ms                                                     | 36.4 ms: 1.07x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 16.5 ms: 1.08x slower                                                      |
| django_template | 20.3 ms                                                     | 25.7 ms: 1.27x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 504 us: 16.82x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 31.9 ms: 2.36x faster                                                      |
| regex_v8                   | 23.8 ms                                                     | 13.2 ms: 1.81x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 218 ms: 1.29x faster                                                       |
| deepcopy                   | 223 us                                                      | 183 us: 1.22x faster                                                       |
| async_tree_io              | 513 ms                                                      | 426 ms: 1.20x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.42 ms: 1.20x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 417 ms: 1.19x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 225 ms: 1.18x faster                                                       |
| async_tree_none            | 219 ms                                                      | 187 ms: 1.17x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 19.9 us: 1.16x faster                                                      |
| float                      | 50.8 ms                                                     | 44.8 ms: 1.13x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 178 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 343 ms: 1.11x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 57.8 ms: 1.10x faster                                                      |
| json                       | 3.30 ms                                                     | 3.04 ms: 1.09x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.91 us: 1.06x faster                                                      |
| regex_dna                  | 115 ms                                                      | 113 ms: 1.02x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.78 ms: 1.01x faster                                                      |
| async_generators           | 223 ms                                                      | 221 ms: 1.01x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.90 sec: 1.01x slower                                                     |
| shortest_path              | 355 ms                                                      | 360 ms: 1.01x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| create_gc_cycles           | 1.22 ms                                                     | 1.25 ms: 1.02x slower                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.66 ms: 1.02x slower                                                      |
| go                         | 84.7 ms                                                     | 86.6 ms: 1.02x slower                                                      |
| nbody                      | 66.3 ms                                                     | 67.9 ms: 1.03x slower                                                      |
| scimark_fft                | 175 ms                                                      | 180 ms: 1.03x slower                                                       |
| pidigits                   | 146 ms                                                      | 151 ms: 1.03x slower                                                       |
| connected_components       | 320 ms                                                      | 330 ms: 1.03x slower                                                       |
| mako                       | 6.56 ms                                                     | 6.79 ms: 1.03x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.04 ms: 1.04x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 87.8 ms: 1.04x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 108 us: 1.04x slower                                                       |
| sympy_expand               | 286 ms                                                      | 299 ms: 1.05x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 847 us: 1.05x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.1 ms: 1.05x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.4 ms: 1.05x slower                                                      |
| asyncio_websockets         | 300 ms                                                      | 315 ms: 1.05x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 40.1 ms: 1.05x slower                                                      |
| sympy_str                  | 167 ms                                                      | 176 ms: 1.05x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 90.0 ms: 1.06x slower                                                      |
| generators                 | 19.0 ms                                                     | 20.1 ms: 1.06x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 56.7 ms: 1.06x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.9 ms: 1.06x slower                                                      |
| 2to3                       | 215 ms                                                      | 229 ms: 1.07x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 42.8 ms: 1.07x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 76.9 ms: 1.07x slower                                                      |
| pycparser                  | 695 ms                                                      | 746 ms: 1.07x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 36.4 ms: 1.07x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 49.1 ms: 1.08x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 87.2 ms: 1.08x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 59.0 ns: 1.08x slower                                                      |
| coverage                   | 45.3 ms                                                     | 49.1 ms: 1.08x slower                                                      |
| sphinx                     | 617 ms                                                      | 669 ms: 1.08x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 16.5 ms: 1.08x slower                                                      |
| chaos                      | 37.9 ms                                                     | 41.1 ms: 1.09x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 39.9 ms: 1.09x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 13.5 ms: 1.09x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 533 ms: 1.10x slower                                                       |
| pyflate                    | 283 ms                                                      | 312 ms: 1.10x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 84.2 ms: 1.10x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.86 ms: 1.11x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.08 sec: 1.11x slower                                                     |
| scimark_monte_carlo        | 40.7 ms                                                     | 45.2 ms: 1.11x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.41 us: 1.11x slower                                                      |
| mdp                        | 1.43 sec                                                    | 1.59 sec: 1.11x slower                                                     |
| comprehensions             | 10.4 us                                                     | 11.5 us: 1.11x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.28 ms: 1.11x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.88 us: 1.11x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.71 sec: 1.12x slower                                                     |
| fannkuch                   | 252 ms                                                      | 282 ms: 1.12x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 63.1 ms: 1.12x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 64.1 ms: 1.13x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 150 us: 1.16x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.30 ms: 1.21x slower                                                      |
| many_optionals             | 361 us                                                      | 445 us: 1.23x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 230 us: 1.23x slower                                                       |
| raytrace                   | 153 ms                                                      | 193 ms: 1.26x slower                                                       |
| django_template            | 20.3 ms                                                     | 25.7 ms: 1.27x slower                                                      |
| richards                   | 26.3 ms                                                     | 35.6 ms: 1.36x slower                                                      |
| richards_super             | 29.8 ms                                                     | 40.6 ms: 1.36x slower                                                      |
| subparsers                 | 10.9 ms                                                     | 16.4 ms: 1.51x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (5): sqlite_synth, json_loads, xml_etree_parse, pylint, k_core
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250307-3.14.0a5+-06bc3bd/bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.006x faster

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown