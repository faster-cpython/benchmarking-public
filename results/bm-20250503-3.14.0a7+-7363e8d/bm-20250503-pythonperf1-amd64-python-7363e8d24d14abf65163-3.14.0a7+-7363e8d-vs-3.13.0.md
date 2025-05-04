# Results vs. 3.13.0

- fork: python
- ref: 7363e8d24d14abf65163
- machine: windows-amd64
- commit hash: 7363e8d
- commit date: 2025-05-03
- overall geometric mean: 1.018x faster
- HPT reliability: 97.77%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 223 ms: 1.03x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                                      |
| sphinx         | 617 ms                                                      | 652 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 164 ms: 1.83x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 400 ms: 1.24x faster                                                        |
| async_tree_io              | 513 ms                                                      | 413 ms: 1.24x faster                                                        |
| async_tree_none            | 219 ms                                                      | 182 ms: 1.20x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 172 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 337 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                        |
| async_generators           | 223 ms                                                      | 231 ms: 1.04x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.10x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.20x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.9 ms: 1.16x faster                                                       |
| nbody          | 66.3 ms                                                     | 63.2 ms: 1.05x faster                                                       |
| pidigits       | 146 ms                                                      | 149 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 15.1 ms: 1.58x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.57 ms: 1.08x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 81.4 ms: 1.01x slower                                                       |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.6 us: 1.03x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 90.7 ms: 1.02x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 134 us: 1.03x slower                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 56.3 ms: 1.05x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.2 ms: 1.06x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 40.0 ms: 1.10x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.80 ms: 1.10x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 213 us: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.4 ms: 1.08x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.7 ms: 1.16x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.70 ms: 1.02x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 15.6 ms: 1.02x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 35.0 ms: 1.03x slower                                                       |
| django_template | 20.3 ms                                                     | 24.3 ms: 1.20x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 32.4 ms: 2.32x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 164 ms: 1.83x faster                                                        |
| mdp                        | 1.43 sec                                                    | 791 ms: 1.81x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 15.1 ms: 1.58x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                        |
| deepcopy                   | 223 us                                                      | 177 us: 1.27x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 18.5 us: 1.25x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 400 ms: 1.24x faster                                                        |
| async_tree_io              | 513 ms                                                      | 413 ms: 1.24x faster                                                        |
| async_tree_none            | 219 ms                                                      | 182 ms: 1.20x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 172 ms: 1.16x faster                                                        |
| float                      | 50.8 ms                                                     | 43.9 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 337 ms: 1.13x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 56.3 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.86 us: 1.09x faster                                                       |
| go                         | 84.7 ms                                                     | 77.9 ms: 1.09x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.57 ms: 1.08x faster                                                       |
| json                       | 3.30 ms                                                     | 3.08 ms: 1.07x faster                                                       |
| nbody                      | 66.3 ms                                                     | 63.2 ms: 1.05x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.64 ms: 1.04x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.6 us: 1.03x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 90.7 ms: 1.02x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 75.1 ms: 1.02x faster                                                       |
| pyflate                    | 283 ms                                                      | 280 ms: 1.01x faster                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.4 ms: 1.01x faster                                                       |
| regex_compile              | 80.7 ms                                                     | 81.4 ms: 1.01x slower                                                       |
| fannkuch                   | 252 ms                                                      | 254 ms: 1.01x slower                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                      |
| chaos                      | 37.9 ms                                                     | 38.4 ms: 1.01x slower                                                       |
| pidigits                   | 146 ms                                                      | 149 ms: 1.02x slower                                                        |
| sympy_integrate            | 12.3 ms                                                     | 12.6 ms: 1.02x slower                                                       |
| mako                       | 6.56 ms                                                     | 6.70 ms: 1.02x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.94 sec: 1.02x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 15.6 ms: 1.02x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 496 ms: 1.02x slower                                                        |
| generators                 | 19.0 ms                                                     | 19.5 ms: 1.03x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.00 sec: 1.03x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 56.2 ns: 1.03x slower                                                       |
| sympy_str                  | 167 ms                                                      | 172 ms: 1.03x slower                                                        |
| unpickle_pure_python       | 130 us                                                      | 134 us: 1.03x slower                                                        |
| meteor_contest             | 72.0 ms                                                     | 74.3 ms: 1.03x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 35.0 ms: 1.03x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 88.1 ms: 1.03x slower                                                       |
| 2to3                       | 215 ms                                                      | 223 ms: 1.03x slower                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.27 ms: 1.04x slower                                                       |
| scimark_fft                | 175 ms                                                      | 181 ms: 1.04x slower                                                        |
| async_generators           | 223 ms                                                      | 231 ms: 1.04x slower                                                        |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.04x slower                                                        |
| sympy_expand               | 286 ms                                                      | 297 ms: 1.04x slower                                                        |
| connected_components       | 320 ms                                                      | 334 ms: 1.04x slower                                                        |
| richards_super             | 29.8 ms                                                     | 31.1 ms: 1.05x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 47.8 ms: 1.05x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.03 ms: 1.05x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 56.3 ms: 1.05x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 109 us: 1.05x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 42.3 ms: 1.06x slower                                                       |
| sphinx                     | 617 ms                                                      | 652 ms: 1.06x slower                                                        |
| richards                   | 26.3 ms                                                     | 27.8 ms: 1.06x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.2 ms: 1.06x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.09 ms: 1.06x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 90.1 ms: 1.07x slower                                                       |
| shortest_path              | 355 ms                                                      | 384 ms: 1.08x slower                                                        |
| python_startup             | 24.4 ms                                                     | 26.4 ms: 1.08x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 60.9 ms: 1.08x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                                      |
| comprehensions             | 10.4 us                                                     | 11.4 us: 1.10x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 40.0 ms: 1.10x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 889 us: 1.10x slower                                                        |
| json_dumps                 | 6.19 ms                                                     | 6.80 ms: 1.10x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.10x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.40 us: 1.11x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.87 us: 1.11x slower                                                       |
| coverage                   | 45.3 ms                                                     | 51.6 ms: 1.14x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.16 ms: 1.14x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 213 us: 1.14x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 19.7 ms: 1.16x slower                                                       |
| raytrace                   | 153 ms                                                      | 182 ms: 1.19x slower                                                        |
| django_template            | 20.3 ms                                                     | 24.3 ms: 1.20x slower                                                       |
| many_optionals             | 361 us                                                      | 440 us: 1.22x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 17.0 ms: 1.56x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (7): pylint, sqlite_synth, scimark_lu, scimark_sparse_mat_mult, k_core, html5lib, pycparser
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250503-3.14.0a7+-7363e8d/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.018x faster

# HPT report

- Reliability score: 97.77% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown