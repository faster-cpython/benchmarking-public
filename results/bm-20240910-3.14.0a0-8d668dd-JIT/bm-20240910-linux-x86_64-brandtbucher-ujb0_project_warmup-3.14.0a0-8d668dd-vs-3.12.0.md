# Results vs. 3.12.0

- fork: brandtbucher
- ref: ujb0_project_warmup
- machine: linux-x86_64
- commit hash: 8d668dd
- commit date: 2024-09-10
- overall geometric mean: 1.041x faster
- HPT reliability: 89.57%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 289 ms: 1.05x slower                                                       |
| docutils       | 2.77 sec                                               | 3.48 sec: 1.26x slower                                                     |
| tornado_http   | 103 ms                                                 | 114 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                  | 1.14x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 316 ms: 1.42x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 411 ms: 1.40x faster                                                       |
| async_tree_none            | 472 ms                                                 | 338 ms: 1.39x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 423 ms: 1.37x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 547 ms: 1.33x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 913 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 571 ms: 1.27x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 953 ms: 1.21x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.33x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 68.4 ms: 1.24x faster                                                      |
| nbody          | 97.0 ms                                                | 79.8 ms: 1.22x faster                                                      |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.15x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 151 ms: 1.02x slower                                                       |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                       |
| regex_effbot   | 3.61 ms                                                | 3.72 ms: 1.03x slower                                                      |
| regex_v8       | 23.1 ms                                                | 25.8 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                  | 1.05x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 230 us                                                 | 196 us: 1.17x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 54.4 ms: 1.13x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 78.7 ms: 1.13x faster                                                      |
| tomli_loads          | 2.33 sec                                               | 2.13 sec: 1.10x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 98.0 ms: 1.09x faster                                                      |
| unpickle             | 15.9 us                                                | 14.9 us: 1.06x faster                                                      |
| json_dumps           | 10.4 ms                                                | 9.95 ms: 1.04x faster                                                      |
| pickle_dict          | 35.5 us                                                | 34.2 us: 1.04x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.02x faster                                                       |
| unpickle_list        | 5.29 us                                                | 5.23 us: 1.01x faster                                                      |
| pickle_list          | 5.08 us                                                | 5.17 us: 1.02x slower                                                      |
| json_loads           | 28.5 us                                                | 29.7 us: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                               |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                      |
| python_startup         | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.86 ms: 1.21x faster                                                      |
| django_template | 34.6 ms                                                | 40.4 ms: 1.17x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 27.3 us: 1.49x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 316 ms: 1.42x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 411 ms: 1.40x faster                                                       |
| async_tree_none            | 472 ms                                                 | 338 ms: 1.39x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 423 ms: 1.37x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 547 ms: 1.33x faster                                                       |
| deepcopy                   | 371 us                                                 | 280 us: 1.33x faster                                                       |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 913 ms: 1.29x faster                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 58.8 ms: 1.28x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 571 ms: 1.27x faster                                                       |
| float                      | 84.7 ms                                                | 68.4 ms: 1.24x faster                                                      |
| scimark_fft                | 382 ms                                                 | 310 ms: 1.23x faster                                                       |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.22x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 67.2 ms: 1.22x faster                                                      |
| nbody                      | 97.0 ms                                                | 79.8 ms: 1.22x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 953 ms: 1.21x faster                                                       |
| mako                       | 11.9 ms                                                | 9.86 ms: 1.21x faster                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.27 ms: 1.19x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 196 us: 1.17x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 54.4 ms: 1.13x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 78.7 ms: 1.13x faster                                                      |
| chaos                      | 67.0 ms                                                | 59.9 ms: 1.12x faster                                                      |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.11x faster                                                       |
| raytrace                   | 312 ms                                                 | 281 ms: 1.11x faster                                                       |
| fannkuch                   | 417 ms                                                 | 376 ms: 1.11x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.83 us: 1.11x faster                                                      |
| logging_format             | 7.23 us                                                | 6.53 us: 1.11x faster                                                      |
| pyflate                    | 482 ms                                                 | 436 ms: 1.11x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 2.13 sec: 1.10x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.10x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                 | 98.0 ms: 1.09x faster                                                      |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                                       |
| scimark_lu                 | 118 ms                                                 | 110 ms: 1.07x faster                                                       |
| gc_traversal               | 3.79 ms                                                | 3.55 ms: 1.07x faster                                                      |
| unpickle                   | 15.9 us                                                | 14.9 us: 1.06x faster                                                      |
| json_dumps                 | 10.4 ms                                                | 9.95 ms: 1.04x faster                                                      |
| pickle_dict                | 35.5 us                                                | 34.2 us: 1.04x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.59 ms: 1.04x faster                                                      |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                       |
| logging_silent             | 104 ns                                                 | 102 ns: 1.03x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.02x faster                                                       |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.02x faster                                                      |
| async_generators           | 463 ms                                                 | 457 ms: 1.01x faster                                                       |
| unpickle_list              | 5.29 us                                                | 5.23 us: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                       |
| pickle_list                | 5.08 us                                                | 5.17 us: 1.02x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 24.4 ms: 1.02x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 161 us: 1.02x slower                                                       |
| regex_compile              | 148 ms                                                 | 151 ms: 1.02x slower                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.02x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                      |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                       |
| regex_effbot               | 3.61 ms                                                | 3.72 ms: 1.03x slower                                                      |
| mdp                        | 2.63 sec                                               | 2.72 sec: 1.03x slower                                                     |
| coroutines                 | 23.2 ms                                                | 24.1 ms: 1.04x slower                                                      |
| json_loads                 | 28.5 us                                                | 29.7 us: 1.04x slower                                                      |
| richards                   | 45.8 ms                                                | 48.3 ms: 1.05x slower                                                      |
| 2to3                       | 274 ms                                                 | 289 ms: 1.05x slower                                                       |
| bench_thread_pool          | 842 us                                                 | 892 us: 1.06x slower                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.66 sec: 1.06x slower                                                     |
| asyncio_tcp                | 491 ms                                                 | 525 ms: 1.07x slower                                                       |
| telco                      | 7.10 ms                                                | 7.62 ms: 1.07x slower                                                      |
| richards_super             | 51.5 ms                                                | 55.8 ms: 1.08x slower                                                      |
| tornado_http               | 103 ms                                                 | 114 ms: 1.11x slower                                                       |
| generators                 | 31.2 ms                                                | 34.7 ms: 1.11x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 25.8 ms: 1.11x slower                                                      |
| python_startup             | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                      |
| sympy_str                  | 300 ms                                                 | 336 ms: 1.12x slower                                                       |
| pycparser                  | 1.18 sec                                               | 1.35 sec: 1.14x slower                                                     |
| sqlglot_normalize          | 110 ms                                                 | 126 ms: 1.15x slower                                                       |
| sympy_expand               | 478 ms                                                 | 554 ms: 1.16x slower                                                       |
| django_template            | 34.6 ms                                                | 40.4 ms: 1.17x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 64.0 ms: 1.17x slower                                                      |
| hexiom                     | 6.41 ms                                                | 7.49 ms: 1.17x slower                                                      |
| sympy_integrate            | 21.4 ms                                                | 25.3 ms: 1.18x slower                                                      |
| coverage                   | 72.7 ms                                                | 86.8 ms: 1.19x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 1.78 ms: 1.20x slower                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.68 ms: 1.23x slower                                                      |
| sympy_sum                  | 169 ms                                                 | 209 ms: 1.24x slower                                                       |
| sqlglot_transpile          | 1.68 ms                                                | 2.08 ms: 1.24x slower                                                      |
| docutils                   | 2.77 sec                                               | 3.48 sec: 1.26x slower                                                     |
| go                         | 139 ms                                                 | 176 ms: 1.26x slower                                                       |
| unpack_sequence            | 54.0 ns                                                | 105 ns: 1.95x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (4): json, pickle, pprint_safe_repr, nqueens
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240910-3.14.0a0-8d668dd-JIT/bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.041x faster
# HPT report

- Reliability score: 89.57% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.13x