# Results vs. 3.12.0

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: linux-x86_64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.042x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 284 ms: 1.00x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.88 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 619 ms: 1.68x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 636 ms: 1.66x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 329 ms: 1.65x faster                                                        |
| async_tree_none            | 452 ms                                                       | 275 ms: 1.64x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 334 ms: 1.62x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 274 ms: 1.57x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 501 ms: 1.39x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.57x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 68.4 ms: 1.12x faster                                                       |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                        |
| nbody          | 88.0 ms                                                      | 97.7 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 131 ms: 1.10x faster                                                        |
| regex_dna      | 239 ms                                                       | 231 ms: 1.03x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 23.4 ms: 1.01x faster                                                       |
| regex_effbot   | 3.57 ms                                                      | 3.67 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.89 sec: 1.14x faster                                                      |
| unpickle_pure_python | 210 us                                                       | 193 us: 1.09x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 80.0 ms: 1.08x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 55.3 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 97.6 ms: 1.05x faster                                                       |
| json_dumps           | 10.2 ms                                                      | 10.0 ms: 1.02x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 142 ms: 1.02x faster                                                        |
| unpickle             | 14.8 us                                                      | 15.0 us: 1.01x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 325 us: 1.02x slower                                                        |
| pickle_dict          | 32.5 us                                                      | 33.9 us: 1.04x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 4.97 us: 1.07x slower                                                       |
| json_loads           | 24.4 us                                                      | 26.4 us: 1.08x slower                                                       |
| pickle_list          | 4.43 us                                                      | 4.98 us: 1.12x slower                                                       |
| pickle               | 10.5 us                                                      | 12.3 us: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.88 ms: 1.03x slower                                                       |
| python_startup         | 11.6 ms                                                      | 15.5 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.17x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.0 ms: 1.09x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.29 sec: 2.00x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 619 ms: 1.68x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 636 ms: 1.66x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 329 ms: 1.65x faster                                                        |
| async_tree_none            | 452 ms                                                       | 275 ms: 1.64x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 334 ms: 1.62x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 23.3 us: 1.58x faster                                                       |
| async_tree_none_tg         | 431 ms                                                       | 274 ms: 1.57x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 501 ms: 1.39x faster                                                        |
| deepcopy                   | 368 us                                                       | 268 us: 1.38x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.4 us: 1.26x faster                                                       |
| go                         | 150 ms                                                       | 119 ms: 1.26x faster                                                        |
| generators                 | 37.4 ms                                                      | 30.0 ms: 1.25x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 15.3 ms: 1.23x faster                                                       |
| richards                   | 45.7 ms                                                      | 38.2 ms: 1.20x faster                                                       |
| richards_super             | 51.3 ms                                                      | 44.5 ms: 1.15x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.93 us: 1.15x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.51 us: 1.15x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 1.89 sec: 1.14x faster                                                      |
| logging_simple             | 6.71 us                                                      | 5.90 us: 1.14x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 61.5 ms: 1.12x faster                                                       |
| float                      | 76.6 ms                                                      | 68.4 ms: 1.12x faster                                                       |
| pyflate                    | 439 ms                                                       | 392 ms: 1.12x faster                                                        |
| dulwich_log                | 65.4 ms                                                      | 58.6 ms: 1.12x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.49 sec: 1.11x faster                                                      |
| pprint_safe_repr           | 807 ms                                                       | 731 ms: 1.10x faster                                                        |
| regex_compile              | 144 ms                                                       | 131 ms: 1.10x faster                                                        |
| scimark_fft                | 301 ms                                                       | 275 ms: 1.09x faster                                                        |
| django_template            | 38.2 ms                                                      | 35.0 ms: 1.09x faster                                                       |
| unpickle_pure_python       | 210 us                                                       | 193 us: 1.09x faster                                                        |
| chaos                      | 64.0 ms                                                      | 59.1 ms: 1.08x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 80.0 ms: 1.08x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 22.3 ms: 1.07x faster                                                       |
| scimark_sor                | 109 ms                                                       | 102 ms: 1.07x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                                        |
| meteor_contest             | 128 ms                                                       | 121 ms: 1.06x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 86.3 ms: 1.06x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 75.8 ms: 1.06x faster                                                       |
| xml_etree_process          | 58.4 ms                                                      | 55.3 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 97.6 ms: 1.05x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 93.9 ms: 1.05x faster                                                       |
| raytrace                   | 298 ms                                                       | 284 ms: 1.05x faster                                                        |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                        |
| pycparser                  | 1.23 sec                                                     | 1.19 sec: 1.04x faster                                                      |
| sympy_str                  | 302 ms                                                       | 291 ms: 1.04x faster                                                        |
| regex_dna                  | 239 ms                                                       | 231 ms: 1.03x faster                                                        |
| logging_silent             | 94.4 ns                                                      | 91.9 ns: 1.03x faster                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.0 ms: 1.02x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 371 ms: 1.02x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 142 ms: 1.02x faster                                                        |
| regex_v8                   | 23.6 ms                                                      | 23.4 ms: 1.01x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 22.8 ms: 1.01x faster                                                       |
| deltablue                  | 3.24 ms                                                      | 3.21 ms: 1.01x faster                                                       |
| hexiom                     | 5.96 ms                                                      | 5.92 ms: 1.01x faster                                                       |
| 2to3                       | 285 ms                                                       | 284 ms: 1.00x faster                                                        |
| docutils                   | 2.87 sec                                                     | 2.88 sec: 1.01x slower                                                      |
| unpickle                   | 14.8 us                                                      | 15.0 us: 1.01x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 91.6 ms: 1.02x slower                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.83 us: 1.02x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 325 us: 1.02x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 8.88 ms: 1.03x slower                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.67 ms: 1.03x slower                                                       |
| sympy_expand               | 484 ms                                                       | 498 ms: 1.03x slower                                                        |
| pickle_dict                | 32.5 us                                                      | 33.9 us: 1.04x slower                                                       |
| fannkuch                   | 350 ms                                                       | 368 ms: 1.05x slower                                                        |
| json                       | 5.12 ms                                                      | 5.45 ms: 1.06x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 4.97 us: 1.07x slower                                                       |
| json_loads                 | 24.4 us                                                      | 26.4 us: 1.08x slower                                                       |
| nbody                      | 88.0 ms                                                      | 97.7 ms: 1.11x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 169 us: 1.11x slower                                                        |
| async_generators           | 390 ms                                                       | 438 ms: 1.12x slower                                                        |
| pickle_list                | 4.43 us                                                      | 4.98 us: 1.12x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.74 ms: 1.13x slower                                                       |
| pickle                     | 10.5 us                                                      | 12.3 us: 1.17x slower                                                       |
| coverage                   | 66.7 ms                                                      | 81.4 ms: 1.22x slower                                                       |
| python_startup             | 11.6 ms                                                      | 15.5 ms: 1.33x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.90 ms: 1.82x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 6.73 ms: 1.94x slower                                                       |
| telco                      | 6.96 ms                                                      | 155 ms: 22.24x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 2.51 sec: 527.18x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (5): bench_thread_pool, mako, asyncio_websockets, asyncio_tcp_ssl, unpack_sequence
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.14x