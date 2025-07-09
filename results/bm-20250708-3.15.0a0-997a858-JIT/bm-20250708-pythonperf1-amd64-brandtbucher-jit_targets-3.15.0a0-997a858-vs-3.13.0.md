# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_targets
- machine: windows-amd64
- commit hash: 997a858
- commit date: 2025-07-08
- overall geometric mean: 1.090x faster
- HPT reliability: 90.51%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 220 ms: 1.02x slower                                                    |
| docutils       | 1.53 sec                                                    | 1.63 sec: 1.07x slower                                                  |
| sphinx         | 617 ms                                                      | 636 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                       | 1.03x slower                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                    |
| async_tree_memoization_tg  | 281 ms                                                      | 206 ms: 1.36x faster                                                    |
| async_tree_none            | 219 ms                                                      | 165 ms: 1.33x faster                                                    |
| async_tree_memoization     | 265 ms                                                      | 203 ms: 1.30x faster                                                    |
| async_tree_io              | 513 ms                                                      | 394 ms: 1.30x faster                                                    |
| async_tree_io_tg           | 497 ms                                                      | 389 ms: 1.28x faster                                                    |
| async_tree_none_tg         | 200 ms                                                      | 165 ms: 1.21x faster                                                    |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 333 ms: 1.15x faster                                                    |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                    |
| async_generators           | 223 ms                                                      | 252 ms: 1.13x slower                                                    |
| coroutines                 | 12.5 ms                                                     | 14.6 ms: 1.17x slower                                                   |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 53.2 ms: 1.25x faster                                                   |
| float          | 50.8 ms                                                     | 44.0 ms: 1.16x faster                                                   |
| pidigits       | 146 ms                                                      | 145 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                       | 1.13x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.2 ms: 1.67x faster                                                   |
| regex_effbot   | 1.69 ms                                                     | 1.57 ms: 1.08x faster                                                   |
| regex_compile  | 80.7 ms                                                     | 78.7 ms: 1.03x faster                                                   |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                       | 1.15x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.12 sec: 1.23x faster                                                  |
| unpickle_pure_python | 130 us                                                      | 106 us: 1.22x faster                                                    |
| xml_etree_generate   | 53.5 ms                                                     | 49.7 ms: 1.08x faster                                                   |
| xml_etree_parse      | 92.2 ms                                                     | 87.5 ms: 1.05x faster                                                   |
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                   |
| xml_etree_process    | 36.5 ms                                                     | 35.2 ms: 1.04x faster                                                   |
| json_dumps           | 6.19 ms                                                     | 6.30 ms: 1.02x slower                                                   |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.9 ms: 1.04x slower                                                   |
| pickle_pure_python   | 186 us                                                      | 203 us: 1.09x slower                                                    |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                   |
| python_startup_no_site | 16.9 ms                                                     | 19.2 ms: 1.14x slower                                                   |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.40 ms: 1.22x faster                                                   |
| genshi_text     | 15.2 ms                                                     | 15.6 ms: 1.02x slower                                                   |
| django_template | 20.3 ms                                                     | 24.6 ms: 1.21x slower                                                   |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 483 us: 17.51x faster                                                   |
| pathlib                    | 75.3 ms                                                     | 28.6 ms: 2.64x faster                                                   |
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                    |
| mdp                        | 1.43 sec                                                    | 809 ms: 1.77x faster                                                    |
| regex_v8                   | 23.8 ms                                                     | 14.2 ms: 1.67x faster                                                   |
| async_tree_memoization_tg  | 281 ms                                                      | 206 ms: 1.36x faster                                                    |
| async_tree_none            | 219 ms                                                      | 165 ms: 1.33x faster                                                    |
| deepcopy                   | 223 us                                                      | 171 us: 1.31x faster                                                    |
| async_tree_memoization     | 265 ms                                                      | 203 ms: 1.30x faster                                                    |
| async_tree_io              | 513 ms                                                      | 394 ms: 1.30x faster                                                    |
| deepcopy_memo              | 23.1 us                                                     | 17.9 us: 1.29x faster                                                   |
| async_tree_io_tg           | 497 ms                                                      | 389 ms: 1.28x faster                                                    |
| nbody                      | 66.3 ms                                                     | 53.2 ms: 1.25x faster                                                   |
| tomli_loads                | 1.37 sec                                                    | 1.12 sec: 1.23x faster                                                  |
| unpickle_pure_python       | 130 us                                                      | 106 us: 1.22x faster                                                    |
| mako                       | 6.56 ms                                                     | 5.40 ms: 1.22x faster                                                   |
| async_tree_none_tg         | 200 ms                                                      | 165 ms: 1.21x faster                                                    |
| float                      | 50.8 ms                                                     | 44.0 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 333 ms: 1.15x faster                                                    |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                    |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.28 ms: 1.14x faster                                                   |
| telco                      | 4.85 ms                                                     | 4.26 ms: 1.14x faster                                                   |
| scimark_fft                | 175 ms                                                      | 154 ms: 1.13x faster                                                    |
| pyflate                    | 283 ms                                                      | 250 ms: 1.13x faster                                                    |
| go                         | 84.7 ms                                                     | 75.8 ms: 1.12x faster                                                   |
| pprint_safe_repr           | 485 ms                                                      | 437 ms: 1.11x faster                                                    |
| fannkuch                   | 252 ms                                                      | 228 ms: 1.10x faster                                                    |
| json                       | 3.30 ms                                                     | 3.00 ms: 1.10x faster                                                   |
| deepcopy_reduce            | 2.02 us                                                     | 1.85 us: 1.09x faster                                                   |
| bpe_tokeniser              | 2.87 sec                                                    | 2.63 sec: 1.09x faster                                                  |
| pprint_pformat             | 977 ms                                                      | 895 ms: 1.09x faster                                                    |
| regex_effbot               | 1.69 ms                                                     | 1.57 ms: 1.08x faster                                                   |
| xml_etree_generate         | 53.5 ms                                                     | 49.7 ms: 1.08x faster                                                   |
| k_core                     | 1.70 sec                                                    | 1.59 sec: 1.06x faster                                                  |
| xml_etree_parse            | 92.2 ms                                                     | 87.5 ms: 1.05x faster                                                   |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                   |
| xml_etree_process          | 36.5 ms                                                     | 35.2 ms: 1.04x faster                                                   |
| regex_compile              | 80.7 ms                                                     | 78.7 ms: 1.03x faster                                                   |
| meteor_contest             | 72.0 ms                                                     | 70.6 ms: 1.02x faster                                                   |
| sqlite_synth               | 1.59 us                                                     | 1.56 us: 1.02x faster                                                   |
| logging_silent             | 54.6 ns                                                     | 54.0 ns: 1.01x faster                                                   |
| pidigits                   | 146 ms                                                      | 145 ms: 1.01x faster                                                    |
| scimark_sor                | 76.2 ms                                                     | 76.5 ms: 1.00x slower                                                   |
| comprehensions             | 10.4 us                                                     | 10.4 us: 1.01x slower                                                   |
| connected_components       | 320 ms                                                      | 322 ms: 1.01x slower                                                    |
| crypto_pyaes               | 45.6 ms                                                     | 46.1 ms: 1.01x slower                                                   |
| richards_super             | 29.8 ms                                                     | 30.2 ms: 1.01x slower                                                   |
| json_dumps                 | 6.19 ms                                                     | 6.30 ms: 1.02x slower                                                   |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.5 ms: 1.02x slower                                                   |
| sympy_integrate            | 12.3 ms                                                     | 12.6 ms: 1.02x slower                                                   |
| genshi_text                | 15.2 ms                                                     | 15.6 ms: 1.02x slower                                                   |
| 2to3                       | 215 ms                                                      | 220 ms: 1.02x slower                                                    |
| sympy_str                  | 167 ms                                                      | 171 ms: 1.02x slower                                                    |
| sphinx                     | 617 ms                                                      | 636 ms: 1.03x slower                                                    |
| sympy_sum                  | 85.2 ms                                                     | 87.9 ms: 1.03x slower                                                   |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                   |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.9 ms: 1.04x slower                                                   |
| sympy_expand               | 286 ms                                                      | 297 ms: 1.04x slower                                                    |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                    |
| hexiom                     | 3.84 ms                                                     | 4.09 ms: 1.06x slower                                                   |
| docutils                   | 1.53 sec                                                    | 1.63 sec: 1.07x slower                                                  |
| create_gc_cycles           | 1.22 ms                                                     | 1.31 ms: 1.07x slower                                                   |
| python_startup             | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                   |
| nqueens                    | 56.1 ms                                                     | 60.3 ms: 1.07x slower                                                   |
| logging_format             | 6.18 us                                                     | 6.67 us: 1.08x slower                                                   |
| logging_simple             | 5.77 us                                                     | 6.24 us: 1.08x slower                                                   |
| pickle_pure_python         | 186 us                                                      | 203 us: 1.09x slower                                                    |
| gc_traversal               | 1.96 ms                                                     | 2.14 ms: 1.09x slower                                                   |
| chaos                      | 37.9 ms                                                     | 41.3 ms: 1.09x slower                                                   |
| spectral_norm              | 63.4 ms                                                     | 70.3 ms: 1.11x slower                                                   |
| async_generators           | 223 ms                                                      | 252 ms: 1.13x slower                                                    |
| scimark_lu                 | 56.7 ms                                                     | 64.5 ms: 1.14x slower                                                   |
| python_startup_no_site     | 16.9 ms                                                     | 19.2 ms: 1.14x slower                                                   |
| deltablue                  | 1.89 ms                                                     | 2.17 ms: 1.15x slower                                                   |
| coverage                   | 45.3 ms                                                     | 52.2 ms: 1.15x slower                                                   |
| raytrace                   | 153 ms                                                      | 180 ms: 1.17x slower                                                    |
| coroutines                 | 12.5 ms                                                     | 14.6 ms: 1.17x slower                                                   |
| django_template            | 20.3 ms                                                     | 24.6 ms: 1.21x slower                                                   |
| many_optionals             | 361 us                                                      | 444 us: 1.23x slower                                                    |
| subparsers                 | 10.9 ms                                                     | 17.1 ms: 1.57x slower                                                   |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                            |

Benchmark hidden because not significant (8): pylint, html5lib, shortest_path, pycparser, dulwich_log, typing_runtime_protocols, richards, genshi_xml
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250708-3.15.0a0-997a858-JIT/bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.090x faster

# HPT report

- Reliability score: 90.51% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown