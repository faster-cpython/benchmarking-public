# Results vs. 3.13.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: windows-amd64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.023x faster
- HPT reliability: 99.86%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 225 ms: 1.04x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                     |
| html5lib       | 38.2 ms                                                     | 40.3 ms: 1.06x slower                                                      |
| sphinx         | 617 ms                                                      | 645 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 168 ms: 1.79x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 219 ms: 1.28x faster                                                       |
| async_tree_io              | 513 ms                                                      | 405 ms: 1.27x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 215 ms: 1.23x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 406 ms: 1.22x faster                                                       |
| async_tree_none            | 219 ms                                                      | 188 ms: 1.17x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 173 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 347 ms: 1.09x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 356 ms: 1.08x faster                                                       |
| async_generators           | 223 ms                                                      | 239 ms: 1.07x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.15x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 46.2 ms: 1.10x faster                                                      |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                       |
| nbody          | 66.3 ms                                                     | 67.0 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.9 ms: 1.72x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.52 ms: 1.11x faster                                                      |
| regex_dna      | 115 ms                                                      | 119 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                     |
| xml_etree_generate   | 53.5 ms                                                     | 58.6 ms: 1.10x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 144 us: 1.11x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 40.7 ms: 1.12x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 68.0 ms: 1.12x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 223 us: 1.20x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.9 ms: 1.10x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 20.3 ms: 1.20x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.67 ms: 1.02x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 15.9 ms: 1.05x slower                                                      |
| genshi_xml      | 33.9 ms                                                     | 36.2 ms: 1.07x slower                                                      |
| django_template | 20.3 ms                                                     | 24.6 ms: 1.21x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.08x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 503 us: 16.82x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 32.5 ms: 2.31x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 168 ms: 1.79x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.9 ms: 1.72x faster                                                      |
| mdp                        | 1.43 sec                                                    | 834 ms: 1.72x faster                                                       |
| deepcopy                   | 223 us                                                      | 172 us: 1.30x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 219 ms: 1.28x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.1 us: 1.28x faster                                                      |
| async_tree_io              | 513 ms                                                      | 405 ms: 1.27x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 215 ms: 1.23x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 406 ms: 1.22x faster                                                       |
| async_tree_none            | 219 ms                                                      | 188 ms: 1.17x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 173 ms: 1.16x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.52 ms: 1.11x faster                                                      |
| float                      | 50.8 ms                                                     | 46.2 ms: 1.10x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 347 ms: 1.09x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.87 us: 1.08x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 356 ms: 1.08x faster                                                       |
| json                       | 3.30 ms                                                     | 3.07 ms: 1.07x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| go                         | 84.7 ms                                                     | 80.7 ms: 1.05x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.64 ms: 1.04x faster                                                      |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                       |
| nbody                      | 66.3 ms                                                     | 67.0 ms: 1.01x slower                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.2 ms: 1.01x slower                                                      |
| mako                       | 6.56 ms                                                     | 6.67 ms: 1.02x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 105 us: 1.02x slower                                                       |
| sympy_str                  | 167 ms                                                      | 171 ms: 1.02x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.6 ms: 1.02x slower                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.68 ms: 1.03x slower                                                      |
| shortest_path              | 355 ms                                                      | 367 ms: 1.03x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.97 sec: 1.04x slower                                                     |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.04x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 56.6 ns: 1.04x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 74.7 ms: 1.04x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 65.9 ms: 1.04x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 79.3 ms: 1.04x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 88.9 ms: 1.04x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                     |
| sphinx                     | 617 ms                                                      | 645 ms: 1.04x slower                                                       |
| 2to3                       | 215 ms                                                      | 225 ms: 1.04x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.9 ms: 1.05x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 507 ms: 1.05x slower                                                       |
| connected_components       | 320 ms                                                      | 335 ms: 1.05x slower                                                       |
| sympy_expand               | 286 ms                                                      | 300 ms: 1.05x slower                                                       |
| pycparser                  | 695 ms                                                      | 732 ms: 1.05x slower                                                       |
| generators                 | 19.0 ms                                                     | 20.0 ms: 1.05x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 40.3 ms: 1.06x slower                                                      |
| pyflate                    | 283 ms                                                      | 302 ms: 1.07x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 36.2 ms: 1.07x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.17 us: 1.07x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                     |
| logging_format             | 6.18 us                                                     | 6.62 us: 1.07x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 48.9 ms: 1.07x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.05 sec: 1.07x slower                                                     |
| async_generators           | 223 ms                                                      | 239 ms: 1.07x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 872 us: 1.08x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.2 us: 1.08x slower                                                      |
| richards                   | 26.3 ms                                                     | 28.6 ms: 1.09x slower                                                      |
| scimark_fft                | 175 ms                                                      | 191 ms: 1.09x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 58.6 ms: 1.10x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 62.2 ms: 1.10x slower                                                      |
| fannkuch                   | 252 ms                                                      | 277 ms: 1.10x slower                                                       |
| coverage                   | 45.3 ms                                                     | 49.9 ms: 1.10x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.17 ms: 1.10x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 44.2 ms: 1.10x slower                                                      |
| python_startup             | 24.4 ms                                                     | 26.9 ms: 1.10x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.25 ms: 1.11x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 144 us: 1.11x slower                                                       |
| chaos                      | 37.9 ms                                                     | 42.0 ms: 1.11x slower                                                      |
| richards_super             | 29.8 ms                                                     | 33.0 ms: 1.11x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 40.7 ms: 1.12x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 68.0 ms: 1.12x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 63.7 ms: 1.13x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.39 ms: 1.13x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 96.1 ms: 1.14x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.15x slower                                                      |
| raytrace                   | 153 ms                                                      | 179 ms: 1.17x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.22 ms: 1.18x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 223 us: 1.20x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 20.3 ms: 1.20x slower                                                      |
| django_template            | 20.3 ms                                                     | 24.6 ms: 1.21x slower                                                      |
| many_optionals             | 361 us                                                      | 585 us: 1.62x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 31.4 ms: 2.89x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (6): pylint, xml_etree_parse, json_dumps, sqlite_synth, regex_compile, k_core
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.023x faster

# HPT report

- Reliability score: 99.86% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown