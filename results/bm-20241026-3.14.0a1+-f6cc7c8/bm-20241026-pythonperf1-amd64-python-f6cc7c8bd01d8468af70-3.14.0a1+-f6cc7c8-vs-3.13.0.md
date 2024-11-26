# Results vs. 3.13.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: windows-amd64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.037x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 230 ms: 1.04x slower                                                        |
| docutils       | 1.57 sec                                                    | 1.72 sec: 1.10x slower                                                      |
| html5lib       | 38.9 ms                                                     | 42.0 ms: 1.08x slower                                                       |
| sphinx         | 633 ms                                                      | 674 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 260 ms: 1.11x faster                                                        |
| async_tree_none            | 226 ms                                                      | 218 ms: 1.04x faster                                                        |
| async_generators           | 223 ms                                                      | 242 ms: 1.08x slower                                                        |
| async_tree_io              | 521 ms                                                      | 564 ms: 1.08x slower                                                        |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 410 ms: 1.09x slower                                                        |
| coroutines                 | 12.8 ms                                                     | 14.1 ms: 1.10x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 644 ms: 1.24x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                                |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 49.9 ms                                                     | 54.9 ms: 1.10x slower                                                       |
| nbody          | 68.4 ms                                                     | 78.1 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                       | 1.08x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.8 ms: 1.36x faster                                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| regex_compile  | 80.5 ms                                                     | 91.6 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.6 ms                                                     | 96.9 ms: 1.04x slower                                                       |
| xml_etree_generate   | 54.0 ms                                                     | 57.8 ms: 1.07x slower                                                       |
| xml_etree_iterparse  | 61.8 ms                                                     | 66.7 ms: 1.08x slower                                                       |
| xml_etree_process    | 37.0 ms                                                     | 40.3 ms: 1.09x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 150 us: 1.12x slower                                                        |
| tomli_loads          | 1.39 sec                                                    | 1.60 sec: 1.15x slower                                                      |
| json_dumps           | 5.92 ms                                                     | 6.84 ms: 1.16x slower                                                       |
| pickle_pure_python   | 190 us                                                      | 223 us: 1.18x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 24.1 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 35.5 ms                                                     | 37.9 ms: 1.07x slower                                                       |
| mako            | 6.35 ms                                                     | 6.82 ms: 1.07x slower                                                       |
| django_template | 22.4 ms                                                     | 25.5 ms: 1.14x slower                                                       |
| genshi_text     | 15.6 ms                                                     | 17.8 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 538 us: 16.36x faster                                                       |
| regex_v8                   | 21.4 ms                                                     | 15.8 ms: 1.36x faster                                                       |
| deepcopy                   | 226 us                                                      | 193 us: 1.17x faster                                                        |
| deepcopy_memo              | 23.3 us                                                     | 20.1 us: 1.16x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 260 ms: 1.11x faster                                                        |
| deepcopy_reduce            | 2.06 us                                                     | 1.94 us: 1.06x faster                                                       |
| python_startup             | 25.4 ms                                                     | 24.1 ms: 1.05x faster                                                       |
| async_tree_none            | 226 ms                                                      | 218 ms: 1.04x faster                                                        |
| bench_mp_pool              | 86.4 ms                                                     | 84.6 ms: 1.02x faster                                                       |
| gc_traversal               | 1.97 ms                                                     | 1.93 ms: 1.02x faster                                                       |
| go                         | 87.0 ms                                                     | 88.0 ms: 1.01x slower                                                       |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| telco                      | 4.79 ms                                                     | 4.87 ms: 1.02x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 89.7 ms: 1.03x slower                                                       |
| xml_etree_parse            | 93.6 ms                                                     | 96.9 ms: 1.04x slower                                                       |
| 2to3                       | 221 ms                                                      | 230 ms: 1.04x slower                                                        |
| meteor_contest             | 73.5 ms                                                     | 76.8 ms: 1.04x slower                                                       |
| sympy_expand               | 291 ms                                                      | 306 ms: 1.05x slower                                                        |
| sympy_str                  | 169 ms                                                      | 179 ms: 1.06x slower                                                        |
| sphinx                     | 633 ms                                                      | 674 ms: 1.07x slower                                                        |
| typing_runtime_protocols   | 105 us                                                      | 112 us: 1.07x slower                                                        |
| genshi_xml                 | 35.5 ms                                                     | 37.9 ms: 1.07x slower                                                       |
| xml_etree_generate         | 54.0 ms                                                     | 57.8 ms: 1.07x slower                                                       |
| dulwich_log                | 40.8 ms                                                     | 43.7 ms: 1.07x slower                                                       |
| mako                       | 6.35 ms                                                     | 6.82 ms: 1.07x slower                                                       |
| pycparser                  | 683 ms                                                      | 734 ms: 1.08x slower                                                        |
| sympy_integrate            | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                       |
| xml_etree_iterparse        | 61.8 ms                                                     | 66.7 ms: 1.08x slower                                                       |
| html5lib                   | 38.9 ms                                                     | 42.0 ms: 1.08x slower                                                       |
| crypto_pyaes               | 45.4 ms                                                     | 49.1 ms: 1.08x slower                                                       |
| async_generators           | 223 ms                                                      | 242 ms: 1.08x slower                                                        |
| coverage                   | 45.6 ms                                                     | 49.3 ms: 1.08x slower                                                       |
| async_tree_io              | 521 ms                                                      | 564 ms: 1.08x slower                                                        |
| pylint                     | 211 ms                                                      | 229 ms: 1.09x slower                                                        |
| spectral_norm              | 62.8 ms                                                     | 68.3 ms: 1.09x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 410 ms: 1.09x slower                                                        |
| xml_etree_process          | 37.0 ms                                                     | 40.3 ms: 1.09x slower                                                       |
| logging_simple             | 5.96 us                                                     | 6.51 us: 1.09x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.72 sec: 1.10x slower                                                      |
| float                      | 49.9 ms                                                     | 54.9 ms: 1.10x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.1 ms: 1.10x slower                                                       |
| create_gc_cycles           | 1.26 ms                                                     | 1.40 ms: 1.11x slower                                                       |
| logging_format             | 6.26 us                                                     | 6.95 us: 1.11x slower                                                       |
| generators                 | 19.5 ms                                                     | 21.7 ms: 1.11x slower                                                       |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.73 ms: 1.11x slower                                                       |
| nqueens                    | 56.7 ms                                                     | 63.2 ms: 1.12x slower                                                       |
| fannkuch                   | 253 ms                                                      | 283 ms: 1.12x slower                                                        |
| sqlglot_optimize           | 32.9 ms                                                     | 36.9 ms: 1.12x slower                                                       |
| mdp                        | 1.39 sec                                                    | 1.56 sec: 1.12x slower                                                      |
| pprint_pformat             | 999 ms                                                      | 1.12 sec: 1.12x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 150 us: 1.12x slower                                                        |
| hexiom                     | 3.89 ms                                                     | 4.40 ms: 1.13x slower                                                       |
| sqlglot_normalize          | 175 ms                                                      | 199 ms: 1.14x slower                                                        |
| chaos                      | 38.5 ms                                                     | 43.8 ms: 1.14x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 62.2 ns: 1.14x slower                                                       |
| regex_compile              | 80.5 ms                                                     | 91.6 ms: 1.14x slower                                                       |
| django_template            | 22.4 ms                                                     | 25.5 ms: 1.14x slower                                                       |
| pprint_safe_repr           | 494 ms                                                      | 562 ms: 1.14x slower                                                        |
| pyflate                    | 283 ms                                                      | 323 ms: 1.14x slower                                                        |
| nbody                      | 68.4 ms                                                     | 78.1 ms: 1.14x slower                                                       |
| genshi_text                | 15.6 ms                                                     | 17.8 ms: 1.14x slower                                                       |
| tomli_loads                | 1.39 sec                                                    | 1.60 sec: 1.15x slower                                                      |
| scimark_monte_carlo        | 40.8 ms                                                     | 47.1 ms: 1.15x slower                                                       |
| scimark_lu                 | 53.0 ms                                                     | 61.2 ms: 1.15x slower                                                       |
| json_dumps                 | 5.92 ms                                                     | 6.84 ms: 1.16x slower                                                       |
| richards_super             | 30.9 ms                                                     | 35.8 ms: 1.16x slower                                                       |
| pickle_pure_python         | 190 us                                                      | 223 us: 1.18x slower                                                        |
| richards                   | 27.3 ms                                                     | 32.2 ms: 1.18x slower                                                       |
| deltablue                  | 1.92 ms                                                     | 2.27 ms: 1.18x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 90.6 ms: 1.19x slower                                                       |
| sqlglot_transpile          | 956 us                                                      | 1.14 ms: 1.19x slower                                                       |
| sqlglot_parse              | 771 us                                                      | 922 us: 1.20x slower                                                        |
| scimark_fft                | 172 ms                                                      | 209 ms: 1.21x slower                                                        |
| comprehensions             | 10.3 us                                                     | 12.5 us: 1.22x slower                                                       |
| raytrace                   | 160 ms                                                      | 196 ms: 1.23x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 644 ms: 1.24x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (11): pathlib, regex_effbot, python_startup_no_site, tornado_http, json, pidigits, bench_thread_pool, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg, json_loads
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.037x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown