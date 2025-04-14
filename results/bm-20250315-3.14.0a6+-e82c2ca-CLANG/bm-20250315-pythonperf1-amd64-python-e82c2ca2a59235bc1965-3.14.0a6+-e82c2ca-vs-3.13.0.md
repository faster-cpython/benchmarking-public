# Results vs. 3.13.0

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: windows-amd64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.145x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 206 ms: 1.04x faster                                                        |
| docutils       | 1.53 sec                                                    | 1.56 sec: 1.02x slower                                                      |
| html5lib       | 38.2 ms                                                     | 36.5 ms: 1.05x faster                                                       |
| sphinx         | 617 ms                                                      | 609 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 513 ms                                                      | 357 ms: 1.43x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 200 ms: 1.40x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 355 ms: 1.40x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 192 ms: 1.38x faster                                                        |
| async_tree_none            | 219 ms                                                      | 161 ms: 1.36x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 154 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 314 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 315 ms: 1.21x faster                                                        |
| async_generators           | 223 ms                                                      | 189 ms: 1.18x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 11.4 ms: 1.09x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 408 ms: 1.36x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.23x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 42.4 ms: 1.20x faster                                                       |
| nbody          | 66.3 ms                                                     | 57.7 ms: 1.15x faster                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.4 ms: 1.78x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.55 ms: 1.09x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 74.6 ms: 1.08x faster                                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.22 sec: 1.12x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 116 us: 1.12x faster                                                        |
| json_loads           | 15.1 us                                                     | 13.8 us: 1.09x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 5.78 ms: 1.07x faster                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 50.1 ms: 1.07x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 35.2 ms: 1.04x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 89.6 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 61.9 ms: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.5 ms: 1.09x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 20.9 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 12.9 ms: 1.18x faster                                                       |
| genshi_xml      | 33.9 ms                                                     | 29.5 ms: 1.15x faster                                                       |
| mako            | 6.56 ms                                                     | 6.14 ms: 1.07x faster                                                       |
| django_template | 20.3 ms                                                     | 21.3 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 447 us: 18.96x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 31.4 ms: 2.40x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.4 ms: 1.78x faster                                                       |
| deepcopy                   | 223 us                                                      | 149 us: 1.50x faster                                                        |
| async_tree_io              | 513 ms                                                      | 357 ms: 1.43x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 45.2 ms: 1.40x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 200 ms: 1.40x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 355 ms: 1.40x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 192 ms: 1.38x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 16.7 us: 1.38x faster                                                       |
| async_tree_none            | 219 ms                                                      | 161 ms: 1.36x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 154 ms: 1.30x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.55 us: 1.30x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.04 ms: 1.28x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 61.0 ms: 1.25x faster                                                       |
| go                         | 84.7 ms                                                     | 68.7 ms: 1.23x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 33.1 ms: 1.23x faster                                                       |
| scimark_lu                 | 56.7 ms                                                     | 46.0 ms: 1.23x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 314 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 315 ms: 1.21x faster                                                        |
| json                       | 3.30 ms                                                     | 2.75 ms: 1.20x faster                                                       |
| float                      | 50.8 ms                                                     | 42.4 ms: 1.20x faster                                                       |
| logging_silent             | 54.6 ns                                                     | 45.7 ns: 1.19x faster                                                       |
| async_generators           | 223 ms                                                      | 189 ms: 1.18x faster                                                        |
| hexiom                     | 3.84 ms                                                     | 3.26 ms: 1.18x faster                                                       |
| genshi_text                | 15.2 ms                                                     | 12.9 ms: 1.18x faster                                                       |
| scimark_fft                | 175 ms                                                      | 152 ms: 1.15x faster                                                        |
| typing_runtime_protocols   | 103 us                                                      | 89.7 us: 1.15x faster                                                       |
| nbody                      | 66.3 ms                                                     | 57.7 ms: 1.15x faster                                                       |
| genshi_xml                 | 33.9 ms                                                     | 29.5 ms: 1.15x faster                                                       |
| richards_super             | 29.8 ms                                                     | 26.0 ms: 1.14x faster                                                       |
| richards                   | 26.3 ms                                                     | 23.1 ms: 1.14x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.22 sec: 1.12x faster                                                      |
| unpickle_pure_python       | 130 us                                                      | 116 us: 1.12x faster                                                        |
| chaos                      | 37.9 ms                                                     | 34.0 ms: 1.12x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.35 ms: 1.11x faster                                                       |
| deltablue                  | 1.89 ms                                                     | 1.71 ms: 1.11x faster                                                       |
| pyflate                    | 283 ms                                                      | 255 ms: 1.11x faster                                                        |
| generators                 | 19.0 ms                                                     | 17.3 ms: 1.10x faster                                                       |
| nqueens                    | 56.1 ms                                                     | 51.2 ms: 1.10x faster                                                       |
| pprint_safe_repr           | 485 ms                                                      | 442 ms: 1.10x faster                                                        |
| json_loads                 | 15.1 us                                                     | 13.8 us: 1.09x faster                                                       |
| coroutines                 | 12.5 ms                                                     | 11.4 ms: 1.09x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.55 ms: 1.09x faster                                                       |
| fannkuch                   | 252 ms                                                      | 230 ms: 1.09x faster                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 2.63 sec: 1.09x faster                                                      |
| pprint_pformat             | 977 ms                                                      | 898 ms: 1.09x faster                                                        |
| coverage                   | 45.3 ms                                                     | 41.7 ms: 1.09x faster                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 42.0 ms: 1.08x faster                                                       |
| pylint                     | 205 ms                                                      | 189 ms: 1.08x faster                                                        |
| regex_compile              | 80.7 ms                                                     | 74.6 ms: 1.08x faster                                                       |
| sympy_expand               | 286 ms                                                      | 264 ms: 1.08x faster                                                        |
| comprehensions             | 10.4 us                                                     | 9.62 us: 1.08x faster                                                       |
| mdp                        | 1.43 sec                                                    | 1.33 sec: 1.07x faster                                                      |
| json_dumps                 | 6.19 ms                                                     | 5.78 ms: 1.07x faster                                                       |
| mako                       | 6.56 ms                                                     | 6.14 ms: 1.07x faster                                                       |
| sympy_str                  | 167 ms                                                      | 156 ms: 1.07x faster                                                        |
| xml_etree_generate         | 53.5 ms                                                     | 50.1 ms: 1.07x faster                                                       |
| pycparser                  | 695 ms                                                      | 663 ms: 1.05x faster                                                        |
| raytrace                   | 153 ms                                                      | 146 ms: 1.05x faster                                                        |
| html5lib                   | 38.2 ms                                                     | 36.5 ms: 1.05x faster                                                       |
| logging_simple             | 5.77 us                                                     | 5.53 us: 1.04x faster                                                       |
| 2to3                       | 215 ms                                                      | 206 ms: 1.04x faster                                                        |
| logging_format             | 6.18 us                                                     | 5.95 us: 1.04x faster                                                       |
| xml_etree_process          | 36.5 ms                                                     | 35.2 ms: 1.04x faster                                                       |
| sympy_sum                  | 85.2 ms                                                     | 82.4 ms: 1.03x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.54 us: 1.03x faster                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.0 ms: 1.03x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 89.6 ms: 1.03x faster                                                       |
| meteor_contest             | 72.0 ms                                                     | 70.4 ms: 1.02x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.66 sec: 1.02x faster                                                      |
| dulwich_log                | 40.1 ms                                                     | 39.5 ms: 1.02x faster                                                       |
| sphinx                     | 617 ms                                                      | 609 ms: 1.01x faster                                                        |
| shortest_path              | 355 ms                                                      | 353 ms: 1.01x faster                                                        |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| docutils                   | 1.53 sec                                                    | 1.56 sec: 1.02x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 61.9 ms: 1.02x slower                                                       |
| connected_components       | 320 ms                                                      | 329 ms: 1.03x slower                                                        |
| bench_thread_pool          | 810 us                                                      | 845 us: 1.04x slower                                                        |
| django_template            | 20.3 ms                                                     | 21.3 ms: 1.05x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 88.8 ms: 1.05x slower                                                       |
| python_startup             | 24.4 ms                                                     | 26.5 ms: 1.09x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.34 ms: 1.10x slower                                                       |
| many_optionals             | 361 us                                                      | 414 us: 1.14x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 20.9 ms: 1.23x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 408 ms: 1.36x slower                                                        |
| gc_traversal               | 1.96 ms                                                     | 2.68 ms: 1.36x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 15.0 ms: 1.38x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.14x faster                                                                |

Benchmark hidden because not significant (2): pidigits, pickle_pure_python
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250315-3.14.0a6+-e82c2ca-CLANG/bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.145x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown