# Results vs. 3.12.0

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: linux-x86_64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.040x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 278 ms: 1.03x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.84 sec: 1.01x faster                                                      |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 618 ms: 1.69x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 634 ms: 1.66x faster                                                        |
| async_tree_none            | 452 ms                                                       | 273 ms: 1.66x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 328 ms: 1.66x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 330 ms: 1.64x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 270 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 501 ms: 1.39x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 508 ms: 1.37x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.58x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 68.9 ms: 1.11x faster                                                       |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| nbody          | 88.0 ms                                                      | 89.6 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 131 ms: 1.10x faster                                                        |
| regex_dna      | 239 ms                                                       | 220 ms: 1.09x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.32 ms: 1.08x faster                                                       |
| regex_v8       | 23.6 ms                                                      | 24.3 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.99 sec: 1.09x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                       | 98.8 ms: 1.04x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 82.8 ms: 1.04x faster                                                       |
| unpickle_pure_python | 210 us                                                       | 205 us: 1.02x faster                                                        |
| json_dumps           | 10.2 ms                                                      | 10.1 ms: 1.01x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 58.0 ms: 1.01x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 143 ms: 1.01x faster                                                        |
| json_loads           | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 329 us: 1.03x slower                                                        |
| pickle_dict          | 32.5 us                                                      | 35.1 us: 1.08x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 5.20 us: 1.12x slower                                                       |
| pickle_list          | 4.43 us                                                      | 5.04 us: 1.14x slower                                                       |
| pickle               | 10.5 us                                                      | 12.7 us: 1.21x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.81 ms: 1.02x slower                                                       |
| python_startup         | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.6 ms: 1.07x faster                                                       |
| mako            | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.00x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.27 sec: 2.02x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 618 ms: 1.69x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 634 ms: 1.66x faster                                                        |
| async_tree_none            | 452 ms                                                       | 273 ms: 1.66x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 328 ms: 1.66x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 330 ms: 1.64x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 270 ms: 1.59x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 25.3 us: 1.45x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 501 ms: 1.39x faster                                                        |
| deepcopy                   | 368 us                                                       | 267 us: 1.38x faster                                                        |
| comprehensions             | 21.9 us                                                      | 15.9 us: 1.38x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 508 ms: 1.37x faster                                                        |
| go                         | 150 ms                                                       | 117 ms: 1.28x faster                                                        |
| generators                 | 37.4 ms                                                      | 30.2 ms: 1.24x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 15.4 ms: 1.22x faster                                                       |
| unpack_sequence            | 53.2 ns                                                      | 45.5 ns: 1.17x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.51 us: 1.15x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.96 us: 1.14x faster                                                       |
| logging_simple             | 6.71 us                                                      | 5.89 us: 1.14x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 61.0 ms: 1.13x faster                                                       |
| float                      | 76.6 ms                                                      | 68.9 ms: 1.11x faster                                                       |
| chaos                      | 64.0 ms                                                      | 57.8 ms: 1.11x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 59.3 ms: 1.10x faster                                                       |
| regex_compile              | 144 ms                                                       | 131 ms: 1.10x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 21.8 ms: 1.10x faster                                                       |
| scimark_fft                | 301 ms                                                       | 276 ms: 1.09x faster                                                        |
| regex_dna                  | 239 ms                                                       | 220 ms: 1.09x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 1.99 sec: 1.09x faster                                                      |
| sympy_sum                  | 162 ms                                                       | 150 ms: 1.08x faster                                                        |
| pyflate                    | 439 ms                                                       | 405 ms: 1.08x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.32 ms: 1.08x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 85.4 ms: 1.07x faster                                                       |
| django_template            | 38.2 ms                                                      | 35.6 ms: 1.07x faster                                                       |
| meteor_contest             | 128 ms                                                       | 120 ms: 1.07x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 75.5 ms: 1.06x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.56 sec: 1.06x faster                                                      |
| sympy_str                  | 302 ms                                                       | 286 ms: 1.06x faster                                                        |
| scimark_sor                | 109 ms                                                       | 103 ms: 1.05x faster                                                        |
| raytrace                   | 298 ms                                                       | 283 ms: 1.05x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 769 ms: 1.05x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 98.8 ms: 1.04x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 82.8 ms: 1.04x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 22.1 ms: 1.04x faster                                                       |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                        |
| hexiom                     | 5.96 ms                                                      | 5.77 ms: 1.03x faster                                                       |
| richards                   | 45.7 ms                                                      | 44.4 ms: 1.03x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 96.1 ms: 1.03x faster                                                       |
| 2to3                       | 285 ms                                                       | 278 ms: 1.03x faster                                                        |
| richards_super             | 51.3 ms                                                      | 50.2 ms: 1.02x faster                                                       |
| unpickle_pure_python       | 210 us                                                       | 205 us: 1.02x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 370 ms: 1.02x faster                                                        |
| deltablue                  | 3.24 ms                                                      | 3.17 ms: 1.02x faster                                                       |
| pycparser                  | 1.23 sec                                                     | 1.21 sec: 1.02x faster                                                      |
| json_dumps                 | 10.2 ms                                                      | 10.1 ms: 1.01x faster                                                       |
| docutils                   | 2.87 sec                                                     | 2.84 sec: 1.01x faster                                                      |
| xml_etree_process          | 58.4 ms                                                      | 58.0 ms: 1.01x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 143 ms: 1.01x faster                                                        |
| logging_silent             | 94.4 ns                                                      | 94.1 ns: 1.00x faster                                                       |
| sympy_expand               | 484 ms                                                       | 486 ms: 1.00x slower                                                        |
| nbody                      | 88.0 ms                                                      | 89.6 ms: 1.02x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.81 ms: 1.02x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 92.1 ms: 1.02x slower                                                       |
| fannkuch                   | 350 ms                                                       | 359 ms: 1.03x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.85 us: 1.03x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 24.3 ms: 1.03x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 329 us: 1.03x slower                                                        |
| json                       | 5.12 ms                                                      | 5.34 ms: 1.04x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.47 ms: 1.06x slower                                                       |
| mako                       | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                       |
| pickle_dict                | 32.5 us                                                      | 35.1 us: 1.08x slower                                                       |
| async_generators           | 390 ms                                                       | 426 ms: 1.09x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 166 us: 1.10x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 5.20 us: 1.12x slower                                                       |
| pickle_list                | 4.43 us                                                      | 5.04 us: 1.14x slower                                                       |
| pickle                     | 10.5 us                                                      | 12.7 us: 1.21x slower                                                       |
| coverage                   | 66.7 ms                                                      | 87.4 ms: 1.31x slower                                                       |
| python_startup             | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.87 ms: 1.81x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 6.49 ms: 1.87x slower                                                       |
| telco                      | 6.96 ms                                                      | 154 ms: 22.18x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 1.98 sec: 415.24x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (4): bench_thread_pool, asyncio_tcp_ssl, unpickle, asyncio_websockets
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20251012-3.15.0a0-d6dd64a/bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.13x