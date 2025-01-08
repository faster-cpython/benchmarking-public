# Results vs. 3.13.0

- fork: brandtbucher
- ref: nojit
- machine: windows-amd64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.041x faster
- HPT reliability: 82.83%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 220 ms: 1.02x slower                                               |
| docutils       | 1.53 sec                                                    | 1.72 sec: 1.13x slower                                             |
| sphinx         | 617 ms                                                      | 668 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                       | 1.06x slower                                                       |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.32x faster                                               |
| async_tree_io              | 513 ms                                                      | 399 ms: 1.28x faster                                               |
| async_tree_io_tg           | 497 ms                                                      | 391 ms: 1.27x faster                                               |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.21x faster                                               |
| async_tree_none            | 219 ms                                                      | 182 ms: 1.21x faster                                               |
| async_tree_memoization     | 265 ms                                                      | 220 ms: 1.20x faster                                               |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                               |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 352 ms: 1.08x faster                                               |
| asyncio_websockets         | 300 ms                                                      | 325 ms: 1.08x slower                                               |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.09x slower                                              |
| async_generators           | 223 ms                                                      | 259 ms: 1.16x slower                                               |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 39.5 ms: 1.29x faster                                              |
| nbody          | 66.3 ms                                                     | 54.2 ms: 1.22x faster                                              |
| Geometric mean | (ref)                                                       | 1.16x faster                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.6 ms: 1.63x faster                                              |
| regex_effbot   | 1.69 ms                                                     | 1.41 ms: 1.20x faster                                              |
| regex_dna      | 115 ms                                                      | 113 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                       | 1.19x faster                                                       |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 109 us: 1.19x faster                                               |
| tomli_loads          | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                             |
| json_loads           | 15.1 us                                                     | 14.0 us: 1.08x faster                                              |
| xml_etree_generate   | 53.5 ms                                                     | 49.6 ms: 1.08x faster                                              |
| xml_etree_parse      | 92.2 ms                                                     | 87.4 ms: 1.05x faster                                              |
| xml_etree_iterparse  | 60.5 ms                                                     | 59.1 ms: 1.02x faster                                              |
| xml_etree_process    | 36.5 ms                                                     | 35.9 ms: 1.02x faster                                              |
| json_dumps           | 6.19 ms                                                     | 6.42 ms: 1.04x slower                                              |
| pickle_pure_python   | 186 us                                                      | 207 us: 1.11x slower                                               |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup | 24.4 ms                                                     | 23.1 ms: 1.06x faster                                              |
| Geometric mean | (ref)                                                       | 1.03x faster                                                       |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.16 ms: 1.27x faster                                              |
| genshi_text     | 15.2 ms                                                     | 18.6 ms: 1.22x slower                                              |
| django_template | 20.3 ms                                                     | 26.0 ms: 1.28x slower                                              |
| genshi_xml      | 33.9 ms                                                     | 44.9 ms: 1.33x slower                                              |
| Geometric mean  | (ref)                                                       | 1.13x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 523 us: 16.18x faster                                              |
| regex_v8                   | 23.8 ms                                                     | 14.6 ms: 1.63x faster                                              |
| deepcopy_memo              | 23.1 us                                                     | 16.0 us: 1.44x faster                                              |
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.32x faster                                               |
| float                      | 50.8 ms                                                     | 39.5 ms: 1.29x faster                                              |
| async_tree_io              | 513 ms                                                      | 399 ms: 1.28x faster                                               |
| spectral_norm              | 63.4 ms                                                     | 49.6 ms: 1.28x faster                                              |
| scimark_sor                | 76.2 ms                                                     | 59.7 ms: 1.28x faster                                              |
| mako                       | 6.56 ms                                                     | 5.16 ms: 1.27x faster                                              |
| async_tree_io_tg           | 497 ms                                                      | 391 ms: 1.27x faster                                               |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.08 ms: 1.25x faster                                              |
| scimark_fft                | 175 ms                                                      | 142 ms: 1.23x faster                                               |
| nbody                      | 66.3 ms                                                     | 54.2 ms: 1.22x faster                                              |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.21x faster                                               |
| async_tree_none            | 219 ms                                                      | 182 ms: 1.21x faster                                               |
| regex_effbot               | 1.69 ms                                                     | 1.41 ms: 1.20x faster                                              |
| async_tree_memoization     | 265 ms                                                      | 220 ms: 1.20x faster                                               |
| unpickle_pure_python       | 130 us                                                      | 109 us: 1.19x faster                                               |
| deepcopy                   | 223 us                                                      | 188 us: 1.19x faster                                               |
| tomli_loads                | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                             |
| scimark_monte_carlo        | 40.7 ms                                                     | 35.7 ms: 1.14x faster                                              |
| json                       | 3.30 ms                                                     | 2.90 ms: 1.14x faster                                              |
| telco                      | 4.85 ms                                                     | 4.35 ms: 1.12x faster                                              |
| crypto_pyaes               | 45.6 ms                                                     | 40.9 ms: 1.11x faster                                              |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                               |
| bpe_tokeniser              | 2.87 sec                                                    | 2.64 sec: 1.09x faster                                             |
| deepcopy_reduce            | 2.02 us                                                     | 1.87 us: 1.08x faster                                              |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 352 ms: 1.08x faster                                               |
| json_loads                 | 15.1 us                                                     | 14.0 us: 1.08x faster                                              |
| xml_etree_generate         | 53.5 ms                                                     | 49.6 ms: 1.08x faster                                              |
| k_core                     | 1.70 sec                                                    | 1.59 sec: 1.07x faster                                             |
| scimark_lu                 | 56.7 ms                                                     | 53.2 ms: 1.07x faster                                              |
| fannkuch                   | 252 ms                                                      | 238 ms: 1.06x faster                                               |
| python_startup             | 24.4 ms                                                     | 23.1 ms: 1.06x faster                                              |
| xml_etree_parse            | 92.2 ms                                                     | 87.4 ms: 1.05x faster                                              |
| connected_components       | 320 ms                                                      | 307 ms: 1.04x faster                                               |
| shortest_path              | 355 ms                                                      | 344 ms: 1.03x faster                                               |
| bench_mp_pool              | 84.2 ms                                                     | 82.0 ms: 1.03x faster                                              |
| pprint_safe_repr           | 485 ms                                                      | 472 ms: 1.03x faster                                               |
| xml_etree_iterparse        | 60.5 ms                                                     | 59.1 ms: 1.02x faster                                              |
| pprint_pformat             | 977 ms                                                      | 955 ms: 1.02x faster                                               |
| pyflate                    | 283 ms                                                      | 277 ms: 1.02x faster                                               |
| xml_etree_process          | 36.5 ms                                                     | 35.9 ms: 1.02x faster                                              |
| regex_dna                  | 115 ms                                                      | 113 ms: 1.01x faster                                               |
| create_gc_cycles           | 1.22 ms                                                     | 1.21 ms: 1.01x faster                                              |
| sqlite_synth               | 1.59 us                                                     | 1.57 us: 1.01x faster                                              |
| dulwich_log                | 40.1 ms                                                     | 39.9 ms: 1.00x faster                                              |
| pathlib                    | 75.3 ms                                                     | 75.8 ms: 1.01x slower                                              |
| meteor_contest             | 72.0 ms                                                     | 72.6 ms: 1.01x slower                                              |
| logging_silent             | 54.6 ns                                                     | 55.7 ns: 1.02x slower                                              |
| 2to3                       | 215 ms                                                      | 220 ms: 1.02x slower                                               |
| coverage                   | 45.3 ms                                                     | 46.5 ms: 1.03x slower                                              |
| json_dumps                 | 6.19 ms                                                     | 6.42 ms: 1.04x slower                                              |
| go                         | 84.7 ms                                                     | 88.6 ms: 1.05x slower                                              |
| sympy_expand               | 286 ms                                                      | 300 ms: 1.05x slower                                               |
| sympy_str                  | 167 ms                                                      | 176 ms: 1.06x slower                                               |
| mdp                        | 1.43 sec                                                    | 1.52 sec: 1.06x slower                                             |
| logging_simple             | 5.77 us                                                     | 6.20 us: 1.07x slower                                              |
| sqlglot_parse              | 764 us                                                      | 824 us: 1.08x slower                                               |
| sympy_sum                  | 85.2 ms                                                     | 91.8 ms: 1.08x slower                                              |
| logging_format             | 6.18 us                                                     | 6.68 us: 1.08x slower                                              |
| asyncio_websockets         | 300 ms                                                      | 325 ms: 1.08x slower                                               |
| sphinx                     | 617 ms                                                      | 668 ms: 1.08x slower                                               |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.09x slower                                              |
| sympy_integrate            | 12.3 ms                                                     | 13.6 ms: 1.10x slower                                              |
| chaos                      | 37.9 ms                                                     | 41.8 ms: 1.10x slower                                              |
| pickle_pure_python         | 186 us                                                      | 207 us: 1.11x slower                                               |
| sqlglot_transpile          | 953 us                                                      | 1.07 ms: 1.12x slower                                              |
| comprehensions             | 10.4 us                                                     | 11.6 us: 1.12x slower                                              |
| typing_runtime_protocols   | 103 us                                                      | 116 us: 1.12x slower                                               |
| docutils                   | 1.53 sec                                                    | 1.72 sec: 1.13x slower                                             |
| sqlglot_optimize           | 32.5 ms                                                     | 37.6 ms: 1.16x slower                                              |
| nqueens                    | 56.1 ms                                                     | 65.1 ms: 1.16x slower                                              |
| async_generators           | 223 ms                                                      | 259 ms: 1.16x slower                                               |
| sqlglot_normalize          | 172 ms                                                      | 203 ms: 1.18x slower                                               |
| deltablue                  | 1.89 ms                                                     | 2.25 ms: 1.19x slower                                              |
| generators                 | 19.0 ms                                                     | 23.1 ms: 1.22x slower                                              |
| genshi_text                | 15.2 ms                                                     | 18.6 ms: 1.22x slower                                              |
| many_optionals             | 361 us                                                      | 454 us: 1.26x slower                                               |
| django_template            | 20.3 ms                                                     | 26.0 ms: 1.28x slower                                              |
| richards_super             | 29.8 ms                                                     | 38.4 ms: 1.29x slower                                              |
| richards                   | 26.3 ms                                                     | 34.2 ms: 1.30x slower                                              |
| hexiom                     | 3.84 ms                                                     | 5.04 ms: 1.31x slower                                              |
| genshi_xml                 | 33.9 ms                                                     | 44.9 ms: 1.33x slower                                              |
| raytrace                   | 153 ms                                                      | 205 ms: 1.34x slower                                               |
| subparsers                 | 10.9 ms                                                     | 15.6 ms: 1.44x slower                                              |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                       |

Benchmark hidden because not significant (8): html5lib, regex_compile, gc_traversal, pidigits, python_startup_no_site, pylint, pycparser, bench_thread_pool
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20250107-3.14.0a3+-f098037-JIT/bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037.json: mypy2

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 82.83% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown