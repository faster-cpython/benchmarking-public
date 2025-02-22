# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: linux-x86_64
- commit hash: b1f0a4e
- commit date: 2024-11-14
- overall geometric mean: 1.030x faster
- HPT reliability: 99.22%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 286 ms: 1.04x slower                                                         |
| docutils       | 2.77 sec                                               | 2.96 sec: 1.07x slower                                                       |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 383 ms: 1.50x faster                                                         |
| async_tree_none            | 472 ms                                                 | 335 ms: 1.41x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 321 ms: 1.40x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 424 ms: 1.36x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 867 ms: 1.33x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 569 ms: 1.28x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 585 ms: 1.24x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 981 ms: 1.21x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.34x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 79.2 ms: 1.07x faster                                                        |
| nbody          | 97.0 ms                                                | 91.0 ms: 1.07x faster                                                        |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 143 ms: 1.04x faster                                                         |
| regex_dna      | 212 ms                                                 | 215 ms: 1.01x slower                                                         |
| regex_effbot   | 3.61 ms                                                | 3.77 ms: 1.04x slower                                                        |
| regex_v8       | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 82.8 ms: 1.08x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                                         |
| json_loads           | 28.5 us                                                | 26.8 us: 1.06x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 58.1 ms: 1.06x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 102 ms: 1.04x faster                                                         |
| unpickle_pure_python | 230 us                                                 | 224 us: 1.03x faster                                                         |
| pickle_pure_python   | 324 us                                                 | 329 us: 1.02x slower                                                         |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                        |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako           | 11.9 ms                                                | 10.9 ms: 1.09x faster                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 383 ms: 1.50x faster                                                         |
| async_tree_none            | 472 ms                                                 | 335 ms: 1.41x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 321 ms: 1.40x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 424 ms: 1.36x faster                                                         |
| deepcopy                   | 371 us                                                 | 278 us: 1.34x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 867 ms: 1.33x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 31.8 us: 1.28x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 569 ms: 1.28x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 585 ms: 1.24x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 981 ms: 1.21x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                | 2.78 us: 1.20x faster                                                        |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.20x faster                                                        |
| comprehensions             | 21.8 us                                                | 18.8 us: 1.16x faster                                                        |
| logging_format             | 7.23 us                                                | 6.26 us: 1.16x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 72.2 ms: 1.13x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.78 us: 1.12x faster                                                        |
| scimark_fft                | 382 ms                                                 | 343 ms: 1.11x faster                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 68.1 ms: 1.10x faster                                                        |
| mako                       | 11.9 ms                                                | 10.9 ms: 1.09x faster                                                        |
| raytrace                   | 312 ms                                                 | 287 ms: 1.09x faster                                                         |
| chaos                      | 67.0 ms                                                | 61.7 ms: 1.08x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 82.8 ms: 1.08x faster                                                        |
| richards_super             | 51.5 ms                                                | 48.0 ms: 1.07x faster                                                        |
| float                      | 84.7 ms                                                | 79.2 ms: 1.07x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                                         |
| nbody                      | 97.0 ms                                                | 91.0 ms: 1.07x faster                                                        |
| json_loads                 | 28.5 us                                                | 26.8 us: 1.06x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 58.1 ms: 1.06x faster                                                        |
| richards                   | 45.8 ms                                                | 43.2 ms: 1.06x faster                                                        |
| json                       | 5.26 ms                                                | 5.01 ms: 1.05x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.9 ms: 1.05x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 102 ms: 1.04x faster                                                         |
| regex_compile              | 148 ms                                                 | 143 ms: 1.04x faster                                                         |
| deltablue                  | 3.72 ms                                                | 3.61 ms: 1.03x faster                                                        |
| scimark_sor                | 129 ms                                                 | 125 ms: 1.03x faster                                                         |
| pprint_safe_repr           | 776 ms                                                 | 756 ms: 1.03x faster                                                         |
| unpickle_pure_python       | 230 us                                                 | 224 us: 1.03x faster                                                         |
| fannkuch                   | 417 ms                                                 | 407 ms: 1.03x faster                                                         |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                       |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.01 ms: 1.01x faster                                                        |
| sqlite_synth               | 2.83 us                                                | 2.81 us: 1.01x faster                                                        |
| mdp                        | 2.63 sec                                               | 2.61 sec: 1.01x faster                                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.35 ms: 1.01x faster                                                        |
| async_generators           | 463 ms                                                 | 460 ms: 1.01x faster                                                         |
| meteor_contest             | 112 ms                                                 | 112 ms: 1.01x faster                                                         |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                         |
| dulwich_log                | 68.5 ms                                                | 69.1 ms: 1.01x slower                                                        |
| pyflate                    | 482 ms                                                 | 487 ms: 1.01x slower                                                         |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.01x slower                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.59 sec: 1.01x slower                                                       |
| sqlalchemy_declarative     | 147 ms                                                 | 149 ms: 1.01x slower                                                         |
| pickle_pure_python         | 324 us                                                 | 329 us: 1.02x slower                                                         |
| sympy_str                  | 300 ms                                                 | 307 ms: 1.02x slower                                                         |
| python_startup_no_site     | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.73 ms: 1.03x slower                                                        |
| 2to3                       | 274 ms                                                 | 286 ms: 1.04x slower                                                         |
| regex_effbot               | 3.61 ms                                                | 3.77 ms: 1.04x slower                                                        |
| logging_silent             | 104 ns                                                 | 109 ns: 1.04x slower                                                         |
| sympy_sum                  | 169 ms                                                 | 178 ms: 1.05x slower                                                         |
| sympy_expand               | 478 ms                                                 | 508 ms: 1.06x slower                                                         |
| sqlglot_normalize          | 110 ms                                                 | 118 ms: 1.07x slower                                                         |
| docutils                   | 2.77 sec                                               | 2.96 sec: 1.07x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                        |
| spectral_norm              | 115 ms                                                 | 123 ms: 1.07x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 907 us: 1.08x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 171 us: 1.08x slower                                                         |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                        |
| nqueens                    | 83.3 ms                                                | 91.5 ms: 1.10x slower                                                        |
| telco                      | 7.10 ms                                                | 7.85 ms: 1.11x slower                                                        |
| sympy_integrate            | 21.4 ms                                                | 23.8 ms: 1.11x slower                                                        |
| sqlglot_optimize           | 54.8 ms                                                | 61.3 ms: 1.12x slower                                                        |
| coverage                   | 72.7 ms                                                | 84.4 ms: 1.16x slower                                                        |
| hexiom                     | 6.41 ms                                                | 7.53 ms: 1.17x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 4.52 ms: 1.19x slower                                                        |
| generators                 | 31.2 ms                                                | 39.7 ms: 1.27x slower                                                        |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.70 ms: 1.83x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 84.8 ms: 3.53x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (4): scimark_lu, go, django_template, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241114-3.14.0a1+-b1f0a4e-JIT/bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.030x faster
# HPT report

- Reliability score: 99.22% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.15x