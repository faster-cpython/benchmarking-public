# Results vs. 3.13.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: windows-amd64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.044x slower
- HPT reliability: 99.95%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 224 ms: 1.04x slower                                                       |
| docutils       | 1.53 sec                                                    | 2.91 sec: 1.90x slower                                                     |
| html5lib       | 38.2 ms                                                     | 39.0 ms: 1.02x slower                                                      |
| sphinx         | 617 ms                                                      | 688 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                       | 1.23x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 143 ms: 2.10x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 329 ms: 1.51x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 190 ms: 1.48x faster                                                       |
| async_tree_io              | 513 ms                                                      | 350 ms: 1.47x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 147 ms: 1.36x faster                                                       |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 208 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 312 ms: 1.23x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                       |
| coroutines                 | 12.5 ms                                                     | 13.1 ms: 1.05x slower                                                      |
| async_generators           | 223 ms                                                      | 260 ms: 1.17x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.30x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.6 ms: 1.12x faster                                                      |
| pidigits       | 146 ms                                                      | 139 ms: 1.05x faster                                                       |
| nbody          | 66.3 ms                                                     | 76.9 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.4 ms: 1.78x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.56 ms: 1.08x faster                                                      |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 91.4 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 60.5 ms                                                     | 59.0 ms: 1.03x faster                                                      |
| json_loads           | 15.1 us                                                     | 16.7 us: 1.10x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 62.2 ms: 1.16x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 152 us: 1.17x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 7.28 ms: 1.18x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 228 us: 1.23x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 44.8 ms: 1.23x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 2.58 sec: 1.88x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.19x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.6 ms: 1.09x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 20.1 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 37.6 ms: 1.11x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 18.4 ms: 1.21x slower                                                      |
| django_template | 20.3 ms                                                     | 26.2 ms: 1.29x slower                                                      |
| mako            | 6.56 ms                                                     | 9.69 ms: 1.48x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.26x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 577 us: 14.68x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 32.0 ms: 2.35x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 143 ms: 2.10x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.4 ms: 1.78x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 329 ms: 1.51x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 190 ms: 1.48x faster                                                       |
| async_tree_io              | 513 ms                                                      | 350 ms: 1.47x faster                                                       |
| gc_traversal               | 1.96 ms                                                     | 1.36 ms: 1.45x faster                                                      |
| mdp                        | 1.43 sec                                                    | 1.03 sec: 1.39x faster                                                     |
| async_tree_none_tg         | 200 ms                                                      | 147 ms: 1.36x faster                                                       |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 208 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 312 ms: 1.23x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.36 us: 1.17x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.08 ms: 1.14x faster                                                      |
| deepcopy                   | 223 us                                                      | 197 us: 1.14x faster                                                       |
| float                      | 50.8 ms                                                     | 45.6 ms: 1.12x faster                                                      |
| deepcopy_memo              | 23.1 us                                                     | 20.8 us: 1.11x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.56 ms: 1.08x faster                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 79.5 ms: 1.06x faster                                                      |
| pidigits                   | 146 ms                                                      | 139 ms: 1.05x faster                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 59.0 ms: 1.03x faster                                                      |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 63.8 ms: 1.01x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 39.0 ms: 1.02x slower                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 2.08 us: 1.03x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 41.5 ms: 1.03x slower                                                      |
| 2to3                       | 215 ms                                                      | 224 ms: 1.04x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.1 ms: 1.05x slower                                                      |
| go                         | 84.7 ms                                                     | 90.7 ms: 1.07x slower                                                      |
| python_startup             | 24.4 ms                                                     | 26.6 ms: 1.09x slower                                                      |
| telco                      | 4.85 ms                                                     | 5.30 ms: 1.09x slower                                                      |
| json_loads                 | 15.1 us                                                     | 16.7 us: 1.10x slower                                                      |
| pyflate                    | 283 ms                                                      | 313 ms: 1.11x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 37.6 ms: 1.11x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 84.7 ms: 1.11x slower                                                      |
| sphinx                     | 617 ms                                                      | 688 ms: 1.11x slower                                                       |
| sympy_str                  | 167 ms                                                      | 187 ms: 1.12x slower                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.94 ms: 1.13x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 91.4 ms: 1.13x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 96.7 ms: 1.14x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 64.4 ms: 1.14x slower                                                      |
| sympy_expand               | 286 ms                                                      | 325 ms: 1.14x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 14.1 ms: 1.14x slower                                                      |
| scimark_fft                | 175 ms                                                      | 200 ms: 1.14x slower                                                       |
| chaos                      | 37.9 ms                                                     | 43.8 ms: 1.16x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 561 ms: 1.16x slower                                                       |
| nbody                      | 66.3 ms                                                     | 76.9 ms: 1.16x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 62.2 ms: 1.16x slower                                                      |
| fannkuch                   | 252 ms                                                      | 293 ms: 1.16x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 152 us: 1.17x slower                                                       |
| async_generators           | 223 ms                                                      | 260 ms: 1.17x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 7.28 ms: 1.18x slower                                                      |
| logging_format             | 6.18 us                                                     | 7.30 us: 1.18x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.54 ms: 1.18x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 20.1 ms: 1.19x slower                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 48.4 ms: 1.19x slower                                                      |
| generators                 | 19.0 ms                                                     | 22.6 ms: 1.19x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.88 us: 1.19x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 18.4 ms: 1.21x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.30 ms: 1.21x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 68.2 ms: 1.22x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 55.7 ms: 1.22x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 88.1 ms: 1.22x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 228 us: 1.23x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 44.8 ms: 1.23x slower                                                      |
| richards                   | 26.3 ms                                                     | 32.2 ms: 1.23x slower                                                      |
| comprehensions             | 10.4 us                                                     | 12.8 us: 1.23x slower                                                      |
| richards_super             | 29.8 ms                                                     | 37.4 ms: 1.26x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 130 us: 1.26x slower                                                       |
| django_template            | 20.3 ms                                                     | 26.2 ms: 1.29x slower                                                      |
| many_optionals             | 361 us                                                      | 471 us: 1.30x slower                                                       |
| raytrace                   | 153 ms                                                      | 205 ms: 1.34x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 1.10 ms: 1.36x slower                                                      |
| mako                       | 6.56 ms                                                     | 9.69 ms: 1.48x slower                                                      |
| coverage                   | 45.3 ms                                                     | 68.2 ms: 1.50x slower                                                      |
| k_core                     | 1.70 sec                                                    | 2.71 sec: 1.60x slower                                                     |
| subparsers                 | 10.9 ms                                                     | 18.4 ms: 1.70x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.74 sec: 1.78x slower                                                     |
| shortest_path              | 355 ms                                                      | 646 ms: 1.82x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 5.38 sec: 1.87x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 2.58 sec: 1.88x slower                                                     |
| docutils                   | 1.53 sec                                                    | 2.91 sec: 1.90x slower                                                     |
| connected_components       | 320 ms                                                      | 617 ms: 1.93x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 368 ns: 6.75x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (4): json, pylint, xml_etree_parse, pycparser
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.044x slower

# HPT report

- Reliability score: 99.95% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown