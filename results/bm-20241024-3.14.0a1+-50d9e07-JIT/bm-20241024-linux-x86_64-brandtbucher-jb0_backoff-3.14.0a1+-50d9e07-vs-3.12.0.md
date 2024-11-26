# Results vs. 3.12.0

- fork: brandtbucher
- ref: jb0_backoff
- machine: linux-x86_64
- commit hash: 50d9e07
- commit date: 2024-10-24
- overall geometric mean: 1.013x faster
- HPT reliability: 86.08%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 286 ms: 1.04x slower                                                |
| docutils       | 2.77 sec                                               | 3.40 sec: 1.23x slower                                              |
| tornado_http   | 103 ms                                                 | 112 ms: 1.09x slower                                                |
| Geometric mean | (ref)                                                  | 1.12x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 405 ms: 1.42x faster                                                |
| async_tree_none            | 472 ms                                                 | 347 ms: 1.36x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 338 ms: 1.33x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 434 ms: 1.33x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 959 ms: 1.23x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 589 ms: 1.23x faster                                                |
| async_tree_io              | 1.16 sec                                               | 941 ms: 1.23x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 599 ms: 1.21x faster                                                |
| Geometric mean             | (ref)                                                  | 1.29x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 81.7 ms: 1.19x faster                                               |
| float          | 84.7 ms                                                | 75.0 ms: 1.13x faster                                               |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                  | 1.10x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 146 ms: 1.01x faster                                                |
| regex_dna      | 212 ms                                                 | 215 ms: 1.02x slower                                                |
| regex_effbot   | 3.61 ms                                                | 3.71 ms: 1.03x slower                                               |
| regex_v8       | 23.1 ms                                                | 25.8 ms: 1.12x slower                                               |
| Geometric mean | (ref)                                                  | 1.04x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                              |
| pickle_pure_python   | 324 us                                                 | 294 us: 1.10x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 83.3 ms: 1.07x faster                                               |
| json_loads           | 28.5 us                                                | 26.7 us: 1.07x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 100 ms: 1.06x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 60.1 ms: 1.03x faster                                               |
| unpickle_pure_python | 230 us                                                 | 226 us: 1.02x faster                                                |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                               |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.11 ms: 1.02x slower                                               |
| python_startup         | 9.55 ms                                                | 11.9 ms: 1.25x slower                                               |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.2 ms: 1.17x faster                                               |
| django_template | 34.6 ms                                                | 40.5 ms: 1.17x slower                                               |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 405 ms: 1.42x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 29.7 us: 1.37x faster                                               |
| async_tree_none            | 472 ms                                                 | 347 ms: 1.36x faster                                                |
| deepcopy                   | 371 us                                                 | 277 us: 1.34x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 338 ms: 1.33x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 434 ms: 1.33x faster                                                |
| comprehensions             | 21.8 us                                                | 17.4 us: 1.25x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 959 ms: 1.23x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 589 ms: 1.23x faster                                                |
| async_tree_io              | 1.16 sec                                               | 941 ms: 1.23x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 61.7 ms: 1.22x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 599 ms: 1.21x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 67.9 ms: 1.21x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                              |
| scimark_fft                | 382 ms                                                 | 321 ms: 1.19x faster                                                |
| nbody                      | 97.0 ms                                                | 81.7 ms: 1.19x faster                                               |
| mako                       | 11.9 ms                                                | 10.2 ms: 1.17x faster                                               |
| pathlib                    | 19.3 ms                                                | 16.6 ms: 1.17x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.91 us: 1.15x faster                                               |
| float                      | 84.7 ms                                                | 75.0 ms: 1.13x faster                                               |
| chaos                      | 67.0 ms                                                | 59.8 ms: 1.12x faster                                               |
| pickle_pure_python         | 324 us                                                 | 294 us: 1.10x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                |
| fannkuch                   | 417 ms                                                 | 384 ms: 1.09x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.66 ms: 1.08x faster                                               |
| pyflate                    | 482 ms                                                 | 446 ms: 1.08x faster                                                |
| go                         | 139 ms                                                 | 129 ms: 1.08x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 83.3 ms: 1.07x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 726 ms: 1.07x faster                                                |
| json_loads                 | 28.5 us                                                | 26.7 us: 1.07x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 100 ms: 1.06x faster                                                |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                              |
| json                       | 5.26 ms                                                | 4.99 ms: 1.05x faster                                               |
| raytrace                   | 312 ms                                                 | 296 ms: 1.05x faster                                                |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.04x faster                                                |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 60.1 ms: 1.03x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 226 us: 1.02x faster                                                |
| regex_compile              | 148 ms                                                 | 146 ms: 1.01x faster                                                |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                |
| async_generators           | 463 ms                                                 | 467 ms: 1.01x slower                                                |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                                |
| logging_silent             | 104 ns                                                 | 106 ns: 1.01x slower                                                |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.02x slower                                                |
| dulwich_log                | 68.5 ms                                                | 70.0 ms: 1.02x slower                                               |
| mdp                        | 2.63 sec                                               | 2.69 sec: 1.02x slower                                              |
| python_startup_no_site     | 6.94 ms                                                | 7.11 ms: 1.02x slower                                               |
| regex_effbot               | 3.61 ms                                                | 3.71 ms: 1.03x slower                                               |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.03x slower                                                |
| 2to3                       | 274 ms                                                 | 286 ms: 1.04x slower                                                |
| logging_format             | 7.23 us                                                | 7.57 us: 1.05x slower                                               |
| sqlglot_parse              | 1.36 ms                                                | 1.43 ms: 1.05x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                |
| richards_super             | 51.5 ms                                                | 54.7 ms: 1.06x slower                                               |
| richards                   | 45.8 ms                                                | 48.8 ms: 1.06x slower                                               |
| telco                      | 7.10 ms                                                | 7.61 ms: 1.07x slower                                               |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                               |
| nqueens                    | 83.3 ms                                                | 89.3 ms: 1.07x slower                                               |
| pycparser                  | 1.18 sec                                               | 1.27 sec: 1.08x slower                                              |
| logging_simple             | 6.46 us                                                | 7.01 us: 1.09x slower                                               |
| sqlglot_normalize          | 110 ms                                                 | 120 ms: 1.09x slower                                                |
| deltablue                  | 3.72 ms                                                | 4.04 ms: 1.09x slower                                               |
| tornado_http               | 103 ms                                                 | 112 ms: 1.09x slower                                                |
| sqlglot_transpile          | 1.68 ms                                                | 1.85 ms: 1.10x slower                                               |
| sympy_expand               | 478 ms                                                 | 533 ms: 1.11x slower                                                |
| sympy_str                  | 300 ms                                                 | 334 ms: 1.11x slower                                                |
| regex_v8                   | 23.1 ms                                                | 25.8 ms: 1.12x slower                                               |
| coroutines                 | 23.2 ms                                                | 26.4 ms: 1.14x slower                                               |
| bench_thread_pool          | 842 us                                                 | 969 us: 1.15x slower                                                |
| hexiom                     | 6.41 ms                                                | 7.44 ms: 1.16x slower                                               |
| django_template            | 34.6 ms                                                | 40.5 ms: 1.17x slower                                               |
| generators                 | 31.2 ms                                                | 36.6 ms: 1.17x slower                                               |
| coverage                   | 72.7 ms                                                | 86.4 ms: 1.19x slower                                               |
| sqlalchemy_declarative     | 147 ms                                                 | 175 ms: 1.19x slower                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 22.5 ms: 1.21x slower                                               |
| sqlglot_optimize           | 54.8 ms                                                | 66.7 ms: 1.22x slower                                               |
| sympy_sum                  | 169 ms                                                 | 206 ms: 1.22x slower                                                |
| docutils                   | 2.77 sec                                               | 3.40 sec: 1.23x slower                                              |
| python_startup             | 9.55 ms                                                | 11.9 ms: 1.25x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.74 ms: 1.25x slower                                               |
| sympy_integrate            | 21.4 ms                                                | 27.3 ms: 1.28x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.66 ms: 1.80x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 89.0 ms: 3.71x slower                                               |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                        |
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241024-3.14.0a1+-50d9e07-JIT/bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.013x faster
# HPT report

- Reliability score: 86.08% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.18x