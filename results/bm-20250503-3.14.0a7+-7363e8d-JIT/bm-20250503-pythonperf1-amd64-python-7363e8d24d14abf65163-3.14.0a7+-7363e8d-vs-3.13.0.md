# Results vs. 3.13.0

- fork: python
- ref: 7363e8d24d14abf65163
- machine: windows-amd64
- commit hash: 7363e8d
- commit date: 2025-05-03
- overall geometric mean: 1.020x faster
- HPT reliability: 62.96%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 223 ms: 1.04x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.72 sec: 1.12x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.4 ms: 1.03x slower                                                       |
| sphinx         | 617 ms                                                      | 662 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 162 ms: 1.85x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 400 ms: 1.24x faster                                                        |
| async_tree_io              | 513 ms                                                      | 415 ms: 1.24x faster                                                        |
| async_tree_none            | 219 ms                                                      | 181 ms: 1.21x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 172 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 335 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 341 ms: 1.12x faster                                                        |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.15x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 56.9 ms: 1.16x faster                                                       |
| float          | 50.8 ms                                                     | 45.3 ms: 1.12x faster                                                       |
| pidigits       | 146 ms                                                      | 149 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.4 ms: 1.66x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.58 ms: 1.08x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 81.5 ms: 1.01x slower                                                       |
| regex_dna      | 115 ms                                                      | 123 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.22 sec: 1.13x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 119 us: 1.09x faster                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 51.7 ms: 1.03x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 90.0 ms: 1.02x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.9 us: 1.02x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.1 ms: 1.06x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.74 ms: 1.09x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 215 us: 1.15x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.7 ms: 1.06x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.2 ms: 1.14x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.60 ms: 1.17x faster                                                       |
| genshi_xml      | 33.9 ms                                                     | 35.4 ms: 1.04x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 16.0 ms: 1.05x slower                                                       |
| django_template | 20.3 ms                                                     | 24.7 ms: 1.21x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 32.1 ms: 2.34x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 162 ms: 1.85x faster                                                        |
| mdp                        | 1.43 sec                                                    | 817 ms: 1.75x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 14.4 ms: 1.66x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 400 ms: 1.24x faster                                                        |
| async_tree_io              | 513 ms                                                      | 415 ms: 1.24x faster                                                        |
| deepcopy                   | 223 us                                                      | 181 us: 1.23x faster                                                        |
| async_tree_none            | 219 ms                                                      | 181 ms: 1.21x faster                                                        |
| mako                       | 6.56 ms                                                     | 5.60 ms: 1.17x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 172 ms: 1.16x faster                                                        |
| nbody                      | 66.3 ms                                                     | 56.9 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 335 ms: 1.14x faster                                                        |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.30 ms: 1.13x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.22 sec: 1.13x faster                                                      |
| float                      | 50.8 ms                                                     | 45.3 ms: 1.12x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 341 ms: 1.12x faster                                                        |
| telco                      | 4.85 ms                                                     | 4.42 ms: 1.10x faster                                                       |
| unpickle_pure_python       | 130 us                                                      | 119 us: 1.09x faster                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 2.64 sec: 1.09x faster                                                      |
| pyflate                    | 283 ms                                                      | 263 ms: 1.08x faster                                                        |
| scimark_fft                | 175 ms                                                      | 162 ms: 1.08x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.58 ms: 1.08x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 21.6 us: 1.07x faster                                                       |
| json                       | 3.30 ms                                                     | 3.10 ms: 1.07x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.92 us: 1.05x faster                                                       |
| go                         | 84.7 ms                                                     | 80.7 ms: 1.05x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 51.7 ms: 1.03x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.65 sec: 1.03x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 90.0 ms: 1.02x faster                                                       |
| pprint_pformat             | 977 ms                                                      | 957 ms: 1.02x faster                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.56 us: 1.02x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.9 us: 1.02x faster                                                       |
| fannkuch                   | 252 ms                                                      | 249 ms: 1.01x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 63.6 ms: 1.00x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 81.5 ms: 1.01x slower                                                       |
| shortest_path              | 355 ms                                                      | 359 ms: 1.01x slower                                                        |
| pidigits                   | 146 ms                                                      | 149 ms: 1.02x slower                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 46.6 ms: 1.02x slower                                                       |
| connected_components       | 320 ms                                                      | 328 ms: 1.03x slower                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.26 ms: 1.03x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.4 ms: 1.03x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 79.0 ms: 1.04x slower                                                       |
| 2to3                       | 215 ms                                                      | 223 ms: 1.04x slower                                                        |
| genshi_xml                 | 33.9 ms                                                     | 35.4 ms: 1.04x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.9 ms: 1.05x slower                                                       |
| sympy_str                  | 167 ms                                                      | 175 ms: 1.05x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 89.2 ms: 1.05x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 42.7 ms: 1.05x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.9 ms: 1.05x slower                                                       |
| chaos                      | 37.9 ms                                                     | 39.8 ms: 1.05x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 16.0 ms: 1.05x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.7 ms: 1.06x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 59.9 ms: 1.06x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 57.7 ns: 1.06x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.1 ms: 1.06x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.08 ms: 1.06x slower                                                       |
| sympy_expand               | 286 ms                                                      | 304 ms: 1.06x slower                                                        |
| pycparser                  | 695 ms                                                      | 739 ms: 1.06x slower                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 89.7 ms: 1.07x slower                                                       |
| regex_dna                  | 115 ms                                                      | 123 ms: 1.07x slower                                                        |
| sphinx                     | 617 ms                                                      | 662 ms: 1.07x slower                                                        |
| meteor_contest             | 72.0 ms                                                     | 77.3 ms: 1.07x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 43.2 ms: 1.08x slower                                                       |
| richards_super             | 29.8 ms                                                     | 32.2 ms: 1.08x slower                                                       |
| richards                   | 26.3 ms                                                     | 28.4 ms: 1.08x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 878 us: 1.08x slower                                                        |
| json_dumps                 | 6.19 ms                                                     | 6.74 ms: 1.09x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.29 us: 1.09x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.75 us: 1.09x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 61.6 ms: 1.10x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 114 us: 1.10x slower                                                        |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                                        |
| docutils                   | 1.53 sec                                                    | 1.72 sec: 1.12x slower                                                      |
| coverage                   | 45.3 ms                                                     | 51.4 ms: 1.13x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.2 ms: 1.14x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.15x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.9 us: 1.15x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 215 us: 1.15x slower                                                        |
| hexiom                     | 3.84 ms                                                     | 4.44 ms: 1.16x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.21 ms: 1.17x slower                                                       |
| raytrace                   | 153 ms                                                      | 179 ms: 1.17x slower                                                        |
| django_template            | 20.3 ms                                                     | 24.7 ms: 1.21x slower                                                       |
| many_optionals             | 361 us                                                      | 460 us: 1.27x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.7 ms: 1.54x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (3): pylint, xml_etree_process, pprint_safe_repr
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250503-3.14.0a7+-7363e8d-JIT/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.020x faster

# HPT report

- Reliability score: 62.96% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown