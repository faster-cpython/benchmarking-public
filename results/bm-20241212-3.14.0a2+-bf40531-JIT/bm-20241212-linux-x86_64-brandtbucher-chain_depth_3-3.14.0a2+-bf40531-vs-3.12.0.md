# Results vs. 3.12.0

- fork: brandtbucher
- ref: chain_depth_3
- machine: linux-x86_64
- commit hash: bf40531
- commit date: 2024-12-12
- overall geometric mean: 1.108x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                                  |
| docutils       | 2.77 sec                                               | 2.67 sec: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 607 ms: 1.95x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 621 ms: 1.86x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                  |
| async_tree_none            | 472 ms                                                 | 271 ms: 1.74x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 339 ms: 1.70x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 489 ms: 1.48x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 505 ms: 1.44x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.71x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 81.0 ms: 1.20x faster                                                 |
| float          | 84.7 ms                                                | 75.6 ms: 1.12x faster                                                 |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.47 ms: 1.04x faster                                                 |
| regex_dna      | 212 ms                                                 | 218 ms: 1.03x slower                                                  |
| regex_v8       | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.90 sec: 1.23x faster                                                |
| unpickle_pure_python | 230 us                                                 | 194 us: 1.19x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 137 ms: 1.16x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 77.3 ms: 1.15x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 54.5 ms: 1.13x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 95.0 ms: 1.12x faster                                                 |
| json_loads           | 28.5 us                                                | 26.2 us: 1.09x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 317 us: 1.02x faster                                                  |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.99 ms: 1.19x faster                                                 |
| django_template | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 607 ms: 1.95x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 621 ms: 1.86x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                  |
| async_tree_none            | 472 ms                                                 | 271 ms: 1.74x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 339 ms: 1.70x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 489 ms: 1.48x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 505 ms: 1.44x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                                 |
| deepcopy                   | 371 us                                                 | 271 us: 1.37x faster                                                  |
| comprehensions             | 21.8 us                                                | 17.2 us: 1.27x faster                                                 |
| richards                   | 45.8 ms                                                | 36.7 ms: 1.25x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.90 sec: 1.23x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.22x faster                                                 |
| richards_super             | 51.5 ms                                                | 42.6 ms: 1.21x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 68.1 ms: 1.20x faster                                                 |
| scimark_fft                | 382 ms                                                 | 318 ms: 1.20x faster                                                  |
| nbody                      | 97.0 ms                                                | 81.0 ms: 1.20x faster                                                 |
| mako                       | 11.9 ms                                                | 9.99 ms: 1.19x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 194 us: 1.19x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.17 ms: 1.17x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 64.1 ms: 1.17x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 137 ms: 1.16x faster                                                  |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                  |
| logging_format             | 7.23 us                                                | 6.25 us: 1.16x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 77.3 ms: 1.15x faster                                                 |
| chaos                      | 67.0 ms                                                | 58.8 ms: 1.14x faster                                                 |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 54.5 ms: 1.13x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.72 us: 1.13x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 95.0 ms: 1.12x faster                                                 |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.6 ms: 1.12x faster                                                 |
| float                      | 84.7 ms                                                | 75.6 ms: 1.12x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.57 ms: 1.11x faster                                                 |
| raytrace                   | 312 ms                                                 | 283 ms: 1.10x faster                                                  |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.10x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 156 ms: 1.09x faster                                                  |
| json_loads                 | 28.5 us                                                | 26.2 us: 1.09x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 715 ms: 1.08x faster                                                  |
| fannkuch                   | 417 ms                                                 | 385 ms: 1.08x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 110 ms: 1.08x faster                                                  |
| pyflate                    | 482 ms                                                 | 448 ms: 1.08x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                                |
| sympy_str                  | 300 ms                                                 | 280 ms: 1.07x faster                                                  |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                                  |
| json                       | 5.26 ms                                                | 4.92 ms: 1.07x faster                                                 |
| go                         | 139 ms                                                 | 131 ms: 1.06x faster                                                  |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.04x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 20.6 ms: 1.04x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                |
| regex_effbot               | 3.61 ms                                                | 3.47 ms: 1.04x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.04x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.67 sec: 1.03x faster                                                |
| async_generators           | 463 ms                                                 | 448 ms: 1.03x faster                                                  |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.03x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                |
| django_template            | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                 |
| logging_silent             | 104 ns                                                 | 102 ns: 1.02x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 317 us: 1.02x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 67.4 ms: 1.02x faster                                                 |
| sqlite_synth               | 2.83 us                                                | 2.81 us: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 55.4 ms: 1.01x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                 |
| regex_dna                  | 212 ms                                                 | 218 ms: 1.03x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 875 us: 1.04x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                  |
| telco                      | 7.10 ms                                                | 7.53 ms: 1.06x slower                                                 |
| nqueens                    | 83.3 ms                                                | 89.5 ms: 1.07x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                 |
| hexiom                     | 6.41 ms                                                | 6.99 ms: 1.09x slower                                                 |
| coverage                   | 72.7 ms                                                | 83.3 ms: 1.15x slower                                                 |
| mypy2                      | 830 ms                                                 | 953 ms: 1.15x slower                                                  |
| generators                 | 31.2 ms                                                | 36.1 ms: 1.16x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 4.78 ms: 1.26x slower                                                 |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 81.1 ms: 3.38x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (4): sympy_expand, coroutines, sqlglot_normalize, asyncio_websockets
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241212-3.14.0a2+-bf40531-JIT/bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.108x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.12x