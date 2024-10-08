# Results vs. 3.12.0

- fork: savannahostrowski
- ref: jit_inv_cold_10k
- machine: linux-x86_64
- commit hash: 14c70a7
- commit date: 2024-09-19
- overall geometric mean: 1.06x faster
- HPT reliability: 99.89%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 285 ms: 1.04x slower                                                         |
| docutils       | 2.77 sec                                               | 2.88 sec: 1.04x slower                                                       |
| tornado_http   | 103 ms                                                 | 95.5 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.50x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 387 ms: 1.48x faster                                                         |
| async_tree_none            | 472 ms                                                 | 321 ms: 1.47x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 395 ms: 1.46x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 874 ms: 1.35x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 546 ms: 1.33x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 883 ms: 1.31x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 558 ms: 1.30x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.40x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.7 ms: 1.22x faster                                                        |
| float          | 84.7 ms                                                | 71.5 ms: 1.18x faster                                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 139 ms: 1.07x faster                                                         |
| regex_effbot   | 3.61 ms                                                | 3.65 ms: 1.01x slower                                                        |
| regex_dna      | 212 ms                                                 | 215 ms: 1.02x slower                                                         |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 79.8 ms: 1.12x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 55.5 ms: 1.11x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 145 ms: 1.10x faster                                                         |
| unpickle             | 15.9 us                                                | 14.7 us: 1.08x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 99.4 ms: 1.07x faster                                                        |
| pickle_dict          | 35.5 us                                                | 33.4 us: 1.06x faster                                                        |
| json_loads           | 28.5 us                                                | 26.8 us: 1.06x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 306 us: 1.06x faster                                                         |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                                         |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                        |
| pickle_list          | 5.08 us                                                | 5.00 us: 1.02x faster                                                        |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                        |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.0 ms: 1.19x faster                                                        |
| django_template | 34.6 ms                                                | 35.4 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 27.1 us: 1.50x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.50x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 387 ms: 1.48x faster                                                         |
| async_tree_none            | 472 ms                                                 | 321 ms: 1.47x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 395 ms: 1.46x faster                                                         |
| deepcopy                   | 371 us                                                 | 265 us: 1.40x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 874 ms: 1.35x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 546 ms: 1.33x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 883 ms: 1.31x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 558 ms: 1.30x faster                                                         |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.63 us: 1.27x faster                                                        |
| scimark_fft                | 382 ms                                                 | 309 ms: 1.23x faster                                                         |
| nbody                      | 97.0 ms                                                | 79.7 ms: 1.22x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 61.9 ms: 1.21x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 68.2 ms: 1.20x faster                                                        |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                       |
| mako                       | 11.9 ms                                                | 10.0 ms: 1.19x faster                                                        |
| float                      | 84.7 ms                                                | 71.5 ms: 1.18x faster                                                        |
| logging_format             | 7.23 us                                                | 6.28 us: 1.15x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.67 us: 1.14x faster                                                        |
| chaos                      | 67.0 ms                                                | 59.6 ms: 1.12x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 79.8 ms: 1.12x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 55.5 ms: 1.11x faster                                                        |
| raytrace                   | 312 ms                                                 | 281 ms: 1.11x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.56 ms: 1.11x faster                                                        |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                         |
| xml_etree_parse            | 159 ms                                                 | 145 ms: 1.10x faster                                                         |
| richards_super             | 51.5 ms                                                | 47.0 ms: 1.10x faster                                                        |
| unpickle                   | 15.9 us                                                | 14.7 us: 1.08x faster                                                        |
| fannkuch                   | 417 ms                                                 | 386 ms: 1.08x faster                                                         |
| tornado_http               | 103 ms                                                 | 95.5 ms: 1.07x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 99.4 ms: 1.07x faster                                                        |
| regex_compile              | 148 ms                                                 | 139 ms: 1.07x faster                                                         |
| pickle_dict                | 35.5 us                                                | 33.4 us: 1.06x faster                                                        |
| json_loads                 | 28.5 us                                                | 26.8 us: 1.06x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 306 us: 1.06x faster                                                         |
| pyflate                    | 482 ms                                                 | 456 ms: 1.06x faster                                                         |
| richards                   | 45.8 ms                                                | 43.5 ms: 1.05x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                                         |
| json                       | 5.26 ms                                                | 5.02 ms: 1.05x faster                                                        |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                         |
| pprint_safe_repr           | 776 ms                                                 | 742 ms: 1.04x faster                                                         |
| sqlite_synth               | 2.83 us                                                | 2.74 us: 1.03x faster                                                        |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                        |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                                         |
| gc_traversal               | 3.79 ms                                                | 3.71 ms: 1.02x faster                                                        |
| go                         | 139 ms                                                 | 137 ms: 1.02x faster                                                         |
| pickle_list                | 5.08 us                                                | 5.00 us: 1.02x faster                                                        |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.34 ms: 1.01x faster                                                        |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.55 sec: 1.01x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.68 ms: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| async_generators           | 463 ms                                                 | 460 ms: 1.01x faster                                                         |
| mdp                        | 2.63 sec                                               | 2.62 sec: 1.01x faster                                                       |
| bench_thread_pool          | 842 us                                                 | 841 us: 1.00x faster                                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.69 ms: 1.00x slower                                                        |
| dulwich_log                | 68.5 ms                                                | 68.9 ms: 1.01x slower                                                        |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                                        |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                         |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                                        |
| regex_effbot               | 3.61 ms                                                | 3.65 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                        |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.02x slower                                                         |
| sympy_str                  | 300 ms                                                 | 306 ms: 1.02x slower                                                         |
| sympy_sum                  | 169 ms                                                 | 173 ms: 1.02x slower                                                         |
| django_template            | 34.6 ms                                                | 35.4 ms: 1.02x slower                                                        |
| 2to3                       | 274 ms                                                 | 285 ms: 1.04x slower                                                         |
| docutils                   | 2.77 sec                                               | 2.88 sec: 1.04x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                         |
| sqlglot_normalize          | 110 ms                                                 | 116 ms: 1.05x slower                                                         |
| sympy_expand               | 478 ms                                                 | 505 ms: 1.06x slower                                                         |
| nqueens                    | 83.3 ms                                                | 88.1 ms: 1.06x slower                                                        |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                        |
| telco                      | 7.10 ms                                                | 8.10 ms: 1.14x slower                                                        |
| generators                 | 31.2 ms                                                | 36.2 ms: 1.16x slower                                                        |
| sqlglot_optimize           | 54.8 ms                                                | 63.7 ms: 1.16x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 1.72 ms: 1.17x slower                                                        |
| coverage                   | 72.7 ms                                                | 85.3 ms: 1.17x slower                                                        |
| hexiom                     | 6.41 ms                                                | 7.89 ms: 1.23x slower                                                        |
| sympy_integrate            | 21.4 ms                                                | 26.5 ms: 1.24x slower                                                        |
| unpack_sequence            | 54.0 ns                                                | 109 ns: 2.03x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                                 |

Benchmark hidden because not significant (4): bench_mp_pool, asyncio_tcp, unpickle_list, pycparser
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240919-3.14.0a0-14c70a7-JIT/bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.89% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x