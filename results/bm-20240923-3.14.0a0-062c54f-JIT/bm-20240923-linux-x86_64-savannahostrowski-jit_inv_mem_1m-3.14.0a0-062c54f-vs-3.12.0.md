# Results vs. 3.12.0

- fork: savannahostrowski
- ref: jit_inv_mem_1m
- machine: linux-x86_64
- commit hash: 062c54f
- commit date: 2024-09-23
- overall geometric mean: 1.084x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 277 ms: 1.01x slower                                                       |
| docutils       | 2.77 sec                                               | 2.93 sec: 1.06x slower                                                     |
| tornado_http   | 103 ms                                                 | 95.0 ms: 1.08x faster                                                      |
| Geometric mean | (ref)                                                  | 1.00x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 313 ms: 1.50x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.46x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 396 ms: 1.46x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 872 ms: 1.36x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 858 ms: 1.35x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 555 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 570 ms: 1.27x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.40x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.6 ms: 1.22x faster                                                      |
| nbody          | 97.0 ms                                                | 84.1 ms: 1.15x faster                                                      |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.12x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 143 ms: 1.04x faster                                                       |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                       |
| regex_effbot   | 3.61 ms                                                | 3.80 ms: 1.05x slower                                                      |
| regex_v8       | 23.1 ms                                                | 24.6 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 77.8 ms: 1.15x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 54.5 ms: 1.13x faster                                                      |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                       |
| unpickle             | 15.9 us                                                | 14.5 us: 1.09x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 98.4 ms: 1.09x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 304 us: 1.06x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                       |
| json_dumps           | 10.4 ms                                                | 9.93 ms: 1.05x faster                                                      |
| json_loads           | 28.5 us                                                | 27.6 us: 1.03x faster                                                      |
| pickle_dict          | 35.5 us                                                | 34.5 us: 1.03x faster                                                      |
| pickle               | 11.6 us                                                | 11.5 us: 1.01x faster                                                      |
| pickle_list          | 5.08 us                                                | 5.10 us: 1.00x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                      |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.87 ms: 1.21x faster                                                      |
| django_template | 34.6 ms                                                | 36.7 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 313 ms: 1.50x faster                                                       |
| deepcopy_memo              | 40.7 us                                                | 27.1 us: 1.50x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.46x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 396 ms: 1.46x faster                                                       |
| deepcopy                   | 371 us                                                 | 263 us: 1.41x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 872 ms: 1.36x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 858 ms: 1.35x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 555 ms: 1.31x faster                                                       |
| comprehensions             | 21.8 us                                                | 16.9 us: 1.29x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 570 ms: 1.27x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 66.7 ms: 1.23x faster                                                      |
| scimark_fft                | 382 ms                                                 | 312 ms: 1.22x faster                                                       |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                      |
| float                      | 84.7 ms                                                | 69.6 ms: 1.22x faster                                                      |
| mako                       | 11.9 ms                                                | 9.87 ms: 1.21x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.26 ms: 1.19x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 63.3 ms: 1.19x faster                                                      |
| logging_format             | 7.23 us                                                | 6.15 us: 1.17x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.59 us: 1.16x faster                                                      |
| nbody                      | 97.0 ms                                                | 84.1 ms: 1.15x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.23 ms: 1.15x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 77.8 ms: 1.15x faster                                                      |
| chaos                      | 67.0 ms                                                | 58.9 ms: 1.14x faster                                                      |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 54.5 ms: 1.13x faster                                                      |
| richards                   | 45.8 ms                                                | 40.7 ms: 1.13x faster                                                      |
| richards_super             | 51.5 ms                                                | 46.7 ms: 1.10x faster                                                      |
| fannkuch                   | 417 ms                                                 | 379 ms: 1.10x faster                                                       |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.10x faster                                                       |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                       |
| unpickle                   | 15.9 us                                                | 14.5 us: 1.09x faster                                                      |
| spectral_norm              | 115 ms                                                 | 105 ms: 1.09x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                 | 98.4 ms: 1.09x faster                                                      |
| tornado_http               | 103 ms                                                 | 95.0 ms: 1.08x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 111 ms: 1.07x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 304 us: 1.06x faster                                                       |
| pyflate                    | 482 ms                                                 | 454 ms: 1.06x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                       |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                       |
| json_dumps                 | 10.4 ms                                                | 9.93 ms: 1.05x faster                                                      |
| go                         | 139 ms                                                 | 134 ms: 1.04x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 745 ms: 1.04x faster                                                       |
| regex_compile              | 148 ms                                                 | 143 ms: 1.04x faster                                                       |
| gc_traversal               | 3.79 ms                                                | 3.66 ms: 1.04x faster                                                      |
| json_loads                 | 28.5 us                                                | 27.6 us: 1.03x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                     |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                                      |
| pickle_dict                | 35.5 us                                                | 34.5 us: 1.03x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.02x faster                                                      |
| mdp                        | 2.63 sec                                               | 2.59 sec: 1.02x faster                                                     |
| logging_silent             | 104 ns                                                 | 103 ns: 1.02x faster                                                       |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                       |
| json                       | 5.26 ms                                                | 5.21 ms: 1.01x faster                                                      |
| async_generators           | 463 ms                                                 | 459 ms: 1.01x faster                                                       |
| pickle                     | 11.6 us                                                | 11.5 us: 1.01x faster                                                      |
| dulwich_log                | 68.5 ms                                                | 68.2 ms: 1.01x faster                                                      |
| bench_thread_pool          | 842 us                                                 | 839 us: 1.00x faster                                                       |
| pickle_list                | 5.08 us                                                | 5.10 us: 1.00x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.68 ms                                                | 1.70 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                     |
| 2to3                       | 274 ms                                                 | 277 ms: 1.01x slower                                                       |
| asyncio_tcp                | 491 ms                                                 | 496 ms: 1.01x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                      |
| sympy_str                  | 300 ms                                                 | 305 ms: 1.02x slower                                                       |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                       |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.03x slower                                                       |
| sympy_sum                  | 169 ms                                                 | 174 ms: 1.03x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                       |
| regex_effbot               | 3.61 ms                                                | 3.80 ms: 1.05x slower                                                      |
| docutils                   | 2.77 sec                                               | 2.93 sec: 1.06x slower                                                     |
| django_template            | 34.6 ms                                                | 36.7 ms: 1.06x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 24.6 ms: 1.07x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 58.6 ms: 1.07x slower                                                      |
| nqueens                    | 83.3 ms                                                | 89.0 ms: 1.07x slower                                                      |
| sympy_integrate            | 21.4 ms                                                | 23.0 ms: 1.07x slower                                                      |
| sympy_expand               | 478 ms                                                 | 514 ms: 1.08x slower                                                       |
| hexiom                     | 6.41 ms                                                | 6.97 ms: 1.09x slower                                                      |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                      |
| generators                 | 31.2 ms                                                | 34.9 ms: 1.12x slower                                                      |
| telco                      | 7.10 ms                                                | 8.08 ms: 1.14x slower                                                      |
| coverage                   | 72.7 ms                                                | 85.0 ms: 1.17x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                                      |
| unpack_sequence            | 54.0 ns                                                | 105 ns: 1.94x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                               |

Benchmark hidden because not significant (3): bench_mp_pool, unpickle_list, pycparser
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240923-3.14.0a0-062c54f-JIT/bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.084x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.04x