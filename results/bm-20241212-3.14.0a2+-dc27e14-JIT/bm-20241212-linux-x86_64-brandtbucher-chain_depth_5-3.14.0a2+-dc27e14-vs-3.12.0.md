# Results vs. 3.12.0

- fork: brandtbucher
- ref: chain_depth_5
- machine: linux-x86_64
- commit hash: dc27e14
- commit date: 2024-12-12
- overall geometric mean: 1.101x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                                  |
| docutils       | 2.77 sec                                               | 2.71 sec: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 602 ms: 1.96x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 617 ms: 1.88x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.84x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                  |
| async_tree_none            | 472 ms                                                 | 271 ms: 1.74x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 340 ms: 1.70x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.52x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.5 ms: 1.21x faster                                                 |
| float          | 84.7 ms                                                | 76.0 ms: 1.11x faster                                                 |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.39 ms: 1.06x faster                                                 |
| regex_dna      | 212 ms                                                 | 215 ms: 1.02x slower                                                  |
| regex_v8       | 23.1 ms                                                | 24.9 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                |
| unpickle_pure_python | 230 us                                                 | 195 us: 1.18x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 138 ms: 1.16x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 78.0 ms: 1.14x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 95.2 ms: 1.12x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 55.4 ms: 1.11x faster                                                 |
| json_loads           | 28.5 us                                                | 26.1 us: 1.09x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 315 us: 1.03x faster                                                  |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.07x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                 |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.3 ms: 1.15x faster                                                 |
| django_template | 34.6 ms                                                | 33.9 ms: 1.02x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 602 ms: 1.96x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 617 ms: 1.88x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.84x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                  |
| async_tree_none            | 472 ms                                                 | 271 ms: 1.74x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 340 ms: 1.70x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.52x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.1 us: 1.40x faster                                                 |
| deepcopy                   | 371 us                                                 | 272 us: 1.36x faster                                                  |
| comprehensions             | 21.8 us                                                | 17.4 us: 1.25x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.23x faster                                                 |
| richards                   | 45.8 ms                                                | 37.6 ms: 1.22x faster                                                 |
| nbody                      | 97.0 ms                                                | 80.5 ms: 1.21x faster                                                 |
| richards_super             | 51.5 ms                                                | 43.1 ms: 1.20x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 68.5 ms: 1.20x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 195 us: 1.18x faster                                                  |
| scimark_fft                | 382 ms                                                 | 325 ms: 1.18x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 64.3 ms: 1.17x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.19 ms: 1.17x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 138 ms: 1.16x faster                                                  |
| logging_format             | 7.23 us                                                | 6.24 us: 1.16x faster                                                 |
| mako                       | 11.9 ms                                                | 10.3 ms: 1.15x faster                                                 |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 78.0 ms: 1.14x faster                                                 |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.74 us: 1.13x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 95.2 ms: 1.12x faster                                                 |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.12x faster                                                 |
| float                      | 84.7 ms                                                | 76.0 ms: 1.11x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 55.4 ms: 1.11x faster                                                 |
| chaos                      | 67.0 ms                                                | 60.2 ms: 1.11x faster                                                 |
| raytrace                   | 312 ms                                                 | 284 ms: 1.10x faster                                                  |
| json                       | 5.26 ms                                                | 4.80 ms: 1.10x faster                                                 |
| json_loads                 | 28.5 us                                                | 26.1 us: 1.09x faster                                                 |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                                  |
| fannkuch                   | 417 ms                                                 | 388 ms: 1.08x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 725 ms: 1.07x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.39 ms: 1.06x faster                                                 |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                                  |
| sympy_str                  | 300 ms                                                 | 283 ms: 1.06x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.06x faster                                                  |
| pyflate                    | 482 ms                                                 | 460 ms: 1.05x faster                                                  |
| go                         | 139 ms                                                 | 133 ms: 1.05x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.04x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.85 ms: 1.04x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 20.8 ms: 1.03x faster                                                 |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                  |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 315 us: 1.03x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.64 ms: 1.03x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.03x faster                                                 |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.02x faster                                                  |
| django_template            | 34.6 ms                                                | 33.9 ms: 1.02x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.71 sec: 1.02x faster                                                |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                 |
| async_generators           | 463 ms                                                 | 455 ms: 1.02x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 67.7 ms: 1.01x faster                                                 |
| sqlite_synth               | 2.83 us                                                | 2.81 us: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 55.5 ms: 1.01x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                 |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.02x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 878 us: 1.04x slower                                                  |
| mdp                        | 2.63 sec                                               | 2.76 sec: 1.05x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.07x slower                                                 |
| telco                      | 7.10 ms                                                | 7.64 ms: 1.08x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 24.9 ms: 1.08x slower                                                 |
| nqueens                    | 83.3 ms                                                | 90.3 ms: 1.08x slower                                                 |
| hexiom                     | 6.41 ms                                                | 7.10 ms: 1.11x slower                                                 |
| mypy2                      | 830 ms                                                 | 960 ms: 1.16x slower                                                  |
| generators                 | 31.2 ms                                                | 36.3 ms: 1.16x slower                                                 |
| coverage                   | 72.7 ms                                                | 86.5 ms: 1.19x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 4.80 ms: 1.26x slower                                                 |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.66x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 80.8 ms: 3.37x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (3): sympy_expand, asyncio_websockets, sqlglot_normalize
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241212-3.14.0a2+-dc27e14-JIT/bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.101x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.12x