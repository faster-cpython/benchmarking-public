# Results vs. 3.13.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: windows-amd64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.114x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 212 ms: 1.01x faster                                                       |
| docutils       | 1.53 sec                                                    | 1.56 sec: 1.02x slower                                                     |
| html5lib       | 38.2 ms                                                     | 34.4 ms: 1.11x faster                                                      |
| sphinx         | 617 ms                                                      | 604 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 163 ms: 1.85x faster                                                       |
| async_tree_none            | 219 ms                                                      | 151 ms: 1.45x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 197 ms: 1.42x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 188 ms: 1.41x faster                                                       |
| async_tree_io              | 513 ms                                                      | 366 ms: 1.40x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 358 ms: 1.39x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 153 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 315 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 319 ms: 1.20x faster                                                       |
| async_generators           | 223 ms                                                      | 194 ms: 1.15x faster                                                       |
| coroutines                 | 12.5 ms                                                     | 11.5 ms: 1.09x faster                                                      |
| Geometric mean             | (ref)                                                       | 1.34x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 38.0 ms: 1.34x faster                                                      |
| nbody          | 66.3 ms                                                     | 52.5 ms: 1.26x faster                                                      |
| pidigits       | 146 ms                                                      | 146 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.0 ms: 1.84x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 68.1 ms: 1.18x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.63 ms: 1.04x faster                                                      |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.04 sec: 1.32x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 103 us: 1.26x faster                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 47.9 ms: 1.12x faster                                                      |
| pickle_pure_python   | 186 us                                                      | 167 us: 1.11x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 33.2 ms: 1.10x faster                                                      |
| json_dumps           | 6.19 ms                                                     | 5.90 ms: 1.05x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.6 us: 1.04x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 90.9 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 61.8 ms: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 27.1 ms: 1.11x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 20.4 ms: 1.20x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text    | 15.2 ms                                                     | 11.4 ms: 1.33x faster                                                      |
| genshi_xml     | 33.9 ms                                                     | 27.7 ms: 1.22x faster                                                      |
| mako           | 6.56 ms                                                     | 5.94 ms: 1.11x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 30.9 ms: 2.44x faster                                                      |
| mdp                        | 1.43 sec                                                    | 684 ms: 2.09x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 163 ms: 1.85x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.0 ms: 1.84x faster                                                      |
| deepcopy_memo              | 23.1 us                                                     | 13.3 us: 1.74x faster                                                      |
| deepcopy                   | 223 us                                                      | 137 us: 1.63x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 49.0 ms: 1.56x faster                                                      |
| async_tree_none            | 219 ms                                                      | 151 ms: 1.45x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 28.2 ms: 1.45x faster                                                      |
| go                         | 84.7 ms                                                     | 59.5 ms: 1.42x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 197 ms: 1.42x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 188 ms: 1.41x faster                                                       |
| async_tree_io              | 513 ms                                                      | 366 ms: 1.40x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 358 ms: 1.39x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.48 us: 1.37x faster                                                      |
| float                      | 50.8 ms                                                     | 38.0 ms: 1.34x faster                                                      |
| genshi_text                | 15.2 ms                                                     | 11.4 ms: 1.33x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.04 sec: 1.32x faster                                                     |
| spectral_norm              | 63.4 ms                                                     | 48.1 ms: 1.32x faster                                                      |
| hexiom                     | 3.84 ms                                                     | 2.92 ms: 1.32x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 153 ms: 1.31x faster                                                       |
| generators                 | 19.0 ms                                                     | 14.7 ms: 1.29x faster                                                      |
| fannkuch                   | 252 ms                                                      | 199 ms: 1.27x faster                                                       |
| nbody                      | 66.3 ms                                                     | 52.5 ms: 1.26x faster                                                      |
| unpickle_pure_python       | 130 us                                                      | 103 us: 1.26x faster                                                       |
| scimark_lu                 | 56.7 ms                                                     | 45.1 ms: 1.26x faster                                                      |
| pprint_safe_repr           | 485 ms                                                      | 395 ms: 1.23x faster                                                       |
| genshi_xml                 | 33.9 ms                                                     | 27.7 ms: 1.22x faster                                                      |
| richards                   | 26.3 ms                                                     | 21.4 ms: 1.22x faster                                                      |
| pprint_pformat             | 977 ms                                                      | 805 ms: 1.21x faster                                                       |
| chaos                      | 37.9 ms                                                     | 31.2 ms: 1.21x faster                                                      |
| deltablue                  | 1.89 ms                                                     | 1.56 ms: 1.21x faster                                                      |
| richards_super             | 29.8 ms                                                     | 24.6 ms: 1.21x faster                                                      |
| scimark_fft                | 175 ms                                                      | 145 ms: 1.21x faster                                                       |
| pyflate                    | 283 ms                                                      | 234 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 315 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 319 ms: 1.20x faster                                                       |
| nqueens                    | 56.1 ms                                                     | 47.3 ms: 1.19x faster                                                      |
| comprehensions             | 10.4 us                                                     | 8.73 us: 1.19x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 68.1 ms: 1.18x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.12 ms: 1.18x faster                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 39.6 ms: 1.15x faster                                                      |
| async_generators           | 223 ms                                                      | 194 ms: 1.15x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.51 sec: 1.14x faster                                                     |
| typing_runtime_protocols   | 103 us                                                      | 91.7 us: 1.13x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.31 ms: 1.13x faster                                                      |
| json                       | 3.30 ms                                                     | 2.94 ms: 1.12x faster                                                      |
| sympy_expand               | 286 ms                                                      | 255 ms: 1.12x faster                                                       |
| sympy_str                  | 167 ms                                                      | 149 ms: 1.12x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 47.9 ms: 1.12x faster                                                      |
| pickle_pure_python         | 186 us                                                      | 167 us: 1.11x faster                                                       |
| html5lib                   | 38.2 ms                                                     | 34.4 ms: 1.11x faster                                                      |
| sympy_integrate            | 12.3 ms                                                     | 11.1 ms: 1.11x faster                                                      |
| mako                       | 6.56 ms                                                     | 5.94 ms: 1.11x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 33.2 ms: 1.10x faster                                                      |
| coroutines                 | 12.5 ms                                                     | 11.5 ms: 1.09x faster                                                      |
| pylint                     | 205 ms                                                      | 189 ms: 1.09x faster                                                       |
| meteor_contest             | 72.0 ms                                                     | 66.3 ms: 1.09x faster                                                      |
| sympy_sum                  | 85.2 ms                                                     | 78.6 ms: 1.08x faster                                                      |
| pycparser                  | 695 ms                                                      | 651 ms: 1.07x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.90 ms: 1.05x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.63 ms: 1.04x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.63 sec: 1.04x faster                                                     |
| json_loads                 | 15.1 us                                                     | 14.6 us: 1.04x faster                                                      |
| dulwich_log                | 40.1 ms                                                     | 38.9 ms: 1.03x faster                                                      |
| sphinx                     | 617 ms                                                      | 604 ms: 1.02x faster                                                       |
| shortest_path              | 355 ms                                                      | 349 ms: 1.02x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.56 us: 1.02x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 90.9 ms: 1.01x faster                                                      |
| 2to3                       | 215 ms                                                      | 212 ms: 1.01x faster                                                       |
| raytrace                   | 153 ms                                                      | 151 ms: 1.01x faster                                                       |
| logging_simple             | 5.77 us                                                     | 5.74 us: 1.01x faster                                                      |
| pidigits                   | 146 ms                                                      | 146 ms: 1.00x faster                                                       |
| docutils                   | 1.53 sec                                                    | 1.56 sec: 1.02x slower                                                     |
| xml_etree_iterparse        | 60.5 ms                                                     | 61.8 ms: 1.02x slower                                                      |
| connected_components       | 320 ms                                                      | 328 ms: 1.03x slower                                                       |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.03x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 853 us: 1.05x slower                                                       |
| python_startup             | 24.4 ms                                                     | 27.1 ms: 1.11x slower                                                      |
| many_optionals             | 361 us                                                      | 410 us: 1.13x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 98.4 ms: 1.17x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.45 ms: 1.18x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 20.4 ms: 1.20x slower                                                      |
| subparsers                 | 10.9 ms                                                     | 15.5 ms: 1.43x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.89 ms: 1.47x slower                                                      |
| coverage                   | 45.3 ms                                                     | 219 ms: 4.82x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 273 ns: 5.01x slower                                                       |
| thrift                     | 8.47 ms                                                     | 95.0 ms: 11.22x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (2): logging_format, django_template
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.114x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown