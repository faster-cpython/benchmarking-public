# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_lto
- machine: linux-x86_64
- commit hash: f5bcb83
- commit date: 2024-12-13
- overall geometric mean: 1.086x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                               |
| docutils       | 2.77 sec                                               | 2.71 sec: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                               |
| async_tree_io              | 1.16 sec                                               | 624 ms: 1.85x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.79x faster                                               |
| async_tree_none            | 472 ms                                                 | 270 ms: 1.74x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 342 ms: 1.69x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.52x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                               |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 82.8 ms: 1.17x faster                                              |
| float          | 84.7 ms                                                | 76.1 ms: 1.11x faster                                              |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                  | 1.09x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 132 ms: 1.12x faster                                               |
| regex_effbot   | 3.61 ms                                                | 3.38 ms: 1.07x faster                                              |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                               |
| regex_v8       | 23.1 ms                                                | 24.9 ms: 1.08x slower                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.22x faster                                             |
| xml_etree_parse      | 159 ms                                                 | 137 ms: 1.17x faster                                               |
| unpickle_pure_python | 230 us                                                 | 199 us: 1.16x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 77.6 ms: 1.15x faster                                              |
| xml_etree_process    | 61.7 ms                                                | 54.9 ms: 1.12x faster                                              |
| xml_etree_iterparse  | 107 ms                                                 | 95.2 ms: 1.12x faster                                              |
| json_loads           | 28.5 us                                                | 26.2 us: 1.09x faster                                              |
| pickle_pure_python   | 324 us                                                 | 326 us: 1.01x slower                                               |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                              |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.03 ms: 1.01x slower                                              |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                              |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.4 ms: 1.15x faster                                              |
| django_template | 34.6 ms                                                | 34.2 ms: 1.01x faster                                              |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                               |
| async_tree_io              | 1.16 sec                                               | 624 ms: 1.85x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.79x faster                                               |
| async_tree_none            | 472 ms                                                 | 270 ms: 1.74x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 342 ms: 1.69x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.52x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                               |
| deepcopy_memo              | 40.7 us                                                | 29.8 us: 1.37x faster                                              |
| deepcopy                   | 371 us                                                 | 276 us: 1.35x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                              |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.22x faster                                             |
| comprehensions             | 21.8 us                                                | 18.1 us: 1.20x faster                                              |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                              |
| crypto_pyaes               | 81.9 ms                                                | 69.3 ms: 1.18x faster                                              |
| nbody                      | 97.0 ms                                                | 82.8 ms: 1.17x faster                                              |
| xml_etree_parse            | 159 ms                                                 | 137 ms: 1.17x faster                                               |
| scimark_fft                | 382 ms                                                 | 329 ms: 1.16x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 199 us: 1.16x faster                                               |
| xml_etree_generate         | 89.2 ms                                                | 77.6 ms: 1.15x faster                                              |
| mako                       | 11.9 ms                                                | 10.4 ms: 1.15x faster                                              |
| scimark_monte_carlo        | 75.1 ms                                                | 66.0 ms: 1.14x faster                                              |
| deltablue                  | 3.72 ms                                                | 3.27 ms: 1.14x faster                                              |
| xml_etree_process          | 61.7 ms                                                | 54.9 ms: 1.12x faster                                              |
| regex_compile              | 148 ms                                                 | 132 ms: 1.12x faster                                               |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 95.2 ms: 1.12x faster                                              |
| float                      | 84.7 ms                                                | 76.1 ms: 1.11x faster                                              |
| logging_format             | 7.23 us                                                | 6.55 us: 1.10x faster                                              |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.0 ms: 1.10x faster                                              |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.10x faster                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.63 ms: 1.09x faster                                              |
| logging_simple             | 6.46 us                                                | 5.92 us: 1.09x faster                                              |
| json_loads                 | 28.5 us                                                | 26.2 us: 1.09x faster                                              |
| richards                   | 45.8 ms                                                | 42.3 ms: 1.08x faster                                              |
| fannkuch                   | 417 ms                                                 | 388 ms: 1.07x faster                                               |
| json                       | 5.26 ms                                                | 4.90 ms: 1.07x faster                                              |
| regex_effbot               | 3.61 ms                                                | 3.38 ms: 1.07x faster                                              |
| sympy_sum                  | 169 ms                                                 | 159 ms: 1.07x faster                                               |
| chaos                      | 67.0 ms                                                | 62.9 ms: 1.06x faster                                              |
| pyflate                    | 482 ms                                                 | 455 ms: 1.06x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 740 ms: 1.05x faster                                               |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                               |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.04x faster                                               |
| sympy_str                  | 300 ms                                                 | 288 ms: 1.04x faster                                               |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                               |
| raytrace                   | 312 ms                                                 | 305 ms: 1.02x faster                                               |
| docutils                   | 2.77 sec                                               | 2.71 sec: 1.02x faster                                             |
| sympy_integrate            | 21.4 ms                                                | 20.9 ms: 1.02x faster                                              |
| mdp                        | 2.63 sec                                               | 2.58 sec: 1.02x faster                                             |
| pprint_pformat             | 1.57 sec                                               | 1.55 sec: 1.01x faster                                             |
| django_template            | 34.6 ms                                                | 34.2 ms: 1.01x faster                                              |
| async_generators           | 463 ms                                                 | 458 ms: 1.01x faster                                               |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                               |
| sqlglot_transpile          | 1.68 ms                                                | 1.67 ms: 1.01x faster                                              |
| sqlglot_parse              | 1.36 ms                                                | 1.35 ms: 1.01x faster                                              |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                              |
| logging_silent             | 104 ns                                                 | 104 ns: 1.00x faster                                               |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                               |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                               |
| pickle_pure_python         | 324 us                                                 | 326 us: 1.01x slower                                               |
| sqlglot_normalize          | 110 ms                                                 | 111 ms: 1.01x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 7.03 ms: 1.01x slower                                              |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                               |
| sympy_expand               | 478 ms                                                 | 490 ms: 1.03x slower                                               |
| sqlglot_optimize           | 54.8 ms                                                | 56.4 ms: 1.03x slower                                              |
| bench_thread_pool          | 842 us                                                 | 881 us: 1.05x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                               |
| nqueens                    | 83.3 ms                                                | 89.3 ms: 1.07x slower                                              |
| telco                      | 7.10 ms                                                | 7.62 ms: 1.07x slower                                              |
| regex_v8                   | 23.1 ms                                                | 24.9 ms: 1.08x slower                                              |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                              |
| go                         | 139 ms                                                 | 155 ms: 1.11x slower                                               |
| coverage                   | 72.7 ms                                                | 83.6 ms: 1.15x slower                                              |
| mypy2                      | 830 ms                                                 | 967 ms: 1.16x slower                                               |
| generators                 | 31.2 ms                                                | 37.4 ms: 1.20x slower                                              |
| gc_traversal               | 3.79 ms                                                | 4.57 ms: 1.21x slower                                              |
| hexiom                     | 6.41 ms                                                | 7.77 ms: 1.21x slower                                              |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                              |
| create_gc_cycles           | 1.48 ms                                                | 2.44 ms: 1.66x slower                                              |
| bench_mp_pool              | 24.0 ms                                                | 81.3 ms: 3.38x slower                                              |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                       |

Benchmark hidden because not significant (4): richards_super, dulwich_log, sqlite_synth, pycparser
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241213-3.14.0a2+-f5bcb83-JIT/bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.086x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.12x