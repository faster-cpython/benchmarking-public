# Results vs. 3.13.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: windows-amd64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.023x slower
- HPT reliability: 93.33%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 225 ms: 1.04x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                     |
| html5lib       | 38.2 ms                                                     | 39.0 ms: 1.02x slower                                                      |
| sphinx         | 617 ms                                                      | 650 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                       |
| async_tree_io              | 513 ms                                                      | 398 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                       |
| async_tree_none            | 219 ms                                                      | 173 ms: 1.27x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 394 ms: 1.26x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 341 ms: 1.12x faster                                                       |
| async_generators           | 223 ms                                                      | 234 ms: 1.05x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.3 ms: 1.17x faster                                                      |
| nbody          | 66.3 ms                                                     | 61.9 ms: 1.07x faster                                                      |
| pidigits       | 146 ms                                                      | 149 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.3 ms: 1.66x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 80.4 ms: 1.00x faster                                                      |
| regex_dna      | 115 ms                                                      | 120 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 90.7 ms: 1.02x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 130 us: 1.00x slower                                                       |
| json_loads           | 15.1 us                                                     | 15.4 us: 1.02x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 56.3 ms: 1.05x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.2 ms: 1.06x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 6.64 ms: 1.07x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 39.8 ms: 1.09x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 208 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.3 ms: 1.08x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.8 ms: 1.17x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.3 ms: 1.01x slower                                                      |
| django_template | 20.3 ms                                                     | 24.0 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 32.6 ms: 2.31x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                       |
| mdp                        | 1.43 sec                                                    | 792 ms: 1.81x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.3 ms: 1.66x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                       |
| deepcopy                   | 223 us                                                      | 173 us: 1.29x faster                                                       |
| async_tree_io              | 513 ms                                                      | 398 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                       |
| async_tree_none            | 219 ms                                                      | 173 ms: 1.27x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 394 ms: 1.26x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.9 us: 1.22x faster                                                      |
| float                      | 50.8 ms                                                     | 43.3 ms: 1.17x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 341 ms: 1.12x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 57.0 ms: 1.11x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                      |
| go                         | 84.7 ms                                                     | 77.2 ms: 1.10x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.86 us: 1.09x faster                                                      |
| json                       | 3.30 ms                                                     | 3.06 ms: 1.08x faster                                                      |
| nbody                      | 66.3 ms                                                     | 61.9 ms: 1.07x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.59 ms: 1.06x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 72.7 ms: 1.05x faster                                                      |
| fannkuch                   | 252 ms                                                      | 242 ms: 1.04x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.3 ms: 1.04x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.53 ms: 1.03x faster                                                      |
| scimark_fft                | 175 ms                                                      | 170 ms: 1.03x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 90.7 ms: 1.02x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 80.4 ms: 1.00x faster                                                      |
| unpickle_pure_python       | 130 us                                                      | 130 us: 1.00x slower                                                       |
| chaos                      | 37.9 ms                                                     | 38.0 ms: 1.00x slower                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.89 sec: 1.00x slower                                                     |
| genshi_text                | 15.2 ms                                                     | 15.3 ms: 1.01x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 57.1 ms: 1.01x slower                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.60 us: 1.01x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 990 ms: 1.01x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.01x slower                                                      |
| pidigits                   | 146 ms                                                      | 149 ms: 1.02x slower                                                       |
| k_core                     | 1.70 sec                                                    | 1.73 sec: 1.02x slower                                                     |
| sympy_str                  | 167 ms                                                      | 170 ms: 1.02x slower                                                       |
| sympy_expand               | 286 ms                                                      | 292 ms: 1.02x slower                                                       |
| json_loads                 | 15.1 us                                                     | 15.4 us: 1.02x slower                                                      |
| shortest_path              | 355 ms                                                      | 363 ms: 1.02x slower                                                       |
| richards                   | 26.3 ms                                                     | 26.8 ms: 1.02x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 39.0 ms: 1.02x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.5 ms: 1.03x slower                                                      |
| pycparser                  | 695 ms                                                      | 718 ms: 1.03x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 74.4 ms: 1.03x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 3.98 ms: 1.04x slower                                                      |
| connected_components       | 320 ms                                                      | 331 ms: 1.04x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 107 us: 1.04x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 88.3 ms: 1.04x slower                                                      |
| richards_super             | 29.8 ms                                                     | 30.9 ms: 1.04x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 47.5 ms: 1.04x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 41.9 ms: 1.04x slower                                                      |
| 2to3                       | 215 ms                                                      | 225 ms: 1.04x slower                                                       |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.05x slower                                                       |
| async_generators           | 223 ms                                                      | 234 ms: 1.05x slower                                                       |
| sphinx                     | 617 ms                                                      | 650 ms: 1.05x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 56.3 ms: 1.05x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.2 ms: 1.06x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 60.0 ms: 1.07x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.31 ms: 1.07x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.64 ms: 1.07x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 872 us: 1.08x slower                                                       |
| python_startup             | 24.4 ms                                                     | 26.3 ms: 1.08x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                     |
| xml_etree_process          | 36.5 ms                                                     | 39.8 ms: 1.09x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                      |
| comprehensions             | 10.4 us                                                     | 11.3 us: 1.09x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.17 ms: 1.11x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.10 ms: 1.11x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.44 us: 1.11x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 208 us: 1.12x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.92 us: 1.12x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 97.2 ms: 1.15x slower                                                      |
| raytrace                   | 153 ms                                                      | 179 ms: 1.17x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.8 ms: 1.17x slower                                                      |
| django_template            | 20.3 ms                                                     | 24.0 ms: 1.18x slower                                                      |
| many_optionals             | 361 us                                                      | 440 us: 1.22x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.9 ms: 1.56x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 318 ns: 5.83x slower                                                       |
| coverage                   | 45.3 ms                                                     | 290 ms: 6.40x slower                                                       |
| thrift                     | 8.47 ms                                                     | 102 ms: 12.09x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (6): pylint, pyflate, tomli_loads, pprint_safe_repr, mako, genshi_xml
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.023x slower

# HPT report

- Reliability score: 93.33% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown