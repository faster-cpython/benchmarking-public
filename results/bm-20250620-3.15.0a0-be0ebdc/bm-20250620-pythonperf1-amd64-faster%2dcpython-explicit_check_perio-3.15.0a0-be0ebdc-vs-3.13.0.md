# Results vs. 3.13.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: windows-amd64
- commit hash: be0ebdc
- commit date: 2025-06-20
- overall geometric mean: 1.057x faster
- HPT reliability: 95.28%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 222 ms: 1.03x slower                                                                 |
| docutils       | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                               |
| html5lib       | 38.2 ms                                                     | 38.9 ms: 1.02x slower                                                                |
| sphinx         | 617 ms                                                      | 648 ms: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                                 |
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.32x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 400 ms: 1.28x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 389 ms: 1.28x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.27x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 208 ms: 1.27x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                                 |
| async_generators           | 223 ms                                                      | 233 ms: 1.05x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.14x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.7 ms: 1.14x faster                                                                |
| nbody          | 66.3 ms                                                     | 62.5 ms: 1.06x faster                                                                |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.7 ms: 1.74x faster                                                                |
| regex_effbot   | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                                |
| regex_compile  | 80.7 ms                                                     | 81.1 ms: 1.00x slower                                                                |
| regex_dna      | 115 ms                                                      | 122 ms: 1.06x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.0 us: 1.08x faster                                                                |
| xml_etree_parse      | 92.2 ms                                                     | 87.5 ms: 1.05x faster                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                               |
| json_dumps           | 6.19 ms                                                     | 6.39 ms: 1.03x slower                                                                |
| unpickle_pure_python | 130 us                                                      | 135 us: 1.04x slower                                                                 |
| xml_etree_generate   | 53.5 ms                                                     | 55.4 ms: 1.04x slower                                                                |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.9 ms: 1.04x slower                                                                |
| xml_etree_process    | 36.5 ms                                                     | 39.1 ms: 1.07x slower                                                                |
| pickle_pure_python   | 186 us                                                      | 216 us: 1.16x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.7 ms: 1.05x slower                                                                |
| python_startup_no_site | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                                |
| genshi_xml      | 33.9 ms                                                     | 35.1 ms: 1.04x slower                                                                |
| mako            | 6.56 ms                                                     | 6.88 ms: 1.05x slower                                                                |
| django_template | 20.3 ms                                                     | 24.0 ms: 1.18x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 507 us: 16.70x faster                                                                |
| pathlib                    | 75.3 ms                                                     | 31.9 ms: 2.36x faster                                                                |
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                                 |
| mdp                        | 1.43 sec                                                    | 811 ms: 1.76x faster                                                                 |
| regex_v8                   | 23.8 ms                                                     | 13.7 ms: 1.74x faster                                                                |
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.32x faster                                                                 |
| deepcopy                   | 223 us                                                      | 173 us: 1.30x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 400 ms: 1.28x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 389 ms: 1.28x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.27x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 208 ms: 1.27x faster                                                                 |
| deepcopy_memo              | 23.1 us                                                     | 18.4 us: 1.25x faster                                                                |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                                 |
| float                      | 50.8 ms                                                     | 44.7 ms: 1.14x faster                                                                |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                                 |
| go                         | 84.7 ms                                                     | 76.2 ms: 1.11x faster                                                                |
| deepcopy_reduce            | 2.02 us                                                     | 1.83 us: 1.11x faster                                                                |
| regex_effbot               | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                                |
| json                       | 3.30 ms                                                     | 3.02 ms: 1.09x faster                                                                |
| json_loads                 | 15.1 us                                                     | 14.0 us: 1.08x faster                                                                |
| telco                      | 4.85 ms                                                     | 4.52 ms: 1.07x faster                                                                |
| nbody                      | 66.3 ms                                                     | 62.5 ms: 1.06x faster                                                                |
| xml_etree_parse            | 92.2 ms                                                     | 87.5 ms: 1.05x faster                                                                |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.51 ms: 1.04x faster                                                                |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.3 ms: 1.04x faster                                                                |
| scimark_sor                | 76.2 ms                                                     | 73.9 ms: 1.03x faster                                                                |
| spectral_norm              | 63.4 ms                                                     | 62.6 ms: 1.01x faster                                                                |
| regex_compile              | 80.7 ms                                                     | 81.1 ms: 1.00x slower                                                                |
| genshi_text                | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                                |
| k_core                     | 1.70 sec                                                    | 1.72 sec: 1.01x slower                                                               |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.02x slower                                                                |
| generators                 | 19.0 ms                                                     | 19.3 ms: 1.02x slower                                                                |
| html5lib                   | 38.2 ms                                                     | 38.9 ms: 1.02x slower                                                                |
| sympy_str                  | 167 ms                                                      | 170 ms: 1.02x slower                                                                 |
| tomli_loads                | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                               |
| shortest_path              | 355 ms                                                      | 364 ms: 1.02x slower                                                                 |
| sympy_expand               | 286 ms                                                      | 293 ms: 1.03x slower                                                                 |
| meteor_contest             | 72.0 ms                                                     | 73.9 ms: 1.03x slower                                                                |
| bpe_tokeniser              | 2.87 sec                                                    | 2.96 sec: 1.03x slower                                                               |
| comprehensions             | 10.4 us                                                     | 10.7 us: 1.03x slower                                                                |
| 2to3                       | 215 ms                                                      | 222 ms: 1.03x slower                                                                 |
| fannkuch                   | 252 ms                                                      | 260 ms: 1.03x slower                                                                 |
| json_dumps                 | 6.19 ms                                                     | 6.39 ms: 1.03x slower                                                                |
| dulwich_log                | 40.1 ms                                                     | 41.4 ms: 1.03x slower                                                                |
| scimark_lu                 | 56.7 ms                                                     | 58.6 ms: 1.03x slower                                                                |
| unpickle_pure_python       | 130 us                                                      | 135 us: 1.04x slower                                                                 |
| xml_etree_generate         | 53.5 ms                                                     | 55.4 ms: 1.04x slower                                                                |
| genshi_xml                 | 33.9 ms                                                     | 35.1 ms: 1.04x slower                                                                |
| sympy_sum                  | 85.2 ms                                                     | 88.3 ms: 1.04x slower                                                                |
| richards                   | 26.3 ms                                                     | 27.3 ms: 1.04x slower                                                                |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.9 ms: 1.04x slower                                                                |
| richards_super             | 29.8 ms                                                     | 31.0 ms: 1.04x slower                                                                |
| crypto_pyaes               | 45.6 ms                                                     | 47.5 ms: 1.04x slower                                                                |
| connected_components       | 320 ms                                                      | 335 ms: 1.05x slower                                                                 |
| async_generators           | 223 ms                                                      | 233 ms: 1.05x slower                                                                 |
| mako                       | 6.56 ms                                                     | 6.88 ms: 1.05x slower                                                                |
| sphinx                     | 617 ms                                                      | 648 ms: 1.05x slower                                                                 |
| hexiom                     | 3.84 ms                                                     | 4.04 ms: 1.05x slower                                                                |
| python_startup             | 24.4 ms                                                     | 25.7 ms: 1.05x slower                                                                |
| regex_dna                  | 115 ms                                                      | 122 ms: 1.06x slower                                                                 |
| docutils                   | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                               |
| coverage                   | 45.3 ms                                                     | 48.2 ms: 1.06x slower                                                                |
| xml_etree_process          | 36.5 ms                                                     | 39.1 ms: 1.07x slower                                                                |
| chaos                      | 37.9 ms                                                     | 40.6 ms: 1.07x slower                                                                |
| nqueens                    | 56.1 ms                                                     | 60.3 ms: 1.07x slower                                                                |
| create_gc_cycles           | 1.22 ms                                                     | 1.32 ms: 1.08x slower                                                                |
| logging_format             | 6.18 us                                                     | 6.73 us: 1.09x slower                                                                |
| gc_traversal               | 1.96 ms                                                     | 2.15 ms: 1.09x slower                                                                |
| logging_simple             | 5.77 us                                                     | 6.36 us: 1.10x slower                                                                |
| pprint_safe_repr           | 485 ms                                                      | 552 ms: 1.14x slower                                                                 |
| python_startup_no_site     | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                                |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.14x slower                                                                |
| pprint_pformat             | 977 ms                                                      | 1.12 sec: 1.15x slower                                                               |
| deltablue                  | 1.89 ms                                                     | 2.18 ms: 1.15x slower                                                                |
| pickle_pure_python         | 186 us                                                      | 216 us: 1.16x slower                                                                 |
| raytrace                   | 153 ms                                                      | 180 ms: 1.18x slower                                                                 |
| django_template            | 20.3 ms                                                     | 24.0 ms: 1.18x slower                                                                |
| many_optionals             | 361 us                                                      | 444 us: 1.23x slower                                                                 |
| subparsers                 | 10.9 ms                                                     | 17.4 ms: 1.60x slower                                                                |
| logging_silent             | 54.6 ns                                                     | 323 ns: 5.92x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                         |

Benchmark hidden because not significant (7): pylint, pidigits, scimark_fft, typing_runtime_protocols, pyflate, sqlite_synth, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250620-3.15.0a0-be0ebdc/bm-20250620-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.057x faster

# HPT report

- Reliability score: 95.28% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown