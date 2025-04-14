# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_peephole
- machine: linux-x86_64
- commit hash: edb68e1
- commit date: 2025-04-08
- overall geometric mean: 1.138x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                 |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                               |
| Geometric mean | (ref)                                                  | 1.06x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 619 ms: 1.91x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 613 ms: 1.89x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.85x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                 |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.81x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 68.8 ms: 1.23x faster                                                |
| nbody          | 97.0 ms                                                | 88.4 ms: 1.10x faster                                                |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.11x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.19x faster                                                 |
| regex_effbot   | 3.61 ms                                                | 3.22 ms: 1.12x faster                                                |
| regex_v8       | 23.1 ms                                                | 21.9 ms: 1.05x faster                                                |
| regex_dna      | 212 ms                                                 | 207 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.83 sec: 1.28x faster                                               |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.14x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 208 us: 1.10x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 81.0 ms: 1.10x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 97.1 ms: 1.10x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 56.6 ms: 1.09x faster                                                |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.02x faster                                                 |
| json_loads           | 28.5 us                                                | 29.4 us: 1.03x slower                                                |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.10x slower                                                |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.18 ms: 1.18x slower                                                |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.8 ms: 1.10x faster                                                |
| django_template | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.16x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 619 ms: 1.91x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 613 ms: 1.89x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.85x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                 |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.81x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                 |
| deepcopy                   | 371 us                                                 | 251 us: 1.48x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 28.7 us: 1.42x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 2.60 us: 1.28x faster                                                |
| richards                   | 45.8 ms                                                | 35.8 ms: 1.28x faster                                                |
| tomli_loads                | 2.33 sec                                               | 1.83 sec: 1.28x faster                                               |
| scimark_fft                | 382 ms                                                 | 303 ms: 1.26x faster                                                 |
| float                      | 84.7 ms                                                | 68.8 ms: 1.23x faster                                                |
| richards_super             | 51.5 ms                                                | 42.0 ms: 1.23x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.04 ms: 1.22x faster                                                |
| raytrace                   | 312 ms                                                 | 260 ms: 1.20x faster                                                 |
| regex_compile              | 148 ms                                                 | 125 ms: 1.19x faster                                                 |
| chaos                      | 67.0 ms                                                | 56.4 ms: 1.19x faster                                                |
| comprehensions             | 21.8 us                                                | 18.5 us: 1.18x faster                                                |
| go                         | 139 ms                                                 | 120 ms: 1.17x faster                                                 |
| spectral_norm              | 115 ms                                                 | 98.8 ms: 1.16x faster                                                |
| logging_format             | 7.23 us                                                | 6.23 us: 1.16x faster                                                |
| logging_simple             | 6.46 us                                                | 5.64 us: 1.15x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.14x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.9 ms: 1.14x faster                                                |
| pyflate                    | 482 ms                                                 | 422 ms: 1.14x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 66.1 ms: 1.14x faster                                                |
| dulwich_log                | 68.5 ms                                                | 60.7 ms: 1.13x faster                                                |
| scimark_sor                | 129 ms                                                 | 115 ms: 1.12x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.51 ms: 1.12x faster                                                |
| regex_effbot               | 3.61 ms                                                | 3.22 ms: 1.12x faster                                                |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                 |
| async_generators           | 463 ms                                                 | 418 ms: 1.11x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.11x faster                                                |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.11x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 74.1 ms: 1.10x faster                                                |
| mako                       | 11.9 ms                                                | 10.8 ms: 1.10x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 208 us: 1.10x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 81.0 ms: 1.10x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 97.1 ms: 1.10x faster                                                |
| nbody                      | 97.0 ms                                                | 88.4 ms: 1.10x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.1 ms: 1.09x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 56.6 ms: 1.09x faster                                                |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                 |
| generators                 | 31.2 ms                                                | 29.0 ms: 1.08x faster                                                |
| django_template            | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                |
| logging_silent             | 104 ns                                                 | 98.2 ns: 1.06x faster                                                |
| pprint_safe_repr           | 776 ms                                                 | 731 ms: 1.06x faster                                                 |
| regex_v8                   | 23.1 ms                                                | 21.9 ms: 1.05x faster                                                |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                               |
| sqlite_synth               | 2.83 us                                                | 2.73 us: 1.04x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                               |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                 |
| sympy_expand               | 478 ms                                                 | 466 ms: 1.03x faster                                                 |
| regex_dna                  | 212 ms                                                 | 207 ms: 1.02x faster                                                 |
| nqueens                    | 83.3 ms                                                | 81.5 ms: 1.02x faster                                                |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.02x faster                                                 |
| fannkuch                   | 417 ms                                                 | 411 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                 |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                 |
| coroutines                 | 23.2 ms                                                | 23.7 ms: 1.02x slower                                                |
| hexiom                     | 6.41 ms                                                | 6.60 ms: 1.03x slower                                                |
| json_loads                 | 28.5 us                                                | 29.4 us: 1.03x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                 |
| bench_thread_pool          | 842 us                                                 | 892 us: 1.06x slower                                                 |
| telco                      | 7.10 ms                                                | 7.68 ms: 1.08x slower                                                |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.10x slower                                                |
| coverage                   | 72.7 ms                                                | 85.1 ms: 1.17x slower                                                |
| python_startup_no_site     | 6.94 ms                                                | 8.18 ms: 1.18x slower                                                |
| gc_traversal               | 3.79 ms                                                | 5.05 ms: 1.33x slower                                                |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 82.0 ms: 3.42x slower                                                |
| Geometric mean             | (ref)                                                  | 1.12x faster                                                         |

Benchmark hidden because not significant (2): pycparser, json
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250408-3.14.0a7+-edb68e1-JIT/bm-20250408-linux-x86_64-brandtbucher-jit_peephole-3.14.0a7+-edb68e1.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.138x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.12x