# Results vs. 3.13.0

- fork: python
- ref: 75f40595e555e7d016cf
- machine: windows-amd64
- commit hash: 75f4059
- commit date: 2025-06-30
- overall geometric mean: 1.076x faster
- HPT reliability: 75.88%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 221 ms: 1.03x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.68 sec: 1.10x slower                                                     |
| html5lib       | 38.2 ms                                                     | 38.8 ms: 1.02x slower                                                      |
| sphinx         | 617 ms                                                      | 653 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.88x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.33x faster                                                       |
| async_tree_io              | 513 ms                                                      | 400 ms: 1.28x faster                                                       |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 208 ms: 1.27x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 391 ms: 1.27x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                       |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 53.7 ms: 1.23x faster                                                      |
| float          | 50.8 ms                                                     | 44.9 ms: 1.13x faster                                                      |
| pidigits       | 146 ms                                                      | 147 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.0 ms: 1.70x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.64 ms: 1.03x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 78.9 ms: 1.02x faster                                                      |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.14 sec: 1.21x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 108 us: 1.20x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 51.2 ms: 1.04x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 88.9 ms: 1.04x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 35.9 ms: 1.02x faster                                                      |
| json_dumps           | 6.19 ms                                                     | 6.28 ms: 1.01x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.9 ms: 1.06x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 205 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.0 ms: 1.07x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.39 ms: 1.22x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.6 ms: 1.03x slower                                                      |
| genshi_xml      | 33.9 ms                                                     | 35.2 ms: 1.04x slower                                                      |
| django_template | 20.3 ms                                                     | 24.3 ms: 1.20x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 490 us: 17.28x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 31.7 ms: 2.38x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.88x faster                                                       |
| mdp                        | 1.43 sec                                                    | 803 ms: 1.78x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.0 ms: 1.70x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.33x faster                                                       |
| deepcopy                   | 223 us                                                      | 169 us: 1.32x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.0 us: 1.28x faster                                                      |
| async_tree_io              | 513 ms                                                      | 400 ms: 1.28x faster                                                       |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 208 ms: 1.27x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 391 ms: 1.27x faster                                                       |
| nbody                      | 66.3 ms                                                     | 53.7 ms: 1.23x faster                                                      |
| mako                       | 6.56 ms                                                     | 5.39 ms: 1.22x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.14 sec: 1.21x faster                                                     |
| unpickle_pure_python       | 130 us                                                      | 108 us: 1.20x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.18x faster                                                       |
| scimark_fft                | 175 ms                                                      | 151 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.15x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.27 ms: 1.15x faster                                                      |
| float                      | 50.8 ms                                                     | 44.9 ms: 1.13x faster                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.56 sec: 1.12x faster                                                     |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                       |
| fannkuch                   | 252 ms                                                      | 228 ms: 1.10x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.41 ms: 1.10x faster                                                      |
| json                       | 3.30 ms                                                     | 3.01 ms: 1.10x faster                                                      |
| pyflate                    | 283 ms                                                      | 258 ms: 1.10x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.85 us: 1.09x faster                                                      |
| go                         | 84.7 ms                                                     | 78.8 ms: 1.07x faster                                                      |
| pprint_safe_repr           | 485 ms                                                      | 453 ms: 1.07x faster                                                       |
| pprint_pformat             | 977 ms                                                      | 931 ms: 1.05x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 51.2 ms: 1.04x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 88.9 ms: 1.04x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.64 sec: 1.03x faster                                                     |
| regex_effbot               | 1.69 ms                                                     | 1.64 ms: 1.03x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 78.9 ms: 1.02x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 35.9 ms: 1.02x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.56 us: 1.02x faster                                                      |
| meteor_contest             | 72.0 ms                                                     | 71.1 ms: 1.01x faster                                                      |
| pidigits                   | 146 ms                                                      | 147 ms: 1.01x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.1 ms: 1.01x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.28 ms: 1.01x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 38.8 ms: 1.02x slower                                                      |
| shortest_path              | 355 ms                                                      | 361 ms: 1.02x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 55.6 ns: 1.02x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 87.0 ms: 1.02x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 46.6 ms: 1.02x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.6 ms: 1.02x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 41.1 ms: 1.02x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 15.6 ms: 1.03x slower                                                      |
| 2to3                       | 215 ms                                                      | 221 ms: 1.03x slower                                                       |
| sympy_str                  | 167 ms                                                      | 172 ms: 1.03x slower                                                       |
| connected_components       | 320 ms                                                      | 329 ms: 1.03x slower                                                       |
| sympy_expand               | 286 ms                                                      | 296 ms: 1.04x slower                                                       |
| comprehensions             | 10.4 us                                                     | 10.7 us: 1.04x slower                                                      |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.7 ms: 1.04x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 35.2 ms: 1.04x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 79.3 ms: 1.04x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.9 ms: 1.06x slower                                                      |
| sphinx                     | 617 ms                                                      | 653 ms: 1.06x slower                                                       |
| richards                   | 26.3 ms                                                     | 27.8 ms: 1.06x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 860 us: 1.06x slower                                                       |
| python_startup             | 24.4 ms                                                     | 26.0 ms: 1.07x slower                                                      |
| richards_super             | 29.8 ms                                                     | 31.8 ms: 1.07x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 60.2 ms: 1.07x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 60.9 ms: 1.07x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.65 us: 1.08x slower                                                      |
| chaos                      | 37.9 ms                                                     | 40.8 ms: 1.08x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.24 us: 1.08x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.33 ms: 1.09x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.19 ms: 1.09x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.68 sec: 1.10x slower                                                     |
| pickle_pure_python         | 186 us                                                      | 205 us: 1.10x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.18 ms: 1.11x slower                                                      |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                       |
| coverage                   | 45.3 ms                                                     | 51.3 ms: 1.13x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 95.6 ms: 1.13x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                      |
| raytrace                   | 153 ms                                                      | 179 ms: 1.17x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.26 ms: 1.19x slower                                                      |
| django_template            | 20.3 ms                                                     | 24.3 ms: 1.20x slower                                                      |
| many_optionals             | 361 us                                                      | 451 us: 1.25x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 17.0 ms: 1.57x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (4): pylint, typing_runtime_protocols, spectral_norm, pycparser
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250630-3.15.0a0-75f4059-JIT/bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.076x faster

# HPT report

- Reliability score: 75.88% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown