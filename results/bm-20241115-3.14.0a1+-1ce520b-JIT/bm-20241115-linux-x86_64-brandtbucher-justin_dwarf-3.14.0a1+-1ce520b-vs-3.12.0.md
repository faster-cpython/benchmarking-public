# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_dwarf
- machine: linux-x86_64
- commit hash: 1ce520b
- commit date: 2024-11-15
- overall geometric mean: 1.066x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 276 ms: 1.01x slower                                                 |
| docutils       | 2.77 sec                                               | 3.00 sec: 1.08x slower                                               |
| Geometric mean | (ref)                                                  | 1.04x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 375 ms: 1.53x faster                                                 |
| async_tree_none            | 472 ms                                                 | 330 ms: 1.43x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 413 ms: 1.40x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 323 ms: 1.39x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 854 ms: 1.35x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 561 ms: 1.29x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 572 ms: 1.27x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 964 ms: 1.23x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 83.5 ms: 1.16x faster                                                |
| float          | 84.7 ms                                                | 76.4 ms: 1.11x faster                                                |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 138 ms: 1.07x faster                                                 |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                 |
| regex_effbot   | 3.61 ms                                                | 3.79 ms: 1.05x slower                                                |
| regex_v8       | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 78.6 ms: 1.13x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 54.5 ms: 1.13x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.08x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 99.9 ms: 1.07x faster                                                |
| json_loads           | 28.5 us                                                | 26.9 us: 1.06x faster                                                |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                                 |
| json_dumps           | 10.4 ms                                                | 10.7 ms: 1.03x slower                                                |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.3 ms: 1.15x faster                                                |
| django_template | 34.6 ms                                                | 33.4 ms: 1.04x faster                                                |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 375 ms: 1.53x faster                                                 |
| async_tree_none            | 472 ms                                                 | 330 ms: 1.43x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 413 ms: 1.40x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 29.2 us: 1.40x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 323 ms: 1.39x faster                                                 |
| deepcopy                   | 371 us                                                 | 271 us: 1.37x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 854 ms: 1.35x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 561 ms: 1.29x faster                                                 |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 572 ms: 1.27x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 964 ms: 1.23x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                                |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                               |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 68.9 ms: 1.19x faster                                                |
| richards                   | 45.8 ms                                                | 38.9 ms: 1.18x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 63.9 ms: 1.18x faster                                                |
| scimark_fft                | 382 ms                                                 | 326 ms: 1.17x faster                                                 |
| logging_format             | 7.23 us                                                | 6.21 us: 1.17x faster                                                |
| nbody                      | 97.0 ms                                                | 83.5 ms: 1.16x faster                                                |
| mako                       | 11.9 ms                                                | 10.3 ms: 1.15x faster                                                |
| logging_simple             | 6.46 us                                                | 5.63 us: 1.15x faster                                                |
| chaos                      | 67.0 ms                                                | 58.6 ms: 1.14x faster                                                |
| raytrace                   | 312 ms                                                 | 275 ms: 1.14x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.27 ms: 1.14x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 78.6 ms: 1.13x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 54.5 ms: 1.13x faster                                                |
| richards_super             | 51.5 ms                                                | 45.8 ms: 1.12x faster                                                |
| float                      | 84.7 ms                                                | 76.4 ms: 1.11x faster                                                |
| fannkuch                   | 417 ms                                                 | 377 ms: 1.11x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.57 ms: 1.11x faster                                                |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 713 ms: 1.09x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.08x faster                                                 |
| go                         | 139 ms                                                 | 129 ms: 1.08x faster                                                 |
| pyflate                    | 482 ms                                                 | 448 ms: 1.08x faster                                                 |
| regex_compile              | 148 ms                                                 | 138 ms: 1.07x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 99.9 ms: 1.07x faster                                                |
| json_loads                 | 28.5 us                                                | 26.9 us: 1.06x faster                                                |
| scimark_lu                 | 118 ms                                                 | 111 ms: 1.06x faster                                                 |
| json                       | 5.26 ms                                                | 4.97 ms: 1.06x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                               |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.8 ms: 1.05x faster                                                |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                 |
| logging_silent             | 104 ns                                                 | 101 ns: 1.04x faster                                                 |
| django_template            | 34.6 ms                                                | 33.4 ms: 1.04x faster                                                |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                |
| coroutines                 | 23.2 ms                                                | 22.5 ms: 1.03x faster                                                |
| sqlite_synth               | 2.83 us                                                | 2.76 us: 1.02x faster                                                |
| async_generators           | 463 ms                                                 | 454 ms: 1.02x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                               |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 68.0 ms: 1.01x faster                                                |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                 |
| sympy_str                  | 300 ms                                                 | 302 ms: 1.01x slower                                                 |
| 2to3                       | 274 ms                                                 | 276 ms: 1.01x slower                                                 |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.01x slower                                                 |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                 |
| sympy_sum                  | 169 ms                                                 | 173 ms: 1.02x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                |
| json_dumps                 | 10.4 ms                                                | 10.7 ms: 1.03x slower                                                |
| mdp                        | 2.63 sec                                               | 2.73 sec: 1.04x slower                                               |
| sqlglot_optimize           | 54.8 ms                                                | 57.4 ms: 1.05x slower                                                |
| regex_effbot               | 3.61 ms                                                | 3.79 ms: 1.05x slower                                                |
| bench_thread_pool          | 842 us                                                 | 886 us: 1.05x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                |
| sympy_expand               | 478 ms                                                 | 508 ms: 1.06x slower                                                 |
| telco                      | 7.10 ms                                                | 7.61 ms: 1.07x slower                                                |
| nqueens                    | 83.3 ms                                                | 89.3 ms: 1.07x slower                                                |
| docutils                   | 2.77 sec                                               | 3.00 sec: 1.08x slower                                               |
| sympy_integrate            | 21.4 ms                                                | 23.2 ms: 1.08x slower                                                |
| hexiom                     | 6.41 ms                                                | 6.98 ms: 1.09x slower                                                |
| generators                 | 31.2 ms                                                | 34.3 ms: 1.10x slower                                                |
| gc_traversal               | 3.79 ms                                                | 4.36 ms: 1.15x slower                                                |
| coverage                   | 72.7 ms                                                | 83.7 ms: 1.15x slower                                                |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 2.70 ms: 1.83x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 85.2 ms: 3.55x slower                                                |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                         |

Benchmark hidden because not significant (4): sqlglot_transpile, sqlalchemy_declarative, asyncio_websockets, spectral_norm
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241115-3.14.0a1+-1ce520b-JIT/bm-20241115-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-1ce520b.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.066x faster
# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.21x