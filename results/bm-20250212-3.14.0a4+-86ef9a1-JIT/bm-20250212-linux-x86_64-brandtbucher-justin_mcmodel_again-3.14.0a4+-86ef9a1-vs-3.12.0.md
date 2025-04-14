# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: linux-x86_64
- commit hash: 86ef9a1
- commit date: 2025-02-12
- overall geometric mean: 1.123x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                                         |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                       |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 618 ms: 1.91x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 620 ms: 1.87x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 325 ms: 1.77x faster                                                         |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.77x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.76x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 480 ms: 1.51x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.1 ms: 1.23x faster                                                        |
| nbody          | 97.0 ms                                                | 84.5 ms: 1.15x faster                                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.00 ms: 1.20x faster                                                        |
| regex_compile  | 148 ms                                                 | 125 ms: 1.19x faster                                                         |
| regex_dna      | 212 ms                                                 | 201 ms: 1.06x faster                                                         |
| regex_v8       | 23.1 ms                                                | 23.8 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.82 sec: 1.28x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 138 ms: 1.16x faster                                                         |
| unpickle_pure_python | 230 us                                                 | 199 us: 1.16x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 78.1 ms: 1.14x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 55.0 ms: 1.12x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 95.7 ms: 1.12x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 317 us: 1.02x faster                                                         |
| json_loads           | 28.5 us                                                | 28.9 us: 1.02x slower                                                        |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                        |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.82 ms: 1.21x faster                                                        |
| django_template | 34.6 ms                                                | 31.7 ms: 1.09x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.15x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 618 ms: 1.91x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 620 ms: 1.87x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 325 ms: 1.77x faster                                                         |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.77x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.76x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 480 ms: 1.51x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                                         |
| deepcopy                   | 371 us                                                 | 257 us: 1.45x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 30.5 us: 1.34x faster                                                        |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.82 sec: 1.28x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                        |
| scimark_fft                | 382 ms                                                 | 308 ms: 1.24x faster                                                         |
| float                      | 84.7 ms                                                | 69.1 ms: 1.23x faster                                                        |
| mako                       | 11.9 ms                                                | 9.82 ms: 1.21x faster                                                        |
| spectral_norm              | 115 ms                                                 | 95.3 ms: 1.21x faster                                                        |
| regex_effbot               | 3.61 ms                                                | 3.00 ms: 1.20x faster                                                        |
| logging_format             | 7.23 us                                                | 6.01 us: 1.20x faster                                                        |
| regex_compile              | 148 ms                                                 | 125 ms: 1.19x faster                                                         |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.49 us: 1.18x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 69.8 ms: 1.17x faster                                                        |
| chaos                      | 67.0 ms                                                | 57.5 ms: 1.17x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 138 ms: 1.16x faster                                                         |
| unpickle_pure_python       | 230 us                                                 | 199 us: 1.16x faster                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 65.5 ms: 1.15x faster                                                        |
| nbody                      | 97.0 ms                                                | 84.5 ms: 1.15x faster                                                        |
| raytrace                   | 312 ms                                                 | 273 ms: 1.14x faster                                                         |
| xml_etree_generate         | 89.2 ms                                                | 78.1 ms: 1.14x faster                                                        |
| async_generators           | 463 ms                                                 | 406 ms: 1.14x faster                                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                         |
| generators                 | 31.2 ms                                                | 27.8 ms: 1.12x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 55.0 ms: 1.12x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.7 ms: 1.12x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 95.7 ms: 1.12x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.56 ms: 1.11x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.35 ms: 1.11x faster                                                        |
| pyflate                    | 482 ms                                                 | 435 ms: 1.11x faster                                                         |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                                         |
| django_template            | 34.6 ms                                                | 31.7 ms: 1.09x faster                                                        |
| go                         | 139 ms                                                 | 128 ms: 1.09x faster                                                         |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.25 ms: 1.09x faster                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.57 ms: 1.07x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 724 ms: 1.07x faster                                                         |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                                         |
| sympy_integrate            | 21.4 ms                                                | 20.1 ms: 1.06x faster                                                        |
| fannkuch                   | 417 ms                                                 | 393 ms: 1.06x faster                                                         |
| regex_dna                  | 212 ms                                                 | 201 ms: 1.06x faster                                                         |
| sqlglot_normalize          | 110 ms                                                 | 105 ms: 1.05x faster                                                         |
| sqlite_synth               | 2.83 us                                                | 2.71 us: 1.05x faster                                                        |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                       |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                       |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                       |
| dulwich_log                | 68.5 ms                                                | 66.1 ms: 1.04x faster                                                        |
| richards                   | 45.8 ms                                                | 44.3 ms: 1.04x faster                                                        |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.04x faster                                                         |
| sqlglot_optimize           | 54.8 ms                                                | 53.2 ms: 1.03x faster                                                        |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                                       |
| sympy_expand               | 478 ms                                                 | 466 ms: 1.03x faster                                                         |
| richards_super             | 51.5 ms                                                | 50.3 ms: 1.02x faster                                                        |
| json                       | 5.26 ms                                                | 5.14 ms: 1.02x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 317 us: 1.02x faster                                                         |
| logging_silent             | 104 ns                                                 | 104 ns: 1.01x faster                                                         |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.01x slower                                                         |
| json_loads                 | 28.5 us                                                | 28.9 us: 1.02x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 23.8 ms: 1.03x slower                                                        |
| bench_thread_pool          | 842 us                                                 | 881 us: 1.05x slower                                                         |
| nqueens                    | 83.3 ms                                                | 87.8 ms: 1.05x slower                                                        |
| hexiom                     | 6.41 ms                                                | 6.83 ms: 1.07x slower                                                        |
| telco                      | 7.10 ms                                                | 7.68 ms: 1.08x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                        |
| coverage                   | 72.7 ms                                                | 88.6 ms: 1.22x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 4.81 ms: 1.27x slower                                                        |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.1 ms: 3.38x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250212-3.14.0a4+-86ef9a1-JIT/bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.123x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.11x