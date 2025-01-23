# Results vs. 3.13.0

- fork: mdboom
- ref: aa_test_2025_2
- machine: linux-x86_64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.062x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 281 ms: 1.04x faster                                                   |
| docutils       | 2.83 sec                                                     | 2.87 sec: 1.02x slower                                                 |
| html5lib       | 73.5 ms                                                      | 67.1 ms: 1.10x faster                                                  |
| sphinx         | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                 |
| Geometric mean | (ref)                                                        | 1.03x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 327 ms: 1.42x faster                                                   |
| async_tree_none            | 376 ms                                                       | 275 ms: 1.37x faster                                                   |
| async_tree_io              | 843 ms                                                       | 624 ms: 1.35x faster                                                   |
| async_tree_io_tg           | 831 ms                                                       | 622 ms: 1.34x faster                                                   |
| async_tree_memoization     | 453 ms                                                       | 341 ms: 1.33x faster                                                   |
| async_tree_none_tg         | 346 ms                                                       | 267 ms: 1.30x faster                                                   |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 505 ms: 1.20x faster                                                   |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 499 ms: 1.16x faster                                                   |
| async_generators           | 457 ms                                                       | 403 ms: 1.13x faster                                                   |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                  |
| Geometric mean             | (ref)                                                        | 1.23x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 69.6 ms: 1.17x faster                                                  |
| nbody          | 89.3 ms                                                      | 87.8 ms: 1.02x faster                                                  |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.06x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.04 ms: 1.21x faster                                                  |
| regex_compile  | 143 ms                                                       | 135 ms: 1.06x faster                                                   |
| regex_dna      | 247 ms                                                       | 240 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                        | 1.07x faster                                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.07 sec: 1.19x faster                                                 |
| xml_etree_parse      | 150 ms                                                       | 134 ms: 1.12x faster                                                   |
| xml_etree_iterparse  | 103 ms                                                       | 95.3 ms: 1.08x faster                                                  |
| xml_etree_generate   | 86.5 ms                                                      | 83.2 ms: 1.04x faster                                                  |
| unpickle_pure_python | 217 us                                                       | 219 us: 1.01x slower                                                   |
| json_loads           | 24.7 us                                                      | 25.3 us: 1.03x slower                                                  |
| pickle_pure_python   | 323 us                                                       | 335 us: 1.04x slower                                                   |
| json_dumps           | 11.1 ms                                                      | 11.7 ms: 1.05x slower                                                  |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 8.98 ms: 1.00x slower                                                  |
| python_startup         | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 24.1 ms: 1.09x faster                                                  |
| genshi_xml      | 57.1 ms                                                      | 54.5 ms: 1.05x faster                                                  |
| django_template | 36.4 ms                                                      | 36.0 ms: 1.01x faster                                                  |
| mako            | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                  |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 327 ms: 1.42x faster                                                   |
| deepcopy                   | 392 us                                                       | 282 us: 1.39x faster                                                   |
| async_tree_none            | 376 ms                                                       | 275 ms: 1.37x faster                                                   |
| async_tree_io              | 843 ms                                                       | 624 ms: 1.35x faster                                                   |
| async_tree_io_tg           | 831 ms                                                       | 622 ms: 1.34x faster                                                   |
| async_tree_memoization     | 453 ms                                                       | 341 ms: 1.33x faster                                                   |
| async_tree_none_tg         | 346 ms                                                       | 267 ms: 1.30x faster                                                   |
| deepcopy_memo              | 38.6 us                                                      | 29.9 us: 1.29x faster                                                  |
| go                         | 162 ms                                                       | 127 ms: 1.27x faster                                                   |
| deepcopy_reduce            | 3.54 us                                                      | 2.92 us: 1.21x faster                                                  |
| regex_effbot               | 3.67 ms                                                      | 3.04 ms: 1.21x faster                                                  |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 505 ms: 1.20x faster                                                   |
| generators                 | 33.6 ms                                                      | 28.2 ms: 1.19x faster                                                  |
| tomli_loads                | 2.46 sec                                                     | 2.07 sec: 1.19x faster                                                 |
| float                      | 81.3 ms                                                      | 69.6 ms: 1.17x faster                                                  |
| pyflate                    | 503 ms                                                       | 431 ms: 1.17x faster                                                   |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 499 ms: 1.16x faster                                                   |
| scimark_sor                | 123 ms                                                       | 108 ms: 1.14x faster                                                   |
| async_generators           | 457 ms                                                       | 403 ms: 1.13x faster                                                   |
| richards                   | 52.9 ms                                                      | 46.7 ms: 1.13x faster                                                  |
| richards_super             | 59.6 ms                                                      | 53.1 ms: 1.12x faster                                                  |
| spectral_norm              | 97.0 ms                                                      | 86.6 ms: 1.12x faster                                                  |
| xml_etree_parse            | 150 ms                                                       | 134 ms: 1.12x faster                                                   |
| pylint                     | 347 ms                                                       | 315 ms: 1.10x faster                                                   |
| pathlib                    | 17.5 ms                                                      | 15.9 ms: 1.10x faster                                                  |
| html5lib                   | 73.5 ms                                                      | 67.1 ms: 1.10x faster                                                  |
| telco                      | 8.79 ms                                                      | 8.06 ms: 1.09x faster                                                  |
| scimark_fft                | 328 ms                                                       | 301 ms: 1.09x faster                                                   |
| genshi_text                | 26.2 ms                                                      | 24.1 ms: 1.09x faster                                                  |
| hexiom                     | 6.55 ms                                                      | 6.03 ms: 1.09x faster                                                  |
| bpe_tokeniser              | 5.09 sec                                                     | 4.69 sec: 1.08x faster                                                 |
| xml_etree_iterparse        | 103 ms                                                       | 95.3 ms: 1.08x faster                                                  |
| json                       | 5.69 ms                                                      | 5.28 ms: 1.08x faster                                                  |
| pprint_pformat             | 1.72 sec                                                     | 1.60 sec: 1.07x faster                                                 |
| pprint_safe_repr           | 843 ms                                                       | 788 ms: 1.07x faster                                                   |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.48 ms: 1.07x faster                                                  |
| sqlglot_parse              | 1.40 ms                                                      | 1.32 ms: 1.06x faster                                                  |
| regex_compile              | 143 ms                                                       | 135 ms: 1.06x faster                                                   |
| sqlglot_transpile          | 1.79 ms                                                      | 1.70 ms: 1.05x faster                                                  |
| genshi_xml                 | 57.1 ms                                                      | 54.5 ms: 1.05x faster                                                  |
| 2to3                       | 293 ms                                                       | 281 ms: 1.04x faster                                                   |
| scimark_lu                 | 98.7 ms                                                      | 94.7 ms: 1.04x faster                                                  |
| xml_etree_generate         | 86.5 ms                                                      | 83.2 ms: 1.04x faster                                                  |
| k_core                     | 2.17 sec                                                     | 2.09 sec: 1.04x faster                                                 |
| shortest_path              | 460 ms                                                       | 445 ms: 1.03x faster                                                   |
| connected_components       | 432 ms                                                       | 419 ms: 1.03x faster                                                   |
| thrift                     | 901 us                                                       | 872 us: 1.03x faster                                                   |
| deltablue                  | 3.42 ms                                                      | 3.31 ms: 1.03x faster                                                  |
| sympy_expand               | 509 ms                                                       | 494 ms: 1.03x faster                                                   |
| sqlalchemy_declarative     | 148 ms                                                       | 144 ms: 1.03x faster                                                   |
| regex_dna                  | 247 ms                                                       | 240 ms: 1.03x faster                                                   |
| sqlglot_normalize          | 119 ms                                                       | 116 ms: 1.03x faster                                                   |
| sympy_str                  | 298 ms                                                       | 290 ms: 1.03x faster                                                   |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                  |
| sqlglot_optimize           | 59.3 ms                                                      | 57.7 ms: 1.03x faster                                                  |
| chaos                      | 60.2 ms                                                      | 58.6 ms: 1.03x faster                                                  |
| mdp                        | 2.54 sec                                                     | 2.48 sec: 1.03x faster                                                 |
| sympy_sum                  | 155 ms                                                       | 151 ms: 1.02x faster                                                   |
| scimark_monte_carlo        | 66.1 ms                                                      | 64.7 ms: 1.02x faster                                                  |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.9 ms: 1.02x faster                                                  |
| pycparser                  | 1.24 sec                                                     | 1.22 sec: 1.02x faster                                                 |
| nqueens                    | 90.7 ms                                                      | 88.8 ms: 1.02x faster                                                  |
| sympy_integrate            | 23.6 ms                                                      | 23.1 ms: 1.02x faster                                                  |
| dulwich_log                | 68.2 ms                                                      | 67.0 ms: 1.02x faster                                                  |
| nbody                      | 89.3 ms                                                      | 87.8 ms: 1.02x faster                                                  |
| sqlite_synth               | 2.91 us                                                      | 2.85 us: 1.02x faster                                                  |
| coverage                   | 80.0 ms                                                      | 79.1 ms: 1.01x faster                                                  |
| logging_silent             | 97.9 ns                                                      | 96.8 ns: 1.01x faster                                                  |
| sphinx                     | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                 |
| django_template            | 36.4 ms                                                      | 36.0 ms: 1.01x faster                                                  |
| meteor_contest             | 130 ms                                                       | 128 ms: 1.01x faster                                                   |
| fannkuch                   | 363 ms                                                       | 362 ms: 1.00x faster                                                   |
| python_startup_no_site     | 8.96 ms                                                      | 8.98 ms: 1.00x slower                                                  |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                  |
| unpickle_pure_python       | 217 us                                                       | 219 us: 1.01x slower                                                   |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                   |
| docutils                   | 2.83 sec                                                     | 2.87 sec: 1.02x slower                                                 |
| comprehensions             | 17.0 us                                                      | 17.5 us: 1.03x slower                                                  |
| logging_simple             | 6.39 us                                                      | 6.56 us: 1.03x slower                                                  |
| json_loads                 | 24.7 us                                                      | 25.3 us: 1.03x slower                                                  |
| pickle_pure_python         | 323 us                                                       | 335 us: 1.04x slower                                                   |
| logging_format             | 6.94 us                                                      | 7.27 us: 1.05x slower                                                  |
| typing_runtime_protocols   | 169 us                                                       | 178 us: 1.05x slower                                                   |
| mako                       | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                  |
| json_dumps                 | 11.1 ms                                                      | 11.7 ms: 1.05x slower                                                  |
| create_gc_cycles           | 2.68 ms                                                      | 2.83 ms: 1.06x slower                                                  |
| many_optionals             | 930 us                                                       | 1.02 ms: 1.10x slower                                                  |
| subparsers                 | 17.5 ms                                                      | 22.8 ms: 1.31x slower                                                  |
| gc_traversal               | 4.74 ms                                                      | 6.47 ms: 1.36x slower                                                  |
| bench_mp_pool              | 5.12 ms                                                      | 1.70 sec: 331.26x slower                                               |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                           |

Benchmark hidden because not significant (6): asyncio_websockets, xml_etree_process, crypto_pyaes, raytrace, bench_thread_pool, regex_v8
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.062x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.02x