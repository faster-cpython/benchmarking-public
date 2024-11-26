# Results vs. 3.12.0

- fork: brandtbucher
- ref: 6de23b358e9e3dd796a2
- machine: linux-x86_64
- commit hash: 6de23b3
- commit date: 2024-11-14
- overall geometric mean: 1.044x slower
- HPT reliability: 95.43%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 1.29 sec: 4.69x slower                                                       |
| docutils       | 2.77 sec                                               | 6.92 sec: 2.50x slower                                                       |
| Geometric mean | (ref)                                                  | 3.43x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 380 ms: 1.51x faster                                                         |
| async_tree_none            | 472 ms                                                 | 335 ms: 1.41x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 322 ms: 1.40x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 418 ms: 1.38x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 865 ms: 1.34x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 569 ms: 1.27x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 586 ms: 1.24x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 978 ms: 1.21x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.34x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 82.1 ms: 1.18x faster                                                        |
| float          | 84.7 ms                                                | 77.0 ms: 1.10x faster                                                        |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.70 ms: 1.02x slower                                                        |
| regex_dna      | 212 ms                                                 | 218 ms: 1.03x slower                                                         |
| regex_compile  | 148 ms                                                 | 226 ms: 1.52x slower                                                         |
| regex_v8       | 23.1 ms                                                | 48.9 ms: 2.11x slower                                                        |
| Geometric mean | (ref)                                                  | 1.36x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 79.0 ms: 1.13x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                                         |
| xml_etree_process    | 61.7 ms                                                | 57.9 ms: 1.07x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.04x faster                                                         |
| xml_etree_iterparse  | 107 ms                                                 | 103 ms: 1.03x faster                                                         |
| json_loads           | 28.5 us                                                | 34.0 us: 1.19x slower                                                        |
| json_dumps           | 10.4 ms                                                | 13.5 ms: 1.30x slower                                                        |
| pickle_pure_python   | 324 us                                                 | 623 us: 1.92x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                        |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.0 ms: 1.18x faster                                                        |
| django_template | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 380 ms: 1.51x faster                                                         |
| async_tree_none            | 472 ms                                                 | 335 ms: 1.41x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 322 ms: 1.40x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 418 ms: 1.38x faster                                                         |
| deepcopy                   | 371 us                                                 | 271 us: 1.37x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 30.0 us: 1.36x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 865 ms: 1.34x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 569 ms: 1.27x faster                                                         |
| comprehensions             | 21.8 us                                                | 17.4 us: 1.25x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 586 ms: 1.24x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 978 ms: 1.21x faster                                                         |
| scimark_fft                | 382 ms                                                 | 317 ms: 1.20x faster                                                         |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                       |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                        |
| mako                       | 11.9 ms                                                | 10.0 ms: 1.18x faster                                                        |
| nbody                      | 97.0 ms                                                | 82.1 ms: 1.18x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 69.4 ms: 1.18x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 64.3 ms: 1.17x faster                                                        |
| logging_format             | 7.23 us                                                | 6.21 us: 1.16x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.61 us: 1.15x faster                                                        |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.47 ms: 1.13x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 79.0 ms: 1.13x faster                                                        |
| richards_super             | 51.5 ms                                                | 45.7 ms: 1.13x faster                                                        |
| chaos                      | 67.0 ms                                                | 59.7 ms: 1.12x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.32 ms: 1.12x faster                                                        |
| richards                   | 45.8 ms                                                | 41.1 ms: 1.11x faster                                                        |
| float                      | 84.7 ms                                                | 77.0 ms: 1.10x faster                                                        |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                                         |
| fannkuch                   | 417 ms                                                 | 382 ms: 1.09x faster                                                         |
| pprint_safe_repr           | 776 ms                                                 | 711 ms: 1.09x faster                                                         |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                                         |
| xml_etree_process          | 61.7 ms                                                | 57.9 ms: 1.07x faster                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.06x faster                                                       |
| logging_silent             | 104 ns                                                 | 99.1 ns: 1.05x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.8 ms: 1.05x faster                                                        |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                         |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.04x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 103 ms: 1.03x faster                                                         |
| go                         | 139 ms                                                 | 136 ms: 1.03x faster                                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.03x faster                                                        |
| django_template            | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                        |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                        |
| async_generators           | 463 ms                                                 | 459 ms: 1.01x faster                                                         |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.70 ms: 1.01x slower                                                        |
| regex_effbot               | 3.61 ms                                                | 3.70 ms: 1.02x slower                                                        |
| pycparser                  | 1.18 sec                                               | 1.21 sec: 1.03x slower                                                       |
| regex_dna                  | 212 ms                                                 | 218 ms: 1.03x slower                                                         |
| python_startup_no_site     | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                        |
| pyflate                    | 482 ms                                                 | 509 ms: 1.05x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 889 us: 1.06x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                         |
| nqueens                    | 83.3 ms                                                | 89.2 ms: 1.07x slower                                                        |
| hexiom                     | 6.41 ms                                                | 7.10 ms: 1.11x slower                                                        |
| generators                 | 31.2 ms                                                | 36.1 ms: 1.16x slower                                                        |
| coverage                   | 72.7 ms                                                | 84.1 ms: 1.16x slower                                                        |
| json                       | 5.26 ms                                                | 6.16 ms: 1.17x slower                                                        |
| sqlite_synth               | 2.83 us                                                | 3.37 us: 1.19x slower                                                        |
| json_loads                 | 28.5 us                                                | 34.0 us: 1.19x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 4.57 ms: 1.20x slower                                                        |
| sympy_integrate            | 21.4 ms                                                | 26.3 ms: 1.23x slower                                                        |
| sympy_expand               | 478 ms                                                 | 599 ms: 1.25x slower                                                         |
| json_dumps                 | 10.4 ms                                                | 13.5 ms: 1.30x slower                                                        |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                        |
| dulwich_log                | 68.5 ms                                                | 96.5 ms: 1.41x slower                                                        |
| telco                      | 7.10 ms                                                | 10.4 ms: 1.47x slower                                                        |
| regex_compile              | 148 ms                                                 | 226 ms: 1.52x slower                                                         |
| sympy_str                  | 300 ms                                                 | 457 ms: 1.52x slower                                                         |
| sqlglot_normalize          | 110 ms                                                 | 194 ms: 1.76x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.70 ms: 1.83x slower                                                        |
| sympy_sum                  | 169 ms                                                 | 317 ms: 1.88x slower                                                         |
| pickle_pure_python         | 324 us                                                 | 623 us: 1.92x slower                                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 284 ms: 1.94x slower                                                         |
| regex_v8                   | 23.1 ms                                                | 48.9 ms: 2.11x slower                                                        |
| docutils                   | 2.77 sec                                               | 6.92 sec: 2.50x slower                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 140 ms: 2.56x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 108 ms: 4.48x slower                                                         |
| 2to3                       | 274 ms                                                 | 1.29 sec: 4.69x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.08x slower                                                                 |

Benchmark hidden because not significant (4): spectral_norm, mdp, asyncio_websockets, scimark_lu
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241114-3.14.0a1+-6de23b3-JIT/bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.044x slower
# HPT report

- Reliability score: 95.43% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.19x