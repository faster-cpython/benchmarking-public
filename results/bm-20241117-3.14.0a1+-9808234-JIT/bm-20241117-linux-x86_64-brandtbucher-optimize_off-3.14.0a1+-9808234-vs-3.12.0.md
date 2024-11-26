# Results vs. 3.12.0

- fork: brandtbucher
- ref: optimize_off
- machine: linux-x86_64
- commit hash: 9808234
- commit date: 2024-11-17
- overall geometric mean: 1.049x faster
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 283 ms: 1.03x slower                                                 |
| docutils       | 2.77 sec                                               | 3.13 sec: 1.13x slower                                               |
| Geometric mean | (ref)                                                  | 1.08x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 383 ms: 1.50x faster                                                 |
| async_tree_none            | 472 ms                                                 | 333 ms: 1.42x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 326 ms: 1.38x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 421 ms: 1.37x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 858 ms: 1.35x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 560 ms: 1.29x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 577 ms: 1.26x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 977 ms: 1.21x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.34x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 84.5 ms: 1.15x faster                                                |
| float          | 84.7 ms                                                | 77.2 ms: 1.10x faster                                                |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 143 ms: 1.04x faster                                                 |
| regex_dna      | 212 ms                                                 | 215 ms: 1.02x slower                                                 |
| regex_effbot   | 3.61 ms                                                | 3.73 ms: 1.03x slower                                                |
| regex_v8       | 23.1 ms                                                | 25.3 ms: 1.09x slower                                                |
| Geometric mean | (ref)                                                  | 1.03x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.22x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 78.7 ms: 1.13x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                |
| json_loads           | 28.5 us                                                | 26.6 us: 1.07x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 99.7 ms: 1.07x faster                                                |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.05x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 328 us: 1.01x slower                                                 |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.3 ms: 1.15x faster                                                |
| django_template | 34.6 ms                                                | 34.3 ms: 1.01x faster                                                |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 383 ms: 1.50x faster                                                 |
| async_tree_none            | 472 ms                                                 | 333 ms: 1.42x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 326 ms: 1.38x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 421 ms: 1.37x faster                                                 |
| deepcopy                   | 371 us                                                 | 272 us: 1.36x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 858 ms: 1.35x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 560 ms: 1.29x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 577 ms: 1.26x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                |
| comprehensions             | 21.8 us                                                | 17.8 us: 1.22x faster                                                |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.22x faster                                               |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.21x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 977 ms: 1.21x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 69.1 ms: 1.18x faster                                                |
| scimark_fft                | 382 ms                                                 | 325 ms: 1.18x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 64.6 ms: 1.16x faster                                                |
| logging_format             | 7.23 us                                                | 6.24 us: 1.16x faster                                                |
| richards                   | 45.8 ms                                                | 39.7 ms: 1.16x faster                                                |
| mako                       | 11.9 ms                                                | 10.3 ms: 1.15x faster                                                |
| nbody                      | 97.0 ms                                                | 84.5 ms: 1.15x faster                                                |
| logging_simple             | 6.46 us                                                | 5.64 us: 1.14x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 78.7 ms: 1.13x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                |
| float                      | 84.7 ms                                                | 77.2 ms: 1.10x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.39 ms: 1.09x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.64 ms: 1.09x faster                                                |
| chaos                      | 67.0 ms                                                | 61.5 ms: 1.09x faster                                                |
| json_loads                 | 28.5 us                                                | 26.6 us: 1.07x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 99.7 ms: 1.07x faster                                                |
| raytrace                   | 312 ms                                                 | 292 ms: 1.07x faster                                                 |
| fannkuch                   | 417 ms                                                 | 390 ms: 1.07x faster                                                 |
| richards_super             | 51.5 ms                                                | 48.2 ms: 1.07x faster                                                |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                                 |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.7 ms: 1.06x faster                                                |
| pyflate                    | 482 ms                                                 | 458 ms: 1.05x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.05x faster                                                 |
| json                       | 5.26 ms                                                | 5.03 ms: 1.05x faster                                                |
| pprint_safe_repr           | 776 ms                                                 | 747 ms: 1.04x faster                                                 |
| regex_compile              | 148 ms                                                 | 143 ms: 1.04x faster                                                 |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                 |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                                 |
| go                         | 139 ms                                                 | 136 ms: 1.03x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.03x faster                                               |
| coroutines                 | 23.2 ms                                                | 22.6 ms: 1.02x faster                                                |
| async_generators           | 463 ms                                                 | 454 ms: 1.02x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.34 ms: 1.02x faster                                                |
| django_template            | 34.6 ms                                                | 34.3 ms: 1.01x faster                                                |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 328 us: 1.01x slower                                                 |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.02x slower                                                 |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                |
| sqlglot_transpile          | 1.68 ms                                                | 1.72 ms: 1.02x slower                                                |
| sympy_str                  | 300 ms                                                 | 307 ms: 1.02x slower                                                 |
| 2to3                       | 274 ms                                                 | 283 ms: 1.03x slower                                                 |
| regex_effbot               | 3.61 ms                                                | 3.73 ms: 1.03x slower                                                |
| telco                      | 7.10 ms                                                | 7.42 ms: 1.05x slower                                                |
| sympy_sum                  | 169 ms                                                 | 177 ms: 1.05x slower                                                 |
| sqlglot_normalize          | 110 ms                                                 | 116 ms: 1.05x slower                                                 |
| spectral_norm              | 115 ms                                                 | 122 ms: 1.06x slower                                                 |
| bench_thread_pool          | 842 us                                                 | 895 us: 1.06x slower                                                 |
| sympy_expand               | 478 ms                                                 | 508 ms: 1.06x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                 |
| nqueens                    | 83.3 ms                                                | 90.7 ms: 1.09x slower                                                |
| regex_v8                   | 23.1 ms                                                | 25.3 ms: 1.09x slower                                                |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                |
| sqlglot_optimize           | 54.8 ms                                                | 60.6 ms: 1.11x slower                                                |
| sympy_integrate            | 21.4 ms                                                | 23.8 ms: 1.11x slower                                                |
| hexiom                     | 6.41 ms                                                | 7.19 ms: 1.12x slower                                                |
| docutils                   | 2.77 sec                                               | 3.13 sec: 1.13x slower                                               |
| generators                 | 31.2 ms                                                | 36.4 ms: 1.16x slower                                                |
| coverage                   | 72.7 ms                                                | 84.7 ms: 1.17x slower                                                |
| gc_traversal               | 3.79 ms                                                | 4.52 ms: 1.19x slower                                                |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 2.68 ms: 1.82x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 84.5 ms: 3.52x slower                                                |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                         |

Benchmark hidden because not significant (5): sqlite_synth, asyncio_websockets, mdp, dulwich_log, sqlalchemy_declarative
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241117-3.14.0a1+-9808234-JIT/bm-20241117-linux-x86_64-brandtbucher-optimize_off-3.14.0a1+-9808234.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.049x faster
# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.15x