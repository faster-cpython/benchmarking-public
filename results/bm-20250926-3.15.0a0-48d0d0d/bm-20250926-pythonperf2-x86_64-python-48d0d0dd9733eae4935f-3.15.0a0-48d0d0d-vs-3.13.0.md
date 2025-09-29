# Results vs. 3.13.0

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: linux-x86_64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.050x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 278 ms: 1.05x faster                                                        |
| docutils       | 2.83 sec                                                     | 2.85 sec: 1.01x slower                                                      |
| html5lib       | 73.5 ms                                                      | 64.9 ms: 1.13x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.08 sec: 1.04x faster                                                      |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                                        |
| async_tree_none            | 376 ms                                                       | 271 ms: 1.39x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 328 ms: 1.38x faster                                                        |
| async_tree_io              | 843 ms                                                       | 614 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 631 ms: 1.32x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 271 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 501 ms: 1.21x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 509 ms: 1.14x faster                                                        |
| async_generators           | 457 ms                                                       | 422 ms: 1.08x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.9 ms: 1.02x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.22x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 67.3 ms: 1.21x faster                                                       |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                        |
| nbody          | 89.3 ms                                                      | 91.2 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.5 ms: 1.11x faster                                                       |
| regex_dna      | 247 ms                                                       | 222 ms: 1.11x faster                                                        |
| regex_compile  | 143 ms                                                       | 131 ms: 1.09x faster                                                        |
| regex_effbot   | 3.67 ms                                                      | 3.42 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.98 sec: 1.24x faster                                                      |
| json_dumps           | 11.1 ms                                                      | 9.92 ms: 1.12x faster                                                       |
| xml_etree_process    | 61.2 ms                                                      | 57.6 ms: 1.06x faster                                                       |
| unpickle_pure_python | 217 us                                                       | 206 us: 1.05x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 82.5 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 99.3 ms: 1.04x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 146 ms: 1.03x faster                                                        |
| pickle_pure_python   | 323 us                                                       | 325 us: 1.01x slower                                                        |
| json_loads           | 24.7 us                                                      | 26.1 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.4 ms: 1.03x faster                                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.83 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.2 ms: 1.13x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 52.4 ms: 1.09x faster                                                       |
| django_template | 36.4 ms                                                      | 34.6 ms: 1.05x faster                                                       |
| mako            | 10.4 ms                                                      | 10.8 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.27 sec: 1.99x faster                                                      |
| deepcopy_memo              | 38.6 us                                                      | 25.3 us: 1.52x faster                                                       |
| deepcopy                   | 392 us                                                       | 264 us: 1.48x faster                                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                                        |
| go                         | 162 ms                                                       | 117 ms: 1.39x faster                                                        |
| async_tree_none            | 376 ms                                                       | 271 ms: 1.39x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 328 ms: 1.38x faster                                                        |
| async_tree_io              | 843 ms                                                       | 614 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 631 ms: 1.32x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 271 ms: 1.28x faster                                                        |
| pyflate                    | 503 ms                                                       | 405 ms: 1.24x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 1.98 sec: 1.24x faster                                                      |
| deepcopy_reduce            | 3.54 us                                                      | 2.91 us: 1.22x faster                                                       |
| scimark_sor                | 123 ms                                                       | 101 ms: 1.22x faster                                                        |
| float                      | 81.3 ms                                                      | 67.3 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 501 ms: 1.21x faster                                                        |
| generators                 | 33.6 ms                                                      | 28.1 ms: 1.20x faster                                                       |
| richards                   | 52.9 ms                                                      | 44.6 ms: 1.19x faster                                                       |
| richards_super             | 59.6 ms                                                      | 50.4 ms: 1.18x faster                                                       |
| scimark_fft                | 328 ms                                                       | 279 ms: 1.17x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 15.0 ms: 1.17x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 59.0 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 509 ms: 1.14x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.51 sec: 1.14x faster                                                      |
| hexiom                     | 6.55 ms                                                      | 5.77 ms: 1.13x faster                                                       |
| pprint_safe_repr           | 843 ms                                                       | 743 ms: 1.13x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 64.9 ms: 1.13x faster                                                       |
| spectral_norm              | 97.0 ms                                                      | 85.9 ms: 1.13x faster                                                       |
| genshi_text                | 26.2 ms                                                      | 23.2 ms: 1.13x faster                                                       |
| json_dumps                 | 11.1 ms                                                      | 9.92 ms: 1.12x faster                                                       |
| scimark_monte_carlo        | 66.1 ms                                                      | 59.3 ms: 1.11x faster                                                       |
| regex_v8                   | 26.1 ms                                                      | 23.5 ms: 1.11x faster                                                       |
| regex_dna                  | 247 ms                                                       | 222 ms: 1.11x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.65 sec: 1.09x faster                                                      |
| meteor_contest             | 130 ms                                                       | 118 ms: 1.09x faster                                                        |
| pylint                     | 347 ms                                                       | 317 ms: 1.09x faster                                                        |
| logging_simple             | 6.39 us                                                      | 5.86 us: 1.09x faster                                                       |
| regex_compile              | 143 ms                                                       | 131 ms: 1.09x faster                                                        |
| genshi_xml                 | 57.1 ms                                                      | 52.4 ms: 1.09x faster                                                       |
| thrift                     | 901 us                                                       | 830 us: 1.09x faster                                                        |
| async_generators           | 457 ms                                                       | 422 ms: 1.08x faster                                                        |
| sympy_integrate            | 23.6 ms                                                      | 21.8 ms: 1.08x faster                                                       |
| logging_format             | 6.94 us                                                      | 6.43 us: 1.08x faster                                                       |
| deltablue                  | 3.42 ms                                                      | 3.17 ms: 1.08x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.42 ms: 1.07x faster                                                       |
| json                       | 5.69 ms                                                      | 5.33 ms: 1.07x faster                                                       |
| logging_silent             | 97.9 ns                                                      | 91.8 ns: 1.07x faster                                                       |
| xml_etree_process          | 61.2 ms                                                      | 57.6 ms: 1.06x faster                                                       |
| sympy_expand               | 509 ms                                                       | 481 ms: 1.06x faster                                                        |
| 2to3                       | 293 ms                                                       | 278 ms: 1.05x faster                                                        |
| unpickle_pure_python       | 217 us                                                       | 206 us: 1.05x faster                                                        |
| scimark_lu                 | 98.7 ms                                                      | 93.7 ms: 1.05x faster                                                       |
| sympy_str                  | 298 ms                                                       | 283 ms: 1.05x faster                                                        |
| django_template            | 36.4 ms                                                      | 34.6 ms: 1.05x faster                                                       |
| xml_etree_generate         | 86.5 ms                                                      | 82.5 ms: 1.05x faster                                                       |
| k_core                     | 2.17 sec                                                     | 2.08 sec: 1.04x faster                                                      |
| comprehensions             | 17.0 us                                                      | 16.3 us: 1.04x faster                                                       |
| sphinx                     | 1.12 sec                                                     | 1.08 sec: 1.04x faster                                                      |
| xml_etree_iterparse        | 103 ms                                                       | 99.3 ms: 1.04x faster                                                       |
| fannkuch                   | 363 ms                                                       | 351 ms: 1.03x faster                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.62 ms: 1.03x faster                                                       |
| python_startup             | 15.9 ms                                                      | 15.4 ms: 1.03x faster                                                       |
| sympy_sum                  | 155 ms                                                       | 150 ms: 1.03x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.82 us: 1.03x faster                                                       |
| xml_etree_parse            | 150 ms                                                       | 146 ms: 1.03x faster                                                        |
| chaos                      | 60.2 ms                                                      | 58.8 ms: 1.02x faster                                                       |
| connected_components       | 432 ms                                                       | 424 ms: 1.02x faster                                                        |
| shortest_path              | 460 ms                                                       | 453 ms: 1.02x faster                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 8.83 ms: 1.01x faster                                                       |
| pycparser                  | 1.24 sec                                                     | 1.23 sec: 1.01x faster                                                      |
| typing_runtime_protocols   | 169 us                                                       | 167 us: 1.01x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                                        |
| nqueens                    | 90.7 ms                                                      | 90.1 ms: 1.01x faster                                                       |
| coverage                   | 80.0 ms                                                      | 80.2 ms: 1.00x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 325 us: 1.01x slower                                                        |
| docutils                   | 2.83 sec                                                     | 2.85 sec: 1.01x slower                                                      |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 21.9 ms: 1.02x slower                                                       |
| nbody                      | 89.3 ms                                                      | 91.2 ms: 1.02x slower                                                       |
| mako                       | 10.4 ms                                                      | 10.8 ms: 1.04x slower                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 76.5 ms: 1.04x slower                                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.83 ms: 1.06x slower                                                       |
| json_loads                 | 24.7 us                                                      | 26.1 us: 1.06x slower                                                       |
| many_optionals             | 930 us                                                       | 1.22 ms: 1.31x slower                                                       |
| gc_traversal               | 4.74 ms                                                      | 6.25 ms: 1.32x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 44.2 ms: 2.53x slower                                                       |
| telco                      | 8.79 ms                                                      | 155 ms: 17.65x slower                                                       |
| bench_mp_pool              | 5.12 ms                                                      | 2.46 sec: 480.02x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (3): raytrace, djangocms, bench_thread_pool
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.050x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x