# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_recursive
- machine: linux-x86_64
- commit hash: fe02176
- commit date: 2025-05-05
- overall geometric mean: 1.121x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 261 ms: 1.05x faster                                                  |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 597 ms: 1.94x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                  |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.82x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.79x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 496 ms: 1.46x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 501 ms: 1.45x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 64.8 ms: 1.31x faster                                                 |
| nbody          | 97.0 ms                                                | 95.6 ms: 1.01x faster                                                 |
| pidigits       | 187 ms                                                 | 191 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 2.95 ms: 1.22x faster                                                 |
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                  |
| regex_dna      | 212 ms                                                 | 196 ms: 1.08x faster                                                  |
| regex_v8       | 23.1 ms                                                | 22.4 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.12x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 208 us: 1.10x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 81.2 ms: 1.10x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 99.3 ms: 1.08x faster                                                 |
| json_loads           | 28.5 us                                                | 29.8 us: 1.05x slower                                                 |
| json_dumps           | 10.4 ms                                                | 11.9 ms: 1.14x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.92 ms: 1.00x faster                                                 |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                 |
| django_template | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.15x faster                                                |
| async_tree_io              | 1.16 sec                                               | 597 ms: 1.94x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                  |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.82x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.79x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 496 ms: 1.46x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 501 ms: 1.45x faster                                                  |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.8 us: 1.37x faster                                                 |
| float                      | 84.7 ms                                                | 64.8 ms: 1.31x faster                                                 |
| richards                   | 45.8 ms                                                | 35.4 ms: 1.30x faster                                                 |
| richards_super             | 51.5 ms                                                | 40.5 ms: 1.27x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.23x faster                                                 |
| comprehensions             | 21.8 us                                                | 17.8 us: 1.22x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 2.95 ms: 1.22x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.05 ms: 1.22x faster                                                 |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                  |
| go                         | 139 ms                                                 | 121 ms: 1.16x faster                                                  |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                                 |
| logging_format             | 7.23 us                                                | 6.36 us: 1.14x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.69 us: 1.14x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.13x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 60.8 ms: 1.13x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.12x faster                                                  |
| raytrace                   | 312 ms                                                 | 281 ms: 1.11x faster                                                  |
| sympy_str                  | 300 ms                                                 | 270 ms: 1.11x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.11x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 208 us: 1.10x faster                                                  |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.10x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 81.2 ms: 1.10x faster                                                 |
| pyflate                    | 482 ms                                                 | 440 ms: 1.10x faster                                                  |
| async_generators           | 463 ms                                                 | 423 ms: 1.09x faster                                                  |
| chaos                      | 67.0 ms                                                | 61.9 ms: 1.08x faster                                                 |
| regex_dna                  | 212 ms                                                 | 196 ms: 1.08x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 99.3 ms: 1.08x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 76.2 ms: 1.07x faster                                                 |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 730 ms: 1.06x faster                                                  |
| django_template            | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                 |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                                  |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.05x faster                                                |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                |
| regex_v8                   | 23.1 ms                                                | 22.4 ms: 1.03x faster                                                 |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.03x faster                                                |
| logging_silent             | 104 ns                                                 | 102 ns: 1.03x faster                                                  |
| fannkuch                   | 417 ms                                                 | 410 ms: 1.02x faster                                                  |
| sympy_expand               | 478 ms                                                 | 471 ms: 1.02x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.01x faster                                                 |
| nbody                      | 97.0 ms                                                | 95.6 ms: 1.01x faster                                                 |
| python_startup_no_site     | 6.94 ms                                                | 6.92 ms: 1.00x faster                                                 |
| generators                 | 31.2 ms                                                | 31.3 ms: 1.00x slower                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 75.5 ms: 1.01x slower                                                 |
| pidigits                   | 187 ms                                                 | 191 ms: 1.02x slower                                                  |
| scimark_lu                 | 118 ms                                                 | 122 ms: 1.03x slower                                                  |
| hexiom                     | 6.41 ms                                                | 6.65 ms: 1.04x slower                                                 |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.05x slower                                                 |
| coroutines                 | 23.2 ms                                                | 24.6 ms: 1.06x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                                  |
| scimark_fft                | 382 ms                                                 | 409 ms: 1.07x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 903 us: 1.07x slower                                                  |
| telco                      | 7.10 ms                                                | 7.88 ms: 1.11x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 11.9 ms: 1.14x slower                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.06 ms: 1.20x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 5.08 ms: 1.34x slower                                                 |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.58 ms: 1.75x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 92.3 ms: 3.85x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (4): pickle_pure_python, asyncio_websockets, nqueens, json
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, coverage, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (20) of results/bm-20250505-3.14.0a7+-fe02176-JIT/bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.121x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.15x