# Results vs. 3.12.0

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: c2fad93
- commit date: 2024-10-17
- overall geometric mean: 1.04x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 278 ms: 1.01x slower                                           |
| docutils       | 2.77 sec                                               | 2.96 sec: 1.07x slower                                         |
| tornado_http   | 103 ms                                                 | 94.9 ms: 1.08x faster                                          |
| Geometric mean | (ref)                                                  | 1.00x slower                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 388 ms: 1.48x faster                                           |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.46x faster                                           |
| async_tree_none            | 472 ms                                                 | 331 ms: 1.43x faster                                           |
| async_tree_memoization     | 578 ms                                                 | 429 ms: 1.35x faster                                           |
| async_tree_io_tg           | 1.18 sec                                               | 890 ms: 1.33x faster                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 555 ms: 1.31x faster                                           |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 561 ms: 1.29x faster                                           |
| async_tree_io              | 1.16 sec                                               | 897 ms: 1.29x faster                                           |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.3 ms: 1.22x faster                                          |
| float          | 84.7 ms                                                | 74.3 ms: 1.14x faster                                          |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                  | 1.12x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 138 ms: 1.07x faster                                           |
| regex_effbot   | 3.61 ms                                                | 3.81 ms: 1.06x slower                                          |
| regex_dna      | 212 ms                                                 | 229 ms: 1.08x slower                                           |
| regex_v8       | 23.1 ms                                                | 26.8 ms: 1.16x slower                                          |
| Geometric mean | (ref)                                                  | 1.05x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                         |
| xml_etree_generate   | 89.2 ms                                                | 78.6 ms: 1.13x faster                                          |
| xml_etree_process    | 61.7 ms                                                | 54.8 ms: 1.13x faster                                          |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.09x faster                                           |
| unpickle             | 15.9 us                                                | 14.6 us: 1.08x faster                                          |
| xml_etree_iterparse  | 107 ms                                                 | 99.5 ms: 1.07x faster                                          |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                           |
| pickle_pure_python   | 324 us                                                 | 304 us: 1.07x faster                                           |
| json_loads           | 28.5 us                                                | 26.8 us: 1.06x faster                                          |
| unpickle_list        | 5.29 us                                                | 5.11 us: 1.03x faster                                          |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.02x faster                                          |
| pickle_dict          | 35.5 us                                                | 35.0 us: 1.01x faster                                          |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                          |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                   |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.07 ms: 1.02x slower                                          |
| python_startup         | 9.55 ms                                                | 11.9 ms: 1.24x slower                                          |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.87 ms: 1.21x faster                                          |
| django_template | 34.6 ms                                                | 36.7 ms: 1.06x slower                                          |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.8 us: 1.52x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 388 ms: 1.48x faster                                           |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.46x faster                                           |
| async_tree_none            | 472 ms                                                 | 331 ms: 1.43x faster                                           |
| deepcopy                   | 371 us                                                 | 262 us: 1.41x faster                                           |
| async_tree_memoization     | 578 ms                                                 | 429 ms: 1.35x faster                                           |
| async_tree_io_tg           | 1.18 sec                                               | 890 ms: 1.33x faster                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 555 ms: 1.31x faster                                           |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 561 ms: 1.29x faster                                           |
| async_tree_io              | 1.16 sec                                               | 897 ms: 1.29x faster                                           |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.27x faster                                          |
| deepcopy_reduce            | 3.35 us                                                | 2.64 us: 1.27x faster                                          |
| scimark_fft                | 382 ms                                                 | 303 ms: 1.26x faster                                           |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.22x faster                                          |
| nbody                      | 97.0 ms                                                | 79.3 ms: 1.22x faster                                          |
| crypto_pyaes               | 81.9 ms                                                | 67.0 ms: 1.22x faster                                          |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                         |
| mako                       | 11.9 ms                                                | 9.87 ms: 1.21x faster                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 62.8 ms: 1.20x faster                                          |
| logging_format             | 7.23 us                                                | 6.14 us: 1.18x faster                                          |
| logging_simple             | 6.46 us                                                | 5.58 us: 1.16x faster                                          |
| deltablue                  | 3.72 ms                                                | 3.22 ms: 1.15x faster                                          |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.40 ms: 1.15x faster                                          |
| float                      | 84.7 ms                                                | 74.3 ms: 1.14x faster                                          |
| xml_etree_generate         | 89.2 ms                                                | 78.6 ms: 1.13x faster                                          |
| xml_etree_process          | 61.7 ms                                                | 54.8 ms: 1.13x faster                                          |
| raytrace                   | 312 ms                                                 | 277 ms: 1.13x faster                                           |
| chaos                      | 67.0 ms                                                | 59.5 ms: 1.13x faster                                          |
| pprint_safe_repr           | 776 ms                                                 | 697 ms: 1.11x faster                                           |
| richards_super             | 51.5 ms                                                | 46.9 ms: 1.10x faster                                          |
| logging_silent             | 104 ns                                                 | 96.0 ns: 1.09x faster                                          |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.09x faster                                           |
| unpickle                   | 15.9 us                                                | 14.6 us: 1.08x faster                                          |
| fannkuch                   | 417 ms                                                 | 385 ms: 1.08x faster                                           |
| tornado_http               | 103 ms                                                 | 94.9 ms: 1.08x faster                                          |
| scimark_lu                 | 118 ms                                                 | 109 ms: 1.08x faster                                           |
| richards                   | 45.8 ms                                                | 42.6 ms: 1.08x faster                                          |
| xml_etree_iterparse        | 107 ms                                                 | 99.5 ms: 1.07x faster                                          |
| regex_compile              | 148 ms                                                 | 138 ms: 1.07x faster                                           |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                           |
| pickle_pure_python         | 324 us                                                 | 304 us: 1.07x faster                                           |
| pyflate                    | 482 ms                                                 | 453 ms: 1.07x faster                                           |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.06x faster                                         |
| json_loads                 | 28.5 us                                                | 26.8 us: 1.06x faster                                          |
| go                         | 139 ms                                                 | 132 ms: 1.06x faster                                           |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                           |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                           |
| json                       | 5.26 ms                                                | 5.06 ms: 1.04x faster                                          |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                         |
| unpickle_list              | 5.29 us                                                | 5.11 us: 1.03x faster                                          |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.03x faster                                           |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                          |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.02x faster                                          |
| coroutines                 | 23.2 ms                                                | 22.6 ms: 1.02x faster                                          |
| dulwich_log                | 68.5 ms                                                | 66.9 ms: 1.02x faster                                          |
| pickle_dict                | 35.5 us                                                | 35.0 us: 1.01x faster                                          |
| sqlite_synth               | 2.83 us                                                | 2.81 us: 1.01x faster                                          |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                           |
| sympy_str                  | 300 ms                                                 | 301 ms: 1.00x slower                                           |
| asyncio_websockets         | 551 ms                                                 | 559 ms: 1.01x slower                                           |
| 2to3                       | 274 ms                                                 | 278 ms: 1.01x slower                                           |
| asyncio_tcp                | 491 ms                                                 | 498 ms: 1.02x slower                                           |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.02x slower                                         |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                          |
| python_startup_no_site     | 6.94 ms                                                | 7.07 ms: 1.02x slower                                          |
| pycparser                  | 1.18 sec                                               | 1.22 sec: 1.03x slower                                         |
| sqlglot_normalize          | 110 ms                                                 | 115 ms: 1.04x slower                                           |
| sympy_sum                  | 169 ms                                                 | 176 ms: 1.04x slower                                           |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                           |
| sympy_expand               | 478 ms                                                 | 502 ms: 1.05x slower                                           |
| regex_effbot               | 3.61 ms                                                | 3.81 ms: 1.06x slower                                          |
| django_template            | 34.6 ms                                                | 36.7 ms: 1.06x slower                                          |
| bench_thread_pool          | 842 us                                                 | 897 us: 1.07x slower                                           |
| docutils                   | 2.77 sec                                               | 2.96 sec: 1.07x slower                                         |
| nqueens                    | 83.3 ms                                                | 89.3 ms: 1.07x slower                                          |
| telco                      | 7.10 ms                                                | 7.64 ms: 1.08x slower                                          |
| regex_dna                  | 212 ms                                                 | 229 ms: 1.08x slower                                           |
| sqlglot_optimize           | 54.8 ms                                                | 59.7 ms: 1.09x slower                                          |
| hexiom                     | 6.41 ms                                                | 6.99 ms: 1.09x slower                                          |
| sympy_integrate            | 21.4 ms                                                | 23.4 ms: 1.09x slower                                          |
| gc_traversal               | 3.79 ms                                                | 4.29 ms: 1.13x slower                                          |
| generators                 | 31.2 ms                                                | 35.4 ms: 1.13x slower                                          |
| regex_v8                   | 23.1 ms                                                | 26.8 ms: 1.16x slower                                          |
| coverage                   | 72.7 ms                                                | 84.9 ms: 1.17x slower                                          |
| python_startup             | 9.55 ms                                                | 11.9 ms: 1.24x slower                                          |
| create_gc_cycles           | 1.48 ms                                                | 2.60 ms: 1.76x slower                                          |
| unpack_sequence            | 54.0 ns                                                | 108 ns: 2.00x slower                                           |
| bench_mp_pool              | 24.0 ms                                                | 84.4 ms: 3.52x slower                                          |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                   |

Benchmark hidden because not significant (3): sqlglot_transpile, async_generators, pickle_list
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20241017-3.14.0a0-c2fad93-JIT/bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.15x