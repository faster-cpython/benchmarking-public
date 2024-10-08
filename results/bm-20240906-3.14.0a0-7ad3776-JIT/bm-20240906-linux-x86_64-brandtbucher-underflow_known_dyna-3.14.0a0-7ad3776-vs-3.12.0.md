# Results vs. 3.12.0

- fork: brandtbucher
- ref: underflow_known_dyna
- machine: linux-x86_64
- commit hash: 7ad3776
- commit date: 2024-09-06
- overall geometric mean: 1.05x faster
- HPT reliability: 99.11%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 285 ms: 1.04x slower                                                        |
| docutils       | 2.77 sec                                               | 3.25 sec: 1.17x slower                                                      |
| Geometric mean | (ref)                                                  | 1.07x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 311 ms: 1.45x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 406 ms: 1.42x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 406 ms: 1.42x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 546 ms: 1.33x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 900 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 933 ms: 1.24x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.6 ms: 1.22x faster                                                       |
| float          | 84.7 ms                                                | 70.9 ms: 1.20x faster                                                       |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 151 ms: 1.02x slower                                                        |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                        |
| regex_v8       | 23.1 ms                                                | 24.6 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.00 sec: 1.16x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 77.8 ms: 1.15x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 201 us: 1.14x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 54.3 ms: 1.14x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 98.7 ms: 1.08x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                        |
| unpickle             | 15.9 us                                                | 15.1 us: 1.05x faster                                                       |
| pickle_pure_python   | 324 us                                                 | 310 us: 1.04x faster                                                        |
| pickle_dict          | 35.5 us                                                | 34.1 us: 1.04x faster                                                       |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                       |
| pickle_list          | 5.08 us                                                | 5.27 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                |

Benchmark hidden because not significant (3): unpickle_list, json_loads, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                       |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.70 ms: 1.23x faster                                                       |
| django_template | 34.6 ms                                                | 37.9 ms: 1.10x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.0 us: 1.57x faster                                                       |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 311 ms: 1.45x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 406 ms: 1.42x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 406 ms: 1.42x faster                                                        |
| deepcopy                   | 371 us                                                 | 263 us: 1.41x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 546 ms: 1.33x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 900 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.64 us: 1.27x faster                                                       |
| crypto_pyaes               | 81.9 ms                                                | 65.4 ms: 1.25x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 933 ms: 1.24x faster                                                        |
| scimark_fft                | 382 ms                                                 | 309 ms: 1.23x faster                                                        |
| mako                       | 11.9 ms                                                | 9.70 ms: 1.23x faster                                                       |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                       |
| nbody                      | 97.0 ms                                                | 79.6 ms: 1.22x faster                                                       |
| richards_super             | 51.5 ms                                                | 42.8 ms: 1.20x faster                                                       |
| float                      | 84.7 ms                                                | 70.9 ms: 1.20x faster                                                       |
| richards                   | 45.8 ms                                                | 38.4 ms: 1.19x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 2.00 sec: 1.16x faster                                                      |
| spectral_norm              | 115 ms                                                 | 99.9 ms: 1.15x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 77.8 ms: 1.15x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.24 ms: 1.15x faster                                                       |
| chaos                      | 67.0 ms                                                | 58.5 ms: 1.14x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 201 us: 1.14x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.44 ms: 1.14x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 54.3 ms: 1.14x faster                                                       |
| raytrace                   | 312 ms                                                 | 275 ms: 1.14x faster                                                        |
| logging_format             | 7.23 us                                                | 6.42 us: 1.13x faster                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 67.4 ms: 1.12x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.91 us: 1.09x faster                                                       |
| fannkuch                   | 417 ms                                                 | 382 ms: 1.09x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 98.7 ms: 1.08x faster                                                       |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                        |
| logging_silent             | 104 ns                                                 | 97.3 ns: 1.07x faster                                                       |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 738 ms: 1.05x faster                                                        |
| unpickle                   | 15.9 us                                                | 15.1 us: 1.05x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 310 us: 1.04x faster                                                        |
| pyflate                    | 482 ms                                                 | 462 ms: 1.04x faster                                                        |
| pickle_dict                | 35.5 us                                                | 34.1 us: 1.04x faster                                                       |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                      |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                                        |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.01x faster                                                       |
| go                         | 139 ms                                                 | 138 ms: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                        |
| async_generators           | 463 ms                                                 | 460 ms: 1.01x faster                                                        |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                       |
| gc_traversal               | 3.79 ms                                                | 3.78 ms: 1.00x faster                                                       |
| bench_thread_pool          | 842 us                                                 | 846 us: 1.01x slower                                                        |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                      |
| regex_compile              | 148 ms                                                 | 151 ms: 1.02x slower                                                        |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                        |
| asyncio_tcp                | 491 ms                                                 | 500 ms: 1.02x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.04x slower                                                        |
| pickle_list                | 5.08 us                                                | 5.27 us: 1.04x slower                                                       |
| 2to3                       | 274 ms                                                 | 285 ms: 1.04x slower                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.78 ms: 1.05x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 24.6 ms: 1.06x slower                                                       |
| generators                 | 31.2 ms                                                | 33.2 ms: 1.06x slower                                                       |
| sympy_str                  | 300 ms                                                 | 319 ms: 1.07x slower                                                        |
| hexiom                     | 6.41 ms                                                | 6.86 ms: 1.07x slower                                                       |
| sqlglot_normalize          | 110 ms                                                 | 119 ms: 1.08x slower                                                        |
| pycparser                  | 1.18 sec                                               | 1.27 sec: 1.08x slower                                                      |
| dulwich_log                | 68.5 ms                                                | 74.1 ms: 1.08x slower                                                       |
| django_template            | 34.6 ms                                                | 37.9 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 60.1 ms: 1.10x slower                                                       |
| telco                      | 7.10 ms                                                | 7.83 ms: 1.10x slower                                                       |
| sympy_expand               | 478 ms                                                 | 530 ms: 1.11x slower                                                        |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.52 ms: 1.11x slower                                                       |
| sympy_sum                  | 169 ms                                                 | 189 ms: 1.12x slower                                                        |
| sympy_integrate            | 21.4 ms                                                | 24.9 ms: 1.16x slower                                                       |
| docutils                   | 2.77 sec                                               | 3.25 sec: 1.17x slower                                                      |
| coverage                   | 72.7 ms                                                | 87.0 ms: 1.20x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.78 ms: 1.21x slower                                                       |
| unpack_sequence            | 54.0 ns                                                | 110 ns: 2.04x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (9): bench_mp_pool, unpickle_list, json_loads, coroutines, regex_effbot, json, pickle, nqueens, tornado_http
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240906-3.14.0a0-7ad3776-JIT/bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.11% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x