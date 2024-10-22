# Results vs. 3.12.0

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-x86_64
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 272 ms: 1.01x faster                                                        |
| docutils       | 2.77 sec                                               | 2.87 sec: 1.04x slower                                                      |
| tornado_http   | 103 ms                                                 | 93.0 ms: 1.10x faster                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 372 ms: 1.54x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 295 ms: 1.53x faster                                                        |
| async_tree_none            | 472 ms                                                 | 321 ms: 1.47x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 403 ms: 1.43x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 841 ms: 1.41x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 840 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 539 ms: 1.35x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.42x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.2 ms: 1.22x faster                                                       |
| float          | 84.7 ms                                                | 69.3 ms: 1.22x faster                                                       |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.15x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 135 ms: 1.10x faster                                                        |
| regex_effbot   | 3.61 ms                                                | 3.73 ms: 1.03x slower                                                       |
| regex_v8       | 23.1 ms                                                | 24.4 ms: 1.05x slower                                                       |
| regex_dna      | 212 ms                                                 | 229 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 80.6 ms: 1.11x faster                                                       |
| pickle_pure_python   | 324 us                                                 | 297 us: 1.09x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 57.0 ms: 1.08x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.08x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 99.1 ms: 1.08x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                        |
| json_loads           | 28.5 us                                                | 27.9 us: 1.02x faster                                                       |
| json_dumps           | 10.4 ms                                                | 10.4 ms: 1.00x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                       |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.86 ms: 1.21x faster                                                       |
| django_template | 34.6 ms                                                | 34.9 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 372 ms: 1.54x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 295 ms: 1.53x faster                                                        |
| async_tree_none            | 472 ms                                                 | 321 ms: 1.47x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 403 ms: 1.43x faster                                                        |
| deepcopy_memo              | 40.7 us                                                | 28.9 us: 1.41x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 841 ms: 1.41x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 840 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 539 ms: 1.35x faster                                                        |
| deepcopy                   | 371 us                                                 | 278 us: 1.34x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 60.9 ms: 1.23x faster                                                       |
| nbody                      | 97.0 ms                                                | 79.2 ms: 1.22x faster                                                       |
| float                      | 84.7 ms                                                | 69.3 ms: 1.22x faster                                                       |
| crypto_pyaes               | 81.9 ms                                                | 67.5 ms: 1.21x faster                                                       |
| scimark_fft                | 382 ms                                                 | 315 ms: 1.21x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                      |
| mako                       | 11.9 ms                                                | 9.86 ms: 1.21x faster                                                       |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.21x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.78 us: 1.20x faster                                                       |
| logging_format             | 7.23 us                                                | 6.07 us: 1.19x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.49 us: 1.18x faster                                                       |
| raytrace                   | 312 ms                                                 | 268 ms: 1.17x faster                                                        |
| chaos                      | 67.0 ms                                                | 58.1 ms: 1.15x faster                                                       |
| fannkuch                   | 417 ms                                                 | 363 ms: 1.15x faster                                                        |
| pyflate                    | 482 ms                                                 | 426 ms: 1.13x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.50 ms: 1.12x faster                                                       |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                        |
| richards                   | 45.8 ms                                                | 41.3 ms: 1.11x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 80.6 ms: 1.11x faster                                                       |
| tornado_http               | 103 ms                                                 | 93.0 ms: 1.10x faster                                                       |
| regex_compile              | 148 ms                                                 | 135 ms: 1.10x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 297 us: 1.09x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 57.0 ms: 1.08x faster                                                       |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.08x faster                                                        |
| richards_super             | 51.5 ms                                                | 47.6 ms: 1.08x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 720 ms: 1.08x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 99.1 ms: 1.08x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                                      |
| gc_traversal               | 3.79 ms                                                | 3.55 ms: 1.07x faster                                                       |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.07x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.54 ms: 1.05x faster                                                       |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.05x faster                                                       |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                      |
| async_generators           | 463 ms                                                 | 449 ms: 1.03x faster                                                        |
| generators                 | 31.2 ms                                                | 30.4 ms: 1.03x faster                                                       |
| json_loads                 | 28.5 us                                                | 27.9 us: 1.02x faster                                                       |
| dask                       | 372 ms                                                 | 364 ms: 1.02x faster                                                        |
| json                       | 5.26 ms                                                | 5.15 ms: 1.02x faster                                                       |
| dulwich_log                | 68.5 ms                                                | 67.2 ms: 1.02x faster                                                       |
| sympy_str                  | 300 ms                                                 | 294 ms: 1.02x faster                                                        |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 167 ms: 1.01x faster                                                        |
| bench_thread_pool          | 842 us                                                 | 834 us: 1.01x faster                                                        |
| 2to3                       | 274 ms                                                 | 272 ms: 1.01x faster                                                        |
| json_dumps                 | 10.4 ms                                                | 10.4 ms: 1.00x faster                                                       |
| scimark_sor                | 129 ms                                                 | 130 ms: 1.01x slower                                                        |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 55.3 ms: 1.01x slower                                                       |
| django_template            | 34.6 ms                                                | 34.9 ms: 1.01x slower                                                       |
| nqueens                    | 83.3 ms                                                | 84.3 ms: 1.01x slower                                                       |
| coroutines                 | 23.2 ms                                                | 23.5 ms: 1.01x slower                                                       |
| logging_silent             | 104 ns                                                 | 106 ns: 1.02x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                       |
| asyncio_tcp                | 491 ms                                                 | 502 ms: 1.02x slower                                                        |
| hexiom                     | 6.41 ms                                                | 6.58 ms: 1.03x slower                                                       |
| go                         | 139 ms                                                 | 144 ms: 1.03x slower                                                        |
| sympy_integrate            | 21.4 ms                                                | 22.1 ms: 1.03x slower                                                       |
| regex_effbot               | 3.61 ms                                                | 3.73 ms: 1.03x slower                                                       |
| docutils                   | 2.77 sec                                               | 2.87 sec: 1.04x slower                                                      |
| sympy_expand               | 478 ms                                                 | 497 ms: 1.04x slower                                                        |
| scimark_lu                 | 118 ms                                                 | 123 ms: 1.04x slower                                                        |
| mdp                        | 2.63 sec                                               | 2.74 sec: 1.04x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 24.4 ms: 1.05x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                                        |
| regex_dna                  | 212 ms                                                 | 229 ms: 1.08x slower                                                        |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                       |
| telco                      | 7.10 ms                                                | 8.04 ms: 1.13x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.18x slower                                                       |
| coverage                   | 72.7 ms                                                | 93.4 ms: 1.29x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                |

Benchmark hidden because not significant (2): bench_mp_pool, sqlglot_normalize
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240713-3.14.0a0-bbb07e8-JIT/bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.04x