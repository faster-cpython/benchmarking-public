# Results vs. 3.13.0

- fork: python
- ref: 6fcac09401e336b25833
- machine: windows-amd64
- commit hash: 6fcac09
- commit date: 2025-08-23
- overall geometric mean: 1.106x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.53 sec                                                    | 1.61 sec: 1.05x slower                                                     |
| html5lib       | 38.2 ms                                                     | 37.3 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 197 ms: 1.35x faster                                                       |
| async_tree_io              | 513 ms                                                      | 383 ms: 1.34x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 377 ms: 1.32x faster                                                       |
| async_tree_none            | 219 ms                                                      | 168 ms: 1.30x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 164 ms: 1.22x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 336 ms: 1.14x faster                                                       |
| async_generators           | 223 ms                                                      | 237 ms: 1.06x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.24x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 42.9 ms: 1.19x faster                                                      |
| nbody          | 66.3 ms                                                     | 60.0 ms: 1.11x faster                                                      |
| pidigits       | 146 ms                                                      | 144 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.5 ms: 1.76x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.55 ms: 1.09x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 77.4 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.08 sec: 1.28x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 104 us: 1.25x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 5.31 ms: 1.17x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 85.5 ms: 1.08x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.1 us: 1.07x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 49.8 ms: 1.07x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 34.7 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 61.6 ms: 1.02x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 197 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.2 ms: 1.03x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.2 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.21 ms: 1.26x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.3 ms: 1.01x slower                                                      |
| django_template | 20.3 ms                                                     | 23.9 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 484 us: 17.49x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 30.1 ms: 2.50x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                                       |
| mdp                        | 1.43 sec                                                    | 777 ms: 1.84x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.5 ms: 1.76x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 197 ms: 1.35x faster                                                       |
| async_tree_io              | 513 ms                                                      | 383 ms: 1.34x faster                                                       |
| deepcopy                   | 223 us                                                      | 168 us: 1.33x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 377 ms: 1.32x faster                                                       |
| async_tree_none            | 219 ms                                                      | 168 ms: 1.30x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.08 sec: 1.28x faster                                                     |
| telco                      | 4.85 ms                                                     | 3.82 ms: 1.27x faster                                                      |
| deepcopy_memo              | 23.1 us                                                     | 18.2 us: 1.27x faster                                                      |
| mako                       | 6.56 ms                                                     | 5.21 ms: 1.26x faster                                                      |
| unpickle_pure_python       | 130 us                                                      | 104 us: 1.25x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 164 ms: 1.22x faster                                                       |
| fannkuch                   | 252 ms                                                      | 210 ms: 1.20x faster                                                       |
| float                      | 50.8 ms                                                     | 42.9 ms: 1.19x faster                                                      |
| scimark_fft                | 175 ms                                                      | 148 ms: 1.18x faster                                                       |
| pprint_safe_repr           | 485 ms                                                      | 414 ms: 1.17x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.46 sec: 1.17x faster                                                     |
| json_dumps                 | 6.19 ms                                                     | 5.31 ms: 1.17x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| pprint_pformat             | 977 ms                                                      | 849 ms: 1.15x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.28 ms: 1.14x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 336 ms: 1.14x faster                                                       |
| go                         | 84.7 ms                                                     | 74.9 ms: 1.13x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.82 us: 1.11x faster                                                      |
| nbody                      | 66.3 ms                                                     | 60.0 ms: 1.11x faster                                                      |
| pyflate                    | 283 ms                                                      | 256 ms: 1.10x faster                                                       |
| json                       | 3.30 ms                                                     | 3.02 ms: 1.09x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.55 ms: 1.09x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 85.5 ms: 1.08x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.1 us: 1.07x faster                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 49.8 ms: 1.07x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.59 sec: 1.07x faster                                                     |
| pylint                     | 205 ms                                                      | 193 ms: 1.07x faster                                                       |
| xml_etree_process          | 36.5 ms                                                     | 34.7 ms: 1.05x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.52 us: 1.04x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 77.4 ms: 1.04x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.1 ms: 1.04x faster                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 44.2 ms: 1.03x faster                                                      |
| typing_runtime_protocols   | 103 us                                                      | 100 us: 1.03x faster                                                       |
| dulwich_log                | 40.1 ms                                                     | 39.1 ms: 1.02x faster                                                      |
| html5lib                   | 38.2 ms                                                     | 37.3 ms: 1.02x faster                                                      |
| meteor_contest             | 72.0 ms                                                     | 70.5 ms: 1.02x faster                                                      |
| shortest_path              | 355 ms                                                      | 348 ms: 1.02x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 62.1 ms: 1.02x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 74.7 ms: 1.02x faster                                                      |
| pidigits                   | 146 ms                                                      | 144 ms: 1.02x faster                                                       |
| logging_silent             | 54.6 ns                                                     | 53.5 ns: 1.02x faster                                                      |
| comprehensions             | 10.4 us                                                     | 10.3 us: 1.01x faster                                                      |
| sympy_sum                  | 85.2 ms                                                     | 84.5 ms: 1.01x faster                                                      |
| sympy_expand               | 286 ms                                                      | 288 ms: 1.01x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.1 ms: 1.01x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 15.3 ms: 1.01x slower                                                      |
| richards_super             | 29.8 ms                                                     | 30.1 ms: 1.01x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 3.91 ms: 1.02x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 61.6 ms: 1.02x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 57.8 ms: 1.02x slower                                                      |
| logging_simple             | 5.77 us                                                     | 5.89 us: 1.02x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.35 us: 1.03x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.2 ms: 1.03x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 842 us: 1.04x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.28 ms: 1.04x slower                                                      |
| chaos                      | 37.9 ms                                                     | 39.6 ms: 1.04x slower                                                      |
| coverage                   | 45.3 ms                                                     | 47.4 ms: 1.05x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.61 sec: 1.05x slower                                                     |
| nqueens                    | 56.1 ms                                                     | 59.2 ms: 1.05x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 197 us: 1.06x slower                                                       |
| async_generators           | 223 ms                                                      | 237 ms: 1.06x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.11 ms: 1.08x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 92.2 ms: 1.09x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.15 ms: 1.13x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.2 ms: 1.14x slower                                                      |
| raytrace                   | 153 ms                                                      | 176 ms: 1.15x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                      |
| django_template            | 20.3 ms                                                     | 23.9 ms: 1.18x slower                                                      |
| many_optionals             | 361 us                                                      | 558 us: 1.54x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 29.4 ms: 2.71x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.10x faster                                                               |

Benchmark hidden because not significant (9): 2to3, connected_components, pycparser, sympy_integrate, sympy_str, richards, regex_dna, sphinx, genshi_xml
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250823-3.15.0a0-6fcac09-JIT/bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.106x faster

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown