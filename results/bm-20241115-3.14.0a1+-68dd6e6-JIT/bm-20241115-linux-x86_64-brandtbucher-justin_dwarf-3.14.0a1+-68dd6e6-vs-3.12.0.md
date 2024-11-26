# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_dwarf
- machine: linux-x86_64
- commit hash: 68dd6e6
- commit date: 2024-11-15
- overall geometric mean: 1.061x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 282 ms: 1.03x slower                                                 |
| docutils       | 2.77 sec                                               | 2.95 sec: 1.06x slower                                               |
| Geometric mean | (ref)                                                  | 1.05x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 380 ms: 1.51x faster                                                 |
| async_tree_none            | 472 ms                                                 | 329 ms: 1.43x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 320 ms: 1.41x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 415 ms: 1.39x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 854 ms: 1.35x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 553 ms: 1.31x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 977 ms: 1.21x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 83.2 ms: 1.17x faster                                                |
| float          | 84.7 ms                                                | 76.5 ms: 1.11x faster                                                |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 141 ms: 1.06x faster                                                 |
| regex_dna      | 212 ms                                                 | 210 ms: 1.01x faster                                                 |
| regex_effbot   | 3.61 ms                                                | 3.58 ms: 1.01x faster                                                |
| regex_v8       | 23.1 ms                                                | 25.3 ms: 1.09x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 79.1 ms: 1.13x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 56.0 ms: 1.10x faster                                                |
| json_loads           | 28.5 us                                                | 26.5 us: 1.07x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.07x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 318 us: 1.02x faster                                                 |
| json_dumps           | 10.4 ms                                                | 10.9 ms: 1.05x slower                                                |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.13 ms: 1.03x slower                                                |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.17x faster                                                |
| django_template | 34.6 ms                                                | 33.7 ms: 1.03x faster                                                |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 380 ms: 1.51x faster                                                 |
| async_tree_none            | 472 ms                                                 | 329 ms: 1.43x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 320 ms: 1.41x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 415 ms: 1.39x faster                                                 |
| deepcopy                   | 371 us                                                 | 268 us: 1.38x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                                |
| async_tree_io              | 1.16 sec                                               | 854 ms: 1.35x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 553 ms: 1.31x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                 |
| comprehensions             | 21.8 us                                                | 17.6 us: 1.24x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 977 ms: 1.21x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                               |
| scimark_fft                | 382 ms                                                 | 320 ms: 1.20x faster                                                 |
| logging_format             | 7.23 us                                                | 6.06 us: 1.19x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 68.8 ms: 1.19x faster                                                |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                |
| logging_simple             | 6.46 us                                                | 5.48 us: 1.18x faster                                                |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.17x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 64.3 ms: 1.17x faster                                                |
| nbody                      | 97.0 ms                                                | 83.2 ms: 1.17x faster                                                |
| richards                   | 45.8 ms                                                | 39.8 ms: 1.15x faster                                                |
| richards_super             | 51.5 ms                                                | 44.9 ms: 1.15x faster                                                |
| chaos                      | 67.0 ms                                                | 58.8 ms: 1.14x faster                                                |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.28 ms: 1.13x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 79.1 ms: 1.13x faster                                                |
| float                      | 84.7 ms                                                | 76.5 ms: 1.11x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 56.0 ms: 1.10x faster                                                |
| pprint_safe_repr           | 776 ms                                                 | 711 ms: 1.09x faster                                                 |
| fannkuch                   | 417 ms                                                 | 383 ms: 1.09x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                               |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                 |
| json_loads                 | 28.5 us                                                | 26.5 us: 1.07x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.07x faster                                                 |
| logging_silent             | 104 ns                                                 | 97.3 ns: 1.07x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                 |
| pyflate                    | 482 ms                                                 | 455 ms: 1.06x faster                                                 |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.6 ms: 1.06x faster                                                |
| json                       | 5.26 ms                                                | 4.97 ms: 1.06x faster                                                |
| regex_compile              | 148 ms                                                 | 141 ms: 1.06x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                                 |
| go                         | 139 ms                                                 | 133 ms: 1.05x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.86 ms: 1.04x faster                                                |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                 |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.03x faster                                                 |
| django_template            | 34.6 ms                                                | 33.7 ms: 1.03x faster                                                |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.02x faster                                                |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                |
| mdp                        | 2.63 sec                                               | 2.57 sec: 1.02x faster                                               |
| pickle_pure_python         | 324 us                                                 | 318 us: 1.02x faster                                                 |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.02x faster                                                |
| async_generators           | 463 ms                                                 | 458 ms: 1.01x faster                                                 |
| regex_dna                  | 212 ms                                                 | 210 ms: 1.01x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.58 ms: 1.01x faster                                                |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 68.2 ms: 1.00x faster                                                |
| sqlalchemy_declarative     | 147 ms                                                 | 148 ms: 1.01x slower                                                 |
| sympy_str                  | 300 ms                                                 | 304 ms: 1.02x slower                                                 |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 7.13 ms: 1.03x slower                                                |
| 2to3                       | 274 ms                                                 | 282 ms: 1.03x slower                                                 |
| sympy_sum                  | 169 ms                                                 | 176 ms: 1.04x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 10.9 ms: 1.05x slower                                                |
| sqlglot_normalize          | 110 ms                                                 | 116 ms: 1.05x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                 |
| bench_thread_pool          | 842 us                                                 | 889 us: 1.06x slower                                                 |
| sympy_expand               | 478 ms                                                 | 506 ms: 1.06x slower                                                 |
| docutils                   | 2.77 sec                                               | 2.95 sec: 1.06x slower                                               |
| nqueens                    | 83.3 ms                                                | 88.7 ms: 1.07x slower                                                |
| telco                      | 7.10 ms                                                | 7.64 ms: 1.08x slower                                                |
| regex_v8                   | 23.1 ms                                                | 25.3 ms: 1.09x slower                                                |
| sympy_integrate            | 21.4 ms                                                | 23.6 ms: 1.10x slower                                                |
| sqlglot_optimize           | 54.8 ms                                                | 60.5 ms: 1.10x slower                                                |
| hexiom                     | 6.41 ms                                                | 7.10 ms: 1.11x slower                                                |
| generators                 | 31.2 ms                                                | 35.9 ms: 1.15x slower                                                |
| coverage                   | 72.7 ms                                                | 84.3 ms: 1.16x slower                                                |
| gc_traversal               | 3.79 ms                                                | 4.73 ms: 1.25x slower                                                |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 2.70 ms: 1.83x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 85.2 ms: 3.55x slower                                                |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                         |

Benchmark hidden because not significant (2): asyncio_websockets, sqlglot_transpile
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241115-3.14.0a1+-68dd6e6-JIT/bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-68dd6e6.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.061x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.17x