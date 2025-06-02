# Results vs. 3.13.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.418x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.66x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 338 ms: 1.57x slower                                                       |
| docutils       | 1.53 sec                                                    | 4.14 sec: 2.71x slower                                                     |
| html5lib       | 38.2 ms                                                     | 63.5 ms: 1.66x slower                                                      |
| sphinx         | 617 ms                                                      | 1.27 sec: 2.06x slower                                                     |
| Geometric mean | (ref)                                                       | 1.95x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 144 ms: 2.09x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 549 ms: 1.10x slower                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 310 ms: 1.10x slower                                                       |
| async_tree_io              | 513 ms                                                      | 575 ms: 1.12x slower                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 452 ms: 1.18x slower                                                       |
| async_tree_none_tg         | 200 ms                                                      | 246 ms: 1.23x slower                                                       |
| async_tree_none            | 219 ms                                                      | 273 ms: 1.25x slower                                                       |
| async_tree_memoization     | 265 ms                                                      | 333 ms: 1.26x slower                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 480 ms: 1.26x slower                                                       |
| async_generators           | 223 ms                                                      | 412 ms: 1.85x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 32.4 ms: 2.59x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.22x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 146 ms                                                      | 141 ms: 1.04x faster                                                       |
| float          | 50.8 ms                                                     | 97.2 ms: 1.91x slower                                                      |
| nbody          | 66.3 ms                                                     | 179 ms: 2.71x slower                                                       |
| Geometric mean | (ref)                                                       | 1.71x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 16.9 ms: 1.41x faster                                                      |
| regex_dna      | 115 ms                                                      | 113 ms: 1.02x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.82 ms: 1.07x slower                                                      |
| regex_compile  | 80.7 ms                                                     | 160 ms: 1.98x slower                                                       |
| Geometric mean | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 111 ms: 1.20x slower                                                       |
| json_loads           | 15.1 us                                                     | 22.3 us: 1.48x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 9.47 ms: 1.53x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 93.9 ms: 1.55x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 110 ms: 2.06x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 79.8 ms: 2.19x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 454 us: 2.44x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 364 us: 2.80x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 5.09 sec: 3.71x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.99x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 27.9 ms: 1.14x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 20.2 ms: 1.20x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.17x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 66.2 ms: 1.95x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 33.4 ms: 2.20x slower                                                      |
| django_template | 20.3 ms                                                     | 45.9 ms: 2.26x slower                                                      |
| mako            | 6.56 ms                                                     | 16.9 ms: 2.58x slower                                                      |
| Geometric mean  | (ref)                                                       | 2.24x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 849 us: 9.97x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 35.3 ms: 2.14x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 144 ms: 2.09x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 16.9 ms: 1.41x faster                                                      |
| gc_traversal               | 1.96 ms                                                     | 1.80 ms: 1.09x faster                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.13 ms: 1.08x faster                                                      |
| pidigits                   | 146 ms                                                      | 141 ms: 1.04x faster                                                       |
| regex_dna                  | 115 ms                                                      | 113 ms: 1.02x faster                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 88.6 ms: 1.05x slower                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.69 us: 1.07x slower                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.82 ms: 1.07x slower                                                      |
| async_tree_io_tg           | 497 ms                                                      | 549 ms: 1.10x slower                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 310 ms: 1.10x slower                                                       |
| async_tree_io              | 513 ms                                                      | 575 ms: 1.12x slower                                                       |
| python_startup             | 24.4 ms                                                     | 27.9 ms: 1.14x slower                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 452 ms: 1.18x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 20.2 ms: 1.20x slower                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 111 ms: 1.20x slower                                                       |
| async_tree_none_tg         | 200 ms                                                      | 246 ms: 1.23x slower                                                       |
| async_tree_none            | 219 ms                                                      | 273 ms: 1.25x slower                                                       |
| json                       | 3.30 ms                                                     | 4.14 ms: 1.25x slower                                                      |
| async_tree_memoization     | 265 ms                                                      | 333 ms: 1.26x slower                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 480 ms: 1.26x slower                                                       |
| pylint                     | 205 ms                                                      | 282 ms: 1.37x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 56.8 ms: 1.42x slower                                                      |
| json_loads                 | 15.1 us                                                     | 22.3 us: 1.48x slower                                                      |
| deepcopy                   | 223 us                                                      | 334 us: 1.50x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 9.47 ms: 1.53x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 1.24 ms: 1.54x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 93.9 ms: 1.55x slower                                                      |
| 2to3                       | 215 ms                                                      | 338 ms: 1.57x slower                                                       |
| mdp                        | 1.43 sec                                                    | 2.30 sec: 1.61x slower                                                     |
| html5lib                   | 38.2 ms                                                     | 63.5 ms: 1.66x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 120 ms: 1.67x slower                                                       |
| telco                      | 4.85 ms                                                     | 8.09 ms: 1.67x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 145 ms: 1.70x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 20.9 ms: 1.70x slower                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 3.48 us: 1.72x slower                                                      |
| sympy_expand               | 286 ms                                                      | 491 ms: 1.72x slower                                                       |
| sympy_str                  | 167 ms                                                      | 292 ms: 1.75x slower                                                       |
| many_optionals             | 361 us                                                      | 641 us: 1.77x slower                                                       |
| k_core                     | 1.70 sec                                                    | 3.07 sec: 1.81x slower                                                     |
| async_generators           | 223 ms                                                      | 412 ms: 1.85x slower                                                       |
| coverage                   | 45.3 ms                                                     | 84.5 ms: 1.86x slower                                                      |
| deepcopy_memo              | 23.1 us                                                     | 43.7 us: 1.89x slower                                                      |
| logging_format             | 6.18 us                                                     | 11.8 us: 1.91x slower                                                      |
| float                      | 50.8 ms                                                     | 97.2 ms: 1.91x slower                                                      |
| logging_simple             | 5.77 us                                                     | 11.2 us: 1.94x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 66.2 ms: 1.95x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 202 us: 1.95x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 160 ms: 1.98x slower                                                       |
| shortest_path              | 355 ms                                                      | 721 ms: 2.03x slower                                                       |
| sphinx                     | 617 ms                                                      | 1.27 sec: 2.06x slower                                                     |
| xml_etree_generate         | 53.5 ms                                                     | 110 ms: 2.06x slower                                                       |
| generators                 | 19.0 ms                                                     | 39.3 ms: 2.07x slower                                                      |
| connected_components       | 320 ms                                                      | 681 ms: 2.13x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 79.8 ms: 2.19x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 33.4 ms: 2.20x slower                                                      |
| pyflate                    | 283 ms                                                      | 626 ms: 2.21x slower                                                       |
| go                         | 84.7 ms                                                     | 189 ms: 2.23x slower                                                       |
| django_template            | 20.3 ms                                                     | 45.9 ms: 2.26x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 127 ms: 2.27x slower                                                       |
| fannkuch                   | 252 ms                                                      | 596 ms: 2.37x slower                                                       |
| scimark_fft                | 175 ms                                                      | 415 ms: 2.37x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 454 us: 2.44x slower                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 6.43 ms: 2.47x slower                                                      |
| pycparser                  | 695 ms                                                      | 1.73 sec: 2.49x slower                                                     |
| scimark_sor                | 76.2 ms                                                     | 190 ms: 2.49x slower                                                       |
| comprehensions             | 10.4 us                                                     | 25.9 us: 2.50x slower                                                      |
| chaos                      | 37.9 ms                                                     | 95.4 ms: 2.52x slower                                                      |
| subparsers                 | 10.9 ms                                                     | 27.6 ms: 2.54x slower                                                      |
| mako                       | 6.56 ms                                                     | 16.9 ms: 2.58x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 32.4 ms: 2.59x slower                                                      |
| raytrace                   | 153 ms                                                      | 403 ms: 2.63x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 107 ms: 2.63x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 120 ms: 2.63x slower                                                       |
| richards                   | 26.3 ms                                                     | 69.7 ms: 2.66x slower                                                      |
| richards_super             | 29.8 ms                                                     | 79.2 ms: 2.66x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 170 ms: 2.67x slower                                                       |
| docutils                   | 1.53 sec                                                    | 4.14 sec: 2.71x slower                                                     |
| nbody                      | 66.3 ms                                                     | 179 ms: 2.71x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 10.6 ms: 2.77x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 364 us: 2.80x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 8.38 sec: 2.92x slower                                                     |
| scimark_lu                 | 56.7 ms                                                     | 167 ms: 2.94x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 1.50 sec: 3.09x slower                                                     |
| deltablue                  | 1.89 ms                                                     | 5.88 ms: 3.11x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 5.09 sec: 3.71x slower                                                     |
| pprint_pformat             | 977 ms                                                      | 4.25 sec: 4.35x slower                                                     |
| logging_silent             | 54.6 ns                                                     | 577 ns: 10.56x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.76x slower                                                               |
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.418x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.77x
- 95% likely to have a slowdown of 1.73x
- 99% likely to have a slowdown of 1.66x

# Memory
- memory change: unknown