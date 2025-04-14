# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_11_7
- machine: linux-x86_64
- commit hash: a70757e
- commit date: 2025-03-28
- overall geometric mean: 1.112x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 264 ms: 1.04x faster                                                |
| docutils       | 2.77 sec                                               | 2.68 sec: 1.03x faster                                              |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.90x faster                                                |
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 317 ms: 1.82x faster                                                |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.82x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 472 ms: 1.54x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 489 ms: 1.48x faster                                                |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.3 ms: 1.30x faster                                               |
| nbody          | 97.0 ms                                                | 88.9 ms: 1.09x faster                                               |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.13x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.10 ms: 1.16x faster                                               |
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                |
| regex_v8       | 23.1 ms                                                | 22.9 ms: 1.01x faster                                               |
| regex_dna      | 212 ms                                                 | 211 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                  | 1.08x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.87 sec: 1.25x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 80.5 ms: 1.11x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 56.6 ms: 1.09x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 98.2 ms: 1.09x faster                                               |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.06x faster                                                |
| json_loads           | 28.5 us                                                | 30.0 us: 1.05x slower                                               |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.11x slower                                               |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.21 ms: 1.18x slower                                               |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                               |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.9 ms: 1.09x faster                                               |
| django_template | 34.6 ms                                                | 32.9 ms: 1.05x faster                                               |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.90x faster                                                |
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 317 ms: 1.82x faster                                                |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.82x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 472 ms: 1.54x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 489 ms: 1.48x faster                                                |
| deepcopy                   | 371 us                                                 | 264 us: 1.41x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                               |
| float                      | 84.7 ms                                                | 65.3 ms: 1.30x faster                                               |
| richards_super             | 51.5 ms                                                | 41.2 ms: 1.25x faster                                               |
| richards                   | 45.8 ms                                                | 36.8 ms: 1.25x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.87 sec: 1.25x faster                                              |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                               |
| scimark_fft                | 382 ms                                                 | 314 ms: 1.22x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.08 ms: 1.21x faster                                               |
| spectral_norm              | 115 ms                                                 | 97.0 ms: 1.18x faster                                               |
| logging_format             | 7.23 us                                                | 6.14 us: 1.18x faster                                               |
| raytrace                   | 312 ms                                                 | 266 ms: 1.18x faster                                                |
| comprehensions             | 21.8 us                                                | 18.7 us: 1.16x faster                                               |
| regex_effbot               | 3.61 ms                                                | 3.10 ms: 1.16x faster                                               |
| pathlib                    | 19.3 ms                                                | 16.6 ms: 1.16x faster                                               |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                |
| logging_simple             | 6.46 us                                                | 5.60 us: 1.15x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                |
| pyflate                    | 482 ms                                                 | 429 ms: 1.13x faster                                                |
| dulwich_log                | 68.5 ms                                                | 60.9 ms: 1.12x faster                                               |
| chaos                      | 67.0 ms                                                | 59.8 ms: 1.12x faster                                               |
| async_generators           | 463 ms                                                 | 414 ms: 1.12x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 80.5 ms: 1.11x faster                                               |
| go                         | 139 ms                                                 | 127 ms: 1.10x faster                                                |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                                |
| nbody                      | 97.0 ms                                                | 88.9 ms: 1.09x faster                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 68.9 ms: 1.09x faster                                               |
| xml_etree_process          | 61.7 ms                                                | 56.6 ms: 1.09x faster                                               |
| mako                       | 11.9 ms                                                | 10.9 ms: 1.09x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 98.2 ms: 1.09x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 75.5 ms: 1.08x faster                                               |
| sqlalchemy_declarative     | 147 ms                                                 | 136 ms: 1.08x faster                                                |
| sympy_str                  | 300 ms                                                 | 277 ms: 1.08x faster                                                |
| generators                 | 31.2 ms                                                | 29.1 ms: 1.07x faster                                               |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.07x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.4 ms: 1.07x faster                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.73 ms: 1.07x faster                                               |
| logging_silent             | 104 ns                                                 | 98.1 ns: 1.07x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.06x faster                                                |
| mdp                        | 2.63 sec                                               | 2.49 sec: 1.06x faster                                              |
| sympy_integrate            | 21.4 ms                                                | 20.3 ms: 1.06x faster                                               |
| django_template            | 34.6 ms                                                | 32.9 ms: 1.05x faster                                               |
| sqlite_synth               | 2.83 us                                                | 2.72 us: 1.04x faster                                               |
| 2to3                       | 274 ms                                                 | 264 ms: 1.04x faster                                                |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.04x faster                                              |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                |
| docutils                   | 2.77 sec                                               | 2.68 sec: 1.03x faster                                              |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.55 sec: 1.01x faster                                              |
| regex_v8                   | 23.1 ms                                                | 22.9 ms: 1.01x faster                                               |
| fannkuch                   | 417 ms                                                 | 414 ms: 1.01x faster                                                |
| regex_dna                  | 212 ms                                                 | 211 ms: 1.00x faster                                                |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                                |
| json                       | 5.26 ms                                                | 5.35 ms: 1.02x slower                                               |
| nqueens                    | 83.3 ms                                                | 85.5 ms: 1.03x slower                                               |
| coroutines                 | 23.2 ms                                                | 24.2 ms: 1.05x slower                                               |
| bench_thread_pool          | 842 us                                                 | 886 us: 1.05x slower                                                |
| json_loads                 | 28.5 us                                                | 30.0 us: 1.05x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.07x slower                                                |
| telco                      | 7.10 ms                                                | 7.78 ms: 1.10x slower                                               |
| hexiom                     | 6.41 ms                                                | 7.11 ms: 1.11x slower                                               |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.11x slower                                               |
| coverage                   | 72.7 ms                                                | 86.0 ms: 1.18x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 8.21 ms: 1.18x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.85 ms: 1.28x slower                                               |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 83.3 ms: 3.47x slower                                               |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                        |

Benchmark hidden because not significant (4): sympy_expand, asyncio_websockets, pprint_safe_repr, pickle_pure_python
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250328-3.14.0a6+-a70757e-JIT/bm-20250328-linux-x86_64-brandtbucher-jit_up_11_7-3.14.0a6+-a70757e.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.112x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.12x