# Results vs. 3.13.0

- fork: python
- ref: 7168e98c80d28ab71f39
- machine: windows-amd64
- commit hash: 7168e98
- commit date: 2025-09-13
- overall geometric mean: 1.070x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 228 ms: 1.06x slower                                                       |
| docutils       | 1.53 sec                                                    | 2.87 sec: 1.87x slower                                                     |
| html5lib       | 38.2 ms                                                     | 40.8 ms: 1.07x slower                                                      |
| sphinx         | 617 ms                                                      | 709 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 139 ms: 2.16x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 335 ms: 1.48x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 194 ms: 1.45x faster                                                       |
| async_tree_io              | 513 ms                                                      | 358 ms: 1.43x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 149 ms: 1.34x faster                                                       |
| async_tree_none            | 219 ms                                                      | 174 ms: 1.26x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 214 ms: 1.24x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 313 ms: 1.22x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 334 ms: 1.14x faster                                                       |
| coroutines                 | 12.5 ms                                                     | 14.8 ms: 1.18x slower                                                      |
| async_generators           | 223 ms                                                      | 265 ms: 1.19x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.27x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 46.5 ms: 1.09x faster                                                      |
| pidigits       | 146 ms                                                      | 136 ms: 1.07x faster                                                       |
| nbody          | 66.3 ms                                                     | 82.5 ms: 1.24x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.5 ms: 1.76x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.60 ms: 1.06x faster                                                      |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                       |
| regex_compile  | 80.7 ms                                                     | 95.2 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 60.5 ms                                                     | 58.4 ms: 1.04x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 91.0 ms: 1.01x faster                                                      |
| json_dumps           | 6.19 ms                                                     | 6.15 ms: 1.01x faster                                                      |
| json_loads           | 15.1 us                                                     | 16.1 us: 1.07x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 62.9 ms: 1.18x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 44.9 ms: 1.23x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 160 us: 1.23x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 238 us: 1.28x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 2.40 sec: 1.75x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.17x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.2 ms: 1.03x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 40.7 ms: 1.20x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 20.1 ms: 1.32x slower                                                      |
| django_template | 20.3 ms                                                     | 27.5 ms: 1.36x slower                                                      |
| mako            | 6.56 ms                                                     | 10.1 ms: 1.54x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.35x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 573 us: 14.78x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 28.9 ms: 2.60x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 139 ms: 2.16x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.5 ms: 1.76x faster                                                      |
| gc_traversal               | 1.96 ms                                                     | 1.30 ms: 1.51x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 335 ms: 1.48x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 194 ms: 1.45x faster                                                       |
| async_tree_io              | 513 ms                                                      | 358 ms: 1.43x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 149 ms: 1.34x faster                                                       |
| async_tree_none            | 219 ms                                                      | 174 ms: 1.26x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 214 ms: 1.24x faster                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 998 us: 1.23x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 313 ms: 1.22x faster                                                       |
| mdp                        | 1.43 sec                                                    | 1.18 sec: 1.21x faster                                                     |
| sqlite_synth               | 1.59 us                                                     | 1.34 us: 1.18x faster                                                      |
| deepcopy_memo              | 23.1 us                                                     | 19.9 us: 1.16x faster                                                      |
| deepcopy                   | 223 us                                                      | 195 us: 1.15x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 334 ms: 1.14x faster                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 75.3 ms: 1.12x faster                                                      |
| float                      | 50.8 ms                                                     | 46.5 ms: 1.09x faster                                                      |
| pidigits                   | 146 ms                                                      | 136 ms: 1.07x faster                                                       |
| json                       | 3.30 ms                                                     | 3.08 ms: 1.07x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.60 ms: 1.06x faster                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 58.4 ms: 1.04x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.77 ms: 1.02x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 91.0 ms: 1.01x faster                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.15 ms: 1.01x faster                                                      |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 2.08 us: 1.03x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.2 ms: 1.03x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 42.3 ms: 1.06x slower                                                      |
| 2to3                       | 215 ms                                                      | 228 ms: 1.06x slower                                                       |
| json_loads                 | 15.1 us                                                     | 16.1 us: 1.07x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 40.8 ms: 1.07x slower                                                      |
| go                         | 84.7 ms                                                     | 91.8 ms: 1.08x slower                                                      |
| pycparser                  | 695 ms                                                      | 775 ms: 1.11x slower                                                       |
| spectral_norm              | 63.4 ms                                                     | 70.7 ms: 1.12x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                      |
| sympy_expand               | 286 ms                                                      | 321 ms: 1.12x slower                                                       |
| pyflate                    | 283 ms                                                      | 319 ms: 1.13x slower                                                       |
| sympy_str                  | 167 ms                                                      | 190 ms: 1.14x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 62.3 ns: 1.14x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 14.1 ms: 1.14x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 97.5 ms: 1.14x slower                                                      |
| sphinx                     | 617 ms                                                      | 709 ms: 1.15x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 65.6 ms: 1.16x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.69 us: 1.16x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 88.4 ms: 1.16x slower                                                      |
| logging_format             | 6.18 us                                                     | 7.19 us: 1.16x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 62.9 ms: 1.18x slower                                                      |
| comprehensions             | 10.4 us                                                     | 12.2 us: 1.18x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 95.2 ms: 1.18x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.8 ms: 1.18x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 577 ms: 1.19x slower                                                       |
| async_generators           | 223 ms                                                      | 265 ms: 1.19x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 40.7 ms: 1.20x slower                                                      |
| scimark_fft                | 175 ms                                                      | 212 ms: 1.21x slower                                                       |
| fannkuch                   | 252 ms                                                      | 305 ms: 1.21x slower                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 3.19 ms: 1.22x slower                                                      |
| generators                 | 19.0 ms                                                     | 23.2 ms: 1.22x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.71 ms: 1.22x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 44.9 ms: 1.23x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 160 us: 1.23x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 89.0 ms: 1.24x slower                                                      |
| nbody                      | 66.3 ms                                                     | 82.5 ms: 1.24x slower                                                      |
| chaos                      | 37.9 ms                                                     | 47.6 ms: 1.26x slower                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 51.3 ms: 1.26x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 238 us: 1.28x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 58.5 ms: 1.28x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.45 ms: 1.30x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 72.9 ms: 1.30x slower                                                      |
| richards                   | 26.3 ms                                                     | 34.1 ms: 1.30x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 134 us: 1.30x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 1.07 ms: 1.32x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 20.1 ms: 1.32x slower                                                      |
| richards_super             | 29.8 ms                                                     | 39.9 ms: 1.34x slower                                                      |
| django_template            | 20.3 ms                                                     | 27.5 ms: 1.36x slower                                                      |
| raytrace                   | 153 ms                                                      | 217 ms: 1.42x slower                                                       |
| coverage                   | 45.3 ms                                                     | 67.7 ms: 1.49x slower                                                      |
| mako                       | 6.56 ms                                                     | 10.1 ms: 1.54x slower                                                      |
| k_core                     | 1.70 sec                                                    | 2.72 sec: 1.60x slower                                                     |
| many_optionals             | 361 us                                                      | 631 us: 1.75x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 2.40 sec: 1.75x slower                                                     |
| pprint_pformat             | 977 ms                                                      | 1.76 sec: 1.80x slower                                                     |
| shortest_path              | 355 ms                                                      | 659 ms: 1.86x slower                                                       |
| docutils                   | 1.53 sec                                                    | 2.87 sec: 1.87x slower                                                     |
| connected_components       | 320 ms                                                      | 619 ms: 1.94x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 5.57 sec: 1.94x slower                                                     |
| subparsers                 | 10.9 ms                                                     | 35.1 ms: 3.24x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.08x slower                                                               |

Benchmark hidden because not significant (1): pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250913-3.15.0a0-7168e98-NOGIL/bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.070x slower

# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown