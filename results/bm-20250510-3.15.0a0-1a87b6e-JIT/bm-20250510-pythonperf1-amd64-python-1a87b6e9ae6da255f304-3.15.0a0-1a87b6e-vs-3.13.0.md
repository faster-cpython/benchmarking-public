# Results vs. 3.13.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: windows-amd64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.017x slower
- HPT reliability: 50.94%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 227 ms: 1.06x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.69 sec: 1.10x slower                                                     |
| sphinx         | 617 ms                                                      | 658 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.87x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                       |
| async_tree_io              | 513 ms                                                      | 398 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 208 ms: 1.27x faster                                                       |
| async_tree_none            | 219 ms                                                      | 173 ms: 1.27x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 399 ms: 1.25x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 335 ms: 1.14x faster                                                       |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                      |
| async_generators           | 223 ms                                                      | 256 ms: 1.15x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.4 ms: 1.15x faster                                                      |
| nbody          | 66.3 ms                                                     | 58.0 ms: 1.14x faster                                                      |
| pidigits       | 146 ms                                                      | 149 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.9 ms: 1.71x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.57 ms: 1.08x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 79.6 ms: 1.01x faster                                                      |
| regex_dna      | 115 ms                                                      | 118 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.16 sec: 1.18x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 118 us: 1.10x faster                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 51.4 ms: 1.04x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.8 us: 1.02x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 90.8 ms: 1.02x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 36.7 ms: 1.01x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.3 ms: 1.06x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 6.75 ms: 1.09x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 209 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.7 ms: 1.09x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 20.0 ms: 1.18x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.66 ms: 1.16x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                      |
| genshi_xml      | 33.9 ms                                                     | 34.9 ms: 1.03x slower                                                      |
| django_template | 20.3 ms                                                     | 24.5 ms: 1.21x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 32.6 ms: 2.31x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.87x faster                                                       |
| mdp                        | 1.43 sec                                                    | 802 ms: 1.78x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.9 ms: 1.71x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                       |
| async_tree_io              | 513 ms                                                      | 398 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 208 ms: 1.27x faster                                                       |
| deepcopy                   | 223 us                                                      | 176 us: 1.27x faster                                                       |
| async_tree_none            | 219 ms                                                      | 173 ms: 1.27x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 399 ms: 1.25x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 19.0 us: 1.22x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.18x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.16 sec: 1.18x faster                                                     |
| mako                       | 6.56 ms                                                     | 5.66 ms: 1.16x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| float                      | 50.8 ms                                                     | 44.4 ms: 1.15x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 335 ms: 1.14x faster                                                       |
| nbody                      | 66.3 ms                                                     | 58.0 ms: 1.14x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.30 ms: 1.13x faster                                                      |
| scimark_fft                | 175 ms                                                      | 156 ms: 1.12x faster                                                       |
| json                       | 3.30 ms                                                     | 2.99 ms: 1.10x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.40 ms: 1.10x faster                                                      |
| unpickle_pure_python       | 130 us                                                      | 118 us: 1.10x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.85 us: 1.09x faster                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.63 sec: 1.09x faster                                                     |
| regex_effbot               | 1.69 ms                                                     | 1.57 ms: 1.08x faster                                                      |
| go                         | 84.7 ms                                                     | 79.6 ms: 1.06x faster                                                      |
| pyflate                    | 283 ms                                                      | 268 ms: 1.06x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 60.9 ms: 1.04x faster                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 51.4 ms: 1.04x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.63 sec: 1.04x faster                                                     |
| json_loads                 | 15.1 us                                                     | 14.8 us: 1.02x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 74.9 ms: 1.02x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 90.8 ms: 1.02x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 79.6 ms: 1.01x faster                                                      |
| fannkuch                   | 252 ms                                                      | 249 ms: 1.01x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.58 us: 1.01x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 36.7 ms: 1.01x slower                                                      |
| shortest_path              | 355 ms                                                      | 358 ms: 1.01x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                      |
| pidigits                   | 146 ms                                                      | 149 ms: 1.02x slower                                                       |
| connected_components       | 320 ms                                                      | 326 ms: 1.02x slower                                                       |
| chaos                      | 37.9 ms                                                     | 38.7 ms: 1.02x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.6 ms: 1.02x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.4 ms: 1.02x slower                                                      |
| sympy_str                  | 167 ms                                                      | 171 ms: 1.03x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 46.9 ms: 1.03x slower                                                      |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.03x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 34.9 ms: 1.03x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 87.8 ms: 1.03x slower                                                      |
| sympy_expand               | 286 ms                                                      | 297 ms: 1.04x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 108 us: 1.05x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 59.5 ms: 1.05x slower                                                      |
| richards                   | 26.3 ms                                                     | 27.6 ms: 1.05x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 75.8 ms: 1.05x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 42.3 ms: 1.05x slower                                                      |
| 2to3                       | 215 ms                                                      | 227 ms: 1.06x slower                                                       |
| richards_super             | 29.8 ms                                                     | 31.6 ms: 1.06x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.3 ms: 1.06x slower                                                      |
| sphinx                     | 617 ms                                                      | 658 ms: 1.07x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 60.1 ms: 1.07x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 876 us: 1.08x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.75 ms: 1.09x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.34 ms: 1.09x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.20 ms: 1.09x slower                                                      |
| python_startup             | 24.4 ms                                                     | 26.7 ms: 1.09x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.69 sec: 1.10x slower                                                     |
| comprehensions             | 10.4 us                                                     | 11.5 us: 1.11x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.19 ms: 1.11x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 209 us: 1.12x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.50 us: 1.13x slower                                                      |
| logging_format             | 6.18 us                                                     | 7.00 us: 1.13x slower                                                      |
| raytrace                   | 153 ms                                                      | 175 ms: 1.14x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.16 ms: 1.14x slower                                                      |
| async_generators           | 223 ms                                                      | 256 ms: 1.15x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 97.1 ms: 1.15x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 20.0 ms: 1.18x slower                                                      |
| django_template            | 20.3 ms                                                     | 24.5 ms: 1.21x slower                                                      |
| many_optionals             | 361 us                                                      | 448 us: 1.24x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 17.4 ms: 1.61x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 328 ns: 6.02x slower                                                       |
| coverage                   | 45.3 ms                                                     | 300 ms: 6.62x slower                                                       |
| thrift                     | 8.47 ms                                                     | 100 ms: 11.87x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (6): html5lib, pylint, pprint_safe_repr, scimark_monte_carlo, pycparser, pprint_pformat
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.017x slower

# HPT report

- Reliability score: 50.94% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown