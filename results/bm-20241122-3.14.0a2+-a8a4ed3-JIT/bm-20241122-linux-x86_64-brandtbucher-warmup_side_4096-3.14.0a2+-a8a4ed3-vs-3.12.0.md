# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmup_side_4096
- machine: linux-x86_64
- commit hash: a8a4ed3
- commit date: 2024-11-22
- overall geometric mean: 1.076x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.06x faster                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 400 ms: 1.44x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 315 ms: 1.43x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 411 ms: 1.41x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 917 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 567 ms: 1.28x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 914 ms: 1.27x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.35x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 82.9 ms: 1.17x faster                                                    |
| float          | 84.7 ms                                                | 78.0 ms: 1.09x faster                                                    |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                  | 1.08x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                     |
| regex_effbot   | 3.61 ms                                                | 3.36 ms: 1.08x faster                                                    |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                     |
| regex_v8       | 23.1 ms                                                | 25.9 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 195 us: 1.18x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 78.5 ms: 1.14x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 55.4 ms: 1.11x faster                                                    |
| json_loads           | 28.5 us                                                | 26.2 us: 1.09x faster                                                    |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.07x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 320 us: 1.01x faster                                                     |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.07x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                    |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.96 ms: 1.19x faster                                                    |
| django_template | 34.6 ms                                                | 33.5 ms: 1.03x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 400 ms: 1.44x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 315 ms: 1.43x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 411 ms: 1.41x faster                                                     |
| deepcopy_memo              | 40.7 us                                                | 29.2 us: 1.40x faster                                                    |
| deepcopy                   | 371 us                                                 | 267 us: 1.39x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 917 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 567 ms: 1.28x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 914 ms: 1.27x faster                                                     |
| comprehensions             | 21.8 us                                                | 17.2 us: 1.27x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.24x faster                                                    |
| scimark_fft                | 382 ms                                                 | 318 ms: 1.20x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 68.5 ms: 1.20x faster                                                    |
| mako                       | 11.9 ms                                                | 9.96 ms: 1.19x faster                                                    |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                   |
| richards                   | 45.8 ms                                                | 38.5 ms: 1.19x faster                                                    |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 195 us: 1.18x faster                                                     |
| nbody                      | 97.0 ms                                                | 82.9 ms: 1.17x faster                                                    |
| deltablue                  | 3.72 ms                                                | 3.19 ms: 1.16x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 64.6 ms: 1.16x faster                                                    |
| richards_super             | 51.5 ms                                                | 44.5 ms: 1.16x faster                                                    |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                     |
| logging_format             | 7.23 us                                                | 6.28 us: 1.15x faster                                                    |
| sqlalchemy_declarative     | 147 ms                                                 | 129 ms: 1.14x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 78.5 ms: 1.14x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.70 us: 1.13x faster                                                    |
| chaos                      | 67.0 ms                                                | 59.6 ms: 1.12x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 55.4 ms: 1.11x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.57 ms: 1.11x faster                                                    |
| json                       | 5.26 ms                                                | 4.78 ms: 1.10x faster                                                    |
| raytrace                   | 312 ms                                                 | 284 ms: 1.10x faster                                                     |
| pyflate                    | 482 ms                                                 | 442 ms: 1.09x faster                                                     |
| json_loads                 | 28.5 us                                                | 26.2 us: 1.09x faster                                                    |
| float                      | 84.7 ms                                                | 78.0 ms: 1.09x faster                                                    |
| sympy_sum                  | 169 ms                                                 | 156 ms: 1.09x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 715 ms: 1.09x faster                                                     |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.3 ms: 1.08x faster                                                    |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                     |
| fannkuch                   | 417 ms                                                 | 386 ms: 1.08x faster                                                     |
| regex_effbot               | 3.61 ms                                                | 3.36 ms: 1.08x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.07x faster                                                     |
| sympy_str                  | 300 ms                                                 | 281 ms: 1.07x faster                                                     |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.06x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                     |
| 2to3                       | 274 ms                                                 | 260 ms: 1.06x faster                                                     |
| go                         | 139 ms                                                 | 133 ms: 1.04x faster                                                     |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                     |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                    |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 20.7 ms: 1.03x faster                                                    |
| django_template            | 34.6 ms                                                | 33.5 ms: 1.03x faster                                                    |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                    |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                                     |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                    |
| dulwich_log                | 68.5 ms                                                | 67.4 ms: 1.02x faster                                                    |
| mdp                        | 2.63 sec                                               | 2.59 sec: 1.02x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 320 us: 1.01x faster                                                     |
| sqlite_synth               | 2.83 us                                                | 2.81 us: 1.01x faster                                                    |
| async_generators           | 463 ms                                                 | 461 ms: 1.00x faster                                                     |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                     |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                     |
| sqlglot_normalize          | 110 ms                                                 | 111 ms: 1.01x slower                                                     |
| sqlglot_optimize           | 54.8 ms                                                | 55.7 ms: 1.02x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                    |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 874 us: 1.04x slower                                                     |
| nqueens                    | 83.3 ms                                                | 88.1 ms: 1.06x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                                     |
| telco                      | 7.10 ms                                                | 7.57 ms: 1.07x slower                                                    |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.07x slower                                                    |
| hexiom                     | 6.41 ms                                                | 7.04 ms: 1.10x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 25.9 ms: 1.12x slower                                                    |
| coverage                   | 72.7 ms                                                | 84.2 ms: 1.16x slower                                                    |
| generators                 | 31.2 ms                                                | 36.5 ms: 1.17x slower                                                    |
| gc_traversal               | 3.79 ms                                                | 4.68 ms: 1.23x slower                                                    |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                    |
| create_gc_cycles           | 1.48 ms                                                | 2.67 ms: 1.81x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 79.3 ms: 3.30x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                             |

Benchmark hidden because not significant (3): spectral_norm, sympy_expand, docutils
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241122-3.14.0a2+-a8a4ed3-JIT/bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.076x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x