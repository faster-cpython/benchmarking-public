# Results vs. 3.13.0

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.034x faster
- HPT reliability: 98.69%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 290 ms: 1.01x faster                                                |
| docutils       | 2.83 sec                                                     | 2.96 sec: 1.05x slower                                              |
| html5lib       | 73.5 ms                                                      | 69.8 ms: 1.05x faster                                               |
| sphinx         | 1.12 sec                                                     | 1.14 sec: 1.01x slower                                              |
| Geometric mean | (ref)                                                        | 1.00x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 328 ms: 1.42x faster                                                |
| async_tree_io              | 843 ms                                                       | 637 ms: 1.32x faster                                                |
| async_tree_io_tg           | 831 ms                                                       | 629 ms: 1.32x faster                                                |
| async_tree_none            | 376 ms                                                       | 287 ms: 1.31x faster                                                |
| async_tree_none_tg         | 346 ms                                                       | 270 ms: 1.28x faster                                                |
| async_tree_memoization     | 453 ms                                                       | 355 ms: 1.28x faster                                                |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 499 ms: 1.16x faster                                                |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 520 ms: 1.16x faster                                                |
| coroutines                 | 21.6 ms                                                      | 20.9 ms: 1.03x faster                                               |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                |
| async_generators           | 457 ms                                                       | 467 ms: 1.02x slower                                                |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 68.1 ms: 1.19x faster                                               |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                |
| nbody          | 89.3 ms                                                      | 98.2 ms: 1.10x slower                                               |
| Geometric mean | (ref)                                                        | 1.02x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.17 ms: 1.16x faster                                               |
| regex_dna      | 247 ms                                                       | 231 ms: 1.07x faster                                                |
| regex_compile  | 143 ms                                                       | 138 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                        | 1.07x faster                                                        |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.03 sec: 1.21x faster                                              |
| xml_etree_parse      | 150 ms                                                       | 137 ms: 1.10x faster                                                |
| unpickle_pure_python | 217 us                                                       | 198 us: 1.10x faster                                                |
| xml_etree_iterparse  | 103 ms                                                       | 93.9 ms: 1.10x faster                                               |
| xml_etree_process    | 61.2 ms                                                      | 57.7 ms: 1.06x faster                                               |
| xml_etree_generate   | 86.5 ms                                                      | 81.7 ms: 1.06x faster                                               |
| json_loads           | 24.7 us                                                      | 24.0 us: 1.03x faster                                               |
| pickle_pure_python   | 323 us                                                       | 335 us: 1.04x slower                                                |
| Geometric mean       | (ref)                                                        | 1.07x faster                                                        |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.05 ms: 1.01x slower                                               |
| python_startup         | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.61 ms: 1.08x faster                                               |
| genshi_text     | 26.2 ms                                                      | 27.0 ms: 1.03x slower                                               |
| django_template | 36.4 ms                                                      | 39.2 ms: 1.08x slower                                               |
| genshi_xml      | 57.1 ms                                                      | 62.9 ms: 1.10x slower                                               |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 328 ms: 1.42x faster                                                |
| deepcopy_memo              | 38.6 us                                                      | 27.9 us: 1.38x faster                                               |
| async_tree_io              | 843 ms                                                       | 637 ms: 1.32x faster                                                |
| async_tree_io_tg           | 831 ms                                                       | 629 ms: 1.32x faster                                                |
| async_tree_none            | 376 ms                                                       | 287 ms: 1.31x faster                                                |
| deepcopy                   | 392 us                                                       | 299 us: 1.31x faster                                                |
| async_tree_none_tg         | 346 ms                                                       | 270 ms: 1.28x faster                                                |
| async_tree_memoization     | 453 ms                                                       | 355 ms: 1.28x faster                                                |
| scimark_sor                | 123 ms                                                       | 98.7 ms: 1.25x faster                                               |
| tomli_loads                | 2.46 sec                                                     | 2.03 sec: 1.21x faster                                              |
| float                      | 81.3 ms                                                      | 68.1 ms: 1.19x faster                                               |
| deepcopy_reduce            | 3.54 us                                                      | 2.98 us: 1.19x faster                                               |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 499 ms: 1.16x faster                                                |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 520 ms: 1.16x faster                                                |
| regex_effbot               | 3.67 ms                                                      | 3.17 ms: 1.16x faster                                               |
| richards                   | 52.9 ms                                                      | 46.3 ms: 1.14x faster                                               |
| richards_super             | 59.6 ms                                                      | 52.5 ms: 1.14x faster                                               |
| telco                      | 8.79 ms                                                      | 7.79 ms: 1.13x faster                                               |
| go                         | 162 ms                                                       | 145 ms: 1.12x faster                                                |
| json                       | 5.69 ms                                                      | 5.09 ms: 1.12x faster                                               |
| xml_etree_parse            | 150 ms                                                       | 137 ms: 1.10x faster                                                |
| unpickle_pure_python       | 217 us                                                       | 198 us: 1.10x faster                                                |
| xml_etree_iterparse        | 103 ms                                                       | 93.9 ms: 1.10x faster                                               |
| scimark_fft                | 328 ms                                                       | 300 ms: 1.09x faster                                                |
| pyflate                    | 503 ms                                                       | 463 ms: 1.09x faster                                                |
| mako                       | 10.4 ms                                                      | 9.61 ms: 1.08x faster                                               |
| spectral_norm              | 97.0 ms                                                      | 90.1 ms: 1.08x faster                                               |
| bpe_tokeniser              | 5.09 sec                                                     | 4.73 sec: 1.08x faster                                              |
| connected_components       | 432 ms                                                       | 403 ms: 1.07x faster                                                |
| regex_dna                  | 247 ms                                                       | 231 ms: 1.07x faster                                                |
| k_core                     | 2.17 sec                                                     | 2.04 sec: 1.06x faster                                              |
| pathlib                    | 17.5 ms                                                      | 16.5 ms: 1.06x faster                                               |
| xml_etree_process          | 61.2 ms                                                      | 57.7 ms: 1.06x faster                                               |
| xml_etree_generate         | 86.5 ms                                                      | 81.7 ms: 1.06x faster                                               |
| scimark_monte_carlo        | 66.1 ms                                                      | 62.6 ms: 1.06x faster                                               |
| html5lib                   | 73.5 ms                                                      | 69.8 ms: 1.05x faster                                               |
| shortest_path              | 460 ms                                                       | 438 ms: 1.05x faster                                                |
| pprint_pformat             | 1.72 sec                                                     | 1.64 sec: 1.05x faster                                              |
| pylint                     | 347 ms                                                       | 331 ms: 1.05x faster                                                |
| pprint_safe_repr           | 843 ms                                                       | 807 ms: 1.04x faster                                                |
| scimark_lu                 | 98.7 ms                                                      | 94.7 ms: 1.04x faster                                               |
| regex_compile              | 143 ms                                                       | 138 ms: 1.03x faster                                                |
| sqlite_synth               | 2.91 us                                                      | 2.82 us: 1.03x faster                                               |
| coroutines                 | 21.6 ms                                                      | 20.9 ms: 1.03x faster                                               |
| sqlglot_parse              | 1.40 ms                                                      | 1.36 ms: 1.03x faster                                               |
| json_loads                 | 24.7 us                                                      | 24.0 us: 1.03x faster                                               |
| thrift                     | 901 us                                                       | 879 us: 1.02x faster                                                |
| dulwich_log                | 68.2 ms                                                      | 66.9 ms: 1.02x faster                                               |
| sqlalchemy_declarative     | 148 ms                                                       | 146 ms: 1.01x faster                                                |
| sqlglot_transpile          | 1.79 ms                                                      | 1.77 ms: 1.01x faster                                               |
| 2to3                       | 293 ms                                                       | 290 ms: 1.01x faster                                                |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                |
| sqlalchemy_imperative      | 18.3 ms                                                      | 18.1 ms: 1.01x faster                                               |
| coverage                   | 80.0 ms                                                      | 79.4 ms: 1.01x faster                                               |
| python_startup_no_site     | 8.96 ms                                                      | 9.05 ms: 1.01x slower                                               |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                |
| python_startup             | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                               |
| sphinx                     | 1.12 sec                                                     | 1.14 sec: 1.01x slower                                              |
| mdp                        | 2.54 sec                                                     | 2.58 sec: 1.01x slower                                              |
| pycparser                  | 1.24 sec                                                     | 1.26 sec: 1.01x slower                                              |
| crypto_pyaes               | 73.3 ms                                                      | 74.5 ms: 1.02x slower                                               |
| meteor_contest             | 130 ms                                                       | 132 ms: 1.02x slower                                                |
| sympy_expand               | 509 ms                                                       | 520 ms: 1.02x slower                                                |
| sympy_integrate            | 23.6 ms                                                      | 24.1 ms: 1.02x slower                                               |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.88 ms: 1.02x slower                                               |
| async_generators           | 457 ms                                                       | 467 ms: 1.02x slower                                                |
| sympy_str                  | 298 ms                                                       | 305 ms: 1.02x slower                                                |
| deltablue                  | 3.42 ms                                                      | 3.51 ms: 1.03x slower                                               |
| logging_silent             | 97.9 ns                                                      | 101 ns: 1.03x slower                                                |
| sympy_sum                  | 155 ms                                                       | 159 ms: 1.03x slower                                                |
| genshi_text                | 26.2 ms                                                      | 27.0 ms: 1.03x slower                                               |
| sqlglot_normalize          | 119 ms                                                       | 123 ms: 1.03x slower                                                |
| sqlglot_optimize           | 59.3 ms                                                      | 61.4 ms: 1.04x slower                                               |
| pickle_pure_python         | 323 us                                                       | 335 us: 1.04x slower                                                |
| logging_simple             | 6.39 us                                                      | 6.63 us: 1.04x slower                                               |
| docutils                   | 2.83 sec                                                     | 2.96 sec: 1.05x slower                                              |
| fannkuch                   | 363 ms                                                       | 382 ms: 1.05x slower                                                |
| bench_thread_pool          | 942 us                                                       | 995 us: 1.06x slower                                                |
| logging_format             | 6.94 us                                                      | 7.36 us: 1.06x slower                                               |
| typing_runtime_protocols   | 169 us                                                       | 180 us: 1.06x slower                                                |
| django_template            | 36.4 ms                                                      | 39.2 ms: 1.08x slower                                               |
| nbody                      | 89.3 ms                                                      | 98.2 ms: 1.10x slower                                               |
| genshi_xml                 | 57.1 ms                                                      | 62.9 ms: 1.10x slower                                               |
| nqueens                    | 90.7 ms                                                      | 102 ms: 1.13x slower                                                |
| many_optionals             | 930 us                                                       | 1.05 ms: 1.13x slower                                               |
| hexiom                     | 6.55 ms                                                      | 7.42 ms: 1.13x slower                                               |
| comprehensions             | 17.0 us                                                      | 19.3 us: 1.13x slower                                               |
| chaos                      | 60.2 ms                                                      | 68.2 ms: 1.13x slower                                               |
| generators                 | 33.6 ms                                                      | 39.9 ms: 1.19x slower                                               |
| raytrace                   | 273 ms                                                       | 334 ms: 1.22x slower                                                |
| subparsers                 | 17.5 ms                                                      | 23.2 ms: 1.33x slower                                               |
| gc_traversal               | 4.74 ms                                                      | 6.32 ms: 1.33x slower                                               |
| bench_mp_pool              | 5.12 ms                                                      | 1.48 sec: 289.81x slower                                            |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                        |

Benchmark hidden because not significant (3): regex_v8, json_dumps, create_gc_cycles
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250107-3.14.0a3+-f098037-JIT/bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037.json: mypy2

- Geometric mean (including insignificant results): 1.034x faster

# HPT report

- Reliability score: 98.69% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x