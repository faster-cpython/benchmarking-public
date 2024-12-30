# Results vs. 3.13.0

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: windows-amd64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.025x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 227 ms: 1.06x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.68 sec: 1.10x slower                                                      |
| html5lib       | 38.2 ms                                                     | 40.1 ms: 1.05x slower                                                       |
| sphinx         | 617 ms                                                      | 655 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                        |
| async_tree_io              | 513 ms                                                      | 410 ms: 1.25x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 403 ms: 1.23x faster                                                        |
| async_tree_none            | 219 ms                                                      | 183 ms: 1.20x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 225 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 173 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 346 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 348 ms: 1.09x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 308 ms: 1.03x slower                                                        |
| async_generators           | 223 ms                                                      | 238 ms: 1.07x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.09x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 146 ms                                                      | 147 ms: 1.00x slower                                                        |
| float          | 50.8 ms                                                     | 55.4 ms: 1.09x slower                                                       |
| nbody          | 66.3 ms                                                     | 83.2 ms: 1.26x slower                                                       |
| Geometric mean | (ref)                                                       | 1.11x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.69 ms                                                     | 1.53 ms: 1.11x faster                                                       |
| regex_dna      | 115 ms                                                      | 119 ms: 1.04x slower                                                        |
| regex_compile  | 80.7 ms                                                     | 88.2 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 87.5 ms: 1.05x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.5 us: 1.04x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.1 ms: 1.04x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.05x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 6.66 ms: 1.08x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 57.7 ms: 1.08x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 40.8 ms: 1.12x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 151 us: 1.16x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 227 us: 1.22x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 24.2 ms: 1.01x faster                                                       |
| python_startup_no_site | 16.9 ms                                                     | 18.1 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 35.1 ms: 1.04x slower                                                       |
| mako            | 6.56 ms                                                     | 7.03 ms: 1.07x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 16.8 ms: 1.10x slower                                                       |
| django_template | 20.3 ms                                                     | 25.1 ms: 1.24x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 525 us: 16.14x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                        |
| async_tree_io              | 513 ms                                                      | 410 ms: 1.25x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 403 ms: 1.23x faster                                                        |
| deepcopy                   | 223 us                                                      | 186 us: 1.20x faster                                                        |
| async_tree_none            | 219 ms                                                      | 183 ms: 1.20x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 225 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 173 ms: 1.16x faster                                                        |
| json                       | 3.30 ms                                                     | 2.93 ms: 1.13x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.53 ms: 1.11x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 346 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 348 ms: 1.09x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 21.3 us: 1.08x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.90 us: 1.06x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 87.5 ms: 1.05x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.5 us: 1.04x faster                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.20 ms: 1.02x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 62.8 ms: 1.01x faster                                                       |
| python_startup             | 24.4 ms                                                     | 24.2 ms: 1.01x faster                                                       |
| pidigits                   | 146 ms                                                      | 147 ms: 1.00x slower                                                        |
| telco                      | 4.85 ms                                                     | 4.89 ms: 1.01x slower                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.61 us: 1.02x slower                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.66 ms: 1.02x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 308 ms: 1.03x slower                                                        |
| coverage                   | 45.3 ms                                                     | 46.9 ms: 1.03x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.48 sec: 1.04x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 35.1 ms: 1.04x slower                                                       |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.04x slower                                                        |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.1 ms: 1.04x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 88.0 ms: 1.04x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.05x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 40.1 ms: 1.05x slower                                                       |
| 2to3                       | 215 ms                                                      | 227 ms: 1.06x slower                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 3.04 sec: 1.06x slower                                                      |
| sphinx                     | 617 ms                                                      | 655 ms: 1.06x slower                                                        |
| pycparser                  | 695 ms                                                      | 738 ms: 1.06x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 90.4 ms: 1.06x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 42.7 ms: 1.06x slower                                                       |
| sympy_expand               | 286 ms                                                      | 305 ms: 1.07x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 18.1 ms: 1.07x slower                                                       |
| sympy_str                  | 167 ms                                                      | 178 ms: 1.07x slower                                                        |
| async_generators           | 223 ms                                                      | 238 ms: 1.07x slower                                                        |
| mako                       | 6.56 ms                                                     | 7.03 ms: 1.07x slower                                                       |
| go                         | 84.7 ms                                                     | 90.9 ms: 1.07x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.66 ms: 1.08x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 57.7 ms: 1.08x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 77.8 ms: 1.08x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 49.5 ms: 1.09x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 112 us: 1.09x slower                                                        |
| float                      | 50.8 ms                                                     | 55.4 ms: 1.09x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 88.2 ms: 1.09x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.5 ms: 1.09x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.09x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.68 sec: 1.10x slower                                                      |
| sqlglot_optimize           | 32.5 ms                                                     | 35.8 ms: 1.10x slower                                                       |
| scimark_fft                | 175 ms                                                      | 193 ms: 1.10x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 16.8 ms: 1.10x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.83 us: 1.11x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.44 us: 1.11x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 63.3 ms: 1.12x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 40.8 ms: 1.12x slower                                                       |
| pyflate                    | 283 ms                                                      | 316 ms: 1.12x slower                                                        |
| generators                 | 19.0 ms                                                     | 21.2 ms: 1.12x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 553 ms: 1.14x slower                                                        |
| fannkuch                   | 252 ms                                                      | 287 ms: 1.14x slower                                                        |
| sqlglot_normalize          | 172 ms                                                      | 196 ms: 1.14x slower                                                        |
| pprint_pformat             | 977 ms                                                      | 1.12 sec: 1.15x slower                                                      |
| chaos                      | 37.9 ms                                                     | 43.5 ms: 1.15x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 151 us: 1.16x slower                                                        |
| scimark_sor                | 76.2 ms                                                     | 88.8 ms: 1.17x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 47.7 ms: 1.17x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 66.3 ms: 1.18x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.13 ms: 1.18x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 909 us: 1.19x slower                                                        |
| hexiom                     | 3.84 ms                                                     | 4.59 ms: 1.19x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 65.8 ns: 1.21x slower                                                       |
| comprehensions             | 10.4 us                                                     | 12.5 us: 1.21x slower                                                       |
| many_optionals             | 361 us                                                      | 438 us: 1.21x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.30 ms: 1.21x slower                                                       |
| richards_super             | 29.8 ms                                                     | 36.2 ms: 1.22x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 227 us: 1.22x slower                                                        |
| richards                   | 26.3 ms                                                     | 32.1 ms: 1.22x slower                                                       |
| django_template            | 20.3 ms                                                     | 25.1 ms: 1.24x slower                                                       |
| nbody                      | 66.3 ms                                                     | 83.2 ms: 1.26x slower                                                       |
| raytrace                   | 153 ms                                                      | 198 ms: 1.29x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.3 ms: 1.51x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (8): regex_v8, pylint, shortest_path, k_core, gc_traversal, connected_components, pathlib, bench_thread_pool
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: mypy2

- Geometric mean (including insignificant results): 1.025x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown