# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_shim
- machine: windows-amd64
- commit hash: a6ef3b7
- commit date: 2025-07-25
- overall geometric mean: 1.064x faster
- HPT reliability: 67.67%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 223 ms: 1.04x slower                                                 |
| docutils       | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                               |
| html5lib       | 38.2 ms                                                     | 39.2 ms: 1.03x slower                                                |
| sphinx         | 617 ms                                                      | 639 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                       | 1.05x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 164 ms: 1.83x faster                                                 |
| async_tree_io              | 513 ms                                                      | 389 ms: 1.32x faster                                                 |
| async_tree_memoization_tg  | 281 ms                                                      | 218 ms: 1.29x faster                                                 |
| async_tree_io_tg           | 497 ms                                                      | 395 ms: 1.26x faster                                                 |
| async_tree_none            | 219 ms                                                      | 176 ms: 1.24x faster                                                 |
| async_tree_memoization     | 265 ms                                                      | 216 ms: 1.23x faster                                                 |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 344 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 350 ms: 1.09x faster                                                 |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                 |
| coroutines                 | 12.5 ms                                                     | 14.9 ms: 1.19x slower                                                |
| Geometric mean             | (ref)                                                       | 1.18x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 57.0 ms: 1.16x faster                                                |
| float          | 50.8 ms                                                     | 43.9 ms: 1.16x faster                                                |
| pidigits       | 146 ms                                                      | 149 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                       | 1.10x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.4 ms: 1.66x faster                                                |
| regex_effbot   | 1.69 ms                                                     | 1.67 ms: 1.02x faster                                                |
| regex_compile  | 80.7 ms                                                     | 82.5 ms: 1.02x slower                                                |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                       | 1.12x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.12 sec: 1.22x faster                                               |
| unpickle_pure_python | 130 us                                                      | 109 us: 1.19x faster                                                 |
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                |
| xml_etree_generate   | 53.5 ms                                                     | 51.4 ms: 1.04x faster                                                |
| xml_etree_parse      | 92.2 ms                                                     | 89.8 ms: 1.03x faster                                                |
| xml_etree_process    | 36.5 ms                                                     | 36.0 ms: 1.01x faster                                                |
| json_dumps           | 6.19 ms                                                     | 6.30 ms: 1.02x slower                                                |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.9 ms: 1.07x slower                                                |
| pickle_pure_python   | 186 us                                                      | 211 us: 1.14x slower                                                 |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 27.1 ms: 1.11x slower                                                |
| python_startup_no_site | 16.9 ms                                                     | 20.1 ms: 1.19x slower                                                |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.33 ms: 1.23x faster                                                |
| genshi_text     | 15.2 ms                                                     | 15.8 ms: 1.04x slower                                                |
| genshi_xml      | 33.9 ms                                                     | 35.6 ms: 1.05x slower                                                |
| django_template | 20.3 ms                                                     | 24.8 ms: 1.22x slower                                                |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 505 us: 16.77x faster                                                |
| pathlib                    | 75.3 ms                                                     | 33.1 ms: 2.28x faster                                                |
| asyncio_websockets         | 300 ms                                                      | 164 ms: 1.83x faster                                                 |
| mdp                        | 1.43 sec                                                    | 802 ms: 1.78x faster                                                 |
| regex_v8                   | 23.8 ms                                                     | 14.4 ms: 1.66x faster                                                |
| deepcopy                   | 223 us                                                      | 168 us: 1.33x faster                                                 |
| async_tree_io              | 513 ms                                                      | 389 ms: 1.32x faster                                                 |
| deepcopy_memo              | 23.1 us                                                     | 17.8 us: 1.30x faster                                                |
| async_tree_memoization_tg  | 281 ms                                                      | 218 ms: 1.29x faster                                                 |
| async_tree_io_tg           | 497 ms                                                      | 395 ms: 1.26x faster                                                 |
| async_tree_none            | 219 ms                                                      | 176 ms: 1.24x faster                                                 |
| mako                       | 6.56 ms                                                     | 5.33 ms: 1.23x faster                                                |
| async_tree_memoization     | 265 ms                                                      | 216 ms: 1.23x faster                                                 |
| tomli_loads                | 1.37 sec                                                    | 1.12 sec: 1.22x faster                                               |
| unpickle_pure_python       | 130 us                                                      | 109 us: 1.19x faster                                                 |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                 |
| nbody                      | 66.3 ms                                                     | 57.0 ms: 1.16x faster                                                |
| float                      | 50.8 ms                                                     | 43.9 ms: 1.16x faster                                                |
| fannkuch                   | 252 ms                                                      | 217 ms: 1.16x faster                                                 |
| bpe_tokeniser              | 2.87 sec                                                    | 2.52 sec: 1.14x faster                                               |
| scimark_fft                | 175 ms                                                      | 154 ms: 1.13x faster                                                 |
| json                       | 3.30 ms                                                     | 2.93 ms: 1.13x faster                                                |
| pyflate                    | 283 ms                                                      | 252 ms: 1.12x faster                                                 |
| telco                      | 4.85 ms                                                     | 4.33 ms: 1.12x faster                                                |
| deepcopy_reduce            | 2.02 us                                                     | 1.81 us: 1.12x faster                                                |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 344 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 350 ms: 1.09x faster                                                 |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.40 ms: 1.09x faster                                                |
| pprint_safe_repr           | 485 ms                                                      | 451 ms: 1.07x faster                                                 |
| go                         | 84.7 ms                                                     | 78.8 ms: 1.07x faster                                                |
| pprint_pformat             | 977 ms                                                      | 911 ms: 1.07x faster                                                 |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                |
| xml_etree_generate         | 53.5 ms                                                     | 51.4 ms: 1.04x faster                                                |
| k_core                     | 1.70 sec                                                    | 1.64 sec: 1.04x faster                                               |
| xml_etree_parse            | 92.2 ms                                                     | 89.8 ms: 1.03x faster                                                |
| sqlite_synth               | 1.59 us                                                     | 1.55 us: 1.02x faster                                                |
| regex_effbot               | 1.69 ms                                                     | 1.67 ms: 1.02x faster                                                |
| xml_etree_process          | 36.5 ms                                                     | 36.0 ms: 1.01x faster                                                |
| shortest_path              | 355 ms                                                      | 358 ms: 1.01x slower                                                 |
| json_dumps                 | 6.19 ms                                                     | 6.30 ms: 1.02x slower                                                |
| pidigits                   | 146 ms                                                      | 149 ms: 1.02x slower                                                 |
| scimark_sor                | 76.2 ms                                                     | 77.7 ms: 1.02x slower                                                |
| connected_components       | 320 ms                                                      | 327 ms: 1.02x slower                                                 |
| regex_compile              | 80.7 ms                                                     | 82.5 ms: 1.02x slower                                                |
| meteor_contest             | 72.0 ms                                                     | 73.8 ms: 1.03x slower                                                |
| html5lib                   | 38.2 ms                                                     | 39.2 ms: 1.03x slower                                                |
| logging_silent             | 54.6 ns                                                     | 56.1 ns: 1.03x slower                                                |
| spectral_norm              | 63.4 ms                                                     | 65.5 ms: 1.03x slower                                                |
| dulwich_log                | 40.1 ms                                                     | 41.4 ms: 1.03x slower                                                |
| scimark_monte_carlo        | 40.7 ms                                                     | 42.2 ms: 1.04x slower                                                |
| sphinx                     | 617 ms                                                      | 639 ms: 1.04x slower                                                 |
| genshi_text                | 15.2 ms                                                     | 15.8 ms: 1.04x slower                                                |
| 2to3                       | 215 ms                                                      | 223 ms: 1.04x slower                                                 |
| sympy_str                  | 167 ms                                                      | 173 ms: 1.04x slower                                                 |
| richards_super             | 29.8 ms                                                     | 31.0 ms: 1.04x slower                                                |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.04x slower                                                 |
| typing_runtime_protocols   | 103 us                                                      | 108 us: 1.04x slower                                                 |
| sympy_expand               | 286 ms                                                      | 300 ms: 1.05x slower                                                 |
| genshi_xml                 | 33.9 ms                                                     | 35.6 ms: 1.05x slower                                                |
| logging_simple             | 5.77 us                                                     | 6.06 us: 1.05x slower                                                |
| generators                 | 19.0 ms                                                     | 20.0 ms: 1.05x slower                                                |
| richards                   | 26.3 ms                                                     | 27.7 ms: 1.06x slower                                                |
| scimark_lu                 | 56.7 ms                                                     | 59.9 ms: 1.06x slower                                                |
| chaos                      | 37.9 ms                                                     | 40.1 ms: 1.06x slower                                                |
| hexiom                     | 3.84 ms                                                     | 4.11 ms: 1.07x slower                                                |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.9 ms: 1.07x slower                                                |
| nqueens                    | 56.1 ms                                                     | 60.2 ms: 1.07x slower                                                |
| sympy_sum                  | 85.2 ms                                                     | 91.4 ms: 1.07x slower                                                |
| docutils                   | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                               |
| sympy_integrate            | 12.3 ms                                                     | 13.4 ms: 1.08x slower                                                |
| logging_format             | 6.18 us                                                     | 6.71 us: 1.09x slower                                                |
| python_startup             | 24.4 ms                                                     | 27.1 ms: 1.11x slower                                                |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                 |
| coverage                   | 45.3 ms                                                     | 51.2 ms: 1.13x slower                                                |
| create_gc_cycles           | 1.22 ms                                                     | 1.39 ms: 1.13x slower                                                |
| pickle_pure_python         | 186 us                                                      | 211 us: 1.14x slower                                                 |
| gc_traversal               | 1.96 ms                                                     | 2.24 ms: 1.14x slower                                                |
| deltablue                  | 1.89 ms                                                     | 2.19 ms: 1.16x slower                                                |
| raytrace                   | 153 ms                                                      | 181 ms: 1.18x slower                                                 |
| coroutines                 | 12.5 ms                                                     | 14.9 ms: 1.19x slower                                                |
| python_startup_no_site     | 16.9 ms                                                     | 20.1 ms: 1.19x slower                                                |
| django_template            | 20.3 ms                                                     | 24.8 ms: 1.22x slower                                                |
| many_optionals             | 361 us                                                      | 576 us: 1.60x slower                                                 |
| subparsers                 | 10.9 ms                                                     | 30.3 ms: 2.79x slower                                                |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                         |

Benchmark hidden because not significant (4): pylint, crypto_pyaes, comprehensions, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-pythonperf1-amd64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 67.67% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown