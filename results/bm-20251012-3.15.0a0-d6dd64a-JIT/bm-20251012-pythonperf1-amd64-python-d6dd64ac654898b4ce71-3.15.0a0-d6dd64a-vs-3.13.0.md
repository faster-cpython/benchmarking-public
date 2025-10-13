# Results vs. 3.13.0

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: windows-amd64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.113x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 212 ms: 1.01x faster                                                       |
| docutils       | 1.53 sec                                                    | 1.60 sec: 1.05x slower                                                     |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 162 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 198 ms: 1.33x faster                                                       |
| async_tree_io              | 513 ms                                                      | 385 ms: 1.33x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 376 ms: 1.32x faster                                                       |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.27x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 164 ms: 1.22x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 334 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 340 ms: 1.13x faster                                                       |
| async_generators           | 223 ms                                                      | 236 ms: 1.06x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.6 ms: 1.17x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 54.5 ms: 1.22x faster                                                      |
| float          | 50.8 ms                                                     | 43.8 ms: 1.16x faster                                                      |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.6 ms: 1.75x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.56 ms: 1.09x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 75.9 ms: 1.06x faster                                                      |
| regex_dna      | 115 ms                                                      | 118 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.09 sec: 1.25x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 107 us: 1.22x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 5.52 ms: 1.12x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 49.2 ms: 1.09x faster                                                      |
| json_loads           | 15.1 us                                                     | 13.9 us: 1.08x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 87.9 ms: 1.05x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 34.8 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.7 ms: 1.04x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 194 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.1 ms: 1.03x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 18.9 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.28 ms: 1.24x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                      |
| django_template | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 499 us: 16.97x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 28.8 ms: 2.61x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 162 ms: 1.85x faster                                                       |
| mdp                        | 1.43 sec                                                    | 781 ms: 1.83x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.6 ms: 1.75x faster                                                      |
| deepcopy_memo              | 23.1 us                                                     | 13.5 us: 1.71x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 43.0 ms: 1.47x faster                                                      |
| deepcopy                   | 223 us                                                      | 159 us: 1.41x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 198 ms: 1.33x faster                                                       |
| async_tree_io              | 513 ms                                                      | 385 ms: 1.33x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 376 ms: 1.32x faster                                                       |
| scimark_fft                | 175 ms                                                      | 134 ms: 1.31x faster                                                       |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.27x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.09 sec: 1.25x faster                                                     |
| telco                      | 4.85 ms                                                     | 3.90 ms: 1.24x faster                                                      |
| mako                       | 6.56 ms                                                     | 5.28 ms: 1.24x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 164 ms: 1.22x faster                                                       |
| unpickle_pure_python       | 130 us                                                      | 107 us: 1.22x faster                                                       |
| nbody                      | 66.3 ms                                                     | 54.5 ms: 1.22x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.19 ms: 1.19x faster                                                      |
| fannkuch                   | 252 ms                                                      | 213 ms: 1.18x faster                                                       |
| pprint_safe_repr           | 485 ms                                                      | 411 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.72 us: 1.17x faster                                                      |
| pprint_pformat             | 977 ms                                                      | 834 ms: 1.17x faster                                                       |
| float                      | 50.8 ms                                                     | 43.8 ms: 1.16x faster                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.51 sec: 1.15x faster                                                     |
| json                       | 3.30 ms                                                     | 2.89 ms: 1.14x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 334 ms: 1.14x faster                                                       |
| go                         | 84.7 ms                                                     | 74.6 ms: 1.14x faster                                                      |
| pyflate                    | 283 ms                                                      | 250 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 340 ms: 1.13x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.52 ms: 1.12x faster                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 49.2 ms: 1.09x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.56 ms: 1.09x faster                                                      |
| json_loads                 | 15.1 us                                                     | 13.9 us: 1.08x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.58 sec: 1.07x faster                                                     |
| pylint                     | 205 ms                                                      | 192 ms: 1.07x faster                                                       |
| regex_compile              | 80.7 ms                                                     | 75.9 ms: 1.06x faster                                                      |
| dulwich_log                | 40.1 ms                                                     | 38.0 ms: 1.06x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 87.9 ms: 1.05x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 34.8 ms: 1.05x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.53 us: 1.04x faster                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 44.4 ms: 1.03x faster                                                      |
| shortest_path              | 355 ms                                                      | 347 ms: 1.02x faster                                                       |
| 2to3                       | 215 ms                                                      | 212 ms: 1.01x faster                                                       |
| sympy_sum                  | 85.2 ms                                                     | 84.4 ms: 1.01x faster                                                      |
| sympy_str                  | 167 ms                                                      | 165 ms: 1.01x faster                                                       |
| richards_super             | 29.8 ms                                                     | 30.0 ms: 1.01x slower                                                      |
| richards                   | 26.3 ms                                                     | 26.6 ms: 1.01x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 105 us: 1.01x slower                                                       |
| comprehensions             | 10.4 us                                                     | 10.5 us: 1.01x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 828 us: 1.02x slower                                                       |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.02x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.25 ms: 1.02x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.1 ms: 1.03x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.7 ms: 1.04x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.00 ms: 1.04x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 194 us: 1.05x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.60 sec: 1.05x slower                                                     |
| bench_mp_pool              | 84.2 ms                                                     | 88.5 ms: 1.05x slower                                                      |
| async_generators           | 223 ms                                                      | 236 ms: 1.06x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 59.4 ms: 1.06x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.09 ms: 1.06x slower                                                      |
| chaos                      | 37.9 ms                                                     | 40.6 ms: 1.07x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 62.2 ms: 1.10x slower                                                      |
| coverage                   | 45.3 ms                                                     | 50.3 ms: 1.11x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 18.9 ms: 1.12x slower                                                      |
| raytrace                   | 153 ms                                                      | 172 ms: 1.12x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.14 ms: 1.13x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.6 ms: 1.17x slower                                                      |
| django_template            | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                      |
| many_optionals             | 361 us                                                      | 573 us: 1.59x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 30.9 ms: 2.85x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                               |

Benchmark hidden because not significant (14): html5lib, scimark_monte_carlo, connected_components, scimark_sor, meteor_contest, sympy_expand, logging_simple, pidigits, logging_silent, logging_format, sympy_integrate, sphinx, pycparser, genshi_xml
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251012-3.15.0a0-d6dd64a-JIT/bm-20251012-pythonperf1-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.113x faster

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown