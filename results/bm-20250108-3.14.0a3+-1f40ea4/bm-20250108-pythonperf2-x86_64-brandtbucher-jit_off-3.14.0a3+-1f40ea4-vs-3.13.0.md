# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_off
- machine: linux-x86_64
- commit hash: 1f40ea4
- commit date: 2025-01-08
- overall geometric mean: 1.063x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 282 ms: 1.04x faster                                                  |
| docutils       | 2.83 sec                                                     | 2.90 sec: 1.03x slower                                                |
| html5lib       | 73.5 ms                                                      | 67.5 ms: 1.09x faster                                                 |
| sphinx         | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                |
| Geometric mean | (ref)                                                        | 1.03x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 327 ms: 1.42x faster                                                  |
| async_tree_io_tg           | 831 ms                                                       | 623 ms: 1.33x faster                                                  |
| async_tree_none            | 376 ms                                                       | 282 ms: 1.33x faster                                                  |
| async_tree_io              | 843 ms                                                       | 633 ms: 1.33x faster                                                  |
| async_tree_memoization     | 453 ms                                                       | 347 ms: 1.30x faster                                                  |
| async_tree_none_tg         | 346 ms                                                       | 268 ms: 1.29x faster                                                  |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 513 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 496 ms: 1.17x faster                                                  |
| async_generators           | 457 ms                                                       | 436 ms: 1.05x faster                                                  |
| coroutines                 | 21.6 ms                                                      | 20.8 ms: 1.04x faster                                                 |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                                  |
| Geometric mean             | (ref)                                                        | 1.22x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 73.0 ms: 1.11x faster                                                 |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                        | 1.03x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.15 ms: 1.17x faster                                                 |
| regex_dna      | 247 ms                                                       | 233 ms: 1.06x faster                                                  |
| regex_compile  | 143 ms                                                       | 135 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                        | 1.07x faster                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.05 sec: 1.20x faster                                                |
| xml_etree_parse      | 150 ms                                                       | 135 ms: 1.11x faster                                                  |
| xml_etree_iterparse  | 103 ms                                                       | 96.4 ms: 1.07x faster                                                 |
| xml_etree_process    | 61.2 ms                                                      | 58.0 ms: 1.05x faster                                                 |
| xml_etree_generate   | 86.5 ms                                                      | 82.2 ms: 1.05x faster                                                 |
| unpickle_pure_python | 217 us                                                       | 207 us: 1.05x faster                                                  |
| json_loads           | 24.7 us                                                      | 24.0 us: 1.03x faster                                                 |
| pickle_pure_python   | 323 us                                                       | 328 us: 1.02x slower                                                  |
| json_dumps           | 11.1 ms                                                      | 11.5 ms: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                        | 1.06x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.03 ms: 1.01x slower                                                 |
| python_startup         | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 57.1 ms                                                      | 51.8 ms: 1.10x faster                                                 |
| genshi_text     | 26.2 ms                                                      | 23.9 ms: 1.10x faster                                                 |
| django_template | 36.4 ms                                                      | 35.7 ms: 1.02x faster                                                 |
| mako            | 10.4 ms                                                      | 11.0 ms: 1.06x slower                                                 |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250108-pythonperf2-x86_64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 327 ms: 1.42x faster                                                  |
| deepcopy                   | 392 us                                                       | 283 us: 1.39x faster                                                  |
| async_tree_io_tg           | 831 ms                                                       | 623 ms: 1.33x faster                                                  |
| async_tree_none            | 376 ms                                                       | 282 ms: 1.33x faster                                                  |
| async_tree_io              | 843 ms                                                       | 633 ms: 1.33x faster                                                  |
| deepcopy_memo              | 38.6 us                                                      | 29.4 us: 1.31x faster                                                 |
| async_tree_memoization     | 453 ms                                                       | 347 ms: 1.30x faster                                                  |
| async_tree_none_tg         | 346 ms                                                       | 268 ms: 1.29x faster                                                  |
| go                         | 162 ms                                                       | 128 ms: 1.27x faster                                                  |
| tomli_loads                | 2.46 sec                                                     | 2.05 sec: 1.20x faster                                                |
| deepcopy_reduce            | 3.54 us                                                      | 2.96 us: 1.20x faster                                                 |
| generators                 | 33.6 ms                                                      | 28.5 ms: 1.18x faster                                                 |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 513 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 496 ms: 1.17x faster                                                  |
| regex_effbot               | 3.67 ms                                                      | 3.15 ms: 1.17x faster                                                 |
| telco                      | 8.79 ms                                                      | 7.68 ms: 1.14x faster                                                 |
| richards                   | 52.9 ms                                                      | 46.4 ms: 1.14x faster                                                 |
| richards_super             | 59.6 ms                                                      | 53.1 ms: 1.12x faster                                                 |
| scimark_sor                | 123 ms                                                       | 110 ms: 1.12x faster                                                  |
| float                      | 81.3 ms                                                      | 73.0 ms: 1.11x faster                                                 |
| json                       | 5.69 ms                                                      | 5.11 ms: 1.11x faster                                                 |
| xml_etree_parse            | 150 ms                                                       | 135 ms: 1.11x faster                                                  |
| spectral_norm              | 97.0 ms                                                      | 87.5 ms: 1.11x faster                                                 |
| pyflate                    | 503 ms                                                       | 456 ms: 1.10x faster                                                  |
| genshi_xml                 | 57.1 ms                                                      | 51.8 ms: 1.10x faster                                                 |
| pprint_pformat             | 1.72 sec                                                     | 1.57 sec: 1.10x faster                                                |
| genshi_text                | 26.2 ms                                                      | 23.9 ms: 1.10x faster                                                 |
| pprint_safe_repr           | 843 ms                                                       | 770 ms: 1.09x faster                                                  |
| pathlib                    | 17.5 ms                                                      | 16.1 ms: 1.09x faster                                                 |
| html5lib                   | 73.5 ms                                                      | 67.5 ms: 1.09x faster                                                 |
| pylint                     | 347 ms                                                       | 319 ms: 1.09x faster                                                  |
| bpe_tokeniser              | 5.09 sec                                                     | 4.69 sec: 1.09x faster                                                |
| scimark_fft                | 328 ms                                                       | 304 ms: 1.08x faster                                                  |
| hexiom                     | 6.55 ms                                                      | 6.09 ms: 1.08x faster                                                 |
| xml_etree_iterparse        | 103 ms                                                       | 96.4 ms: 1.07x faster                                                 |
| scimark_monte_carlo        | 66.1 ms                                                      | 62.4 ms: 1.06x faster                                                 |
| regex_dna                  | 247 ms                                                       | 233 ms: 1.06x faster                                                  |
| sqlglot_parse              | 1.40 ms                                                      | 1.33 ms: 1.05x faster                                                 |
| xml_etree_process          | 61.2 ms                                                      | 58.0 ms: 1.05x faster                                                 |
| regex_compile              | 143 ms                                                       | 135 ms: 1.05x faster                                                  |
| xml_etree_generate         | 86.5 ms                                                      | 82.2 ms: 1.05x faster                                                 |
| unpickle_pure_python       | 217 us                                                       | 207 us: 1.05x faster                                                  |
| sqlglot_normalize          | 119 ms                                                       | 114 ms: 1.05x faster                                                  |
| async_generators           | 457 ms                                                       | 436 ms: 1.05x faster                                                  |
| scimark_lu                 | 98.7 ms                                                      | 94.2 ms: 1.05x faster                                                 |
| connected_components       | 432 ms                                                       | 415 ms: 1.04x faster                                                  |
| sqlglot_transpile          | 1.79 ms                                                      | 1.72 ms: 1.04x faster                                                 |
| thrift                     | 901 us                                                       | 866 us: 1.04x faster                                                  |
| meteor_contest             | 130 ms                                                       | 125 ms: 1.04x faster                                                  |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.59 ms: 1.04x faster                                                 |
| 2to3                       | 293 ms                                                       | 282 ms: 1.04x faster                                                  |
| coroutines                 | 21.6 ms                                                      | 20.8 ms: 1.04x faster                                                 |
| sqlalchemy_declarative     | 148 ms                                                       | 143 ms: 1.04x faster                                                  |
| k_core                     | 2.17 sec                                                     | 2.10 sec: 1.03x faster                                                |
| mdp                        | 2.54 sec                                                     | 2.47 sec: 1.03x faster                                                |
| coverage                   | 80.0 ms                                                      | 77.7 ms: 1.03x faster                                                 |
| shortest_path              | 460 ms                                                       | 447 ms: 1.03x faster                                                  |
| sqlglot_optimize           | 59.3 ms                                                      | 57.6 ms: 1.03x faster                                                 |
| json_loads                 | 24.7 us                                                      | 24.0 us: 1.03x faster                                                 |
| dulwich_log                | 68.2 ms                                                      | 66.7 ms: 1.02x faster                                                 |
| django_template            | 36.4 ms                                                      | 35.7 ms: 1.02x faster                                                 |
| sqlite_synth               | 2.91 us                                                      | 2.85 us: 1.02x faster                                                 |
| sympy_sum                  | 155 ms                                                       | 152 ms: 1.02x faster                                                  |
| sympy_str                  | 298 ms                                                       | 293 ms: 1.02x faster                                                  |
| sqlalchemy_imperative      | 18.3 ms                                                      | 18.0 ms: 1.02x faster                                                 |
| sympy_integrate            | 23.6 ms                                                      | 23.2 ms: 1.02x faster                                                 |
| fannkuch                   | 363 ms                                                       | 358 ms: 1.02x faster                                                  |
| sympy_expand               | 509 ms                                                       | 502 ms: 1.02x faster                                                  |
| sphinx                     | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                |
| pycparser                  | 1.24 sec                                                     | 1.23 sec: 1.01x faster                                                |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                                  |
| raytrace                   | 273 ms                                                       | 271 ms: 1.01x faster                                                  |
| nqueens                    | 90.7 ms                                                      | 90.1 ms: 1.01x faster                                                 |
| deltablue                  | 3.42 ms                                                      | 3.40 ms: 1.00x faster                                                 |
| python_startup_no_site     | 8.96 ms                                                      | 9.03 ms: 1.01x slower                                                 |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                  |
| python_startup             | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                 |
| pickle_pure_python         | 323 us                                                       | 328 us: 1.02x slower                                                  |
| create_gc_cycles           | 2.68 ms                                                      | 2.74 ms: 1.02x slower                                                 |
| docutils                   | 2.83 sec                                                     | 2.90 sec: 1.03x slower                                                |
| comprehensions             | 17.0 us                                                      | 17.6 us: 1.03x slower                                                 |
| json_dumps                 | 11.1 ms                                                      | 11.5 ms: 1.03x slower                                                 |
| typing_runtime_protocols   | 169 us                                                       | 175 us: 1.04x slower                                                  |
| chaos                      | 60.2 ms                                                      | 63.0 ms: 1.05x slower                                                 |
| mako                       | 10.4 ms                                                      | 11.0 ms: 1.06x slower                                                 |
| many_optionals             | 930 us                                                       | 1.03 ms: 1.11x slower                                                 |
| subparsers                 | 17.5 ms                                                      | 22.8 ms: 1.30x slower                                                 |
| gc_traversal               | 4.74 ms                                                      | 6.25 ms: 1.32x slower                                                 |
| bench_mp_pool              | 5.12 ms                                                      | 1.52 sec: 296.50x slower                                              |
| Geometric mean             | (ref)                                                        | 1.00x faster                                                          |

Benchmark hidden because not significant (7): regex_v8, bench_thread_pool, logging_simple, nbody, crypto_pyaes, logging_silent, logging_format
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.063x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.03x