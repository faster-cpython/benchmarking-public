# Results vs. 3.13.0

- fork: python
- ref: a4625d597f9fc2d083fb
- machine: linux-x86_64
- commit hash: a4625d5
- commit date: 2025-06-26
- overall geometric mean: 1.080x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 280 ms: 1.05x faster                                                        |
| html5lib       | 73.5 ms                                                      | 67.3 ms: 1.09x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.08 sec: 1.04x faster                                                      |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 331 ms: 1.37x faster                                                        |
| async_tree_io              | 843 ms                                                       | 631 ms: 1.34x faster                                                        |
| async_tree_none            | 376 ms                                                       | 283 ms: 1.33x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 631 ms: 1.32x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 271 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 504 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 508 ms: 1.15x faster                                                        |
| async_generators           | 457 ms                                                       | 427 ms: 1.07x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.9 ms: 1.02x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 70.6 ms: 1.15x faster                                                       |
| pidigits       | 252 ms                                                       | 260 ms: 1.03x slower                                                        |
| nbody          | 89.3 ms                                                      | 92.3 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.1 ms: 1.13x faster                                                       |
| regex_dna      | 247 ms                                                       | 221 ms: 1.12x faster                                                        |
| regex_compile  | 143 ms                                                       | 133 ms: 1.08x faster                                                        |
| regex_effbot   | 3.67 ms                                                      | 3.49 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.05 sec: 1.20x faster                                                      |
| xml_etree_parse      | 150 ms                                                       | 140 ms: 1.07x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 97.4 ms: 1.06x faster                                                       |
| unpickle_pure_python | 217 us                                                       | 206 us: 1.05x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 58.2 ms: 1.05x faster                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 83.4 ms: 1.04x faster                                                       |
| pickle_pure_python   | 323 us                                                       | 330 us: 1.02x slower                                                        |
| json_loads           | 24.7 us                                                      | 25.5 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.80 ms: 1.02x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 22.8 ms: 1.15x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 52.1 ms: 1.09x faster                                                       |
| django_template | 36.4 ms                                                      | 35.3 ms: 1.03x faster                                                       |
| mako            | 10.4 ms                                                      | 10.8 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.29 sec: 1.97x faster                                                      |
| deepcopy                   | 392 us                                                       | 273 us: 1.44x faster                                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 331 ms: 1.37x faster                                                        |
| go                         | 162 ms                                                       | 119 ms: 1.37x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 28.5 us: 1.36x faster                                                       |
| async_tree_io              | 843 ms                                                       | 631 ms: 1.34x faster                                                        |
| async_tree_none            | 376 ms                                                       | 283 ms: 1.33x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 631 ms: 1.32x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 271 ms: 1.28x faster                                                        |
| pyflate                    | 503 ms                                                       | 402 ms: 1.25x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.94 us: 1.20x faster                                                       |
| tomli_loads                | 2.46 sec                                                     | 2.05 sec: 1.20x faster                                                      |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 504 ms: 1.20x faster                                                        |
| scimark_sor                | 123 ms                                                       | 104 ms: 1.18x faster                                                        |
| richards                   | 52.9 ms                                                      | 45.4 ms: 1.17x faster                                                       |
| richards_super             | 59.6 ms                                                      | 51.7 ms: 1.15x faster                                                       |
| float                      | 81.3 ms                                                      | 70.6 ms: 1.15x faster                                                       |
| telco                      | 8.79 ms                                                      | 7.64 ms: 1.15x faster                                                       |
| genshi_text                | 26.2 ms                                                      | 22.8 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 508 ms: 1.15x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 59.6 ms: 1.14x faster                                                       |
| regex_v8                   | 26.1 ms                                                      | 23.1 ms: 1.13x faster                                                       |
| spectral_norm              | 97.0 ms                                                      | 86.3 ms: 1.12x faster                                                       |
| regex_dna                  | 247 ms                                                       | 221 ms: 1.12x faster                                                        |
| generators                 | 33.6 ms                                                      | 30.1 ms: 1.12x faster                                                       |
| hexiom                     | 6.55 ms                                                      | 5.93 ms: 1.10x faster                                                       |
| genshi_xml                 | 57.1 ms                                                      | 52.1 ms: 1.09x faster                                                       |
| html5lib                   | 73.5 ms                                                      | 67.3 ms: 1.09x faster                                                       |
| scimark_monte_carlo        | 66.1 ms                                                      | 60.6 ms: 1.09x faster                                                       |
| pylint                     | 347 ms                                                       | 319 ms: 1.09x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.58 sec: 1.09x faster                                                      |
| meteor_contest             | 130 ms                                                       | 119 ms: 1.09x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.69 sec: 1.08x faster                                                      |
| pprint_safe_repr           | 843 ms                                                       | 779 ms: 1.08x faster                                                        |
| sympy_integrate            | 23.6 ms                                                      | 21.9 ms: 1.08x faster                                                       |
| regex_compile              | 143 ms                                                       | 133 ms: 1.08x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 140 ms: 1.07x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 3.18 ms: 1.07x faster                                                       |
| async_generators           | 457 ms                                                       | 427 ms: 1.07x faster                                                        |
| scimark_fft                | 328 ms                                                       | 307 ms: 1.07x faster                                                        |
| thrift                     | 901 us                                                       | 846 us: 1.06x faster                                                        |
| logging_simple             | 6.39 us                                                      | 6.01 us: 1.06x faster                                                       |
| json                       | 5.69 ms                                                      | 5.37 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 97.4 ms: 1.06x faster                                                       |
| sympy_expand               | 509 ms                                                       | 483 ms: 1.05x faster                                                        |
| unpickle_pure_python       | 217 us                                                       | 206 us: 1.05x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.49 ms: 1.05x faster                                                       |
| xml_etree_process          | 61.2 ms                                                      | 58.2 ms: 1.05x faster                                                       |
| sympy_str                  | 298 ms                                                       | 284 ms: 1.05x faster                                                        |
| 2to3                       | 293 ms                                                       | 280 ms: 1.05x faster                                                        |
| logging_format             | 6.94 us                                                      | 6.64 us: 1.05x faster                                                       |
| sphinx                     | 1.12 sec                                                     | 1.08 sec: 1.04x faster                                                      |
| comprehensions             | 17.0 us                                                      | 16.3 us: 1.04x faster                                                       |
| logging_silent             | 97.9 ns                                                      | 93.8 ns: 1.04x faster                                                       |
| python_startup             | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                       |
| pathlib                    | 17.5 ms                                                      | 16.9 ms: 1.04x faster                                                       |
| scimark_lu                 | 98.7 ms                                                      | 95.0 ms: 1.04x faster                                                       |
| xml_etree_generate         | 86.5 ms                                                      | 83.4 ms: 1.04x faster                                                       |
| sympy_sum                  | 155 ms                                                       | 149 ms: 1.04x faster                                                        |
| typing_runtime_protocols   | 169 us                                                       | 163 us: 1.03x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.11 sec: 1.03x faster                                                      |
| django_template            | 36.4 ms                                                      | 35.3 ms: 1.03x faster                                                       |
| connected_components       | 432 ms                                                       | 421 ms: 1.03x faster                                                        |
| chaos                      | 60.2 ms                                                      | 58.8 ms: 1.02x faster                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.84 us: 1.02x faster                                                       |
| shortest_path              | 460 ms                                                       | 452 ms: 1.02x faster                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 8.80 ms: 1.02x faster                                                       |
| coroutines                 | 21.6 ms                                                      | 21.9 ms: 1.02x slower                                                       |
| pycparser                  | 1.24 sec                                                     | 1.27 sec: 1.02x slower                                                      |
| pickle_pure_python         | 323 us                                                       | 330 us: 1.02x slower                                                        |
| raytrace                   | 273 ms                                                       | 279 ms: 1.02x slower                                                        |
| pidigits                   | 252 ms                                                       | 260 ms: 1.03x slower                                                        |
| nbody                      | 89.3 ms                                                      | 92.3 ms: 1.03x slower                                                       |
| json_loads                 | 24.7 us                                                      | 25.5 us: 1.03x slower                                                       |
| coverage                   | 80.0 ms                                                      | 82.8 ms: 1.04x slower                                                       |
| mako                       | 10.4 ms                                                      | 10.8 ms: 1.04x slower                                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.83 ms: 1.05x slower                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 77.9 ms: 1.06x slower                                                       |
| many_optionals             | 930 us                                                       | 1.03 ms: 1.11x slower                                                       |
| gc_traversal               | 4.74 ms                                                      | 6.47 ms: 1.36x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 24.8 ms: 1.42x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.08x faster                                                                |

Benchmark hidden because not significant (7): djangocms, docutils, scimark_sparse_mat_mult, fannkuch, asyncio_websockets, nqueens, json_dumps
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250626-3.15.0a0-a4625d5/bm-20250626-pythonperf2-x86_64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.080x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.09x