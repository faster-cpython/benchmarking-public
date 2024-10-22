# Results vs. 3.12.0

- fork: savannahostrowski
- ref: jit_inv_cold_10k
- machine: linux-x86_64
- commit hash: 4ab420c
- commit date: 2024-09-23
- overall geometric mean: 1.05x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 285 ms: 1.04x slower                                                         |
| docutils       | 2.77 sec                                               | 2.89 sec: 1.04x slower                                                       |
| tornado_http   | 103 ms                                                 | 96.0 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.50x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                                         |
| async_tree_none            | 472 ms                                                 | 320 ms: 1.47x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 399 ms: 1.45x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 878 ms: 1.35x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 551 ms: 1.32x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 886 ms: 1.31x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.28x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.4 ms: 1.19x faster                                                        |
| nbody          | 97.0 ms                                                | 82.1 ms: 1.18x faster                                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 139 ms: 1.06x faster                                                         |
| regex_effbot   | 3.61 ms                                                | 3.78 ms: 1.05x slower                                                        |
| regex_dna      | 212 ms                                                 | 224 ms: 1.06x slower                                                         |
| regex_v8       | 23.1 ms                                                | 26.2 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 80.7 ms: 1.11x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                                         |
| xml_etree_iterparse  | 107 ms                                                 | 99.7 ms: 1.07x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 303 us: 1.07x faster                                                         |
| unpickle             | 15.9 us                                                | 15.0 us: 1.06x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                                         |
| json_loads           | 28.5 us                                                | 27.4 us: 1.04x faster                                                        |
| pickle_dict          | 35.5 us                                                | 34.6 us: 1.03x faster                                                        |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                        |
| unpickle_list        | 5.29 us                                                | 5.32 us: 1.01x slower                                                        |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                                        |
| pickle_list          | 5.08 us                                                | 5.18 us: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                        |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.94 ms: 1.20x faster                                                        |
| django_template | 34.6 ms                                                | 36.9 ms: 1.07x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 27.0 us: 1.51x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.50x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                                         |
| async_tree_none            | 472 ms                                                 | 320 ms: 1.47x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 399 ms: 1.45x faster                                                         |
| deepcopy                   | 371 us                                                 | 269 us: 1.38x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 878 ms: 1.35x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 551 ms: 1.32x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 886 ms: 1.31x faster                                                         |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.28x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.25x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                       |
| crypto_pyaes               | 81.9 ms                                                | 67.9 ms: 1.21x faster                                                        |
| scimark_fft                | 382 ms                                                 | 317 ms: 1.20x faster                                                         |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                        |
| mako                       | 11.9 ms                                                | 9.94 ms: 1.20x faster                                                        |
| float                      | 84.7 ms                                                | 71.4 ms: 1.19x faster                                                        |
| nbody                      | 97.0 ms                                                | 82.1 ms: 1.18x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 63.7 ms: 1.18x faster                                                        |
| logging_format             | 7.23 us                                                | 6.18 us: 1.17x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.40 ms: 1.15x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.68 us: 1.14x faster                                                        |
| chaos                      | 67.0 ms                                                | 59.3 ms: 1.13x faster                                                        |
| fannkuch                   | 417 ms                                                 | 376 ms: 1.11x faster                                                         |
| raytrace                   | 312 ms                                                 | 281 ms: 1.11x faster                                                         |
| xml_etree_generate         | 89.2 ms                                                | 80.7 ms: 1.11x faster                                                        |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                         |
| xml_etree_process          | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                        |
| richards_super             | 51.5 ms                                                | 47.0 ms: 1.10x faster                                                        |
| richards                   | 45.8 ms                                                | 42.7 ms: 1.07x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 99.7 ms: 1.07x faster                                                        |
| tornado_http               | 103 ms                                                 | 96.0 ms: 1.07x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 303 us: 1.07x faster                                                         |
| regex_compile              | 148 ms                                                 | 139 ms: 1.06x faster                                                         |
| unpickle                   | 15.9 us                                                | 15.0 us: 1.06x faster                                                        |
| pyflate                    | 482 ms                                                 | 456 ms: 1.06x faster                                                         |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                         |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                                         |
| json_loads                 | 28.5 us                                                | 27.4 us: 1.04x faster                                                        |
| json                       | 5.26 ms                                                | 5.08 ms: 1.04x faster                                                        |
| mdp                        | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                       |
| go                         | 139 ms                                                 | 136 ms: 1.03x faster                                                         |
| pickle_dict                | 35.5 us                                                | 34.6 us: 1.03x faster                                                        |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                                        |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.02x faster                                                         |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                        |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.02x faster                                                         |
| logging_silent             | 104 ns                                                 | 102 ns: 1.02x faster                                                         |
| pprint_safe_repr           | 776 ms                                                 | 760 ms: 1.02x faster                                                         |
| deltablue                  | 3.72 ms                                                | 3.65 ms: 1.02x faster                                                        |
| async_generators           | 463 ms                                                 | 456 ms: 1.02x faster                                                         |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| dulwich_log                | 68.5 ms                                                | 68.1 ms: 1.01x faster                                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.35 ms: 1.01x faster                                                        |
| gc_traversal               | 3.79 ms                                                | 3.80 ms: 1.00x slower                                                        |
| unpickle_list              | 5.29 us                                                | 5.32 us: 1.01x slower                                                        |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                         |
| asyncio_tcp                | 491 ms                                                 | 495 ms: 1.01x slower                                                         |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                       |
| coroutines                 | 23.2 ms                                                | 23.5 ms: 1.01x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                        |
| sympy_sum                  | 169 ms                                                 | 172 ms: 1.02x slower                                                         |
| pickle_list                | 5.08 us                                                | 5.18 us: 1.02x slower                                                        |
| sympy_str                  | 300 ms                                                 | 308 ms: 1.03x slower                                                         |
| 2to3                       | 274 ms                                                 | 285 ms: 1.04x slower                                                         |
| pycparser                  | 1.18 sec                                               | 1.23 sec: 1.04x slower                                                       |
| docutils                   | 2.77 sec                                               | 2.89 sec: 1.04x slower                                                       |
| regex_effbot               | 3.61 ms                                                | 3.78 ms: 1.05x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.05x slower                                                         |
| nqueens                    | 83.3 ms                                                | 87.7 ms: 1.05x slower                                                        |
| sympy_expand               | 478 ms                                                 | 503 ms: 1.05x slower                                                         |
| regex_dna                  | 212 ms                                                 | 224 ms: 1.06x slower                                                         |
| sqlglot_normalize          | 110 ms                                                 | 117 ms: 1.06x slower                                                         |
| django_template            | 34.6 ms                                                | 36.9 ms: 1.07x slower                                                        |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                        |
| telco                      | 7.10 ms                                                | 8.03 ms: 1.13x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 26.2 ms: 1.13x slower                                                        |
| generators                 | 31.2 ms                                                | 35.6 ms: 1.14x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 1.72 ms: 1.17x slower                                                        |
| sqlglot_optimize           | 54.8 ms                                                | 64.3 ms: 1.17x slower                                                        |
| coverage                   | 72.7 ms                                                | 86.9 ms: 1.20x slower                                                        |
| hexiom                     | 6.41 ms                                                | 7.80 ms: 1.22x slower                                                        |
| sympy_integrate            | 21.4 ms                                                | 26.7 ms: 1.25x slower                                                        |
| unpack_sequence            | 54.0 ns                                                | 112 ns: 2.07x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (4): pprint_pformat, bench_thread_pool, bench_mp_pool, sqlglot_transpile
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240923-3.14.0a0-4ab420c-JIT/bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.01x