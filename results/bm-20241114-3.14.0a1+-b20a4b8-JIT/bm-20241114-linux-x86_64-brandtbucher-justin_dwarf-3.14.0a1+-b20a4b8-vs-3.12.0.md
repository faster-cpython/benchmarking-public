# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_dwarf
- machine: linux-x86_64
- commit hash: b20a4b8
- commit date: 2024-11-14
- overall geometric mean: 1.068x slower
- HPT reliability: 57.04%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 1.29 sec: 4.71x slower                                               |
| docutils       | 2.77 sec                                               | 6.96 sec: 2.51x slower                                               |
| Geometric mean | (ref)                                                  | 3.44x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 382 ms: 1.50x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 323 ms: 1.39x faster                                                 |
| async_tree_none            | 472 ms                                                 | 339 ms: 1.39x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 422 ms: 1.37x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 870 ms: 1.33x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 561 ms: 1.29x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 579 ms: 1.25x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 980 ms: 1.21x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.34x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 89.5 ms: 1.08x faster                                                |
| float          | 84.7 ms                                                | 80.1 ms: 1.06x faster                                                |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna      | 212 ms                                                 | 214 ms: 1.01x slower                                                 |
| regex_effbot   | 3.61 ms                                                | 3.66 ms: 1.01x slower                                                |
| regex_compile  | 148 ms                                                 | 229 ms: 1.54x slower                                                 |
| regex_v8       | 23.1 ms                                                | 48.4 ms: 2.09x slower                                                |
| Geometric mean | (ref)                                                  | 1.35x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|---------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads         | 2.33 sec                                               | 2.05 sec: 1.14x faster                                               |
| xml_etree_generate  | 89.2 ms                                                | 83.1 ms: 1.07x faster                                                |
| xml_etree_parse     | 159 ms                                                 | 150 ms: 1.06x faster                                                 |
| xml_etree_process   | 61.7 ms                                                | 60.4 ms: 1.02x faster                                                |
| xml_etree_iterparse | 107 ms                                                 | 106 ms: 1.01x faster                                                 |
| json_loads          | 28.5 us                                                | 34.2 us: 1.20x slower                                                |
| json_dumps          | 10.4 ms                                                | 13.7 ms: 1.32x slower                                                |
| pickle_pure_python  | 324 us                                                 | 628 us: 1.94x slower                                                 |
| Geometric mean      | (ref)                                                  | 1.10x slower                                                         |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.7 ms: 1.11x faster                                                |
| django_template | 34.6 ms                                                | 34.3 ms: 1.01x faster                                                |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 382 ms: 1.50x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 323 ms: 1.39x faster                                                 |
| async_tree_none            | 472 ms                                                 | 339 ms: 1.39x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 422 ms: 1.37x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 870 ms: 1.33x faster                                                 |
| deepcopy                   | 371 us                                                 | 284 us: 1.30x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 561 ms: 1.29x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 31.9 us: 1.28x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 579 ms: 1.25x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 980 ms: 1.21x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 2.83 us: 1.18x faster                                                |
| comprehensions             | 21.8 us                                                | 18.8 us: 1.16x faster                                                |
| logging_format             | 7.23 us                                                | 6.31 us: 1.15x faster                                                |
| tomli_loads                | 2.33 sec                                               | 2.05 sec: 1.14x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 71.9 ms: 1.14x faster                                                |
| scimark_fft                | 382 ms                                                 | 338 ms: 1.13x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.78 us: 1.12x faster                                                |
| mako                       | 11.9 ms                                                | 10.7 ms: 1.11x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 67.9 ms: 1.11x faster                                                |
| raytrace                   | 312 ms                                                 | 286 ms: 1.09x faster                                                 |
| nbody                      | 97.0 ms                                                | 89.5 ms: 1.08x faster                                                |
| richards_super             | 51.5 ms                                                | 47.7 ms: 1.08x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 83.1 ms: 1.07x faster                                                |
| chaos                      | 67.0 ms                                                | 62.6 ms: 1.07x faster                                                |
| richards                   | 45.8 ms                                                | 42.9 ms: 1.07x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 150 ms: 1.06x faster                                                 |
| float                      | 84.7 ms                                                | 80.1 ms: 1.06x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.9 ms: 1.04x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.59 ms: 1.03x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.94 ms: 1.02x faster                                                |
| fannkuch                   | 417 ms                                                 | 407 ms: 1.02x faster                                                 |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.02x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 60.4 ms: 1.02x faster                                                |
| pprint_safe_repr           | 776 ms                                                 | 763 ms: 1.02x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                 |
| django_template            | 34.6 ms                                                | 34.3 ms: 1.01x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 106 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                 |
| async_generators           | 463 ms                                                 | 464 ms: 1.00x slower                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.58 sec: 1.01x slower                                               |
| mdp                        | 2.63 sec                                               | 2.65 sec: 1.01x slower                                               |
| regex_dna                  | 212 ms                                                 | 214 ms: 1.01x slower                                                 |
| go                         | 139 ms                                                 | 141 ms: 1.01x slower                                                 |
| regex_effbot               | 3.61 ms                                                | 3.66 ms: 1.01x slower                                                |
| sqlglot_transpile          | 1.68 ms                                                | 1.73 ms: 1.03x slower                                                |
| python_startup_no_site     | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                |
| logging_silent             | 104 ns                                                 | 111 ns: 1.06x slower                                                 |
| spectral_norm              | 115 ms                                                 | 123 ms: 1.07x slower                                                 |
| bench_thread_pool          | 842 us                                                 | 906 us: 1.08x slower                                                 |
| pycparser                  | 1.18 sec                                               | 1.28 sec: 1.09x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 172 us: 1.09x slower                                                 |
| nqueens                    | 83.3 ms                                                | 91.1 ms: 1.09x slower                                                |
| pyflate                    | 482 ms                                                 | 543 ms: 1.13x slower                                                 |
| coverage                   | 72.7 ms                                                | 83.2 ms: 1.14x slower                                                |
| sqlite_synth               | 2.83 us                                                | 3.35 us: 1.18x slower                                                |
| gc_traversal               | 3.79 ms                                                | 4.49 ms: 1.18x slower                                                |
| hexiom                     | 6.41 ms                                                | 7.65 ms: 1.19x slower                                                |
| json                       | 5.26 ms                                                | 6.27 ms: 1.19x slower                                                |
| json_loads                 | 28.5 us                                                | 34.2 us: 1.20x slower                                                |
| sympy_integrate            | 21.4 ms                                                | 26.5 ms: 1.24x slower                                                |
| sympy_expand               | 478 ms                                                 | 601 ms: 1.26x slower                                                 |
| generators                 | 31.2 ms                                                | 39.7 ms: 1.27x slower                                                |
| json_dumps                 | 10.4 ms                                                | 13.7 ms: 1.32x slower                                                |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                |
| dulwich_log                | 68.5 ms                                                | 97.0 ms: 1.42x slower                                                |
| telco                      | 7.10 ms                                                | 10.5 ms: 1.48x slower                                                |
| sympy_str                  | 300 ms                                                 | 457 ms: 1.53x slower                                                 |
| regex_compile              | 148 ms                                                 | 229 ms: 1.54x slower                                                 |
| sqlglot_normalize          | 110 ms                                                 | 197 ms: 1.78x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.69 ms: 1.82x slower                                                |
| sympy_sum                  | 169 ms                                                 | 317 ms: 1.88x slower                                                 |
| sqlalchemy_declarative     | 147 ms                                                 | 283 ms: 1.93x slower                                                 |
| pickle_pure_python         | 324 us                                                 | 628 us: 1.94x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 48.4 ms: 2.09x slower                                                |
| docutils                   | 2.77 sec                                               | 6.96 sec: 2.51x slower                                               |
| sqlglot_optimize           | 54.8 ms                                                | 142 ms: 2.58x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 108 ms: 4.50x slower                                                 |
| 2to3                       | 274 ms                                                 | 1.29 sec: 4.71x slower                                               |
| Geometric mean             | (ref)                                                  | 1.11x slower                                                         |

Benchmark hidden because not significant (5): coroutines, sqlglot_parse, meteor_contest, asyncio_websockets, unpickle_pure_python
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241114-3.14.0a1+-b20a4b8-JIT/bm-20241114-linux-x86_64-brandtbucher-justin_dwarf-3.14.0a1+-b20a4b8.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.068x slower
# HPT report

- Reliability score: 57.04% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.19x