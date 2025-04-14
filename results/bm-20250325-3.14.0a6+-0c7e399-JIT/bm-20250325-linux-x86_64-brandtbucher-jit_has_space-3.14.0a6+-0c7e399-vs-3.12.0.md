# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_has_space
- machine: linux-x86_64
- commit hash: 0c7e399
- commit date: 2025-03-25
- overall geometric mean: 1.112x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 264 ms: 1.04x faster                                                  |
| docutils       | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 622 ms: 1.90x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 626 ms: 1.85x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 317 ms: 1.82x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                  |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.77x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.52x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 499 ms: 1.46x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.3 ms: 1.30x faster                                                 |
| nbody          | 97.0 ms                                                | 87.5 ms: 1.11x faster                                                 |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.14 ms: 1.15x faster                                                 |
| regex_v8       | 23.1 ms                                                | 22.7 ms: 1.02x faster                                                 |
| regex_dna      | 212 ms                                                 | 213 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.87 sec: 1.24x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 80.7 ms: 1.10x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 56.9 ms: 1.09x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 98.4 ms: 1.09x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.07x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 322 us: 1.01x faster                                                  |
| json_loads           | 28.5 us                                                | 29.9 us: 1.05x slower                                                 |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.11x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.18 ms: 1.18x slower                                                 |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.9 ms: 1.09x faster                                                 |
| django_template | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 622 ms: 1.90x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 626 ms: 1.85x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 317 ms: 1.82x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                  |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.77x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.52x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 499 ms: 1.46x faster                                                  |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 28.9 us: 1.41x faster                                                 |
| float                      | 84.7 ms                                                | 65.3 ms: 1.30x faster                                                 |
| richards                   | 45.8 ms                                                | 36.4 ms: 1.26x faster                                                 |
| richards_super             | 51.5 ms                                                | 41.3 ms: 1.25x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.87 sec: 1.24x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.23x faster                                                 |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.08 ms: 1.20x faster                                                 |
| spectral_norm              | 115 ms                                                 | 97.0 ms: 1.18x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.6 ms: 1.16x faster                                                 |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                  |
| logging_format             | 7.23 us                                                | 6.24 us: 1.16x faster                                                 |
| comprehensions             | 21.8 us                                                | 18.9 us: 1.15x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.14 ms: 1.15x faster                                                 |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.63 us: 1.15x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 60.8 ms: 1.13x faster                                                 |
| async_generators           | 463 ms                                                 | 415 ms: 1.12x faster                                                  |
| chaos                      | 67.0 ms                                                | 60.2 ms: 1.11x faster                                                 |
| nbody                      | 97.0 ms                                                | 87.5 ms: 1.11x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 153 ms: 1.11x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 80.7 ms: 1.10x faster                                                 |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.10x faster                                                  |
| mako                       | 11.9 ms                                                | 10.9 ms: 1.09x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 68.7 ms: 1.09x faster                                                 |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.1 ms: 1.09x faster                                                 |
| django_template            | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 56.9 ms: 1.09x faster                                                 |
| sympy_str                  | 300 ms                                                 | 276 ms: 1.09x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 98.4 ms: 1.09x faster                                                 |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                  |
| go                         | 139 ms                                                 | 129 ms: 1.08x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.07x faster                                                  |
| pyflate                    | 482 ms                                                 | 450 ms: 1.07x faster                                                  |
| generators                 | 31.2 ms                                                | 29.2 ms: 1.07x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.75 ms: 1.06x faster                                                 |
| logging_silent             | 104 ns                                                 | 98.2 ns: 1.06x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 20.1 ms: 1.06x faster                                                 |
| mdp                        | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 78.2 ms: 1.05x faster                                                 |
| sqlite_synth               | 2.83 us                                                | 2.72 us: 1.04x faster                                                 |
| 2to3                       | 274 ms                                                 | 264 ms: 1.04x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.04x faster                                                |
| docutils                   | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 753 ms: 1.03x faster                                                  |
| regex_v8                   | 23.1 ms                                                | 22.7 ms: 1.02x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.55 sec: 1.01x faster                                                |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                  |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 322 us: 1.01x faster                                                  |
| regex_dna                  | 212 ms                                                 | 213 ms: 1.00x slower                                                  |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                                 |
| fannkuch                   | 417 ms                                                 | 423 ms: 1.01x slower                                                  |
| nqueens                    | 83.3 ms                                                | 85.0 ms: 1.02x slower                                                 |
| coroutines                 | 23.2 ms                                                | 24.1 ms: 1.04x slower                                                 |
| bench_thread_pool          | 842 us                                                 | 880 us: 1.05x slower                                                  |
| json_loads                 | 28.5 us                                                | 29.9 us: 1.05x slower                                                 |
| hexiom                     | 6.41 ms                                                | 6.81 ms: 1.06x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                                  |
| telco                      | 7.10 ms                                                | 7.79 ms: 1.10x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.11x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 8.18 ms: 1.18x slower                                                 |
| coverage                   | 72.7 ms                                                | 86.7 ms: 1.19x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 4.85 ms: 1.28x slower                                                 |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.69x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 82.7 ms: 3.44x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (2): sympy_expand, asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250325-3.14.0a6+-0c7e399-JIT/bm-20250325-linux-x86_64-brandtbucher-jit_has_space-3.14.0a6+-0c7e399.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.112x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.11x