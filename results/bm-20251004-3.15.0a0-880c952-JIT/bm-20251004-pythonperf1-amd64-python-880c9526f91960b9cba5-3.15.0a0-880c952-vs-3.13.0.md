# Results vs. 3.13.0

- fork: python
- ref: 880c9526f91960b9cba5
- machine: windows-amd64
- commit hash: 880c952
- commit date: 2025-10-04
- overall geometric mean: 1.088x faster
- HPT reliability: 93.02%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                     |
| html5lib       | 38.2 ms                                                     | 39.0 ms: 1.02x slower                                                      |
| sphinx         | 617 ms                                                      | 637 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 165 ms: 1.81x faster                                                       |
| async_tree_io              | 513 ms                                                      | 379 ms: 1.35x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 378 ms: 1.31x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 203 ms: 1.30x faster                                                       |
| async_tree_none            | 219 ms                                                      | 174 ms: 1.26x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 167 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 337 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 336 ms: 1.13x faster                                                       |
| async_generators           | 223 ms                                                      | 246 ms: 1.10x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.6 ms: 1.17x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 54.9 ms: 1.21x faster                                                      |
| float          | 50.8 ms                                                     | 43.5 ms: 1.17x faster                                                      |
| pidigits       | 146 ms                                                      | 147 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 78.0 ms: 1.04x faster                                                      |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.11 sec: 1.24x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 107 us: 1.22x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 5.47 ms: 1.13x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.1 us: 1.07x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 49.9 ms: 1.07x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 35.6 ms: 1.03x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 90.5 ms: 1.02x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.9 ms: 1.06x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 200 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.7 ms: 1.05x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.43 ms: 1.21x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.6 ms: 1.03x slower                                                      |
| genshi_xml      | 33.9 ms                                                     | 35.2 ms: 1.04x slower                                                      |
| django_template | 20.3 ms                                                     | 24.1 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 514 us: 16.49x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 29.6 ms: 2.55x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 165 ms: 1.81x faster                                                       |
| mdp                        | 1.43 sec                                                    | 811 ms: 1.77x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                      |
| deepcopy_memo              | 23.1 us                                                     | 16.7 us: 1.38x faster                                                      |
| deepcopy                   | 223 us                                                      | 165 us: 1.36x faster                                                       |
| async_tree_io              | 513 ms                                                      | 379 ms: 1.35x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 378 ms: 1.31x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 203 ms: 1.30x faster                                                       |
| scimark_fft                | 175 ms                                                      | 137 ms: 1.27x faster                                                       |
| async_tree_none            | 219 ms                                                      | 174 ms: 1.26x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.11 sec: 1.24x faster                                                     |
| unpickle_pure_python       | 130 us                                                      | 107 us: 1.22x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.43 ms: 1.21x faster                                                      |
| nbody                      | 66.3 ms                                                     | 54.9 ms: 1.21x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.04 ms: 1.20x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 167 ms: 1.20x faster                                                       |
| fannkuch                   | 252 ms                                                      | 213 ms: 1.18x faster                                                       |
| pprint_safe_repr           | 485 ms                                                      | 412 ms: 1.18x faster                                                       |
| float                      | 50.8 ms                                                     | 43.5 ms: 1.17x faster                                                      |
| pprint_pformat             | 977 ms                                                      | 839 ms: 1.16x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.24 ms: 1.16x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.76 us: 1.15x faster                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.53 sec: 1.14x faster                                                     |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 337 ms: 1.13x faster                                                       |
| pyflate                    | 283 ms                                                      | 250 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 336 ms: 1.13x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.47 ms: 1.13x faster                                                      |
| json                       | 3.30 ms                                                     | 2.93 ms: 1.12x faster                                                      |
| go                         | 84.7 ms                                                     | 75.8 ms: 1.12x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.1 us: 1.07x faster                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 49.9 ms: 1.07x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.62 sec: 1.05x faster                                                     |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.4 ms: 1.04x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 78.0 ms: 1.04x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.54 us: 1.03x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 35.6 ms: 1.03x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 90.5 ms: 1.02x faster                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 45.0 ms: 1.01x faster                                                      |
| pidigits                   | 146 ms                                                      | 147 ms: 1.01x slower                                                       |
| connected_components       | 320 ms                                                      | 323 ms: 1.01x slower                                                       |
| spectral_norm              | 63.4 ms                                                     | 64.0 ms: 1.01x slower                                                      |
| logging_simple             | 5.77 us                                                     | 5.85 us: 1.01x slower                                                      |
| sympy_str                  | 167 ms                                                      | 169 ms: 1.01x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 55.5 ns: 1.02x slower                                                      |
| sympy_expand               | 286 ms                                                      | 291 ms: 1.02x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.0 ms: 1.02x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 87.0 ms: 1.02x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.6 ms: 1.02x slower                                                      |
| richards_super             | 29.8 ms                                                     | 30.5 ms: 1.02x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 15.6 ms: 1.03x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 58.3 ms: 1.03x slower                                                      |
| richards                   | 26.3 ms                                                     | 27.1 ms: 1.03x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.37 us: 1.03x slower                                                      |
| sphinx                     | 617 ms                                                      | 637 ms: 1.03x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 35.2 ms: 1.04x slower                                                      |
| comprehensions             | 10.4 us                                                     | 10.8 us: 1.04x slower                                                      |
| chaos                      | 37.9 ms                                                     | 39.7 ms: 1.05x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 850 us: 1.05x slower                                                       |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.7 ms: 1.05x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.29 ms: 1.05x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.9 ms: 1.06x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 60.0 ms: 1.07x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 90.1 ms: 1.07x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 200 us: 1.07x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                     |
| hexiom                     | 3.84 ms                                                     | 4.14 ms: 1.08x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.12 ms: 1.08x slower                                                      |
| async_generators           | 223 ms                                                      | 246 ms: 1.10x slower                                                       |
| coverage                   | 45.3 ms                                                     | 51.2 ms: 1.13x slower                                                      |
| raytrace                   | 153 ms                                                      | 176 ms: 1.15x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.6 ms: 1.17x slower                                                      |
| django_template            | 20.3 ms                                                     | 24.1 ms: 1.19x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.26 ms: 1.20x slower                                                      |
| many_optionals             | 361 us                                                      | 570 us: 1.58x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 31.0 ms: 2.86x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (8): pylint, 2to3, scimark_sor, meteor_contest, typing_runtime_protocols, dulwich_log, shortest_path, pycparser
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251004-3.15.0a0-880c952-JIT/bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.088x faster

# HPT report

- Reliability score: 93.02% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown