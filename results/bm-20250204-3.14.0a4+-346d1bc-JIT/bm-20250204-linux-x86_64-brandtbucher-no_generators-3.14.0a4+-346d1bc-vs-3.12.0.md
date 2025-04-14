# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_generators
- machine: linux-x86_64
- commit hash: 346d1bc
- commit date: 2025-02-04
- overall geometric mean: 1.112x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 259 ms: 1.06x faster                                                  |
| docutils       | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.91x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 622 ms: 1.86x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.80x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 327 ms: 1.77x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.76x faster                                                  |
| async_tree_none            | 472 ms                                                 | 270 ms: 1.75x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.52x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.47x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 67.4 ms: 1.26x faster                                                 |
| nbody          | 97.0 ms                                                | 90.1 ms: 1.08x faster                                                 |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 2.97 ms: 1.21x faster                                                 |
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                  |
| regex_dna      | 212 ms                                                 | 194 ms: 1.09x faster                                                  |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.82 sec: 1.28x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 138 ms: 1.16x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 201 us: 1.15x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 94.6 ms: 1.13x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 79.7 ms: 1.12x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 56.1 ms: 1.10x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 315 us: 1.03x faster                                                  |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                 |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                 |
| django_template | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.91x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 622 ms: 1.86x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.80x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 327 ms: 1.77x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.76x faster                                                  |
| async_tree_none            | 472 ms                                                 | 270 ms: 1.75x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.52x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.47x faster                                                  |
| deepcopy                   | 371 us                                                 | 269 us: 1.38x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 30.6 us: 1.33x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.82 sec: 1.28x faster                                                |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                                 |
| float                      | 84.7 ms                                                | 67.4 ms: 1.26x faster                                                 |
| scimark_fft                | 382 ms                                                 | 311 ms: 1.23x faster                                                  |
| spectral_norm              | 115 ms                                                 | 93.4 ms: 1.23x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                                 |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 2.97 ms: 1.21x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 62.6 ms: 1.20x faster                                                 |
| logging_format             | 7.23 us                                                | 6.16 us: 1.17x faster                                                 |
| mako                       | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 70.1 ms: 1.17x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 138 ms: 1.16x faster                                                  |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 201 us: 1.15x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.65 us: 1.14x faster                                                 |
| async_generators           | 463 ms                                                 | 408 ms: 1.13x faster                                                  |
| scimark_sor                | 129 ms                                                 | 114 ms: 1.13x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 94.6 ms: 1.13x faster                                                 |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 79.7 ms: 1.12x faster                                                 |
| chaos                      | 67.0 ms                                                | 60.0 ms: 1.12x faster                                                 |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 56.1 ms: 1.10x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 154 ms: 1.10x faster                                                  |
| go                         | 139 ms                                                 | 127 ms: 1.10x faster                                                  |
| regex_dna                  | 212 ms                                                 | 194 ms: 1.09x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.64 ms: 1.09x faster                                                 |
| generators                 | 31.2 ms                                                | 28.8 ms: 1.08x faster                                                 |
| raytrace                   | 312 ms                                                 | 289 ms: 1.08x faster                                                  |
| nbody                      | 97.0 ms                                                | 90.1 ms: 1.08x faster                                                 |
| sympy_str                  | 300 ms                                                 | 279 ms: 1.07x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.07x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                 |
| django_template            | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                 |
| fannkuch                   | 417 ms                                                 | 393 ms: 1.06x faster                                                  |
| richards                   | 45.8 ms                                                | 43.3 ms: 1.06x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.51 ms: 1.06x faster                                                 |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                                  |
| pyflate                    | 482 ms                                                 | 460 ms: 1.05x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 741 ms: 1.05x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.04x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 20.5 ms: 1.04x faster                                                 |
| richards_super             | 51.5 ms                                                | 49.5 ms: 1.04x faster                                                 |
| sqlite_synth               | 2.83 us                                                | 2.73 us: 1.04x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 315 us: 1.03x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                |
| dulwich_log                | 68.5 ms                                                | 66.8 ms: 1.03x faster                                                 |
| json                       | 5.26 ms                                                | 5.13 ms: 1.02x faster                                                 |
| sympy_expand               | 478 ms                                                 | 470 ms: 1.02x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 53.9 ms: 1.02x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                  |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                 |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                                  |
| pycparser                  | 1.18 sec                                               | 1.21 sec: 1.03x slower                                                |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                 |
| logging_silent             | 104 ns                                                 | 109 ns: 1.04x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 892 us: 1.06x slower                                                  |
| telco                      | 7.10 ms                                                | 7.62 ms: 1.07x slower                                                 |
| nqueens                    | 83.3 ms                                                | 89.8 ms: 1.08x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.08x slower                                                 |
| hexiom                     | 6.41 ms                                                | 7.42 ms: 1.16x slower                                                 |
| coverage                   | 72.7 ms                                                | 90.7 ms: 1.25x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 4.86 ms: 1.28x slower                                                 |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.45 ms: 1.66x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 81.0 ms: 3.38x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250204-3.14.0a4+-346d1bc-JIT/bm-20250204-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-346d1bc.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.112x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.10x