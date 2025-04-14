# Results vs. 3.12.0

- fork: brandtbucher
- ref: compact_alt
- machine: linux-x86_64
- commit hash: d1a7426
- commit date: 2025-02-11
- overall geometric mean: 1.085x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4+-d1a7426 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                                |
| docutils       | 2.77 sec                                               | 2.71 sec: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4+-d1a7426 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 641 ms: 1.85x faster                                                |
| async_tree_io              | 1.16 sec                                               | 637 ms: 1.82x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 334 ms: 1.72x faster                                                |
| async_tree_none            | 472 ms                                                 | 275 ms: 1.71x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 340 ms: 1.70x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 268 ms: 1.67x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 504 ms: 1.44x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 511 ms: 1.42x faster                                                |
| Geometric mean             | (ref)                                                  | 1.66x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4+-d1a7426 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 75.5 ms: 1.12x faster                                               |
| nbody          | 97.0 ms                                                | 93.7 ms: 1.03x faster                                               |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4+-d1a7426 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.18x faster                                                |
| regex_effbot   | 3.61 ms                                                | 3.11 ms: 1.16x faster                                               |
| regex_dna      | 212 ms                                                 | 210 ms: 1.01x faster                                                |
| regex_v8       | 23.1 ms                                                | 24.2 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4+-d1a7426 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.85 sec: 1.26x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 81.2 ms: 1.10x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 58.6 ms: 1.05x faster                                               |
| unpickle_pure_python | 230 us                                                 | 223 us: 1.03x faster                                                |
| json_loads           | 28.5 us                                                | 28.6 us: 1.00x slower                                               |
| pickle_pure_python   | 324 us                                                 | 330 us: 1.02x slower                                                |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.11x slower                                               |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4+-d1a7426 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                               |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                               |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4+-d1a7426 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                               |
| django_template | 34.6 ms                                                | 33.5 ms: 1.03x faster                                               |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4+-d1a7426 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 641 ms: 1.85x faster                                                |
| async_tree_io              | 1.16 sec                                               | 637 ms: 1.82x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 334 ms: 1.72x faster                                                |
| async_tree_none            | 472 ms                                                 | 275 ms: 1.71x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 340 ms: 1.70x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 268 ms: 1.67x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 504 ms: 1.44x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 511 ms: 1.42x faster                                                |
| deepcopy                   | 371 us                                                 | 282 us: 1.32x faster                                                |
| tomli_loads                | 2.33 sec                                               | 1.85 sec: 1.26x faster                                              |
| comprehensions             | 21.8 us                                                | 17.3 us: 1.26x faster                                               |
| deepcopy_memo              | 40.7 us                                                | 32.5 us: 1.25x faster                                               |
| scimark_fft                | 382 ms                                                 | 315 ms: 1.21x faster                                                |
| regex_compile              | 148 ms                                                 | 125 ms: 1.18x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 2.83 us: 1.18x faster                                               |
| logging_format             | 7.23 us                                                | 6.14 us: 1.18x faster                                               |
| regex_effbot               | 3.61 ms                                                | 3.11 ms: 1.16x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 70.6 ms: 1.16x faster                                               |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                               |
| async_generators           | 463 ms                                                 | 404 ms: 1.15x faster                                                |
| logging_simple             | 6.46 us                                                | 5.64 us: 1.15x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                |
| go                         | 139 ms                                                 | 124 ms: 1.13x faster                                                |
| float                      | 84.7 ms                                                | 75.5 ms: 1.12x faster                                               |
| raytrace                   | 312 ms                                                 | 280 ms: 1.11x faster                                                |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.0 ms: 1.10x faster                                               |
| xml_etree_generate         | 89.2 ms                                                | 81.2 ms: 1.10x faster                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.62 ms: 1.10x faster                                               |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                                |
| chaos                      | 67.0 ms                                                | 61.9 ms: 1.08x faster                                               |
| spectral_norm              | 115 ms                                                 | 107 ms: 1.08x faster                                                |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 70.4 ms: 1.07x faster                                               |
| sympy_str                  | 300 ms                                                 | 281 ms: 1.07x faster                                                |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                |
| pyflate                    | 482 ms                                                 | 457 ms: 1.06x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 58.6 ms: 1.05x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.54 ms: 1.05x faster                                               |
| sympy_integrate            | 21.4 ms                                                | 20.5 ms: 1.05x faster                                               |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                               |
| nbody                      | 97.0 ms                                                | 93.7 ms: 1.03x faster                                               |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.03x faster                                               |
| django_template            | 34.6 ms                                                | 33.5 ms: 1.03x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 223 us: 1.03x faster                                                |
| mdp                        | 2.63 sec                                               | 2.57 sec: 1.03x faster                                              |
| docutils                   | 2.77 sec                                               | 2.71 sec: 1.02x faster                                              |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                               |
| json                       | 5.26 ms                                                | 5.17 ms: 1.02x faster                                               |
| scimark_sor                | 129 ms                                                 | 127 ms: 1.02x faster                                                |
| dulwich_log                | 68.5 ms                                                | 67.5 ms: 1.01x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 765 ms: 1.01x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.55 sec: 1.01x faster                                              |
| generators                 | 31.2 ms                                                | 30.9 ms: 1.01x faster                                               |
| fannkuch                   | 417 ms                                                 | 413 ms: 1.01x faster                                                |
| regex_dna                  | 212 ms                                                 | 210 ms: 1.01x faster                                                |
| json_loads                 | 28.5 us                                                | 28.6 us: 1.00x slower                                               |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                |
| sqlglot_optimize           | 54.8 ms                                                | 55.5 ms: 1.01x slower                                               |
| sympy_expand               | 478 ms                                                 | 484 ms: 1.01x slower                                                |
| pickle_pure_python         | 324 us                                                 | 330 us: 1.02x slower                                                |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                               |
| hexiom                     | 6.41 ms                                                | 6.61 ms: 1.03x slower                                               |
| coroutines                 | 23.2 ms                                                | 23.9 ms: 1.03x slower                                               |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.03x slower                                                |
| regex_v8                   | 23.1 ms                                                | 24.2 ms: 1.05x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                |
| nqueens                    | 83.3 ms                                                | 88.0 ms: 1.06x slower                                               |
| bench_thread_pool          | 842 us                                                 | 898 us: 1.07x slower                                                |
| telco                      | 7.10 ms                                                | 7.61 ms: 1.07x slower                                               |
| scimark_lu                 | 118 ms                                                 | 129 ms: 1.09x slower                                                |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.11x slower                                               |
| coverage                   | 72.7 ms                                                | 89.6 ms: 1.23x slower                                               |
| logging_silent             | 104 ns                                                 | 134 ns: 1.28x slower                                                |
| gc_traversal               | 3.79 ms                                                | 5.05 ms: 1.33x slower                                               |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.69x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 81.4 ms: 3.39x slower                                               |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (3): richards, asyncio_websockets, richards_super
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pycparser, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250211-3.14.0a4+-d1a7426-JIT/bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4+-d1a7426.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.085x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.11x