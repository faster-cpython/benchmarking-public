# Results vs. 3.13.0

- fork: python
- ref: ded105a62b9d78717f8d
- machine: windows-amd64
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.011x slower
- HPT reliability: 99.84%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 250 ms: 1.13x slower                                                        |
| docutils       | 1.57 sec                                                    | 1.89 sec: 1.21x slower                                                      |
| sphinx         | 633 ms                                                      | 769 ms: 1.22x slower                                                        |
| tornado_http   | 93.0 ms                                                     | 99.5 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.12x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 263 ms: 1.10x faster                                                        |
| async_tree_none            | 226 ms                                                      | 218 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 400 ms: 1.06x slower                                                        |
| async_tree_io              | 521 ms                                                      | 564 ms: 1.08x slower                                                        |
| coroutines                 | 12.8 ms                                                     | 15.0 ms: 1.18x slower                                                       |
| async_generators           | 223 ms                                                      | 268 ms: 1.20x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 634 ms: 1.22x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                                |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 54.3 ms: 1.26x faster                                                       |
| float          | 49.9 ms                                                     | 48.0 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.2 ms: 1.41x faster                                                       |
| regex_dna      | 115 ms                                                      | 122 ms: 1.06x slower                                                        |
| regex_compile  | 80.5 ms                                                     | 91.9 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                    | 1.29 sec: 1.08x faster                                                      |
| xml_etree_generate   | 54.0 ms                                                     | 51.1 ms: 1.06x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.5 us: 1.04x faster                                                       |
| xml_etree_process    | 37.0 ms                                                     | 36.4 ms: 1.02x faster                                                       |
| xml_etree_parse      | 93.6 ms                                                     | 94.6 ms: 1.01x slower                                                       |
| xml_etree_iterparse  | 61.8 ms                                                     | 63.3 ms: 1.02x slower                                                       |
| pickle_pure_python   | 190 us                                                      | 199 us: 1.05x slower                                                        |
| json_dumps           | 5.92 ms                                                     | 6.24 ms: 1.05x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 147 us: 1.10x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 25.1 ms: 1.01x faster                                                       |
| python_startup_no_site | 18.1 ms                                                     | 19.2 ms: 1.06x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 4.97 ms: 1.28x faster                                                       |
| django_template | 22.4 ms                                                     | 26.4 ms: 1.18x slower                                                       |
| genshi_text     | 15.6 ms                                                     | 19.8 ms: 1.27x slower                                                       |
| genshi_xml      | 35.5 ms                                                     | 46.2 ms: 1.30x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 528 us: 16.65x faster                                                       |
| regex_v8                   | 21.4 ms                                                     | 15.2 ms: 1.41x faster                                                       |
| deepcopy_memo              | 23.3 us                                                     | 17.1 us: 1.36x faster                                                       |
| mako                       | 6.35 ms                                                     | 4.97 ms: 1.28x faster                                                       |
| nbody                      | 68.4 ms                                                     | 54.3 ms: 1.26x faster                                                       |
| deepcopy                   | 226 us                                                      | 187 us: 1.21x faster                                                        |
| scimark_sor                | 76.2 ms                                                     | 64.2 ms: 1.19x faster                                                       |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.10 ms: 1.17x faster                                                       |
| crypto_pyaes               | 45.4 ms                                                     | 39.9 ms: 1.14x faster                                                       |
| spectral_norm              | 62.8 ms                                                     | 55.6 ms: 1.13x faster                                                       |
| scimark_fft                | 172 ms                                                      | 154 ms: 1.12x faster                                                        |
| scimark_monte_carlo        | 40.8 ms                                                     | 36.8 ms: 1.11x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 1.86 us: 1.11x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 263 ms: 1.10x faster                                                        |
| pprint_safe_repr           | 494 ms                                                      | 450 ms: 1.10x faster                                                        |
| fannkuch                   | 253 ms                                                      | 232 ms: 1.09x faster                                                        |
| json                       | 3.19 ms                                                     | 2.94 ms: 1.08x faster                                                       |
| tomli_loads                | 1.39 sec                                                    | 1.29 sec: 1.08x faster                                                      |
| xml_etree_generate         | 54.0 ms                                                     | 51.1 ms: 1.06x faster                                                       |
| pprint_pformat             | 999 ms                                                      | 949 ms: 1.05x faster                                                        |
| json_loads                 | 15.1 us                                                     | 14.5 us: 1.04x faster                                                       |
| float                      | 49.9 ms                                                     | 48.0 ms: 1.04x faster                                                       |
| async_tree_none            | 226 ms                                                      | 218 ms: 1.03x faster                                                        |
| telco                      | 4.79 ms                                                     | 4.64 ms: 1.03x faster                                                       |
| xml_etree_process          | 37.0 ms                                                     | 36.4 ms: 1.02x faster                                                       |
| python_startup             | 25.4 ms                                                     | 25.1 ms: 1.01x faster                                                       |
| gc_traversal               | 1.97 ms                                                     | 1.94 ms: 1.01x faster                                                       |
| xml_etree_parse            | 93.6 ms                                                     | 94.6 ms: 1.01x slower                                                       |
| pyflate                    | 283 ms                                                      | 288 ms: 1.02x slower                                                        |
| xml_etree_iterparse        | 61.8 ms                                                     | 63.3 ms: 1.02x slower                                                       |
| meteor_contest             | 73.5 ms                                                     | 76.1 ms: 1.04x slower                                                       |
| scimark_lu                 | 53.0 ms                                                     | 55.0 ms: 1.04x slower                                                       |
| logging_simple             | 5.96 us                                                     | 6.20 us: 1.04x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 57.3 ns: 1.05x slower                                                       |
| pickle_pure_python         | 190 us                                                      | 199 us: 1.05x slower                                                        |
| go                         | 87.0 ms                                                     | 91.7 ms: 1.05x slower                                                       |
| bench_mp_pool              | 86.4 ms                                                     | 91.1 ms: 1.05x slower                                                       |
| json_dumps                 | 5.92 ms                                                     | 6.24 ms: 1.05x slower                                                       |
| python_startup_no_site     | 18.1 ms                                                     | 19.2 ms: 1.06x slower                                                       |
| regex_dna                  | 115 ms                                                      | 122 ms: 1.06x slower                                                        |
| logging_format             | 6.26 us                                                     | 6.63 us: 1.06x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 400 ms: 1.06x slower                                                        |
| tornado_http               | 93.0 ms                                                     | 99.5 ms: 1.07x slower                                                       |
| pycparser                  | 683 ms                                                      | 730 ms: 1.07x slower                                                        |
| chaos                      | 38.5 ms                                                     | 41.5 ms: 1.08x slower                                                       |
| async_tree_io              | 521 ms                                                      | 564 ms: 1.08x slower                                                        |
| coverage                   | 45.6 ms                                                     | 49.3 ms: 1.08x slower                                                       |
| nqueens                    | 56.7 ms                                                     | 62.5 ms: 1.10x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 147 us: 1.10x slower                                                        |
| typing_runtime_protocols   | 105 us                                                      | 117 us: 1.11x slower                                                        |
| sympy_expand               | 291 ms                                                      | 326 ms: 1.12x slower                                                        |
| create_gc_cycles           | 1.26 ms                                                     | 1.41 ms: 1.12x slower                                                       |
| 2to3                       | 221 ms                                                      | 250 ms: 1.13x slower                                                        |
| comprehensions             | 10.3 us                                                     | 11.6 us: 1.14x slower                                                       |
| sympy_str                  | 169 ms                                                      | 192 ms: 1.14x slower                                                        |
| regex_compile              | 80.5 ms                                                     | 91.9 ms: 1.14x slower                                                       |
| mdp                        | 1.39 sec                                                    | 1.61 sec: 1.16x slower                                                      |
| sqlglot_parse              | 771 us                                                      | 902 us: 1.17x slower                                                        |
| coroutines                 | 12.8 ms                                                     | 15.0 ms: 1.18x slower                                                       |
| django_template            | 22.4 ms                                                     | 26.4 ms: 1.18x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 103 ms: 1.19x slower                                                        |
| sqlglot_normalize          | 175 ms                                                      | 210 ms: 1.20x slower                                                        |
| async_generators           | 223 ms                                                      | 268 ms: 1.20x slower                                                        |
| docutils                   | 1.57 sec                                                    | 1.89 sec: 1.21x slower                                                      |
| deltablue                  | 1.92 ms                                                     | 2.32 ms: 1.21x slower                                                       |
| sphinx                     | 633 ms                                                      | 769 ms: 1.22x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 634 ms: 1.22x slower                                                        |
| generators                 | 19.5 ms                                                     | 24.2 ms: 1.24x slower                                                       |
| sqlglot_transpile          | 956 us                                                      | 1.19 ms: 1.25x slower                                                       |
| richards_super             | 30.9 ms                                                     | 38.6 ms: 1.25x slower                                                       |
| richards                   | 27.3 ms                                                     | 34.2 ms: 1.25x slower                                                       |
| sympy_integrate            | 12.5 ms                                                     | 15.8 ms: 1.26x slower                                                       |
| genshi_text                | 15.6 ms                                                     | 19.8 ms: 1.27x slower                                                       |
| sqlglot_optimize           | 32.9 ms                                                     | 42.7 ms: 1.30x slower                                                       |
| genshi_xml                 | 35.5 ms                                                     | 46.2 ms: 1.30x slower                                                       |
| raytrace                   | 160 ms                                                      | 212 ms: 1.33x slower                                                        |
| hexiom                     | 3.89 ms                                                     | 5.17 ms: 1.33x slower                                                       |
| pylint                     | 211 ms                                                      | 281 ms: 1.33x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (9): pathlib, bench_thread_pool, pidigits, regex_effbot, async_tree_none_tg, async_tree_cpu_io_mixed, dulwich_log, html5lib, async_tree_memoization
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.011x slower
# HPT report

- Reliability score: 99.84% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown