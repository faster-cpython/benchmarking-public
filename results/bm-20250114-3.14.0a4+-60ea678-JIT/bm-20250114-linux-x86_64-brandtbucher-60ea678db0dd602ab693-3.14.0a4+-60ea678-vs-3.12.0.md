# Results vs. 3.12.0

- fork: brandtbucher
- ref: 60ea678db0dd602ab693
- machine: linux-x86_64
- commit hash: 60ea678
- commit date: 2025-01-14
- overall geometric mean: 1.101x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 261 ms: 1.05x faster                                                         |
| docutils       | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 592 ms: 2.00x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 617 ms: 1.87x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                                         |
| async_tree_none            | 472 ms                                                 | 267 ms: 1.77x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 333 ms: 1.74x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 466 ms: 1.56x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.48x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.2 ms: 1.21x faster                                                        |
| nbody          | 97.0 ms                                                | 93.8 ms: 1.03x faster                                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.00 ms: 1.20x faster                                                        |
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                         |
| regex_dna      | 212 ms                                                 | 202 ms: 1.05x faster                                                         |
| regex_v8       | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.83 sec: 1.27x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 194 us: 1.18x faster                                                         |
| xml_etree_parse      | 159 ms                                                 | 137 ms: 1.17x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 78.1 ms: 1.14x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 94.5 ms: 1.13x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 54.7 ms: 1.13x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.02x faster                                                         |
| json_loads           | 28.5 us                                                | 29.4 us: 1.03x slower                                                        |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                        |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                        |
| django_template | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 592 ms: 2.00x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 617 ms: 1.87x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                                         |
| async_tree_none            | 472 ms                                                 | 267 ms: 1.77x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 333 ms: 1.74x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 466 ms: 1.56x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.48x faster                                                         |
| deepcopy                   | 371 us                                                 | 268 us: 1.38x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 29.9 us: 1.36x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.83 sec: 1.27x faster                                                       |
| comprehensions             | 21.8 us                                                | 17.2 us: 1.26x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                                        |
| float                      | 84.7 ms                                                | 70.2 ms: 1.21x faster                                                        |
| regex_effbot               | 3.61 ms                                                | 3.00 ms: 1.20x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 63.0 ms: 1.19x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 194 us: 1.18x faster                                                         |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                        |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 137 ms: 1.17x faster                                                         |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                         |
| scimark_fft                | 382 ms                                                 | 331 ms: 1.15x faster                                                         |
| xml_etree_generate         | 89.2 ms                                                | 78.1 ms: 1.14x faster                                                        |
| logging_format             | 7.23 us                                                | 6.35 us: 1.14x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.27 ms: 1.14x faster                                                        |
| async_generators           | 463 ms                                                 | 408 ms: 1.14x faster                                                         |
| crypto_pyaes               | 81.9 ms                                                | 72.2 ms: 1.13x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 94.5 ms: 1.13x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 54.7 ms: 1.13x faster                                                        |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                         |
| logging_simple             | 6.46 us                                                | 5.77 us: 1.12x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.11x faster                                                        |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.60 ms: 1.10x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 156 ms: 1.09x faster                                                         |
| pyflate                    | 482 ms                                                 | 449 ms: 1.07x faster                                                         |
| fannkuch                   | 417 ms                                                 | 389 ms: 1.07x faster                                                         |
| raytrace                   | 312 ms                                                 | 291 ms: 1.07x faster                                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                        |
| sympy_str                  | 300 ms                                                 | 280 ms: 1.07x faster                                                         |
| chaos                      | 67.0 ms                                                | 62.7 ms: 1.07x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 728 ms: 1.06x faster                                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                        |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                                         |
| regex_dna                  | 212 ms                                                 | 202 ms: 1.05x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.05x faster                                                       |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.04x faster                                                         |
| sympy_integrate            | 21.4 ms                                                | 20.6 ms: 1.04x faster                                                        |
| richards                   | 45.8 ms                                                | 44.2 ms: 1.04x faster                                                        |
| sqlite_synth               | 2.83 us                                                | 2.74 us: 1.04x faster                                                        |
| nbody                      | 97.0 ms                                                | 93.8 ms: 1.03x faster                                                        |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                         |
| go                         | 139 ms                                                 | 135 ms: 1.03x faster                                                         |
| mdp                        | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                       |
| docutils                   | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                       |
| django_template            | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                        |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                                         |
| dulwich_log                | 68.5 ms                                                | 67.4 ms: 1.02x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.02x faster                                                         |
| richards_super             | 51.5 ms                                                | 50.9 ms: 1.01x faster                                                        |
| json                       | 5.26 ms                                                | 5.21 ms: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| sympy_expand               | 478 ms                                                 | 476 ms: 1.00x faster                                                         |
| sqlglot_optimize           | 54.8 ms                                                | 54.6 ms: 1.00x faster                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                        |
| coroutines                 | 23.2 ms                                                | 23.8 ms: 1.03x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                        |
| json_loads                 | 28.5 us                                                | 29.4 us: 1.03x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                         |
| spectral_norm              | 115 ms                                                 | 121 ms: 1.05x slower                                                         |
| logging_silent             | 104 ns                                                 | 111 ns: 1.06x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 895 us: 1.06x slower                                                         |
| telco                      | 7.10 ms                                                | 7.55 ms: 1.06x slower                                                        |
| nqueens                    | 83.3 ms                                                | 89.8 ms: 1.08x slower                                                        |
| hexiom                     | 6.41 ms                                                | 7.18 ms: 1.12x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                        |
| generators                 | 31.2 ms                                                | 37.5 ms: 1.20x slower                                                        |
| coverage                   | 72.7 ms                                                | 90.2 ms: 1.24x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 4.84 ms: 1.28x slower                                                        |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.44 ms: 1.65x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.2 ms: 3.38x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                 |

Benchmark hidden because not significant (2): pycparser, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250114-3.14.0a4+-60ea678-JIT/bm-20250114-linux-x86_64-brandtbucher-60ea678db0dd602ab693-3.14.0a4+-60ea678.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.101x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x