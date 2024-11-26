# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmup_side_256
- machine: linux-x86_64
- commit hash: 225f351
- commit date: 2024-11-20
- overall geometric mean: 1.072x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                                    |
| docutils       | 2.77 sec                                               | 2.79 sec: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 400 ms: 1.43x faster                                                    |
| async_tree_none            | 472 ms                                                 | 330 ms: 1.43x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 318 ms: 1.41x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 415 ms: 1.39x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 922 ms: 1.28x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 567 ms: 1.28x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 922 ms: 1.25x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.34x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 83.1 ms: 1.17x faster                                                   |
| float          | 84.7 ms                                                | 78.4 ms: 1.08x faster                                                   |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 131 ms: 1.14x faster                                                    |
| regex_effbot   | 3.61 ms                                                | 3.34 ms: 1.08x faster                                                   |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                                    |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 194 us: 1.19x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 79.0 ms: 1.13x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 55.5 ms: 1.11x faster                                                   |
| json_loads           | 28.5 us                                                | 26.4 us: 1.08x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 102 ms: 1.05x faster                                                    |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                                    |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                   |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.0 ms: 1.19x faster                                                   |
| django_template | 34.6 ms                                                | 33.2 ms: 1.04x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 400 ms: 1.43x faster                                                    |
| async_tree_none            | 472 ms                                                 | 330 ms: 1.43x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 318 ms: 1.41x faster                                                    |
| deepcopy                   | 371 us                                                 | 267 us: 1.39x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 415 ms: 1.39x faster                                                    |
| deepcopy_memo              | 40.7 us                                                | 29.6 us: 1.37x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 922 ms: 1.28x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 567 ms: 1.28x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 922 ms: 1.25x faster                                                    |
| comprehensions             | 21.8 us                                                | 17.9 us: 1.22x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 68.4 ms: 1.20x faster                                                   |
| scimark_fft                | 382 ms                                                 | 319 ms: 1.20x faster                                                    |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                   |
| logging_format             | 7.23 us                                                | 6.07 us: 1.19x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 194 us: 1.19x faster                                                    |
| mako                       | 11.9 ms                                                | 10.0 ms: 1.19x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.49 us: 1.18x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 64.3 ms: 1.17x faster                                                   |
| nbody                      | 97.0 ms                                                | 83.1 ms: 1.17x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.19 ms: 1.16x faster                                                   |
| richards                   | 45.8 ms                                                | 39.6 ms: 1.16x faster                                                   |
| regex_compile              | 148 ms                                                 | 131 ms: 1.14x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 79.0 ms: 1.13x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                    |
| chaos                      | 67.0 ms                                                | 59.8 ms: 1.12x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 55.5 ms: 1.11x faster                                                   |
| richards_super             | 51.5 ms                                                | 46.7 ms: 1.10x faster                                                   |
| json                       | 5.26 ms                                                | 4.80 ms: 1.10x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.62 ms: 1.09x faster                                                   |
| raytrace                   | 312 ms                                                 | 287 ms: 1.09x faster                                                    |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                  |
| float                      | 84.7 ms                                                | 78.4 ms: 1.08x faster                                                   |
| json_loads                 | 28.5 us                                                | 26.4 us: 1.08x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 718 ms: 1.08x faster                                                    |
| regex_effbot               | 3.61 ms                                                | 3.34 ms: 1.08x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                    |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.4 ms: 1.07x faster                                                   |
| pyflate                    | 482 ms                                                 | 450 ms: 1.07x faster                                                    |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                                    |
| sympy_sum                  | 169 ms                                                 | 159 ms: 1.06x faster                                                    |
| fannkuch                   | 417 ms                                                 | 396 ms: 1.05x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 102 ms: 1.05x faster                                                    |
| sympy_str                  | 300 ms                                                 | 285 ms: 1.05x faster                                                    |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                                    |
| logging_silent             | 104 ns                                                 | 100 ns: 1.04x faster                                                    |
| django_template            | 34.6 ms                                                | 33.2 ms: 1.04x faster                                                   |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                    |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                  |
| go                         | 139 ms                                                 | 135 ms: 1.03x faster                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.65 ms: 1.02x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.02x faster                                                    |
| async_generators           | 463 ms                                                 | 453 ms: 1.02x faster                                                    |
| sympy_integrate            | 21.4 ms                                                | 21.0 ms: 1.02x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.34 ms: 1.02x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 67.5 ms: 1.02x faster                                                   |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.01x faster                                                    |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                                    |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                    |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                    |
| sqlglot_normalize          | 110 ms                                                 | 111 ms: 1.01x slower                                                    |
| docutils                   | 2.77 sec                                               | 2.79 sec: 1.01x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 55.9 ms: 1.02x slower                                                   |
| sympy_expand               | 478 ms                                                 | 488 ms: 1.02x slower                                                    |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                                    |
| bench_thread_pool          | 842 us                                                 | 875 us: 1.04x slower                                                    |
| mdp                        | 2.63 sec                                               | 2.77 sec: 1.05x slower                                                  |
| telco                      | 7.10 ms                                                | 7.56 ms: 1.07x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                    |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                   |
| nqueens                    | 83.3 ms                                                | 90.1 ms: 1.08x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                   |
| hexiom                     | 6.41 ms                                                | 7.16 ms: 1.12x slower                                                   |
| generators                 | 31.2 ms                                                | 35.8 ms: 1.15x slower                                                   |
| gc_traversal               | 3.79 ms                                                | 4.36 ms: 1.15x slower                                                   |
| coverage                   | 72.7 ms                                                | 83.5 ms: 1.15x slower                                                   |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 2.65 ms: 1.79x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 79.0 ms: 3.29x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                            |

Benchmark hidden because not significant (1): coroutines
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241120-3.14.0a2+-225f351-JIT/bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.072x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.10x