# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_targets
- machine: windows-amd64
- commit hash: aa2b0df
- commit date: 2025-07-07
- overall geometric mean: 1.086x faster
- HPT reliability: 89.45%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 218 ms: 1.01x slower                                                    |
| docutils       | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                  |
| sphinx         | 617 ms                                                      | 644 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                       | 1.03x slower                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 165 ms: 1.82x faster                                                    |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                    |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.30x faster                                                    |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                                    |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                    |
| async_tree_io_tg           | 497 ms                                                      | 391 ms: 1.27x faster                                                    |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                    |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 334 ms: 1.14x faster                                                    |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                    |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                    |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.15x slower                                                   |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.9 ms: 1.13x faster                                                   |
| nbody          | 66.3 ms                                                     | 59.8 ms: 1.11x faster                                                   |
| pidigits       | 146 ms                                                      | 146 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                       | 1.08x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                   |
| regex_effbot   | 1.69 ms                                                     | 1.62 ms: 1.05x faster                                                   |
| regex_compile  | 80.7 ms                                                     | 78.8 ms: 1.02x faster                                                   |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                       | 1.14x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 105 us: 1.24x faster                                                    |
| tomli_loads          | 1.37 sec                                                    | 1.12 sec: 1.22x faster                                                  |
| xml_etree_generate   | 53.5 ms                                                     | 49.2 ms: 1.09x faster                                                   |
| xml_etree_process    | 36.5 ms                                                     | 34.8 ms: 1.05x faster                                                   |
| json_loads           | 15.1 us                                                     | 14.5 us: 1.04x faster                                                   |
| xml_etree_parse      | 92.2 ms                                                     | 88.5 ms: 1.04x faster                                                   |
| json_dumps           | 6.19 ms                                                     | 6.27 ms: 1.01x slower                                                   |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.6 ms: 1.05x slower                                                   |
| pickle_pure_python   | 186 us                                                      | 207 us: 1.11x slower                                                    |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.9 ms: 1.06x slower                                                   |
| python_startup_no_site | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                   |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.38 ms: 1.22x faster                                                   |
| genshi_text     | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                   |
| genshi_xml      | 33.9 ms                                                     | 35.2 ms: 1.04x slower                                                   |
| django_template | 20.3 ms                                                     | 25.0 ms: 1.23x slower                                                   |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 496 us: 17.06x faster                                                   |
| pathlib                    | 75.3 ms                                                     | 31.6 ms: 2.38x faster                                                   |
| asyncio_websockets         | 300 ms                                                      | 165 ms: 1.82x faster                                                    |
| mdp                        | 1.43 sec                                                    | 797 ms: 1.80x faster                                                    |
| regex_v8                   | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                   |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                    |
| deepcopy                   | 223 us                                                      | 169 us: 1.32x faster                                                    |
| deepcopy_memo              | 23.1 us                                                     | 17.8 us: 1.30x faster                                                   |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.30x faster                                                    |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                                    |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                    |
| async_tree_io_tg           | 497 ms                                                      | 391 ms: 1.27x faster                                                    |
| unpickle_pure_python       | 130 us                                                      | 105 us: 1.24x faster                                                    |
| tomli_loads                | 1.37 sec                                                    | 1.12 sec: 1.22x faster                                                  |
| mako                       | 6.56 ms                                                     | 5.38 ms: 1.22x faster                                                   |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                    |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.25 ms: 1.16x faster                                                   |
| scimark_fft                | 175 ms                                                      | 152 ms: 1.15x faster                                                    |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 334 ms: 1.14x faster                                                    |
| float                      | 50.8 ms                                                     | 44.9 ms: 1.13x faster                                                   |
| json                       | 3.30 ms                                                     | 2.93 ms: 1.13x faster                                                   |
| bpe_tokeniser              | 2.87 sec                                                    | 2.55 sec: 1.12x faster                                                  |
| deepcopy_reduce            | 2.02 us                                                     | 1.81 us: 1.12x faster                                                   |
| pyflate                    | 283 ms                                                      | 253 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                    |
| pprint_safe_repr           | 485 ms                                                      | 434 ms: 1.12x faster                                                    |
| telco                      | 4.85 ms                                                     | 4.37 ms: 1.11x faster                                                   |
| pprint_pformat             | 977 ms                                                      | 881 ms: 1.11x faster                                                    |
| nbody                      | 66.3 ms                                                     | 59.8 ms: 1.11x faster                                                   |
| go                         | 84.7 ms                                                     | 77.4 ms: 1.09x faster                                                   |
| xml_etree_generate         | 53.5 ms                                                     | 49.2 ms: 1.09x faster                                                   |
| fannkuch                   | 252 ms                                                      | 232 ms: 1.08x faster                                                    |
| k_core                     | 1.70 sec                                                    | 1.61 sec: 1.05x faster                                                  |
| xml_etree_process          | 36.5 ms                                                     | 34.8 ms: 1.05x faster                                                   |
| regex_effbot               | 1.69 ms                                                     | 1.62 ms: 1.05x faster                                                   |
| json_loads                 | 15.1 us                                                     | 14.5 us: 1.04x faster                                                   |
| xml_etree_parse            | 92.2 ms                                                     | 88.5 ms: 1.04x faster                                                   |
| regex_compile              | 80.7 ms                                                     | 78.8 ms: 1.02x faster                                                   |
| sqlite_synth               | 1.59 us                                                     | 1.55 us: 1.02x faster                                                   |
| meteor_contest             | 72.0 ms                                                     | 70.8 ms: 1.02x faster                                                   |
| comprehensions             | 10.4 us                                                     | 10.3 us: 1.01x faster                                                   |
| logging_silent             | 54.6 ns                                                     | 54.2 ns: 1.01x faster                                                   |
| pidigits                   | 146 ms                                                      | 146 ms: 1.01x faster                                                    |
| shortest_path              | 355 ms                                                      | 353 ms: 1.01x faster                                                    |
| crypto_pyaes               | 45.6 ms                                                     | 45.9 ms: 1.01x slower                                                   |
| json_dumps                 | 6.19 ms                                                     | 6.27 ms: 1.01x slower                                                   |
| 2to3                       | 215 ms                                                      | 218 ms: 1.01x slower                                                    |
| spectral_norm              | 63.4 ms                                                     | 64.5 ms: 1.02x slower                                                   |
| sympy_str                  | 167 ms                                                      | 170 ms: 1.02x slower                                                    |
| sympy_expand               | 286 ms                                                      | 291 ms: 1.02x slower                                                    |
| sympy_sum                  | 85.2 ms                                                     | 86.9 ms: 1.02x slower                                                   |
| scimark_sor                | 76.2 ms                                                     | 77.9 ms: 1.02x slower                                                   |
| dulwich_log                | 40.1 ms                                                     | 41.1 ms: 1.03x slower                                                   |
| richards                   | 26.3 ms                                                     | 26.9 ms: 1.03x slower                                                   |
| richards_super             | 29.8 ms                                                     | 30.6 ms: 1.03x slower                                                   |
| generators                 | 19.0 ms                                                     | 19.5 ms: 1.03x slower                                                   |
| genshi_text                | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                   |
| sympy_integrate            | 12.3 ms                                                     | 12.7 ms: 1.03x slower                                                   |
| scimark_lu                 | 56.7 ms                                                     | 58.8 ms: 1.04x slower                                                   |
| genshi_xml                 | 33.9 ms                                                     | 35.2 ms: 1.04x slower                                                   |
| sphinx                     | 617 ms                                                      | 644 ms: 1.04x slower                                                    |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.6 ms: 1.05x slower                                                   |
| nqueens                    | 56.1 ms                                                     | 59.0 ms: 1.05x slower                                                   |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                    |
| python_startup             | 24.4 ms                                                     | 25.9 ms: 1.06x slower                                                   |
| logging_format             | 6.18 us                                                     | 6.58 us: 1.07x slower                                                   |
| logging_simple             | 5.77 us                                                     | 6.16 us: 1.07x slower                                                   |
| chaos                      | 37.9 ms                                                     | 40.6 ms: 1.07x slower                                                   |
| hexiom                     | 3.84 ms                                                     | 4.12 ms: 1.07x slower                                                   |
| create_gc_cycles           | 1.22 ms                                                     | 1.32 ms: 1.08x slower                                                   |
| docutils                   | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                  |
| gc_traversal               | 1.96 ms                                                     | 2.13 ms: 1.09x slower                                                   |
| coverage                   | 45.3 ms                                                     | 49.3 ms: 1.09x slower                                                   |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                    |
| pickle_pure_python         | 186 us                                                      | 207 us: 1.11x slower                                                    |
| python_startup_no_site     | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                   |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.15x slower                                                   |
| deltablue                  | 1.89 ms                                                     | 2.21 ms: 1.17x slower                                                   |
| raytrace                   | 153 ms                                                      | 183 ms: 1.20x slower                                                    |
| django_template            | 20.3 ms                                                     | 25.0 ms: 1.23x slower                                                   |
| many_optionals             | 361 us                                                      | 447 us: 1.24x slower                                                    |
| subparsers                 | 10.9 ms                                                     | 16.8 ms: 1.55x slower                                                   |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                            |

Benchmark hidden because not significant (6): pylint, html5lib, pycparser, typing_runtime_protocols, scimark_monte_carlo, connected_components
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250707-3.15.0a0-aa2b0df-JIT/bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.086x faster

# HPT report

- Reliability score: 89.45% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown