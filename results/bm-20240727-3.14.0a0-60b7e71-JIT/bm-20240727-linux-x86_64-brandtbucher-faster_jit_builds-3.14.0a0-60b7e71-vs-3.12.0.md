# Results vs. 3.12.0

- fork: brandtbucher
- ref: faster_jit_builds
- machine: linux-x86_64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.08x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 272 ms: 1.01x faster                                                     |
| docutils       | 2.77 sec                                               | 2.91 sec: 1.05x slower                                                   |
| tornado_http   | 103 ms                                                 | 93.3 ms: 1.10x faster                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 302 ms: 1.49x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 394 ms: 1.46x faster                                                     |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 416 ms: 1.39x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 536 ms: 1.35x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 874 ms: 1.35x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 904 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 568 ms: 1.28x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.1 ms: 1.21x faster                                                    |
| float          | 84.7 ms                                                | 70.6 ms: 1.20x faster                                                    |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.14x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.10x faster                                                     |
| regex_effbot   | 3.61 ms                                                | 3.82 ms: 1.06x slower                                                    |
| regex_dna      | 212 ms                                                 | 229 ms: 1.08x slower                                                     |
| regex_v8       | 23.1 ms                                                | 25.8 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                  | 1.04x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 81.3 ms: 1.10x faster                                                    |
| pickle_pure_python   | 324 us                                                 | 297 us: 1.09x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 56.8 ms: 1.09x faster                                                    |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 100 ms: 1.07x faster                                                     |
| json_loads           | 28.5 us                                                | 27.8 us: 1.03x faster                                                    |
| json_dumps           | 10.4 ms                                                | 10.4 ms: 1.00x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                    |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.82 ms: 1.21x faster                                                    |
| django_template | 34.6 ms                                                | 35.6 ms: 1.03x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 302 ms: 1.49x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 394 ms: 1.46x faster                                                     |
| deepcopy_memo              | 40.7 us                                                | 28.3 us: 1.44x faster                                                    |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 416 ms: 1.39x faster                                                     |
| deepcopy                   | 371 us                                                 | 273 us: 1.36x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 536 ms: 1.35x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 874 ms: 1.35x faster                                                     |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 904 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 568 ms: 1.28x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 66.3 ms: 1.23x faster                                                    |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 61.8 ms: 1.22x faster                                                    |
| nbody                      | 97.0 ms                                                | 80.1 ms: 1.21x faster                                                    |
| mako                       | 11.9 ms                                                | 9.82 ms: 1.21x faster                                                    |
| scimark_fft                | 382 ms                                                 | 316 ms: 1.21x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                   |
| float                      | 84.7 ms                                                | 70.6 ms: 1.20x faster                                                    |
| logging_format             | 7.23 us                                                | 6.03 us: 1.20x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 2.81 us: 1.19x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.46 us: 1.18x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.30 ms: 1.18x faster                                                    |
| raytrace                   | 312 ms                                                 | 270 ms: 1.16x faster                                                     |
| chaos                      | 67.0 ms                                                | 58.5 ms: 1.14x faster                                                    |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                                     |
| fannkuch                   | 417 ms                                                 | 367 ms: 1.14x faster                                                     |
| richards                   | 45.8 ms                                                | 40.4 ms: 1.14x faster                                                    |
| regex_compile              | 148 ms                                                 | 134 ms: 1.10x faster                                                     |
| tornado_http               | 103 ms                                                 | 93.3 ms: 1.10x faster                                                    |
| richards_super             | 51.5 ms                                                | 46.9 ms: 1.10x faster                                                    |
| pyflate                    | 482 ms                                                 | 439 ms: 1.10x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 707 ms: 1.10x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 81.3 ms: 1.10x faster                                                    |
| pickle_pure_python         | 324 us                                                 | 297 us: 1.09x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 56.8 ms: 1.09x faster                                                    |
| generators                 | 31.2 ms                                                | 28.8 ms: 1.09x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                     |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.08x faster                                                   |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                                     |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.07x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 100 ms: 1.07x faster                                                     |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                    |
| json_loads                 | 28.5 us                                                | 27.8 us: 1.03x faster                                                    |
| async_generators           | 463 ms                                                 | 452 ms: 1.02x faster                                                     |
| bench_thread_pool          | 842 us                                                 | 826 us: 1.02x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.65 ms: 1.02x faster                                                    |
| json                       | 5.26 ms                                                | 5.17 ms: 1.02x faster                                                    |
| sympy_str                  | 300 ms                                                 | 294 ms: 1.02x faster                                                     |
| dask                       | 372 ms                                                 | 365 ms: 1.02x faster                                                     |
| mdp                        | 2.63 sec                                               | 2.60 sec: 1.01x faster                                                   |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                     |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                     |
| 2to3                       | 274 ms                                                 | 272 ms: 1.01x faster                                                     |
| gc_traversal               | 3.79 ms                                                | 3.78 ms: 1.00x faster                                                    |
| json_dumps                 | 10.4 ms                                                | 10.4 ms: 1.00x slower                                                    |
| scimark_sor                | 129 ms                                                 | 130 ms: 1.01x slower                                                     |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                   |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                                     |
| asyncio_tcp                | 491 ms                                                 | 498 ms: 1.02x slower                                                     |
| sqlglot_optimize           | 54.8 ms                                                | 56.2 ms: 1.03x slower                                                    |
| django_template            | 34.6 ms                                                | 35.6 ms: 1.03x slower                                                    |
| hexiom                     | 6.41 ms                                                | 6.59 ms: 1.03x slower                                                    |
| nqueens                    | 83.3 ms                                                | 86.0 ms: 1.03x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                    |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.04x slower                                                     |
| sympy_integrate            | 21.4 ms                                                | 22.3 ms: 1.04x slower                                                    |
| sympy_expand               | 478 ms                                                 | 501 ms: 1.05x slower                                                     |
| docutils                   | 2.77 sec                                               | 2.91 sec: 1.05x slower                                                   |
| regex_effbot               | 3.61 ms                                                | 3.82 ms: 1.06x slower                                                    |
| go                         | 139 ms                                                 | 149 ms: 1.07x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                     |
| regex_dna                  | 212 ms                                                 | 229 ms: 1.08x slower                                                     |
| scimark_lu                 | 118 ms                                                 | 128 ms: 1.09x slower                                                     |
| telco                      | 7.10 ms                                                | 7.84 ms: 1.10x slower                                                    |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 25.8 ms: 1.11x slower                                                    |
| create_gc_cycles           | 1.48 ms                                                | 1.77 ms: 1.20x slower                                                    |
| coverage                   | 72.7 ms                                                | 93.0 ms: 1.28x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                             |

Benchmark hidden because not significant (4): sympy_sum, pycparser, bench_mp_pool, coroutines
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240727-3.14.0a0-60b7e71-JIT/bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.05x