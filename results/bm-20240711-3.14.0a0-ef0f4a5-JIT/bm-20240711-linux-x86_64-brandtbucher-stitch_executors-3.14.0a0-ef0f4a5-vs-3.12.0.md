# Results vs. 3.12.0

- fork: brandtbucher
- ref: stitch_executors
- machine: linux-x86_64
- commit hash: ef0f4a5
- commit date: 2024-07-11
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 271 ms: 1.01x faster                                                    |
| docutils       | 2.77 sec                                               | 2.85 sec: 1.03x slower                                                  |
| tornado_http   | 103 ms                                                 | 92.5 ms: 1.11x faster                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 376 ms: 1.53x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                    |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 406 ms: 1.42x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 845 ms: 1.40x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 836 ms: 1.38x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 540 ms: 1.34x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.42x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.6 ms: 1.22x faster                                                   |
| float          | 84.7 ms                                                | 69.8 ms: 1.21x faster                                                   |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.14x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 136 ms: 1.09x faster                                                    |
| regex_effbot   | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                   |
| regex_dna      | 212 ms                                                 | 228 ms: 1.07x slower                                                    |
| regex_v8       | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 81.0 ms: 1.10x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 295 us: 1.10x faster                                                    |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 98.5 ms: 1.08x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 57.6 ms: 1.07x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.06x faster                                                    |
| json_loads           | 28.5 us                                                | 27.9 us: 1.02x faster                                                   |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.10 ms: 1.02x slower                                                   |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.84 ms: 1.21x faster                                                   |
| django_template | 34.6 ms                                                | 35.3 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 376 ms: 1.53x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                    |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                                    |
| deepcopy_memo              | 40.7 us                                                | 28.2 us: 1.44x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 406 ms: 1.42x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 845 ms: 1.40x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 836 ms: 1.38x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 540 ms: 1.34x faster                                                    |
| deepcopy                   | 371 us                                                 | 278 us: 1.33x faster                                                    |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.31x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                                   |
| scimark_fft                | 382 ms                                                 | 311 ms: 1.23x faster                                                    |
| crypto_pyaes               | 81.9 ms                                                | 66.8 ms: 1.23x faster                                                   |
| nbody                      | 97.0 ms                                                | 79.6 ms: 1.22x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 61.7 ms: 1.22x faster                                                   |
| float                      | 84.7 ms                                                | 69.8 ms: 1.21x faster                                                   |
| mako                       | 11.9 ms                                                | 9.84 ms: 1.21x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                   |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.48 us: 1.18x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.36 ms: 1.16x faster                                                   |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                                    |
| chaos                      | 67.0 ms                                                | 58.2 ms: 1.15x faster                                                   |
| fannkuch                   | 417 ms                                                 | 363 ms: 1.15x faster                                                    |
| tornado_http               | 103 ms                                                 | 92.5 ms: 1.11x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 81.0 ms: 1.10x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 295 us: 1.10x faster                                                    |
| regex_compile              | 148 ms                                                 | 136 ms: 1.09x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 98.5 ms: 1.08x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 717 ms: 1.08x faster                                                    |
| spectral_norm              | 115 ms                                                 | 106 ms: 1.08x faster                                                    |
| pyflate                    | 482 ms                                                 | 447 ms: 1.08x faster                                                    |
| sqlglot_parse              | 1.36 ms                                                | 1.26 ms: 1.08x faster                                                   |
| richards                   | 45.8 ms                                                | 42.6 ms: 1.08x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 57.6 ms: 1.07x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.06x faster                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                                   |
| richards_super             | 51.5 ms                                                | 48.7 ms: 1.06x faster                                                   |
| generators                 | 31.2 ms                                                | 29.6 ms: 1.06x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.55 ms: 1.05x faster                                                   |
| gc_traversal               | 3.79 ms                                                | 3.65 ms: 1.04x faster                                                   |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                    |
| mdp                        | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                  |
| dask                       | 372 ms                                                 | 362 ms: 1.03x faster                                                    |
| sympy_sum                  | 169 ms                                                 | 165 ms: 1.02x faster                                                    |
| json_loads                 | 28.5 us                                                | 27.9 us: 1.02x faster                                                   |
| sympy_str                  | 300 ms                                                 | 293 ms: 1.02x faster                                                    |
| json                       | 5.26 ms                                                | 5.16 ms: 1.02x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 67.4 ms: 1.02x faster                                                   |
| 2to3                       | 274 ms                                                 | 271 ms: 1.01x faster                                                    |
| bench_thread_pool          | 842 us                                                 | 832 us: 1.01x faster                                                    |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                    |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 55.4 ms: 1.01x slower                                                   |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                  |
| hexiom                     | 6.41 ms                                                | 6.52 ms: 1.02x slower                                                   |
| logging_silent             | 104 ns                                                 | 106 ns: 1.02x slower                                                    |
| coroutines                 | 23.2 ms                                                | 23.6 ms: 1.02x slower                                                   |
| django_template            | 34.6 ms                                                | 35.3 ms: 1.02x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.10 ms: 1.02x slower                                                   |
| sympy_integrate            | 21.4 ms                                                | 21.9 ms: 1.02x slower                                                   |
| scimark_sor                | 129 ms                                                 | 132 ms: 1.03x slower                                                    |
| asyncio_tcp                | 491 ms                                                 | 504 ms: 1.03x slower                                                    |
| nqueens                    | 83.3 ms                                                | 85.7 ms: 1.03x slower                                                   |
| docutils                   | 2.77 sec                                               | 2.85 sec: 1.03x slower                                                  |
| sympy_expand               | 478 ms                                                 | 495 ms: 1.04x slower                                                    |
| go                         | 139 ms                                                 | 145 ms: 1.04x slower                                                    |
| regex_effbot               | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                   |
| scimark_lu                 | 118 ms                                                 | 123 ms: 1.04x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                                    |
| regex_dna                  | 212 ms                                                 | 228 ms: 1.07x slower                                                    |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                   |
| telco                      | 7.10 ms                                                | 8.06 ms: 1.14x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                   |
| coverage                   | 72.7 ms                                                | 93.2 ms: 1.28x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                            |

Benchmark hidden because not significant (4): sqlglot_normalize, bench_mp_pool, async_generators, pycparser
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240711-3.14.0a0-ef0f4a5-JIT/bm-20240711-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-ef0f4a5.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.04x