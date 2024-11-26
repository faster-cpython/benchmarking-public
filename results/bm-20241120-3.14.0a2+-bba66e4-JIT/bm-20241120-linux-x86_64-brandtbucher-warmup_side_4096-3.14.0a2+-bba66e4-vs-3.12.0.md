# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmup_side_4096
- machine: linux-x86_64
- commit hash: bba66e4
- commit date: 2024-11-20
- overall geometric mean: 1.079x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 259 ms: 1.06x faster                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 396 ms: 1.45x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 314 ms: 1.43x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 411 ms: 1.41x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 910 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 562 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 562 ms: 1.29x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 903 ms: 1.28x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 83.2 ms: 1.17x faster                                                    |
| float          | 84.7 ms                                                | 79.0 ms: 1.07x faster                                                    |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.08x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                     |
| regex_effbot   | 3.61 ms                                                | 3.42 ms: 1.06x faster                                                    |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                     |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 195 us: 1.18x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 79.0 ms: 1.13x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 55.7 ms: 1.11x faster                                                    |
| json_loads           | 28.5 us                                                | 26.1 us: 1.09x faster                                                    |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.09x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 317 us: 1.02x faster                                                     |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.02x slower                                                    |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.0 ms: 1.18x faster                                                    |
| django_template | 34.6 ms                                                | 33.3 ms: 1.04x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 396 ms: 1.45x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 314 ms: 1.43x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 411 ms: 1.41x faster                                                     |
| deepcopy                   | 371 us                                                 | 266 us: 1.39x faster                                                     |
| deepcopy_memo              | 40.7 us                                                | 29.2 us: 1.39x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 910 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 562 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 562 ms: 1.29x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 903 ms: 1.28x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.25x faster                                                    |
| comprehensions             | 21.8 us                                                | 17.5 us: 1.25x faster                                                    |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 67.2 ms: 1.22x faster                                                    |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                   |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.18x faster                                                    |
| mako                       | 11.9 ms                                                | 10.0 ms: 1.18x faster                                                    |
| richards                   | 45.8 ms                                                | 38.7 ms: 1.18x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 195 us: 1.18x faster                                                     |
| logging_format             | 7.23 us                                                | 6.20 us: 1.17x faster                                                    |
| deltablue                  | 3.72 ms                                                | 3.18 ms: 1.17x faster                                                    |
| nbody                      | 97.0 ms                                                | 83.2 ms: 1.17x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.59 us: 1.16x faster                                                    |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                     |
| richards_super             | 51.5 ms                                                | 44.7 ms: 1.15x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 65.7 ms: 1.14x faster                                                    |
| sqlalchemy_declarative     | 147 ms                                                 | 129 ms: 1.13x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 79.0 ms: 1.13x faster                                                    |
| chaos                      | 67.0 ms                                                | 59.3 ms: 1.13x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.52 ms: 1.12x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 55.7 ms: 1.11x faster                                                    |
| pyflate                    | 482 ms                                                 | 438 ms: 1.10x faster                                                     |
| json                       | 5.26 ms                                                | 4.77 ms: 1.10x faster                                                    |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.0 ms: 1.10x faster                                                    |
| raytrace                   | 312 ms                                                 | 285 ms: 1.10x faster                                                     |
| json_loads                 | 28.5 us                                                | 26.1 us: 1.09x faster                                                    |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.09x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 716 ms: 1.08x faster                                                     |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.07x faster                                                     |
| float                      | 84.7 ms                                                | 79.0 ms: 1.07x faster                                                    |
| fannkuch                   | 417 ms                                                 | 390 ms: 1.07x faster                                                     |
| sympy_str                  | 300 ms                                                 | 280 ms: 1.07x faster                                                     |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                   |
| logging_silent             | 104 ns                                                 | 98.5 ns: 1.06x faster                                                    |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                     |
| regex_effbot               | 3.61 ms                                                | 3.42 ms: 1.06x faster                                                    |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                     |
| go                         | 139 ms                                                 | 133 ms: 1.05x faster                                                     |
| django_template            | 34.6 ms                                                | 33.3 ms: 1.04x faster                                                    |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.04x faster                                                     |
| sympy_integrate            | 21.4 ms                                                | 20.7 ms: 1.04x faster                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.03x faster                                                    |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                    |
| async_generators           | 463 ms                                                 | 450 ms: 1.03x faster                                                     |
| pickle_pure_python         | 324 us                                                 | 317 us: 1.02x faster                                                     |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                    |
| dulwich_log                | 68.5 ms                                                | 67.1 ms: 1.02x faster                                                    |
| mdp                        | 2.63 sec                                               | 2.59 sec: 1.02x faster                                                   |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                     |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                    |
| sympy_expand               | 478 ms                                                 | 475 ms: 1.01x faster                                                     |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                     |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.01x slower                                                     |
| sqlglot_optimize           | 54.8 ms                                                | 55.6 ms: 1.01x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.02x slower                                                    |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 872 us: 1.04x slower                                                     |
| telco                      | 7.10 ms                                                | 7.50 ms: 1.06x slower                                                    |
| nqueens                    | 83.3 ms                                                | 88.5 ms: 1.06x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                    |
| hexiom                     | 6.41 ms                                                | 7.02 ms: 1.09x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                    |
| coverage                   | 72.7 ms                                                | 83.1 ms: 1.14x slower                                                    |
| generators                 | 31.2 ms                                                | 36.5 ms: 1.17x slower                                                    |
| gc_traversal               | 3.79 ms                                                | 4.54 ms: 1.20x slower                                                    |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                    |
| create_gc_cycles           | 1.48 ms                                                | 2.65 ms: 1.80x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 78.8 ms: 3.28x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                             |

Benchmark hidden because not significant (3): sqlglot_normalize, pycparser, docutils
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241120-3.14.0a2+-bba66e4-JIT/bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.079x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x