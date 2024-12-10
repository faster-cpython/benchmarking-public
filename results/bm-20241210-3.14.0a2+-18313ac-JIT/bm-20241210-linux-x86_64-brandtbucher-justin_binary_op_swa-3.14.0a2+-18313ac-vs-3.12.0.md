# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_binary_op_swa
- machine: linux-x86_64
- commit hash: 18313ac
- commit date: 2024-12-10
- overall geometric mean: 1.100x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                                         |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 618 ms: 1.87x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                         |
| async_tree_none            | 472 ms                                                 | 268 ms: 1.76x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 337 ms: 1.71x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 476 ms: 1.53x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.48x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 76.7 ms: 1.10x faster                                                        |
| nbody          | 97.0 ms                                                | 93.2 ms: 1.04x faster                                                        |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                         |
| regex_effbot   | 3.61 ms                                                | 3.25 ms: 1.11x faster                                                        |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                         |
| regex_v8       | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 194 us: 1.19x faster                                                         |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.15x faster                                                         |
| xml_etree_process    | 61.7 ms                                                | 55.0 ms: 1.12x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 95.8 ms: 1.12x faster                                                        |
| xml_etree_generate   | 89.2 ms                                                | 81.1 ms: 1.10x faster                                                        |
| json_loads           | 28.5 us                                                | 26.1 us: 1.09x faster                                                        |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                                 |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                        |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                        |
| django_template | 34.6 ms                                                | 33.3 ms: 1.04x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 618 ms: 1.87x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                         |
| async_tree_none            | 472 ms                                                 | 268 ms: 1.76x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 337 ms: 1.71x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 476 ms: 1.53x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.48x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 29.4 us: 1.39x faster                                                        |
| deepcopy                   | 371 us                                                 | 270 us: 1.37x faster                                                         |
| comprehensions             | 21.8 us                                                | 17.3 us: 1.26x faster                                                        |
| richards                   | 45.8 ms                                                | 36.9 ms: 1.24x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                       |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 194 us: 1.19x faster                                                         |
| crypto_pyaes               | 81.9 ms                                                | 69.3 ms: 1.18x faster                                                        |
| richards_super             | 51.5 ms                                                | 43.6 ms: 1.18x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.16 ms: 1.18x faster                                                        |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                        |
| logging_format             | 7.23 us                                                | 6.21 us: 1.16x faster                                                        |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                         |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.15x faster                                                         |
| logging_simple             | 6.46 us                                                | 5.64 us: 1.15x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 65.8 ms: 1.14x faster                                                        |
| scimark_fft                | 382 ms                                                 | 336 ms: 1.14x faster                                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 129 ms: 1.14x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.6 ms: 1.12x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 55.0 ms: 1.12x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 95.8 ms: 1.12x faster                                                        |
| regex_effbot               | 3.61 ms                                                | 3.25 ms: 1.11x faster                                                        |
| float                      | 84.7 ms                                                | 76.7 ms: 1.10x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 81.1 ms: 1.10x faster                                                        |
| json                       | 5.26 ms                                                | 4.79 ms: 1.10x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 709 ms: 1.09x faster                                                         |
| json_loads                 | 28.5 us                                                | 26.1 us: 1.09x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 156 ms: 1.08x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                       |
| chaos                      | 67.0 ms                                                | 62.3 ms: 1.08x faster                                                        |
| fannkuch                   | 417 ms                                                 | 388 ms: 1.07x faster                                                         |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.07x faster                                                         |
| sympy_str                  | 300 ms                                                 | 281 ms: 1.07x faster                                                         |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                                         |
| raytrace                   | 312 ms                                                 | 294 ms: 1.06x faster                                                         |
| pyflate                    | 482 ms                                                 | 455 ms: 1.06x faster                                                         |
| logging_silent             | 104 ns                                                 | 99.1 ns: 1.05x faster                                                        |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.04x faster                                                         |
| nbody                      | 97.0 ms                                                | 93.2 ms: 1.04x faster                                                        |
| django_template            | 34.6 ms                                                | 33.3 ms: 1.04x faster                                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                        |
| async_generators           | 463 ms                                                 | 446 ms: 1.04x faster                                                         |
| go                         | 139 ms                                                 | 135 ms: 1.04x faster                                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.04x faster                                                        |
| sympy_integrate            | 21.4 ms                                                | 20.7 ms: 1.03x faster                                                        |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                         |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                       |
| dulwich_log                | 68.5 ms                                                | 67.1 ms: 1.02x faster                                                        |
| sqlite_synth               | 2.83 us                                                | 2.78 us: 1.02x faster                                                        |
| mdp                        | 2.63 sec                                               | 2.58 sec: 1.02x faster                                                       |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                         |
| sqlglot_optimize           | 54.8 ms                                                | 55.4 ms: 1.01x slower                                                        |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                         |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                        |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.03x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 873 us: 1.04x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                         |
| telco                      | 7.10 ms                                                | 7.59 ms: 1.07x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                        |
| hexiom                     | 6.41 ms                                                | 7.00 ms: 1.09x slower                                                        |
| nqueens                    | 83.3 ms                                                | 91.1 ms: 1.09x slower                                                        |
| mypy2                      | 830 ms                                                 | 954 ms: 1.15x slower                                                         |
| generators                 | 31.2 ms                                                | 36.2 ms: 1.16x slower                                                        |
| coverage                   | 72.7 ms                                                | 85.7 ms: 1.18x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 4.60 ms: 1.21x slower                                                        |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.44 ms: 1.66x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.4 ms: 3.39x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                 |

Benchmark hidden because not significant (6): pickle_pure_python, sympy_expand, asyncio_websockets, sqlglot_normalize, scimark_sparse_mat_mult, pycparser
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241210-3.14.0a2+-18313ac-JIT/bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.100x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.12x