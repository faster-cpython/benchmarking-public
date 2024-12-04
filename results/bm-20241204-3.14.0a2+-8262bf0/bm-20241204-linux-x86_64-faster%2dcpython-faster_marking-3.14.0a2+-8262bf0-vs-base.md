# Results vs. base

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: 8262bf0
- commit date: 2024-12-04
- overall geometric mean: 1.000x slower
- HPT reliability: 64.28%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 255 ms: 1.00x slower                                                       |
| docutils       | 2.60 sec                                                               | 2.58 sec: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io              | 633 ms                                                                 | 610 ms: 1.04x faster                                                       |
| async_generators           | 429 ms                                                                 | 423 ms: 1.01x faster                                                       |
| coroutines                 | 23.5 ms                                                                | 23.7 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed_tg | 488 ms                                                                 | 498 ms: 1.02x slower                                                       |
| async_tree_none_tg         | 252 ms                                                                 | 268 ms: 1.06x slower                                                       |
| async_tree_memoization_tg  | 315 ms                                                                 | 336 ms: 1.07x slower                                                       |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (5): async_tree_io_tg, async_tree_memoization, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 187 ms: 1.00x slower                                                       |
| nbody          | 94.0 ms                                                                | 96.3 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.45 ms                                                                | 3.39 ms: 1.02x faster                                                      |
| regex_compile  | 128 ms                                                                 | 129 ms: 1.01x slower                                                       |
| regex_v8       | 25.2 ms                                                                | 25.9 ms: 1.03x slower                                                      |
| regex_dna      | 213 ms                                                                 | 219 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 27.0 us                                                                | 26.3 us: 1.02x faster                                                      |
| tomli_loads          | 2.11 sec                                                               | 2.08 sec: 1.02x faster                                                     |
| json_dumps           | 11.6 ms                                                                | 11.5 ms: 1.01x faster                                                      |
| unpickle_pure_python | 219 us                                                                 | 217 us: 1.01x faster                                                       |
| pickle_pure_python   | 328 us                                                                 | 325 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 96.9 ms                                                                | 98.1 ms: 1.01x slower                                                      |
| xml_etree_process    | 59.0 ms                                                                | 60.9 ms: 1.03x slower                                                      |
| xml_etree_parse      | 139 ms                                                                 | 145 ms: 1.04x slower                                                       |
| xml_etree_generate   | 83.8 ms                                                                | 87.5 ms: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                                | 12.7 ms: 1.00x faster                                                      |
| python_startup_no_site | 7.02 ms                                                                | 7.03 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 49.6 ms                                                                | 49.8 ms: 1.00x slower                                                      |
| django_template | 32.2 ms                                                                | 32.6 ms: 1.01x slower                                                      |
| mako            | 11.2 ms                                                                | 11.3 ms: 1.01x slower                                                      |
| genshi_text     | 22.4 ms                                                                | 22.9 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-8262bf0 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| create_gc_cycles           | 2.47 ms                                                                | 2.23 ms: 1.10x faster                                                      |
| gc_traversal               | 4.79 ms                                                                | 4.45 ms: 1.08x faster                                                      |
| pylint                     | 278 ms                                                                 | 265 ms: 1.05x faster                                                       |
| async_tree_io              | 633 ms                                                                 | 610 ms: 1.04x faster                                                       |
| k_core                     | 2.29 sec                                                               | 2.21 sec: 1.04x faster                                                     |
| bench_mp_pool              | 81.1 ms                                                                | 78.4 ms: 1.04x faster                                                      |
| json                       | 5.00 ms                                                                | 4.85 ms: 1.03x faster                                                      |
| json_loads                 | 27.0 us                                                                | 26.3 us: 1.02x faster                                                      |
| comprehensions             | 17.0 us                                                                | 16.7 us: 1.02x faster                                                      |
| pprint_pformat             | 1.52 sec                                                               | 1.49 sec: 1.02x faster                                                     |
| regex_effbot               | 3.45 ms                                                                | 3.39 ms: 1.02x faster                                                      |
| pycparser                  | 1.13 sec                                                               | 1.11 sec: 1.02x faster                                                     |
| mdp                        | 2.55 sec                                                               | 2.51 sec: 1.02x faster                                                     |
| tomli_loads                | 2.11 sec                                                               | 2.08 sec: 1.02x faster                                                     |
| go                         | 119 ms                                                                 | 117 ms: 1.01x faster                                                       |
| deltablue                  | 3.27 ms                                                                | 3.22 ms: 1.01x faster                                                      |
| richards                   | 47.3 ms                                                                | 46.6 ms: 1.01x faster                                                      |
| async_generators           | 429 ms                                                                 | 423 ms: 1.01x faster                                                       |
| pprint_safe_repr           | 744 ms                                                                 | 735 ms: 1.01x faster                                                       |
| logging_format             | 6.17 us                                                                | 6.10 us: 1.01x faster                                                      |
| fannkuch                   | 406 ms                                                                 | 402 ms: 1.01x faster                                                       |
| json_dumps                 | 11.6 ms                                                                | 11.5 ms: 1.01x faster                                                      |
| unpickle_pure_python       | 219 us                                                                 | 217 us: 1.01x faster                                                       |
| scimark_sor                | 127 ms                                                                 | 126 ms: 1.01x faster                                                       |
| richards_super             | 53.4 ms                                                                | 52.9 ms: 1.01x faster                                                      |
| pickle_pure_python         | 328 us                                                                 | 325 us: 1.01x faster                                                       |
| docutils                   | 2.60 sec                                                               | 2.58 sec: 1.01x faster                                                     |
| crypto_pyaes               | 72.3 ms                                                                | 72.0 ms: 1.00x faster                                                      |
| pyflate                    | 468 ms                                                                 | 466 ms: 1.00x faster                                                       |
| raytrace                   | 272 ms                                                                 | 272 ms: 1.00x faster                                                       |
| python_startup             | 12.7 ms                                                                | 12.7 ms: 1.00x faster                                                      |
| python_startup_no_site     | 7.02 ms                                                                | 7.03 ms: 1.00x slower                                                      |
| pidigits                   | 186 ms                                                                 | 187 ms: 1.00x slower                                                       |
| 2to3                       | 254 ms                                                                 | 255 ms: 1.00x slower                                                       |
| meteor_contest             | 107 ms                                                                 | 108 ms: 1.00x slower                                                       |
| genshi_xml                 | 49.6 ms                                                                | 49.8 ms: 1.00x slower                                                      |
| sqlglot_normalize          | 107 ms                                                                 | 108 ms: 1.01x slower                                                       |
| deepcopy_reduce            | 2.72 us                                                                | 2.73 us: 1.01x slower                                                      |
| spectral_norm              | 111 ms                                                                 | 112 ms: 1.01x slower                                                       |
| regex_compile              | 128 ms                                                                 | 129 ms: 1.01x slower                                                       |
| hexiom                     | 6.23 ms                                                                | 6.28 ms: 1.01x slower                                                      |
| subparsers                 | 20.7 ms                                                                | 20.9 ms: 1.01x slower                                                      |
| sqlglot_parse              | 1.29 ms                                                                | 1.30 ms: 1.01x slower                                                      |
| django_template            | 32.2 ms                                                                | 32.6 ms: 1.01x slower                                                      |
| coroutines                 | 23.5 ms                                                                | 23.7 ms: 1.01x slower                                                      |
| mako                       | 11.2 ms                                                                | 11.3 ms: 1.01x slower                                                      |
| coverage                   | 83.1 ms                                                                | 84.2 ms: 1.01x slower                                                      |
| xml_etree_iterparse        | 96.9 ms                                                                | 98.1 ms: 1.01x slower                                                      |
| many_optionals             | 939 us                                                                 | 952 us: 1.01x slower                                                       |
| generators                 | 28.0 ms                                                                | 28.5 ms: 1.02x slower                                                      |
| scimark_lu                 | 115 ms                                                                 | 117 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 488 ms                                                                 | 498 ms: 1.02x slower                                                       |
| genshi_text                | 22.4 ms                                                                | 22.9 ms: 1.02x slower                                                      |
| scimark_fft                | 364 ms                                                                 | 372 ms: 1.02x slower                                                       |
| nbody                      | 94.0 ms                                                                | 96.3 ms: 1.02x slower                                                      |
| regex_v8                   | 25.2 ms                                                                | 25.9 ms: 1.03x slower                                                      |
| regex_dna                  | 213 ms                                                                 | 219 ms: 1.03x slower                                                       |
| xml_etree_process          | 59.0 ms                                                                | 60.9 ms: 1.03x slower                                                      |
| xml_etree_parse            | 139 ms                                                                 | 145 ms: 1.04x slower                                                       |
| xml_etree_generate         | 83.8 ms                                                                | 87.5 ms: 1.05x slower                                                      |
| async_tree_none_tg         | 252 ms                                                                 | 268 ms: 1.06x slower                                                       |
| async_tree_memoization_tg  | 315 ms                                                                 | 336 ms: 1.07x slower                                                       |
| scimark_sparse_mat_mult    | 4.84 ms                                                                | 5.17 ms: 1.07x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (34): async_tree_io_tg, connected_components, async_tree_memoization, logging_silent, sphinx, float, sympy_sum, shortest_path, sqlalchemy_declarative, sqlglot_optimize, bpe_tokeniser, bench_thread_pool, chaos, sympy_str, thrift, async_tree_cpu_io_mixed, sympy_integrate, deepcopy, logging_simple, scimark_monte_carlo, nqueens, html5lib, dulwich_log, sympy_expand, sqlglot_transpile, deepcopy_memo, typing_runtime_protocols, telco, asyncio_websockets, sqlite_synth, sqlalchemy_imperative, pathlib, async_tree_none, djangocms

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 64.28% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x