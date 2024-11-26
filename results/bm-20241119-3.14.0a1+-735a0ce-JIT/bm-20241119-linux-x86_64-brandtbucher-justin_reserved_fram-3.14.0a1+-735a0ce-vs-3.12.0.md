# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_reserved_fram
- machine: linux-x86_64
- commit hash: 735a0ce
- commit date: 2024-11-19
- overall geometric mean: 1.058x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 279 ms: 1.02x slower                                                         |
| docutils       | 2.77 sec                                               | 2.93 sec: 1.06x slower                                                       |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 379 ms: 1.51x faster                                                         |
| async_tree_none            | 472 ms                                                 | 334 ms: 1.41x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 323 ms: 1.39x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 420 ms: 1.37x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 864 ms: 1.34x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 572 ms: 1.27x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 584 ms: 1.24x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 986 ms: 1.20x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.34x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 82.4 ms: 1.18x faster                                                        |
| float          | 84.7 ms                                                | 76.6 ms: 1.11x faster                                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 139 ms: 1.07x faster                                                         |
| regex_effbot   | 3.61 ms                                                | 3.65 ms: 1.01x slower                                                        |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                         |
| regex_v8       | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.97 sec: 1.18x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 79.1 ms: 1.13x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 55.7 ms: 1.11x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                                         |
| json_loads           | 28.5 us                                                | 26.7 us: 1.07x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                         |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.05x faster                                                         |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                        |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.17x faster                                                        |
| django_template | 34.6 ms                                                | 33.9 ms: 1.02x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 379 ms: 1.51x faster                                                         |
| async_tree_none            | 472 ms                                                 | 334 ms: 1.41x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 323 ms: 1.39x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 420 ms: 1.37x faster                                                         |
| deepcopy                   | 371 us                                                 | 272 us: 1.36x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 29.9 us: 1.36x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 864 ms: 1.34x faster                                                         |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.27x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 572 ms: 1.27x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.25x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 584 ms: 1.24x faster                                                         |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 986 ms: 1.20x faster                                                         |
| crypto_pyaes               | 81.9 ms                                                | 68.9 ms: 1.19x faster                                                        |
| scimark_fft                | 382 ms                                                 | 322 ms: 1.18x faster                                                         |
| tomli_loads                | 2.33 sec                                               | 1.97 sec: 1.18x faster                                                       |
| logging_format             | 7.23 us                                                | 6.15 us: 1.18x faster                                                        |
| nbody                      | 97.0 ms                                                | 82.4 ms: 1.18x faster                                                        |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.17x faster                                                        |
| richards                   | 45.8 ms                                                | 39.1 ms: 1.17x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 64.5 ms: 1.16x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.56 us: 1.16x faster                                                        |
| richards_super             | 51.5 ms                                                | 45.1 ms: 1.14x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.28 ms: 1.13x faster                                                        |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                         |
| xml_etree_generate         | 89.2 ms                                                | 79.1 ms: 1.13x faster                                                        |
| chaos                      | 67.0 ms                                                | 59.6 ms: 1.12x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 55.7 ms: 1.11x faster                                                        |
| float                      | 84.7 ms                                                | 76.6 ms: 1.11x faster                                                        |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                                         |
| pyflate                    | 482 ms                                                 | 443 ms: 1.09x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.65 ms: 1.09x faster                                                        |
| logging_silent             | 104 ns                                                 | 96.3 ns: 1.08x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                                         |
| regex_compile              | 148 ms                                                 | 139 ms: 1.07x faster                                                         |
| fannkuch                   | 417 ms                                                 | 390 ms: 1.07x faster                                                         |
| json_loads                 | 28.5 us                                                | 26.7 us: 1.07x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                         |
| json                       | 5.26 ms                                                | 4.98 ms: 1.06x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.05x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.7 ms: 1.05x faster                                                        |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                         |
| go                         | 139 ms                                                 | 134 ms: 1.04x faster                                                         |
| pprint_safe_repr           | 776 ms                                                 | 743 ms: 1.04x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.03x faster                                                        |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.02x faster                                                         |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                                        |
| django_template            | 34.6 ms                                                | 33.9 ms: 1.02x faster                                                        |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                        |
| async_generators           | 463 ms                                                 | 454 ms: 1.02x faster                                                         |
| mdp                        | 2.63 sec                                               | 2.58 sec: 1.02x faster                                                       |
| dulwich_log                | 68.5 ms                                                | 67.8 ms: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                                         |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.70 ms: 1.01x slower                                                        |
| regex_effbot               | 3.61 ms                                                | 3.65 ms: 1.01x slower                                                        |
| sympy_str                  | 300 ms                                                 | 304 ms: 1.01x slower                                                         |
| 2to3                       | 274 ms                                                 | 279 ms: 1.02x slower                                                         |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                        |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.03x slower                                                         |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                         |
| sympy_sum                  | 169 ms                                                 | 175 ms: 1.04x slower                                                         |
| sqlglot_normalize          | 110 ms                                                 | 116 ms: 1.05x slower                                                         |
| sympy_expand               | 478 ms                                                 | 504 ms: 1.05x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 888 us: 1.06x slower                                                         |
| nqueens                    | 83.3 ms                                                | 87.9 ms: 1.06x slower                                                        |
| docutils                   | 2.77 sec                                               | 2.93 sec: 1.06x slower                                                       |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.06x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 171 us: 1.08x slower                                                         |
| telco                      | 7.10 ms                                                | 7.69 ms: 1.08x slower                                                        |
| hexiom                     | 6.41 ms                                                | 7.00 ms: 1.09x slower                                                        |
| sympy_integrate            | 21.4 ms                                                | 23.4 ms: 1.09x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                        |
| sqlglot_optimize           | 54.8 ms                                                | 60.4 ms: 1.10x slower                                                        |
| generators                 | 31.2 ms                                                | 35.9 ms: 1.15x slower                                                        |
| coverage                   | 72.7 ms                                                | 84.0 ms: 1.16x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 4.57 ms: 1.20x slower                                                        |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.69 ms: 1.82x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 84.3 ms: 3.51x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (2): sqlalchemy_declarative, pickle_pure_python
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241119-3.14.0a1+-735a0ce-JIT/bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.058x faster
# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.15x