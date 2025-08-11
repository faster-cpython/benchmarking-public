# Results vs. 3.13.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: windows-amd64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.068x faster
- HPT reliability: 71.33%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 219 ms: 1.02x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.59 sec: 1.04x slower                                                     |
| html5lib       | 38.2 ms                                                     | 37.2 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.92x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.36x faster                                                       |
| async_tree_io              | 513 ms                                                      | 382 ms: 1.34x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 200 ms: 1.32x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 379 ms: 1.31x faster                                                       |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 164 ms: 1.22x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 327 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 334 ms: 1.15x faster                                                       |
| async_generators           | 223 ms                                                      | 228 ms: 1.02x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.24x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.1 ms: 1.18x faster                                                      |
| pidigits       | 146 ms                                                      | 145 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.2 ms: 1.81x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.48 ms: 1.14x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 78.4 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 6.19 ms                                                     | 5.27 ms: 1.18x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.0 us: 1.08x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 86.8 ms: 1.06x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 132 us: 1.01x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 38.8 ms: 1.06x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.5 ms: 1.07x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 57.5 ms: 1.08x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 208 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.7 ms: 1.16x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.6 ms: 1.03x slower                                                      |
| django_template | 20.3 ms                                                     | 23.9 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 489 us: 17.32x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 32.1 ms: 2.34x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.92x faster                                                       |
| mdp                        | 1.43 sec                                                    | 790 ms: 1.81x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.2 ms: 1.81x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.36x faster                                                       |
| async_tree_io              | 513 ms                                                      | 382 ms: 1.34x faster                                                       |
| deepcopy                   | 223 us                                                      | 167 us: 1.34x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 200 ms: 1.32x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 379 ms: 1.31x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 17.8 us: 1.30x faster                                                      |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 164 ms: 1.22x faster                                                       |
| float                      | 50.8 ms                                                     | 43.1 ms: 1.18x faster                                                      |
| json_dumps                 | 6.19 ms                                                     | 5.27 ms: 1.18x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 327 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 334 ms: 1.15x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.77 us: 1.14x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.48 ms: 1.14x faster                                                      |
| go                         | 84.7 ms                                                     | 75.6 ms: 1.12x faster                                                      |
| json                       | 3.30 ms                                                     | 2.96 ms: 1.12x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.47 ms: 1.08x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.0 us: 1.08x faster                                                      |
| pylint                     | 205 ms                                                      | 193 ms: 1.06x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 86.8 ms: 1.06x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.46 ms: 1.06x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 38.9 ms: 1.05x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 78.4 ms: 1.03x faster                                                      |
| html5lib                   | 38.2 ms                                                     | 37.2 ms: 1.03x faster                                                      |
| dulwich_log                | 40.1 ms                                                     | 39.1 ms: 1.03x faster                                                      |
| sympy_expand               | 286 ms                                                      | 279 ms: 1.02x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.55 us: 1.02x faster                                                      |
| scimark_lu                 | 56.7 ms                                                     | 55.9 ms: 1.01x faster                                                      |
| pidigits                   | 146 ms                                                      | 145 ms: 1.01x faster                                                       |
| sympy_str                  | 167 ms                                                      | 165 ms: 1.01x faster                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.2 ms: 1.01x faster                                                      |
| typing_runtime_protocols   | 103 us                                                      | 102 us: 1.01x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 75.7 ms: 1.01x faster                                                      |
| meteor_contest             | 72.0 ms                                                     | 71.5 ms: 1.01x faster                                                      |
| richards                   | 26.3 ms                                                     | 26.1 ms: 1.00x faster                                                      |
| richards_super             | 29.8 ms                                                     | 30.1 ms: 1.01x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 988 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 132 us: 1.01x slower                                                       |
| 2to3                       | 215 ms                                                      | 219 ms: 1.02x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.93 sec: 1.02x slower                                                     |
| pyflate                    | 283 ms                                                      | 289 ms: 1.02x slower                                                       |
| async_generators           | 223 ms                                                      | 228 ms: 1.02x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.6 ms: 1.03x slower                                                      |
| connected_components       | 320 ms                                                      | 328 ms: 1.03x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 56.0 ns: 1.03x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 46.9 ms: 1.03x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 3.97 ms: 1.03x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.59 sec: 1.04x slower                                                     |
| logging_simple             | 5.77 us                                                     | 5.99 us: 1.04x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.41 us: 1.04x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 66.0 ms: 1.04x slower                                                      |
| fannkuch                   | 252 ms                                                      | 262 ms: 1.04x slower                                                       |
| scimark_fft                | 175 ms                                                      | 182 ms: 1.04x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.8 ms: 1.04x slower                                                      |
| comprehensions             | 10.4 us                                                     | 10.8 us: 1.04x slower                                                      |
| chaos                      | 37.9 ms                                                     | 39.7 ms: 1.05x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.30 ms: 1.06x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 38.8 ms: 1.06x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 862 us: 1.06x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.5 ms: 1.07x slower                                                      |
| python_startup             | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.11 ms: 1.07x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 57.5 ms: 1.08x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 60.8 ms: 1.08x slower                                                      |
| coverage                   | 45.3 ms                                                     | 49.5 ms: 1.09x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 208 us: 1.12x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 94.9 ms: 1.13x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.20 ms: 1.16x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.7 ms: 1.16x slower                                                      |
| django_template            | 20.3 ms                                                     | 23.9 ms: 1.18x slower                                                      |
| raytrace                   | 153 ms                                                      | 193 ms: 1.26x slower                                                       |
| many_optionals             | 361 us                                                      | 555 us: 1.54x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 29.7 ms: 2.74x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (11): nbody, pycparser, k_core, mako, tomli_loads, regex_dna, sympy_sum, shortest_path, pprint_safe_repr, sphinx, genshi_xml
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.068x faster

# HPT report

- Reliability score: 71.33% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown