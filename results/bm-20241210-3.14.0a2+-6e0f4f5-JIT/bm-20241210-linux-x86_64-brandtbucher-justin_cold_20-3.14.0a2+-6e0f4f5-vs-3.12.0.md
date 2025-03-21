# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_cold_20
- machine: linux-x86_64
- commit hash: 6e0f4f5
- commit date: 2024-12-10
- overall geometric mean: 1.101x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                                   |
| docutils       | 2.77 sec                                               | 2.79 sec: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 611 ms: 1.94x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 617 ms: 1.87x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                   |
| async_tree_none            | 472 ms                                                 | 272 ms: 1.73x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 342 ms: 1.69x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.51x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 498 ms: 1.46x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 84.4 ms: 1.15x faster                                                  |
| float          | 84.7 ms                                                | 75.3 ms: 1.13x faster                                                  |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.46 ms: 1.04x faster                                                  |
| regex_dna      | 212 ms                                                 | 222 ms: 1.05x slower                                                   |
| regex_v8       | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 193 us: 1.19x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 137 ms: 1.16x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 77.7 ms: 1.15x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 94.7 ms: 1.13x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 54.9 ms: 1.12x faster                                                  |
| json_loads           | 28.5 us                                                | 26.2 us: 1.09x faster                                                  |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                           |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                  |
| django_template | 34.6 ms                                                | 33.6 ms: 1.03x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 611 ms: 1.94x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 617 ms: 1.87x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                   |
| async_tree_none            | 472 ms                                                 | 272 ms: 1.73x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 342 ms: 1.69x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.51x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 498 ms: 1.46x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                                  |
| deepcopy                   | 371 us                                                 | 276 us: 1.34x faster                                                   |
| comprehensions             | 21.8 us                                                | 17.2 us: 1.27x faster                                                  |
| richards                   | 45.8 ms                                                | 37.5 ms: 1.22x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.75 us: 1.22x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 193 us: 1.19x faster                                                   |
| richards_super             | 51.5 ms                                                | 43.4 ms: 1.19x faster                                                  |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.16 ms: 1.17x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 70.2 ms: 1.17x faster                                                  |
| scimark_fft                | 382 ms                                                 | 328 ms: 1.16x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 137 ms: 1.16x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 64.6 ms: 1.16x faster                                                  |
| nbody                      | 97.0 ms                                                | 84.4 ms: 1.15x faster                                                  |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 77.7 ms: 1.15x faster                                                  |
| logging_format             | 7.23 us                                                | 6.32 us: 1.14x faster                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.73 us: 1.13x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 94.7 ms: 1.13x faster                                                  |
| float                      | 84.7 ms                                                | 75.3 ms: 1.13x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 54.9 ms: 1.12x faster                                                  |
| chaos                      | 67.0 ms                                                | 59.7 ms: 1.12x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                  |
| json                       | 5.26 ms                                                | 4.80 ms: 1.10x faster                                                  |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                                   |
| raytrace                   | 312 ms                                                 | 286 ms: 1.09x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                                   |
| json_loads                 | 28.5 us                                                | 26.2 us: 1.09x faster                                                  |
| fannkuch                   | 417 ms                                                 | 385 ms: 1.08x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 718 ms: 1.08x faster                                                   |
| pyflate                    | 482 ms                                                 | 452 ms: 1.07x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                 |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                                   |
| sympy_str                  | 300 ms                                                 | 283 ms: 1.06x faster                                                   |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                   |
| logging_silent             | 104 ns                                                 | 99.9 ns: 1.05x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.46 ms: 1.04x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.04x faster                                                   |
| go                         | 139 ms                                                 | 134 ms: 1.04x faster                                                   |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                 |
| async_generators           | 463 ms                                                 | 446 ms: 1.04x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 20.7 ms: 1.04x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.91 ms: 1.03x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.64 ms: 1.03x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                  |
| django_template            | 34.6 ms                                                | 33.6 ms: 1.03x faster                                                  |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                   |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 67.8 ms: 1.01x faster                                                  |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                   |
| docutils                   | 2.77 sec                                               | 2.79 sec: 1.01x slower                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 55.6 ms: 1.01x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                  |
| sympy_expand               | 478 ms                                                 | 490 ms: 1.03x slower                                                   |
| mdp                        | 2.63 sec                                               | 2.71 sec: 1.03x slower                                                 |
| regex_dna                  | 212 ms                                                 | 222 ms: 1.05x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 881 us: 1.05x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                   |
| telco                      | 7.10 ms                                                | 7.52 ms: 1.06x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                  |
| nqueens                    | 83.3 ms                                                | 90.0 ms: 1.08x slower                                                  |
| hexiom                     | 6.41 ms                                                | 6.96 ms: 1.09x slower                                                  |
| coverage                   | 72.7 ms                                                | 83.7 ms: 1.15x slower                                                  |
| generators                 | 31.2 ms                                                | 36.7 ms: 1.18x slower                                                  |
| mypy2                      | 830 ms                                                 | 991 ms: 1.19x slower                                                   |
| gc_traversal               | 3.79 ms                                                | 4.78 ms: 1.26x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.4 ms: 3.39x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (4): sqlite_synth, pickle_pure_python, asyncio_websockets, sqlglot_normalize
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241210-3.14.0a2+-6e0f4f5-JIT/bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.101x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.12x