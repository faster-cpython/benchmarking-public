# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_cold_16
- machine: linux-x86_64
- commit hash: 189256b
- commit date: 2024-12-04
- overall geometric mean: 1.102x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.05x faster                                                   |
| docutils       | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 609 ms: 1.94x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 623 ms: 1.86x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                   |
| async_tree_none            | 472 ms                                                 | 271 ms: 1.74x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 340 ms: 1.70x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.51x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.5 ms: 1.20x faster                                                  |
| float          | 84.7 ms                                                | 75.9 ms: 1.12x faster                                                  |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.20 ms: 1.13x faster                                                  |
| regex_v8       | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 194 us: 1.19x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 138 ms: 1.16x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 77.8 ms: 1.15x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 94.9 ms: 1.12x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 55.4 ms: 1.11x faster                                                  |
| json_loads           | 28.5 us                                                | 26.3 us: 1.08x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.01x faster                                                   |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                  |
| django_template | 34.6 ms                                                | 34.1 ms: 1.02x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 609 ms: 1.94x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 623 ms: 1.86x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                   |
| async_tree_none            | 472 ms                                                 | 271 ms: 1.74x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 340 ms: 1.70x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.51x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                                  |
| deepcopy                   | 371 us                                                 | 271 us: 1.37x faster                                                   |
| comprehensions             | 21.8 us                                                | 17.3 us: 1.26x faster                                                  |
| richards                   | 45.8 ms                                                | 37.9 ms: 1.21x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.78 us: 1.21x faster                                                  |
| richards_super             | 51.5 ms                                                | 42.8 ms: 1.21x faster                                                  |
| nbody                      | 97.0 ms                                                | 80.5 ms: 1.20x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 194 us: 1.19x faster                                                   |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 69.4 ms: 1.18x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.18 ms: 1.17x faster                                                  |
| scimark_fft                | 382 ms                                                 | 327 ms: 1.17x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 138 ms: 1.16x faster                                                   |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 65.5 ms: 1.15x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 77.8 ms: 1.15x faster                                                  |
| logging_format             | 7.23 us                                                | 6.31 us: 1.15x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.20 ms: 1.13x faster                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 94.9 ms: 1.12x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.75 us: 1.12x faster                                                  |
| float                      | 84.7 ms                                                | 75.9 ms: 1.12x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 55.4 ms: 1.11x faster                                                  |
| chaos                      | 67.0 ms                                                | 60.4 ms: 1.11x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.11x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                                   |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                                   |
| json                       | 5.26 ms                                                | 4.85 ms: 1.08x faster                                                  |
| json_loads                 | 28.5 us                                                | 26.3 us: 1.08x faster                                                  |
| raytrace                   | 312 ms                                                 | 289 ms: 1.08x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 720 ms: 1.08x faster                                                   |
| sympy_str                  | 300 ms                                                 | 281 ms: 1.07x faster                                                   |
| pyflate                    | 482 ms                                                 | 454 ms: 1.06x faster                                                   |
| fannkuch                   | 417 ms                                                 | 393 ms: 1.06x faster                                                   |
| 2to3                       | 274 ms                                                 | 260 ms: 1.05x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.05x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                 |
| go                         | 139 ms                                                 | 135 ms: 1.04x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 20.7 ms: 1.04x faster                                                  |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.04x faster                                                   |
| docutils                   | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.65 ms: 1.02x faster                                                  |
| async_generators           | 463 ms                                                 | 453 ms: 1.02x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.97 ms: 1.02x faster                                                  |
| django_template            | 34.6 ms                                                | 34.1 ms: 1.02x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.01x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                  |
| sympy_expand               | 478 ms                                                 | 474 ms: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                                   |
| sqlglot_normalize          | 110 ms                                                 | 111 ms: 1.00x slower                                                   |
| logging_silent             | 104 ns                                                 | 106 ns: 1.01x slower                                                   |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.01x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                  |
| coroutines                 | 23.2 ms                                                | 23.6 ms: 1.02x slower                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 55.9 ms: 1.02x slower                                                  |
| mdp                        | 2.63 sec                                               | 2.70 sec: 1.02x slower                                                 |
| bench_thread_pool          | 842 us                                                 | 879 us: 1.04x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                  |
| telco                      | 7.10 ms                                                | 7.53 ms: 1.06x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                   |
| nqueens                    | 83.3 ms                                                | 89.7 ms: 1.08x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                  |
| hexiom                     | 6.41 ms                                                | 7.05 ms: 1.10x slower                                                  |
| coverage                   | 72.7 ms                                                | 83.6 ms: 1.15x slower                                                  |
| generators                 | 31.2 ms                                                | 36.8 ms: 1.18x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 5.04 ms: 1.33x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.1 ms: 3.38x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (4): spectral_norm, regex_dna, dulwich_log, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241204-3.14.0a2+-189256b-JIT/bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.102x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x