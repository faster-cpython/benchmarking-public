# Results vs. 3.12.0

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: linux-x86_64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.045x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 278 ms: 1.03x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.85 sec: 1.01x faster                                                      |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 614 ms: 1.70x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 631 ms: 1.67x faster                                                        |
| async_tree_none            | 452 ms                                                       | 271 ms: 1.67x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 328 ms: 1.66x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 271 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 501 ms: 1.39x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 509 ms: 1.37x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.58x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 67.3 ms: 1.14x faster                                                       |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                        |
| nbody          | 88.0 ms                                                      | 91.2 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 131 ms: 1.10x faster                                                        |
| regex_dna      | 239 ms                                                       | 222 ms: 1.07x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.42 ms: 1.04x faster                                                       |
| regex_v8       | 23.6 ms                                                      | 23.5 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.98 sec: 1.09x faster                                                      |
| xml_etree_generate   | 86.1 ms                                                      | 82.5 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 99.3 ms: 1.04x faster                                                       |
| json_dumps           | 10.2 ms                                                      | 9.92 ms: 1.03x faster                                                       |
| unpickle             | 14.8 us                                                      | 14.6 us: 1.02x faster                                                       |
| unpickle_pure_python | 210 us                                                       | 206 us: 1.01x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 57.6 ms: 1.01x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 146 ms: 1.02x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 325 us: 1.02x slower                                                        |
| pickle_dict          | 32.5 us                                                      | 33.5 us: 1.03x slower                                                       |
| json_loads           | 24.4 us                                                      | 26.1 us: 1.07x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 5.07 us: 1.09x slower                                                       |
| pickle_list          | 4.43 us                                                      | 4.84 us: 1.09x slower                                                       |
| pickle               | 10.5 us                                                      | 12.5 us: 1.19x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.83 ms: 1.02x slower                                                       |
| python_startup         | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 34.6 ms: 1.10x faster                                                       |
| mako            | 10.0 ms                                                      | 10.8 ms: 1.07x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.27 sec: 2.02x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 614 ms: 1.70x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 631 ms: 1.67x faster                                                        |
| async_tree_none            | 452 ms                                                       | 271 ms: 1.67x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 328 ms: 1.66x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 271 ms: 1.59x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 25.3 us: 1.45x faster                                                       |
| deepcopy                   | 368 us                                                       | 264 us: 1.39x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 501 ms: 1.39x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 509 ms: 1.37x faster                                                        |
| comprehensions             | 21.9 us                                                      | 16.3 us: 1.34x faster                                                       |
| generators                 | 37.4 ms                                                      | 28.1 ms: 1.33x faster                                                       |
| go                         | 150 ms                                                       | 117 ms: 1.28x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.0 ms: 1.26x faster                                                       |
| unpack_sequence            | 53.2 ns                                                      | 42.7 ns: 1.25x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.43 us: 1.16x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 59.3 ms: 1.16x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.91 us: 1.16x faster                                                       |
| logging_simple             | 6.71 us                                                      | 5.86 us: 1.15x faster                                                       |
| float                      | 76.6 ms                                                      | 67.3 ms: 1.14x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 59.0 ms: 1.11x faster                                                       |
| django_template            | 38.2 ms                                                      | 34.6 ms: 1.10x faster                                                       |
| regex_compile              | 144 ms                                                       | 131 ms: 1.10x faster                                                        |
| raytrace                   | 298 ms                                                       | 271 ms: 1.10x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 21.8 ms: 1.10x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.51 sec: 1.09x faster                                                      |
| tomli_loads                | 2.16 sec                                                     | 1.98 sec: 1.09x faster                                                      |
| chaos                      | 64.0 ms                                                      | 58.8 ms: 1.09x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 743 ms: 1.09x faster                                                        |
| pyflate                    | 439 ms                                                       | 405 ms: 1.08x faster                                                        |
| meteor_contest             | 128 ms                                                       | 118 ms: 1.08x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 150 ms: 1.08x faster                                                        |
| scimark_fft                | 301 ms                                                       | 279 ms: 1.08x faster                                                        |
| scimark_sor                | 109 ms                                                       | 101 ms: 1.07x faster                                                        |
| regex_dna                  | 239 ms                                                       | 222 ms: 1.07x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 85.9 ms: 1.07x faster                                                       |
| sympy_str                  | 302 ms                                                       | 283 ms: 1.07x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 93.7 ms: 1.05x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 76.5 ms: 1.05x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 21.9 ms: 1.05x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.42 ms: 1.04x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 82.5 ms: 1.04x faster                                                       |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 99.3 ms: 1.04x faster                                                       |
| hexiom                     | 5.96 ms                                                      | 5.77 ms: 1.03x faster                                                       |
| json_dumps                 | 10.2 ms                                                      | 9.92 ms: 1.03x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 368 ms: 1.03x faster                                                        |
| logging_silent             | 94.4 ns                                                      | 91.8 ns: 1.03x faster                                                       |
| 2to3                       | 285 ms                                                       | 278 ms: 1.03x faster                                                        |
| richards                   | 45.7 ms                                                      | 44.6 ms: 1.02x faster                                                       |
| deltablue                  | 3.24 ms                                                      | 3.17 ms: 1.02x faster                                                       |
| richards_super             | 51.3 ms                                                      | 50.4 ms: 1.02x faster                                                       |
| unpickle                   | 14.8 us                                                      | 14.6 us: 1.02x faster                                                       |
| unpickle_pure_python       | 210 us                                                       | 206 us: 1.01x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 57.6 ms: 1.01x faster                                                       |
| regex_v8                   | 23.6 ms                                                      | 23.5 ms: 1.01x faster                                                       |
| docutils                   | 2.87 sec                                                     | 2.85 sec: 1.01x faster                                                      |
| sympy_expand               | 484 ms                                                       | 481 ms: 1.01x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 146 ms: 1.02x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.82 us: 1.02x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 325 us: 1.02x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 8.83 ms: 1.02x slower                                                       |
| pickle_dict                | 32.5 us                                                      | 33.5 us: 1.03x slower                                                       |
| nbody                      | 88.0 ms                                                      | 91.2 ms: 1.04x slower                                                       |
| json                       | 5.12 ms                                                      | 5.33 ms: 1.04x slower                                                       |
| json_loads                 | 24.4 us                                                      | 26.1 us: 1.07x slower                                                       |
| mako                       | 10.0 ms                                                      | 10.8 ms: 1.07x slower                                                       |
| async_generators           | 390 ms                                                       | 422 ms: 1.08x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 5.07 us: 1.09x slower                                                       |
| pickle_list                | 4.43 us                                                      | 4.84 us: 1.09x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.62 ms: 1.10x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 167 us: 1.10x slower                                                        |
| pickle                     | 10.5 us                                                      | 12.5 us: 1.19x slower                                                       |
| coverage                   | 66.7 ms                                                      | 80.2 ms: 1.20x slower                                                       |
| python_startup             | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.83 ms: 1.78x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 6.25 ms: 1.80x slower                                                       |
| telco                      | 6.96 ms                                                      | 155 ms: 22.28x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 2.46 sec: 516.14x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                |

Benchmark hidden because not significant (6): bench_thread_pool, asyncio_websockets, pycparser, asyncio_tcp_ssl, nqueens, fannkuch
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.045x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.13x