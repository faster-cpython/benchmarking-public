# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: fewer_set_ip
- machine: linux-x86_64
- commit hash: 3d98d27
- commit date: 2024-09-17
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 275 ms: 1.00x slower                                                    |
| docutils       | 2.77 sec                                               | 2.96 sec: 1.07x slower                                                  |
| tornado_http   | 103 ms                                                 | 94.8 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                  | 1.00x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 317 ms: 1.49x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 388 ms: 1.48x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 308 ms: 1.46x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 398 ms: 1.45x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 877 ms: 1.35x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 863 ms: 1.34x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 552 ms: 1.31x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.1 ms: 1.23x faster                                                   |
| nbody          | 97.0 ms                                                | 82.1 ms: 1.18x faster                                                   |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.14x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 141 ms: 1.05x faster                                                    |
| regex_v8       | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                   |
| regex_dna      | 212 ms                                                 | 228 ms: 1.08x slower                                                    |
| regex_effbot   | 3.61 ms                                                | 4.01 ms: 1.11x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.90 sec: 1.23x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 77.5 ms: 1.15x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 53.9 ms: 1.15x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 144 ms: 1.11x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 97.8 ms: 1.09x faster                                                   |
| unpickle             | 15.9 us                                                | 14.7 us: 1.08x faster                                                   |
| pickle_dict          | 35.5 us                                                | 33.0 us: 1.08x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.07x faster                                                    |
| json_loads           | 28.5 us                                                | 27.0 us: 1.06x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 307 us: 1.06x faster                                                    |
| unpickle_list        | 5.29 us                                                | 5.18 us: 1.02x faster                                                   |
| pickle_list          | 5.08 us                                                | 5.02 us: 1.01x faster                                                   |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                            |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                   |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.80 ms: 1.21x faster                                                   |
| django_template | 34.6 ms                                                | 35.2 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.7 us: 1.52x faster                                                   |
| async_tree_none            | 472 ms                                                 | 317 ms: 1.49x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 388 ms: 1.48x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 308 ms: 1.46x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 398 ms: 1.45x faster                                                    |
| deepcopy                   | 371 us                                                 | 267 us: 1.39x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 877 ms: 1.35x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 863 ms: 1.34x faster                                                    |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 552 ms: 1.31x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 2.63 us: 1.27x faster                                                   |
| scimark_fft                | 382 ms                                                 | 301 ms: 1.27x faster                                                    |
| crypto_pyaes               | 81.9 ms                                                | 65.4 ms: 1.25x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.90 sec: 1.23x faster                                                  |
| float                      | 84.7 ms                                                | 69.1 ms: 1.23x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.14 ms: 1.22x faster                                                   |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                   |
| mako                       | 11.9 ms                                                | 9.80 ms: 1.21x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 61.9 ms: 1.21x faster                                                   |
| logging_format             | 7.23 us                                                | 6.05 us: 1.20x faster                                                   |
| nbody                      | 97.0 ms                                                | 82.1 ms: 1.18x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.52 us: 1.17x faster                                                   |
| richards                   | 45.8 ms                                                | 39.5 ms: 1.16x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.21 ms: 1.16x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 77.5 ms: 1.15x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 53.9 ms: 1.15x faster                                                   |
| richards_super             | 51.5 ms                                                | 45.0 ms: 1.15x faster                                                   |
| chaos                      | 67.0 ms                                                | 58.6 ms: 1.14x faster                                                   |
| fannkuch                   | 417 ms                                                 | 369 ms: 1.13x faster                                                    |
| raytrace                   | 312 ms                                                 | 277 ms: 1.13x faster                                                    |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.12x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 144 ms: 1.11x faster                                                    |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 97.8 ms: 1.09x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 109 ms: 1.09x faster                                                    |
| tornado_http               | 103 ms                                                 | 94.8 ms: 1.08x faster                                                   |
| unpickle                   | 15.9 us                                                | 14.7 us: 1.08x faster                                                   |
| pyflate                    | 482 ms                                                 | 448 ms: 1.08x faster                                                    |
| pickle_dict                | 35.5 us                                                | 33.0 us: 1.08x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.07x faster                                                    |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                    |
| go                         | 139 ms                                                 | 131 ms: 1.07x faster                                                    |
| json_loads                 | 28.5 us                                                | 27.0 us: 1.06x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 307 us: 1.06x faster                                                    |
| regex_compile              | 148 ms                                                 | 141 ms: 1.05x faster                                                    |
| pprint_safe_repr           | 776 ms                                                 | 743 ms: 1.04x faster                                                    |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                                    |
| mdp                        | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                  |
| json                       | 5.26 ms                                                | 5.12 ms: 1.03x faster                                                   |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                  |
| async_generators           | 463 ms                                                 | 453 ms: 1.02x faster                                                    |
| unpickle_list              | 5.29 us                                                | 5.18 us: 1.02x faster                                                   |
| gc_traversal               | 3.79 ms                                                | 3.74 ms: 1.02x faster                                                   |
| sympy_str                  | 300 ms                                                 | 295 ms: 1.01x faster                                                    |
| pickle_list                | 5.08 us                                                | 5.02 us: 1.01x faster                                                   |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                    |
| dulwich_log                | 68.5 ms                                                | 67.8 ms: 1.01x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.35 ms: 1.01x faster                                                   |
| bench_thread_pool          | 842 us                                                 | 836 us: 1.01x faster                                                    |
| 2to3                       | 274 ms                                                 | 275 ms: 1.00x slower                                                    |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                    |
| sympy_sum                  | 169 ms                                                 | 170 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.02x slower                                                    |
| django_template            | 34.6 ms                                                | 35.2 ms: 1.02x slower                                                   |
| asyncio_tcp                | 491 ms                                                 | 500 ms: 1.02x slower                                                    |
| nqueens                    | 83.3 ms                                                | 85.0 ms: 1.02x slower                                                   |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.02x slower                                                    |
| sympy_expand               | 478 ms                                                 | 499 ms: 1.04x slower                                                    |
| sympy_integrate            | 21.4 ms                                                | 22.6 ms: 1.06x slower                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 57.9 ms: 1.06x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                   |
| generators                 | 31.2 ms                                                | 33.3 ms: 1.07x slower                                                   |
| hexiom                     | 6.41 ms                                                | 6.84 ms: 1.07x slower                                                   |
| docutils                   | 2.77 sec                                               | 2.96 sec: 1.07x slower                                                  |
| regex_dna                  | 212 ms                                                 | 228 ms: 1.08x slower                                                    |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                   |
| regex_effbot               | 3.61 ms                                                | 4.01 ms: 1.11x slower                                                   |
| telco                      | 7.10 ms                                                | 7.91 ms: 1.11x slower                                                   |
| coverage                   | 72.7 ms                                                | 85.0 ms: 1.17x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.18x slower                                                   |
| unpack_sequence            | 54.0 ns                                                | 113 ns: 2.09x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                            |

Benchmark hidden because not significant (6): sqlite_synth, pprint_pformat, bench_mp_pool, pickle, sqlglot_transpile, coroutines
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240917-3.14.0a0-3d98d27-JIT/bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.05x