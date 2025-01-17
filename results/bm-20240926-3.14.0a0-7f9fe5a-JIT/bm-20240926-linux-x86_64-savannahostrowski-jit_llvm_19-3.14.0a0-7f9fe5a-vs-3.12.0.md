# Results vs. 3.12.0

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: linux-x86_64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.089x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.77 sec                                               | 2.94 sec: 1.06x slower                                                  |
| tornado_http   | 103 ms                                                 | 94.6 ms: 1.09x faster                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 315 ms: 1.50x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 388 ms: 1.48x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 308 ms: 1.46x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 397 ms: 1.45x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 875 ms: 1.35x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 885 ms: 1.31x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 556 ms: 1.30x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 572 ms: 1.27x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.1 ms: 1.21x faster                                                   |
| nbody          | 97.0 ms                                                | 81.8 ms: 1.19x faster                                                   |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.13x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 142 ms: 1.04x faster                                                    |
| regex_effbot   | 3.61 ms                                                | 3.72 ms: 1.03x slower                                                   |
| regex_v8       | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 78.1 ms: 1.14x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 55.0 ms: 1.12x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.09x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 98.6 ms: 1.08x faster                                                   |
| unpickle             | 15.9 us                                                | 14.7 us: 1.08x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                    |
| pickle_dict          | 35.5 us                                                | 33.3 us: 1.07x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 307 us: 1.05x faster                                                    |
| json_loads           | 28.5 us                                                | 27.2 us: 1.05x faster                                                   |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                   |
| pickle_list          | 5.08 us                                                | 5.20 us: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                            |

Benchmark hidden because not significant (2): pickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                   |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                   |
| django_template | 34.6 ms                                                | 35.5 ms: 1.03x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.7 us: 1.53x faster                                                   |
| async_tree_none            | 472 ms                                                 | 315 ms: 1.50x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 388 ms: 1.48x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 308 ms: 1.46x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 397 ms: 1.45x faster                                                    |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 875 ms: 1.35x faster                                                    |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 885 ms: 1.31x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 556 ms: 1.30x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 572 ms: 1.27x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 2.65 us: 1.26x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 66.8 ms: 1.23x faster                                                   |
| scimark_fft                | 382 ms                                                 | 312 ms: 1.22x faster                                                    |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                   |
| float                      | 84.7 ms                                                | 70.1 ms: 1.21x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 62.8 ms: 1.20x faster                                                   |
| logging_format             | 7.23 us                                                | 6.05 us: 1.19x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                  |
| nbody                      | 97.0 ms                                                | 81.8 ms: 1.19x faster                                                   |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.19 ms: 1.17x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.58 us: 1.16x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.39 ms: 1.15x faster                                                   |
| richards                   | 45.8 ms                                                | 39.8 ms: 1.15x faster                                                   |
| richards_super             | 51.5 ms                                                | 44.9 ms: 1.15x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 78.1 ms: 1.14x faster                                                   |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                                    |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 55.0 ms: 1.12x faster                                                   |
| chaos                      | 67.0 ms                                                | 59.7 ms: 1.12x faster                                                   |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.09x faster                                                    |
| fannkuch                   | 417 ms                                                 | 384 ms: 1.09x faster                                                    |
| tornado_http               | 103 ms                                                 | 94.6 ms: 1.09x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 98.6 ms: 1.08x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 109 ms: 1.08x faster                                                    |
| unpickle                   | 15.9 us                                                | 14.7 us: 1.08x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                                    |
| pickle_dict                | 35.5 us                                                | 33.3 us: 1.07x faster                                                   |
| go                         | 139 ms                                                 | 132 ms: 1.06x faster                                                    |
| pickle_pure_python         | 324 us                                                 | 307 us: 1.05x faster                                                    |
| pyflate                    | 482 ms                                                 | 458 ms: 1.05x faster                                                    |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                    |
| json_loads                 | 28.5 us                                                | 27.2 us: 1.05x faster                                                   |
| regex_compile              | 148 ms                                                 | 142 ms: 1.04x faster                                                    |
| sqlite_synth               | 2.83 us                                                | 2.74 us: 1.03x faster                                                   |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                   |
| json                       | 5.26 ms                                                | 5.11 ms: 1.03x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.03x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                  |
| async_generators           | 463 ms                                                 | 455 ms: 1.02x faster                                                    |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.01x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.60 sec: 1.01x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 67.9 ms: 1.01x faster                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.67 ms: 1.01x faster                                                   |
| sympy_str                  | 300 ms                                                 | 298 ms: 1.01x faster                                                    |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                  |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.01x slower                                                    |
| sympy_sum                  | 169 ms                                                 | 172 ms: 1.02x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                   |
| pickle_list                | 5.08 us                                                | 5.20 us: 1.02x slower                                                   |
| django_template            | 34.6 ms                                                | 35.5 ms: 1.03x slower                                                   |
| nqueens                    | 83.3 ms                                                | 85.6 ms: 1.03x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                                    |
| regex_effbot               | 3.61 ms                                                | 3.72 ms: 1.03x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                   |
| gc_traversal               | 3.79 ms                                                | 3.97 ms: 1.05x slower                                                   |
| sympy_expand               | 478 ms                                                 | 502 ms: 1.05x slower                                                    |
| sqlglot_optimize           | 54.8 ms                                                | 57.7 ms: 1.05x slower                                                   |
| generators                 | 31.2 ms                                                | 33.1 ms: 1.06x slower                                                   |
| sympy_integrate            | 21.4 ms                                                | 22.7 ms: 1.06x slower                                                   |
| docutils                   | 2.77 sec                                               | 2.94 sec: 1.06x slower                                                  |
| hexiom                     | 6.41 ms                                                | 6.87 ms: 1.07x slower                                                   |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                   |
| telco                      | 7.10 ms                                                | 7.86 ms: 1.11x slower                                                   |
| coverage                   | 72.7 ms                                                | 84.8 ms: 1.17x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                   |
| unpack_sequence            | 54.0 ns                                                | 112 ns: 2.07x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                            |

Benchmark hidden because not significant (9): pprint_safe_repr, bench_thread_pool, logging_silent, 2to3, pickle, bench_mp_pool, asyncio_tcp, regex_dna, unpickle_list
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240926-3.14.0a0-7f9fe5a-JIT/bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.089x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.06x