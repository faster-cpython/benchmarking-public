# Results vs. 3.12.0

- fork: python
- ref: 800d37feca2e0ea33439
- machine: linux-x86_64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.035x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 281 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 612 ms: 1.70x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 619 ms: 1.70x faster                                                        |
| async_tree_none            | 452 ms                                                       | 267 ms: 1.69x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 323 ms: 1.68x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 327 ms: 1.65x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 268 ms: 1.61x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 494 ms: 1.41x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 503 ms: 1.39x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.60x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 71.2 ms: 1.08x faster                                                       |
| pidigits       | 265 ms                                                       | 256 ms: 1.04x faster                                                        |
| nbody          | 88.0 ms                                                      | 93.0 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 131 ms: 1.10x faster                                                        |
| regex_dna      | 239 ms                                                       | 227 ms: 1.05x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.50 ms: 1.02x faster                                                       |
| regex_v8       | 23.6 ms                                                      | 23.6 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 2.00 sec: 1.08x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                       | 97.5 ms: 1.05x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 81.9 ms: 1.05x faster                                                       |
| unpickle_pure_python | 210 us                                                       | 205 us: 1.02x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 57.2 ms: 1.02x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 325 us: 1.02x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 5.02 us: 1.08x slower                                                       |
| json_loads           | 24.4 us                                                      | 26.3 us: 1.08x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 11.1 ms: 1.08x slower                                                       |
| pickle_dict          | 32.5 us                                                      | 36.5 us: 1.12x slower                                                       |
| pickle_list          | 4.43 us                                                      | 4.99 us: 1.13x slower                                                       |
| pickle               | 10.5 us                                                      | 12.5 us: 1.19x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.68 ms: 1.00x slower                                                       |
| python_startup         | 11.6 ms                                                      | 15.2 ms: 1.31x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.15x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 36.1 ms: 1.06x faster                                                       |
| mako            | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.27 sec: 2.02x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 612 ms: 1.70x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 619 ms: 1.70x faster                                                        |
| async_tree_none            | 452 ms                                                       | 267 ms: 1.69x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 323 ms: 1.68x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 327 ms: 1.65x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 268 ms: 1.61x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 494 ms: 1.41x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 503 ms: 1.39x faster                                                        |
| deepcopy                   | 368 us                                                       | 268 us: 1.38x faster                                                        |
| comprehensions             | 21.9 us                                                      | 16.1 us: 1.36x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 27.2 us: 1.35x faster                                                       |
| go                         | 150 ms                                                       | 116 ms: 1.29x faster                                                        |
| generators                 | 37.4 ms                                                      | 29.4 ms: 1.27x faster                                                       |
| unpack_sequence            | 53.2 ns                                                      | 42.3 ns: 1.26x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.91 us: 1.16x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.62 us: 1.13x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 61.2 ms: 1.13x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 58.3 ms: 1.12x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 16.9 ms: 1.12x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.02 us: 1.11x faster                                                       |
| regex_compile              | 144 ms                                                       | 131 ms: 1.10x faster                                                        |
| chaos                      | 64.0 ms                                                      | 58.4 ms: 1.10x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 21.9 ms: 1.09x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 149 ms: 1.09x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.52 sec: 1.09x faster                                                      |
| tomli_loads                | 2.16 sec                                                     | 2.00 sec: 1.08x faster                                                      |
| float                      | 76.6 ms                                                      | 71.2 ms: 1.08x faster                                                       |
| raytrace                   | 298 ms                                                       | 278 ms: 1.07x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 754 ms: 1.07x faster                                                        |
| sympy_str                  | 302 ms                                                       | 283 ms: 1.07x faster                                                        |
| pyflate                    | 439 ms                                                       | 412 ms: 1.07x faster                                                        |
| meteor_contest             | 128 ms                                                       | 120 ms: 1.07x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 86.3 ms: 1.06x faster                                                       |
| django_template            | 38.2 ms                                                      | 36.1 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 97.5 ms: 1.05x faster                                                       |
| scimark_sor                | 109 ms                                                       | 103 ms: 1.05x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 76.2 ms: 1.05x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 81.9 ms: 1.05x faster                                                       |
| regex_dna                  | 239 ms                                                       | 227 ms: 1.05x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 22.1 ms: 1.04x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 95.2 ms: 1.04x faster                                                       |
| pidigits                   | 265 ms                                                       | 256 ms: 1.04x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 368 ms: 1.03x faster                                                        |
| unpickle_pure_python       | 210 us                                                       | 205 us: 1.02x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.50 ms: 1.02x faster                                                       |
| xml_etree_process          | 58.4 ms                                                      | 57.2 ms: 1.02x faster                                                       |
| deltablue                  | 3.24 ms                                                      | 3.17 ms: 1.02x faster                                                       |
| asyncio_websockets         | 387 ms                                                       | 380 ms: 1.02x faster                                                        |
| hexiom                     | 5.96 ms                                                      | 5.86 ms: 1.02x faster                                                       |
| 2to3                       | 285 ms                                                       | 281 ms: 1.02x faster                                                        |
| richards                   | 45.7 ms                                                      | 45.1 ms: 1.01x faster                                                       |
| richards_super             | 51.3 ms                                                      | 50.9 ms: 1.01x faster                                                       |
| sympy_expand               | 484 ms                                                       | 481 ms: 1.01x faster                                                        |
| logging_silent             | 94.4 ns                                                      | 93.9 ns: 1.00x faster                                                       |
| regex_v8                   | 23.6 ms                                                      | 23.6 ms: 1.00x faster                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.68 ms: 1.00x slower                                                       |
| scimark_fft                | 301 ms                                                       | 303 ms: 1.01x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 325 us: 1.02x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 91.8 ms: 1.02x slower                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.84 us: 1.02x slower                                                       |
| fannkuch                   | 350 ms                                                       | 360 ms: 1.03x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                                      |
| json                       | 5.12 ms                                                      | 5.39 ms: 1.05x slower                                                       |
| nbody                      | 88.0 ms                                                      | 93.0 ms: 1.06x slower                                                       |
| mako                       | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 5.02 us: 1.08x slower                                                       |
| json_loads                 | 24.4 us                                                      | 26.3 us: 1.08x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 11.1 ms: 1.08x slower                                                       |
| async_generators           | 390 ms                                                       | 424 ms: 1.09x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 166 us: 1.10x slower                                                        |
| pickle_dict                | 32.5 us                                                      | 36.5 us: 1.12x slower                                                       |
| pickle_list                | 4.43 us                                                      | 4.99 us: 1.13x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.75 ms: 1.13x slower                                                       |
| coverage                   | 66.7 ms                                                      | 77.7 ms: 1.17x slower                                                       |
| pickle                     | 10.5 us                                                      | 12.5 us: 1.19x slower                                                       |
| python_startup             | 11.6 ms                                                      | 15.2 ms: 1.31x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 6.25 ms: 1.80x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.90 ms: 1.82x slower                                                       |
| telco                      | 6.96 ms                                                      | 160 ms: 22.92x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 2.38 sec: 500.11x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (4): asyncio_tcp_ssl, unpickle, docutils, bench_thread_pool
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250719-3.15.0a0-800d37f/bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.035x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.13x