# Results vs. 3.13.0

- fork: faster-cpython
- ref: account_for_escapes_
- machine: linux-x86_64
- commit hash: 17b3e16
- commit date: 2025-02-07
- overall geometric mean: 1.058x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 285 ms: 1.03x faster                                                                   |
| docutils       | 2.83 sec                                                     | 2.86 sec: 1.01x slower                                                                 |
| html5lib       | 73.5 ms                                                      | 66.7 ms: 1.10x faster                                                                  |
| sphinx         | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                                 |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 338 ms: 1.38x faster                                                                   |
| async_tree_none            | 376 ms                                                       | 288 ms: 1.31x faster                                                                   |
| async_tree_io              | 843 ms                                                       | 654 ms: 1.29x faster                                                                   |
| async_tree_io_tg           | 831 ms                                                       | 645 ms: 1.29x faster                                                                   |
| async_tree_memoization     | 453 ms                                                       | 353 ms: 1.28x faster                                                                   |
| async_tree_none_tg         | 346 ms                                                       | 278 ms: 1.25x faster                                                                   |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 522 ms: 1.16x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 509 ms: 1.14x faster                                                                   |
| async_generators           | 457 ms                                                       | 402 ms: 1.14x faster                                                                   |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.02x faster                                                                  |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                                   |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 70.2 ms: 1.16x faster                                                                  |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                                   |
| nbody          | 89.3 ms                                                      | 91.6 ms: 1.03x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.19 ms: 1.15x faster                                                                  |
| regex_compile  | 143 ms                                                       | 136 ms: 1.05x faster                                                                   |
| regex_dna      | 247 ms                                                       | 250 ms: 1.01x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.08 sec: 1.18x faster                                                                 |
| xml_etree_parse      | 150 ms                                                       | 135 ms: 1.11x faster                                                                   |
| xml_etree_iterparse  | 103 ms                                                       | 95.1 ms: 1.08x faster                                                                  |
| unpickle_pure_python | 217 us                                                       | 206 us: 1.05x faster                                                                   |
| xml_etree_generate   | 86.5 ms                                                      | 82.3 ms: 1.05x faster                                                                  |
| xml_etree_process    | 61.2 ms                                                      | 58.8 ms: 1.04x faster                                                                  |
| pickle_pure_python   | 323 us                                                       | 332 us: 1.03x slower                                                                   |
| json_dumps           | 11.1 ms                                                      | 11.6 ms: 1.04x slower                                                                  |
| json_loads           | 24.7 us                                                      | 26.5 us: 1.08x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 8.99 ms: 1.00x slower                                                                  |
| python_startup         | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 24.4 ms: 1.07x faster                                                                  |
| genshi_xml      | 57.1 ms                                                      | 55.7 ms: 1.02x faster                                                                  |
| django_template | 36.4 ms                                                      | 35.9 ms: 1.01x faster                                                                  |
| mako            | 10.4 ms                                                      | 11.0 ms: 1.06x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| deepcopy                   | 392 us                                                       | 282 us: 1.39x faster                                                                   |
| async_tree_memoization_tg  | 466 ms                                                       | 338 ms: 1.38x faster                                                                   |
| async_tree_none            | 376 ms                                                       | 288 ms: 1.31x faster                                                                   |
| deepcopy_memo              | 38.6 us                                                      | 29.7 us: 1.30x faster                                                                  |
| async_tree_io              | 843 ms                                                       | 654 ms: 1.29x faster                                                                   |
| async_tree_io_tg           | 831 ms                                                       | 645 ms: 1.29x faster                                                                   |
| async_tree_memoization     | 453 ms                                                       | 353 ms: 1.28x faster                                                                   |
| go                         | 162 ms                                                       | 129 ms: 1.26x faster                                                                   |
| async_tree_none_tg         | 346 ms                                                       | 278 ms: 1.25x faster                                                                   |
| deepcopy_reduce            | 3.54 us                                                      | 2.96 us: 1.20x faster                                                                  |
| tomli_loads                | 2.46 sec                                                     | 2.08 sec: 1.18x faster                                                                 |
| spectral_norm              | 97.0 ms                                                      | 82.5 ms: 1.18x faster                                                                  |
| float                      | 81.3 ms                                                      | 70.2 ms: 1.16x faster                                                                  |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 522 ms: 1.16x faster                                                                   |
| regex_effbot               | 3.67 ms                                                      | 3.19 ms: 1.15x faster                                                                  |
| pyflate                    | 503 ms                                                       | 439 ms: 1.15x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 509 ms: 1.14x faster                                                                   |
| async_generators           | 457 ms                                                       | 402 ms: 1.14x faster                                                                   |
| scimark_sor                | 123 ms                                                       | 109 ms: 1.13x faster                                                                   |
| richards                   | 52.9 ms                                                      | 46.7 ms: 1.13x faster                                                                  |
| pathlib                    | 17.5 ms                                                      | 15.6 ms: 1.12x faster                                                                  |
| bpe_tokeniser              | 5.09 sec                                                     | 4.53 sec: 1.12x faster                                                                 |
| richards_super             | 59.6 ms                                                      | 53.4 ms: 1.11x faster                                                                  |
| xml_etree_parse            | 150 ms                                                       | 135 ms: 1.11x faster                                                                   |
| generators                 | 33.6 ms                                                      | 30.2 ms: 1.11x faster                                                                  |
| html5lib                   | 73.5 ms                                                      | 66.7 ms: 1.10x faster                                                                  |
| pylint                     | 347 ms                                                       | 315 ms: 1.10x faster                                                                   |
| telco                      | 8.79 ms                                                      | 8.04 ms: 1.09x faster                                                                  |
| pprint_safe_repr           | 843 ms                                                       | 776 ms: 1.09x faster                                                                   |
| pprint_pformat             | 1.72 sec                                                     | 1.58 sec: 1.09x faster                                                                 |
| scimark_fft                | 328 ms                                                       | 303 ms: 1.08x faster                                                                   |
| xml_etree_iterparse        | 103 ms                                                       | 95.1 ms: 1.08x faster                                                                  |
| scimark_monte_carlo        | 66.1 ms                                                      | 61.5 ms: 1.07x faster                                                                  |
| genshi_text                | 26.2 ms                                                      | 24.4 ms: 1.07x faster                                                                  |
| hexiom                     | 6.55 ms                                                      | 6.16 ms: 1.06x faster                                                                  |
| unpickle_pure_python       | 217 us                                                       | 206 us: 1.05x faster                                                                   |
| connected_components       | 432 ms                                                       | 411 ms: 1.05x faster                                                                   |
| xml_etree_generate         | 86.5 ms                                                      | 82.3 ms: 1.05x faster                                                                  |
| regex_compile              | 143 ms                                                       | 136 ms: 1.05x faster                                                                   |
| meteor_contest             | 130 ms                                                       | 124 ms: 1.05x faster                                                                   |
| scimark_lu                 | 98.7 ms                                                      | 94.4 ms: 1.04x faster                                                                  |
| thrift                     | 901 us                                                       | 863 us: 1.04x faster                                                                   |
| json                       | 5.69 ms                                                      | 5.46 ms: 1.04x faster                                                                  |
| shortest_path              | 460 ms                                                       | 442 ms: 1.04x faster                                                                   |
| xml_etree_process          | 61.2 ms                                                      | 58.8 ms: 1.04x faster                                                                  |
| k_core                     | 2.17 sec                                                     | 2.10 sec: 1.03x faster                                                                 |
| sqlglot_optimize           | 59.3 ms                                                      | 57.4 ms: 1.03x faster                                                                  |
| sqlite_synth               | 2.91 us                                                      | 2.81 us: 1.03x faster                                                                  |
| sqlglot_parse              | 1.40 ms                                                      | 1.36 ms: 1.03x faster                                                                  |
| sqlalchemy_declarative     | 148 ms                                                       | 144 ms: 1.03x faster                                                                   |
| sympy_expand               | 509 ms                                                       | 495 ms: 1.03x faster                                                                   |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.8 ms: 1.03x faster                                                                  |
| dulwich_log                | 68.2 ms                                                      | 66.3 ms: 1.03x faster                                                                  |
| sympy_str                  | 298 ms                                                       | 290 ms: 1.03x faster                                                                   |
| sqlglot_normalize          | 119 ms                                                       | 116 ms: 1.03x faster                                                                   |
| 2to3                       | 293 ms                                                       | 285 ms: 1.03x faster                                                                   |
| sqlglot_transpile          | 1.79 ms                                                      | 1.74 ms: 1.03x faster                                                                  |
| mdp                        | 2.54 sec                                                     | 2.48 sec: 1.02x faster                                                                 |
| genshi_xml                 | 57.1 ms                                                      | 55.7 ms: 1.02x faster                                                                  |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.02x faster                                                                  |
| coverage                   | 80.0 ms                                                      | 78.3 ms: 1.02x faster                                                                  |
| sympy_sum                  | 155 ms                                                       | 152 ms: 1.02x faster                                                                   |
| sympy_integrate            | 23.6 ms                                                      | 23.1 ms: 1.02x faster                                                                  |
| sphinx                     | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                                 |
| deltablue                  | 3.42 ms                                                      | 3.37 ms: 1.01x faster                                                                  |
| django_template            | 36.4 ms                                                      | 35.9 ms: 1.01x faster                                                                  |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                                   |
| logging_silent             | 97.9 ns                                                      | 96.9 ns: 1.01x faster                                                                  |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.73 ms: 1.01x faster                                                                  |
| nqueens                    | 90.7 ms                                                      | 89.9 ms: 1.01x faster                                                                  |
| comprehensions             | 17.0 us                                                      | 17.0 us: 1.00x faster                                                                  |
| python_startup_no_site     | 8.96 ms                                                      | 8.99 ms: 1.00x slower                                                                  |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                                  |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                                   |
| pycparser                  | 1.24 sec                                                     | 1.26 sec: 1.01x slower                                                                 |
| regex_dna                  | 247 ms                                                       | 250 ms: 1.01x slower                                                                   |
| docutils                   | 2.83 sec                                                     | 2.86 sec: 1.01x slower                                                                 |
| raytrace                   | 273 ms                                                       | 277 ms: 1.02x slower                                                                   |
| logging_simple             | 6.39 us                                                      | 6.50 us: 1.02x slower                                                                  |
| crypto_pyaes               | 73.3 ms                                                      | 75.0 ms: 1.02x slower                                                                  |
| nbody                      | 89.3 ms                                                      | 91.6 ms: 1.03x slower                                                                  |
| pickle_pure_python         | 323 us                                                       | 332 us: 1.03x slower                                                                   |
| create_gc_cycles           | 2.68 ms                                                      | 2.76 ms: 1.03x slower                                                                  |
| logging_format             | 6.94 us                                                      | 7.14 us: 1.03x slower                                                                  |
| json_dumps                 | 11.1 ms                                                      | 11.6 ms: 1.04x slower                                                                  |
| mako                       | 10.4 ms                                                      | 11.0 ms: 1.06x slower                                                                  |
| many_optionals             | 930 us                                                       | 1.00 ms: 1.08x slower                                                                  |
| json_loads                 | 24.7 us                                                      | 26.5 us: 1.08x slower                                                                  |
| gc_traversal               | 4.74 ms                                                      | 6.12 ms: 1.29x slower                                                                  |
| subparsers                 | 17.5 ms                                                      | 22.7 ms: 1.30x slower                                                                  |
| bench_mp_pool              | 5.12 ms                                                      | 1.03 sec: 201.22x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.00x faster                                                                           |

Benchmark hidden because not significant (5): bench_thread_pool, chaos, typing_runtime_protocols, regex_v8, fannkuch
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.058x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.02x