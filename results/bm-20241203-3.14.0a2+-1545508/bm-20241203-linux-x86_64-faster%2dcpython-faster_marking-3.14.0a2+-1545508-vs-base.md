# Results vs. base

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: 1545508
- commit date: 2024-12-03
- overall geometric mean: 1.007x slower
- HPT reliability: 99.82%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 256 ms: 1.01x slower                                                       |
| docutils       | 2.60 sec                                                               | 2.59 sec: 1.00x faster                                                     |
| html5lib       | 63.1 ms                                                                | 64.2 ms: 1.02x slower                                                      |
| sphinx         | 1.02 sec                                                               | 1.03 sec: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 502 ms                                                                 | 510 ms: 1.02x slower                                                       |
| async_tree_memoization     | 341 ms                                                                 | 348 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 488 ms                                                                 | 502 ms: 1.03x slower                                                       |
| coroutines                 | 23.5 ms                                                                | 24.1 ms: 1.03x slower                                                      |
| async_tree_none            | 271 ms                                                                 | 284 ms: 1.05x slower                                                       |
| async_tree_io_tg           | 626 ms                                                                 | 673 ms: 1.08x slower                                                       |
| async_tree_memoization_tg  | 315 ms                                                                 | 349 ms: 1.11x slower                                                       |
| async_tree_none_tg         | 252 ms                                                                 | 283 ms: 1.12x slower                                                       |
| Geometric mean             | (ref)                                                                  | 1.04x slower                                                               |

