# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: windows-amd64
- commit hash: 9698931
- commit date: 2024-10-24
- overall geometric mean: 1.060x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 258 ms: 1.17x slower                                                           |
| docutils       | 1.57 sec                                                    | 1.94 sec: 1.24x slower                                                         |
| html5lib       | 38.9 ms                                                     | 40.5 ms: 1.04x slower                                                          |
| sphinx         | 633 ms                                                      | 798 ms: 1.26x slower                                                           |
| tornado_http   | 93.0 ms                                                     | 100 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                       | 1.15x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 262 ms: 1.10x faster                                                           |
| async_tree_none_tg         | 209 ms                                                      | 214 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 402 ms: 1.07x slower                                                           |
| async_tree_io              | 521 ms                                                      | 564 ms: 1.08x slower                                                           |
| coroutines                 | 12.8 ms                                                     | 14.1 ms: 1.11x slower                                                          |
| async_generators           | 223 ms                                                      | 265 ms: 1.19x slower                                                           |
| async_tree_io_tg           | 518 ms                                                      | 646 ms: 1.25x slower                                                           |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                                   |

Benchmark hidden because not significant (3): async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 57.3 ms: 1.19x faster                                                          |
| float          | 49.9 ms                                                     | 46.8 ms: 1.07x faster                                                          |
| pidigits       | 148 ms                                                      | 149 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.0 ms: 1.43x faster                                                          |
| regex_effbot   | 1.58 ms                                                     | 1.58 ms: 1.01x slower                                                          |
| regex_dna      | 115 ms                                                      | 118 ms: 1.02x slower                                                           |
| regex_compile  | 80.5 ms                                                     | 98.9 ms: 1.23x slower                                                          |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                          |
| tomli_loads          | 1.39 sec                                                    | 1.41 sec: 1.01x slower                                                         |
| xml_etree_parse      | 93.6 ms                                                     | 95.0 ms: 1.01x slower                                                          |
| xml_etree_generate   | 54.0 ms                                                     | 55.8 ms: 1.03x slower                                                          |
| xml_etree_iterparse  | 61.8 ms                                                     | 63.9 ms: 1.03x slower                                                          |
| xml_etree_process    | 37.0 ms                                                     | 40.7 ms: 1.10x slower                                                          |
| unpickle_pure_python | 133 us                                                      | 151 us: 1.13x slower                                                           |
| json_dumps           | 5.92 ms                                                     | 6.71 ms: 1.13x slower                                                          |
| pickle_pure_python   | 190 us                                                      | 219 us: 1.16x slower                                                           |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 24.8 ms: 1.03x faster                                                          |
| python_startup_no_site | 18.1 ms                                                     | 18.9 ms: 1.04x slower                                                          |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 5.60 ms: 1.13x faster                                                          |
| django_template | 22.4 ms                                                     | 28.8 ms: 1.29x slower                                                          |
| genshi_text     | 15.6 ms                                                     | 20.9 ms: 1.34x slower                                                          |
| genshi_xml      | 35.5 ms                                                     | 49.5 ms: 1.40x slower                                                          |
| Geometric mean  | (ref)                                                       | 1.21x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 529 us: 16.61x faster                                                          |
| regex_v8                   | 21.4 ms                                                     | 15.0 ms: 1.43x faster                                                          |
| deepcopy_memo              | 23.3 us                                                     | 17.6 us: 1.32x faster                                                          |
| nbody                      | 68.4 ms                                                     | 57.3 ms: 1.19x faster                                                          |
| mako                       | 6.35 ms                                                     | 5.60 ms: 1.13x faster                                                          |
| spectral_norm              | 62.8 ms                                                     | 56.3 ms: 1.12x faster                                                          |
| async_tree_memoization_tg  | 288 ms                                                      | 262 ms: 1.10x faster                                                           |
| deepcopy                   | 226 us                                                      | 210 us: 1.08x faster                                                           |
| float                      | 49.9 ms                                                     | 46.8 ms: 1.07x faster                                                          |
| scimark_sor                | 76.2 ms                                                     | 71.8 ms: 1.06x faster                                                          |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                          |
| dulwich_log                | 40.8 ms                                                     | 39.4 ms: 1.04x faster                                                          |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.38 ms: 1.03x faster                                                          |
| python_startup             | 25.4 ms                                                     | 24.8 ms: 1.03x faster                                                          |
| deepcopy_reduce            | 2.06 us                                                     | 2.03 us: 1.01x faster                                                          |
| pathlib                    | 80.9 ms                                                     | 80.2 ms: 1.01x faster                                                          |
| regex_effbot               | 1.58 ms                                                     | 1.58 ms: 1.01x slower                                                          |
| pidigits                   | 148 ms                                                      | 149 ms: 1.01x slower                                                           |
| tomli_loads                | 1.39 sec                                                    | 1.41 sec: 1.01x slower                                                         |
| xml_etree_parse            | 93.6 ms                                                     | 95.0 ms: 1.01x slower                                                          |
| scimark_fft                | 172 ms                                                      | 175 ms: 1.01x slower                                                           |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.02x slower                                                           |
| async_tree_none_tg         | 209 ms                                                      | 214 ms: 1.02x slower                                                           |
| telco                      | 4.79 ms                                                     | 4.90 ms: 1.02x slower                                                          |
| xml_etree_generate         | 54.0 ms                                                     | 55.8 ms: 1.03x slower                                                          |
| xml_etree_iterparse        | 61.8 ms                                                     | 63.9 ms: 1.03x slower                                                          |
| bench_mp_pool              | 86.4 ms                                                     | 89.7 ms: 1.04x slower                                                          |
| crypto_pyaes               | 45.4 ms                                                     | 47.2 ms: 1.04x slower                                                          |
| html5lib                   | 38.9 ms                                                     | 40.5 ms: 1.04x slower                                                          |
| python_startup_no_site     | 18.1 ms                                                     | 18.9 ms: 1.04x slower                                                          |
| logging_simple             | 5.96 us                                                     | 6.30 us: 1.06x slower                                                          |
| logging_format             | 6.26 us                                                     | 6.68 us: 1.07x slower                                                          |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 402 ms: 1.07x slower                                                           |
| tornado_http               | 93.0 ms                                                     | 100 ms: 1.08x slower                                                           |
| async_tree_io              | 521 ms                                                      | 564 ms: 1.08x slower                                                           |
| coverage                   | 45.6 ms                                                     | 49.6 ms: 1.09x slower                                                          |
| pprint_safe_repr           | 494 ms                                                      | 539 ms: 1.09x slower                                                           |
| xml_etree_process          | 37.0 ms                                                     | 40.7 ms: 1.10x slower                                                          |
| scimark_monte_carlo        | 40.8 ms                                                     | 45.0 ms: 1.10x slower                                                          |
| scimark_lu                 | 53.0 ms                                                     | 58.4 ms: 1.10x slower                                                          |
| create_gc_cycles           | 1.26 ms                                                     | 1.39 ms: 1.10x slower                                                          |
| pprint_pformat             | 999 ms                                                      | 1.10 sec: 1.10x slower                                                         |
| coroutines                 | 12.8 ms                                                     | 14.1 ms: 1.11x slower                                                          |
| pycparser                  | 683 ms                                                      | 758 ms: 1.11x slower                                                           |
| meteor_contest             | 73.5 ms                                                     | 81.9 ms: 1.11x slower                                                          |
| unpickle_pure_python       | 133 us                                                      | 151 us: 1.13x slower                                                           |
| json_dumps                 | 5.92 ms                                                     | 6.71 ms: 1.13x slower                                                          |
| pyflate                    | 283 ms                                                      | 324 ms: 1.14x slower                                                           |
| mdp                        | 1.39 sec                                                    | 1.59 sec: 1.15x slower                                                         |
| pickle_pure_python         | 190 us                                                      | 219 us: 1.16x slower                                                           |
| sympy_expand               | 291 ms                                                      | 337 ms: 1.16x slower                                                           |
| 2to3                       | 221 ms                                                      | 258 ms: 1.17x slower                                                           |
| typing_runtime_protocols   | 105 us                                                      | 123 us: 1.17x slower                                                           |
| go                         | 87.0 ms                                                     | 102 ms: 1.17x slower                                                           |
| sympy_str                  | 169 ms                                                      | 199 ms: 1.18x slower                                                           |
| async_generators           | 223 ms                                                      | 265 ms: 1.19x slower                                                           |
| generators                 | 19.5 ms                                                     | 23.7 ms: 1.22x slower                                                          |
| sqlglot_parse              | 771 us                                                      | 940 us: 1.22x slower                                                           |
| sympy_sum                  | 86.9 ms                                                     | 107 ms: 1.23x slower                                                           |
| regex_compile              | 80.5 ms                                                     | 98.9 ms: 1.23x slower                                                          |
| docutils                   | 1.57 sec                                                    | 1.94 sec: 1.24x slower                                                         |
| chaos                      | 38.5 ms                                                     | 47.8 ms: 1.24x slower                                                          |
| async_tree_io_tg           | 518 ms                                                      | 646 ms: 1.25x slower                                                           |
| sphinx                     | 633 ms                                                      | 798 ms: 1.26x slower                                                           |
| deltablue                  | 1.92 ms                                                     | 2.43 ms: 1.27x slower                                                          |
| logging_silent             | 54.6 ns                                                     | 69.4 ns: 1.27x slower                                                          |
| nqueens                    | 56.7 ms                                                     | 72.8 ms: 1.28x slower                                                          |
| django_template            | 22.4 ms                                                     | 28.8 ms: 1.29x slower                                                          |
| sqlglot_transpile          | 956 us                                                      | 1.25 ms: 1.30x slower                                                          |
| sqlglot_normalize          | 175 ms                                                      | 228 ms: 1.31x slower                                                           |
| comprehensions             | 10.3 us                                                     | 13.5 us: 1.32x slower                                                          |
| sympy_integrate            | 12.5 ms                                                     | 16.5 ms: 1.32x slower                                                          |
| genshi_text                | 15.6 ms                                                     | 20.9 ms: 1.34x slower                                                          |
| pylint                     | 211 ms                                                      | 287 ms: 1.36x slower                                                           |
| richards_super             | 30.9 ms                                                     | 42.5 ms: 1.38x slower                                                          |
| raytrace                   | 160 ms                                                      | 221 ms: 1.38x slower                                                           |
| genshi_xml                 | 35.5 ms                                                     | 49.5 ms: 1.40x slower                                                          |
| sqlglot_optimize           | 32.9 ms                                                     | 46.1 ms: 1.40x slower                                                          |
| richards                   | 27.3 ms                                                     | 38.6 ms: 1.41x slower                                                          |
| hexiom                     | 3.89 ms                                                     | 5.95 ms: 1.53x slower                                                          |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                                   |

Benchmark hidden because not significant (7): json, async_tree_none, gc_traversal, bench_thread_pool, fannkuch, async_tree_cpu_io_mixed, async_tree_memoization
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.060x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown