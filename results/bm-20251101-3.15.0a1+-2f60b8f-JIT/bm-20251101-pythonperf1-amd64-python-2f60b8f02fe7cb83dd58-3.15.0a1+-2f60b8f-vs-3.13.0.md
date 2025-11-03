# Results vs. 3.13.0

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: windows-amd64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.120x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 213 ms: 1.01x faster                                                        |
| docutils       | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                      |
| html5lib       | 38.2 ms                                                     | 35.8 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 142 ms: 2.12x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 192 ms: 1.46x faster                                                        |
| async_tree_io              | 513 ms                                                      | 360 ms: 1.43x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 190 ms: 1.39x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 366 ms: 1.36x faster                                                        |
| async_tree_none            | 219 ms                                                      | 164 ms: 1.34x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 154 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 321 ms: 1.18x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 330 ms: 1.16x faster                                                        |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.12x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.29x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 38.9 ms: 1.31x faster                                                       |
| nbody          | 66.3 ms                                                     | 53.1 ms: 1.25x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.0 ms: 1.70x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.59 ms: 1.07x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 77.5 ms: 1.04x faster                                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.06 sec: 1.30x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 103 us: 1.27x faster                                                        |
| json_dumps           | 6.19 ms                                                     | 5.38 ms: 1.15x faster                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 48.6 ms: 1.10x faster                                                       |
| json_loads           | 15.1 us                                                     | 13.9 us: 1.09x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 85.3 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 56.6 ms: 1.07x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 34.2 ms: 1.07x faster                                                       |
| pickle_pure_python   | 186 us                                                      | 193 us: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.4 ms: 1.04x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.12 ms: 1.28x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 15.3 ms: 1.01x slower                                                       |
| django_template | 20.3 ms                                                     | 23.7 ms: 1.17x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 491 us: 17.24x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 29.0 ms: 2.60x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 142 ms: 2.12x faster                                                        |
| mdp                        | 1.43 sec                                                    | 779 ms: 1.84x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 14.0 ms: 1.70x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 192 ms: 1.46x faster                                                        |
| async_tree_io              | 513 ms                                                      | 360 ms: 1.43x faster                                                        |
| deepcopy                   | 223 us                                                      | 160 us: 1.40x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 190 ms: 1.39x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 366 ms: 1.36x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 17.0 us: 1.36x faster                                                       |
| async_tree_none            | 219 ms                                                      | 164 ms: 1.34x faster                                                        |
| scimark_fft                | 175 ms                                                      | 132 ms: 1.32x faster                                                        |
| float                      | 50.8 ms                                                     | 38.9 ms: 1.31x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 154 ms: 1.30x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.06 sec: 1.30x faster                                                      |
| mako                       | 6.56 ms                                                     | 5.12 ms: 1.28x faster                                                       |
| unpickle_pure_python       | 130 us                                                      | 103 us: 1.27x faster                                                        |
| telco                      | 4.85 ms                                                     | 3.88 ms: 1.25x faster                                                       |
| nbody                      | 66.3 ms                                                     | 53.1 ms: 1.25x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.15 ms: 1.21x faster                                                       |
| fannkuch                   | 252 ms                                                      | 210 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 321 ms: 1.18x faster                                                        |
| pprint_safe_repr           | 485 ms                                                      | 413 ms: 1.17x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.73 us: 1.17x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 330 ms: 1.16x faster                                                        |
| json_dumps                 | 6.19 ms                                                     | 5.38 ms: 1.15x faster                                                       |
| pyflate                    | 283 ms                                                      | 246 ms: 1.15x faster                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 2.50 sec: 1.15x faster                                                      |
| pprint_pformat             | 977 ms                                                      | 854 ms: 1.14x faster                                                        |
| go                         | 84.7 ms                                                     | 75.0 ms: 1.13x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 48.6 ms: 1.10x faster                                                       |
| json                       | 3.30 ms                                                     | 3.00 ms: 1.10x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.54 sec: 1.10x faster                                                      |
| json_loads                 | 15.1 us                                                     | 13.9 us: 1.09x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 85.3 ms: 1.08x faster                                                       |
| pycparser                  | 695 ms                                                      | 646 ms: 1.08x faster                                                        |
| xml_etree_iterparse        | 60.5 ms                                                     | 56.6 ms: 1.07x faster                                                       |
| xml_etree_process          | 36.5 ms                                                     | 34.2 ms: 1.07x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.59 ms: 1.07x faster                                                       |
| html5lib                   | 38.2 ms                                                     | 35.8 ms: 1.06x faster                                                       |
| regex_compile              | 80.7 ms                                                     | 77.5 ms: 1.04x faster                                                       |
| meteor_contest             | 72.0 ms                                                     | 69.3 ms: 1.04x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.53 us: 1.03x faster                                                       |
| dulwich_log                | 40.1 ms                                                     | 38.9 ms: 1.03x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.9 ms: 1.02x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 74.8 ms: 1.02x faster                                                       |
| comprehensions             | 10.4 us                                                     | 10.2 us: 1.02x faster                                                       |
| shortest_path              | 355 ms                                                      | 350 ms: 1.01x faster                                                        |
| connected_components       | 320 ms                                                      | 316 ms: 1.01x faster                                                        |
| 2to3                       | 215 ms                                                      | 213 ms: 1.01x faster                                                        |
| sympy_expand               | 286 ms                                                      | 284 ms: 1.01x faster                                                        |
| logging_silent             | 54.6 ns                                                     | 54.8 ns: 1.00x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 3.87 ms: 1.01x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.4 ms: 1.01x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.3 ms: 1.01x slower                                                       |
| spectral_norm              | 63.4 ms                                                     | 64.0 ms: 1.01x slower                                                       |
| chaos                      | 37.9 ms                                                     | 38.2 ms: 1.01x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 57.4 ms: 1.01x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.2 ms: 1.01x slower                                                       |
| logging_simple             | 5.77 us                                                     | 5.86 us: 1.02x slower                                                       |
| sympy_str                  | 167 ms                                                      | 170 ms: 1.02x slower                                                        |
| richards_super             | 29.8 ms                                                     | 30.3 ms: 1.02x slower                                                       |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| typing_runtime_protocols   | 103 us                                                      | 105 us: 1.02x slower                                                        |
| richards                   | 26.3 ms                                                     | 27.0 ms: 1.03x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.36 us: 1.03x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 193 us: 1.04x slower                                                        |
| python_startup             | 24.4 ms                                                     | 25.4 ms: 1.04x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.29 ms: 1.05x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 88.6 ms: 1.05x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 59.4 ms: 1.06x slower                                                       |
| coverage                   | 45.3 ms                                                     | 48.6 ms: 1.07x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.12 ms: 1.08x slower                                                       |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                        |
| raytrace                   | 153 ms                                                      | 170 ms: 1.11x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.12x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.16 ms: 1.14x slower                                                       |
| django_template            | 20.3 ms                                                     | 23.7 ms: 1.17x slower                                                       |
| many_optionals             | 361 us                                                      | 563 us: 1.56x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 30.8 ms: 2.84x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                                |

Benchmark hidden because not significant (7): pylint, sympy_sum, sphinx, pidigits, crypto_pyaes, genshi_xml, bench_thread_pool
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251101-3.15.0a1+-2f60b8f-JIT/bm-20251101-pythonperf1-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.120x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown