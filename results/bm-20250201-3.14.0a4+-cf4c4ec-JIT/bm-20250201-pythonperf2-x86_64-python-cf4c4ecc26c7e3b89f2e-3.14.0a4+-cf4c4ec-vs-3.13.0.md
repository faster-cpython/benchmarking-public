# Results vs. 3.13.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-x86_64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.035x faster
- HPT reliability: 99.72%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 289 ms: 1.01x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.95 sec: 1.05x slower                                                       |
| html5lib       | 73.5 ms                                                      | 69.7 ms: 1.05x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.14 sec: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 344 ms: 1.36x faster                                                         |
| async_tree_io              | 843 ms                                                       | 656 ms: 1.28x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 657 ms: 1.27x faster                                                         |
| async_tree_none            | 376 ms                                                       | 298 ms: 1.26x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 359 ms: 1.26x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 284 ms: 1.22x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 528 ms: 1.14x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 518 ms: 1.12x faster                                                         |
| async_generators           | 457 ms                                                       | 426 ms: 1.07x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 20.7 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.18x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 67.7 ms: 1.20x faster                                                        |
| pidigits       | 252 ms                                                       | 253 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.13 ms: 1.17x faster                                                        |
| regex_dna      | 247 ms                                                       | 239 ms: 1.03x faster                                                         |
| regex_compile  | 143 ms                                                       | 139 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.04 sec: 1.21x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 136 ms: 1.11x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 94.5 ms: 1.09x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 80.3 ms: 1.08x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 203 us: 1.07x faster                                                         |
| xml_etree_process    | 61.2 ms                                                      | 57.1 ms: 1.07x faster                                                        |
| json_dumps           | 11.1 ms                                                      | 11.0 ms: 1.02x faster                                                        |
| pickle_pure_python   | 323 us                                                       | 334 us: 1.04x slower                                                         |
| json_loads           | 24.7 us                                                      | 26.7 us: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.06x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.03 ms: 1.01x slower                                                        |
| python_startup         | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.42 ms: 1.10x faster                                                        |
| genshi_text     | 26.2 ms                                                      | 26.5 ms: 1.01x slower                                                        |
| django_template | 36.4 ms                                                      | 37.7 ms: 1.04x slower                                                        |
| genshi_xml      | 57.1 ms                                                      | 61.8 ms: 1.08x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 344 ms: 1.36x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 29.9 us: 1.29x faster                                                        |
| async_tree_io              | 843 ms                                                       | 656 ms: 1.28x faster                                                         |
| deepcopy                   | 392 us                                                       | 308 us: 1.27x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 657 ms: 1.27x faster                                                         |
| async_tree_none            | 376 ms                                                       | 298 ms: 1.26x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 359 ms: 1.26x faster                                                         |
| scimark_sor                | 123 ms                                                       | 101 ms: 1.22x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 284 ms: 1.22x faster                                                         |
| tomli_loads                | 2.46 sec                                                     | 2.04 sec: 1.21x faster                                                       |
| float                      | 81.3 ms                                                      | 67.7 ms: 1.20x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.13 ms: 1.17x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 3.03 us: 1.17x faster                                                        |
| go                         | 162 ms                                                       | 140 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 528 ms: 1.14x faster                                                         |
| telco                      | 8.79 ms                                                      | 7.71 ms: 1.14x faster                                                        |
| richards                   | 52.9 ms                                                      | 46.8 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 518 ms: 1.12x faster                                                         |
| richards_super             | 59.6 ms                                                      | 53.2 ms: 1.12x faster                                                        |
| scimark_fft                | 328 ms                                                       | 294 ms: 1.11x faster                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 4.60 sec: 1.11x faster                                                       |
| xml_etree_parse            | 150 ms                                                       | 136 ms: 1.11x faster                                                         |
| spectral_norm              | 97.0 ms                                                      | 87.8 ms: 1.10x faster                                                        |
| mako                       | 10.4 ms                                                      | 9.42 ms: 1.10x faster                                                        |
| pyflate                    | 503 ms                                                       | 458 ms: 1.10x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 94.5 ms: 1.09x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 16.3 ms: 1.08x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 80.3 ms: 1.08x faster                                                        |
| pprint_safe_repr           | 843 ms                                                       | 785 ms: 1.07x faster                                                         |
| unpickle_pure_python       | 217 us                                                       | 203 us: 1.07x faster                                                         |
| connected_components       | 432 ms                                                       | 403 ms: 1.07x faster                                                         |
| async_generators           | 457 ms                                                       | 426 ms: 1.07x faster                                                         |
| xml_etree_process          | 61.2 ms                                                      | 57.1 ms: 1.07x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.62 sec: 1.06x faster                                                       |
| pylint                     | 347 ms                                                       | 328 ms: 1.06x faster                                                         |
| sqlite_synth               | 2.91 us                                                      | 2.75 us: 1.05x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 69.7 ms: 1.05x faster                                                        |
| shortest_path              | 460 ms                                                       | 438 ms: 1.05x faster                                                         |
| k_core                     | 2.17 sec                                                     | 2.07 sec: 1.05x faster                                                       |
| coroutines                 | 21.6 ms                                                      | 20.7 ms: 1.04x faster                                                        |
| regex_dna                  | 247 ms                                                       | 239 ms: 1.03x faster                                                         |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.7 ms: 1.03x faster                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 64.3 ms: 1.03x faster                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 145 ms: 1.03x faster                                                         |
| regex_compile              | 143 ms                                                       | 139 ms: 1.02x faster                                                         |
| json                       | 5.69 ms                                                      | 5.56 ms: 1.02x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 66.8 ms: 1.02x faster                                                        |
| json_dumps                 | 11.1 ms                                                      | 11.0 ms: 1.02x faster                                                        |
| 2to3                       | 293 ms                                                       | 289 ms: 1.01x faster                                                         |
| logging_simple             | 6.39 us                                                      | 6.30 us: 1.01x faster                                                        |
| thrift                     | 901 us                                                       | 889 us: 1.01x faster                                                         |
| create_gc_cycles           | 2.68 ms                                                      | 2.65 ms: 1.01x faster                                                        |
| coverage                   | 80.0 ms                                                      | 79.2 ms: 1.01x faster                                                        |
| logging_format             | 6.94 us                                                      | 6.90 us: 1.01x faster                                                        |
| pidigits                   | 252 ms                                                       | 253 ms: 1.00x slower                                                         |
| sqlglot_parse              | 1.40 ms                                                      | 1.41 ms: 1.00x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 9.03 ms: 1.01x slower                                                        |
| python_startup             | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                        |
| meteor_contest             | 130 ms                                                       | 131 ms: 1.01x slower                                                         |
| sphinx                     | 1.12 sec                                                     | 1.14 sec: 1.01x slower                                                       |
| logging_silent             | 97.9 ns                                                      | 99.1 ns: 1.01x slower                                                        |
| genshi_text                | 26.2 ms                                                      | 26.5 ms: 1.01x slower                                                        |
| sympy_sum                  | 155 ms                                                       | 157 ms: 1.01x slower                                                         |
| mdp                        | 2.54 sec                                                     | 2.58 sec: 1.01x slower                                                       |
| sympy_expand               | 509 ms                                                       | 517 ms: 1.01x slower                                                         |
| sympy_str                  | 298 ms                                                       | 303 ms: 1.02x slower                                                         |
| sympy_integrate            | 23.6 ms                                                      | 24.0 ms: 1.02x slower                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.88 ms: 1.02x slower                                                        |
| scimark_lu                 | 98.7 ms                                                      | 101 ms: 1.03x slower                                                         |
| bench_thread_pool          | 942 us                                                       | 969 us: 1.03x slower                                                         |
| sqlglot_optimize           | 59.3 ms                                                      | 61.1 ms: 1.03x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 175 us: 1.03x slower                                                         |
| pickle_pure_python         | 323 us                                                       | 334 us: 1.04x slower                                                         |
| django_template            | 36.4 ms                                                      | 37.7 ms: 1.04x slower                                                        |
| docutils                   | 2.83 sec                                                     | 2.95 sec: 1.05x slower                                                       |
| sqlglot_normalize          | 119 ms                                                       | 125 ms: 1.05x slower                                                         |
| crypto_pyaes               | 73.3 ms                                                      | 78.2 ms: 1.07x slower                                                        |
| fannkuch                   | 363 ms                                                       | 388 ms: 1.07x slower                                                         |
| json_loads                 | 24.7 us                                                      | 26.7 us: 1.08x slower                                                        |
| genshi_xml                 | 57.1 ms                                                      | 61.8 ms: 1.08x slower                                                        |
| many_optionals             | 930 us                                                       | 1.03 ms: 1.11x slower                                                        |
| comprehensions             | 17.0 us                                                      | 19.0 us: 1.12x slower                                                        |
| raytrace                   | 273 ms                                                       | 306 ms: 1.12x slower                                                         |
| chaos                      | 60.2 ms                                                      | 67.6 ms: 1.12x slower                                                        |
| nqueens                    | 90.7 ms                                                      | 103 ms: 1.14x slower                                                         |
| hexiom                     | 6.55 ms                                                      | 7.54 ms: 1.15x slower                                                        |
| generators                 | 33.6 ms                                                      | 42.0 ms: 1.25x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 23.0 ms: 1.32x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.29 ms: 1.33x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.33 sec: 259.04x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                 |

Benchmark hidden because not significant (6): regex_v8, asyncio_websockets, sqlglot_transpile, pycparser, nbody, deltablue
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.035x faster

# HPT report

- Reliability score: 99.72% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x