# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmup_256
- machine: linux-x86_64
- commit hash: 29895e9
- commit date: 2024-11-10
- overall geometric mean: 1.064x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 278 ms: 1.01x slower                                               |
| docutils       | 2.77 sec                                               | 2.90 sec: 1.05x slower                                             |
| Geometric mean | (ref)                                                  | 1.03x slower                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 380 ms: 1.51x faster                                               |
| async_tree_none            | 472 ms                                                 | 331 ms: 1.42x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 323 ms: 1.39x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 417 ms: 1.39x faster                                               |
| async_tree_io              | 1.16 sec                                               | 861 ms: 1.34x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 569 ms: 1.28x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 584 ms: 1.24x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 977 ms: 1.21x faster                                               |
| Geometric mean             | (ref)                                                  | 1.34x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.9 ms: 1.20x faster                                              |
| float          | 84.7 ms                                                | 76.5 ms: 1.11x faster                                              |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                  | 1.10x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 137 ms: 1.08x faster                                               |
| regex_dna      | 212 ms                                                 | 215 ms: 1.01x slower                                               |
| regex_effbot   | 3.61 ms                                                | 3.69 ms: 1.02x slower                                              |
| regex_v8       | 23.1 ms                                                | 24.8 ms: 1.07x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                             |
| unpickle_pure_python | 230 us                                                 | 196 us: 1.17x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 78.2 ms: 1.14x faster                                              |
| xml_etree_process    | 61.7 ms                                                | 55.5 ms: 1.11x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 100 ms: 1.07x faster                                               |
| json_loads           | 28.5 us                                                | 27.1 us: 1.05x faster                                              |
| pickle_pure_python   | 324 us                                                 | 328 us: 1.01x slower                                               |
| json_dumps           | 10.4 ms                                                | 10.9 ms: 1.05x slower                                              |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                              |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                              |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.2 ms: 1.16x faster                                              |
| django_template | 34.6 ms                                                | 35.9 ms: 1.04x slower                                              |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 380 ms: 1.51x faster                                               |
| async_tree_none            | 472 ms                                                 | 331 ms: 1.42x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 323 ms: 1.39x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 417 ms: 1.39x faster                                               |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                              |
| deepcopy                   | 371 us                                                 | 272 us: 1.37x faster                                               |
| async_tree_io              | 1.16 sec                                               | 861 ms: 1.34x faster                                               |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 569 ms: 1.28x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 584 ms: 1.24x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.76 us: 1.21x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 977 ms: 1.21x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 68.1 ms: 1.20x faster                                              |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                             |
| nbody                      | 97.0 ms                                                | 80.9 ms: 1.20x faster                                              |
| scimark_fft                | 382 ms                                                 | 322 ms: 1.19x faster                                               |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                              |
| logging_format             | 7.23 us                                                | 6.15 us: 1.18x faster                                              |
| unpickle_pure_python       | 230 us                                                 | 196 us: 1.17x faster                                               |
| mako                       | 11.9 ms                                                | 10.2 ms: 1.16x faster                                              |
| scimark_monte_carlo        | 75.1 ms                                                | 64.6 ms: 1.16x faster                                              |
| richards                   | 45.8 ms                                                | 39.7 ms: 1.16x faster                                              |
| logging_simple             | 6.46 us                                                | 5.62 us: 1.15x faster                                              |
| xml_etree_generate         | 89.2 ms                                                | 78.2 ms: 1.14x faster                                              |
| deltablue                  | 3.72 ms                                                | 3.26 ms: 1.14x faster                                              |
| raytrace                   | 312 ms                                                 | 275 ms: 1.14x faster                                               |
| chaos                      | 67.0 ms                                                | 59.3 ms: 1.13x faster                                              |
| richards_super             | 51.5 ms                                                | 46.1 ms: 1.12x faster                                              |
| xml_etree_process          | 61.7 ms                                                | 55.5 ms: 1.11x faster                                              |
| float                      | 84.7 ms                                                | 76.5 ms: 1.11x faster                                              |
| fannkuch                   | 417 ms                                                 | 383 ms: 1.09x faster                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.65 ms: 1.09x faster                                              |
| regex_compile              | 148 ms                                                 | 137 ms: 1.08x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                               |
| pyflate                    | 482 ms                                                 | 451 ms: 1.07x faster                                               |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.5 ms: 1.07x faster                                              |
| xml_etree_iterparse        | 107 ms                                                 | 100 ms: 1.07x faster                                               |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.06x faster                                               |
| go                         | 139 ms                                                 | 131 ms: 1.06x faster                                               |
| json                       | 5.26 ms                                                | 4.99 ms: 1.05x faster                                              |
| json_loads                 | 28.5 us                                                | 27.1 us: 1.05x faster                                              |
| logging_silent             | 104 ns                                                 | 99.5 ns: 1.05x faster                                              |
| pprint_safe_repr           | 776 ms                                                 | 739 ms: 1.05x faster                                               |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                               |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.04x faster                                               |
| mdp                        | 2.63 sec                                               | 2.55 sec: 1.03x faster                                             |
| async_generators           | 463 ms                                                 | 449 ms: 1.03x faster                                               |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                              |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.03x faster                                             |
| dulwich_log                | 68.5 ms                                                | 67.4 ms: 1.02x faster                                              |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                             |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                              |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.01x faster                                               |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                              |
| sqlalchemy_declarative     | 147 ms                                                 | 145 ms: 1.01x faster                                               |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                               |
| sympy_sum                  | 169 ms                                                 | 170 ms: 1.01x slower                                               |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                               |
| 2to3                       | 274 ms                                                 | 278 ms: 1.01x slower                                               |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.01x slower                                               |
| pickle_pure_python         | 324 us                                                 | 328 us: 1.01x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                              |
| regex_effbot               | 3.61 ms                                                | 3.69 ms: 1.02x slower                                              |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.03x slower                                               |
| django_template            | 34.6 ms                                                | 35.9 ms: 1.04x slower                                              |
| sympy_expand               | 478 ms                                                 | 500 ms: 1.05x slower                                               |
| docutils                   | 2.77 sec                                               | 2.90 sec: 1.05x slower                                             |
| nqueens                    | 83.3 ms                                                | 87.6 ms: 1.05x slower                                              |
| bench_thread_pool          | 842 us                                                 | 886 us: 1.05x slower                                               |
| json_dumps                 | 10.4 ms                                                | 10.9 ms: 1.05x slower                                              |
| sqlglot_optimize           | 54.8 ms                                                | 58.1 ms: 1.06x slower                                              |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                               |
| sympy_integrate            | 21.4 ms                                                | 22.8 ms: 1.06x slower                                              |
| regex_v8                   | 23.1 ms                                                | 24.8 ms: 1.07x slower                                              |
| telco                      | 7.10 ms                                                | 7.72 ms: 1.09x slower                                              |
| hexiom                     | 6.41 ms                                                | 7.07 ms: 1.10x slower                                              |
| coverage                   | 72.7 ms                                                | 84.0 ms: 1.16x slower                                              |
| gc_traversal               | 3.79 ms                                                | 4.38 ms: 1.16x slower                                              |
| generators                 | 31.2 ms                                                | 36.7 ms: 1.18x slower                                              |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                              |
| create_gc_cycles           | 1.48 ms                                                | 2.66 ms: 1.80x slower                                              |
| bench_mp_pool              | 24.0 ms                                                | 80.3 ms: 3.35x slower                                              |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                       |

Benchmark hidden because not significant (2): sympy_str, sqlglot_transpile
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241110-3.14.0a1+-29895e9-JIT/bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.064x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.11x