# Results vs. 3.13.0

- fork: python
- ref: 9c7b2af73dee2b997936
- machine: linux-x86_64
- commit hash: 9c7b2af
- commit date: 2025-07-21
- overall geometric mean: 1.041x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 286 ms: 1.02x faster                                                        |
| docutils       | 2.83 sec                                                     | 2.92 sec: 1.03x slower                                                      |
| html5lib       | 73.5 ms                                                      | 67.5 ms: 1.09x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 329 ms: 1.38x faster                                                        |
| async_tree_none            | 376 ms                                                       | 274 ms: 1.37x faster                                                        |
| async_tree_io              | 843 ms                                                       | 625 ms: 1.35x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 633 ms: 1.31x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 272 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 500 ms: 1.21x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 507 ms: 1.15x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 381 ms: 1.02x faster                                                        |
| async_generators           | 457 ms                                                       | 448 ms: 1.02x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 64.2 ms: 1.27x faster                                                       |
| pidigits       | 252 ms                                                       | 256 ms: 1.01x slower                                                        |
| nbody          | 89.3 ms                                                      | 98.4 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 22.9 ms: 1.14x faster                                                       |
| regex_dna      | 247 ms                                                       | 228 ms: 1.08x faster                                                        |
| regex_compile  | 143 ms                                                       | 132 ms: 1.08x faster                                                        |
| regex_effbot   | 3.67 ms                                                      | 3.71 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.92 sec: 1.28x faster                                                      |
| unpickle_pure_python | 217 us                                                       | 197 us: 1.11x faster                                                        |
| xml_etree_parse      | 150 ms                                                       | 138 ms: 1.09x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 56.6 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 96.9 ms: 1.06x faster                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 81.6 ms: 1.06x faster                                                       |
| json_loads           | 24.7 us                                                      | 24.9 us: 1.01x slower                                                       |
| json_dumps           | 11.1 ms                                                      | 11.3 ms: 1.01x slower                                                       |
| pickle_pure_python   | 323 us                                                       | 334 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.72 ms: 1.03x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.0 ms: 1.14x faster                                                       |
| mako            | 10.4 ms                                                      | 9.65 ms: 1.07x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 54.4 ms: 1.05x faster                                                       |
| django_template | 36.4 ms                                                      | 35.5 ms: 1.03x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.07x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.28 sec: 1.98x faster                                                      |
| richards                   | 52.9 ms                                                      | 35.0 ms: 1.51x faster                                                       |
| richards_super             | 59.6 ms                                                      | 40.8 ms: 1.46x faster                                                       |
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                                        |
| deepcopy                   | 392 us                                                       | 280 us: 1.40x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 329 ms: 1.38x faster                                                        |
| async_tree_none            | 376 ms                                                       | 274 ms: 1.37x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 28.3 us: 1.36x faster                                                       |
| async_tree_io              | 843 ms                                                       | 625 ms: 1.35x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 633 ms: 1.31x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 1.92 sec: 1.28x faster                                                      |
| async_tree_none_tg         | 346 ms                                                       | 272 ms: 1.27x faster                                                        |
| go                         | 162 ms                                                       | 128 ms: 1.27x faster                                                        |
| float                      | 81.3 ms                                                      | 64.2 ms: 1.27x faster                                                       |
| spectral_norm              | 97.0 ms                                                      | 79.2 ms: 1.22x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 500 ms: 1.21x faster                                                        |
| scimark_sor                | 123 ms                                                       | 103 ms: 1.20x faster                                                        |
| pyflate                    | 503 ms                                                       | 421 ms: 1.20x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 2.90 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 3.03 us: 1.17x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 58.4 ms: 1.17x faster                                                       |
| generators                 | 33.6 ms                                                      | 29.0 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 507 ms: 1.15x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.50 sec: 1.14x faster                                                      |
| regex_v8                   | 26.1 ms                                                      | 22.9 ms: 1.14x faster                                                       |
| genshi_text                | 26.2 ms                                                      | 23.0 ms: 1.14x faster                                                       |
| pprint_safe_repr           | 843 ms                                                       | 741 ms: 1.14x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.56 sec: 1.12x faster                                                      |
| unpickle_pure_python       | 217 us                                                       | 197 us: 1.11x faster                                                        |
| scimark_fft                | 328 ms                                                       | 300 ms: 1.09x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 138 ms: 1.09x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 67.5 ms: 1.09x faster                                                       |
| regex_dna                  | 247 ms                                                       | 228 ms: 1.08x faster                                                        |
| regex_compile              | 143 ms                                                       | 132 ms: 1.08x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 56.6 ms: 1.08x faster                                                       |
| mako                       | 10.4 ms                                                      | 9.65 ms: 1.07x faster                                                       |
| k_core                     | 2.17 sec                                                     | 2.02 sec: 1.07x faster                                                      |
| thrift                     | 901 us                                                       | 840 us: 1.07x faster                                                        |
| pylint                     | 347 ms                                                       | 324 ms: 1.07x faster                                                        |
| meteor_contest             | 130 ms                                                       | 121 ms: 1.07x faster                                                        |
| connected_components       | 432 ms                                                       | 408 ms: 1.06x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 96.9 ms: 1.06x faster                                                       |
| xml_etree_generate         | 86.5 ms                                                      | 81.6 ms: 1.06x faster                                                       |
| scimark_monte_carlo        | 66.1 ms                                                      | 62.5 ms: 1.06x faster                                                       |
| hexiom                     | 6.55 ms                                                      | 6.20 ms: 1.06x faster                                                       |
| logging_simple             | 6.39 us                                                      | 6.06 us: 1.05x faster                                                       |
| json                       | 5.69 ms                                                      | 5.40 ms: 1.05x faster                                                       |
| sympy_integrate            | 23.6 ms                                                      | 22.4 ms: 1.05x faster                                                       |
| genshi_xml                 | 57.1 ms                                                      | 54.4 ms: 1.05x faster                                                       |
| logging_silent             | 97.9 ns                                                      | 93.8 ns: 1.04x faster                                                       |
| python_startup             | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                       |
| shortest_path              | 460 ms                                                       | 442 ms: 1.04x faster                                                        |
| scimark_lu                 | 98.7 ms                                                      | 95.0 ms: 1.04x faster                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.80 us: 1.04x faster                                                       |
| logging_format             | 6.94 us                                                      | 6.69 us: 1.04x faster                                                       |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| pathlib                    | 17.5 ms                                                      | 17.0 ms: 1.03x faster                                                       |
| python_startup_no_site     | 8.96 ms                                                      | 8.72 ms: 1.03x faster                                                       |
| sympy_str                  | 298 ms                                                       | 291 ms: 1.03x faster                                                        |
| django_template            | 36.4 ms                                                      | 35.5 ms: 1.03x faster                                                       |
| 2to3                       | 293 ms                                                       | 286 ms: 1.02x faster                                                        |
| sympy_expand               | 509 ms                                                       | 498 ms: 1.02x faster                                                        |
| sympy_sum                  | 155 ms                                                       | 151 ms: 1.02x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 381 ms: 1.02x faster                                                        |
| async_generators           | 457 ms                                                       | 448 ms: 1.02x faster                                                        |
| chaos                      | 60.2 ms                                                      | 59.9 ms: 1.00x faster                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.81 ms: 1.01x slower                                                       |
| typing_runtime_protocols   | 169 us                                                       | 171 us: 1.01x slower                                                        |
| pycparser                  | 1.24 sec                                                     | 1.26 sec: 1.01x slower                                                      |
| regex_effbot               | 3.67 ms                                                      | 3.71 ms: 1.01x slower                                                       |
| json_loads                 | 24.7 us                                                      | 24.9 us: 1.01x slower                                                       |
| json_dumps                 | 11.1 ms                                                      | 11.3 ms: 1.01x slower                                                       |
| pidigits                   | 252 ms                                                       | 256 ms: 1.01x slower                                                        |
| fannkuch                   | 363 ms                                                       | 369 ms: 1.02x slower                                                        |
| comprehensions             | 17.0 us                                                      | 17.3 us: 1.02x slower                                                       |
| coverage                   | 80.0 ms                                                      | 81.7 ms: 1.02x slower                                                       |
| nqueens                    | 90.7 ms                                                      | 93.2 ms: 1.03x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                       |
| docutils                   | 2.83 sec                                                     | 2.92 sec: 1.03x slower                                                      |
| pickle_pure_python         | 323 us                                                       | 334 us: 1.03x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 77.3 ms: 1.05x slower                                                       |
| raytrace                   | 273 ms                                                       | 291 ms: 1.07x slower                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.91 ms: 1.08x slower                                                       |
| nbody                      | 89.3 ms                                                      | 98.4 ms: 1.10x slower                                                       |
| many_optionals             | 930 us                                                       | 1.23 ms: 1.32x slower                                                       |
| gc_traversal               | 4.74 ms                                                      | 6.53 ms: 1.38x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 42.9 ms: 2.46x slower                                                       |
| telco                      | 8.79 ms                                                      | 159 ms: 18.09x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (1): djangocms
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250721-3.15.0a0-9c7b2af-JIT/bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.12x