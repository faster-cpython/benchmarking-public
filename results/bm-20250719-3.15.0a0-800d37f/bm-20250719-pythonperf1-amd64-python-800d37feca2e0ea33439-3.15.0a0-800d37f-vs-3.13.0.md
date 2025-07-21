# Results vs. 3.13.0

- fork: python
- ref: 800d37feca2e0ea33439
- machine: windows-amd64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.068x faster
- HPT reliability: 92.96%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.60 sec: 1.05x slower                                                     |
| sphinx         | 617 ms                                                      | 636 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 206 ms: 1.36x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 202 ms: 1.31x faster                                                       |
| async_tree_io              | 513 ms                                                      | 392 ms: 1.31x faster                                                       |
| async_tree_none            | 219 ms                                                      | 168 ms: 1.30x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 385 ms: 1.29x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 333 ms: 1.15x faster                                                       |
| async_generators           | 223 ms                                                      | 232 ms: 1.04x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.15x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 42.7 ms: 1.19x faster                                                      |
| nbody          | 66.3 ms                                                     | 65.5 ms: 1.01x faster                                                      |
| pidigits       | 146 ms                                                      | 145 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.9 ms: 1.72x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.47 ms: 1.15x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 78.8 ms: 1.02x faster                                                      |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.2 us: 1.06x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 88.4 ms: 1.04x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| unpickle_pure_python | 130 us                                                      | 132 us: 1.02x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 54.9 ms: 1.03x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.3 ms: 1.05x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 38.4 ms: 1.05x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 212 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.7 ms: 1.05x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.7 ms: 1.17x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.44 ms: 1.02x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.0 ms: 1.01x faster                                                      |
| django_template | 20.3 ms                                                     | 24.5 ms: 1.21x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 496 us: 17.06x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 30.4 ms: 2.47x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                       |
| mdp                        | 1.43 sec                                                    | 804 ms: 1.78x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.9 ms: 1.72x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 206 ms: 1.36x faster                                                       |
| deepcopy                   | 223 us                                                      | 167 us: 1.33x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 17.5 us: 1.32x faster                                                      |
| async_tree_memoization     | 265 ms                                                      | 202 ms: 1.31x faster                                                       |
| async_tree_io              | 513 ms                                                      | 392 ms: 1.31x faster                                                       |
| async_tree_none            | 219 ms                                                      | 168 ms: 1.30x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 385 ms: 1.29x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                       |
| float                      | 50.8 ms                                                     | 42.7 ms: 1.19x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.47 ms: 1.15x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 333 ms: 1.15x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.80 us: 1.12x faster                                                      |
| json                       | 3.30 ms                                                     | 2.99 ms: 1.10x faster                                                      |
| go                         | 84.7 ms                                                     | 77.0 ms: 1.10x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.47 ms: 1.08x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.06x faster                                                      |
| pylint                     | 205 ms                                                      | 195 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.48 ms: 1.05x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 88.4 ms: 1.04x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 78.8 ms: 1.02x faster                                                      |
| mako                       | 6.56 ms                                                     | 6.44 ms: 1.02x faster                                                      |
| typing_runtime_protocols   | 103 us                                                      | 101 us: 1.02x faster                                                       |
| genshi_text                | 15.2 ms                                                     | 15.0 ms: 1.01x faster                                                      |
| nbody                      | 66.3 ms                                                     | 65.5 ms: 1.01x faster                                                      |
| pidigits                   | 146 ms                                                      | 145 ms: 1.01x faster                                                       |
| sympy_expand               | 286 ms                                                      | 284 ms: 1.00x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.1 ms: 1.01x slower                                                      |
| pyflate                    | 283 ms                                                      | 285 ms: 1.01x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 40.5 ms: 1.01x slower                                                      |
| sympy_str                  | 167 ms                                                      | 168 ms: 1.01x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 55.1 ns: 1.01x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 77.0 ms: 1.01x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 490 ms: 1.01x slower                                                       |
| shortest_path              | 355 ms                                                      | 360 ms: 1.01x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| unpickle_pure_python       | 130 us                                                      | 132 us: 1.02x slower                                                       |
| richards                   | 26.3 ms                                                     | 26.8 ms: 1.02x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.4 ms: 1.02x slower                                                      |
| 2to3                       | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 54.9 ms: 1.03x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.00 sec: 1.03x slower                                                     |
| scimark_lu                 | 56.7 ms                                                     | 58.3 ms: 1.03x slower                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.95 sec: 1.03x slower                                                     |
| sympy_sum                  | 85.2 ms                                                     | 87.6 ms: 1.03x slower                                                      |
| sphinx                     | 617 ms                                                      | 636 ms: 1.03x slower                                                       |
| connected_components       | 320 ms                                                      | 330 ms: 1.03x slower                                                       |
| comprehensions             | 10.4 us                                                     | 10.7 us: 1.03x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 65.6 ms: 1.03x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 843 us: 1.04x slower                                                       |
| richards_super             | 29.8 ms                                                     | 31.0 ms: 1.04x slower                                                      |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| async_generators           | 223 ms                                                      | 232 ms: 1.04x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.60 sec: 1.05x slower                                                     |
| logging_simple             | 5.77 us                                                     | 6.04 us: 1.05x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.46 us: 1.05x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.3 ms: 1.05x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.03 ms: 1.05x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 38.4 ms: 1.05x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.7 ms: 1.05x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 48.7 ms: 1.07x slower                                                      |
| fannkuch                   | 252 ms                                                      | 270 ms: 1.07x slower                                                       |
| chaos                      | 37.9 ms                                                     | 40.9 ms: 1.08x slower                                                      |
| scimark_fft                | 175 ms                                                      | 189 ms: 1.08x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.33 ms: 1.08x slower                                                      |
| coverage                   | 45.3 ms                                                     | 49.6 ms: 1.10x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 61.5 ms: 1.10x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.16 ms: 1.10x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 94.5 ms: 1.12x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 212 us: 1.14x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.15x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.17 ms: 1.15x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.7 ms: 1.17x slower                                                      |
| raytrace                   | 153 ms                                                      | 181 ms: 1.18x slower                                                       |
| many_optionals             | 361 us                                                      | 435 us: 1.21x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.5 ms: 1.21x slower                                                      |
| subparsers                 | 10.9 ms                                                     | 17.0 ms: 1.57x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (8): sympy_integrate, json_dumps, meteor_contest, html5lib, genshi_xml, sqlite_synth, k_core, pycparser
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250719-3.15.0a0-800d37f/bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.068x faster

# HPT report

- Reliability score: 92.96% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown