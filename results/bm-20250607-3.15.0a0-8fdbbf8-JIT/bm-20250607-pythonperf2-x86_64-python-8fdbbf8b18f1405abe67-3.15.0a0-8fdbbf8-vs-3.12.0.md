# Results vs. 3.12.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-x86_64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.127x slower
- HPT reliability: 99.91%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 320 ms: 1.12x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.14 sec: 1.10x slower                                                      |
| Geometric mean | (ref)                                                        | 1.11x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 694 ms: 1.50x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 705 ms: 1.50x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 364 ms: 1.50x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 367 ms: 1.47x faster                                                        |
| async_tree_none            | 452 ms                                                       | 313 ms: 1.44x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 299 ms: 1.44x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 672 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 675 ms: 1.03x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.35x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 72.3 ms: 1.06x faster                                                       |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                        |
| nbody          | 88.0 ms                                                      | 108 ms: 1.23x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.29 ms: 1.09x faster                                                       |
| regex_compile  | 144 ms                                                       | 156 ms: 1.08x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 26.1 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 2.33 sec: 1.08x slower                                                      |
| pickle_dict          | 32.5 us                                                      | 36.1 us: 1.11x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 115 ms: 1.12x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 238 us: 1.14x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 170 ms: 1.18x slower                                                        |
| json_loads           | 24.4 us                                                      | 29.2 us: 1.20x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 5.58 us: 1.20x slower                                                       |
| unpickle             | 14.8 us                                                      | 17.8 us: 1.20x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 385 us: 1.21x slower                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 105 ms: 1.22x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 71.4 ms: 1.22x slower                                                       |
| pickle_list          | 4.43 us                                                      | 5.90 us: 1.33x slower                                                       |
| pickle               | 10.5 us                                                      | 14.7 us: 1.40x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 14.5 ms: 1.41x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.21x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.43 ms: 1.09x slower                                                       |
| python_startup         | 11.6 ms                                                      | 16.5 ms: 1.42x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.24x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 43.0 ms: 1.13x slower                                                       |
| mako            | 10.0 ms                                                      | 13.4 ms: 1.34x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.23x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.59 sec: 1.62x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 694 ms: 1.50x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 705 ms: 1.50x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 364 ms: 1.50x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 367 ms: 1.47x faster                                                        |
| async_tree_none            | 452 ms                                                       | 313 ms: 1.44x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 299 ms: 1.44x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 31.5 us: 1.17x faster                                                       |
| deepcopy                   | 368 us                                                       | 326 us: 1.13x faster                                                        |
| richards                   | 45.7 ms                                                      | 41.1 ms: 1.11x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.29 ms: 1.09x faster                                                       |
| generators                 | 37.4 ms                                                      | 34.8 ms: 1.07x faster                                                       |
| float                      | 76.6 ms                                                      | 72.3 ms: 1.06x faster                                                       |
| richards_super             | 51.3 ms                                                      | 48.6 ms: 1.06x faster                                                       |
| go                         | 150 ms                                                       | 143 ms: 1.05x faster                                                        |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 672 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 675 ms: 1.03x faster                                                        |
| comprehensions             | 21.9 us                                                      | 21.3 us: 1.03x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 63.7 ms: 1.03x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 375 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.59 sec: 1.00x slower                                                      |
| sympy_integrate            | 23.9 ms                                                      | 24.4 ms: 1.02x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.34 ms: 1.03x slower                                                       |
| coroutines                 | 23.0 ms                                                      | 24.0 ms: 1.04x slower                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.53 us: 1.05x slower                                                       |
| pathlib                    | 18.9 ms                                                      | 20.0 ms: 1.06x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 172 ms: 1.06x slower                                                        |
| pyflate                    | 439 ms                                                       | 466 ms: 1.06x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.33 sec: 1.08x slower                                                      |
| tomli_loads                | 2.16 sec                                                     | 2.33 sec: 1.08x slower                                                      |
| regex_compile              | 144 ms                                                       | 156 ms: 1.08x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.43 ms: 1.09x slower                                                       |
| docutils                   | 2.87 sec                                                     | 3.14 sec: 1.10x slower                                                      |
| regex_v8                   | 23.6 ms                                                      | 26.1 ms: 1.10x slower                                                       |
| pickle_dict                | 32.5 us                                                      | 36.1 us: 1.11x slower                                                       |
| bench_thread_pool          | 950 us                                                       | 1.06 ms: 1.11x slower                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 77.0 ms: 1.12x slower                                                       |
| sympy_str                  | 302 ms                                                       | 338 ms: 1.12x slower                                                        |
| chaos                      | 64.0 ms                                                      | 71.7 ms: 1.12x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 115 ms: 1.12x slower                                                        |
| 2to3                       | 285 ms                                                       | 320 ms: 1.12x slower                                                        |
| meteor_contest             | 128 ms                                                       | 144 ms: 1.12x slower                                                        |
| django_template            | 38.2 ms                                                      | 43.0 ms: 1.13x slower                                                       |
| raytrace                   | 298 ms                                                       | 337 ms: 1.13x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 238 us: 1.14x slower                                                        |
| logging_format             | 7.48 us                                                      | 8.51 us: 1.14x slower                                                       |
| logging_simple             | 6.71 us                                                      | 7.69 us: 1.15x slower                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 93.4 ms: 1.16x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 7.03 ms: 1.18x slower                                                       |
| json                       | 5.12 ms                                                      | 6.04 ms: 1.18x slower                                                       |
| xml_etree_parse            | 144 ms                                                       | 170 ms: 1.18x slower                                                        |
| scimark_sor                | 109 ms                                                       | 129 ms: 1.18x slower                                                        |
| json_loads                 | 24.4 us                                                      | 29.2 us: 1.20x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 5.58 us: 1.20x slower                                                       |
| unpickle                   | 14.8 us                                                      | 17.8 us: 1.20x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 119 ms: 1.20x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 3.35 us: 1.21x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 385 us: 1.21x slower                                                        |
| sympy_expand               | 484 ms                                                       | 588 ms: 1.22x slower                                                        |
| async_generators           | 390 ms                                                       | 475 ms: 1.22x slower                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 105 ms: 1.22x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 71.4 ms: 1.22x slower                                                       |
| nbody                      | 88.0 ms                                                      | 108 ms: 1.23x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 111 ms: 1.23x slower                                                        |
| unpack_sequence            | 53.2 ns                                                      | 67.1 ns: 1.26x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 2.10 sec: 1.27x slower                                                      |
| pprint_safe_repr           | 807 ms                                                       | 1.04 sec: 1.29x slower                                                      |
| scimark_fft                | 301 ms                                                       | 392 ms: 1.30x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 122 ms: 1.33x slower                                                        |
| pickle_list                | 4.43 us                                                      | 5.90 us: 1.33x slower                                                       |
| mako                       | 10.0 ms                                                      | 13.4 ms: 1.34x slower                                                       |
| fannkuch                   | 350 ms                                                       | 483 ms: 1.38x slower                                                        |
| telco                      | 6.96 ms                                                      | 9.72 ms: 1.40x slower                                                       |
| pickle                     | 10.5 us                                                      | 14.7 us: 1.40x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 14.5 ms: 1.41x slower                                                       |
| python_startup             | 11.6 ms                                                      | 16.5 ms: 1.42x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 216 us: 1.43x slower                                                        |
| coverage                   | 66.7 ms                                                      | 101 ms: 1.51x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 6.34 ms: 1.51x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 5.59 ms: 1.61x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.92 ms: 1.83x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 677 ns: 7.18x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 2.14 sec: 449.28x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.20x slower                                                                |

Benchmark hidden because not significant (2): regex_dna, asyncio_websockets
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.127x slower

# HPT report

- Reliability score: 99.91% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.12x