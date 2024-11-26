# Results vs. 3.12.0

- fork: brandtbucher
- ref: jump_backward_0
- machine: linux-x86_64
- commit hash: d0d3a27
- commit date: 2024-10-23
- overall geometric mean: 1.016x faster
- HPT reliability: 89.12%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 288 ms: 1.05x slower                                                    |
| docutils       | 2.77 sec                                               | 3.41 sec: 1.23x slower                                                  |
| tornado_http   | 103 ms                                                 | 112 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                  | 1.12x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 408 ms: 1.41x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 331 ms: 1.36x faster                                                    |
| async_tree_none            | 472 ms                                                 | 350 ms: 1.35x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 434 ms: 1.33x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 584 ms: 1.24x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 956 ms: 1.24x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 940 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 596 ms: 1.22x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.29x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 81.2 ms: 1.19x faster                                                   |
| float          | 84.7 ms                                                | 75.5 ms: 1.12x faster                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 147 ms: 1.01x faster                                                    |
| regex_dna      | 212 ms                                                 | 223 ms: 1.05x slower                                                    |
| regex_effbot   | 3.61 ms                                                | 3.94 ms: 1.09x slower                                                   |
| regex_v8       | 23.1 ms                                                | 26.1 ms: 1.13x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 296 us: 1.10x faster                                                    |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 82.8 ms: 1.08x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 99.4 ms: 1.07x faster                                                   |
| json_loads           | 28.5 us                                                | 26.7 us: 1.07x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 59.8 ms: 1.03x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 226 us: 1.02x faster                                                    |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.22 ms: 1.04x slower                                                   |
| python_startup         | 9.55 ms                                                | 11.9 ms: 1.25x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.14x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.5 ms: 1.13x faster                                                   |
| django_template | 34.6 ms                                                | 40.5 ms: 1.17x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 408 ms: 1.41x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 331 ms: 1.36x faster                                                    |
| deepcopy_memo              | 40.7 us                                                | 30.1 us: 1.35x faster                                                   |
| async_tree_none            | 472 ms                                                 | 350 ms: 1.35x faster                                                    |
| deepcopy                   | 371 us                                                 | 276 us: 1.34x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 434 ms: 1.33x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 584 ms: 1.24x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 956 ms: 1.24x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 940 ms: 1.23x faster                                                    |
| comprehensions             | 21.8 us                                                | 17.8 us: 1.22x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 596 ms: 1.22x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 62.3 ms: 1.21x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 68.3 ms: 1.20x faster                                                   |
| scimark_fft                | 382 ms                                                 | 319 ms: 1.20x faster                                                    |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                  |
| nbody                      | 97.0 ms                                                | 81.2 ms: 1.19x faster                                                   |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.91 us: 1.15x faster                                                   |
| mako                       | 11.9 ms                                                | 10.5 ms: 1.13x faster                                                   |
| chaos                      | 67.0 ms                                                | 59.5 ms: 1.12x faster                                                   |
| float                      | 84.7 ms                                                | 75.5 ms: 1.12x faster                                                   |
| fannkuch                   | 417 ms                                                 | 378 ms: 1.10x faster                                                    |
| pickle_pure_python         | 324 us                                                 | 296 us: 1.10x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                    |
| pprint_safe_repr           | 776 ms                                                 | 715 ms: 1.08x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.66 ms: 1.08x faster                                                   |
| go                         | 139 ms                                                 | 129 ms: 1.08x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 82.8 ms: 1.08x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 99.4 ms: 1.07x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                                  |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.07x faster                                                    |
| json_loads                 | 28.5 us                                                | 26.7 us: 1.07x faster                                                   |
| json                       | 5.26 ms                                                | 4.97 ms: 1.06x faster                                                   |
| raytrace                   | 312 ms                                                 | 295 ms: 1.06x faster                                                    |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                    |
| pyflate                    | 482 ms                                                 | 467 ms: 1.03x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 59.8 ms: 1.03x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.03x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 226 us: 1.02x faster                                                    |
| regex_compile              | 148 ms                                                 | 147 ms: 1.01x faster                                                    |
| mdp                        | 2.63 sec                                               | 2.65 sec: 1.01x slower                                                  |
| async_generators           | 463 ms                                                 | 468 ms: 1.01x slower                                                    |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                    |
| logging_format             | 7.23 us                                                | 7.43 us: 1.03x slower                                                   |
| logging_silent             | 104 ns                                                 | 108 ns: 1.03x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 7.22 ms: 1.04x slower                                                   |
| nqueens                    | 83.3 ms                                                | 87.3 ms: 1.05x slower                                                   |
| 2to3                       | 274 ms                                                 | 288 ms: 1.05x slower                                                    |
| regex_dna                  | 212 ms                                                 | 223 ms: 1.05x slower                                                    |
| sqlglot_parse              | 1.36 ms                                                | 1.44 ms: 1.06x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                    |
| logging_simple             | 6.46 us                                                | 6.90 us: 1.07x slower                                                   |
| richards_super             | 51.5 ms                                                | 55.2 ms: 1.07x slower                                                   |
| telco                      | 7.10 ms                                                | 7.64 ms: 1.08x slower                                                   |
| deltablue                  | 3.72 ms                                                | 4.03 ms: 1.09x slower                                                   |
| richards                   | 45.8 ms                                                | 49.9 ms: 1.09x slower                                                   |
| tornado_http               | 103 ms                                                 | 112 ms: 1.09x slower                                                    |
| regex_effbot               | 3.61 ms                                                | 3.94 ms: 1.09x slower                                                   |
| sqlglot_normalize          | 110 ms                                                 | 121 ms: 1.09x slower                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.85 ms: 1.10x slower                                                   |
| sympy_str                  | 300 ms                                                 | 333 ms: 1.11x slower                                                    |
| sympy_expand               | 478 ms                                                 | 536 ms: 1.12x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 26.1 ms: 1.13x slower                                                   |
| pycparser                  | 1.18 sec                                               | 1.34 sec: 1.14x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 963 us: 1.14x slower                                                    |
| coroutines                 | 23.2 ms                                                | 26.6 ms: 1.15x slower                                                   |
| hexiom                     | 6.41 ms                                                | 7.48 ms: 1.17x slower                                                   |
| generators                 | 31.2 ms                                                | 36.5 ms: 1.17x slower                                                   |
| django_template            | 34.6 ms                                                | 40.5 ms: 1.17x slower                                                   |
| coverage                   | 72.7 ms                                                | 86.9 ms: 1.20x slower                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 67.2 ms: 1.23x slower                                                   |
| docutils                   | 2.77 sec                                               | 3.41 sec: 1.23x slower                                                  |
| sympy_sum                  | 169 ms                                                 | 208 ms: 1.23x slower                                                    |
| python_startup             | 9.55 ms                                                | 11.9 ms: 1.25x slower                                                   |
| gc_traversal               | 3.79 ms                                                | 4.85 ms: 1.28x slower                                                   |
| sympy_integrate            | 21.4 ms                                                | 27.6 ms: 1.29x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 2.69 ms: 1.82x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 89.9 ms: 3.75x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (3): pidigits, dulwich_log, spectral_norm
Ignored benchmarks (16) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241023-3.14.0a1+-d0d3a27-JIT/bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.016x faster
# HPT report

- Reliability score: 89.12% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.18x