# Results vs. 3.13.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: linux-x86_64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.296x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x slower
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 430 ms: 1.47x slower                                                         |
| docutils       | 2.81 sec                                                     | 3.40 sec: 1.21x slower                                                       |
| html5lib       | 72.9 ms                                                      | 103 ms: 1.41x slower                                                         |
| sphinx         | 1.11 sec                                                     | 1.35 sec: 1.21x slower                                                       |
| tornado_http   | 119 ms                                                       | 166 ms: 1.39x slower                                                         |
| Geometric mean | (ref)                                                        | 1.33x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_websockets         | 395 ms                                                       | 381 ms: 1.04x faster                                                         |
| async_tree_memoization_tg  | 458 ms                                                       | 477 ms: 1.04x slower                                                         |
| async_tree_io_tg           | 823 ms                                                       | 890 ms: 1.08x slower                                                         |
| async_tree_none_tg         | 342 ms                                                       | 373 ms: 1.09x slower                                                         |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 633 ms: 1.10x slower                                                         |
| async_tree_none            | 370 ms                                                       | 416 ms: 1.12x slower                                                         |
| async_tree_io              | 832 ms                                                       | 936 ms: 1.13x slower                                                         |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 680 ms: 1.14x slower                                                         |
| async_tree_memoization     | 447 ms                                                       | 517 ms: 1.16x slower                                                         |
| coroutines                 | 21.6 ms                                                      | 28.0 ms: 1.30x slower                                                        |
| async_generators           | 364 ms                                                       | 492 ms: 1.35x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.13x slower                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 252 ms                                                       | 249 ms: 1.01x faster                                                         |
| float          | 81.6 ms                                                      | 145 ms: 1.78x slower                                                         |
| nbody          | 92.1 ms                                                      | 194 ms: 2.11x slower                                                         |
| Geometric mean | (ref)                                                        | 1.55x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 239 ms: 1.00x slower                                                         |
| regex_effbot   | 3.51 ms                                                      | 3.60 ms: 1.03x slower                                                        |
| regex_v8       | 24.9 ms                                                      | 26.8 ms: 1.07x slower                                                        |
| regex_compile  | 143 ms                                                       | 226 ms: 1.59x slower                                                         |
| Geometric mean | (ref)                                                        | 1.15x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 139 ms: 1.04x faster                                                         |
| xml_etree_iterparse  | 99.8 ms                                                      | 109 ms: 1.09x slower                                                         |
| json_loads           | 24.7 us                                                      | 28.8 us: 1.16x slower                                                        |
| xml_etree_generate   | 85.2 ms                                                      | 116 ms: 1.36x slower                                                         |
| json_dumps           | 10.8 ms                                                      | 15.1 ms: 1.40x slower                                                        |
| tomli_loads          | 2.43 sec                                                     | 3.41 sec: 1.40x slower                                                       |
| xml_etree_process    | 60.7 ms                                                      | 95.3 ms: 1.57x slower                                                        |
| pickle_pure_python   | 322 us                                                       | 598 us: 1.86x slower                                                         |
| unpickle_pure_python | 216 us                                                       | 408 us: 1.89x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.38x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 19.3 ms: 1.23x slower                                                        |
| python_startup_no_site | 8.93 ms                                                      | 11.8 ms: 1.33x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.28x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 58.0 ms                                                      | 81.0 ms: 1.40x slower                                                        |
| genshi_text     | 27.2 ms                                                      | 42.5 ms: 1.56x slower                                                        |
| django_template | 38.9 ms                                                      | 67.2 ms: 1.73x slower                                                        |
| mako            | 10.3 ms                                                      | 22.3 ms: 2.16x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.69x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal               | 4.48 ms                                                      | 3.63 ms: 1.24x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 139 ms: 1.04x faster                                                         |
| asyncio_websockets         | 395 ms                                                       | 381 ms: 1.04x faster                                                         |
| pidigits                   | 252 ms                                                       | 249 ms: 1.01x faster                                                         |
| regex_dna                  | 238 ms                                                       | 239 ms: 1.00x slower                                                         |
| regex_effbot               | 3.51 ms                                                      | 3.60 ms: 1.03x slower                                                        |
| async_tree_memoization_tg  | 458 ms                                                       | 477 ms: 1.04x slower                                                         |
| json                       | 5.62 ms                                                      | 5.96 ms: 1.06x slower                                                        |
| regex_v8                   | 24.9 ms                                                      | 26.8 ms: 1.07x slower                                                        |
| async_tree_io_tg           | 823 ms                                                       | 890 ms: 1.08x slower                                                         |
| async_tree_none_tg         | 342 ms                                                       | 373 ms: 1.09x slower                                                         |
| xml_etree_iterparse        | 99.8 ms                                                      | 109 ms: 1.09x slower                                                         |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 633 ms: 1.10x slower                                                         |
| deepcopy                   | 388 us                                                       | 432 us: 1.11x slower                                                         |
| pathlib                    | 17.4 ms                                                      | 19.4 ms: 1.11x slower                                                        |
| async_tree_none            | 370 ms                                                       | 416 ms: 1.12x slower                                                         |
| async_tree_io              | 832 ms                                                       | 936 ms: 1.13x slower                                                         |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 680 ms: 1.14x slower                                                         |
| async_tree_memoization     | 447 ms                                                       | 517 ms: 1.16x slower                                                         |
| telco                      | 8.77 ms                                                      | 10.2 ms: 1.16x slower                                                        |
| json_loads                 | 24.7 us                                                      | 28.8 us: 1.16x slower                                                        |
| generators                 | 33.9 ms                                                      | 40.8 ms: 1.20x slower                                                        |
| docutils                   | 2.81 sec                                                     | 3.40 sec: 1.21x slower                                                       |
| sphinx                     | 1.11 sec                                                     | 1.35 sec: 1.21x slower                                                       |
| python_startup             | 15.6 ms                                                      | 19.3 ms: 1.23x slower                                                        |
| pylint                     | 345 ms                                                       | 432 ms: 1.25x slower                                                         |
| deepcopy_memo              | 38.9 us                                                      | 48.8 us: 1.26x slower                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 6.46 sec: 1.27x slower                                                       |
| mdp                        | 2.53 sec                                                     | 3.24 sec: 1.28x slower                                                       |
| coverage                   | 84.5 ms                                                      | 108 ms: 1.28x slower                                                         |
| coroutines                 | 21.6 ms                                                      | 28.0 ms: 1.30x slower                                                        |
| meteor_contest             | 130 ms                                                       | 169 ms: 1.30x slower                                                         |
| sqlalchemy_imperative      | 18.1 ms                                                      | 23.9 ms: 1.32x slower                                                        |
| python_startup_no_site     | 8.93 ms                                                      | 11.8 ms: 1.33x slower                                                        |
| scimark_fft                | 298 ms                                                       | 397 ms: 1.33x slower                                                         |
| deepcopy_reduce            | 3.49 us                                                      | 4.69 us: 1.34x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.68 ms: 1.35x slower                                                        |
| pycparser                  | 1.28 sec                                                     | 1.73 sec: 1.35x slower                                                       |
| dulwich_log                | 65.5 ms                                                      | 88.6 ms: 1.35x slower                                                        |
| async_generators           | 364 ms                                                       | 492 ms: 1.35x slower                                                         |
| xml_etree_generate         | 85.2 ms                                                      | 116 ms: 1.36x slower                                                         |
| tornado_http               | 119 ms                                                       | 166 ms: 1.39x slower                                                         |
| genshi_xml                 | 58.0 ms                                                      | 81.0 ms: 1.40x slower                                                        |
| json_dumps                 | 10.8 ms                                                      | 15.1 ms: 1.40x slower                                                        |
| sympy_integrate            | 23.4 ms                                                      | 32.8 ms: 1.40x slower                                                        |
| tomli_loads                | 2.43 sec                                                     | 3.41 sec: 1.40x slower                                                       |
| html5lib                   | 72.9 ms                                                      | 103 ms: 1.41x slower                                                         |
| nqueens                    | 92.3 ms                                                      | 131 ms: 1.42x slower                                                         |
| 2to3                       | 293 ms                                                       | 430 ms: 1.47x slower                                                         |
| thrift                     | 918 us                                                       | 1.39 ms: 1.51x slower                                                        |
| sympy_str                  | 297 ms                                                       | 449 ms: 1.52x slower                                                         |
| typing_runtime_protocols   | 176 us                                                       | 266 us: 1.52x slower                                                         |
| sqlalchemy_declarative     | 148 ms                                                       | 226 ms: 1.52x slower                                                         |
| fannkuch                   | 384 ms                                                       | 590 ms: 1.53x slower                                                         |
| richards                   | 52.5 ms                                                      | 81.0 ms: 1.54x slower                                                        |
| sqlglot_normalize          | 119 ms                                                       | 184 ms: 1.55x slower                                                         |
| genshi_text                | 27.2 ms                                                      | 42.5 ms: 1.56x slower                                                        |
| xml_etree_process          | 60.7 ms                                                      | 95.3 ms: 1.57x slower                                                        |
| pyflate                    | 493 ms                                                       | 774 ms: 1.57x slower                                                         |
| sqlglot_optimize           | 58.7 ms                                                      | 92.3 ms: 1.57x slower                                                        |
| regex_compile              | 143 ms                                                       | 226 ms: 1.59x slower                                                         |
| sympy_expand               | 506 ms                                                       | 805 ms: 1.59x slower                                                         |
| richards_super             | 60.2 ms                                                      | 99.9 ms: 1.66x slower                                                        |
| pprint_safe_repr           | 835 ms                                                       | 1.39 sec: 1.67x slower                                                       |
| crypto_pyaes               | 73.5 ms                                                      | 123 ms: 1.67x slower                                                         |
| bench_thread_pool          | 929 us                                                       | 1.57 ms: 1.69x slower                                                        |
| sympy_sum                  | 154 ms                                                       | 261 ms: 1.70x slower                                                         |
| spectral_norm              | 97.4 ms                                                      | 166 ms: 1.70x slower                                                         |
| pprint_pformat             | 1.70 sec                                                     | 2.89 sec: 1.70x slower                                                       |
| django_template            | 38.9 ms                                                      | 67.2 ms: 1.73x slower                                                        |
| go                         | 167 ms                                                       | 291 ms: 1.74x slower                                                         |
| logging_format             | 6.95 us                                                      | 12.2 us: 1.75x slower                                                        |
| comprehensions             | 17.3 us                                                      | 30.3 us: 1.76x slower                                                        |
| float                      | 81.6 ms                                                      | 145 ms: 1.78x slower                                                         |
| logging_simple             | 6.28 us                                                      | 11.3 us: 1.79x slower                                                        |
| hexiom                     | 6.47 ms                                                      | 11.7 ms: 1.81x slower                                                        |
| pickle_pure_python         | 322 us                                                       | 598 us: 1.86x slower                                                         |
| logging_silent             | 97.5 ns                                                      | 183 ns: 1.88x slower                                                         |
| unpickle_pure_python       | 216 us                                                       | 408 us: 1.89x slower                                                         |
| sqlglot_transpile          | 1.76 ms                                                      | 3.39 ms: 1.92x slower                                                        |
| scimark_sor                | 125 ms                                                       | 242 ms: 1.94x slower                                                         |
| sqlglot_parse              | 1.37 ms                                                      | 2.81 ms: 2.06x slower                                                        |
| scimark_monte_carlo        | 65.2 ms                                                      | 134 ms: 2.06x slower                                                         |
| chaos                      | 60.6 ms                                                      | 125 ms: 2.07x slower                                                         |
| nbody                      | 92.1 ms                                                      | 194 ms: 2.11x slower                                                         |
| mako                       | 10.3 ms                                                      | 22.3 ms: 2.16x slower                                                        |
| scimark_lu                 | 97.4 ms                                                      | 218 ms: 2.24x slower                                                         |
| raytrace                   | 267 ms                                                       | 616 ms: 2.30x slower                                                         |
| deltablue                  | 3.38 ms                                                      | 8.20 ms: 2.42x slower                                                        |
| bench_mp_pool              | 4.82 ms                                                      | 52.2 ms: 10.83x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.46x slower                                                                 |

Benchmark hidden because not significant (1): create_gc_cycles
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path

- Geometric mean (including insignificant results): 1.296x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.33x
- 95% likely to have a slowdown of 1.31x
- 99% likely to have a slowdown of 1.28x

# Memory
- memory change: 1.18x