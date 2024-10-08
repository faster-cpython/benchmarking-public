# Results vs. 3.12.0

- fork: serhiy-storchaka
- ref: pickle_save_global3
- machine: linux-x86_64
- commit hash: 5efa5a5
- commit date: 2024-07-30
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 263 ms: 1.04x faster                                                             |
| docutils       | 2.77 sec                                               | 2.73 sec: 1.02x faster                                                           |
| tornado_http   | 103 ms                                                 | 90.2 ms: 1.14x faster                                                            |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 391 ms: 1.47x faster                                                             |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.46x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 531 ms: 1.37x faster                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 869 ms: 1.36x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 425 ms: 1.36x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 903 ms: 1.28x faster                                                             |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 86.5 ms: 1.12x faster                                                            |
| float          | 84.7 ms                                                | 78.6 ms: 1.08x faster                                                            |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                             |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                             |
| regex_effbot   | 3.61 ms                                                | 3.83 ms: 1.06x slower                                                            |
| regex_dna      | 212 ms                                                 | 227 ms: 1.07x slower                                                             |
| regex_v8       | 23.1 ms                                                | 26.4 ms: 1.14x slower                                                            |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.04 sec: 1.14x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                             |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                                             |
| xml_etree_process    | 61.7 ms                                                | 58.6 ms: 1.05x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 84.9 ms: 1.05x faster                                                            |
| json_loads           | 28.5 us                                                | 27.8 us: 1.03x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.01x faster                                                             |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                            |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                     |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                            |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.09x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                            |
| django_template | 34.6 ms                                                | 35.0 ms: 1.01x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 391 ms: 1.47x faster                                                             |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.46x faster                                                             |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                             |
| deepcopy_memo              | 40.7 us                                                | 29.7 us: 1.37x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 531 ms: 1.37x faster                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 869 ms: 1.36x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 425 ms: 1.36x faster                                                             |
| comprehensions             | 21.8 us                                                | 16.9 us: 1.29x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 903 ms: 1.28x faster                                                             |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                                            |
| raytrace                   | 312 ms                                                 | 258 ms: 1.21x faster                                                             |
| logging_format             | 7.23 us                                                | 6.01 us: 1.20x faster                                                            |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                            |
| logging_simple             | 6.46 us                                                | 5.44 us: 1.19x faster                                                            |
| deltablue                  | 3.72 ms                                                | 3.23 ms: 1.15x faster                                                            |
| tomli_loads                | 2.33 sec                                               | 2.04 sec: 1.14x faster                                                           |
| chaos                      | 67.0 ms                                                | 58.6 ms: 1.14x faster                                                            |
| tornado_http               | 103 ms                                                 | 90.2 ms: 1.14x faster                                                            |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                             |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                                             |
| crypto_pyaes               | 81.9 ms                                                | 72.9 ms: 1.12x faster                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.51 ms: 1.12x faster                                                            |
| nbody                      | 97.0 ms                                                | 86.5 ms: 1.12x faster                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 67.2 ms: 1.12x faster                                                            |
| sympy_str                  | 300 ms                                                 | 270 ms: 1.11x faster                                                             |
| generators                 | 31.2 ms                                                | 28.5 ms: 1.10x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 19.7 ms: 1.09x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                             |
| float                      | 84.7 ms                                                | 78.6 ms: 1.08x faster                                                            |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                                             |
| bench_thread_pool          | 842 us                                                 | 786 us: 1.07x faster                                                             |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.07x faster                                                            |
| gc_traversal               | 3.79 ms                                                | 3.56 ms: 1.07x faster                                                            |
| scimark_fft                | 382 ms                                                 | 359 ms: 1.06x faster                                                             |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                                            |
| spectral_norm              | 115 ms                                                 | 109 ms: 1.06x faster                                                             |
| xml_etree_process          | 61.7 ms                                                | 58.6 ms: 1.05x faster                                                            |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                             |
| xml_etree_generate         | 89.2 ms                                                | 84.9 ms: 1.05x faster                                                            |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.05x faster                                                             |
| nqueens                    | 83.3 ms                                                | 79.6 ms: 1.05x faster                                                            |
| async_generators           | 463 ms                                                 | 443 ms: 1.05x faster                                                             |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                           |
| 2to3                       | 274 ms                                                 | 263 ms: 1.04x faster                                                             |
| pprint_safe_repr           | 776 ms                                                 | 744 ms: 1.04x faster                                                             |
| json                       | 5.26 ms                                                | 5.04 ms: 1.04x faster                                                            |
| sympy_expand               | 478 ms                                                 | 458 ms: 1.04x faster                                                             |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                           |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                             |
| fannkuch                   | 417 ms                                                 | 403 ms: 1.03x faster                                                             |
| sqlglot_optimize           | 54.8 ms                                                | 53.1 ms: 1.03x faster                                                            |
| json_loads                 | 28.5 us                                                | 27.8 us: 1.03x faster                                                            |
| logging_silent             | 104 ns                                                 | 102 ns: 1.03x faster                                                             |
| hexiom                     | 6.41 ms                                                | 6.26 ms: 1.02x faster                                                            |
| scimark_sor                | 129 ms                                                 | 127 ms: 1.02x faster                                                             |
| docutils                   | 2.77 sec                                               | 2.73 sec: 1.02x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.01x faster                                                             |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                            |
| pyflate                    | 482 ms                                                 | 477 ms: 1.01x faster                                                             |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                            |
| asyncio_tcp                | 491 ms                                                 | 487 ms: 1.01x faster                                                             |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                             |
| richards_super             | 51.5 ms                                                | 51.8 ms: 1.01x slower                                                            |
| django_template            | 34.6 ms                                                | 35.0 ms: 1.01x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                            |
| asyncio_websockets         | 551 ms                                                 | 560 ms: 1.02x slower                                                             |
| typing_runtime_protocols   | 158 us                                                 | 161 us: 1.02x slower                                                             |
| regex_effbot               | 3.61 ms                                                | 3.83 ms: 1.06x slower                                                            |
| regex_dna                  | 212 ms                                                 | 227 ms: 1.07x slower                                                             |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.09x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 26.4 ms: 1.14x slower                                                            |
| telco                      | 7.10 ms                                                | 8.11 ms: 1.14x slower                                                            |
| coverage                   | 72.7 ms                                                | 84.1 ms: 1.16x slower                                                            |
| create_gc_cycles           | 1.48 ms                                                | 1.72 ms: 1.17x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                     |

Benchmark hidden because not significant (6): xml_etree_parse, pycparser, richards, bench_mp_pool, asyncio_tcp_ssl, go
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240730-3.14.0a0-5efa5a5/bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.98x