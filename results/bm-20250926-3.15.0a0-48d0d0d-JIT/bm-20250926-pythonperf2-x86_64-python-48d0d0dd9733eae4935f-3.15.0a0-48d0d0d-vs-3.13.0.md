# Results vs. 3.13.0

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: linux-x86_64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.047x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 284 ms: 1.03x faster                                                        |
| docutils       | 2.83 sec                                                     | 2.88 sec: 1.02x slower                                                      |
| html5lib       | 73.5 ms                                                      | 65.9 ms: 1.11x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 334 ms: 1.40x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 329 ms: 1.38x faster                                                        |
| async_tree_none            | 376 ms                                                       | 275 ms: 1.37x faster                                                        |
| async_tree_io              | 843 ms                                                       | 619 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 636 ms: 1.31x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 274 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 501 ms: 1.21x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                        |
| async_generators           | 457 ms                                                       | 438 ms: 1.04x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 22.8 ms: 1.06x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 68.4 ms: 1.19x faster                                                       |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                        |
| nbody          | 89.3 ms                                                      | 97.7 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.4 ms: 1.12x faster                                                       |
| regex_compile  | 143 ms                                                       | 131 ms: 1.09x faster                                                        |
| regex_dna      | 247 ms                                                       | 231 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.89 sec: 1.30x faster                                                      |
| unpickle_pure_python | 217 us                                                       | 193 us: 1.13x faster                                                        |
| json_dumps           | 11.1 ms                                                      | 10.0 ms: 1.11x faster                                                       |
| xml_etree_process    | 61.2 ms                                                      | 55.3 ms: 1.11x faster                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 80.0 ms: 1.08x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 142 ms: 1.06x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 97.6 ms: 1.05x faster                                                       |
| pickle_pure_python   | 323 us                                                       | 325 us: 1.01x slower                                                        |
| json_loads           | 24.7 us                                                      | 26.4 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.5 ms: 1.03x faster                                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.88 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.2 ms: 1.13x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 53.6 ms: 1.06x faster                                                       |
| mako            | 10.4 ms                                                      | 9.90 ms: 1.05x faster                                                       |
| django_template | 36.4 ms                                                      | 35.0 ms: 1.04x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.07x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.29 sec: 1.97x faster                                                      |
| deepcopy_memo              | 38.6 us                                                      | 23.3 us: 1.66x faster                                                       |
| deepcopy                   | 392 us                                                       | 268 us: 1.46x faster                                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 334 ms: 1.40x faster                                                        |
| richards                   | 52.9 ms                                                      | 38.2 ms: 1.39x faster                                                       |
| async_tree_memoization     | 453 ms                                                       | 329 ms: 1.38x faster                                                        |
| async_tree_none            | 376 ms                                                       | 275 ms: 1.37x faster                                                        |
| go                         | 162 ms                                                       | 119 ms: 1.36x faster                                                        |
| async_tree_io              | 843 ms                                                       | 619 ms: 1.36x faster                                                        |
| richards_super             | 59.6 ms                                                      | 44.5 ms: 1.34x faster                                                       |
| async_tree_io_tg           | 831 ms                                                       | 636 ms: 1.31x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 1.89 sec: 1.30x faster                                                      |
| pyflate                    | 503 ms                                                       | 392 ms: 1.28x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 274 ms: 1.26x faster                                                        |
| scimark_sor                | 123 ms                                                       | 102 ms: 1.21x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.93 us: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 501 ms: 1.21x faster                                                        |
| scimark_fft                | 328 ms                                                       | 275 ms: 1.19x faster                                                        |
| float                      | 81.3 ms                                                      | 68.4 ms: 1.19x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 58.6 ms: 1.16x faster                                                       |
| pprint_pformat             | 1.72 sec                                                     | 1.49 sec: 1.15x faster                                                      |
| pprint_safe_repr           | 843 ms                                                       | 731 ms: 1.15x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 15.3 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 23.2 ms: 1.13x faster                                                       |
| unpickle_pure_python       | 217 us                                                       | 193 us: 1.13x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 86.3 ms: 1.12x faster                                                       |
| generators                 | 33.6 ms                                                      | 30.0 ms: 1.12x faster                                                       |
| regex_v8                   | 26.1 ms                                                      | 23.4 ms: 1.12x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.56 sec: 1.11x faster                                                      |
| html5lib                   | 73.5 ms                                                      | 65.9 ms: 1.11x faster                                                       |
| json_dumps                 | 11.1 ms                                                      | 10.0 ms: 1.11x faster                                                       |
| xml_etree_process          | 61.2 ms                                                      | 55.3 ms: 1.11x faster                                                       |
| hexiom                     | 6.55 ms                                                      | 5.92 ms: 1.11x faster                                                       |
| regex_compile              | 143 ms                                                       | 131 ms: 1.09x faster                                                        |
| pylint                     | 347 ms                                                       | 319 ms: 1.09x faster                                                        |
| logging_simple             | 6.39 us                                                      | 5.90 us: 1.08x faster                                                       |
| xml_etree_generate         | 86.5 ms                                                      | 80.0 ms: 1.08x faster                                                       |
| k_core                     | 2.17 sec                                                     | 2.01 sec: 1.08x faster                                                      |
| scimark_monte_carlo        | 66.1 ms                                                      | 61.5 ms: 1.07x faster                                                       |
| meteor_contest             | 130 ms                                                       | 121 ms: 1.07x faster                                                        |
| regex_dna                  | 247 ms                                                       | 231 ms: 1.07x faster                                                        |
| logging_format             | 6.94 us                                                      | 6.51 us: 1.07x faster                                                       |
| logging_silent             | 97.9 ns                                                      | 91.9 ns: 1.06x faster                                                       |
| genshi_xml                 | 57.1 ms                                                      | 53.6 ms: 1.06x faster                                                       |
| deltablue                  | 3.42 ms                                                      | 3.21 ms: 1.06x faster                                                       |
| xml_etree_parse            | 150 ms                                                       | 142 ms: 1.06x faster                                                        |
| sympy_integrate            | 23.6 ms                                                      | 22.3 ms: 1.06x faster                                                       |
| thrift                     | 901 us                                                       | 855 us: 1.05x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 97.6 ms: 1.05x faster                                                       |
| connected_components       | 432 ms                                                       | 411 ms: 1.05x faster                                                        |
| scimark_lu                 | 98.7 ms                                                      | 93.9 ms: 1.05x faster                                                       |
| mako                       | 10.4 ms                                                      | 9.90 ms: 1.05x faster                                                       |
| pycparser                  | 1.24 sec                                                     | 1.19 sec: 1.05x faster                                                      |
| json                       | 5.69 ms                                                      | 5.45 ms: 1.04x faster                                                       |
| async_generators           | 457 ms                                                       | 438 ms: 1.04x faster                                                        |
| django_template            | 36.4 ms                                                      | 35.0 ms: 1.04x faster                                                       |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| shortest_path              | 460 ms                                                       | 446 ms: 1.03x faster                                                        |
| 2to3                       | 293 ms                                                       | 284 ms: 1.03x faster                                                        |
| python_startup             | 15.9 ms                                                      | 15.5 ms: 1.03x faster                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.83 us: 1.03x faster                                                       |
| sympy_str                  | 298 ms                                                       | 291 ms: 1.02x faster                                                        |
| sympy_expand               | 509 ms                                                       | 498 ms: 1.02x faster                                                        |
| sympy_sum                  | 155 ms                                                       | 151 ms: 1.02x faster                                                        |
| chaos                      | 60.2 ms                                                      | 59.1 ms: 1.02x faster                                                       |
| python_startup_no_site     | 8.96 ms                                                      | 8.88 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.74 ms: 1.01x faster                                                       |
| pickle_pure_python         | 323 us                                                       | 325 us: 1.01x slower                                                        |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                        |
| nqueens                    | 90.7 ms                                                      | 91.6 ms: 1.01x slower                                                       |
| fannkuch                   | 363 ms                                                       | 368 ms: 1.01x slower                                                        |
| coverage                   | 80.0 ms                                                      | 81.4 ms: 1.02x slower                                                       |
| docutils                   | 2.83 sec                                                     | 2.88 sec: 1.02x slower                                                      |
| comprehensions             | 17.0 us                                                      | 17.4 us: 1.02x slower                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 75.8 ms: 1.03x slower                                                       |
| raytrace                   | 273 ms                                                       | 284 ms: 1.04x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.8 ms: 1.06x slower                                                       |
| json_loads                 | 24.7 us                                                      | 26.4 us: 1.07x slower                                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.90 ms: 1.08x slower                                                       |
| nbody                      | 89.3 ms                                                      | 97.7 ms: 1.09x slower                                                       |
| many_optionals             | 930 us                                                       | 1.24 ms: 1.33x slower                                                       |
| gc_traversal               | 4.74 ms                                                      | 6.73 ms: 1.42x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 44.7 ms: 2.56x slower                                                       |
| telco                      | 8.79 ms                                                      | 155 ms: 17.62x slower                                                       |
| bench_mp_pool              | 5.12 ms                                                      | 2.51 sec: 490.29x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (5): asyncio_websockets, djangocms, bench_thread_pool, typing_runtime_protocols, regex_effbot
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.047x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.12x