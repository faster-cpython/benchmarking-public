# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_compact_alt
- machine: linux-x86_64
- commit hash: 3aecbaa
- commit date: 2025-01-26
- overall geometric mean: 1.074x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 263 ms: 1.04x faster                                                    |
| docutils       | 2.77 sec                                               | 2.83 sec: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 625 ms: 1.89x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 637 ms: 1.81x faster                                                    |
| async_tree_none            | 472 ms                                                 | 268 ms: 1.76x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 326 ms: 1.76x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 262 ms: 1.72x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 338 ms: 1.71x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 488 ms: 1.49x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 505 ms: 1.44x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.69x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 67.6 ms: 1.25x faster                                                   |
| nbody          | 97.0 ms                                                | 92.9 ms: 1.04x faster                                                   |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.10x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 133 ms: 1.12x faster                                                    |
| regex_effbot   | 3.61 ms                                                | 3.27 ms: 1.10x faster                                                   |
| regex_dna      | 212 ms                                                 | 209 ms: 1.01x faster                                                    |
| regex_v8       | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.90 sec: 1.23x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 137 ms: 1.16x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 79.6 ms: 1.12x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 95.7 ms: 1.12x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 59.7 ms: 1.03x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 332 us: 1.02x slower                                                    |
| json_loads           | 28.5 us                                                | 29.2 us: 1.03x slower                                                   |
| unpickle_pure_python | 230 us                                                 | 237 us: 1.03x slower                                                    |
| json_dumps           | 10.4 ms                                                | 11.9 ms: 1.15x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.33 ms: 1.06x slower                                                   |
| python_startup         | 9.55 ms                                                | 13.0 ms: 1.36x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.20x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 11.9 ms                                                | 10.4 ms: 1.14x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                            |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 625 ms: 1.89x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 637 ms: 1.81x faster                                                    |
| async_tree_none            | 472 ms                                                 | 268 ms: 1.76x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 326 ms: 1.76x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 262 ms: 1.72x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 338 ms: 1.71x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 488 ms: 1.49x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 505 ms: 1.44x faster                                                    |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                                   |
| deepcopy                   | 371 us                                                 | 270 us: 1.37x faster                                                    |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.31x faster                                                   |
| float                      | 84.7 ms                                                | 67.6 ms: 1.25x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.90 sec: 1.23x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.77 us: 1.21x faster                                                   |
| scimark_fft                | 382 ms                                                 | 318 ms: 1.20x faster                                                    |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 69.0 ms: 1.19x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 64.1 ms: 1.17x faster                                                   |
| async_generators           | 463 ms                                                 | 396 ms: 1.17x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 137 ms: 1.16x faster                                                    |
| spectral_norm              | 115 ms                                                 | 99.0 ms: 1.16x faster                                                   |
| mako                       | 11.9 ms                                                | 10.4 ms: 1.14x faster                                                   |
| chaos                      | 67.0 ms                                                | 58.7 ms: 1.14x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 79.6 ms: 1.12x faster                                                   |
| regex_compile              | 148 ms                                                 | 133 ms: 1.12x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 95.7 ms: 1.12x faster                                                   |
| richards                   | 45.8 ms                                                | 41.1 ms: 1.11x faster                                                   |
| regex_effbot               | 3.61 ms                                                | 3.27 ms: 1.10x faster                                                   |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                    |
| deltablue                  | 3.72 ms                                                | 3.38 ms: 1.10x faster                                                   |
| richards_super             | 51.5 ms                                                | 46.9 ms: 1.10x faster                                                   |
| raytrace                   | 312 ms                                                 | 290 ms: 1.08x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.72 ms: 1.07x faster                                                   |
| pyflate                    | 482 ms                                                 | 451 ms: 1.07x faster                                                    |
| hexiom                     | 6.41 ms                                                | 6.06 ms: 1.06x faster                                                   |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                    |
| nbody                      | 97.0 ms                                                | 92.9 ms: 1.04x faster                                                   |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                  |
| 2to3                       | 274 ms                                                 | 263 ms: 1.04x faster                                                    |
| pprint_safe_repr           | 776 ms                                                 | 750 ms: 1.03x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 59.7 ms: 1.03x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                   |
| fannkuch                   | 417 ms                                                 | 406 ms: 1.03x faster                                                    |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.03x faster                                                  |
| nqueens                    | 83.3 ms                                                | 81.2 ms: 1.03x faster                                                   |
| sympy_str                  | 300 ms                                                 | 292 ms: 1.02x faster                                                    |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                                   |
| regex_dna                  | 212 ms                                                 | 209 ms: 1.01x faster                                                    |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                    |
| scimark_lu                 | 118 ms                                                 | 120 ms: 1.01x slower                                                    |
| json                       | 5.26 ms                                                | 5.33 ms: 1.01x slower                                                   |
| logging_silent             | 104 ns                                                 | 106 ns: 1.02x slower                                                    |
| docutils                   | 2.77 sec                                               | 2.83 sec: 1.02x slower                                                  |
| go                         | 139 ms                                                 | 143 ms: 1.02x slower                                                    |
| sympy_expand               | 478 ms                                                 | 489 ms: 1.02x slower                                                    |
| pickle_pure_python         | 324 us                                                 | 332 us: 1.02x slower                                                    |
| json_loads                 | 28.5 us                                                | 29.2 us: 1.03x slower                                                   |
| unpickle_pure_python       | 230 us                                                 | 237 us: 1.03x slower                                                    |
| sqlglot_optimize           | 54.8 ms                                                | 56.8 ms: 1.04x slower                                                   |
| coroutines                 | 23.2 ms                                                | 24.3 ms: 1.05x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                   |
| sympy_sum                  | 169 ms                                                 | 178 ms: 1.05x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 7.33 ms: 1.06x slower                                                   |
| sympy_integrate            | 21.4 ms                                                | 23.1 ms: 1.08x slower                                                   |
| logging_format             | 7.23 us                                                | 7.87 us: 1.09x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 172 us: 1.09x slower                                                    |
| dulwich_log                | 68.5 ms                                                | 75.6 ms: 1.10x slower                                                   |
| telco                      | 7.10 ms                                                | 7.86 ms: 1.11x slower                                                   |
| logging_simple             | 6.46 us                                                | 7.26 us: 1.12x slower                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 166 ms: 1.13x slower                                                    |
| json_dumps                 | 10.4 ms                                                | 11.9 ms: 1.15x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 972 us: 1.15x slower                                                    |
| sqlalchemy_imperative      | 18.7 ms                                                | 21.6 ms: 1.15x slower                                                   |
| gc_traversal               | 3.79 ms                                                | 4.61 ms: 1.22x slower                                                   |
| generators                 | 31.2 ms                                                | 38.5 ms: 1.23x slower                                                   |
| coverage                   | 72.7 ms                                                | 92.5 ms: 1.27x slower                                                   |
| python_startup             | 9.55 ms                                                | 13.0 ms: 1.36x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 90.2 ms: 3.76x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                            |

Benchmark hidden because not significant (4): sqlglot_normalize, pycparser, django_template, sqlglot_transpile
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250126-3.14.0a4+-3aecbaa-JIT/bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.074x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.24x