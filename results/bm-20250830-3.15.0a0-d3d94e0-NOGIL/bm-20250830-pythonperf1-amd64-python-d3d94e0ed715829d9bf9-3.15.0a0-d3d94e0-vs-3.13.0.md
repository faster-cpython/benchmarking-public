# Results vs. 3.13.0

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: windows-amd64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.065x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 227 ms: 1.05x slower                                                       |
| docutils       | 1.53 sec                                                    | 2.87 sec: 1.87x slower                                                     |
| html5lib       | 38.2 ms                                                     | 40.7 ms: 1.07x slower                                                      |
| sphinx         | 617 ms                                                      | 658 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.22x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 142 ms: 2.11x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 329 ms: 1.51x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 190 ms: 1.48x faster                                                       |
| async_tree_io              | 513 ms                                                      | 350 ms: 1.46x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 149 ms: 1.35x faster                                                       |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 209 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 310 ms: 1.24x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 333 ms: 1.14x faster                                                       |
| async_generators           | 223 ms                                                      | 256 ms: 1.15x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 15.5 ms: 1.24x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.28x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 47.0 ms: 1.08x faster                                                      |
| pidigits       | 146 ms                                                      | 136 ms: 1.08x faster                                                       |
| nbody          | 66.3 ms                                                     | 82.6 ms: 1.25x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.2 ms: 1.81x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.56 ms: 1.08x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 94.6 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 6.19 ms                                                     | 5.99 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 59.8 ms: 1.01x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 93.4 ms: 1.01x slower                                                      |
| json_loads           | 15.1 us                                                     | 16.0 us: 1.06x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 63.5 ms: 1.19x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 44.7 ms: 1.23x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 161 us: 1.24x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 237 us: 1.27x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 2.41 sec: 1.76x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.17x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.9 ms: 1.06x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.7 ms: 1.16x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 40.6 ms: 1.20x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 19.8 ms: 1.30x slower                                                      |
| django_template | 20.3 ms                                                     | 27.4 ms: 1.35x slower                                                      |
| mako            | 6.56 ms                                                     | 9.98 ms: 1.52x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.34x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 570 us: 14.85x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 30.2 ms: 2.49x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 142 ms: 2.11x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.2 ms: 1.81x faster                                                      |
| gc_traversal               | 1.96 ms                                                     | 1.20 ms: 1.64x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 329 ms: 1.51x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 190 ms: 1.48x faster                                                       |
| async_tree_io              | 513 ms                                                      | 350 ms: 1.46x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 149 ms: 1.35x faster                                                       |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 209 ms: 1.26x faster                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 979 us: 1.25x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 310 ms: 1.24x faster                                                       |
| mdp                        | 1.43 sec                                                    | 1.16 sec: 1.23x faster                                                     |
| sqlite_synth               | 1.59 us                                                     | 1.35 us: 1.17x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 333 ms: 1.14x faster                                                       |
| deepcopy                   | 223 us                                                      | 202 us: 1.10x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 21.2 us: 1.09x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.56 ms: 1.08x faster                                                      |
| float                      | 50.8 ms                                                     | 47.0 ms: 1.08x faster                                                      |
| pidigits                   | 146 ms                                                      | 136 ms: 1.08x faster                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 79.4 ms: 1.06x faster                                                      |
| json                       | 3.30 ms                                                     | 3.13 ms: 1.06x faster                                                      |
| json_dumps                 | 6.19 ms                                                     | 5.99 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 59.8 ms: 1.01x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.87 ms: 1.00x slower                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 93.4 ms: 1.01x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 42.0 ms: 1.05x slower                                                      |
| 2to3                       | 215 ms                                                      | 227 ms: 1.05x slower                                                       |
| json_loads                 | 15.1 us                                                     | 16.0 us: 1.06x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.9 ms: 1.06x slower                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 2.15 us: 1.06x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 40.7 ms: 1.07x slower                                                      |
| sphinx                     | 617 ms                                                      | 658 ms: 1.07x slower                                                       |
| go                         | 84.7 ms                                                     | 92.7 ms: 1.09x slower                                                      |
| pyflate                    | 283 ms                                                      | 312 ms: 1.10x slower                                                       |
| sympy_expand               | 286 ms                                                      | 321 ms: 1.12x slower                                                       |
| sympy_str                  | 167 ms                                                      | 188 ms: 1.13x slower                                                       |
| spectral_norm              | 63.4 ms                                                     | 72.4 ms: 1.14x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 97.3 ms: 1.14x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 14.2 ms: 1.15x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.64 us: 1.15x slower                                                      |
| async_generators           | 223 ms                                                      | 256 ms: 1.15x slower                                                       |
| logging_format             | 6.18 us                                                     | 7.12 us: 1.15x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 63.1 ns: 1.16x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 88.4 ms: 1.16x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 65.9 ms: 1.16x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.7 ms: 1.16x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 564 ms: 1.16x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 94.6 ms: 1.17x slower                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 3.08 ms: 1.18x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 63.5 ms: 1.19x slower                                                      |
| comprehensions             | 10.4 us                                                     | 12.3 us: 1.19x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 40.6 ms: 1.20x slower                                                      |
| fannkuch                   | 252 ms                                                      | 301 ms: 1.20x slower                                                       |
| scimark_fft                | 175 ms                                                      | 210 ms: 1.20x slower                                                       |
| generators                 | 19.0 ms                                                     | 23.1 ms: 1.21x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 88.2 ms: 1.23x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 44.7 ms: 1.23x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.71 ms: 1.23x slower                                                      |
| chaos                      | 37.9 ms                                                     | 46.4 ms: 1.23x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 15.5 ms: 1.24x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 161 us: 1.24x slower                                                       |
| nbody                      | 66.3 ms                                                     | 82.6 ms: 1.25x slower                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 51.0 ms: 1.25x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 57.0 ms: 1.25x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.39 ms: 1.26x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 237 us: 1.27x slower                                                       |
| richards                   | 26.3 ms                                                     | 33.8 ms: 1.29x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 134 us: 1.30x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 19.8 ms: 1.30x slower                                                      |
| richards_super             | 29.8 ms                                                     | 39.6 ms: 1.33x slower                                                      |
| django_template            | 20.3 ms                                                     | 27.4 ms: 1.35x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 75.8 ms: 1.35x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 1.10 ms: 1.36x slower                                                      |
| raytrace                   | 153 ms                                                      | 217 ms: 1.41x slower                                                       |
| coverage                   | 45.3 ms                                                     | 66.8 ms: 1.48x slower                                                      |
| mako                       | 6.56 ms                                                     | 9.98 ms: 1.52x slower                                                      |
| k_core                     | 1.70 sec                                                    | 2.71 sec: 1.60x slower                                                     |
| many_optionals             | 361 us                                                      | 619 us: 1.71x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.71 sec: 1.75x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 2.41 sec: 1.76x slower                                                     |
| shortest_path              | 355 ms                                                      | 653 ms: 1.84x slower                                                       |
| docutils                   | 1.53 sec                                                    | 2.87 sec: 1.87x slower                                                     |
| bpe_tokeniser              | 2.87 sec                                                    | 5.50 sec: 1.91x slower                                                     |
| connected_components       | 320 ms                                                      | 622 ms: 1.95x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 34.8 ms: 3.21x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (3): pylint, regex_dna, pycparser
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250830-3.15.0a0-d3d94e0-NOGIL/bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.065x slower

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown