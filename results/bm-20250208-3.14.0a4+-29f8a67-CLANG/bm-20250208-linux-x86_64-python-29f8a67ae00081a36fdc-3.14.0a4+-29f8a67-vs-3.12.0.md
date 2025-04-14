# Results vs. 3.12.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-x86_64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.153x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 247 ms: 1.11x faster                                                   |
| docutils       | 2.77 sec                                               | 2.56 sec: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.92x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 605 ms: 1.91x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 310 ms: 1.86x faster                                                   |
| async_tree_none            | 472 ms                                                 | 254 ms: 1.86x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 310 ms: 1.85x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 244 ms: 1.85x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 514 ms: 1.41x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 528 ms: 1.38x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.4 ms: 1.30x faster                                                  |
| nbody          | 97.0 ms                                                | 81.8 ms: 1.19x faster                                                  |
| pidigits       | 187 ms                                                 | 212 ms: 1.13x slower                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 123 ms: 1.20x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.20 ms: 1.13x faster                                                  |
| regex_dna      | 212 ms                                                 | 197 ms: 1.08x faster                                                   |
| regex_v8       | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.90 sec: 1.23x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 57.5 ms: 1.07x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 99.7 ms: 1.07x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 84.6 ms: 1.05x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                                   |
| json_loads           | 28.5 us                                                | 30.2 us: 1.06x slower                                                  |
| json_dumps           | 10.4 ms                                                | 12.2 ms: 1.18x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.96 ms: 1.00x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.6 ms: 1.32x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.15x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 30.3 ms: 1.14x faster                                                  |
| mako            | 11.9 ms                                                | 11.5 ms: 1.04x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.92x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 605 ms: 1.91x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 310 ms: 1.86x faster                                                   |
| async_tree_none            | 472 ms                                                 | 254 ms: 1.86x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 310 ms: 1.85x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 244 ms: 1.85x faster                                                   |
| deepcopy                   | 371 us                                                 | 245 us: 1.51x faster                                                   |
| comprehensions             | 21.8 us                                                | 15.1 us: 1.44x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 28.6 us: 1.42x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 514 ms: 1.41x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 528 ms: 1.38x faster                                                   |
| spectral_norm              | 115 ms                                                 | 84.5 ms: 1.36x faster                                                  |
| pathlib                    | 19.3 ms                                                | 14.6 ms: 1.33x faster                                                  |
| scimark_fft                | 382 ms                                                 | 292 ms: 1.31x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.56 us: 1.31x faster                                                  |
| float                      | 84.7 ms                                                | 65.4 ms: 1.30x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 59.4 ms: 1.26x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.02 ms: 1.26x faster                                                  |
| logging_format             | 7.23 us                                                | 5.84 us: 1.24x faster                                                  |
| go                         | 139 ms                                                 | 113 ms: 1.23x faster                                                   |
| chaos                      | 67.0 ms                                                | 54.4 ms: 1.23x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.90 sec: 1.23x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.03 ms: 1.23x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.30 us: 1.22x faster                                                  |
| raytrace                   | 312 ms                                                 | 257 ms: 1.21x faster                                                   |
| async_generators           | 463 ms                                                 | 382 ms: 1.21x faster                                                   |
| regex_compile              | 148 ms                                                 | 123 ms: 1.20x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 68.5 ms: 1.19x faster                                                  |
| pyflate                    | 482 ms                                                 | 405 ms: 1.19x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 142 ms: 1.19x faster                                                   |
| nbody                      | 97.0 ms                                                | 81.8 ms: 1.19x faster                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 124 ms: 1.18x faster                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 15.9 ms: 1.18x faster                                                  |
| scimark_sor                | 129 ms                                                 | 110 ms: 1.18x faster                                                   |
| sympy_str                  | 300 ms                                                 | 258 ms: 1.16x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.18 ms: 1.16x faster                                                  |
| logging_silent             | 104 ns                                                 | 91.1 ns: 1.15x faster                                                  |
| django_template            | 34.6 ms                                                | 30.3 ms: 1.14x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.48 ms: 1.14x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 18.9 ms: 1.13x faster                                                  |
| generators                 | 31.2 ms                                                | 27.6 ms: 1.13x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.20 ms: 1.13x faster                                                  |
| nqueens                    | 83.3 ms                                                | 74.3 ms: 1.12x faster                                                  |
| 2to3                       | 274 ms                                                 | 247 ms: 1.11x faster                                                   |
| richards                   | 45.8 ms                                                | 41.2 ms: 1.11x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 62.0 ms: 1.11x faster                                                  |
| sympy_expand               | 478 ms                                                 | 435 ms: 1.10x faster                                                   |
| hexiom                     | 6.41 ms                                                | 5.91 ms: 1.08x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.56 sec: 1.08x faster                                                 |
| richards_super             | 51.5 ms                                                | 47.6 ms: 1.08x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 102 ms: 1.08x faster                                                   |
| fannkuch                   | 417 ms                                                 | 386 ms: 1.08x faster                                                   |
| regex_dna                  | 212 ms                                                 | 197 ms: 1.08x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 110 ms: 1.08x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 57.5 ms: 1.07x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 99.7 ms: 1.07x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 51.5 ms: 1.06x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.67 us: 1.06x faster                                                  |
| coroutines                 | 23.2 ms                                                | 21.8 ms: 1.06x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.11 sec: 1.06x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 732 ms: 1.06x faster                                                   |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 84.6 ms: 1.05x faster                                                  |
| typing_runtime_protocols   | 158 us                                                 | 150 us: 1.05x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                 |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.04x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                                   |
| bench_thread_pool          | 842 us                                                 | 826 us: 1.02x faster                                                   |
| mdp                        | 2.63 sec                                               | 2.60 sec: 1.01x faster                                                 |
| python_startup_no_site     | 6.94 ms                                                | 6.96 ms: 1.00x slower                                                  |
| telco                      | 7.10 ms                                                | 7.21 ms: 1.02x slower                                                  |
| json                       | 5.26 ms                                                | 5.39 ms: 1.03x slower                                                  |
| json_loads                 | 28.5 us                                                | 30.2 us: 1.06x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                  |
| coverage                   | 72.7 ms                                                | 79.6 ms: 1.10x slower                                                  |
| pidigits                   | 187 ms                                                 | 212 ms: 1.13x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 12.2 ms: 1.18x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.91 ms: 1.29x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.6 ms: 1.32x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.52 ms: 1.71x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 79.7 ms: 3.32x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.13x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-linux-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.153x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.10x