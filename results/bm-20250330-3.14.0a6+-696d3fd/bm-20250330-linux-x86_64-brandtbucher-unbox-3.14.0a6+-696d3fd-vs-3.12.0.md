# Results vs. 3.12.0

- fork: brandtbucher
- ref: unbox
- machine: linux-x86_64
- commit hash: 696d3fd
- commit date: 2025-03-30
- overall geometric mean: 1.085x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x faster
- Memory change: 2.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                          |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.04x faster                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 605 ms: 1.96x faster                                          |
| async_tree_io              | 1.16 sec                                               | 603 ms: 1.92x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 242 ms: 1.86x faster                                          |
| async_tree_none            | 472 ms                                                 | 255 ms: 1.85x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.84x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 473 ms: 1.53x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                          |
| Geometric mean             | (ref)                                                  | 1.77x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 84.7 ms                                                | 85.4 ms: 1.01x slower                                         |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                          |
| nbody          | 97.0 ms                                                | 111 ms: 1.14x slower                                          |
| Geometric mean | (ref)                                                  | 1.05x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.10x faster                                          |
| regex_effbot   | 3.61 ms                                                | 3.32 ms: 1.09x faster                                         |
| regex_v8       | 23.1 ms                                                | 23.3 ms: 1.01x slower                                         |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                  | 1.04x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.89 sec: 1.23x faster                                        |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.12x faster                                          |
| xml_etree_iterparse  | 107 ms                                                 | 100 ms: 1.06x faster                                          |
| xml_etree_generate   | 89.2 ms                                                | 87.2 ms: 1.02x faster                                         |
| xml_etree_process    | 61.7 ms                                                | 60.7 ms: 1.02x faster                                         |
| unpickle_pure_python | 230 us                                                 | 228 us: 1.01x faster                                          |
| pickle_pure_python   | 324 us                                                 | 330 us: 1.02x slower                                          |
| json_loads           | 28.5 us                                                | 29.7 us: 1.04x slower                                         |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                         |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.18 ms: 1.18x slower                                         |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.38x slower                                         |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.7 ms: 1.06x faster                                         |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                  |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.29 sec: 2.04x faster                                        |
| async_tree_io_tg           | 1.18 sec                                               | 605 ms: 1.96x faster                                          |
| async_tree_io              | 1.16 sec                                               | 603 ms: 1.92x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 242 ms: 1.86x faster                                          |
| async_tree_none            | 472 ms                                                 | 255 ms: 1.85x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.84x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 473 ms: 1.53x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                          |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                          |
| deepcopy_memo              | 40.7 us                                                | 30.4 us: 1.34x faster                                         |
| comprehensions             | 21.8 us                                                | 17.6 us: 1.24x faster                                         |
| tomli_loads                | 2.33 sec                                               | 1.89 sec: 1.23x faster                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.23x faster                                         |
| logging_format             | 7.23 us                                                | 6.24 us: 1.16x faster                                         |
| async_generators           | 463 ms                                                 | 400 ms: 1.16x faster                                          |
| pathlib                    | 19.3 ms                                                | 16.8 ms: 1.15x faster                                         |
| go                         | 139 ms                                                 | 122 ms: 1.14x faster                                          |
| dulwich_log                | 68.5 ms                                                | 60.1 ms: 1.14x faster                                         |
| logging_simple             | 6.46 us                                                | 5.66 us: 1.14x faster                                         |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.12x faster                                          |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                          |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.11x faster                                          |
| chaos                      | 67.0 ms                                                | 60.6 ms: 1.11x faster                                         |
| regex_compile              | 148 ms                                                 | 134 ms: 1.10x faster                                          |
| raytrace                   | 312 ms                                                 | 283 ms: 1.10x faster                                          |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.0 ms: 1.10x faster                                         |
| sympy_str                  | 300 ms                                                 | 274 ms: 1.09x faster                                          |
| regex_effbot               | 3.61 ms                                                | 3.32 ms: 1.09x faster                                         |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 69.9 ms: 1.08x faster                                         |
| xml_etree_iterparse        | 107 ms                                                 | 100 ms: 1.06x faster                                          |
| pyflate                    | 482 ms                                                 | 455 ms: 1.06x faster                                          |
| django_template            | 34.6 ms                                                | 32.7 ms: 1.06x faster                                         |
| generators                 | 31.2 ms                                                | 29.7 ms: 1.05x faster                                         |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                          |
| hexiom                     | 6.41 ms                                                | 6.13 ms: 1.05x faster                                         |
| coroutines                 | 23.2 ms                                                | 22.2 ms: 1.05x faster                                         |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.04x faster                                        |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                          |
| pprint_safe_repr           | 776 ms                                                 | 747 ms: 1.04x faster                                          |
| logging_silent             | 104 ns                                                 | 101 ns: 1.04x faster                                          |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.03x faster                                        |
| sympy_expand               | 478 ms                                                 | 466 ms: 1.03x faster                                          |
| xml_etree_generate         | 89.2 ms                                                | 87.2 ms: 1.02x faster                                         |
| deltablue                  | 3.72 ms                                                | 3.65 ms: 1.02x faster                                         |
| xml_etree_process          | 61.7 ms                                                | 60.7 ms: 1.02x faster                                         |
| richards                   | 45.8 ms                                                | 45.3 ms: 1.01x faster                                         |
| unpickle_pure_python       | 230 us                                                 | 228 us: 1.01x faster                                          |
| regex_v8                   | 23.1 ms                                                | 23.3 ms: 1.01x slower                                         |
| richards_super             | 51.5 ms                                                | 51.8 ms: 1.01x slower                                         |
| float                      | 84.7 ms                                                | 85.4 ms: 1.01x slower                                         |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                          |
| crypto_pyaes               | 81.9 ms                                                | 82.9 ms: 1.01x slower                                         |
| pickle_pure_python         | 324 us                                                 | 330 us: 1.02x slower                                          |
| nqueens                    | 83.3 ms                                                | 85.5 ms: 1.03x slower                                         |
| pycparser                  | 1.18 sec                                               | 1.21 sec: 1.03x slower                                        |
| fannkuch                   | 417 ms                                                 | 431 ms: 1.03x slower                                          |
| scimark_sor                | 129 ms                                                 | 134 ms: 1.03x slower                                          |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                          |
| json_loads                 | 28.5 us                                                | 29.7 us: 1.04x slower                                         |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.05x slower                                          |
| bench_thread_pool          | 842 us                                                 | 884 us: 1.05x slower                                          |
| scimark_lu                 | 118 ms                                                 | 127 ms: 1.08x slower                                          |
| spectral_norm              | 115 ms                                                 | 127 ms: 1.10x slower                                          |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                         |
| telco                      | 7.10 ms                                                | 7.92 ms: 1.12x slower                                         |
| nbody                      | 97.0 ms                                                | 111 ms: 1.14x slower                                          |
| scimark_fft                | 382 ms                                                 | 450 ms: 1.18x slower                                          |
| python_startup_no_site     | 6.94 ms                                                | 8.18 ms: 1.18x slower                                         |
| coverage                   | 72.7 ms                                                | 86.1 ms: 1.18x slower                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.30 ms: 1.25x slower                                         |
| gc_traversal               | 3.79 ms                                                | 4.86 ms: 1.28x slower                                         |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.38x slower                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.51 ms: 1.70x slower                                         |
| bench_mp_pool              | 24.0 ms                                                | 83.7 ms: 3.49x slower                                         |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                  |

Benchmark hidden because not significant (4): sqlite_synth, mako, asyncio_websockets, json
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250330-3.14.0a6+-696d3fd/bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.085x faster

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 2.06x