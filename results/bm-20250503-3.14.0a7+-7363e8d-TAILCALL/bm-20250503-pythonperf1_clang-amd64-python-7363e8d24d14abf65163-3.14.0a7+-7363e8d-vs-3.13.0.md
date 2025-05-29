# Results vs. 3.13.0

- fork: python
- ref: 7363e8d24d14abf65163
- machine: windows-amd64
- commit hash: 7363e8d
- commit date: 2025-05-03
- overall geometric mean: 1.171x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 205 ms: 1.05x faster                                                        |
| docutils       | 1.53 sec                                                    | 1.59 sec: 1.04x slower                                                      |
| html5lib       | 38.2 ms                                                     | 34.4 ms: 1.11x faster                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.87x faster                                                        |
| async_tree_io              | 513 ms                                                      | 347 ms: 1.48x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 184 ms: 1.44x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 196 ms: 1.43x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 355 ms: 1.40x faster                                                        |
| async_tree_none            | 219 ms                                                      | 157 ms: 1.40x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 149 ms: 1.34x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 317 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 322 ms: 1.19x faster                                                        |
| async_generators           | 223 ms                                                      | 195 ms: 1.14x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 11.1 ms: 1.13x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.35x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 37.9 ms: 1.34x faster                                                       |
| nbody          | 66.3 ms                                                     | 52.2 ms: 1.27x faster                                                       |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.8 ms: 1.73x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 68.6 ms: 1.18x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.76 ms: 1.04x slower                                                       |
| regex_dna      | 115 ms                                                      | 127 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.06 sec: 1.30x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 104 us: 1.25x faster                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 48.3 ms: 1.11x faster                                                       |
| pickle_pure_python   | 186 us                                                      | 169 us: 1.10x faster                                                        |
| xml_etree_process    | 36.5 ms                                                     | 33.5 ms: 1.09x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 5.79 ms: 1.07x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 93.8 ms: 1.02x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.2 ms: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 27.0 ms: 1.11x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 20.2 ms: 1.19x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 11.3 ms: 1.35x faster                                                       |
| genshi_xml      | 33.9 ms                                                     | 28.0 ms: 1.21x faster                                                       |
| mako            | 6.56 ms                                                     | 5.93 ms: 1.11x faster                                                       |
| django_template | 20.3 ms                                                     | 20.0 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 30.7 ms: 2.45x faster                                                       |
| mdp                        | 1.43 sec                                                    | 682 ms: 2.10x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.87x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 13.8 ms: 1.73x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 13.4 us: 1.73x faster                                                       |
| deepcopy                   | 223 us                                                      | 141 us: 1.59x faster                                                        |
| scimark_sor                | 76.2 ms                                                     | 49.0 ms: 1.55x faster                                                       |
| async_tree_io              | 513 ms                                                      | 347 ms: 1.48x faster                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 28.0 ms: 1.45x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 184 ms: 1.44x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 196 ms: 1.43x faster                                                        |
| go                         | 84.7 ms                                                     | 59.7 ms: 1.42x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 355 ms: 1.40x faster                                                        |
| async_tree_none            | 219 ms                                                      | 157 ms: 1.40x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.49 us: 1.36x faster                                                       |
| genshi_text                | 15.2 ms                                                     | 11.3 ms: 1.35x faster                                                       |
| float                      | 50.8 ms                                                     | 37.9 ms: 1.34x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 149 ms: 1.34x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 48.1 ms: 1.32x faster                                                       |
| hexiom                     | 3.84 ms                                                     | 2.94 ms: 1.31x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.06 sec: 1.30x faster                                                      |
| generators                 | 19.0 ms                                                     | 14.8 ms: 1.28x faster                                                       |
| fannkuch                   | 252 ms                                                      | 197 ms: 1.28x faster                                                        |
| nbody                      | 66.3 ms                                                     | 52.2 ms: 1.27x faster                                                       |
| pprint_safe_repr           | 485 ms                                                      | 383 ms: 1.27x faster                                                        |
| logging_silent             | 54.6 ns                                                     | 43.1 ns: 1.26x faster                                                       |
| unpickle_pure_python       | 130 us                                                      | 104 us: 1.25x faster                                                        |
| pprint_pformat             | 977 ms                                                      | 786 ms: 1.24x faster                                                        |
| scimark_lu                 | 56.7 ms                                                     | 46.0 ms: 1.23x faster                                                       |
| richards                   | 26.3 ms                                                     | 21.4 ms: 1.23x faster                                                       |
| pyflate                    | 283 ms                                                      | 232 ms: 1.22x faster                                                        |
| deltablue                  | 1.89 ms                                                     | 1.55 ms: 1.22x faster                                                       |
| genshi_xml                 | 33.9 ms                                                     | 28.0 ms: 1.21x faster                                                       |
| chaos                      | 37.9 ms                                                     | 31.4 ms: 1.21x faster                                                       |
| comprehensions             | 10.4 us                                                     | 8.59 us: 1.21x faster                                                       |
| richards_super             | 29.8 ms                                                     | 24.8 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 317 ms: 1.20x faster                                                        |
| scimark_fft                | 175 ms                                                      | 146 ms: 1.19x faster                                                        |
| telco                      | 4.85 ms                                                     | 4.08 ms: 1.19x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 322 ms: 1.19x faster                                                        |
| nqueens                    | 56.1 ms                                                     | 47.5 ms: 1.18x faster                                                       |
| regex_compile              | 80.7 ms                                                     | 68.6 ms: 1.18x faster                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 39.1 ms: 1.17x faster                                                       |
| async_generators           | 223 ms                                                      | 195 ms: 1.14x faster                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 2.52 sec: 1.14x faster                                                      |
| typing_runtime_protocols   | 103 us                                                      | 90.7 us: 1.14x faster                                                       |
| json                       | 3.30 ms                                                     | 2.92 ms: 1.13x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.30 ms: 1.13x faster                                                       |
| coroutines                 | 12.5 ms                                                     | 11.1 ms: 1.13x faster                                                       |
| sympy_expand               | 286 ms                                                      | 256 ms: 1.12x faster                                                        |
| sympy_str                  | 167 ms                                                      | 150 ms: 1.11x faster                                                        |
| html5lib                   | 38.2 ms                                                     | 34.4 ms: 1.11x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 48.3 ms: 1.11x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.93 ms: 1.11x faster                                                       |
| pickle_pure_python         | 186 us                                                      | 169 us: 1.10x faster                                                        |
| coverage                   | 45.3 ms                                                     | 41.1 ms: 1.10x faster                                                       |
| sympy_integrate            | 12.3 ms                                                     | 11.2 ms: 1.10x faster                                                       |
| xml_etree_process          | 36.5 ms                                                     | 33.5 ms: 1.09x faster                                                       |
| sympy_sum                  | 85.2 ms                                                     | 78.2 ms: 1.09x faster                                                       |
| pylint                     | 205 ms                                                      | 190 ms: 1.08x faster                                                        |
| pycparser                  | 695 ms                                                      | 649 ms: 1.07x faster                                                        |
| meteor_contest             | 72.0 ms                                                     | 67.2 ms: 1.07x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.79 ms: 1.07x faster                                                       |
| raytrace                   | 153 ms                                                      | 144 ms: 1.06x faster                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.51 us: 1.05x faster                                                       |
| 2to3                       | 215 ms                                                      | 205 ms: 1.05x faster                                                        |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                       |
| dulwich_log                | 40.1 ms                                                     | 38.9 ms: 1.03x faster                                                       |
| logging_simple             | 5.77 us                                                     | 5.60 us: 1.03x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.65 sec: 1.03x faster                                                      |
| logging_format             | 6.18 us                                                     | 6.00 us: 1.03x faster                                                       |
| django_template            | 20.3 ms                                                     | 20.0 ms: 1.01x faster                                                       |
| shortest_path              | 355 ms                                                      | 352 ms: 1.01x faster                                                        |
| xml_etree_parse            | 92.2 ms                                                     | 93.8 ms: 1.02x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.59 sec: 1.04x slower                                                      |
| connected_components       | 320 ms                                                      | 332 ms: 1.04x slower                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.76 ms: 1.04x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 845 us: 1.04x slower                                                        |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.2 ms: 1.04x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 90.3 ms: 1.07x slower                                                       |
| regex_dna                  | 115 ms                                                      | 127 ms: 1.10x slower                                                        |
| python_startup             | 24.4 ms                                                     | 27.0 ms: 1.11x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.38 ms: 1.13x slower                                                       |
| many_optionals             | 361 us                                                      | 413 us: 1.14x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 20.2 ms: 1.19x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 15.7 ms: 1.45x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.87 ms: 1.46x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.17x faster                                                                |

Benchmark hidden because not significant (2): sphinx, pidigits
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250503-3.14.0a7+-7363e8d-CLANG/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.171x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown