# Results vs. 3.13.0

- fork: python
- ref: 880c9526f91960b9cba5
- machine: windows-amd64
- commit hash: 880c952
- commit date: 2025-10-04
- overall geometric mean: 1.028x slower
- HPT reliability: 99.87%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 218 ms: 1.02x slower                                                       |
| docutils       | 1.53 sec                                                    | 2.81 sec: 1.84x slower                                                     |
| html5lib       | 38.2 ms                                                     | 39.4 ms: 1.03x slower                                                      |
| sphinx         | 617 ms                                                      | 685 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                       | 1.21x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 149 ms: 2.01x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 318 ms: 1.56x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 185 ms: 1.52x faster                                                       |
| async_tree_io              | 513 ms                                                      | 342 ms: 1.50x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 144 ms: 1.39x faster                                                       |
| async_tree_none            | 219 ms                                                      | 165 ms: 1.32x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 202 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 305 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 327 ms: 1.16x faster                                                       |
| async_generators           | 223 ms                                                      | 246 ms: 1.10x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.14x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.31x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.3 ms: 1.15x faster                                                      |
| pidigits       | 146 ms                                                      | 136 ms: 1.08x faster                                                       |
| nbody          | 66.3 ms                                                     | 78.1 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.3 ms: 1.79x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                      |
| regex_dna      | 115 ms                                                      | 112 ms: 1.03x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 88.7 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 60.5 ms                                                     | 58.5 ms: 1.03x faster                                                      |
| json_dumps           | 6.19 ms                                                     | 6.07 ms: 1.02x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 90.5 ms: 1.02x faster                                                      |
| json_loads           | 15.1 us                                                     | 16.0 us: 1.06x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 61.6 ms: 1.15x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 151 us: 1.17x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 43.4 ms: 1.19x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 223 us: 1.20x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 2.31 sec: 1.69x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.2 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 37.8 ms: 1.12x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 18.5 ms: 1.22x slower                                                      |
| django_template | 20.3 ms                                                     | 25.7 ms: 1.27x slower                                                      |
| mako            | 6.56 ms                                                     | 9.68 ms: 1.47x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.26x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 564 us: 15.00x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 29.2 ms: 2.58x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 149 ms: 2.01x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.3 ms: 1.79x faster                                                      |
| gc_traversal               | 1.96 ms                                                     | 1.16 ms: 1.70x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 318 ms: 1.56x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 185 ms: 1.52x faster                                                       |
| async_tree_io              | 513 ms                                                      | 342 ms: 1.50x faster                                                       |
| mdp                        | 1.43 sec                                                    | 1.00 sec: 1.42x faster                                                     |
| async_tree_none_tg         | 200 ms                                                      | 144 ms: 1.39x faster                                                       |
| async_tree_none            | 219 ms                                                      | 165 ms: 1.32x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 202 ms: 1.31x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.1 us: 1.28x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 305 ms: 1.25x faster                                                       |
| deepcopy                   | 223 us                                                      | 183 us: 1.22x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 327 ms: 1.16x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.36 us: 1.16x faster                                                      |
| float                      | 50.8 ms                                                     | 44.3 ms: 1.15x faster                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 74.4 ms: 1.13x faster                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.09 ms: 1.13x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                      |
| pidigits                   | 146 ms                                                      | 136 ms: 1.08x faster                                                       |
| json                       | 3.30 ms                                                     | 3.07 ms: 1.08x faster                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 58.5 ms: 1.03x faster                                                      |
| regex_dna                  | 115 ms                                                      | 112 ms: 1.03x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.07 ms: 1.02x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 90.5 ms: 1.02x faster                                                      |
| 2to3                       | 215 ms                                                      | 218 ms: 1.02x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 40.8 ms: 1.02x slower                                                      |
| go                         | 84.7 ms                                                     | 86.4 ms: 1.02x slower                                                      |
| scimark_fft                | 175 ms                                                      | 179 ms: 1.02x slower                                                       |
| telco                      | 4.85 ms                                                     | 4.97 ms: 1.02x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 39.4 ms: 1.03x slower                                                      |
| pyflate                    | 283 ms                                                      | 298 ms: 1.05x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 80.2 ms: 1.05x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                      |
| json_loads                 | 15.1 us                                                     | 16.0 us: 1.06x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 60.8 ms: 1.07x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 58.6 ns: 1.07x slower                                                      |
| sympy_str                  | 167 ms                                                      | 180 ms: 1.08x slower                                                       |
| sympy_expand               | 286 ms                                                      | 308 ms: 1.08x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 526 ms: 1.09x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 93.0 ms: 1.09x slower                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.84 ms: 1.09x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 88.7 ms: 1.10x slower                                                      |
| async_generators           | 223 ms                                                      | 246 ms: 1.10x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.6 ms: 1.11x slower                                                      |
| sphinx                     | 617 ms                                                      | 685 ms: 1.11x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.42 us: 1.11x slower                                                      |
| comprehensions             | 10.4 us                                                     | 11.5 us: 1.11x slower                                                      |
| generators                 | 19.0 ms                                                     | 21.1 ms: 1.11x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 37.8 ms: 1.12x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.34 ms: 1.13x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 71.7 ms: 1.13x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.99 us: 1.13x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.2 ms: 1.13x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.14x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 61.6 ms: 1.15x slower                                                      |
| fannkuch                   | 252 ms                                                      | 293 ms: 1.16x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 151 us: 1.17x slower                                                       |
| nbody                      | 66.3 ms                                                     | 78.1 ms: 1.18x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 85.2 ms: 1.18x slower                                                      |
| richards                   | 26.3 ms                                                     | 31.1 ms: 1.18x slower                                                      |
| chaos                      | 37.9 ms                                                     | 45.0 ms: 1.19x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 43.4 ms: 1.19x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 54.5 ms: 1.19x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 223 us: 1.20x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 49.0 ms: 1.20x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 125 us: 1.21x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 18.5 ms: 1.22x slower                                                      |
| richards_super             | 29.8 ms                                                     | 36.4 ms: 1.22x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.31 ms: 1.22x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 1.02 ms: 1.26x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 70.9 ms: 1.26x slower                                                      |
| django_template            | 20.3 ms                                                     | 25.7 ms: 1.27x slower                                                      |
| raytrace                   | 153 ms                                                      | 202 ms: 1.32x slower                                                       |
| coverage                   | 45.3 ms                                                     | 66.3 ms: 1.46x slower                                                      |
| mako                       | 6.56 ms                                                     | 9.68 ms: 1.47x slower                                                      |
| k_core                     | 1.70 sec                                                    | 2.68 sec: 1.58x slower                                                     |
| pprint_pformat             | 977 ms                                                      | 1.57 sec: 1.60x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 2.31 sec: 1.69x slower                                                     |
| many_optionals             | 361 us                                                      | 624 us: 1.73x slower                                                       |
| shortest_path              | 355 ms                                                      | 646 ms: 1.82x slower                                                       |
| docutils                   | 1.53 sec                                                    | 2.81 sec: 1.84x slower                                                     |
| bpe_tokeniser              | 2.87 sec                                                    | 5.46 sec: 1.90x slower                                                     |
| connected_components       | 320 ms                                                      | 617 ms: 1.93x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 34.6 ms: 3.19x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (3): pycparser, pylint, deepcopy_reduce
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251004-3.15.0a0-880c952-NOGIL/bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.028x slower

# HPT report

- Reliability score: 99.87% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown