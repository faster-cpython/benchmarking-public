# Results vs. 3.12.0

- fork: brandtbucher
- ref: cache_dynamic_exits
- machine: linux-x86_64
- commit hash: 55bff1c
- commit date: 2024-08-28
- overall geometric mean: 1.084x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 2.77 sec                                               | 3.05 sec: 1.10x slower                                                     |
| tornado_http   | 103 ms                                                 | 94.3 ms: 1.09x faster                                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.47x faster                                                       |
| async_tree_none            | 472 ms                                                 | 322 ms: 1.46x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 398 ms: 1.45x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 403 ms: 1.42x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 542 ms: 1.34x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 897 ms: 1.32x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 933 ms: 1.24x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.7 ms: 1.22x faster                                                      |
| float          | 84.7 ms                                                | 70.5 ms: 1.20x faster                                                      |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.14x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 143 ms: 1.04x faster                                                       |
| regex_effbot   | 3.61 ms                                                | 3.56 ms: 1.01x faster                                                      |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                                       |
| regex_v8       | 23.1 ms                                                | 24.4 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 76.6 ms: 1.16x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 54.2 ms: 1.14x faster                                                      |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 98.3 ms: 1.09x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                       |
| pickle_pure_python   | 324 us                                                 | 305 us: 1.06x faster                                                       |
| json_dumps           | 10.4 ms                                                | 9.99 ms: 1.04x faster                                                      |
| json_loads           | 28.5 us                                                | 28.6 us: 1.00x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.14 ms: 1.03x slower                                                      |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.87 ms: 1.21x faster                                                      |
| django_template | 34.6 ms                                                | 37.7 ms: 1.09x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 27.1 us: 1.50x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.47x faster                                                       |
| async_tree_none            | 472 ms                                                 | 322 ms: 1.46x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 398 ms: 1.45x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 403 ms: 1.42x faster                                                       |
| deepcopy                   | 371 us                                                 | 269 us: 1.38x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 542 ms: 1.34x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 897 ms: 1.32x faster                                                       |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 65.9 ms: 1.24x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 933 ms: 1.24x faster                                                       |
| scimark_fft                | 382 ms                                                 | 311 ms: 1.23x faster                                                       |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.22x faster                                                      |
| nbody                      | 97.0 ms                                                | 79.7 ms: 1.22x faster                                                      |
| mako                       | 11.9 ms                                                | 9.87 ms: 1.21x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                     |
| float                      | 84.7 ms                                                | 70.5 ms: 1.20x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 62.6 ms: 1.20x faster                                                      |
| logging_format             | 7.23 us                                                | 6.06 us: 1.19x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.49 us: 1.18x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 76.6 ms: 1.16x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.20 ms: 1.16x faster                                                      |
| richards                   | 45.8 ms                                                | 39.6 ms: 1.16x faster                                                      |
| chaos                      | 67.0 ms                                                | 58.4 ms: 1.15x faster                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.44 ms: 1.14x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 54.2 ms: 1.14x faster                                                      |
| richards_super             | 51.5 ms                                                | 45.4 ms: 1.13x faster                                                      |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.13x faster                                                       |
| fannkuch                   | 417 ms                                                 | 370 ms: 1.13x faster                                                       |
| raytrace                   | 312 ms                                                 | 281 ms: 1.11x faster                                                       |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                       |
| tornado_http               | 103 ms                                                 | 94.3 ms: 1.09x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 98.3 ms: 1.09x faster                                                      |
| pyflate                    | 482 ms                                                 | 445 ms: 1.08x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 726 ms: 1.07x faster                                                       |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 305 us: 1.06x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.05x faster                                                     |
| json_dumps                 | 10.4 ms                                                | 9.99 ms: 1.04x faster                                                      |
| regex_compile              | 148 ms                                                 | 143 ms: 1.04x faster                                                       |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.04x faster                                                       |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                     |
| coroutines                 | 23.2 ms                                                | 22.5 ms: 1.03x faster                                                      |
| bench_thread_pool          | 842 us                                                 | 820 us: 1.03x faster                                                       |
| scimark_sor                | 129 ms                                                 | 127 ms: 1.02x faster                                                       |
| regex_effbot               | 3.61 ms                                                | 3.56 ms: 1.01x faster                                                      |
| gc_traversal               | 3.79 ms                                                | 3.75 ms: 1.01x faster                                                      |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                       |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.35 ms: 1.01x faster                                                      |
| async_generators           | 463 ms                                                 | 461 ms: 1.00x faster                                                       |
| json_loads                 | 28.5 us                                                | 28.6 us: 1.00x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                       |
| nqueens                    | 83.3 ms                                                | 83.8 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                     |
| sqlglot_transpile          | 1.68 ms                                                | 1.71 ms: 1.02x slower                                                      |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                                       |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.03x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.14 ms: 1.03x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                       |
| sympy_integrate            | 21.4 ms                                                | 22.3 ms: 1.04x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 24.4 ms: 1.05x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 58.0 ms: 1.06x slower                                                      |
| sympy_expand               | 478 ms                                                 | 514 ms: 1.08x slower                                                       |
| hexiom                     | 6.41 ms                                                | 6.95 ms: 1.08x slower                                                      |
| generators                 | 31.2 ms                                                | 33.9 ms: 1.08x slower                                                      |
| django_template            | 34.6 ms                                                | 37.7 ms: 1.09x slower                                                      |
| telco                      | 7.10 ms                                                | 7.75 ms: 1.09x slower                                                      |
| docutils                   | 2.77 sec                                               | 3.05 sec: 1.10x slower                                                     |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                      |
| coverage                   | 72.7 ms                                                | 86.2 ms: 1.19x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 1.78 ms: 1.20x slower                                                      |
| go                         | 139 ms                                                 | 171 ms: 1.23x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                               |

Benchmark hidden because not significant (7): sympy_str, pycparser, sympy_sum, 2to3, bench_mp_pool, asyncio_tcp, json
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240828-3.14.0a0-55bff1c-JIT/bm-20240828-linux-x86_64-brandtbucher-cache_dynamic_exits-3.14.0a0-55bff1c.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.084x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.06x