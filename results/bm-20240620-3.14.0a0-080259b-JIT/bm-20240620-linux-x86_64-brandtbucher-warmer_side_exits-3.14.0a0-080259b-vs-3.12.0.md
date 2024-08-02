# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmer_side_exits
- machine: linux-x86_64
- commit hash: 080259b
- commit date: 2024-06-20
- overall geometric mean: 1.07x faster
- HPT reliability: 99.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 276 ms: 1.00x slower                                                     |
| docutils       | 2.77 sec                                               | 2.88 sec: 1.04x slower                                                   |
| tornado_http   | 103 ms                                                 | 94.1 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                  | 1.01x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 424 ms: 1.36x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 338 ms: 1.33x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 902 ms: 1.31x faster                                                     |
| async_tree_none            | 472 ms                                                 | 369 ms: 1.28x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 452 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 570 ms: 1.27x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 911 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 596 ms: 1.22x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.29x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.6 ms: 1.20x faster                                                    |
| nbody          | 97.0 ms                                                | 83.0 ms: 1.17x faster                                                    |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.12x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.10x faster                                                     |
| regex_effbot   | 3.61 ms                                                | 3.72 ms: 1.03x slower                                                    |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                    |
| regex_dna      | 212 ms                                                 | 228 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.90 sec: 1.22x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 204 us: 1.13x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 80.6 ms: 1.11x faster                                                    |
| pickle_pure_python   | 324 us                                                 | 294 us: 1.10x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 99.3 ms: 1.08x faster                                                    |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 57.8 ms: 1.07x faster                                                    |
| unpickle_list        | 5.29 us                                                | 5.13 us: 1.03x faster                                                    |
| pickle_dict          | 35.5 us                                                | 35.9 us: 1.01x slower                                                    |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                    |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                                    |
| pickle_list          | 5.08 us                                                | 5.19 us: 1.02x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                             |

Benchmark hidden because not significant (2): unpickle, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.39 ms: 1.07x slower                                                    |
| python_startup         | 9.55 ms                                                | 10.8 ms: 1.13x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.58 ms: 1.24x faster                                                    |
| django_template | 34.6 ms                                                | 35.5 ms: 1.03x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 29.1 us: 1.40x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 424 ms: 1.36x faster                                                     |
| deepcopy                   | 371 us                                                 | 279 us: 1.33x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 338 ms: 1.33x faster                                                     |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 902 ms: 1.31x faster                                                     |
| async_tree_none            | 472 ms                                                 | 369 ms: 1.28x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 452 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 570 ms: 1.27x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 911 ms: 1.27x faster                                                     |
| mako                       | 11.9 ms                                                | 9.58 ms: 1.24x faster                                                    |
| crypto_pyaes               | 81.9 ms                                                | 66.8 ms: 1.23x faster                                                    |
| tomli_loads                | 2.33 sec                                               | 1.90 sec: 1.22x faster                                                   |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 596 ms: 1.22x faster                                                     |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 61.9 ms: 1.21x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 2.76 us: 1.21x faster                                                    |
| fannkuch                   | 417 ms                                                 | 345 ms: 1.21x faster                                                     |
| float                      | 84.7 ms                                                | 70.6 ms: 1.20x faster                                                    |
| logging_format             | 7.23 us                                                | 6.03 us: 1.20x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.22 ms: 1.20x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.46 us: 1.18x faster                                                    |
| nbody                      | 97.0 ms                                                | 83.0 ms: 1.17x faster                                                    |
| chaos                      | 67.0 ms                                                | 58.3 ms: 1.15x faster                                                    |
| richards                   | 45.8 ms                                                | 40.5 ms: 1.13x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 204 us: 1.13x faster                                                     |
| raytrace                   | 312 ms                                                 | 277 ms: 1.13x faster                                                     |
| pyflate                    | 482 ms                                                 | 434 ms: 1.11x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 80.6 ms: 1.11x faster                                                    |
| regex_compile              | 148 ms                                                 | 134 ms: 1.10x faster                                                     |
| pickle_pure_python         | 324 us                                                 | 294 us: 1.10x faster                                                     |
| spectral_norm              | 115 ms                                                 | 105 ms: 1.09x faster                                                     |
| tornado_http               | 103 ms                                                 | 94.1 ms: 1.09x faster                                                    |
| pprint_safe_repr           | 776 ms                                                 | 712 ms: 1.09x faster                                                     |
| richards_super             | 51.5 ms                                                | 47.6 ms: 1.08x faster                                                    |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.08x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 99.3 ms: 1.08x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 57.8 ms: 1.07x faster                                                    |
| gc_traversal               | 3.79 ms                                                | 3.57 ms: 1.06x faster                                                    |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                    |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                     |
| generators                 | 31.2 ms                                                | 29.7 ms: 1.05x faster                                                    |
| unpickle_list              | 5.29 us                                                | 5.13 us: 1.03x faster                                                    |
| bench_thread_pool          | 842 us                                                 | 827 us: 1.02x faster                                                     |
| dask                       | 372 ms                                                 | 366 ms: 1.02x faster                                                     |
| async_generators           | 463 ms                                                 | 457 ms: 1.01x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 67.7 ms: 1.01x faster                                                    |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                     |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                   |
| 2to3                       | 274 ms                                                 | 276 ms: 1.00x slower                                                     |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                     |
| pickle_dict                | 35.5 us                                                | 35.9 us: 1.01x slower                                                    |
| logging_silent             | 104 ns                                                 | 106 ns: 1.01x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                    |
| nqueens                    | 83.3 ms                                                | 84.7 ms: 1.02x slower                                                    |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                                    |
| hexiom                     | 6.41 ms                                                | 6.54 ms: 1.02x slower                                                    |
| pickle_list                | 5.08 us                                                | 5.19 us: 1.02x slower                                                    |
| django_template            | 34.6 ms                                                | 35.5 ms: 1.03x slower                                                    |
| sqlglot_optimize           | 54.8 ms                                                | 56.3 ms: 1.03x slower                                                    |
| regex_effbot               | 3.61 ms                                                | 3.72 ms: 1.03x slower                                                    |
| deltablue                  | 3.72 ms                                                | 3.84 ms: 1.03x slower                                                    |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.03x slower                                                     |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                    |
| docutils                   | 2.77 sec                                               | 2.88 sec: 1.04x slower                                                   |
| sympy_integrate            | 21.4 ms                                                | 22.3 ms: 1.04x slower                                                    |
| mdp                        | 2.63 sec                                               | 2.75 sec: 1.05x slower                                                   |
| scimark_lu                 | 118 ms                                                 | 124 ms: 1.05x slower                                                     |
| scimark_sor                | 129 ms                                                 | 136 ms: 1.05x slower                                                     |
| go                         | 139 ms                                                 | 147 ms: 1.05x slower                                                     |
| sympy_expand               | 478 ms                                                 | 505 ms: 1.06x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 7.39 ms: 1.07x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                     |
| regex_dna                  | 212 ms                                                 | 228 ms: 1.07x slower                                                     |
| telco                      | 7.10 ms                                                | 7.97 ms: 1.12x slower                                                    |
| python_startup             | 9.55 ms                                                | 10.8 ms: 1.13x slower                                                    |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.18x slower                                                    |
| coverage                   | 72.7 ms                                                | 92.9 ms: 1.28x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                             |

Benchmark hidden because not significant (9): unpickle, sqlite_synth, sympy_sum, bench_mp_pool, json_loads, sympy_str, asyncio_tcp, json, pycparser
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240620-3.14.0a0-080259b-JIT/bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.84% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x