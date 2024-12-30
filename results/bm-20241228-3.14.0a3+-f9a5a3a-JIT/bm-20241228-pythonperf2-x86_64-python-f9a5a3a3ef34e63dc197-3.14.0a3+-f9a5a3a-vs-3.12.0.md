# Results vs. 3.12.0

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: linux-x86_64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.016x faster
- HPT reliability: 69.03%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 293 ms: 1.03x slower                                                         |
| docutils       | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 646 ms: 1.63x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 333 ms: 1.62x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 661 ms: 1.58x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 274 ms: 1.57x faster                                                         |
| async_tree_none            | 452 ms                                                       | 297 ms: 1.52x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 366 ms: 1.49x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 508 ms: 1.37x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 527 ms: 1.32x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.51x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 73.0 ms: 1.05x faster                                                        |
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| nbody          | 88.0 ms                                                      | 92.6 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.23 ms: 1.11x faster                                                        |
| regex_compile  | 144 ms                                                       | 139 ms: 1.03x faster                                                         |
| regex_dna      | 239 ms                                                       | 244 ms: 1.02x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 24.9 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 93.7 ms: 1.10x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.03 sec: 1.06x faster                                                       |
| unpickle_pure_python | 210 us                                                       | 198 us: 1.06x faster                                                         |
| xml_etree_parse      | 144 ms                                                       | 137 ms: 1.05x faster                                                         |
| xml_etree_generate   | 86.1 ms                                                      | 82.5 ms: 1.04x faster                                                        |
| json_loads           | 24.4 us                                                      | 25.2 us: 1.03x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 340 us: 1.07x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.04 ms: 1.05x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.61 ms: 1.04x faster                                                        |
| django_template | 38.2 ms                                                      | 38.5 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 646 ms: 1.63x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 333 ms: 1.62x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 661 ms: 1.58x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 274 ms: 1.57x faster                                                         |
| async_tree_none            | 452 ms                                                       | 297 ms: 1.52x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 366 ms: 1.49x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 508 ms: 1.37x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 527 ms: 1.32x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 30.1 us: 1.22x faster                                                        |
| deepcopy                   | 368 us                                                       | 306 us: 1.21x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 16.2 ms: 1.17x faster                                                        |
| comprehensions             | 21.9 us                                                      | 19.4 us: 1.13x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.00 us: 1.12x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.23 ms: 1.11x faster                                                        |
| scimark_sor                | 109 ms                                                       | 98.6 ms: 1.10x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 62.5 ms: 1.10x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 93.7 ms: 1.10x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 147 ms: 1.09x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 21.2 ms: 1.08x faster                                                        |
| go                         | 150 ms                                                       | 139 ms: 1.07x faster                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 75.0 ms: 1.07x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.03 sec: 1.06x faster                                                       |
| unpickle_pure_python       | 210 us                                                       | 198 us: 1.06x faster                                                         |
| float                      | 76.6 ms                                                      | 73.0 ms: 1.05x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 137 ms: 1.05x faster                                                         |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| scimark_lu                 | 98.8 ms                                                      | 94.6 ms: 1.04x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 82.5 ms: 1.04x faster                                                        |
| mako                       | 10.0 ms                                                      | 9.61 ms: 1.04x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 778 ms: 1.04x faster                                                         |
| logging_simple             | 6.71 us                                                      | 6.49 us: 1.03x faster                                                        |
| logging_format             | 7.48 us                                                      | 7.24 us: 1.03x faster                                                        |
| regex_compile              | 144 ms                                                       | 139 ms: 1.03x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.2 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.61 sec: 1.03x faster                                                       |
| pyflate                    | 439 ms                                                       | 432 ms: 1.02x faster                                                         |
| sympy_sum                  | 162 ms                                                       | 161 ms: 1.01x faster                                                         |
| scimark_fft                | 301 ms                                                       | 299 ms: 1.01x faster                                                         |
| django_template            | 38.2 ms                                                      | 38.5 ms: 1.01x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 92.5 ms: 1.01x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 24.2 ms: 1.01x slower                                                        |
| mdp                        | 2.57 sec                                                     | 2.60 sec: 1.01x slower                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.82 us: 1.02x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.30 ms: 1.02x slower                                                        |
| sympy_str                  | 302 ms                                                       | 308 ms: 1.02x slower                                                         |
| regex_dna                  | 239 ms                                                       | 244 ms: 1.02x slower                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 1.82 ms: 1.02x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.03x slower                                                        |
| 2to3                       | 285 ms                                                       | 293 ms: 1.03x slower                                                         |
| richards_super             | 51.3 ms                                                      | 52.8 ms: 1.03x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.2 us: 1.03x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.28 sec: 1.03x slower                                                       |
| docutils                   | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                       |
| meteor_contest             | 128 ms                                                       | 134 ms: 1.04x slower                                                         |
| dulwich_log                | 65.4 ms                                                      | 68.3 ms: 1.05x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.04 ms: 1.05x slower                                                        |
| nbody                      | 88.0 ms                                                      | 92.6 ms: 1.05x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 24.9 ms: 1.05x slower                                                        |
| chaos                      | 64.0 ms                                                      | 67.5 ms: 1.05x slower                                                        |
| bench_thread_pool          | 950 us                                                       | 1.01 ms: 1.06x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 340 us: 1.07x slower                                                         |
| logging_silent             | 94.4 ns                                                      | 101 ns: 1.07x slower                                                         |
| fannkuch                   | 350 ms                                                       | 379 ms: 1.08x slower                                                         |
| generators                 | 37.4 ms                                                      | 40.6 ms: 1.08x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 126 ms: 1.09x slower                                                         |
| sympy_expand               | 484 ms                                                       | 526 ms: 1.09x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 62.5 ms: 1.09x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                                        |
| raytrace                   | 298 ms                                                       | 329 ms: 1.11x slower                                                         |
| nqueens                    | 89.9 ms                                                      | 100.0 ms: 1.11x slower                                                       |
| telco                      | 6.96 ms                                                      | 7.90 ms: 1.13x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.83 ms: 1.15x slower                                                        |
| async_generators           | 390 ms                                                       | 457 ms: 1.17x slower                                                         |
| typing_runtime_protocols   | 152 us                                                       | 178 us: 1.17x slower                                                         |
| coverage                   | 66.7 ms                                                      | 79.6 ms: 1.19x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 7.25 ms: 1.22x slower                                                        |
| mypy2                      | 830 ms                                                       | 1.04 sec: 1.26x slower                                                       |
| python_startup             | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.64 ms: 1.66x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.30 ms: 1.81x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.15 sec: 241.09x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                                 |

Benchmark hidden because not significant (4): asyncio_websockets, json, xml_etree_process, richards
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.016x faster

# HPT report

- Reliability score: 69.03% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x