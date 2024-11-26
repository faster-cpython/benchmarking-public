# Results vs. 3.13.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: windows-amd64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.012x slower
- HPT reliability: 99.90%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 250 ms: 1.13x slower                                                        |
| docutils       | 1.57 sec                                                    | 1.92 sec: 1.22x slower                                                      |
| sphinx         | 633 ms                                                      | 767 ms: 1.21x slower                                                        |
| tornado_http   | 93.0 ms                                                     | 98.7 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.12x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 262 ms: 1.10x faster                                                        |
| async_tree_memoization     | 276 ms                                                      | 266 ms: 1.04x faster                                                        |
| async_tree_none            | 226 ms                                                      | 219 ms: 1.03x faster                                                        |
| async_tree_io              | 521 ms                                                      | 539 ms: 1.03x slower                                                        |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 396 ms: 1.04x slower                                                        |
| async_tree_none_tg         | 209 ms                                                      | 221 ms: 1.06x slower                                                        |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 403 ms: 1.07x slower                                                        |
| coroutines                 | 12.8 ms                                                     | 14.4 ms: 1.13x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 604 ms: 1.17x slower                                                        |
| async_generators           | 223 ms                                                      | 267 ms: 1.19x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 53.7 ms: 1.27x faster                                                       |
| float          | 49.9 ms                                                     | 47.4 ms: 1.05x faster                                                       |
| pidigits       | 148 ms                                                      | 149 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.5 ms: 1.38x faster                                                       |
| regex_effbot   | 1.58 ms                                                     | 1.63 ms: 1.03x slower                                                       |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| regex_compile  | 80.5 ms                                                     | 91.5 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                    | 1.28 sec: 1.09x faster                                                      |
| xml_etree_generate   | 54.0 ms                                                     | 50.5 ms: 1.07x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.6 us: 1.04x faster                                                       |
| xml_etree_process    | 37.0 ms                                                     | 36.2 ms: 1.02x faster                                                       |
| xml_etree_iterparse  | 61.8 ms                                                     | 63.1 ms: 1.02x slower                                                       |
| xml_etree_parse      | 93.6 ms                                                     | 95.9 ms: 1.03x slower                                                       |
| json_dumps           | 5.92 ms                                                     | 6.18 ms: 1.04x slower                                                       |
| pickle_pure_python   | 190 us                                                      | 204 us: 1.08x slower                                                        |
| unpickle_pure_python | 133 us                                                      | 144 us: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 24.3 ms: 1.05x faster                                                       |
| python_startup_no_site | 18.1 ms                                                     | 18.4 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 5.06 ms: 1.26x faster                                                       |
| django_template | 22.4 ms                                                     | 27.0 ms: 1.21x slower                                                       |
| genshi_text     | 15.6 ms                                                     | 19.2 ms: 1.23x slower                                                       |
| genshi_xml      | 35.5 ms                                                     | 46.3 ms: 1.30x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 532 us: 16.55x faster                                                       |
| deepcopy_memo              | 23.3 us                                                     | 16.8 us: 1.39x faster                                                       |
| regex_v8                   | 21.4 ms                                                     | 15.5 ms: 1.38x faster                                                       |
| nbody                      | 68.4 ms                                                     | 53.7 ms: 1.27x faster                                                       |
| mako                       | 6.35 ms                                                     | 5.06 ms: 1.26x faster                                                       |
| deepcopy                   | 226 us                                                      | 190 us: 1.19x faster                                                        |
| scimark_sor                | 76.2 ms                                                     | 64.9 ms: 1.17x faster                                                       |
| crypto_pyaes               | 45.4 ms                                                     | 40.5 ms: 1.12x faster                                                       |
| scimark_fft                | 172 ms                                                      | 155 ms: 1.11x faster                                                        |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.23 ms: 1.10x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 262 ms: 1.10x faster                                                        |
| scimark_monte_carlo        | 40.8 ms                                                     | 37.2 ms: 1.10x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 1.88 us: 1.10x faster                                                       |
| json                       | 3.19 ms                                                     | 2.92 ms: 1.09x faster                                                       |
| spectral_norm              | 62.8 ms                                                     | 57.6 ms: 1.09x faster                                                       |
| tomli_loads                | 1.39 sec                                                    | 1.28 sec: 1.09x faster                                                      |
| xml_etree_generate         | 54.0 ms                                                     | 50.5 ms: 1.07x faster                                                       |
| telco                      | 4.79 ms                                                     | 4.53 ms: 1.06x faster                                                       |
| fannkuch                   | 253 ms                                                      | 240 ms: 1.06x faster                                                        |
| pprint_safe_repr           | 494 ms                                                      | 468 ms: 1.06x faster                                                        |
| float                      | 49.9 ms                                                     | 47.4 ms: 1.05x faster                                                       |
| pprint_pformat             | 999 ms                                                      | 950 ms: 1.05x faster                                                        |
| python_startup             | 25.4 ms                                                     | 24.3 ms: 1.05x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.6 us: 1.04x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 266 ms: 1.04x faster                                                        |
| async_tree_none            | 226 ms                                                      | 219 ms: 1.03x faster                                                        |
| xml_etree_process          | 37.0 ms                                                     | 36.2 ms: 1.02x faster                                                       |
| gc_traversal               | 1.97 ms                                                     | 1.95 ms: 1.01x faster                                                       |
| dulwich_log                | 40.8 ms                                                     | 40.4 ms: 1.01x faster                                                       |
| pidigits                   | 148 ms                                                      | 149 ms: 1.01x slower                                                        |
| python_startup_no_site     | 18.1 ms                                                     | 18.4 ms: 1.01x slower                                                       |
| meteor_contest             | 73.5 ms                                                     | 74.7 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 61.8 ms                                                     | 63.1 ms: 1.02x slower                                                       |
| xml_etree_parse            | 93.6 ms                                                     | 95.9 ms: 1.03x slower                                                       |
| pyflate                    | 283 ms                                                      | 292 ms: 1.03x slower                                                        |
| regex_effbot               | 1.58 ms                                                     | 1.63 ms: 1.03x slower                                                       |
| bench_mp_pool              | 86.4 ms                                                     | 89.3 ms: 1.03x slower                                                       |
| async_tree_io              | 521 ms                                                      | 539 ms: 1.03x slower                                                        |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 396 ms: 1.04x slower                                                        |
| json_dumps                 | 5.92 ms                                                     | 6.18 ms: 1.04x slower                                                       |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| go                         | 87.0 ms                                                     | 91.8 ms: 1.06x slower                                                       |
| logging_simple             | 5.96 us                                                     | 6.30 us: 1.06x slower                                                       |
| async_tree_none_tg         | 209 ms                                                      | 221 ms: 1.06x slower                                                        |
| logging_format             | 6.26 us                                                     | 6.63 us: 1.06x slower                                                       |
| scimark_lu                 | 53.0 ms                                                     | 56.2 ms: 1.06x slower                                                       |
| tornado_http               | 93.0 ms                                                     | 98.7 ms: 1.06x slower                                                       |
| chaos                      | 38.5 ms                                                     | 40.9 ms: 1.06x slower                                                       |
| pycparser                  | 683 ms                                                      | 727 ms: 1.06x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 58.4 ns: 1.07x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 403 ms: 1.07x slower                                                        |
| coverage                   | 45.6 ms                                                     | 49.0 ms: 1.08x slower                                                       |
| pickle_pure_python         | 190 us                                                      | 204 us: 1.08x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 144 us: 1.08x slower                                                        |
| typing_runtime_protocols   | 105 us                                                      | 116 us: 1.10x slower                                                        |
| create_gc_cycles           | 1.26 ms                                                     | 1.41 ms: 1.12x slower                                                       |
| sympy_expand               | 291 ms                                                      | 326 ms: 1.12x slower                                                        |
| coroutines                 | 12.8 ms                                                     | 14.4 ms: 1.13x slower                                                       |
| 2to3                       | 221 ms                                                      | 250 ms: 1.13x slower                                                        |
| nqueens                    | 56.7 ms                                                     | 64.1 ms: 1.13x slower                                                       |
| sympy_str                  | 169 ms                                                      | 191 ms: 1.13x slower                                                        |
| regex_compile              | 80.5 ms                                                     | 91.5 ms: 1.14x slower                                                       |
| comprehensions             | 10.3 us                                                     | 11.7 us: 1.14x slower                                                       |
| sqlglot_parse              | 771 us                                                      | 886 us: 1.15x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 604 ms: 1.17x slower                                                        |
| mdp                        | 1.39 sec                                                    | 1.63 sec: 1.17x slower                                                      |
| generators                 | 19.5 ms                                                     | 22.9 ms: 1.17x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 103 ms: 1.18x slower                                                        |
| async_generators           | 223 ms                                                      | 267 ms: 1.19x slower                                                        |
| sqlglot_normalize          | 175 ms                                                      | 210 ms: 1.20x slower                                                        |
| django_template            | 22.4 ms                                                     | 27.0 ms: 1.21x slower                                                       |
| sphinx                     | 633 ms                                                      | 767 ms: 1.21x slower                                                        |
| deltablue                  | 1.92 ms                                                     | 2.34 ms: 1.22x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.92 sec: 1.22x slower                                                      |
| genshi_text                | 15.6 ms                                                     | 19.2 ms: 1.23x slower                                                       |
| sqlglot_transpile          | 956 us                                                      | 1.18 ms: 1.23x slower                                                       |
| richards_super             | 30.9 ms                                                     | 38.5 ms: 1.25x slower                                                       |
| sympy_integrate            | 12.5 ms                                                     | 15.7 ms: 1.26x slower                                                       |
| richards                   | 27.3 ms                                                     | 34.4 ms: 1.26x slower                                                       |
| raytrace                   | 160 ms                                                      | 208 ms: 1.30x slower                                                        |
| sqlglot_optimize           | 32.9 ms                                                     | 42.9 ms: 1.30x slower                                                       |
| genshi_xml                 | 35.5 ms                                                     | 46.3 ms: 1.30x slower                                                       |
| pylint                     | 211 ms                                                      | 281 ms: 1.33x slower                                                        |
| hexiom                     | 3.89 ms                                                     | 5.26 ms: 1.35x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (3): bench_thread_pool, html5lib, pathlib
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.012x slower
# HPT report

- Reliability score: 99.90% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown