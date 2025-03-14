# Results vs. 3.13.0

- fork: brandtbucher
- ref: jump_backoff
- machine: windows-x86
- commit hash: 2e7a174
- commit date: 2024-11-13
- overall geometric mean: 1.055x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 267 ms: 1.05x slower                                                          |
| docutils       | 1.80 sec                                                        | 2.08 sec: 1.16x slower                                                        |
| html5lib       | 47.1 ms                                                         | 48.9 ms: 1.04x slower                                                         |
| sphinx         | 729 ms                                                          | 875 ms: 1.20x slower                                                          |
| Geometric mean | (ref)                                                           | 1.11x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 264 ms: 1.09x faster                                                          |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 460 ms: 1.02x faster                                                          |
| async_tree_none_tg         | 216 ms                                                          | 213 ms: 1.01x faster                                                          |
| asyncio_websockets         | 352 ms                                                          | 362 ms: 1.03x slower                                                          |
| coroutines                 | 16.1 ms                                                         | 16.7 ms: 1.04x slower                                                         |
| async_tree_io              | 530 ms                                                          | 559 ms: 1.05x slower                                                          |
| async_tree_io_tg           | 499 ms                                                          | 561 ms: 1.12x slower                                                          |
| async_generators           | 267 ms                                                          | 324 ms: 1.21x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.03x slower                                                                  |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 56.4 ms                                                         | 55.6 ms: 1.02x faster                                                         |
| pidigits       | 204 ms                                                          | 203 ms: 1.00x faster                                                          |
| nbody          | 81.4 ms                                                         | 100 ms: 1.23x slower                                                          |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 1.82 ms                                                         | 1.83 ms: 1.00x slower                                                         |
| regex_dna      | 112 ms                                                          | 116 ms: 1.03x slower                                                          |
| regex_v8       | 15.5 ms                                                         | 16.1 ms: 1.04x slower                                                         |
| regex_compile  | 101 ms                                                          | 117 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 20.7 us: 1.05x faster                                                         |
| tomli_loads          | 1.74 sec                                                        | 1.85 sec: 1.06x slower                                                        |
| xml_etree_parse      | 102 ms                                                          | 112 ms: 1.10x slower                                                          |
| xml_etree_iterparse  | 61.3 ms                                                         | 68.0 ms: 1.11x slower                                                         |
| json_dumps           | 7.53 ms                                                         | 8.79 ms: 1.17x slower                                                         |
| xml_etree_generate   | 61.9 ms                                                         | 73.3 ms: 1.18x slower                                                         |
| xml_etree_process    | 44.6 ms                                                         | 53.9 ms: 1.21x slower                                                         |
| pickle_pure_python   | 239 us                                                          | 302 us: 1.26x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 208 us: 1.28x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.14x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.5 ms: 1.11x faster                                                         |
| python_startup_no_site | 20.2 ms                                                         | 19.2 ms: 1.05x faster                                                         |
| Geometric mean         | (ref)                                                           | 1.08x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 7.02 ms                                                         | 7.37 ms: 1.05x slower                                                         |
| django_template | 32.0 ms                                                         | 36.0 ms: 1.12x slower                                                         |
| genshi_xml      | 49.0 ms                                                         | 56.5 ms: 1.15x slower                                                         |
| genshi_text     | 21.7 ms                                                         | 25.8 ms: 1.19x slower                                                         |
| Geometric mean  | (ref)                                                           | 1.13x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 776 us: 13.23x faster                                                         |
| coverage                   | 326 ms                                                          | 51.7 ms: 6.31x faster                                                         |
| sqlglot_normalize          | 223 ms                                                          | 110 ms: 2.02x faster                                                          |
| deepcopy_memo              | 26.2 us                                                         | 23.1 us: 1.14x faster                                                         |
| deepcopy                   | 311 us                                                          | 277 us: 1.12x faster                                                          |
| python_startup             | 28.3 ms                                                         | 25.5 ms: 1.11x faster                                                         |
| async_tree_memoization_tg  | 287 ms                                                          | 264 ms: 1.09x faster                                                          |
| bench_mp_pool              | 93.6 ms                                                         | 86.3 ms: 1.08x faster                                                         |
| pathlib                    | 89.1 ms                                                         | 82.6 ms: 1.08x faster                                                         |
| python_startup_no_site     | 20.2 ms                                                         | 19.2 ms: 1.05x faster                                                         |
| json_loads                 | 21.7 us                                                         | 20.7 us: 1.05x faster                                                         |
| deepcopy_reduce            | 2.94 us                                                         | 2.82 us: 1.04x faster                                                         |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 460 ms: 1.02x faster                                                          |
| float                      | 56.4 ms                                                         | 55.6 ms: 1.02x faster                                                         |
| dulwich_log                | 50.2 ms                                                         | 49.5 ms: 1.01x faster                                                         |
| async_tree_none_tg         | 216 ms                                                          | 213 ms: 1.01x faster                                                          |
| pidigits                   | 204 ms                                                          | 203 ms: 1.00x faster                                                          |
| regex_effbot               | 1.82 ms                                                         | 1.83 ms: 1.00x slower                                                         |
| gc_traversal               | 1.76 ms                                                         | 1.78 ms: 1.01x slower                                                         |
| asyncio_websockets         | 352 ms                                                          | 362 ms: 1.03x slower                                                          |
| regex_dna                  | 112 ms                                                          | 116 ms: 1.03x slower                                                          |
| coroutines                 | 16.1 ms                                                         | 16.7 ms: 1.04x slower                                                         |
| html5lib                   | 47.1 ms                                                         | 48.9 ms: 1.04x slower                                                         |
| regex_v8                   | 15.5 ms                                                         | 16.1 ms: 1.04x slower                                                         |
| 2to3                       | 255 ms                                                          | 267 ms: 1.05x slower                                                          |
| mako                       | 7.02 ms                                                         | 7.37 ms: 1.05x slower                                                         |
| logging_format             | 8.59 us                                                         | 9.04 us: 1.05x slower                                                         |
| async_tree_io              | 530 ms                                                          | 559 ms: 1.05x slower                                                          |
| tomli_loads                | 1.74 sec                                                        | 1.85 sec: 1.06x slower                                                        |
| pycparser                  | 869 ms                                                          | 922 ms: 1.06x slower                                                          |
| logging_simple             | 7.89 us                                                         | 8.39 us: 1.06x slower                                                         |
| create_gc_cycles           | 1.08 ms                                                         | 1.16 ms: 1.07x slower                                                         |
| bpe_tokeniser              | 3.49 sec                                                        | 3.76 sec: 1.08x slower                                                        |
| connected_components       | 266 ms                                                          | 287 ms: 1.08x slower                                                          |
| sympy_sum                  | 108 ms                                                          | 117 ms: 1.08x slower                                                          |
| shortest_path              | 298 ms                                                          | 322 ms: 1.08x slower                                                          |
| xml_etree_parse            | 102 ms                                                          | 112 ms: 1.10x slower                                                          |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.19 ms: 1.11x slower                                                         |
| xml_etree_iterparse        | 61.3 ms                                                         | 68.0 ms: 1.11x slower                                                         |
| sympy_expand               | 377 ms                                                          | 424 ms: 1.12x slower                                                          |
| async_tree_io_tg           | 499 ms                                                          | 561 ms: 1.12x slower                                                          |
| django_template            | 32.0 ms                                                         | 36.0 ms: 1.12x slower                                                         |
| pprint_safe_repr           | 658 ms                                                          | 740 ms: 1.12x slower                                                          |
| go                         | 111 ms                                                          | 125 ms: 1.13x slower                                                          |
| sympy_str                  | 214 ms                                                          | 243 ms: 1.14x slower                                                          |
| telco                      | 6.27 ms                                                         | 7.18 ms: 1.15x slower                                                         |
| meteor_contest             | 78.1 ms                                                         | 89.8 ms: 1.15x slower                                                         |
| mdp                        | 1.70 sec                                                        | 1.95 sec: 1.15x slower                                                        |
| pylint                     | 225 ms                                                          | 258 ms: 1.15x slower                                                          |
| pprint_pformat             | 1.32 sec                                                        | 1.52 sec: 1.15x slower                                                        |
| genshi_xml                 | 49.0 ms                                                         | 56.5 ms: 1.15x slower                                                         |
| regex_compile              | 101 ms                                                          | 117 ms: 1.15x slower                                                          |
| docutils                   | 1.80 sec                                                        | 2.08 sec: 1.16x slower                                                        |
| sympy_integrate            | 15.2 ms                                                         | 17.6 ms: 1.16x slower                                                         |
| sqlglot_parse              | 1.02 ms                                                         | 1.18 ms: 1.16x slower                                                         |
| crypto_pyaes               | 56.6 ms                                                         | 65.9 ms: 1.16x slower                                                         |
| json_dumps                 | 7.53 ms                                                         | 8.79 ms: 1.17x slower                                                         |
| sqlglot_transpile          | 1.26 ms                                                         | 1.47 ms: 1.17x slower                                                         |
| fannkuch                   | 288 ms                                                          | 338 ms: 1.17x slower                                                          |
| scimark_sor                | 85.8 ms                                                         | 101 ms: 1.18x slower                                                          |
| xml_etree_generate         | 61.9 ms                                                         | 73.3 ms: 1.18x slower                                                         |
| genshi_text                | 21.7 ms                                                         | 25.8 ms: 1.19x slower                                                         |
| typing_runtime_protocols   | 141 us                                                          | 168 us: 1.19x slower                                                          |
| scimark_fft                | 204 ms                                                          | 244 ms: 1.20x slower                                                          |
| sphinx                     | 729 ms                                                          | 875 ms: 1.20x slower                                                          |
| spectral_norm              | 70.0 ms                                                         | 84.3 ms: 1.20x slower                                                         |
| xml_etree_process          | 44.6 ms                                                         | 53.9 ms: 1.21x slower                                                         |
| sqlglot_optimize           | 42.4 ms                                                         | 51.5 ms: 1.21x slower                                                         |
| async_generators           | 267 ms                                                          | 324 ms: 1.21x slower                                                          |
| nbody                      | 81.4 ms                                                         | 100 ms: 1.23x slower                                                          |
| scimark_lu                 | 60.7 ms                                                         | 75.9 ms: 1.25x slower                                                         |
| pyflate                    | 322 ms                                                          | 404 ms: 1.26x slower                                                          |
| pickle_pure_python         | 239 us                                                          | 302 us: 1.26x slower                                                          |
| scimark_monte_carlo        | 48.7 ms                                                         | 62.1 ms: 1.28x slower                                                         |
| unpickle_pure_python       | 162 us                                                          | 208 us: 1.28x slower                                                          |
| richards                   | 33.4 ms                                                         | 43.1 ms: 1.29x slower                                                         |
| nqueens                    | 75.1 ms                                                         | 97.8 ms: 1.30x slower                                                         |
| chaos                      | 49.4 ms                                                         | 65.3 ms: 1.32x slower                                                         |
| richards_super             | 37.0 ms                                                         | 49.4 ms: 1.33x slower                                                         |
| deltablue                  | 2.35 ms                                                         | 3.23 ms: 1.38x slower                                                         |
| logging_silent             | 62.4 ns                                                         | 86.0 ns: 1.38x slower                                                         |
| comprehensions             | 13.1 us                                                         | 18.2 us: 1.38x slower                                                         |
| k_core                     | 1.43 sec                                                        | 2.06 sec: 1.44x slower                                                        |
| raytrace                   | 203 ms                                                          | 308 ms: 1.52x slower                                                          |
| hexiom                     | 4.60 ms                                                         | 7.21 ms: 1.57x slower                                                         |
| generators                 | 21.5 ms                                                         | 35.6 ms: 1.66x slower                                                         |
| Geometric mean             | (ref)                                                           | 1.06x slower                                                                  |

Benchmark hidden because not significant (5): async_tree_memoization, bench_thread_pool, async_tree_cpu_io_mixed, async_tree_none, json
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20241113-3.14.0a1+-2e7a174-JIT/bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174.json: sqlite_synth

- Geometric mean (including insignificant results): 1.055x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown