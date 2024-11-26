# Results vs. 3.13.0

- fork: python
- ref: faa3272fb8d63d481a13
- machine: windows-amd64
- commit hash: faa3272
- commit date: 2024-10-29
- overall geometric mean: 1.024x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 224 ms: 1.01x slower                                                        |
| docutils       | 1.57 sec                                                    | 1.71 sec: 1.09x slower                                                      |
| html5lib       | 38.9 ms                                                     | 40.1 ms: 1.03x slower                                                       |
| sphinx         | 633 ms                                                      | 668 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 258 ms: 1.12x faster                                                        |
| async_tree_none            | 226 ms                                                      | 220 ms: 1.03x faster                                                        |
| asyncio_websockets         | 318 ms                                                      | 312 ms: 1.02x faster                                                        |
| coroutines                 | 12.8 ms                                                     | 13.6 ms: 1.06x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 401 ms: 1.06x slower                                                        |
| async_generators           | 223 ms                                                      | 238 ms: 1.07x slower                                                        |
| async_tree_io              | 521 ms                                                      | 559 ms: 1.07x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 634 ms: 1.22x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 49.9 ms                                                     | 55.0 ms: 1.10x slower                                                       |
| nbody          | 68.4 ms                                                     | 76.9 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.2 ms: 1.41x faster                                                       |
| regex_effbot   | 1.58 ms                                                     | 1.55 ms: 1.01x faster                                                       |
| regex_dna      | 115 ms                                                      | 123 ms: 1.07x slower                                                        |
| regex_compile  | 80.5 ms                                                     | 90.6 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.7 us: 1.03x faster                                                       |
| xml_etree_parse      | 93.6 ms                                                     | 96.1 ms: 1.03x slower                                                       |
| xml_etree_generate   | 54.0 ms                                                     | 57.1 ms: 1.06x slower                                                       |
| xml_etree_iterparse  | 61.8 ms                                                     | 65.7 ms: 1.06x slower                                                       |
| xml_etree_process    | 37.0 ms                                                     | 40.2 ms: 1.09x slower                                                       |
| json_dumps           | 5.92 ms                                                     | 6.62 ms: 1.12x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 151 us: 1.13x slower                                                        |
| tomli_loads          | 1.39 sec                                                    | 1.58 sec: 1.13x slower                                                      |
| pickle_pure_python   | 190 us                                                      | 217 us: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 24.0 ms: 1.06x faster                                                       |
| python_startup_no_site | 18.1 ms                                                     | 17.9 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 6.64 ms: 1.05x slower                                                       |
| genshi_text     | 15.6 ms                                                     | 17.1 ms: 1.10x slower                                                       |
| django_template | 22.4 ms                                                     | 25.7 ms: 1.15x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.08x slower                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 518 us: 16.98x faster                                                       |
| regex_v8                   | 21.4 ms                                                     | 15.2 ms: 1.41x faster                                                       |
| deepcopy                   | 226 us                                                      | 187 us: 1.21x faster                                                        |
| deepcopy_memo              | 23.3 us                                                     | 19.5 us: 1.19x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 258 ms: 1.12x faster                                                        |
| python_startup             | 25.4 ms                                                     | 24.0 ms: 1.06x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 1.94 us: 1.06x faster                                                       |
| bench_thread_pool          | 847 us                                                      | 811 us: 1.04x faster                                                        |
| bench_mp_pool              | 86.4 ms                                                     | 83.1 ms: 1.04x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.7 us: 1.03x faster                                                       |
| connected_components       | 332 ms                                                      | 322 ms: 1.03x faster                                                        |
| pathlib                    | 80.9 ms                                                     | 78.6 ms: 1.03x faster                                                       |
| gc_traversal               | 1.97 ms                                                     | 1.91 ms: 1.03x faster                                                       |
| async_tree_none            | 226 ms                                                      | 220 ms: 1.03x faster                                                        |
| asyncio_websockets         | 318 ms                                                      | 312 ms: 1.02x faster                                                        |
| shortest_path              | 362 ms                                                      | 356 ms: 1.02x faster                                                        |
| python_startup_no_site     | 18.1 ms                                                     | 17.9 ms: 1.01x faster                                                       |
| regex_effbot               | 1.58 ms                                                     | 1.55 ms: 1.01x faster                                                       |
| coverage                   | 45.6 ms                                                     | 45.8 ms: 1.01x slower                                                       |
| 2to3                       | 221 ms                                                      | 224 ms: 1.01x slower                                                        |
| telco                      | 4.79 ms                                                     | 4.91 ms: 1.02x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 89.2 ms: 1.03x slower                                                       |
| xml_etree_parse            | 93.6 ms                                                     | 96.1 ms: 1.03x slower                                                       |
| html5lib                   | 38.9 ms                                                     | 40.1 ms: 1.03x slower                                                       |
| spectral_norm              | 62.8 ms                                                     | 64.7 ms: 1.03x slower                                                       |
| meteor_contest             | 73.5 ms                                                     | 75.8 ms: 1.03x slower                                                       |
| mdp                        | 1.39 sec                                                    | 1.43 sec: 1.03x slower                                                      |
| dulwich_log                | 40.8 ms                                                     | 42.5 ms: 1.04x slower                                                       |
| sympy_expand               | 291 ms                                                      | 304 ms: 1.04x slower                                                        |
| fannkuch                   | 253 ms                                                      | 265 ms: 1.04x slower                                                        |
| bpe_tokeniser              | 2.91 sec                                                    | 3.04 sec: 1.05x slower                                                      |
| mako                       | 6.35 ms                                                     | 6.64 ms: 1.05x slower                                                       |
| sympy_str                  | 169 ms                                                      | 177 ms: 1.05x slower                                                        |
| crypto_pyaes               | 45.4 ms                                                     | 47.9 ms: 1.05x slower                                                       |
| pycparser                  | 683 ms                                                      | 721 ms: 1.06x slower                                                        |
| sphinx                     | 633 ms                                                      | 668 ms: 1.06x slower                                                        |
| xml_etree_generate         | 54.0 ms                                                     | 57.1 ms: 1.06x slower                                                       |
| sympy_integrate            | 12.5 ms                                                     | 13.3 ms: 1.06x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 13.6 ms: 1.06x slower                                                       |
| xml_etree_iterparse        | 61.8 ms                                                     | 65.7 ms: 1.06x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 401 ms: 1.06x slower                                                        |
| typing_runtime_protocols   | 105 us                                                      | 112 us: 1.07x slower                                                        |
| regex_dna                  | 115 ms                                                      | 123 ms: 1.07x slower                                                        |
| async_generators           | 223 ms                                                      | 238 ms: 1.07x slower                                                        |
| logging_simple             | 5.96 us                                                     | 6.35 us: 1.07x slower                                                       |
| async_tree_io              | 521 ms                                                      | 559 ms: 1.07x slower                                                        |
| pprint_safe_repr           | 494 ms                                                      | 535 ms: 1.08x slower                                                        |
| xml_etree_process          | 37.0 ms                                                     | 40.2 ms: 1.09x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.71 sec: 1.09x slower                                                      |
| logging_format             | 6.26 us                                                     | 6.82 us: 1.09x slower                                                       |
| pprint_pformat             | 999 ms                                                      | 1.09 sec: 1.09x slower                                                      |
| create_gc_cycles           | 1.26 ms                                                     | 1.37 ms: 1.09x slower                                                       |
| genshi_text                | 15.6 ms                                                     | 17.1 ms: 1.10x slower                                                       |
| float                      | 49.9 ms                                                     | 55.0 ms: 1.10x slower                                                       |
| nqueens                    | 56.7 ms                                                     | 62.4 ms: 1.10x slower                                                       |
| pyflate                    | 283 ms                                                      | 315 ms: 1.11x slower                                                        |
| hexiom                     | 3.89 ms                                                     | 4.35 ms: 1.12x slower                                                       |
| json_dumps                 | 5.92 ms                                                     | 6.62 ms: 1.12x slower                                                       |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.75 ms: 1.12x slower                                                       |
| chaos                      | 38.5 ms                                                     | 43.3 ms: 1.12x slower                                                       |
| regex_compile              | 80.5 ms                                                     | 90.6 ms: 1.13x slower                                                       |
| nbody                      | 68.4 ms                                                     | 76.9 ms: 1.13x slower                                                       |
| sqlglot_optimize           | 32.9 ms                                                     | 37.2 ms: 1.13x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 151 us: 1.13x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 61.7 ns: 1.13x slower                                                       |
| generators                 | 19.5 ms                                                     | 22.0 ms: 1.13x slower                                                       |
| tomli_loads                | 1.39 sec                                                    | 1.58 sec: 1.13x slower                                                      |
| sqlglot_normalize          | 175 ms                                                      | 199 ms: 1.14x slower                                                        |
| scimark_fft                | 172 ms                                                      | 196 ms: 1.14x slower                                                        |
| pickle_pure_python         | 190 us                                                      | 217 us: 1.14x slower                                                        |
| scimark_monte_carlo        | 40.8 ms                                                     | 46.7 ms: 1.15x slower                                                       |
| django_template            | 22.4 ms                                                     | 25.7 ms: 1.15x slower                                                       |
| comprehensions             | 10.3 us                                                     | 11.8 us: 1.15x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 88.0 ms: 1.16x slower                                                       |
| scimark_lu                 | 53.0 ms                                                     | 61.3 ms: 1.16x slower                                                       |
| sqlglot_transpile          | 956 us                                                      | 1.12 ms: 1.17x slower                                                       |
| sqlglot_parse              | 771 us                                                      | 910 us: 1.18x slower                                                        |
| richards                   | 27.3 ms                                                     | 32.3 ms: 1.18x slower                                                       |
| richards_super             | 30.9 ms                                                     | 36.6 ms: 1.19x slower                                                       |
| deltablue                  | 1.92 ms                                                     | 2.31 ms: 1.20x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 634 ms: 1.22x slower                                                        |
| raytrace                   | 160 ms                                                      | 198 ms: 1.23x slower                                                        |
| k_core                     | 1.74 sec                                                    | 2.52 sec: 1.45x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (9): json, pidigits, go, tornado_http, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_memoization, genshi_xml, pylint
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20241029-3.14.0a1+-faa3272/bm-20241029-pythonperf1-amd64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272.json: sqlite_synth

- Geometric mean (including insignificant results): 1.024x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown