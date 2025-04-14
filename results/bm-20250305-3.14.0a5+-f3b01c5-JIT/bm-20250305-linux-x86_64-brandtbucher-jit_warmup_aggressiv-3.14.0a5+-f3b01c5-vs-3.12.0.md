# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_warmup_aggressiv
- machine: linux-x86_64
- commit hash: f3b01c5
- commit date: 2025-03-05
- overall geometric mean: 1.099x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 273 ms: 1.01x faster                                                         |
| docutils       | 2.77 sec                                               | 2.70 sec: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 628 ms: 1.88x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 618 ms: 1.87x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.82x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                         |
| async_tree_none            | 472 ms                                                 | 267 ms: 1.77x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 330 ms: 1.75x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 475 ms: 1.53x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.7 ms: 1.21x faster                                                        |
| nbody          | 97.0 ms                                                | 89.1 ms: 1.09x faster                                                        |
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 132 ms: 1.12x faster                                                         |
| regex_effbot   | 3.61 ms                                                | 3.34 ms: 1.08x faster                                                        |
| regex_dna      | 212 ms                                                 | 210 ms: 1.01x faster                                                         |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.89 sec: 1.23x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 79.4 ms: 1.12x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 56.1 ms: 1.10x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 210 us: 1.09x faster                                                         |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.09x faster                                                         |
| xml_etree_iterparse  | 107 ms                                                 | 99.6 ms: 1.07x faster                                                        |
| json_loads           | 28.5 us                                                | 29.8 us: 1.05x slower                                                        |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                        |
| python_startup         | 9.55 ms                                                | 13.0 ms: 1.36x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.6 ms: 1.13x faster                                                        |
| django_template | 34.6 ms                                                | 32.1 ms: 1.08x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 628 ms: 1.88x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 618 ms: 1.87x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.82x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                         |
| async_tree_none            | 472 ms                                                 | 267 ms: 1.77x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 330 ms: 1.75x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 475 ms: 1.53x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                         |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 29.0 us: 1.40x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.89 sec: 1.23x faster                                                       |
| scimark_fft                | 382 ms                                                 | 314 ms: 1.22x faster                                                         |
| float                      | 84.7 ms                                                | 69.7 ms: 1.21x faster                                                        |
| comprehensions             | 21.8 us                                                | 18.1 us: 1.20x faster                                                        |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.52 us: 1.17x faster                                                        |
| pathlib                    | 19.3 ms                                                | 16.9 ms: 1.15x faster                                                        |
| go                         | 139 ms                                                 | 122 ms: 1.15x faster                                                         |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.48 ms: 1.13x faster                                                        |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                         |
| async_generators           | 463 ms                                                 | 411 ms: 1.13x faster                                                         |
| mako                       | 11.9 ms                                                | 10.6 ms: 1.13x faster                                                        |
| regex_compile              | 148 ms                                                 | 132 ms: 1.12x faster                                                         |
| xml_etree_generate         | 89.2 ms                                                | 79.4 ms: 1.12x faster                                                        |
| chaos                      | 67.0 ms                                                | 59.7 ms: 1.12x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.34 ms: 1.11x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 56.1 ms: 1.10x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 210 us: 1.09x faster                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 68.7 ms: 1.09x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 75.2 ms: 1.09x faster                                                        |
| nbody                      | 97.0 ms                                                | 89.1 ms: 1.09x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.09x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.3 ms: 1.08x faster                                                        |
| regex_effbot               | 3.61 ms                                                | 3.34 ms: 1.08x faster                                                        |
| pyflate                    | 482 ms                                                 | 447 ms: 1.08x faster                                                         |
| generators                 | 31.2 ms                                                | 28.9 ms: 1.08x faster                                                        |
| django_template            | 34.6 ms                                                | 32.1 ms: 1.08x faster                                                        |
| sympy_str                  | 300 ms                                                 | 278 ms: 1.08x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 99.6 ms: 1.07x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 158 ms: 1.07x faster                                                         |
| pprint_safe_repr           | 776 ms                                                 | 736 ms: 1.05x faster                                                         |
| mdp                        | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                       |
| sqlalchemy_declarative     | 147 ms                                                 | 140 ms: 1.05x faster                                                         |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.05x faster                                                        |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                                         |
| richards                   | 45.8 ms                                                | 44.2 ms: 1.04x faster                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.03x faster                                                        |
| sympy_integrate            | 21.4 ms                                                | 20.8 ms: 1.03x faster                                                        |
| sqlite_synth               | 2.83 us                                                | 2.76 us: 1.03x faster                                                        |
| docutils                   | 2.77 sec                                               | 2.70 sec: 1.02x faster                                                       |
| dulwich_log                | 68.5 ms                                                | 67.3 ms: 1.02x faster                                                        |
| richards_super             | 51.5 ms                                                | 50.6 ms: 1.02x faster                                                        |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                                         |
| fannkuch                   | 417 ms                                                 | 412 ms: 1.01x faster                                                         |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                       |
| regex_dna                  | 212 ms                                                 | 210 ms: 1.01x faster                                                         |
| sympy_expand               | 478 ms                                                 | 474 ms: 1.01x faster                                                         |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                         |
| 2to3                       | 274 ms                                                 | 273 ms: 1.01x faster                                                         |
| hexiom                     | 6.41 ms                                                | 6.43 ms: 1.00x slower                                                        |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                         |
| sqlglot_optimize           | 54.8 ms                                                | 55.3 ms: 1.01x slower                                                        |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                                         |
| json                       | 5.26 ms                                                | 5.33 ms: 1.01x slower                                                        |
| logging_silent             | 104 ns                                                 | 107 ns: 1.02x slower                                                         |
| python_startup_no_site     | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                        |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.05x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 890 us: 1.06x slower                                                         |
| telco                      | 7.10 ms                                                | 7.54 ms: 1.06x slower                                                        |
| coroutines                 | 23.2 ms                                                | 24.9 ms: 1.07x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.08x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                        |
| coverage                   | 72.7 ms                                                | 84.4 ms: 1.16x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 4.73 ms: 1.25x slower                                                        |
| python_startup             | 9.55 ms                                                | 13.0 ms: 1.36x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.45 ms: 1.66x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 87.3 ms: 3.64x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                 |

Benchmark hidden because not significant (3): pickle_pure_python, pprint_pformat, nqueens
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250305-3.14.0a5+-f3b01c5-JIT/bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.099x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.15x