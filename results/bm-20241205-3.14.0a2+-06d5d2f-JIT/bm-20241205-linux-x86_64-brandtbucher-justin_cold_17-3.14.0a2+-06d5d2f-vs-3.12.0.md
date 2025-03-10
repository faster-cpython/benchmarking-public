# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_cold_17
- machine: linux-x86_64
- commit hash: 06d5d2f
- commit date: 2024-12-05
- overall geometric mean: 1.106x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_17-3.14.0a2+-06d5d2f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                                   |
| docutils       | 2.77 sec                                               | 2.70 sec: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_17-3.14.0a2+-06d5d2f |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 620 ms: 1.86x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.77x faster                                                   |
| async_tree_none            | 472 ms                                                 | 272 ms: 1.73x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 342 ms: 1.69x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 484 ms: 1.50x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 499 ms: 1.45x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.71x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_17-3.14.0a2+-06d5d2f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 83.1 ms: 1.17x faster                                                  |
| float          | 84.7 ms                                                | 75.5 ms: 1.12x faster                                                  |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_17-3.14.0a2+-06d5d2f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.43 ms: 1.05x faster                                                  |
| regex_dna      | 212 ms                                                 | 213 ms: 1.00x slower                                                   |
| regex_v8       | 23.1 ms                                                | 24.9 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_17-3.14.0a2+-06d5d2f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 194 us: 1.19x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 137 ms: 1.17x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 78.5 ms: 1.14x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 94.8 ms: 1.13x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 55.0 ms: 1.12x faster                                                  |
| json_loads           | 28.5 us                                                | 26.1 us: 1.09x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 318 us: 1.02x faster                                                   |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_17-3.14.0a2+-06d5d2f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_17-3.14.0a2+-06d5d2f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.0 ms: 1.18x faster                                                  |
| django_template | 34.6 ms                                                | 33.9 ms: 1.02x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_17-3.14.0a2+-06d5d2f |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 620 ms: 1.86x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.77x faster                                                   |
| async_tree_none            | 472 ms                                                 | 272 ms: 1.73x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 342 ms: 1.69x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 484 ms: 1.50x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 499 ms: 1.45x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 28.8 us: 1.41x faster                                                  |
| deepcopy                   | 371 us                                                 | 268 us: 1.38x faster                                                   |
| comprehensions             | 21.8 us                                                | 17.3 us: 1.26x faster                                                  |
| richards                   | 45.8 ms                                                | 36.6 ms: 1.25x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.75 us: 1.22x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 68.6 ms: 1.19x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 194 us: 1.19x faster                                                   |
| richards_super             | 51.5 ms                                                | 43.5 ms: 1.19x faster                                                  |
| mako                       | 11.9 ms                                                | 10.0 ms: 1.18x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                  |
| scimark_fft                | 382 ms                                                 | 326 ms: 1.17x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.17 ms: 1.17x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 137 ms: 1.17x faster                                                   |
| nbody                      | 97.0 ms                                                | 83.1 ms: 1.17x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 64.8 ms: 1.16x faster                                                  |
| logging_format             | 7.23 us                                                | 6.26 us: 1.16x faster                                                  |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                   |
| chaos                      | 67.0 ms                                                | 58.6 ms: 1.14x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 78.5 ms: 1.14x faster                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 129 ms: 1.13x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 94.8 ms: 1.13x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.74 us: 1.12x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.6 ms: 1.12x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 55.0 ms: 1.12x faster                                                  |
| float                      | 84.7 ms                                                | 75.5 ms: 1.12x faster                                                  |
| raytrace                   | 312 ms                                                 | 283 ms: 1.10x faster                                                   |
| json                       | 5.26 ms                                                | 4.78 ms: 1.10x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 708 ms: 1.10x faster                                                   |
| json_loads                 | 28.5 us                                                | 26.1 us: 1.09x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 156 ms: 1.08x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                 |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                   |
| fannkuch                   | 417 ms                                                 | 388 ms: 1.08x faster                                                   |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                                   |
| sympy_str                  | 300 ms                                                 | 282 ms: 1.06x faster                                                   |
| go                         | 139 ms                                                 | 132 ms: 1.06x faster                                                   |
| pyflate                    | 482 ms                                                 | 458 ms: 1.05x faster                                                   |
| regex_effbot               | 3.61 ms                                                | 3.43 ms: 1.05x faster                                                  |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                   |
| logging_silent             | 104 ns                                                 | 99.8 ns: 1.05x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.84 ms: 1.05x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.04x faster                                                   |
| async_generators           | 463 ms                                                 | 446 ms: 1.04x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 20.6 ms: 1.04x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.03x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.70 sec: 1.02x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                 |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 318 us: 1.02x faster                                                   |
| django_template            | 34.6 ms                                                | 33.9 ms: 1.02x faster                                                  |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 67.4 ms: 1.02x faster                                                  |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| regex_dna                  | 212 ms                                                 | 213 ms: 1.00x slower                                                   |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.01x slower                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 55.7 ms: 1.02x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 873 us: 1.04x slower                                                   |
| mdp                        | 2.63 sec                                               | 2.75 sec: 1.04x slower                                                 |
| telco                      | 7.10 ms                                                | 7.52 ms: 1.06x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 24.9 ms: 1.08x slower                                                  |
| hexiom                     | 6.41 ms                                                | 6.99 ms: 1.09x slower                                                  |
| nqueens                    | 83.3 ms                                                | 90.9 ms: 1.09x slower                                                  |
| coverage                   | 72.7 ms                                                | 83.9 ms: 1.15x slower                                                  |
| generators                 | 31.2 ms                                                | 36.2 ms: 1.16x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.88 ms: 1.29x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.3 ms: 3.38x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (3): sympy_expand, sqlglot_normalize, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241205-3.14.0a2+-06d5d2f-JIT/bm-20241205-linux-x86_64-brandtbucher-justin_cold_17-3.14.0a2+-06d5d2f.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.106x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x