Benchmark hidden because not significant (3): async_tree_io, async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 187 ms: 1.00x slower                                                       |
| float          | 78.0 ms                                                                | 79.1 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.45 ms                                                                | 3.36 ms: 1.03x faster                                                      |
| regex_compile  | 128 ms                                                                 | 129 ms: 1.01x slower                                                       |
| regex_v8       | 25.2 ms                                                                | 26.1 ms: 1.04x slower                                                      |
| regex_dna      | 213 ms                                                                 | 225 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 27.0 us                                                                | 26.2 us: 1.03x faster                                                      |
| json_dumps           | 11.6 ms                                                                | 11.4 ms: 1.02x faster                                                      |
| tomli_loads          | 2.11 sec                                                               | 2.08 sec: 1.02x faster                                                     |
| unpickle_pure_python | 219 us                                                                 | 217 us: 1.01x faster                                                       |
| pickle_pure_python   | 328 us                                                                 | 334 us: 1.02x slower                                                       |
| xml_etree_process    | 59.0 ms                                                                | 60.9 ms: 1.03x slower                                                      |
| xml_etree_generate   | 83.8 ms                                                                | 87.7 ms: 1.05x slower                                                      |
| xml_etree_parse      | 139 ms                                                                 | 148 ms: 1.06x slower                                                       |
| xml_etree_iterparse  | 96.9 ms                                                                | 103 ms: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                                | 12.7 ms: 1.00x slower                                                      |
| python_startup_no_site | 7.02 ms                                                                | 7.03 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 32.2 ms                                                                | 31.9 ms: 1.01x faster                                                      |
| genshi_xml      | 49.6 ms                                                                | 50.2 ms: 1.01x slower                                                      |
| genshi_text     | 22.4 ms                                                                | 22.7 ms: 1.01x slower                                                      |
| mako            | 11.2 ms                                                                | 11.4 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241203-linux-x86_64-python-7c2bd9b2266665ff4010-3.14.0a2+-7c2bd9b | bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| create_gc_cycles           | 2.47 ms                                                                | 2.24 ms: 1.10x faster                                                      |
| gc_traversal               | 4.79 ms                                                                | 4.47 ms: 1.07x faster                                                      |
| json                       | 5.00 ms                                                                | 4.79 ms: 1.04x faster                                                      |
| json_loads                 | 27.0 us                                                                | 26.2 us: 1.03x faster                                                      |
| pyflate                    | 468 ms                                                                 | 454 ms: 1.03x faster                                                       |
| regex_effbot               | 3.45 ms                                                                | 3.36 ms: 1.03x faster                                                      |
| sqlite_synth               | 2.90 us                                                                | 2.84 us: 1.02x faster                                                      |
| richards                   | 47.3 ms                                                                | 46.4 ms: 1.02x faster                                                      |
| pprint_pformat             | 1.52 sec                                                               | 1.50 sec: 1.02x faster                                                     |
| mdp                        | 2.55 sec                                                               | 2.50 sec: 1.02x faster                                                     |
| json_dumps                 | 11.6 ms                                                                | 11.4 ms: 1.02x faster                                                      |
| tomli_loads                | 2.11 sec                                                               | 2.08 sec: 1.02x faster                                                     |
| richards_super             | 53.4 ms                                                                | 52.8 ms: 1.01x faster                                                      |
| deepcopy_reduce            | 2.72 us                                                                | 2.69 us: 1.01x faster                                                      |
| scimark_lu                 | 115 ms                                                                 | 114 ms: 1.01x faster                                                       |
| pprint_safe_repr           | 744 ms                                                                 | 737 ms: 1.01x faster                                                       |
| pathlib                    | 16.5 ms                                                                | 16.3 ms: 1.01x faster                                                      |
| django_template            | 32.2 ms                                                                | 31.9 ms: 1.01x faster                                                      |
| logging_format             | 6.17 us                                                                | 6.12 us: 1.01x faster                                                      |
| unpickle_pure_python       | 219 us                                                                 | 217 us: 1.01x faster                                                       |
| deepcopy_memo              | 30.6 us                                                                | 30.4 us: 1.01x faster                                                      |
| scimark_monte_carlo        | 69.0 ms                                                                | 68.6 ms: 1.01x faster                                                      |
| meteor_contest             | 107 ms                                                                 | 107 ms: 1.00x faster                                                       |
| bench_mp_pool              | 81.1 ms                                                                | 80.8 ms: 1.00x faster                                                      |
| docutils                   | 2.60 sec                                                               | 2.59 sec: 1.00x faster                                                     |
| raytrace                   | 272 ms                                                                 | 272 ms: 1.00x faster                                                       |
| python_startup             | 12.7 ms                                                                | 12.7 ms: 1.00x slower                                                      |
| python_startup_no_site     | 7.02 ms                                                                | 7.03 ms: 1.00x slower                                                      |
| bench_thread_pool          | 850 us                                                                 | 853 us: 1.00x slower                                                       |
| pidigits                   | 186 ms                                                                 | 187 ms: 1.00x slower                                                       |
| coverage                   | 83.1 ms                                                                | 83.5 ms: 1.00x slower                                                      |
| sympy_integrate            | 19.8 ms                                                                | 19.9 ms: 1.00x slower                                                      |
| go                         | 119 ms                                                                 | 120 ms: 1.01x slower                                                       |
| 2to3                       | 254 ms                                                                 | 256 ms: 1.01x slower                                                       |
| sqlglot_parse              | 1.29 ms                                                                | 1.29 ms: 1.01x slower                                                      |
| scimark_fft                | 364 ms                                                                 | 366 ms: 1.01x slower                                                       |
| sqlalchemy_declarative     | 127 ms                                                                 | 128 ms: 1.01x slower                                                       |
| sympy_str                  | 269 ms                                                                 | 271 ms: 1.01x slower                                                       |
| subparsers                 | 20.7 ms                                                                | 20.9 ms: 1.01x slower                                                      |
| regex_compile              | 128 ms                                                                 | 129 ms: 1.01x slower                                                       |
| sqlalchemy_imperative      | 16.5 ms                                                                | 16.6 ms: 1.01x slower                                                      |
| sphinx                     | 1.02 sec                                                               | 1.03 sec: 1.01x slower                                                     |
| logging_silent             | 107 ns                                                                 | 108 ns: 1.01x slower                                                       |
| scimark_sor                | 127 ms                                                                 | 128 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 107 ms                                                                 | 108 ms: 1.01x slower                                                       |
| deltablue                  | 3.27 ms                                                                | 3.30 ms: 1.01x slower                                                      |
| genshi_xml                 | 49.6 ms                                                                | 50.2 ms: 1.01x slower                                                      |
| genshi_text                | 22.4 ms                                                                | 22.7 ms: 1.01x slower                                                      |
| bpe_tokeniser              | 4.51 sec                                                               | 4.57 sec: 1.01x slower                                                     |
| float                      | 78.0 ms                                                                | 79.1 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed    | 502 ms                                                                 | 510 ms: 1.02x slower                                                       |
| mako                       | 11.2 ms                                                                | 11.4 ms: 1.02x slower                                                      |
| many_optionals             | 939 us                                                                 | 954 us: 1.02x slower                                                       |
| html5lib                   | 63.1 ms                                                                | 64.2 ms: 1.02x slower                                                      |
| crypto_pyaes               | 72.3 ms                                                                | 73.5 ms: 1.02x slower                                                      |
| pickle_pure_python         | 328 us                                                                 | 334 us: 1.02x slower                                                       |
| generators                 | 28.0 ms                                                                | 28.5 ms: 1.02x slower                                                      |
| pycparser                  | 1.13 sec                                                               | 1.15 sec: 1.02x slower                                                     |
| async_tree_memoization     | 341 ms                                                                 | 348 ms: 1.02x slower                                                       |
| djangocms                  | 21.6 us                                                                | 22.2 us: 1.03x slower                                                      |
| async_tree_cpu_io_mixed_tg | 488 ms                                                                 | 502 ms: 1.03x slower                                                       |
| coroutines                 | 23.5 ms                                                                | 24.1 ms: 1.03x slower                                                      |
| xml_etree_process          | 59.0 ms                                                                | 60.9 ms: 1.03x slower                                                      |
| spectral_norm              | 111 ms                                                                 | 115 ms: 1.03x slower                                                       |
| nqueens                    | 80.2 ms                                                                | 82.9 ms: 1.03x slower                                                      |
| regex_v8                   | 25.2 ms                                                                | 26.1 ms: 1.04x slower                                                      |
| async_tree_none            | 271 ms                                                                 | 284 ms: 1.05x slower                                                       |
| xml_etree_generate         | 83.8 ms                                                                | 87.7 ms: 1.05x slower                                                      |
| k_core                     | 2.29 sec                                                               | 2.42 sec: 1.06x slower                                                     |
| regex_dna                  | 213 ms                                                                 | 225 ms: 1.06x slower                                                       |
| xml_etree_parse            | 139 ms                                                                 | 148 ms: 1.06x slower                                                       |
| xml_etree_iterparse        | 96.9 ms                                                                | 103 ms: 1.06x slower                                                       |
| async_tree_io_tg           | 626 ms                                                                 | 673 ms: 1.08x slower                                                       |
| async_tree_memoization_tg  | 315 ms                                                                 | 349 ms: 1.11x slower                                                       |
| async_tree_none_tg         | 252 ms                                                                 | 283 ms: 1.12x slower                                                       |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (22): pylint, connected_components, nbody, thrift, async_tree_io, deepcopy, shortest_path, dulwich_log, chaos, async_generators, comprehensions, sqlglot_transpile, hexiom, telco, fannkuch, scimark_sparse_mat_mult, typing_runtime_protocols, sympy_sum, sqlglot_optimize, asyncio_websockets, sympy_expand, logging_simple

- Geometric mean (including insignificant results): 1.007x slower

# HPT report

- Reliability score: 99.82% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.98x