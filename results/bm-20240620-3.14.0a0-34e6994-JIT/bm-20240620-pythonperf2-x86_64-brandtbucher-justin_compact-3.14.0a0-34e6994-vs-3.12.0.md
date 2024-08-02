# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_compact
- machine: linux-x86_64
- commit hash: 34e6994
- commit date: 2024-06-20
- overall geometric mean: 1.00x slower
- HPT reliability: 55.67%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 308 ms: 1.08x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.12 sec: 1.09x slower                                                      |
| tornado_http   | 121 ms                                                       | 123 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 430 ms: 1.26x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 347 ms: 1.24x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 877 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 587 ms: 1.19x faster                                                        |
| async_tree_none            | 452 ms                                                       | 383 ms: 1.18x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 476 ms: 1.14x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 915 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 629 ms: 1.11x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.18x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 82.4 ms: 1.07x faster                                                       |
| pidigits       | 265 ms                                                       | 251 ms: 1.06x faster                                                        |
| float          | 76.6 ms                                                      | 74.4 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.58 ms: 1.00x slower                                                       |
| regex_dna      | 239 ms                                                       | 240 ms: 1.01x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 25.4 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 81.0 ms: 1.06x faster                                                       |
| pickle_dict          | 32.5 us                                                      | 31.3 us: 1.04x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 99.8 ms: 1.03x faster                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.11 sec: 1.02x faster                                                      |
| xml_etree_parse      | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| pickle_list          | 4.43 us                                                      | 4.36 us: 1.01x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 57.9 ms: 1.01x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 316 us: 1.01x faster                                                        |
| unpickle_list        | 4.66 us                                                      | 4.74 us: 1.02x slower                                                       |
| pickle               | 10.5 us                                                      | 10.9 us: 1.03x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.6 ms: 1.04x slower                                                       |
| unpickle             | 14.8 us                                                      | 15.4 us: 1.04x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 218 us: 1.04x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.6 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.50 ms: 1.10x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.9 ms: 1.19x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.15x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.23 ms: 1.08x faster                                                       |
| django_template | 38.2 ms                                                      | 41.2 ms: 1.08x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.00x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 36.8 us                                                      | 29.0 us: 1.27x faster                                                       |
| async_tree_memoization_tg  | 540 ms                                                       | 430 ms: 1.26x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 347 ms: 1.24x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 877 ms: 1.20x faster                                                        |
| deepcopy                   | 368 us                                                       | 307 us: 1.20x faster                                                        |
| comprehensions             | 21.9 us                                                      | 18.3 us: 1.20x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 587 ms: 1.19x faster                                                        |
| async_tree_none            | 452 ms                                                       | 383 ms: 1.18x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.2 ms: 1.17x faster                                                       |
| async_tree_memoization     | 544 ms                                                       | 476 ms: 1.14x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 915 ms: 1.14x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 72.0 ms: 1.12x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 3.03 us: 1.11x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 629 ms: 1.11x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 82.9 ms: 1.11x faster                                                       |
| generators                 | 37.4 ms                                                      | 34.1 ms: 1.10x faster                                                       |
| mako                       | 10.0 ms                                                      | 9.23 ms: 1.08x faster                                                       |
| nbody                      | 88.0 ms                                                      | 82.4 ms: 1.07x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 81.0 ms: 1.06x faster                                                       |
| logging_format             | 7.48 us                                                      | 7.06 us: 1.06x faster                                                       |
| pidigits                   | 265 ms                                                       | 251 ms: 1.06x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.02 ms: 1.05x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.43 us: 1.04x faster                                                       |
| raytrace                   | 298 ms                                                       | 287 ms: 1.04x faster                                                        |
| pickle_dict                | 32.5 us                                                      | 31.3 us: 1.04x faster                                                       |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 22.2 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 99.8 ms: 1.03x faster                                                       |
| float                      | 76.6 ms                                                      | 74.4 ms: 1.03x faster                                                       |
| fannkuch                   | 350 ms                                                       | 341 ms: 1.03x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.11 sec: 1.02x faster                                                      |
| scimark_monte_carlo        | 69.0 ms                                                      | 67.4 ms: 1.02x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 793 ms: 1.02x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.63 sec: 1.02x faster                                                      |
| xml_etree_parse            | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| scimark_fft                | 301 ms                                                       | 296 ms: 1.02x faster                                                        |
| pickle_list                | 4.43 us                                                      | 4.36 us: 1.01x faster                                                       |
| xml_etree_process          | 58.4 ms                                                      | 57.9 ms: 1.01x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 316 us: 1.01x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 376 ms: 1.01x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.58 ms: 1.00x slower                                                       |
| regex_dna                  | 239 ms                                                       | 240 ms: 1.01x slower                                                        |
| mdp                        | 2.57 sec                                                     | 2.59 sec: 1.01x slower                                                      |
| tornado_http               | 121 ms                                                       | 123 ms: 1.01x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 164 ms: 1.01x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 4.74 us: 1.02x slower                                                       |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.02x slower                                                        |
| pyflate                    | 439 ms                                                       | 449 ms: 1.02x slower                                                        |
| richards                   | 45.7 ms                                                      | 46.9 ms: 1.03x slower                                                       |
| dulwich_log                | 65.4 ms                                                      | 67.1 ms: 1.03x slower                                                       |
| bench_thread_pool          | 950 us                                                       | 975 us: 1.03x slower                                                        |
| pickle                     | 10.5 us                                                      | 10.9 us: 1.03x slower                                                       |
| chaos                      | 64.0 ms                                                      | 66.1 ms: 1.03x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.6 ms: 1.04x slower                                                       |
| dask                       | 392 ms                                                       | 407 ms: 1.04x slower                                                        |
| sympy_str                  | 302 ms                                                       | 314 ms: 1.04x slower                                                        |
| unpickle                   | 14.8 us                                                      | 15.4 us: 1.04x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.28 sec: 1.04x slower                                                      |
| unpickle_pure_python       | 210 us                                                       | 218 us: 1.04x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.85 ms: 1.04x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.6 us: 1.05x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.45 ms: 1.05x slower                                                       |
| richards_super             | 51.3 ms                                                      | 54.5 ms: 1.06x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 25.5 ms: 1.07x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 96.2 ms: 1.07x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 25.4 ms: 1.07x slower                                                       |
| json                       | 5.12 ms                                                      | 5.52 ms: 1.08x slower                                                       |
| django_template            | 38.2 ms                                                      | 41.2 ms: 1.08x slower                                                       |
| 2to3                       | 285 ms                                                       | 308 ms: 1.08x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.12 sec: 1.09x slower                                                      |
| python_startup_no_site     | 8.64 ms                                                      | 9.50 ms: 1.10x slower                                                       |
| sympy_expand               | 484 ms                                                       | 533 ms: 1.10x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 104 ns: 1.10x slower                                                        |
| go                         | 150 ms                                                       | 165 ms: 1.10x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 64.4 ms: 1.12x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.66 ms: 1.13x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 131 ms: 1.13x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.75 ms: 1.13x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 115 ms: 1.16x slower                                                        |
| telco                      | 6.96 ms                                                      | 8.22 ms: 1.18x slower                                                       |
| coverage                   | 66.7 ms                                                      | 79.1 ms: 1.19x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.9 ms: 1.19x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.91 ms: 1.20x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 185 us: 1.22x slower                                                        |
| scimark_sor                | 109 ms                                                       | 137 ms: 1.26x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 4.42 ms: 1.27x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (5): bench_mp_pool, async_generators, asyncio_tcp_ssl, sqlite_synth, asyncio_websockets
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240620-3.14.0a0-34e6994-JIT/bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 55.67% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x