# Results vs. 3.13.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: windows-amd64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.007x slower
- HPT reliability: 99.87%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 232 ms: 1.08x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.74 sec: 1.13x slower                                                      |
| sphinx         | 617 ms                                                      | 688 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                       | 1.08x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                        |
| async_tree_io              | 513 ms                                                      | 400 ms: 1.28x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 397 ms: 1.25x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 213 ms: 1.24x faster                                                        |
| async_tree_none            | 219 ms                                                      | 179 ms: 1.22x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 358 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 365 ms: 1.05x faster                                                        |
| async_generators           | 223 ms                                                      | 229 ms: 1.03x slower                                                        |
| asyncio_websockets         | 300 ms                                                      | 316 ms: 1.05x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.2 ms: 1.15x faster                                                       |
| nbody          | 66.3 ms                                                     | 60.5 ms: 1.09x faster                                                       |
| pidigits       | 146 ms                                                      | 155 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 16.7 ms: 1.43x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 83.6 ms: 1.04x slower                                                       |
| regex_dna      | 115 ms                                                      | 130 ms: 1.13x slower                                                        |
| regex_effbot   | 1.69 ms                                                     | 1.94 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.32 sec: 1.04x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 102 ms: 1.10x slower                                                        |
| unpickle_pure_python | 130 us                                                      | 146 us: 1.12x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 211 us: 1.13x slower                                                        |
| xml_etree_iterparse  | 60.5 ms                                                     | 69.4 ms: 1.15x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 64.3 ms: 1.20x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 44.8 ms: 1.23x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 7.62 ms: 1.23x slower                                                       |
| json_loads           | 15.1 us                                                     | 19.3 us: 1.28x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.15x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 27.4 ms: 1.13x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 20.4 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 31.7 ms: 1.07x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 14.5 ms: 1.05x faster                                                       |
| mako            | 6.56 ms                                                     | 7.56 ms: 1.15x slower                                                       |
| django_template | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 543 us: 15.60x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 16.7 ms: 1.43x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                        |
| deepcopy                   | 223 us                                                      | 172 us: 1.30x faster                                                        |
| async_tree_io              | 513 ms                                                      | 400 ms: 1.28x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 397 ms: 1.25x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 213 ms: 1.24x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 18.9 us: 1.22x faster                                                       |
| async_tree_none            | 219 ms                                                      | 179 ms: 1.22x faster                                                        |
| pathlib                    | 75.3 ms                                                     | 62.1 ms: 1.21x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                        |
| float                      | 50.8 ms                                                     | 44.2 ms: 1.15x faster                                                       |
| go                         | 84.7 ms                                                     | 73.8 ms: 1.15x faster                                                       |
| generators                 | 19.0 ms                                                     | 17.0 ms: 1.11x faster                                                       |
| nbody                      | 66.3 ms                                                     | 60.5 ms: 1.09x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.89 us: 1.07x faster                                                       |
| genshi_xml                 | 33.9 ms                                                     | 31.7 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 358 ms: 1.06x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 59.7 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 365 ms: 1.05x faster                                                        |
| genshi_text                | 15.2 ms                                                     | 14.5 ms: 1.05x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.32 sec: 1.04x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 74.0 ms: 1.03x faster                                                       |
| shortest_path              | 355 ms                                                      | 351 ms: 1.01x faster                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.5 ms: 1.01x faster                                                       |
| meteor_contest             | 72.0 ms                                                     | 72.5 ms: 1.01x slower                                                       |
| connected_components       | 320 ms                                                      | 323 ms: 1.01x slower                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.62 us: 1.02x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 1.93 ms: 1.02x slower                                                       |
| async_generators           | 223 ms                                                      | 229 ms: 1.03x slower                                                        |
| pyflate                    | 283 ms                                                      | 293 ms: 1.03x slower                                                        |
| regex_compile              | 80.7 ms                                                     | 83.6 ms: 1.04x slower                                                       |
| chaos                      | 37.9 ms                                                     | 39.4 ms: 1.04x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 42.0 ms: 1.05x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 316 ms: 1.05x slower                                                        |
| pidigits                   | 146 ms                                                      | 155 ms: 1.06x slower                                                        |
| sympy_expand               | 286 ms                                                      | 302 ms: 1.06x slower                                                        |
| typing_runtime_protocols   | 103 us                                                      | 109 us: 1.06x slower                                                        |
| hexiom                     | 3.84 ms                                                     | 4.07 ms: 1.06x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 3.06 sec: 1.06x slower                                                      |
| sympy_str                  | 167 ms                                                      | 178 ms: 1.07x slower                                                        |
| pprint_safe_repr           | 485 ms                                                      | 517 ms: 1.07x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 91.5 ms: 1.07x slower                                                       |
| telco                      | 4.85 ms                                                     | 5.22 ms: 1.08x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.05 sec: 1.08x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.22 us: 1.08x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 874 us: 1.08x slower                                                        |
| scimark_fft                | 175 ms                                                      | 189 ms: 1.08x slower                                                        |
| logging_format             | 6.18 us                                                     | 6.67 us: 1.08x slower                                                       |
| 2to3                       | 215 ms                                                      | 232 ms: 1.08x slower                                                        |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                                       |
| json                       | 3.30 ms                                                     | 3.58 ms: 1.08x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                       |
| fannkuch                   | 252 ms                                                      | 273 ms: 1.09x slower                                                        |
| sqlglot_parse              | 764 us                                                      | 831 us: 1.09x slower                                                        |
| sqlglot_optimize           | 32.5 ms                                                     | 35.4 ms: 1.09x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.04 ms: 1.09x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 188 ms: 1.10x slower                                                        |
| richards                   | 26.3 ms                                                     | 28.8 ms: 1.10x slower                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 102 ms: 1.10x slower                                                        |
| nqueens                    | 56.1 ms                                                     | 62.1 ms: 1.11x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.36 ms: 1.11x slower                                                       |
| richards_super             | 29.8 ms                                                     | 33.0 ms: 1.11x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.5 us: 1.11x slower                                                       |
| sphinx                     | 617 ms                                                      | 688 ms: 1.11x slower                                                        |
| unpickle_pure_python       | 130 us                                                      | 146 us: 1.12x slower                                                        |
| python_startup             | 24.4 ms                                                     | 27.4 ms: 1.13x slower                                                       |
| raytrace                   | 153 ms                                                      | 173 ms: 1.13x slower                                                        |
| regex_dna                  | 115 ms                                                      | 130 ms: 1.13x slower                                                        |
| pickle_pure_python         | 186 us                                                      | 211 us: 1.13x slower                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 51.6 ms: 1.13x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.74 sec: 1.13x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 95.8 ms: 1.14x slower                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.94 ms: 1.14x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 69.4 ms: 1.15x slower                                                       |
| mako                       | 6.56 ms                                                     | 7.56 ms: 1.15x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 62.9 ns: 1.15x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 67.7 ms: 1.19x slower                                                       |
| coverage                   | 45.3 ms                                                     | 54.1 ms: 1.20x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.72 sec: 1.20x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 64.3 ms: 1.20x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 20.4 ms: 1.21x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 44.8 ms: 1.23x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 7.62 ms: 1.23x slower                                                       |
| many_optionals             | 361 us                                                      | 448 us: 1.24x slower                                                        |
| json_loads                 | 15.1 us                                                     | 19.3 us: 1.28x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.82 ms: 1.43x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.1 ms: 1.48x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (5): pylint, scimark_sparse_mat_mult, k_core, html5lib, pycparser
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.007x slower

# HPT report

- Reliability score: 99.87% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown