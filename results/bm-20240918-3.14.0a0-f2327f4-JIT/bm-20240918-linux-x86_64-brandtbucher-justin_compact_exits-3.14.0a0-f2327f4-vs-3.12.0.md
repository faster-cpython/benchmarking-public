# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: f2327f4
- commit date: 2024-09-18
- overall geometric mean: 1.05x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 282 ms: 1.03x slower                                                        |
| docutils       | 2.77 sec                                               | 3.20 sec: 1.16x slower                                                      |
| tornado_http   | 103 ms                                                 | 95.0 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 360 ms: 1.31x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 455 ms: 1.27x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 941 ms: 1.23x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 605 ms: 1.20x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 1.02 sec: 1.16x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 401 ms: 1.12x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 513 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 666 ms: 1.09x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 81.1 ms: 1.20x faster                                                       |
| float          | 84.7 ms                                                | 72.1 ms: 1.18x faster                                                       |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 138 ms: 1.08x faster                                                        |
| regex_effbot   | 3.61 ms                                                | 3.65 ms: 1.01x slower                                                       |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                        |
| regex_v8       | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 77.4 ms: 1.15x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 54.2 ms: 1.14x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.07x faster                                                        |
| unpickle             | 15.9 us                                                | 14.8 us: 1.07x faster                                                       |
| pickle_pure_python   | 324 us                                                 | 305 us: 1.06x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 150 ms: 1.06x faster                                                        |
| json_loads           | 28.5 us                                                | 27.0 us: 1.05x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.03x faster                                                        |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                       |
| pickle_dict          | 35.5 us                                                | 35.1 us: 1.01x faster                                                       |
| pickle               | 11.6 us                                                | 11.5 us: 1.01x faster                                                       |
| unpickle_list        | 5.29 us                                                | 5.41 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                       |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.0 ms: 1.19x faster                                                       |
| django_template | 34.6 ms                                                | 35.7 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.9 us: 1.51x faster                                                       |
| deepcopy                   | 371 us                                                 | 250 us: 1.48x faster                                                        |
| async_tree_none            | 472 ms                                                 | 360 ms: 1.31x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 455 ms: 1.27x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.65 us: 1.26x faster                                                       |
| scimark_fft                | 382 ms                                                 | 308 ms: 1.24x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 66.5 ms: 1.23x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 941 ms: 1.23x faster                                                        |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.22x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 62.6 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 605 ms: 1.20x faster                                                        |
| nbody                      | 97.0 ms                                                | 81.1 ms: 1.20x faster                                                       |
| mako                       | 11.9 ms                                                | 10.0 ms: 1.19x faster                                                       |
| float                      | 84.7 ms                                                | 72.1 ms: 1.18x faster                                                       |
| logging_format             | 7.23 us                                                | 6.20 us: 1.17x faster                                                       |
| spectral_norm              | 115 ms                                                 | 98.6 ms: 1.16x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 1.02 sec: 1.16x faster                                                      |
| richards                   | 45.8 ms                                                | 39.5 ms: 1.16x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.21 ms: 1.16x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 77.4 ms: 1.15x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.64 us: 1.15x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.42 ms: 1.14x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 54.2 ms: 1.14x faster                                                       |
| chaos                      | 67.0 ms                                                | 58.9 ms: 1.14x faster                                                       |
| richards_super             | 51.5 ms                                                | 45.6 ms: 1.13x faster                                                       |
| raytrace                   | 312 ms                                                 | 277 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 401 ms: 1.12x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 513 ms: 1.12x faster                                                        |
| go                         | 139 ms                                                 | 126 ms: 1.11x faster                                                        |
| fannkuch                   | 417 ms                                                 | 377 ms: 1.11x faster                                                        |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 666 ms: 1.09x faster                                                        |
| tornado_http               | 103 ms                                                 | 95.0 ms: 1.08x faster                                                       |
| regex_compile              | 148 ms                                                 | 138 ms: 1.08x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.07x faster                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                                      |
| unpickle                   | 15.9 us                                                | 14.8 us: 1.07x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 725 ms: 1.07x faster                                                        |
| pyflate                    | 482 ms                                                 | 452 ms: 1.07x faster                                                        |
| scimark_lu                 | 118 ms                                                 | 111 ms: 1.06x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 305 us: 1.06x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 150 ms: 1.06x faster                                                        |
| json_loads                 | 28.5 us                                                | 27.0 us: 1.05x faster                                                       |
| json                       | 5.26 ms                                                | 4.99 ms: 1.05x faster                                                       |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                        |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.03x faster                                                        |
| sqlite_synth               | 2.83 us                                                | 2.76 us: 1.03x faster                                                       |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                       |
| dulwich_log                | 68.5 ms                                                | 67.6 ms: 1.01x faster                                                       |
| async_generators           | 463 ms                                                 | 457 ms: 1.01x faster                                                        |
| sympy_str                  | 300 ms                                                 | 296 ms: 1.01x faster                                                        |
| pickle_dict                | 35.5 us                                                | 35.1 us: 1.01x faster                                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.35 ms: 1.01x faster                                                       |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                        |
| bench_thread_pool          | 842 us                                                 | 837 us: 1.01x faster                                                        |
| pickle                     | 11.6 us                                                | 11.5 us: 1.01x faster                                                       |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                        |
| sqlglot_normalize          | 110 ms                                                 | 111 ms: 1.01x slower                                                        |
| logging_silent             | 104 ns                                                 | 105 ns: 1.01x slower                                                        |
| regex_effbot               | 3.61 ms                                                | 3.65 ms: 1.01x slower                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                      |
| sympy_sum                  | 169 ms                                                 | 171 ms: 1.01x slower                                                        |
| nqueens                    | 83.3 ms                                                | 84.6 ms: 1.02x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                       |
| unpickle_list              | 5.29 us                                                | 5.41 us: 1.02x slower                                                       |
| pycparser                  | 1.18 sec                                               | 1.21 sec: 1.03x slower                                                      |
| asyncio_tcp                | 491 ms                                                 | 505 ms: 1.03x slower                                                        |
| 2to3                       | 274 ms                                                 | 282 ms: 1.03x slower                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.73 ms: 1.03x slower                                                       |
| django_template            | 34.6 ms                                                | 35.7 ms: 1.03x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                        |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                        |
| sqlglot_optimize           | 54.8 ms                                                | 57.1 ms: 1.04x slower                                                       |
| generators                 | 31.2 ms                                                | 32.6 ms: 1.05x slower                                                       |
| sympy_expand               | 478 ms                                                 | 503 ms: 1.05x slower                                                        |
| sympy_integrate            | 21.4 ms                                                | 22.7 ms: 1.06x slower                                                       |
| gc_traversal               | 3.79 ms                                                | 4.04 ms: 1.06x slower                                                       |
| hexiom                     | 6.41 ms                                                | 6.83 ms: 1.07x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                       |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| telco                      | 7.10 ms                                                | 8.07 ms: 1.14x slower                                                       |
| docutils                   | 2.77 sec                                               | 3.20 sec: 1.16x slower                                                      |
| coverage                   | 72.7 ms                                                | 85.9 ms: 1.18x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.77 ms: 1.20x slower                                                       |
| unpack_sequence            | 54.0 ns                                                | 107 ns: 1.98x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (3): bench_mp_pool, pickle_list, coroutines
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240918-3.14.0a0-f2327f4-JIT/bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.05x