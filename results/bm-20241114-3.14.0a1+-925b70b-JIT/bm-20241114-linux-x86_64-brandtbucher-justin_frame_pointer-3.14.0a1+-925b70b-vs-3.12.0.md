# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: linux-x86_64
- commit hash: 925b70b
- commit date: 2024-11-14
- overall geometric mean: 1.029x faster
- HPT reliability: 98.45%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 286 ms: 1.04x slower                                                         |
| docutils       | 2.77 sec                                               | 2.97 sec: 1.07x slower                                                       |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 381 ms: 1.51x faster                                                         |
| async_tree_none            | 472 ms                                                 | 337 ms: 1.40x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 325 ms: 1.38x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 425 ms: 1.36x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 876 ms: 1.32x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 564 ms: 1.29x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 577 ms: 1.26x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 984 ms: 1.20x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.34x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 90.0 ms: 1.08x faster                                                        |
| float          | 84.7 ms                                                | 79.1 ms: 1.07x faster                                                        |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 144 ms: 1.03x faster                                                         |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                                         |
| regex_effbot   | 3.61 ms                                                | 3.72 ms: 1.03x slower                                                        |
| regex_v8       | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.05 sec: 1.14x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 82.5 ms: 1.08x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                                         |
| xml_etree_process    | 61.7 ms                                                | 57.8 ms: 1.07x faster                                                        |
| json_loads           | 28.5 us                                                | 27.0 us: 1.06x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 102 ms: 1.05x faster                                                         |
| unpickle_pure_python | 230 us                                                 | 223 us: 1.03x faster                                                         |
| pickle_pure_python   | 324 us                                                 | 332 us: 1.02x slower                                                         |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                        |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako           | 11.9 ms                                                | 10.8 ms: 1.10x faster                                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 381 ms: 1.51x faster                                                         |
| async_tree_none            | 472 ms                                                 | 337 ms: 1.40x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 325 ms: 1.38x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 425 ms: 1.36x faster                                                         |
| deepcopy                   | 371 us                                                 | 281 us: 1.32x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 876 ms: 1.32x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 564 ms: 1.29x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 32.0 us: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 577 ms: 1.26x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 984 ms: 1.20x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                | 2.79 us: 1.20x faster                                                        |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                                        |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                        |
| comprehensions             | 21.8 us                                                | 18.8 us: 1.16x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.60 us: 1.15x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 2.05 sec: 1.14x faster                                                       |
| crypto_pyaes               | 81.9 ms                                                | 72.3 ms: 1.13x faster                                                        |
| scimark_fft                | 382 ms                                                 | 337 ms: 1.13x faster                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 67.2 ms: 1.12x faster                                                        |
| mako                       | 11.9 ms                                                | 10.8 ms: 1.10x faster                                                        |
| raytrace                   | 312 ms                                                 | 288 ms: 1.08x faster                                                         |
| chaos                      | 67.0 ms                                                | 61.9 ms: 1.08x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 82.5 ms: 1.08x faster                                                        |
| nbody                      | 97.0 ms                                                | 90.0 ms: 1.08x faster                                                        |
| richards_super             | 51.5 ms                                                | 47.9 ms: 1.08x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                                         |
| float                      | 84.7 ms                                                | 79.1 ms: 1.07x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 57.8 ms: 1.07x faster                                                        |
| richards                   | 45.8 ms                                                | 43.2 ms: 1.06x faster                                                        |
| json_loads                 | 28.5 us                                                | 27.0 us: 1.06x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.7 ms: 1.05x faster                                                        |
| json                       | 5.26 ms                                                | 5.02 ms: 1.05x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 102 ms: 1.05x faster                                                         |
| deltablue                  | 3.72 ms                                                | 3.57 ms: 1.04x faster                                                        |
| regex_compile              | 148 ms                                                 | 144 ms: 1.03x faster                                                         |
| fannkuch                   | 417 ms                                                 | 405 ms: 1.03x faster                                                         |
| unpickle_pure_python       | 230 us                                                 | 223 us: 1.03x faster                                                         |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.03x faster                                                         |
| pprint_safe_repr           | 776 ms                                                 | 760 ms: 1.02x faster                                                         |
| async_generators           | 463 ms                                                 | 455 ms: 1.02x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.97 ms: 1.02x faster                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                       |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.01x faster                                                        |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                       |
| dulwich_log                | 68.5 ms                                                | 68.1 ms: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                         |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 149 ms: 1.02x slower                                                         |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                                         |
| pickle_pure_python         | 324 us                                                 | 332 us: 1.02x slower                                                         |
| sympy_str                  | 300 ms                                                 | 307 ms: 1.02x slower                                                         |
| python_startup_no_site     | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.73 ms: 1.03x slower                                                        |
| regex_effbot               | 3.61 ms                                                | 3.72 ms: 1.03x slower                                                        |
| logging_silent             | 104 ns                                                 | 108 ns: 1.03x slower                                                         |
| 2to3                       | 274 ms                                                 | 286 ms: 1.04x slower                                                         |
| mdp                        | 2.63 sec                                               | 2.75 sec: 1.04x slower                                                       |
| sympy_sum                  | 169 ms                                                 | 178 ms: 1.05x slower                                                         |
| spectral_norm              | 115 ms                                                 | 122 ms: 1.07x slower                                                         |
| sympy_expand               | 478 ms                                                 | 510 ms: 1.07x slower                                                         |
| sqlglot_normalize          | 110 ms                                                 | 118 ms: 1.07x slower                                                         |
| regex_v8                   | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                        |
| docutils                   | 2.77 sec                                               | 2.97 sec: 1.07x slower                                                       |
| bench_thread_pool          | 842 us                                                 | 908 us: 1.08x slower                                                         |
| telco                      | 7.10 ms                                                | 7.83 ms: 1.10x slower                                                        |
| nqueens                    | 83.3 ms                                                | 92.2 ms: 1.11x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 175 us: 1.11x slower                                                         |
| sympy_integrate            | 21.4 ms                                                | 23.9 ms: 1.11x slower                                                        |
| sqlglot_optimize           | 54.8 ms                                                | 61.7 ms: 1.13x slower                                                        |
| coverage                   | 72.7 ms                                                | 84.9 ms: 1.17x slower                                                        |
| hexiom                     | 6.41 ms                                                | 7.57 ms: 1.18x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 4.64 ms: 1.22x slower                                                        |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                        |
| generators                 | 31.2 ms                                                | 41.9 ms: 1.34x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.70 ms: 1.83x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 84.6 ms: 3.52x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (7): sqlglot_parse, pyflate, sqlite_synth, go, meteor_contest, django_template, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241114-3.14.0a1+-925b70b-JIT/bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.029x faster
# HPT report

- Reliability score: 98.45% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.15x