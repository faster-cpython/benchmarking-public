# Results vs. 3.13.0

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: windows-amd64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.022x slower
- HPT reliability: 99.81%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 217 ms: 1.01x slower                                                        |
| docutils       | 1.53 sec                                                    | 2.72 sec: 1.78x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.2 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.17x slower                                                                |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 137 ms: 2.19x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 316 ms: 1.57x faster                                                        |
| async_tree_io              | 513 ms                                                      | 336 ms: 1.53x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 186 ms: 1.51x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 144 ms: 1.39x faster                                                        |
| async_tree_none            | 219 ms                                                      | 163 ms: 1.34x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 208 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 309 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.15x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                       |
| async_generators           | 223 ms                                                      | 262 ms: 1.18x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.31x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.0 ms: 1.13x faster                                                       |
| pidigits       | 146 ms                                                      | 134 ms: 1.09x faster                                                        |
| nbody          | 66.3 ms                                                     | 76.9 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.1 ms: 1.82x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.57 ms: 1.08x faster                                                       |
| regex_dna      | 115 ms                                                      | 111 ms: 1.03x faster                                                        |
| regex_compile  | 80.7 ms                                                     | 88.6 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 87.2 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 57.7 ms: 1.05x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 5.95 ms: 1.04x faster                                                       |
| json_loads           | 15.1 us                                                     | 15.8 us: 1.04x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 60.1 ms: 1.12x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 148 us: 1.14x slower                                                        |
| xml_etree_process    | 36.5 ms                                                     | 42.5 ms: 1.16x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 225 us: 1.21x slower                                                        |
| tomli_loads          | 1.37 sec                                                    | 2.17 sec: 1.58x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.11x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.2 ms: 1.03x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 18.9 ms: 1.12x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 37.6 ms: 1.11x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 18.4 ms: 1.21x slower                                                       |
| django_template | 20.3 ms                                                     | 26.0 ms: 1.28x slower                                                       |
| mako            | 6.56 ms                                                     | 9.63 ms: 1.47x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.26x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 555 us: 15.26x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 29.0 ms: 2.60x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 137 ms: 2.19x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 13.1 ms: 1.82x faster                                                       |
| gc_traversal               | 1.96 ms                                                     | 1.22 ms: 1.61x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 316 ms: 1.57x faster                                                        |
| async_tree_io              | 513 ms                                                      | 336 ms: 1.53x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 186 ms: 1.51x faster                                                        |
| mdp                        | 1.43 sec                                                    | 1.01 sec: 1.42x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 144 ms: 1.39x faster                                                        |
| async_tree_none            | 219 ms                                                      | 163 ms: 1.34x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 208 ms: 1.27x faster                                                        |
| deepcopy                   | 223 us                                                      | 179 us: 1.24x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 18.6 us: 1.24x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 309 ms: 1.24x faster                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.34 us: 1.18x faster                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 72.7 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.15x faster                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.07 ms: 1.15x faster                                                       |
| float                      | 50.8 ms                                                     | 45.0 ms: 1.13x faster                                                       |
| json                       | 3.30 ms                                                     | 3.00 ms: 1.10x faster                                                       |
| pidigits                   | 146 ms                                                      | 134 ms: 1.09x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.57 ms: 1.08x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 87.2 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 57.7 ms: 1.05x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.95 ms: 1.04x faster                                                       |
| regex_dna                  | 115 ms                                                      | 111 ms: 1.03x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.98 us: 1.02x faster                                                       |
| 2to3                       | 215 ms                                                      | 217 ms: 1.01x slower                                                        |
| telco                      | 4.85 ms                                                     | 4.91 ms: 1.01x slower                                                       |
| go                         | 84.7 ms                                                     | 86.2 ms: 1.02x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.2 ms: 1.03x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.2 ms: 1.03x slower                                                       |
| json_loads                 | 15.1 us                                                     | 15.8 us: 1.04x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 58.0 ns: 1.06x slower                                                       |
| pyflate                    | 283 ms                                                      | 302 ms: 1.07x slower                                                        |
| sympy_expand               | 286 ms                                                      | 305 ms: 1.07x slower                                                        |
| sympy_str                  | 167 ms                                                      | 178 ms: 1.07x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 91.2 ms: 1.07x slower                                                       |
| scimark_fft                | 175 ms                                                      | 188 ms: 1.07x slower                                                        |
| spectral_norm              | 63.4 ms                                                     | 68.6 ms: 1.08x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.4 ms: 1.09x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 83.4 ms: 1.09x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 88.6 ms: 1.10x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 534 ms: 1.10x slower                                                        |
| logging_simple             | 5.77 us                                                     | 6.40 us: 1.11x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 37.6 ms: 1.11x slower                                                       |
| generators                 | 19.0 ms                                                     | 21.1 ms: 1.11x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.87 us: 1.11x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.6 us: 1.12x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 18.9 ms: 1.12x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 60.1 ms: 1.12x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 63.9 ms: 1.13x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.96 ms: 1.14x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 148 us: 1.14x slower                                                        |
| hexiom                     | 3.84 ms                                                     | 4.45 ms: 1.16x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 83.3 ms: 1.16x slower                                                       |
| nbody                      | 66.3 ms                                                     | 76.9 ms: 1.16x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 42.5 ms: 1.16x slower                                                       |
| chaos                      | 37.9 ms                                                     | 44.5 ms: 1.18x slower                                                       |
| async_generators           | 223 ms                                                      | 262 ms: 1.18x slower                                                        |
| richards                   | 26.3 ms                                                     | 30.9 ms: 1.18x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 123 us: 1.19x slower                                                        |
| pickle_pure_python         | 186 us                                                      | 225 us: 1.21x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 18.4 ms: 1.21x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 49.4 ms: 1.21x slower                                                       |
| richards_super             | 29.8 ms                                                     | 36.2 ms: 1.22x slower                                                       |
| fannkuch                   | 252 ms                                                      | 306 ms: 1.22x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.31 ms: 1.22x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 55.9 ms: 1.23x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 1.01 ms: 1.24x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 70.1 ms: 1.25x slower                                                       |
| django_template            | 20.3 ms                                                     | 26.0 ms: 1.28x slower                                                       |
| raytrace                   | 153 ms                                                      | 205 ms: 1.34x slower                                                        |
| mako                       | 6.56 ms                                                     | 9.63 ms: 1.47x slower                                                       |
| coverage                   | 45.3 ms                                                     | 67.1 ms: 1.48x slower                                                       |
| k_core                     | 1.70 sec                                                    | 2.59 sec: 1.53x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 2.17 sec: 1.58x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.55 sec: 1.59x slower                                                      |
| many_optionals             | 361 us                                                      | 602 us: 1.67x slower                                                        |
| shortest_path              | 355 ms                                                      | 630 ms: 1.77x slower                                                        |
| docutils                   | 1.53 sec                                                    | 2.72 sec: 1.78x slower                                                      |
| connected_components       | 320 ms                                                      | 590 ms: 1.84x slower                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 5.30 sec: 1.85x slower                                                      |
| subparsers                 | 10.9 ms                                                     | 35.0 ms: 3.23x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (4): pylint, pycparser, dulwich_log, sphinx
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251101-3.15.0a1+-2f60b8f-NOGIL/bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.022x slower

# HPT report

- Reliability score: 99.81% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown