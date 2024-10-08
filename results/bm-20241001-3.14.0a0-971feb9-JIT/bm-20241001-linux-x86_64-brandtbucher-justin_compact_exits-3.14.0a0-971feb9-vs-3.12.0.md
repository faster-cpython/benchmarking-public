# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: 971feb9
- commit date: 2024-10-01
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 277 ms: 1.01x slower                                                        |
| tornado_http   | 103 ms                                                 | 94.1 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                                        |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 314 ms: 1.43x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 405 ms: 1.43x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 883 ms: 1.34x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 558 ms: 1.30x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 892 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.27x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.4 ms: 1.19x faster                                                       |
| nbody          | 97.0 ms                                                | 82.8 ms: 1.17x faster                                                       |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 140 ms: 1.06x faster                                                        |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                                        |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 76.7 ms: 1.16x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 54.1 ms: 1.14x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                        |
| unpickle             | 15.9 us                                                | 14.6 us: 1.09x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 98.7 ms: 1.08x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                        |
| json_loads           | 28.5 us                                                | 26.8 us: 1.06x faster                                                       |
| pickle_pure_python   | 324 us                                                 | 307 us: 1.06x faster                                                        |
| pickle_dict          | 35.5 us                                                | 34.1 us: 1.04x faster                                                       |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                       |
| unpickle_list        | 5.29 us                                                | 5.25 us: 1.01x faster                                                       |
| pickle_list          | 5.08 us                                                | 5.06 us: 1.01x faster                                                       |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                       |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.79 ms: 1.21x faster                                                       |
| django_template | 34.6 ms                                                | 35.4 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.8 us: 1.52x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                                        |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 314 ms: 1.43x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 405 ms: 1.43x faster                                                        |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                        |
| richards                   | 45.8 ms                                                | 32.7 ms: 1.40x faster                                                       |
| comprehensions             | 21.8 us                                                | 16.2 us: 1.35x faster                                                       |
| richards_super             | 51.5 ms                                                | 38.5 ms: 1.34x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 883 ms: 1.34x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 558 ms: 1.30x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 892 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.27x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 64.9 ms: 1.26x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                       |
| scimark_fft                | 382 ms                                                 | 307 ms: 1.24x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                      |
| pathlib                    | 19.3 ms                                                | 15.6 ms: 1.24x faster                                                       |
| mako                       | 11.9 ms                                                | 9.79 ms: 1.21x faster                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 62.2 ms: 1.21x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.13 ms: 1.19x faster                                                       |
| float                      | 84.7 ms                                                | 71.4 ms: 1.19x faster                                                       |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                                       |
| nbody                      | 97.0 ms                                                | 82.8 ms: 1.17x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 76.7 ms: 1.16x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.40 ms: 1.15x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.62 us: 1.15x faster                                                       |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 54.1 ms: 1.14x faster                                                       |
| fannkuch                   | 417 ms                                                 | 366 ms: 1.14x faster                                                        |
| chaos                      | 67.0 ms                                                | 59.3 ms: 1.13x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 691 ms: 1.12x faster                                                        |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                        |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                        |
| go                         | 139 ms                                                 | 127 ms: 1.09x faster                                                        |
| pyflate                    | 482 ms                                                 | 441 ms: 1.09x faster                                                        |
| tornado_http               | 103 ms                                                 | 94.1 ms: 1.09x faster                                                       |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.44 sec: 1.09x faster                                                      |
| unpickle                   | 15.9 us                                                | 14.6 us: 1.09x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                 | 98.7 ms: 1.08x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                        |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                        |
| json_loads                 | 28.5 us                                                | 26.8 us: 1.06x faster                                                       |
| regex_compile              | 148 ms                                                 | 140 ms: 1.06x faster                                                        |
| scimark_lu                 | 118 ms                                                 | 111 ms: 1.06x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 307 us: 1.06x faster                                                        |
| pickle_dict                | 35.5 us                                                | 34.1 us: 1.04x faster                                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                       |
| mdp                        | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                      |
| sqlite_synth               | 2.83 us                                                | 2.74 us: 1.04x faster                                                       |
| json                       | 5.26 ms                                                | 5.10 ms: 1.03x faster                                                       |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                       |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.65 ms: 1.02x faster                                                       |
| asyncio_tcp                | 491 ms                                                 | 484 ms: 1.01x faster                                                        |
| dulwich_log                | 68.5 ms                                                | 67.6 ms: 1.01x faster                                                       |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                        |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                       |
| unpickle_list              | 5.29 us                                                | 5.25 us: 1.01x faster                                                       |
| sympy_str                  | 300 ms                                                 | 298 ms: 1.01x faster                                                        |
| pickle_list                | 5.08 us                                                | 5.06 us: 1.01x faster                                                       |
| async_generators           | 463 ms                                                 | 461 ms: 1.00x faster                                                        |
| logging_silent             | 104 ns                                                 | 105 ns: 1.00x slower                                                        |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                      |
| 2to3                       | 274 ms                                                 | 277 ms: 1.01x slower                                                        |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                                       |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                       |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.02x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 3.88 ms: 1.02x slower                                                       |
| django_template            | 34.6 ms                                                | 35.4 ms: 1.02x slower                                                       |
| hexiom                     | 6.41 ms                                                | 6.67 ms: 1.04x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                        |
| sympy_expand               | 478 ms                                                 | 500 ms: 1.05x slower                                                        |
| sympy_sum                  | 169 ms                                                 | 177 ms: 1.05x slower                                                        |
| sympy_integrate            | 21.4 ms                                                | 22.6 ms: 1.06x slower                                                       |
| bench_thread_pool          | 842 us                                                 | 891 us: 1.06x slower                                                        |
| telco                      | 7.10 ms                                                | 7.63 ms: 1.08x slower                                                       |
| nqueens                    | 83.3 ms                                                | 89.6 ms: 1.08x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                       |
| generators                 | 31.2 ms                                                | 34.1 ms: 1.09x slower                                                       |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.73 ms: 1.17x slower                                                       |
| coverage                   | 72.7 ms                                                | 85.9 ms: 1.18x slower                                                       |
| unpack_sequence            | 54.0 ns                                                | 105 ns: 1.94x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 60.8 ms: 2.53x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (9) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, docutils, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_optimize
Ignored benchmarks (6) of results/bm-20241001-3.14.0a0-971feb9-JIT/bm-20241001-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-971feb9.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.03x