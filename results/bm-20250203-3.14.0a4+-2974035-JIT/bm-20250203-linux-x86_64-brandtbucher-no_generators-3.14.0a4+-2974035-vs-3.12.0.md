# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_generators
- machine: linux-x86_64
- commit hash: 2974035
- commit date: 2025-02-03
- overall geometric mean: 1.110x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                                  |
| docutils       | 2.77 sec                                               | 2.73 sec: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 627 ms: 1.84x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.82x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                  |
| async_tree_none            | 472 ms                                                 | 270 ms: 1.75x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 331 ms: 1.74x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.51x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 67.4 ms: 1.26x faster                                                 |
| nbody          | 97.0 ms                                                | 92.5 ms: 1.05x faster                                                 |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.18 ms: 1.13x faster                                                 |
| regex_dna      | 212 ms                                                 | 207 ms: 1.02x faster                                                  |
| regex_v8       | 23.1 ms                                                | 23.7 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.85 sec: 1.26x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 137 ms: 1.17x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 77.7 ms: 1.15x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 201 us: 1.15x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 54.8 ms: 1.13x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 95.3 ms: 1.12x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 315 us: 1.03x faster                                                  |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                 |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.89 ms: 1.20x faster                                                 |
| django_template | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 627 ms: 1.84x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.82x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                  |
| async_tree_none            | 472 ms                                                 | 270 ms: 1.75x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 331 ms: 1.74x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.51x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                                  |
| deepcopy                   | 371 us                                                 | 274 us: 1.35x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 30.6 us: 1.33x faster                                                 |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.85 sec: 1.26x faster                                                |
| float                      | 84.7 ms                                                | 67.4 ms: 1.26x faster                                                 |
| scimark_fft                | 382 ms                                                 | 309 ms: 1.24x faster                                                  |
| spectral_norm              | 115 ms                                                 | 94.7 ms: 1.21x faster                                                 |
| async_generators           | 463 ms                                                 | 383 ms: 1.21x faster                                                  |
| mako                       | 11.9 ms                                                | 9.89 ms: 1.20x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 63.0 ms: 1.19x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 137 ms: 1.17x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.88 us: 1.16x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 70.9 ms: 1.16x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 77.7 ms: 1.15x faster                                                 |
| logging_format             | 7.23 us                                                | 6.31 us: 1.15x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 201 us: 1.15x faster                                                  |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.18 ms: 1.13x faster                                                 |
| scimark_sor                | 129 ms                                                 | 114 ms: 1.13x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 54.8 ms: 1.13x faster                                                 |
| chaos                      | 67.0 ms                                                | 59.5 ms: 1.13x faster                                                 |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 95.3 ms: 1.12x faster                                                 |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.54 ms: 1.11x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.82 us: 1.11x faster                                                 |
| go                         | 139 ms                                                 | 127 ms: 1.10x faster                                                  |
| sympy_str                  | 300 ms                                                 | 277 ms: 1.08x faster                                                  |
| django_template            | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                 |
| raytrace                   | 312 ms                                                 | 291 ms: 1.07x faster                                                  |
| pyflate                    | 482 ms                                                 | 451 ms: 1.07x faster                                                  |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                                  |
| nqueens                    | 83.3 ms                                                | 78.2 ms: 1.07x faster                                                 |
| mdp                        | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.52 ms: 1.05x faster                                                 |
| sqlglot_normalize          | 110 ms                                                 | 105 ms: 1.05x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 20.4 ms: 1.05x faster                                                 |
| nbody                      | 97.0 ms                                                | 92.5 ms: 1.05x faster                                                 |
| sqlite_synth               | 2.83 us                                                | 2.73 us: 1.04x faster                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 52.8 ms: 1.04x faster                                                 |
| fannkuch                   | 417 ms                                                 | 402 ms: 1.04x faster                                                  |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                  |
| richards                   | 45.8 ms                                                | 44.3 ms: 1.03x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                                |
| pprint_safe_repr           | 776 ms                                                 | 750 ms: 1.03x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 315 us: 1.03x faster                                                  |
| richards_super             | 51.5 ms                                                | 50.2 ms: 1.03x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.03x faster                                                |
| regex_dna                  | 212 ms                                                 | 207 ms: 1.02x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 67.0 ms: 1.02x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                  |
| sympy_expand               | 478 ms                                                 | 471 ms: 1.02x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.73 sec: 1.01x faster                                                |
| json                       | 5.26 ms                                                | 5.21 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 23.7 ms: 1.03x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 881 us: 1.05x slower                                                  |
| telco                      | 7.10 ms                                                | 7.56 ms: 1.07x slower                                                 |
| logging_silent             | 104 ns                                                 | 112 ns: 1.07x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                 |
| hexiom                     | 6.41 ms                                                | 7.19 ms: 1.12x slower                                                 |
| generators                 | 31.2 ms                                                | 37.1 ms: 1.19x slower                                                 |
| coverage                   | 72.7 ms                                                | 91.5 ms: 1.26x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 4.94 ms: 1.30x slower                                                 |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 80.1 ms: 3.34x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250203-3.14.0a4+-2974035-JIT/bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.110x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.10x