# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.007x slower
- HPT reliability: 65.09%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 314 ms: 1.07x slower                                                  |
| docutils       | 2.81 sec                                                     | 3.18 sec: 1.13x slower                                                |
| html5lib       | 72.9 ms                                                      | 70.4 ms: 1.04x faster                                                 |
| sphinx         | 1.11 sec                                                     | 1.26 sec: 1.13x slower                                                |
| tornado_http   | 119 ms                                                       | 123 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                        | 1.07x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 374 ms: 1.23x faster                                                  |
| async_tree_memoization     | 447 ms                                                       | 412 ms: 1.09x faster                                                  |
| async_tree_none            | 370 ms                                                       | 341 ms: 1.09x faster                                                  |
| async_tree_none_tg         | 342 ms                                                       | 323 ms: 1.06x faster                                                  |
| asyncio_websockets         | 395 ms                                                       | 382 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 577 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 562 ms: 1.02x faster                                                  |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                 |
| async_tree_io_tg           | 823 ms                                                       | 871 ms: 1.06x slower                                                  |
| async_generators           | 364 ms                                                       | 387 ms: 1.07x slower                                                  |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                          |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 87.0 ms: 1.06x faster                                                 |
| float          | 81.6 ms                                                      | 79.6 ms: 1.02x faster                                                 |
| pidigits       | 252 ms                                                       | 251 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                        | 1.03x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 147 ms: 1.03x slower                                                  |
| regex_v8       | 24.9 ms                                                      | 25.9 ms: 1.04x slower                                                 |
| regex_effbot   | 3.51 ms                                                      | 3.73 ms: 1.06x slower                                                 |
| regex_dna      | 238 ms                                                       | 257 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                        | 1.05x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.11 sec: 1.15x faster                                                |
| xml_etree_generate   | 85.2 ms                                                      | 81.1 ms: 1.05x faster                                                 |
| xml_etree_process    | 60.7 ms                                                      | 58.1 ms: 1.05x faster                                                 |
| xml_etree_iterparse  | 99.8 ms                                                      | 100 ms: 1.01x slower                                                  |
| json_loads           | 24.7 us                                                      | 25.0 us: 1.01x slower                                                 |
| xml_etree_parse      | 144 ms                                                       | 146 ms: 1.01x slower                                                  |
| unpickle_pure_python | 216 us                                                       | 220 us: 1.02x slower                                                  |
| json_dumps           | 10.8 ms                                                      | 11.1 ms: 1.03x slower                                                 |
| pickle_pure_python   | 322 us                                                       | 332 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 14.9 ms: 1.05x faster                                                 |
| python_startup_no_site | 8.93 ms                                                      | 9.03 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.62 ms: 1.07x faster                                                 |
| genshi_text     | 27.2 ms                                                      | 27.7 ms: 1.02x slower                                                 |
| genshi_xml      | 58.0 ms                                                      | 61.9 ms: 1.07x slower                                                 |
| django_template | 38.9 ms                                                      | 43.1 ms: 1.11x slower                                                 |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 38.9 us                                                      | 30.3 us: 1.29x faster                                                 |
| deepcopy                   | 388 us                                                       | 314 us: 1.24x faster                                                  |
| async_tree_memoization_tg  | 458 ms                                                       | 374 ms: 1.23x faster                                                  |
| scimark_sor                | 125 ms                                                       | 105 ms: 1.19x faster                                                  |
| richards                   | 52.5 ms                                                      | 45.1 ms: 1.16x faster                                                 |
| tomli_loads                | 2.43 sec                                                     | 2.11 sec: 1.15x faster                                                |
| deepcopy_reduce            | 3.49 us                                                      | 3.04 us: 1.15x faster                                                 |
| telco                      | 8.77 ms                                                      | 7.78 ms: 1.13x faster                                                 |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                                 |
| richards_super             | 60.2 ms                                                      | 54.7 ms: 1.10x faster                                                 |
| coverage                   | 84.5 ms                                                      | 77.8 ms: 1.09x faster                                                 |
| async_tree_memoization     | 447 ms                                                       | 412 ms: 1.09x faster                                                  |
| async_tree_none            | 370 ms                                                       | 341 ms: 1.09x faster                                                  |
| json                       | 5.62 ms                                                      | 5.22 ms: 1.08x faster                                                 |
| go                         | 167 ms                                                       | 155 ms: 1.08x faster                                                  |
| mako                       | 10.3 ms                                                      | 9.62 ms: 1.07x faster                                                 |
| bpe_tokeniser              | 5.09 sec                                                     | 4.76 sec: 1.07x faster                                                |
| pprint_safe_repr           | 835 ms                                                       | 788 ms: 1.06x faster                                                  |
| nbody                      | 92.1 ms                                                      | 87.0 ms: 1.06x faster                                                 |
| async_tree_none_tg         | 342 ms                                                       | 323 ms: 1.06x faster                                                  |
| pyflate                    | 493 ms                                                       | 466 ms: 1.06x faster                                                  |
| logging_silent             | 97.5 ns                                                      | 92.3 ns: 1.06x faster                                                 |
| xml_etree_generate         | 85.2 ms                                                      | 81.1 ms: 1.05x faster                                                 |
| python_startup             | 15.6 ms                                                      | 14.9 ms: 1.05x faster                                                 |
| scimark_fft                | 298 ms                                                       | 285 ms: 1.05x faster                                                  |
| fannkuch                   | 384 ms                                                       | 367 ms: 1.05x faster                                                  |
| xml_etree_process          | 60.7 ms                                                      | 58.1 ms: 1.05x faster                                                 |
| html5lib                   | 72.9 ms                                                      | 70.4 ms: 1.04x faster                                                 |
| pprint_pformat             | 1.70 sec                                                     | 1.65 sec: 1.03x faster                                                |
| asyncio_websockets         | 395 ms                                                       | 382 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 577 ms: 1.03x faster                                                  |
| dulwich_log                | 65.5 ms                                                      | 63.5 ms: 1.03x faster                                                 |
| spectral_norm              | 97.4 ms                                                      | 94.8 ms: 1.03x faster                                                 |
| float                      | 81.6 ms                                                      | 79.6 ms: 1.02x faster                                                 |
| thrift                     | 918 us                                                       | 897 us: 1.02x faster                                                  |
| scimark_lu                 | 97.4 ms                                                      | 95.4 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 562 ms: 1.02x faster                                                  |
| deltablue                  | 3.38 ms                                                      | 3.34 ms: 1.01x faster                                                 |
| crypto_pyaes               | 73.5 ms                                                      | 73.0 ms: 1.01x faster                                                 |
| pidigits                   | 252 ms                                                       | 251 ms: 1.00x faster                                                  |
| xml_etree_iterparse        | 99.8 ms                                                      | 100 ms: 1.01x slower                                                  |
| json_loads                 | 24.7 us                                                      | 25.0 us: 1.01x slower                                                 |
| python_startup_no_site     | 8.93 ms                                                      | 9.03 ms: 1.01x slower                                                 |
| xml_etree_parse            | 144 ms                                                       | 146 ms: 1.01x slower                                                  |
| meteor_contest             | 130 ms                                                       | 132 ms: 1.02x slower                                                  |
| unpickle_pure_python       | 216 us                                                       | 220 us: 1.02x slower                                                  |
| mdp                        | 2.53 sec                                                     | 2.57 sec: 1.02x slower                                                |
| genshi_text                | 27.2 ms                                                      | 27.7 ms: 1.02x slower                                                 |
| json_dumps                 | 10.8 ms                                                      | 11.1 ms: 1.03x slower                                                 |
| regex_compile              | 143 ms                                                       | 147 ms: 1.03x slower                                                  |
| pickle_pure_python         | 322 us                                                       | 332 us: 1.03x slower                                                  |
| tornado_http               | 119 ms                                                       | 123 ms: 1.03x slower                                                  |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                 |
| logging_format             | 6.95 us                                                      | 7.23 us: 1.04x slower                                                 |
| regex_v8                   | 24.9 ms                                                      | 25.9 ms: 1.04x slower                                                 |
| sympy_expand               | 506 ms                                                       | 527 ms: 1.04x slower                                                  |
| typing_runtime_protocols   | 176 us                                                       | 183 us: 1.04x slower                                                  |
| scimark_monte_carlo        | 65.2 ms                                                      | 68.8 ms: 1.06x slower                                                 |
| async_tree_io_tg           | 823 ms                                                       | 871 ms: 1.06x slower                                                  |
| regex_effbot               | 3.51 ms                                                      | 3.73 ms: 1.06x slower                                                 |
| async_generators           | 364 ms                                                       | 387 ms: 1.07x slower                                                  |
| genshi_xml                 | 58.0 ms                                                      | 61.9 ms: 1.07x slower                                                 |
| sympy_str                  | 297 ms                                                       | 317 ms: 1.07x slower                                                  |
| 2to3                       | 293 ms                                                       | 314 ms: 1.07x slower                                                  |
| logging_simple             | 6.28 us                                                      | 6.75 us: 1.08x slower                                                 |
| regex_dna                  | 238 ms                                                       | 257 ms: 1.08x slower                                                  |
| comprehensions             | 17.3 us                                                      | 18.8 us: 1.09x slower                                                 |
| sqlglot_parse              | 1.37 ms                                                      | 1.50 ms: 1.09x slower                                                 |
| create_gc_cycles           | 2.65 ms                                                      | 2.90 ms: 1.10x slower                                                 |
| nqueens                    | 92.3 ms                                                      | 102 ms: 1.10x slower                                                  |
| django_template            | 38.9 ms                                                      | 43.1 ms: 1.11x slower                                                 |
| sqlglot_transpile          | 1.76 ms                                                      | 1.96 ms: 1.11x slower                                                 |
| hexiom                     | 6.47 ms                                                      | 7.21 ms: 1.11x slower                                                 |
| sqlglot_normalize          | 119 ms                                                       | 133 ms: 1.11x slower                                                  |
| sympy_sum                  | 154 ms                                                       | 173 ms: 1.13x slower                                                  |
| docutils                   | 2.81 sec                                                     | 3.18 sec: 1.13x slower                                                |
| sphinx                     | 1.11 sec                                                     | 1.26 sec: 1.13x slower                                                |
| chaos                      | 60.6 ms                                                      | 68.7 ms: 1.13x slower                                                 |
| generators                 | 33.9 ms                                                      | 38.7 ms: 1.14x slower                                                 |
| sympy_integrate            | 23.4 ms                                                      | 27.2 ms: 1.16x slower                                                 |
| sqlglot_optimize           | 58.7 ms                                                      | 68.8 ms: 1.17x slower                                                 |
| raytrace                   | 267 ms                                                       | 316 ms: 1.18x slower                                                  |
| pylint                     | 345 ms                                                       | 415 ms: 1.20x slower                                                  |
| gc_traversal               | 4.48 ms                                                      | 5.81 ms: 1.30x slower                                                 |
| bench_mp_pool              | 4.82 ms                                                      | 3.17 sec: 657.95x slower                                              |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                          |

Benchmark hidden because not significant (4): pycparser, scimark_sparse_mat_mult, async_tree_io, bench_thread_pool
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.007x slower
# HPT report

- Reliability score: 65.09% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x