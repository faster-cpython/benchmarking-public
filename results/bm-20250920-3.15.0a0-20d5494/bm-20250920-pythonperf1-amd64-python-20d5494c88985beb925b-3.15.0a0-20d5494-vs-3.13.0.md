# Results vs. 3.13.0

- fork: python
- ref: 20d5494c88985beb925b
- machine: windows-amd64
- commit hash: 20d5494
- commit date: 2025-09-20
- overall geometric mean: 1.050x faster
- HPT reliability: 66.39%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 217 ms: 1.01x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.60 sec: 1.04x slower                                                     |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 170 ms: 1.76x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 238 ms: 1.18x faster                                                       |
| async_tree_io              | 513 ms                                                      | 444 ms: 1.15x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 432 ms: 1.15x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 233 ms: 1.14x faster                                                       |
| async_tree_none            | 219 ms                                                      | 199 ms: 1.10x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 350 ms: 1.09x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 355 ms: 1.08x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 195 ms: 1.03x faster                                                       |
| async_generators           | 223 ms                                                      | 231 ms: 1.04x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.9 ms: 1.19x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.7 ms: 1.16x faster                                                      |
| nbody          | 66.3 ms                                                     | 63.7 ms: 1.04x faster                                                      |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.48 ms: 1.15x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 79.7 ms: 1.01x faster                                                      |
| regex_dna      | 115 ms                                                      | 118 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 6.19 ms                                                     | 5.42 ms: 1.14x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.0 us: 1.08x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 86.8 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.1 ms: 1.03x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 55.2 ms: 1.03x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 137 us: 1.05x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 39.0 ms: 1.07x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 212 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.2 ms: 1.03x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 18.7 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.70 ms: 1.02x slower                                                      |
| genshi_xml      | 33.9 ms                                                     | 35.5 ms: 1.05x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 16.1 ms: 1.06x slower                                                      |
| django_template | 20.3 ms                                                     | 24.7 ms: 1.22x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.08x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 504 us: 16.79x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 29.9 ms: 2.52x faster                                                      |
| mdp                        | 1.43 sec                                                    | 792 ms: 1.81x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 170 ms: 1.76x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                      |
| deepcopy                   | 223 us                                                      | 168 us: 1.33x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 17.7 us: 1.30x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 238 ms: 1.18x faster                                                       |
| float                      | 50.8 ms                                                     | 43.7 ms: 1.16x faster                                                      |
| async_tree_io              | 513 ms                                                      | 444 ms: 1.15x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 432 ms: 1.15x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.48 ms: 1.15x faster                                                      |
| json_dumps                 | 6.19 ms                                                     | 5.42 ms: 1.14x faster                                                      |
| async_tree_memoization     | 265 ms                                                      | 233 ms: 1.14x faster                                                       |
| json                       | 3.30 ms                                                     | 2.92 ms: 1.13x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.29 ms: 1.13x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.81 us: 1.12x faster                                                      |
| go                         | 84.7 ms                                                     | 76.6 ms: 1.11x faster                                                      |
| async_tree_none            | 219 ms                                                      | 199 ms: 1.10x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 350 ms: 1.09x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.0 us: 1.08x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 355 ms: 1.08x faster                                                       |
| pylint                     | 205 ms                                                      | 193 ms: 1.06x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 86.8 ms: 1.06x faster                                                      |
| dulwich_log                | 40.1 ms                                                     | 38.4 ms: 1.04x faster                                                      |
| nbody                      | 66.3 ms                                                     | 63.7 ms: 1.04x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 195 ms: 1.03x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 74.2 ms: 1.03x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.66 sec: 1.02x faster                                                     |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.54 ms: 1.02x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.8 ms: 1.02x faster                                                      |
| sympy_expand               | 286 ms                                                      | 281 ms: 1.02x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.56 us: 1.02x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 79.7 ms: 1.01x faster                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.2 ms: 1.01x faster                                                      |
| sympy_sum                  | 85.2 ms                                                     | 84.4 ms: 1.01x faster                                                      |
| sympy_str                  | 167 ms                                                      | 166 ms: 1.01x faster                                                       |
| pprint_safe_repr           | 485 ms                                                      | 487 ms: 1.01x slower                                                       |
| 2to3                       | 215 ms                                                      | 217 ms: 1.01x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 55.2 ns: 1.01x slower                                                      |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                       |
| connected_components       | 320 ms                                                      | 325 ms: 1.02x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 993 ms: 1.02x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 57.8 ms: 1.02x slower                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.93 sec: 1.02x slower                                                     |
| mako                       | 6.56 ms                                                     | 6.70 ms: 1.02x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.25 ms: 1.02x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 73.6 ms: 1.02x slower                                                      |
| shortest_path              | 355 ms                                                      | 364 ms: 1.02x slower                                                       |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.1 ms: 1.03x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.5 ms: 1.03x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 65.3 ms: 1.03x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 55.2 ms: 1.03x slower                                                      |
| logging_simple             | 5.77 us                                                     | 5.97 us: 1.03x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.2 ms: 1.03x slower                                                      |
| richards_super             | 29.8 ms                                                     | 30.8 ms: 1.03x slower                                                      |
| richards                   | 26.3 ms                                                     | 27.2 ms: 1.04x slower                                                      |
| async_generators           | 223 ms                                                      | 231 ms: 1.04x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.42 us: 1.04x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.60 sec: 1.04x slower                                                     |
| gc_traversal               | 1.96 ms                                                     | 2.05 ms: 1.04x slower                                                      |
| fannkuch                   | 252 ms                                                      | 263 ms: 1.05x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 35.5 ms: 1.05x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 47.9 ms: 1.05x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 137 us: 1.05x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 16.1 ms: 1.06x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 860 us: 1.06x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 90.0 ms: 1.07x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 39.0 ms: 1.07x slower                                                      |
| scimark_fft                | 175 ms                                                      | 187 ms: 1.07x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.2 us: 1.08x slower                                                      |
| coverage                   | 45.3 ms                                                     | 49.4 ms: 1.09x slower                                                      |
| chaos                      | 37.9 ms                                                     | 41.5 ms: 1.10x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.21 ms: 1.10x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 18.7 ms: 1.11x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 62.3 ms: 1.11x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 212 us: 1.14x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.25 ms: 1.19x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.9 ms: 1.19x slower                                                      |
| django_template            | 20.3 ms                                                     | 24.7 ms: 1.22x slower                                                      |
| raytrace                   | 153 ms                                                      | 188 ms: 1.22x slower                                                       |
| many_optionals             | 361 us                                                      | 559 us: 1.55x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 31.1 ms: 2.86x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (6): html5lib, pyflate, tomli_loads, typing_runtime_protocols, sphinx, pycparser
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250920-3.15.0a0-20d5494/bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.050x faster

# HPT report

- Reliability score: 66.39% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown