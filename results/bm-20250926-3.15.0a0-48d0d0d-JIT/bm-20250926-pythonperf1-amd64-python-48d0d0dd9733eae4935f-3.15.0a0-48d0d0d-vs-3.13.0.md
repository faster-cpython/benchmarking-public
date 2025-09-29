# Results vs. 3.13.0

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: windows-amd64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.104x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 214 ms: 1.01x faster                                                       |
| docutils       | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                     |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.87x faster                                                       |
| async_tree_io              | 513 ms                                                      | 381 ms: 1.35x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 199 ms: 1.33x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 377 ms: 1.32x faster                                                       |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 164 ms: 1.22x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 333 ms: 1.15x faster                                                       |
| async_generators           | 223 ms                                                      | 239 ms: 1.07x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.24x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 39.8 ms: 1.28x faster                                                      |
| nbody          | 66.3 ms                                                     | 55.8 ms: 1.19x faster                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.3 ms: 1.79x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.60 ms: 1.06x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 77.3 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.08 sec: 1.27x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 105 us: 1.24x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 5.31 ms: 1.17x faster                                                      |
| json_loads           | 15.1 us                                                     | 13.8 us: 1.09x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 50.0 ms: 1.07x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 87.6 ms: 1.05x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 35.7 ms: 1.02x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 61.5 ms: 1.02x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 198 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.2 ms: 1.04x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.1 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.34 ms: 1.23x faster                                                      |
| genshi_xml      | 33.9 ms                                                     | 34.9 ms: 1.03x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                      |
| django_template | 20.3 ms                                                     | 24.0 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 489 us: 17.31x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 28.9 ms: 2.61x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.87x faster                                                       |
| mdp                        | 1.43 sec                                                    | 786 ms: 1.82x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.3 ms: 1.79x faster                                                      |
| deepcopy                   | 223 us                                                      | 164 us: 1.37x faster                                                       |
| async_tree_io              | 513 ms                                                      | 381 ms: 1.35x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 17.2 us: 1.35x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 199 ms: 1.33x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 377 ms: 1.32x faster                                                       |
| scimark_fft                | 175 ms                                                      | 134 ms: 1.31x faster                                                       |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                       |
| float                      | 50.8 ms                                                     | 39.8 ms: 1.28x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.08 sec: 1.27x faster                                                     |
| unpickle_pure_python       | 130 us                                                      | 105 us: 1.24x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.34 ms: 1.23x faster                                                      |
| telco                      | 4.85 ms                                                     | 3.96 ms: 1.22x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 164 ms: 1.22x faster                                                       |
| fannkuch                   | 252 ms                                                      | 207 ms: 1.22x faster                                                       |
| nbody                      | 66.3 ms                                                     | 55.8 ms: 1.19x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.21 ms: 1.18x faster                                                      |
| json                       | 3.30 ms                                                     | 2.80 ms: 1.18x faster                                                      |
| json_dumps                 | 6.19 ms                                                     | 5.31 ms: 1.17x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 333 ms: 1.15x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.76 us: 1.15x faster                                                      |
| pyflate                    | 283 ms                                                      | 250 ms: 1.13x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.54 sec: 1.13x faster                                                     |
| pprint_safe_repr           | 485 ms                                                      | 433 ms: 1.12x faster                                                       |
| go                         | 84.7 ms                                                     | 76.7 ms: 1.10x faster                                                      |
| pprint_pformat             | 977 ms                                                      | 886 ms: 1.10x faster                                                       |
| json_loads                 | 15.1 us                                                     | 13.8 us: 1.09x faster                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 50.0 ms: 1.07x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.59 sec: 1.07x faster                                                     |
| regex_effbot               | 1.69 ms                                                     | 1.60 ms: 1.06x faster                                                      |
| pylint                     | 205 ms                                                      | 195 ms: 1.05x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 87.6 ms: 1.05x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 60.5 ms: 1.05x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 77.3 ms: 1.04x faster                                                      |
| dulwich_log                | 40.1 ms                                                     | 38.6 ms: 1.04x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 35.7 ms: 1.02x faster                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 44.6 ms: 1.02x faster                                                      |
| shortest_path              | 355 ms                                                      | 348 ms: 1.02x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 75.0 ms: 1.02x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.57 us: 1.01x faster                                                      |
| sympy_sum                  | 85.2 ms                                                     | 84.2 ms: 1.01x faster                                                      |
| connected_components       | 320 ms                                                      | 317 ms: 1.01x faster                                                       |
| sympy_str                  | 167 ms                                                      | 165 ms: 1.01x faster                                                       |
| meteor_contest             | 72.0 ms                                                     | 71.4 ms: 1.01x faster                                                      |
| sympy_expand               | 286 ms                                                      | 284 ms: 1.01x faster                                                       |
| 2to3                       | 215 ms                                                      | 214 ms: 1.01x faster                                                       |
| logging_silent             | 54.6 ns                                                     | 54.3 ns: 1.01x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.9 ms: 1.00x slower                                                      |
| comprehensions             | 10.4 us                                                     | 10.5 us: 1.01x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 61.5 ms: 1.02x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.3 ms: 1.02x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 3.92 ms: 1.02x slower                                                      |
| richards                   | 26.3 ms                                                     | 26.8 ms: 1.02x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.25 ms: 1.02x slower                                                      |
| richards_super             | 29.8 ms                                                     | 30.6 ms: 1.03x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 834 us: 1.03x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 34.9 ms: 1.03x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.2 ms: 1.04x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 88.8 ms: 1.05x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.09 us: 1.05x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                     |
| chaos                      | 37.9 ms                                                     | 40.2 ms: 1.06x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 59.7 ms: 1.06x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 198 us: 1.06x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.57 us: 1.06x slower                                                      |
| async_generators           | 223 ms                                                      | 239 ms: 1.07x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.12 ms: 1.08x slower                                                      |
| coverage                   | 45.3 ms                                                     | 49.0 ms: 1.08x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.1 ms: 1.13x slower                                                      |
| raytrace                   | 153 ms                                                      | 173 ms: 1.13x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.19 ms: 1.16x slower                                                      |
| django_template            | 20.3 ms                                                     | 24.0 ms: 1.18x slower                                                      |
| many_optionals             | 361 us                                                      | 563 us: 1.56x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 30.1 ms: 2.77x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.10x faster                                                               |

Benchmark hidden because not significant (8): pycparser, typing_runtime_protocols, html5lib, regex_dna, pidigits, scimark_lu, sympy_integrate, sphinx
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.104x faster

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown