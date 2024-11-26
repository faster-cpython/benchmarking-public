# Results vs. 3.12.0

- fork: brandtbucher
- ref: jb0_invalidate
- machine: linux-x86_64
- commit hash: 69e9a0e
- commit date: 2024-10-24
- overall geometric mean: 1.011x faster
- HPT reliability: 81.38%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 284 ms: 1.04x slower                                                   |
| docutils       | 2.77 sec                                               | 3.36 sec: 1.21x slower                                                 |
| tornado_http   | 103 ms                                                 | 112 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 407 ms: 1.41x faster                                                   |
| async_tree_none            | 472 ms                                                 | 347 ms: 1.36x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 332 ms: 1.35x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 434 ms: 1.33x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 953 ms: 1.24x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 589 ms: 1.23x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 950 ms: 1.22x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 599 ms: 1.21x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.29x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 82.4 ms: 1.18x faster                                                  |
| float          | 84.7 ms                                                | 75.3 ms: 1.13x faster                                                  |
| pidigits       | 187 ms                                                 | 188 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 147 ms: 1.01x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.74 ms: 1.04x slower                                                  |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                                   |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.99 sec: 1.17x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 295 us: 1.10x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 99.4 ms: 1.07x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 83.2 ms: 1.07x faster                                                  |
| json_loads           | 28.5 us                                                | 27.0 us: 1.06x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 59.8 ms: 1.03x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 225 us: 1.02x faster                                                   |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.22 ms: 1.04x slower                                                  |
| python_startup         | 9.55 ms                                                | 11.9 ms: 1.25x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.14x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.6 ms: 1.12x faster                                                  |
| django_template | 34.6 ms                                                | 40.1 ms: 1.16x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 407 ms: 1.41x faster                                                   |
| async_tree_none            | 472 ms                                                 | 347 ms: 1.36x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 332 ms: 1.35x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 30.2 us: 1.35x faster                                                  |
| deepcopy                   | 371 us                                                 | 275 us: 1.35x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 434 ms: 1.33x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 953 ms: 1.24x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 589 ms: 1.23x faster                                                   |
| comprehensions             | 21.8 us                                                | 17.9 us: 1.22x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 950 ms: 1.22x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 599 ms: 1.21x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 62.4 ms: 1.20x faster                                                  |
| scimark_fft                | 382 ms                                                 | 319 ms: 1.20x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 69.1 ms: 1.18x faster                                                  |
| nbody                      | 97.0 ms                                                | 82.4 ms: 1.18x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.99 sec: 1.17x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.87 us: 1.16x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.8 ms: 1.15x faster                                                  |
| chaos                      | 67.0 ms                                                | 59.4 ms: 1.13x faster                                                  |
| float                      | 84.7 ms                                                | 75.3 ms: 1.13x faster                                                  |
| mako                       | 11.9 ms                                                | 10.6 ms: 1.12x faster                                                  |
| fannkuch                   | 417 ms                                                 | 378 ms: 1.10x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 295 us: 1.10x faster                                                   |
| go                         | 139 ms                                                 | 129 ms: 1.08x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 99.4 ms: 1.07x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 723 ms: 1.07x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 83.2 ms: 1.07x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.73 ms: 1.07x faster                                                  |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.06x faster                                                   |
| json_loads                 | 28.5 us                                                | 27.0 us: 1.06x faster                                                  |
| raytrace                   | 312 ms                                                 | 299 ms: 1.04x faster                                                   |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.04x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.04x faster                                                   |
| json                       | 5.26 ms                                                | 5.08 ms: 1.04x faster                                                  |
| pyflate                    | 482 ms                                                 | 466 ms: 1.04x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 59.8 ms: 1.03x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 225 us: 1.02x faster                                                   |
| regex_compile              | 148 ms                                                 | 147 ms: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 188 ms: 1.01x slower                                                   |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.01x slower                                                   |
| asyncio_websockets         | 551 ms                                                 | 559 ms: 1.01x slower                                                   |
| 2to3                       | 274 ms                                                 | 284 ms: 1.04x slower                                                   |
| regex_effbot               | 3.61 ms                                                | 3.74 ms: 1.04x slower                                                  |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.22 ms: 1.04x slower                                                  |
| logging_silent             | 104 ns                                                 | 109 ns: 1.04x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.05x slower                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.43 ms: 1.05x slower                                                  |
| logging_format             | 7.23 us                                                | 7.61 us: 1.05x slower                                                  |
| mdp                        | 2.63 sec                                               | 2.81 sec: 1.07x slower                                                 |
| nqueens                    | 83.3 ms                                                | 89.3 ms: 1.07x slower                                                  |
| telco                      | 7.10 ms                                                | 7.62 ms: 1.07x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                  |
| richards_super             | 51.5 ms                                                | 55.4 ms: 1.07x slower                                                  |
| sqlglot_normalize          | 110 ms                                                 | 119 ms: 1.08x slower                                                   |
| richards                   | 45.8 ms                                                | 49.6 ms: 1.08x slower                                                  |
| logging_simple             | 6.46 us                                                | 7.01 us: 1.09x slower                                                  |
| deltablue                  | 3.72 ms                                                | 4.04 ms: 1.09x slower                                                  |
| tornado_http               | 103 ms                                                 | 112 ms: 1.09x slower                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.85 ms: 1.10x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                  |
| pycparser                  | 1.18 sec                                               | 1.31 sec: 1.11x slower                                                 |
| sympy_str                  | 300 ms                                                 | 335 ms: 1.12x slower                                                   |
| hexiom                     | 6.41 ms                                                | 7.17 ms: 1.12x slower                                                  |
| sympy_expand               | 478 ms                                                 | 536 ms: 1.12x slower                                                   |
| coroutines                 | 23.2 ms                                                | 26.5 ms: 1.14x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 967 us: 1.15x slower                                                   |
| django_template            | 34.6 ms                                                | 40.1 ms: 1.16x slower                                                  |
| generators                 | 31.2 ms                                                | 36.7 ms: 1.17x slower                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 174 ms: 1.19x slower                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 65.1 ms: 1.19x slower                                                  |
| coverage                   | 72.7 ms                                                | 86.9 ms: 1.19x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.55 ms: 1.20x slower                                                  |
| docutils                   | 2.77 sec                                               | 3.36 sec: 1.21x slower                                                 |
| sqlalchemy_imperative      | 18.7 ms                                                | 22.7 ms: 1.22x slower                                                  |
| sympy_integrate            | 21.4 ms                                                | 26.5 ms: 1.24x slower                                                  |
| sympy_sum                  | 169 ms                                                 | 209 ms: 1.24x slower                                                   |
| python_startup             | 9.55 ms                                                | 11.9 ms: 1.25x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.69 ms: 1.82x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 89.3 ms: 3.72x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (2): async_generators, dulwich_log
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241024-3.14.0a1+-69e9a0e-JIT/bm-20241024-linux-x86_64-brandtbucher-jb0_invalidate-3.14.0a1+-69e9a0e.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.011x faster
# HPT report

- Reliability score: 81.38% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.19x