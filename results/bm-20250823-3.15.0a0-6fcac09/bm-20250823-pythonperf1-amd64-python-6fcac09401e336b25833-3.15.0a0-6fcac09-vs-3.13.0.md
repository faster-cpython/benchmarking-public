# Results vs. 3.13.0

- fork: python
- ref: 6fcac09401e336b25833
- machine: windows-amd64
- commit hash: 6fcac09
- commit date: 2025-08-23
- overall geometric mean: 1.069x faster
- HPT reliability: 74.27%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 217 ms: 1.01x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.63 sec: 1.07x slower                                                     |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.86x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 204 ms: 1.37x faster                                                       |
| async_tree_io              | 513 ms                                                      | 384 ms: 1.34x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 201 ms: 1.32x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 392 ms: 1.27x faster                                                       |
| async_tree_none            | 219 ms                                                      | 173 ms: 1.27x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 334 ms: 1.14x faster                                                       |
| async_generators           | 223 ms                                                      | 224 ms: 1.01x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.14x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.5 ms: 1.17x faster                                                      |
| nbody          | 66.3 ms                                                     | 62.8 ms: 1.06x faster                                                      |
| pidigits       | 146 ms                                                      | 143 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.7 ms: 1.74x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.52 ms: 1.11x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 78.1 ms: 1.03x faster                                                      |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 6.19 ms                                                     | 5.36 ms: 1.16x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.3 us: 1.06x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 87.6 ms: 1.05x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 133 us: 1.02x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 55.6 ms: 1.04x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.1 ms: 1.04x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 38.4 ms: 1.05x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 209 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.5 ms: 1.04x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (3): genshi_text, mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 493 us: 17.19x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 30.4 ms: 2.48x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.86x faster                                                       |
| mdp                        | 1.43 sec                                                    | 800 ms: 1.79x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.7 ms: 1.74x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 204 ms: 1.37x faster                                                       |
| async_tree_io              | 513 ms                                                      | 384 ms: 1.34x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 201 ms: 1.32x faster                                                       |
| deepcopy                   | 223 us                                                      | 171 us: 1.31x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 17.9 us: 1.29x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 392 ms: 1.27x faster                                                       |
| async_tree_none            | 219 ms                                                      | 173 ms: 1.27x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.14 ms: 1.17x faster                                                      |
| float                      | 50.8 ms                                                     | 43.5 ms: 1.17x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.36 ms: 1.16x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 334 ms: 1.14x faster                                                       |
| json                       | 3.30 ms                                                     | 2.91 ms: 1.13x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.52 ms: 1.11x faster                                                      |
| go                         | 84.7 ms                                                     | 76.5 ms: 1.11x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.86 us: 1.09x faster                                                      |
| pylint                     | 205 ms                                                      | 192 ms: 1.07x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.3 us: 1.06x faster                                                      |
| scimark_lu                 | 56.7 ms                                                     | 53.6 ms: 1.06x faster                                                      |
| nbody                      | 66.3 ms                                                     | 62.8 ms: 1.06x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 87.6 ms: 1.05x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.48 ms: 1.05x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.1 ms: 1.04x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 73.5 ms: 1.04x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 78.1 ms: 1.03x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.54 us: 1.03x faster                                                      |
| sympy_expand               | 286 ms                                                      | 278 ms: 1.03x faster                                                       |
| pidigits                   | 146 ms                                                      | 143 ms: 1.02x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 62.7 ms: 1.01x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                     |
| richards                   | 26.3 ms                                                     | 26.4 ms: 1.00x slower                                                      |
| async_generators           | 223 ms                                                      | 224 ms: 1.01x slower                                                       |
| 2to3                       | 215 ms                                                      | 217 ms: 1.01x slower                                                       |
| richards_super             | 29.8 ms                                                     | 30.1 ms: 1.01x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 55.2 ns: 1.01x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.2 ms: 1.01x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 991 ms: 1.01x slower                                                       |
| shortest_path              | 355 ms                                                      | 361 ms: 1.02x slower                                                       |
| fannkuch                   | 252 ms                                                      | 256 ms: 1.02x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.93 sec: 1.02x slower                                                     |
| unpickle_pure_python       | 130 us                                                      | 133 us: 1.02x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 87.2 ms: 1.02x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 47.1 ms: 1.03x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 840 us: 1.04x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 55.6 ms: 1.04x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.1 ms: 1.04x slower                                                      |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.5 ms: 1.04x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.06 us: 1.05x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.04 ms: 1.05x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 38.4 ms: 1.05x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.29 ms: 1.06x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.53 us: 1.06x slower                                                      |
| comprehensions             | 10.4 us                                                     | 11.0 us: 1.06x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.63 sec: 1.07x slower                                                     |
| gc_traversal               | 1.96 ms                                                     | 2.10 ms: 1.07x slower                                                      |
| chaos                      | 37.9 ms                                                     | 40.6 ms: 1.07x slower                                                      |
| connected_components       | 320 ms                                                      | 344 ms: 1.08x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 61.0 ms: 1.09x slower                                                      |
| coverage                   | 45.3 ms                                                     | 50.5 ms: 1.11x slower                                                      |
| raytrace                   | 153 ms                                                      | 172 ms: 1.12x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 94.3 ms: 1.12x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 209 us: 1.12x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.14x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.18 ms: 1.15x slower                                                      |
| django_template            | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                      |
| many_optionals             | 361 us                                                      | 553 us: 1.53x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 29.6 ms: 2.73x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (15): html5lib, dulwich_log, pyflate, sympy_integrate, meteor_contest, k_core, sympy_str, pprint_safe_repr, genshi_text, mako, scimark_fft, typing_runtime_protocols, sphinx, pycparser, genshi_xml
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250823-3.15.0a0-6fcac09/bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.069x faster

# HPT report

- Reliability score: 74.27% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown