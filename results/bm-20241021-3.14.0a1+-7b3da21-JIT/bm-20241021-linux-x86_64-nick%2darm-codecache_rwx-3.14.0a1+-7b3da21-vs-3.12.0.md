# Results vs. 3.12.0

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 271 ms: 1.01x faster                                                |
| docutils       | 2.77 sec                                               | 2.88 sec: 1.04x slower                                              |
| tornado_http   | 103 ms                                                 | 94.0 ms: 1.09x faster                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 380 ms: 1.51x faster                                                |
| async_tree_none            | 472 ms                                                 | 338 ms: 1.40x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 323 ms: 1.39x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 417 ms: 1.39x faster                                                |
| async_tree_io              | 1.16 sec                                               | 861 ms: 1.34x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 557 ms: 1.30x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 573 ms: 1.27x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 963 ms: 1.23x faster                                                |
| Geometric mean             | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 82.4 ms: 1.18x faster                                               |
| float          | 84.7 ms                                                | 75.6 ms: 1.12x faster                                               |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                  | 1.10x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 135 ms: 1.10x faster                                                |
| regex_dna      | 212 ms                                                 | 212 ms: 1.00x faster                                                |
| regex_effbot   | 3.61 ms                                                | 3.65 ms: 1.01x slower                                               |
| regex_v8       | 23.1 ms                                                | 24.4 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.21x faster                                              |
| xml_etree_generate   | 89.2 ms                                                | 78.3 ms: 1.14x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 54.8 ms: 1.13x faster                                               |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                |
| json_loads           | 28.5 us                                                | 26.6 us: 1.07x faster                                               |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 100 ms: 1.06x faster                                                |
| pickle_pure_python   | 324 us                                                 | 313 us: 1.03x faster                                                |
| json_dumps           | 10.4 ms                                                | 10.8 ms: 1.04x slower                                               |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                               |
| python_startup         | 9.55 ms                                                | 11.8 ms: 1.24x slower                                               |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.0 ms: 1.19x faster                                               |
| django_template | 34.6 ms                                                | 35.4 ms: 1.02x slower                                               |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 380 ms: 1.51x faster                                                |
| deepcopy                   | 371 us                                                 | 266 us: 1.40x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 29.2 us: 1.40x faster                                               |
| async_tree_none            | 472 ms                                                 | 338 ms: 1.40x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 323 ms: 1.39x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 417 ms: 1.39x faster                                                |
| async_tree_io              | 1.16 sec                                               | 861 ms: 1.34x faster                                                |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 557 ms: 1.30x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 573 ms: 1.27x faster                                                |
| richards                   | 45.8 ms                                                | 37.1 ms: 1.23x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 963 ms: 1.23x faster                                                |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.21x faster                                              |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 68.4 ms: 1.20x faster                                               |
| logging_format             | 7.23 us                                                | 6.08 us: 1.19x faster                                               |
| scimark_fft                | 382 ms                                                 | 322 ms: 1.19x faster                                                |
| mako                       | 11.9 ms                                                | 10.0 ms: 1.19x faster                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 63.5 ms: 1.18x faster                                               |
| nbody                      | 97.0 ms                                                | 82.4 ms: 1.18x faster                                               |
| richards_super             | 51.5 ms                                                | 43.8 ms: 1.18x faster                                               |
| logging_simple             | 6.46 us                                                | 5.57 us: 1.16x faster                                               |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.24 ms: 1.15x faster                                               |
| chaos                      | 67.0 ms                                                | 58.6 ms: 1.14x faster                                               |
| xml_etree_generate         | 89.2 ms                                                | 78.3 ms: 1.14x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 689 ms: 1.13x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 54.8 ms: 1.13x faster                                               |
| float                      | 84.7 ms                                                | 75.6 ms: 1.12x faster                                               |
| fannkuch                   | 417 ms                                                 | 375 ms: 1.11x faster                                                |
| regex_compile              | 148 ms                                                 | 135 ms: 1.10x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.43 sec: 1.10x faster                                              |
| tornado_http               | 103 ms                                                 | 94.0 ms: 1.09x faster                                               |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                                |
| pyflate                    | 482 ms                                                 | 447 ms: 1.08x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                |
| json_loads                 | 28.5 us                                                | 26.6 us: 1.07x faster                                               |
| go                         | 139 ms                                                 | 130 ms: 1.07x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                                |
| json                       | 5.26 ms                                                | 4.93 ms: 1.07x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 100 ms: 1.06x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.77 ms: 1.06x faster                                               |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                              |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.04x faster                                                |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.03x faster                                              |
| pickle_pure_python         | 324 us                                                 | 313 us: 1.03x faster                                                |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                |
| dulwich_log                | 68.5 ms                                                | 66.5 ms: 1.03x faster                                               |
| async_generators           | 463 ms                                                 | 449 ms: 1.03x faster                                                |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                               |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.02x faster                                               |
| sympy_str                  | 300 ms                                                 | 296 ms: 1.01x faster                                                |
| sqlglot_transpile          | 1.68 ms                                                | 1.67 ms: 1.01x faster                                               |
| 2to3                       | 274 ms                                                 | 271 ms: 1.01x faster                                                |
| regex_dna                  | 212 ms                                                 | 212 ms: 1.00x faster                                                |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.01x slower                                                |
| regex_effbot               | 3.61 ms                                                | 3.65 ms: 1.01x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                               |
| django_template            | 34.6 ms                                                | 35.4 ms: 1.02x slower                                               |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.03x slower                                                |
| sympy_sum                  | 169 ms                                                 | 174 ms: 1.03x slower                                                |
| sympy_expand               | 478 ms                                                 | 494 ms: 1.03x slower                                                |
| docutils                   | 2.77 sec                                               | 2.88 sec: 1.04x slower                                              |
| json_dumps                 | 10.4 ms                                                | 10.8 ms: 1.04x slower                                               |
| bench_thread_pool          | 842 us                                                 | 879 us: 1.04x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                |
| regex_v8                   | 23.1 ms                                                | 24.4 ms: 1.05x slower                                               |
| sqlglot_optimize           | 54.8 ms                                                | 58.3 ms: 1.06x slower                                               |
| nqueens                    | 83.3 ms                                                | 89.4 ms: 1.07x slower                                               |
| sympy_integrate            | 21.4 ms                                                | 23.1 ms: 1.08x slower                                               |
| hexiom                     | 6.41 ms                                                | 6.91 ms: 1.08x slower                                               |
| telco                      | 7.10 ms                                                | 7.71 ms: 1.09x slower                                               |
| generators                 | 31.2 ms                                                | 35.1 ms: 1.13x slower                                               |
| coverage                   | 72.7 ms                                                | 84.3 ms: 1.16x slower                                               |
| python_startup             | 9.55 ms                                                | 11.8 ms: 1.24x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.74 ms: 1.25x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.67 ms: 1.81x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 83.4 ms: 3.47x slower                                               |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (1): logging_silent
Ignored benchmarks (16) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241021-3.14.0a1+-7b3da21-JIT/bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.15x