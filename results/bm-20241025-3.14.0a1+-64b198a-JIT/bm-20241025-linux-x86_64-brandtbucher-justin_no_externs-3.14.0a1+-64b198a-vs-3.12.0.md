# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-x86_64
- commit hash: 64b198a
- commit date: 2024-10-25
- overall geometric mean: 1.028x faster
- HPT reliability: 96.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 286 ms: 1.04x slower                                                      |
| docutils       | 2.77 sec                                               | 2.97 sec: 1.07x slower                                                    |
| tornado_http   | 103 ms                                                 | 96.4 ms: 1.06x faster                                                     |
| Geometric mean | (ref)                                                  | 1.02x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 381 ms: 1.51x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 323 ms: 1.39x faster                                                      |
| async_tree_none            | 472 ms                                                 | 339 ms: 1.39x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 419 ms: 1.38x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 858 ms: 1.35x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 566 ms: 1.28x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 580 ms: 1.25x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 974 ms: 1.21x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.34x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 87.6 ms: 1.11x faster                                                     |
| float          | 84.7 ms                                                | 78.6 ms: 1.08x faster                                                     |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 142 ms: 1.04x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.77 ms: 1.04x slower                                                     |
| regex_dna      | 212 ms                                                 | 222 ms: 1.05x slower                                                      |
| regex_v8       | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.01 sec: 1.16x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 82.4 ms: 1.08x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.07x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 58.0 ms: 1.07x faster                                                     |
| json_loads           | 28.5 us                                                | 27.1 us: 1.05x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 102 ms: 1.05x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 226 us: 1.02x faster                                                      |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                     |
| python_startup         | 9.55 ms                                                | 11.8 ms: 1.24x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.8 ms: 1.10x faster                                                     |
| django_template | 34.6 ms                                                | 36.6 ms: 1.06x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 381 ms: 1.51x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 323 ms: 1.39x faster                                                      |
| async_tree_none            | 472 ms                                                 | 339 ms: 1.39x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 419 ms: 1.38x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 858 ms: 1.35x faster                                                      |
| deepcopy                   | 371 us                                                 | 283 us: 1.31x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 31.3 us: 1.30x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 566 ms: 1.28x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 580 ms: 1.25x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 974 ms: 1.21x faster                                                      |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                     |
| logging_format             | 7.23 us                                                | 6.13 us: 1.18x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.88 us: 1.16x faster                                                     |
| comprehensions             | 21.8 us                                                | 18.8 us: 1.16x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 2.01 sec: 1.16x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.60 us: 1.15x faster                                                     |
| scimark_fft                | 382 ms                                                 | 336 ms: 1.14x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 73.0 ms: 1.12x faster                                                     |
| nbody                      | 97.0 ms                                                | 87.6 ms: 1.11x faster                                                     |
| mako                       | 11.9 ms                                                | 10.8 ms: 1.10x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 82.4 ms: 1.08x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 69.6 ms: 1.08x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.44 ms: 1.08x faster                                                     |
| float                      | 84.7 ms                                                | 78.6 ms: 1.08x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.07x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 58.0 ms: 1.07x faster                                                     |
| tornado_http               | 103 ms                                                 | 96.4 ms: 1.06x faster                                                     |
| chaos                      | 67.0 ms                                                | 63.2 ms: 1.06x faster                                                     |
| json_loads                 | 28.5 us                                                | 27.1 us: 1.05x faster                                                     |
| raytrace                   | 312 ms                                                 | 297 ms: 1.05x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 102 ms: 1.05x faster                                                      |
| regex_compile              | 148 ms                                                 | 142 ms: 1.04x faster                                                      |
| richards_super             | 51.5 ms                                                | 49.7 ms: 1.04x faster                                                     |
| json                       | 5.26 ms                                                | 5.11 ms: 1.03x faster                                                     |
| sqlalchemy_imperative      | 18.7 ms                                                | 18.2 ms: 1.03x faster                                                     |
| fannkuch                   | 417 ms                                                 | 409 ms: 1.02x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 226 us: 1.02x faster                                                      |
| scimark_sor                | 129 ms                                                 | 127 ms: 1.01x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 766 ms: 1.01x faster                                                      |
| richards                   | 45.8 ms                                                | 45.3 ms: 1.01x faster                                                     |
| async_generators           | 463 ms                                                 | 458 ms: 1.01x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.56 sec: 1.01x faster                                                    |
| pyflate                    | 482 ms                                                 | 480 ms: 1.00x faster                                                      |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                      |
| go                         | 139 ms                                                 | 140 ms: 1.00x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.01x slower                                                      |
| meteor_contest             | 112 ms                                                 | 113 ms: 1.01x slower                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 148 ms: 1.01x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                     |
| sqlglot_transpile          | 1.68 ms                                                | 1.72 ms: 1.02x slower                                                     |
| sympy_str                  | 300 ms                                                 | 312 ms: 1.04x slower                                                      |
| 2to3                       | 274 ms                                                 | 286 ms: 1.04x slower                                                      |
| regex_effbot               | 3.61 ms                                                | 3.77 ms: 1.04x slower                                                     |
| mdp                        | 2.63 sec                                               | 2.75 sec: 1.04x slower                                                    |
| regex_dna                  | 212 ms                                                 | 222 ms: 1.05x slower                                                      |
| django_template            | 34.6 ms                                                | 36.6 ms: 1.06x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 893 us: 1.06x slower                                                      |
| logging_silent             | 104 ns                                                 | 111 ns: 1.07x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                     |
| sympy_sum                  | 169 ms                                                 | 180 ms: 1.07x slower                                                      |
| spectral_norm              | 115 ms                                                 | 123 ms: 1.07x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 118 ms: 1.07x slower                                                      |
| docutils                   | 2.77 sec                                               | 2.97 sec: 1.07x slower                                                    |
| sympy_expand               | 478 ms                                                 | 516 ms: 1.08x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 173 us: 1.10x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.10x slower                                                     |
| sympy_integrate            | 21.4 ms                                                | 24.0 ms: 1.12x slower                                                     |
| nqueens                    | 83.3 ms                                                | 93.2 ms: 1.12x slower                                                     |
| sqlglot_optimize           | 54.8 ms                                                | 61.6 ms: 1.12x slower                                                     |
| telco                      | 7.10 ms                                                | 8.04 ms: 1.13x slower                                                     |
| coverage                   | 72.7 ms                                                | 83.8 ms: 1.15x slower                                                     |
| hexiom                     | 6.41 ms                                                | 7.60 ms: 1.19x slower                                                     |
| generators                 | 31.2 ms                                                | 37.6 ms: 1.21x slower                                                     |
| python_startup             | 9.55 ms                                                | 11.8 ms: 1.24x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 4.75 ms: 1.25x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 2.68 ms: 1.81x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 84.7 ms: 3.53x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (6): scimark_sparse_mat_mult, dulwich_log, coroutines, sqlglot_parse, pycparser, pickle_pure_python
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241025-3.14.0a1+-64b198a-JIT/bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.028x faster
# HPT report

- Reliability score: 96.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.14x