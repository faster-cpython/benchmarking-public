# Results vs. 3.12.0

- fork: brandtbucher
- ref: inline_class_call_de
- machine: linux-x86_64
- commit hash: 5f50be9
- commit date: 2024-07-26
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 272 ms: 1.01x faster                                                        |
| docutils       | 2.77 sec                                               | 2.91 sec: 1.05x slower                                                      |
| tornado_http   | 103 ms                                                 | 92.9 ms: 1.10x faster                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 303 ms: 1.48x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 395 ms: 1.46x faster                                                        |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 420 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 872 ms: 1.36x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 535 ms: 1.36x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 902 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 78.9 ms: 1.23x faster                                                       |
| float          | 84.7 ms                                                | 71.2 ms: 1.19x faster                                                       |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 135 ms: 1.10x faster                                                        |
| regex_effbot   | 3.61 ms                                                | 3.74 ms: 1.04x slower                                                       |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                        |
| regex_v8       | 23.1 ms                                                | 26.1 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.20x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 79.9 ms: 1.12x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 144 ms: 1.11x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 293 us: 1.11x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 56.3 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 99.2 ms: 1.08x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                                        |
| json_loads           | 28.5 us                                                | 28.0 us: 1.02x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.20 ms: 1.04x slower                                                       |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.81 ms: 1.21x faster                                                       |
| django_template | 34.6 ms                                                | 35.0 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 303 ms: 1.48x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 395 ms: 1.46x faster                                                        |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                        |
| deepcopy_memo              | 40.7 us                                                | 28.8 us: 1.41x faster                                                       |
| deepcopy                   | 371 us                                                 | 269 us: 1.38x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 420 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 872 ms: 1.36x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 535 ms: 1.36x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 902 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 60.2 ms: 1.25x faster                                                       |
| scimark_fft                | 382 ms                                                 | 307 ms: 1.24x faster                                                        |
| nbody                      | 97.0 ms                                                | 78.9 ms: 1.23x faster                                                       |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                       |
| crypto_pyaes               | 81.9 ms                                                | 67.2 ms: 1.22x faster                                                       |
| mako                       | 11.9 ms                                                | 9.81 ms: 1.21x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.20x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.81 us: 1.19x faster                                                       |
| float                      | 84.7 ms                                                | 71.2 ms: 1.19x faster                                                       |
| logging_format             | 7.23 us                                                | 6.15 us: 1.18x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.55 us: 1.16x faster                                                       |
| raytrace                   | 312 ms                                                 | 268 ms: 1.16x faster                                                        |
| chaos                      | 67.0 ms                                                | 57.7 ms: 1.16x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.40 ms: 1.15x faster                                                       |
| richards                   | 45.8 ms                                                | 40.4 ms: 1.14x faster                                                       |
| fannkuch                   | 417 ms                                                 | 368 ms: 1.13x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 79.9 ms: 1.12x faster                                                       |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.11x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 144 ms: 1.11x faster                                                        |
| richards_super             | 51.5 ms                                                | 46.6 ms: 1.11x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 293 us: 1.11x faster                                                        |
| tornado_http               | 103 ms                                                 | 92.9 ms: 1.10x faster                                                       |
| regex_compile              | 148 ms                                                 | 135 ms: 1.10x faster                                                        |
| pyflate                    | 482 ms                                                 | 438 ms: 1.10x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 706 ms: 1.10x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 56.3 ms: 1.10x faster                                                       |
| generators                 | 31.2 ms                                                | 28.7 ms: 1.09x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                 | 99.2 ms: 1.08x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.08x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                                        |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.50 ms: 1.06x faster                                                       |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                       |
| json                       | 5.26 ms                                                | 5.16 ms: 1.02x faster                                                       |
| json_loads                 | 28.5 us                                                | 28.0 us: 1.02x faster                                                       |
| dask                       | 372 ms                                                 | 365 ms: 1.02x faster                                                        |
| bench_thread_pool          | 842 us                                                 | 827 us: 1.02x faster                                                        |
| sympy_str                  | 300 ms                                                 | 295 ms: 1.02x faster                                                        |
| mdp                        | 2.63 sec                                               | 2.60 sec: 1.01x faster                                                      |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                        |
| 2to3                       | 274 ms                                                 | 272 ms: 1.01x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 168 ms: 1.01x faster                                                        |
| logging_silent             | 104 ns                                                 | 105 ns: 1.00x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                        |
| asyncio_tcp                | 491 ms                                                 | 497 ms: 1.01x slower                                                        |
| django_template            | 34.6 ms                                                | 35.0 ms: 1.01x slower                                                       |
| hexiom                     | 6.41 ms                                                | 6.52 ms: 1.02x slower                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 55.9 ms: 1.02x slower                                                       |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 3.87 ms: 1.02x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.02x slower                                                        |
| go                         | 139 ms                                                 | 144 ms: 1.03x slower                                                        |
| nqueens                    | 83.3 ms                                                | 86.2 ms: 1.04x slower                                                       |
| regex_effbot               | 3.61 ms                                                | 3.74 ms: 1.04x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.20 ms: 1.04x slower                                                       |
| sympy_integrate            | 21.4 ms                                                | 22.3 ms: 1.04x slower                                                       |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                        |
| docutils                   | 2.77 sec                                               | 2.91 sec: 1.05x slower                                                      |
| sympy_expand               | 478 ms                                                 | 502 ms: 1.05x slower                                                        |
| scimark_lu                 | 118 ms                                                 | 125 ms: 1.06x slower                                                        |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| telco                      | 7.10 ms                                                | 7.94 ms: 1.12x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 26.1 ms: 1.13x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.77 ms: 1.20x slower                                                       |
| coverage                   | 72.7 ms                                                | 92.3 ms: 1.27x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                |

Benchmark hidden because not significant (5): json_dumps, async_generators, coroutines, scimark_sor, bench_mp_pool
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240726-3.14.0a0-5f50be9-JIT/bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.05x