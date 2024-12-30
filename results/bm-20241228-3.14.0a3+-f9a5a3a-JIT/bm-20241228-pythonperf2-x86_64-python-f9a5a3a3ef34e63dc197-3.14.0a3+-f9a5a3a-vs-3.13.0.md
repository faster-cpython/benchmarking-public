# Results vs. 3.13.0

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: linux-x86_64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.029x faster
- HPT reliability: 97.54%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| docutils       | 2.83 sec                                                     | 2.98 sec: 1.06x slower                                                       |
| html5lib       | 73.5 ms                                                      | 69.5 ms: 1.06x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.16 sec: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 333 ms: 1.40x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 646 ms: 1.29x faster                                                         |
| async_tree_io              | 843 ms                                                       | 661 ms: 1.28x faster                                                         |
| async_tree_none            | 376 ms                                                       | 297 ms: 1.27x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 274 ms: 1.27x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 366 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 508 ms: 1.15x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 527 ms: 1.15x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.18x faster                                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 73.0 ms: 1.11x faster                                                        |
| pidigits       | 252 ms                                                       | 253 ms: 1.00x slower                                                         |
| nbody          | 89.3 ms                                                      | 92.6 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.23 ms: 1.14x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 24.9 ms: 1.05x faster                                                        |
| regex_compile  | 143 ms                                                       | 139 ms: 1.02x faster                                                         |
| regex_dna      | 247 ms                                                       | 244 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.03 sec: 1.21x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 93.7 ms: 1.10x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 198 us: 1.10x faster                                                         |
| xml_etree_parse      | 150 ms                                                       | 137 ms: 1.10x faster                                                         |
| xml_etree_generate   | 86.5 ms                                                      | 82.5 ms: 1.05x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 58.3 ms: 1.05x faster                                                        |
| json_loads           | 24.7 us                                                      | 25.2 us: 1.02x slower                                                        |
| pickle_pure_python   | 323 us                                                       | 340 us: 1.05x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.04 ms: 1.01x slower                                                        |
| python_startup         | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.61 ms: 1.08x faster                                                        |
| django_template | 36.4 ms                                                      | 38.5 ms: 1.06x slower                                                        |
| genshi_text     | 26.2 ms                                                      | 28.5 ms: 1.09x slower                                                        |
| genshi_xml      | 57.1 ms                                                      | 63.4 ms: 1.11x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 333 ms: 1.40x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 646 ms: 1.29x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 30.1 us: 1.28x faster                                                        |
| deepcopy                   | 392 us                                                       | 306 us: 1.28x faster                                                         |
| async_tree_io              | 843 ms                                                       | 661 ms: 1.28x faster                                                         |
| async_tree_none            | 376 ms                                                       | 297 ms: 1.27x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 274 ms: 1.27x faster                                                         |
| scimark_sor                | 123 ms                                                       | 98.6 ms: 1.25x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 366 ms: 1.24x faster                                                         |
| tomli_loads                | 2.46 sec                                                     | 2.03 sec: 1.21x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 3.00 us: 1.18x faster                                                        |
| pyflate                    | 503 ms                                                       | 432 ms: 1.17x faster                                                         |
| go                         | 162 ms                                                       | 139 ms: 1.17x faster                                                         |
| richards                   | 52.9 ms                                                      | 46.0 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 508 ms: 1.15x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 527 ms: 1.15x faster                                                         |
| regex_effbot               | 3.67 ms                                                      | 3.23 ms: 1.14x faster                                                        |
| richards_super             | 59.6 ms                                                      | 52.8 ms: 1.13x faster                                                        |
| float                      | 81.3 ms                                                      | 73.0 ms: 1.11x faster                                                        |
| json                       | 5.69 ms                                                      | 5.11 ms: 1.11x faster                                                        |
| telco                      | 8.79 ms                                                      | 7.90 ms: 1.11x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 93.7 ms: 1.10x faster                                                        |
| unpickle_pure_python       | 217 us                                                       | 198 us: 1.10x faster                                                         |
| xml_etree_parse            | 150 ms                                                       | 137 ms: 1.10x faster                                                         |
| scimark_fft                | 328 ms                                                       | 299 ms: 1.10x faster                                                         |
| pathlib                    | 17.5 ms                                                      | 16.2 ms: 1.08x faster                                                        |
| pprint_safe_repr           | 843 ms                                                       | 778 ms: 1.08x faster                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 4.70 sec: 1.08x faster                                                       |
| mako                       | 10.4 ms                                                      | 9.61 ms: 1.08x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.61 sec: 1.07x faster                                                       |
| connected_components       | 432 ms                                                       | 406 ms: 1.06x faster                                                         |
| k_core                     | 2.17 sec                                                     | 2.04 sec: 1.06x faster                                                       |
| scimark_monte_carlo        | 66.1 ms                                                      | 62.5 ms: 1.06x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 69.5 ms: 1.06x faster                                                        |
| regex_v8                   | 26.1 ms                                                      | 24.9 ms: 1.05x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 82.5 ms: 1.05x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 92.5 ms: 1.05x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 58.3 ms: 1.05x faster                                                        |
| shortest_path              | 460 ms                                                       | 441 ms: 1.04x faster                                                         |
| scimark_lu                 | 98.7 ms                                                      | 94.6 ms: 1.04x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 3.30 ms: 1.04x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.82 us: 1.03x faster                                                        |
| regex_compile              | 143 ms                                                       | 139 ms: 1.02x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.64 ms: 1.02x faster                                                        |
| regex_dna                  | 247 ms                                                       | 244 ms: 1.01x faster                                                         |
| sqlalchemy_declarative     | 148 ms                                                       | 147 ms: 1.01x faster                                                         |
| sqlalchemy_imperative      | 18.3 ms                                                      | 18.2 ms: 1.01x faster                                                        |
| thrift                     | 901 us                                                       | 896 us: 1.01x faster                                                         |
| coverage                   | 80.0 ms                                                      | 79.6 ms: 1.00x faster                                                        |
| pidigits                   | 252 ms                                                       | 253 ms: 1.00x slower                                                         |
| sqlglot_parse              | 1.40 ms                                                      | 1.41 ms: 1.01x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 9.04 ms: 1.01x slower                                                        |
| python_startup             | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.83 ms: 1.01x slower                                                        |
| logging_simple             | 6.39 us                                                      | 6.49 us: 1.01x slower                                                        |
| sqlglot_transpile          | 1.79 ms                                                      | 1.82 ms: 1.02x slower                                                        |
| json_loads                 | 24.7 us                                                      | 25.2 us: 1.02x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 75.0 ms: 1.02x slower                                                        |
| mdp                        | 2.54 sec                                                     | 2.60 sec: 1.02x slower                                                       |
| pycparser                  | 1.24 sec                                                     | 1.28 sec: 1.03x slower                                                       |
| sympy_integrate            | 23.6 ms                                                      | 24.2 ms: 1.03x slower                                                        |
| meteor_contest             | 130 ms                                                       | 134 ms: 1.03x slower                                                         |
| sympy_expand               | 509 ms                                                       | 526 ms: 1.03x slower                                                         |
| sphinx                     | 1.12 sec                                                     | 1.16 sec: 1.03x slower                                                       |
| sympy_str                  | 298 ms                                                       | 308 ms: 1.03x slower                                                         |
| nbody                      | 89.3 ms                                                      | 92.6 ms: 1.04x slower                                                        |
| logging_silent             | 97.9 ns                                                      | 101 ns: 1.04x slower                                                         |
| sympy_sum                  | 155 ms                                                       | 161 ms: 1.04x slower                                                         |
| logging_format             | 6.94 us                                                      | 7.24 us: 1.04x slower                                                        |
| fannkuch                   | 363 ms                                                       | 379 ms: 1.04x slower                                                         |
| sqlglot_normalize          | 119 ms                                                       | 126 ms: 1.05x slower                                                         |
| typing_runtime_protocols   | 169 us                                                       | 178 us: 1.05x slower                                                         |
| pickle_pure_python         | 323 us                                                       | 340 us: 1.05x slower                                                         |
| sqlglot_optimize           | 59.3 ms                                                      | 62.5 ms: 1.05x slower                                                        |
| docutils                   | 2.83 sec                                                     | 2.98 sec: 1.06x slower                                                       |
| django_template            | 36.4 ms                                                      | 38.5 ms: 1.06x slower                                                        |
| bench_thread_pool          | 942 us                                                       | 1.01 ms: 1.07x slower                                                        |
| genshi_text                | 26.2 ms                                                      | 28.5 ms: 1.09x slower                                                        |
| nqueens                    | 90.7 ms                                                      | 100.0 ms: 1.10x slower                                                       |
| hexiom                     | 6.55 ms                                                      | 7.25 ms: 1.11x slower                                                        |
| genshi_xml                 | 57.1 ms                                                      | 63.4 ms: 1.11x slower                                                        |
| chaos                      | 60.2 ms                                                      | 67.5 ms: 1.12x slower                                                        |
| many_optionals             | 930 us                                                       | 1.06 ms: 1.14x slower                                                        |
| comprehensions             | 17.0 us                                                      | 19.4 us: 1.14x slower                                                        |
| generators                 | 33.6 ms                                                      | 40.6 ms: 1.21x slower                                                        |
| raytrace                   | 273 ms                                                       | 329 ms: 1.21x slower                                                         |
| subparsers                 | 17.5 ms                                                      | 23.1 ms: 1.32x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.30 ms: 1.33x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.15 sec: 224.22x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                 |

Benchmark hidden because not significant (7): pylint, asyncio_websockets, djangocms, 2to3, async_generators, dulwich_log, json_dumps
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: mypy2

- Geometric mean (including insignificant results): 1.029x faster

# HPT report

- Reliability score: 97.54% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x