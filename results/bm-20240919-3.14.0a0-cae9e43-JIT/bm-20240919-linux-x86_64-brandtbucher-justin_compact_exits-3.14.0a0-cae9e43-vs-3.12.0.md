# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: cae9e43
- commit date: 2024-09-19
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 277 ms: 1.01x slower                                                        |
| docutils       | 2.77 sec                                               | 2.92 sec: 1.06x slower                                                      |
| tornado_http   | 103 ms                                                 | 94.0 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 371 ms: 1.55x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 380 ms: 1.52x faster                                                        |
| async_tree_none            | 472 ms                                                 | 320 ms: 1.47x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.46x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 536 ms: 1.35x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 875 ms: 1.35x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 540 ms: 1.34x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 929 ms: 1.24x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.41x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.5 ms: 1.20x faster                                                       |
| float          | 84.7 ms                                                | 70.4 ms: 1.20x faster                                                       |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 137 ms: 1.08x faster                                                        |
| regex_effbot   | 3.61 ms                                                | 3.63 ms: 1.01x slower                                                       |
| regex_dna      | 212 ms                                                 | 215 ms: 1.02x slower                                                        |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 76.0 ms: 1.17x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 53.7 ms: 1.15x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 97.4 ms: 1.10x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.09x faster                                                        |
| pickle_dict          | 35.5 us                                                | 32.9 us: 1.08x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                                        |
| unpickle             | 15.9 us                                                | 15.0 us: 1.06x faster                                                       |
| json_loads           | 28.5 us                                                | 27.2 us: 1.05x faster                                                       |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                       |
| unpickle_list        | 5.29 us                                                | 5.19 us: 1.02x faster                                                       |
| pickle               | 11.6 us                                                | 11.5 us: 1.00x faster                                                       |
| pickle_list          | 5.08 us                                                | 5.18 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                       |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.72 ms: 1.22x faster                                                       |
| django_template | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 371 ms: 1.55x faster                                                        |
| deepcopy_memo              | 40.7 us                                                | 26.7 us: 1.53x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 380 ms: 1.52x faster                                                        |
| async_tree_none            | 472 ms                                                 | 320 ms: 1.47x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.46x faster                                                        |
| deepcopy                   | 371 us                                                 | 254 us: 1.46x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 536 ms: 1.35x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 875 ms: 1.35x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 540 ms: 1.34x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.25x faster                                                       |
| scimark_fft                | 382 ms                                                 | 306 ms: 1.25x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 929 ms: 1.24x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 66.0 ms: 1.24x faster                                                       |
| pathlib                    | 19.3 ms                                                | 15.7 ms: 1.23x faster                                                       |
| mako                       | 11.9 ms                                                | 9.72 ms: 1.22x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                      |
| nbody                      | 97.0 ms                                                | 80.5 ms: 1.20x faster                                                       |
| float                      | 84.7 ms                                                | 70.4 ms: 1.20x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.21 ms: 1.20x faster                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 62.7 ms: 1.20x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.14 ms: 1.18x faster                                                       |
| logging_format             | 7.23 us                                                | 6.14 us: 1.18x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 76.0 ms: 1.17x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.57 us: 1.16x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 53.7 ms: 1.15x faster                                                       |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.15x faster                                                        |
| chaos                      | 67.0 ms                                                | 58.4 ms: 1.15x faster                                                       |
| raytrace                   | 312 ms                                                 | 275 ms: 1.13x faster                                                        |
| richards                   | 45.8 ms                                                | 40.7 ms: 1.13x faster                                                       |
| richards_super             | 51.5 ms                                                | 45.7 ms: 1.13x faster                                                       |
| go                         | 139 ms                                                 | 125 ms: 1.12x faster                                                        |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.11x faster                                                        |
| fannkuch                   | 417 ms                                                 | 380 ms: 1.10x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 97.4 ms: 1.10x faster                                                       |
| tornado_http               | 103 ms                                                 | 94.0 ms: 1.09x faster                                                       |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.09x faster                                                        |
| regex_compile              | 148 ms                                                 | 137 ms: 1.08x faster                                                        |
| pickle_dict                | 35.5 us                                                | 32.9 us: 1.08x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 722 ms: 1.07x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                                        |
| scimark_lu                 | 118 ms                                                 | 110 ms: 1.07x faster                                                        |
| unpickle                   | 15.9 us                                                | 15.0 us: 1.06x faster                                                       |
| pyflate                    | 482 ms                                                 | 457 ms: 1.06x faster                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                      |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                        |
| json_loads                 | 28.5 us                                                | 27.2 us: 1.05x faster                                                       |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                      |
| sqlite_synth               | 2.83 us                                                | 2.73 us: 1.04x faster                                                       |
| json                       | 5.26 ms                                                | 5.09 ms: 1.03x faster                                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                       |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                       |
| gc_traversal               | 3.79 ms                                                | 3.72 ms: 1.02x faster                                                       |
| unpickle_list              | 5.29 us                                                | 5.19 us: 1.02x faster                                                       |
| dulwich_log                | 68.5 ms                                                | 67.3 ms: 1.02x faster                                                       |
| async_generators           | 463 ms                                                 | 458 ms: 1.01x faster                                                        |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                        |
| sympy_str                  | 300 ms                                                 | 297 ms: 1.01x faster                                                        |
| bench_thread_pool          | 842 us                                                 | 837 us: 1.01x faster                                                        |
| pickle                     | 11.6 us                                                | 11.5 us: 1.00x faster                                                       |
| sqlglot_normalize          | 110 ms                                                 | 110 ms: 1.00x faster                                                        |
| regex_effbot               | 3.61 ms                                                | 3.63 ms: 1.01x slower                                                       |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                        |
| 2to3                       | 274 ms                                                 | 277 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.70 ms: 1.01x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| sympy_sum                  | 169 ms                                                 | 171 ms: 1.01x slower                                                        |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.02x slower                                                        |
| asyncio_tcp                | 491 ms                                                 | 499 ms: 1.02x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                       |
| pickle_list                | 5.08 us                                                | 5.18 us: 1.02x slower                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 56.5 ms: 1.03x slower                                                       |
| generators                 | 31.2 ms                                                | 32.4 ms: 1.04x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                       |
| django_template            | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                       |
| nqueens                    | 83.3 ms                                                | 86.8 ms: 1.04x slower                                                       |
| sympy_expand               | 478 ms                                                 | 502 ms: 1.05x slower                                                        |
| docutils                   | 2.77 sec                                               | 2.92 sec: 1.06x slower                                                      |
| sympy_integrate            | 21.4 ms                                                | 22.7 ms: 1.06x slower                                                       |
| hexiom                     | 6.41 ms                                                | 6.87 ms: 1.07x slower                                                       |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                       |
| telco                      | 7.10 ms                                                | 7.95 ms: 1.12x slower                                                       |
| coverage                   | 72.7 ms                                                | 84.7 ms: 1.17x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                                       |
| unpack_sequence            | 54.0 ns                                                | 109 ns: 2.02x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                |

Benchmark hidden because not significant (2): coroutines, bench_mp_pool
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pycparser, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240919-3.14.0a0-cae9e43-JIT/bm-20240919-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-cae9e43.json: bpe_tokeniser, genshi_text, genshi_xml, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.05x