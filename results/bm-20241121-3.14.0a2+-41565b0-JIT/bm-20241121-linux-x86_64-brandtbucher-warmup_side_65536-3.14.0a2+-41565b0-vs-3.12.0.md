# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmup_side_65536
- machine: linux-x86_64
- commit hash: 41565b0
- commit date: 2024-11-21
- overall geometric mean: 1.074x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.06x faster                                                      |
| docutils       | 2.77 sec                                               | 2.71 sec: 1.02x faster                                                    |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 400 ms: 1.44x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 407 ms: 1.42x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 319 ms: 1.41x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 916 ms: 1.29x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 568 ms: 1.28x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 906 ms: 1.28x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.35x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 84.8 ms: 1.14x faster                                                     |
| float          | 84.7 ms                                                | 82.3 ms: 1.03x faster                                                     |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 131 ms: 1.13x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.40 ms: 1.06x faster                                                     |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                      |
| regex_v8       | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 230 us                                                 | 194 us: 1.19x faster                                                      |
| tomli_loads          | 2.33 sec                                               | 1.99 sec: 1.17x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 78.8 ms: 1.13x faster                                                     |
| json_loads           | 28.5 us                                                | 26.3 us: 1.08x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 57.1 ms: 1.08x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 102 ms: 1.05x faster                                                      |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                              |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                     |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                     |
| django_template | 34.6 ms                                                | 33.1 ms: 1.04x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 400 ms: 1.44x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 407 ms: 1.42x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 319 ms: 1.41x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 29.1 us: 1.40x faster                                                     |
| deepcopy                   | 371 us                                                 | 267 us: 1.39x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 916 ms: 1.29x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 568 ms: 1.28x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 906 ms: 1.28x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                     |
| comprehensions             | 21.8 us                                                | 17.6 us: 1.24x faster                                                     |
| scimark_fft                | 382 ms                                                 | 315 ms: 1.21x faster                                                      |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.20x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 68.6 ms: 1.19x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 194 us: 1.19x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.14 ms: 1.18x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.99 sec: 1.17x faster                                                    |
| mako                       | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                     |
| richards                   | 45.8 ms                                                | 39.3 ms: 1.17x faster                                                     |
| logging_format             | 7.23 us                                                | 6.25 us: 1.16x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.61 us: 1.15x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 65.5 ms: 1.15x faster                                                     |
| nbody                      | 97.0 ms                                                | 84.8 ms: 1.14x faster                                                     |
| sqlalchemy_declarative     | 147 ms                                                 | 129 ms: 1.14x faster                                                      |
| regex_compile              | 148 ms                                                 | 131 ms: 1.13x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 78.8 ms: 1.13x faster                                                     |
| richards_super             | 51.5 ms                                                | 45.6 ms: 1.13x faster                                                     |
| raytrace                   | 312 ms                                                 | 280 ms: 1.11x faster                                                      |
| go                         | 139 ms                                                 | 126 ms: 1.11x faster                                                      |
| chaos                      | 67.0 ms                                                | 60.4 ms: 1.11x faster                                                     |
| sympy_sum                  | 169 ms                                                 | 153 ms: 1.10x faster                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.62 ms: 1.09x faster                                                     |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.2 ms: 1.08x faster                                                     |
| json_loads                 | 28.5 us                                                | 26.3 us: 1.08x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 57.1 ms: 1.08x faster                                                     |
| fannkuch                   | 417 ms                                                 | 388 ms: 1.08x faster                                                      |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.07x faster                                                      |
| sympy_str                  | 300 ms                                                 | 280 ms: 1.07x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                                      |
| regex_effbot               | 3.61 ms                                                | 3.40 ms: 1.06x faster                                                     |
| pyflate                    | 482 ms                                                 | 455 ms: 1.06x faster                                                      |
| json                       | 5.26 ms                                                | 4.97 ms: 1.06x faster                                                     |
| 2to3                       | 274 ms                                                 | 260 ms: 1.06x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 736 ms: 1.05x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 102 ms: 1.05x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.05x faster                                                      |
| django_template            | 34.6 ms                                                | 33.1 ms: 1.04x faster                                                     |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                     |
| logging_silent             | 104 ns                                                 | 100 ns: 1.04x faster                                                      |
| sympy_integrate            | 21.4 ms                                                | 20.7 ms: 1.04x faster                                                     |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                     |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                      |
| float                      | 84.7 ms                                                | 82.3 ms: 1.03x faster                                                     |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                    |
| sqlite_synth               | 2.83 us                                                | 2.76 us: 1.03x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 66.8 ms: 1.03x faster                                                     |
| docutils                   | 2.77 sec                                               | 2.71 sec: 1.02x faster                                                    |
| mdp                        | 2.63 sec                                               | 2.58 sec: 1.02x faster                                                    |
| async_generators           | 463 ms                                                 | 457 ms: 1.01x faster                                                      |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                    |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 55.1 ms: 1.00x slower                                                     |
| sqlglot_normalize          | 110 ms                                                 | 111 ms: 1.01x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                      |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                     |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                      |
| bench_thread_pool          | 842 us                                                 | 872 us: 1.04x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.05x slower                                                      |
| hexiom                     | 6.41 ms                                                | 6.83 ms: 1.06x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                     |
| nqueens                    | 83.3 ms                                                | 89.2 ms: 1.07x slower                                                     |
| telco                      | 7.10 ms                                                | 7.63 ms: 1.07x slower                                                     |
| regex_v8                   | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                     |
| generators                 | 31.2 ms                                                | 35.6 ms: 1.14x slower                                                     |
| coverage                   | 72.7 ms                                                | 85.4 ms: 1.17x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 4.73 ms: 1.25x slower                                                     |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 2.67 ms: 1.81x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 79.2 ms: 3.30x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                              |

Benchmark hidden because not significant (3): pickle_pure_python, sympy_expand, spectral_norm
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241121-3.14.0a2+-41565b0-JIT/bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.074x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.10x