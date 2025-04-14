# Results vs. 3.13.0

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: windows-amd64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.015x faster
- HPT reliability: 97.16%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 228 ms: 1.06x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.75 sec: 1.14x slower                                                      |
| html5lib       | 38.2 ms                                                     | 40.4 ms: 1.06x slower                                                       |
| sphinx         | 617 ms                                                      | 673 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                       | 1.09x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 219 ms: 1.28x faster                                                        |
| async_tree_io              | 513 ms                                                      | 425 ms: 1.21x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 421 ms: 1.18x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 227 ms: 1.17x faster                                                        |
| async_tree_none            | 219 ms                                                      | 189 ms: 1.16x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 179 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 348 ms: 1.09x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 304 ms: 1.01x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                       |
| async_generators           | 223 ms                                                      | 250 ms: 1.12x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 46.9 ms: 1.08x faster                                                       |
| nbody          | 66.3 ms                                                     | 63.4 ms: 1.04x faster                                                       |
| pidigits       | 146 ms                                                      | 149 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.5 ms: 1.77x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.41 ms: 1.20x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 86.2 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.24 sec: 1.11x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 88.6 ms: 1.04x faster                                                       |
| unpickle_pure_python | 130 us                                                      | 125 us: 1.04x faster                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 52.6 ms: 1.02x faster                                                       |
| json_loads           | 15.1 us                                                     | 15.3 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.0 ms: 1.04x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 38.3 ms: 1.05x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 7.13 ms: 1.15x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 217 us: 1.17x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.7 ms: 1.06x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 20.6 ms: 1.22x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.76 ms: 1.14x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 17.3 ms: 1.14x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 40.1 ms: 1.18x slower                                                       |
| django_template | 20.3 ms                                                     | 26.7 ms: 1.32x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.12x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 541 us: 15.64x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 32.7 ms: 2.30x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.5 ms: 1.77x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 219 ms: 1.28x faster                                                        |
| async_tree_io              | 513 ms                                                      | 425 ms: 1.21x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.41 ms: 1.20x faster                                                       |
| deepcopy                   | 223 us                                                      | 188 us: 1.19x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 421 ms: 1.18x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 227 ms: 1.17x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 19.8 us: 1.17x faster                                                       |
| async_tree_none            | 219 ms                                                      | 189 ms: 1.16x faster                                                        |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.28 ms: 1.14x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.76 ms: 1.14x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 179 ms: 1.12x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.24 sec: 1.11x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                                        |
| scimark_fft                | 175 ms                                                      | 159 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 348 ms: 1.09x faster                                                        |
| telco                      | 4.85 ms                                                     | 4.45 ms: 1.09x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 58.3 ms: 1.09x faster                                                       |
| float                      | 50.8 ms                                                     | 46.9 ms: 1.08x faster                                                       |
| json                       | 3.30 ms                                                     | 3.10 ms: 1.06x faster                                                       |
| nbody                      | 66.3 ms                                                     | 63.4 ms: 1.04x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.76 sec: 1.04x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 88.6 ms: 1.04x faster                                                       |
| unpickle_pure_python       | 130 us                                                      | 125 us: 1.04x faster                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.53 us: 1.04x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 52.6 ms: 1.02x faster                                                       |
| shortest_path              | 355 ms                                                      | 358 ms: 1.01x slower                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.24 ms: 1.01x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 304 ms: 1.01x slower                                                        |
| json_loads                 | 15.1 us                                                     | 15.3 us: 1.01x slower                                                       |
| connected_components       | 320 ms                                                      | 325 ms: 1.02x slower                                                        |
| pidigits                   | 146 ms                                                      | 149 ms: 1.02x slower                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 2.07 us: 1.02x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.0 ms: 1.04x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 75.1 ms: 1.04x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.05 ms: 1.04x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 38.3 ms: 1.05x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 88.7 ms: 1.05x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.7 ms: 1.06x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 59.9 ms: 1.06x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 80.6 ms: 1.06x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 40.4 ms: 1.06x slower                                                       |
| 2to3                       | 215 ms                                                      | 228 ms: 1.06x slower                                                        |
| bench_thread_pool          | 810 us                                                      | 862 us: 1.06x slower                                                        |
| regex_compile              | 80.7 ms                                                     | 86.2 ms: 1.07x slower                                                       |
| go                         | 84.7 ms                                                     | 90.6 ms: 1.07x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 43.0 ms: 1.07x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.05 sec: 1.07x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 91.5 ms: 1.07x slower                                                       |
| generators                 | 19.0 ms                                                     | 20.5 ms: 1.08x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 523 ms: 1.08x slower                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 49.4 ms: 1.08x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.09x slower                                                       |
| sphinx                     | 617 ms                                                      | 673 ms: 1.09x slower                                                        |
| sympy_str                  | 167 ms                                                      | 182 ms: 1.09x slower                                                        |
| pycparser                  | 695 ms                                                      | 759 ms: 1.09x slower                                                        |
| coverage                   | 45.3 ms                                                     | 49.4 ms: 1.09x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 59.6 ns: 1.09x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 44.6 ms: 1.10x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.6 ms: 1.10x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 115 us: 1.11x slower                                                        |
| richards_super             | 29.8 ms                                                     | 33.2 ms: 1.11x slower                                                       |
| sympy_expand               | 286 ms                                                      | 319 ms: 1.12x slower                                                        |
| richards                   | 26.3 ms                                                     | 29.4 ms: 1.12x slower                                                       |
| async_generators           | 223 ms                                                      | 250 ms: 1.12x slower                                                        |
| logging_simple             | 5.77 us                                                     | 6.55 us: 1.13x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 64.0 ms: 1.14x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 17.3 ms: 1.14x slower                                                       |
| chaos                      | 37.9 ms                                                     | 43.2 ms: 1.14x slower                                                       |
| logging_format             | 6.18 us                                                     | 7.06 us: 1.14x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.75 sec: 1.14x slower                                                      |
| comprehensions             | 10.4 us                                                     | 11.9 us: 1.15x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.64 sec: 1.15x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.42 ms: 1.15x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 7.13 ms: 1.15x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 217 us: 1.17x slower                                                        |
| genshi_xml                 | 33.9 ms                                                     | 40.1 ms: 1.18x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 20.6 ms: 1.22x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.38 ms: 1.26x slower                                                       |
| many_optionals             | 361 us                                                      | 455 us: 1.26x slower                                                        |
| raytrace                   | 153 ms                                                      | 194 ms: 1.27x slower                                                        |
| django_template            | 20.3 ms                                                     | 26.7 ms: 1.32x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.6 ms: 1.53x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (5): k_core, pyflate, fannkuch, regex_dna, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250315-3.14.0a6+-e82c2ca-JIT/bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.015x faster

# HPT report

- Reliability score: 97.16% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown