# Results vs. 3.12.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-x86_64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.023x faster
- HPT reliability: 85.78%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 283 ms: 1.01x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.88 sec: 1.00x slower                                                      |
| tornado_http   | 121 ms                                                       | 115 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 319 ms: 1.41x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 309 ms: 1.40x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 392 ms: 1.38x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 401 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 786 ms: 1.34x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 821 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 561 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 571 ms: 1.22x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| nbody          | 88.0 ms                                                      | 89.9 ms: 1.02x slower                                                       |
| float          | 76.6 ms                                                      | 78.8 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.48 ms: 1.03x faster                                                       |
| regex_dna      | 239 ms                                                       | 242 ms: 1.01x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 25.0 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 318 us                                                       | 315 us: 1.01x faster                                                        |
| pickle_dict          | 32.5 us                                                      | 32.8 us: 1.01x slower                                                       |
| unpickle             | 14.8 us                                                      | 15.1 us: 1.02x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 4.76 us: 1.02x slower                                                       |
| pickle               | 10.5 us                                                      | 10.8 us: 1.02x slower                                                       |
| json_loads           | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 218 us: 1.04x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 150 ms: 1.04x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 61.4 ms: 1.05x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.8 ms: 1.06x slower                                                       |
| pickle_list          | 4.43 us                                                      | 4.71 us: 1.06x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.54 sec: 1.18x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.95 ms: 1.04x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| django_template | 38.2 ms                                                      | 39.9 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 319 ms: 1.41x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 309 ms: 1.40x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 392 ms: 1.38x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 401 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 786 ms: 1.34x faster                                                        |
| deepcopy                   | 368 us                                                       | 284 us: 1.30x faster                                                        |
| generators                 | 37.4 ms                                                      | 29.1 ms: 1.29x faster                                                       |
| comprehensions             | 21.9 us                                                      | 17.1 us: 1.28x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 821 ms: 1.27x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 29.5 us: 1.25x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 561 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 571 ms: 1.22x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.8 ms: 1.19x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.90 us: 1.16x faster                                                       |
| go                         | 150 ms                                                       | 135 ms: 1.11x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.80 us: 1.10x faster                                                       |
| raytrace                   | 298 ms                                                       | 273 ms: 1.09x faster                                                        |
| async_generators           | 390 ms                                                       | 358 ms: 1.09x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 74.2 ms: 1.08x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.08x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.28 us: 1.07x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 93.5 ms: 1.06x faster                                                       |
| tornado_http               | 121 ms                                                       | 115 ms: 1.05x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.9 ms: 1.05x faster                                                       |
| unpack_sequence            | 53.2 ns                                                      | 50.7 ns: 1.05x faster                                                       |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| sympy_str                  | 302 ms                                                       | 289 ms: 1.05x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.48 sec: 1.04x faster                                                      |
| bench_thread_pool          | 950 us                                                       | 919 us: 1.03x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 67.1 ms: 1.03x faster                                                       |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.48 ms: 1.03x faster                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.72 us: 1.02x faster                                                       |
| chaos                      | 64.0 ms                                                      | 63.0 ms: 1.02x faster                                                       |
| nqueens                    | 89.9 ms                                                      | 88.8 ms: 1.01x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 315 us: 1.01x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.01x faster                                                      |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 374 ms: 1.01x faster                                                        |
| 2to3                       | 285 ms                                                       | 283 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                      |
| pprint_safe_repr           | 807 ms                                                       | 803 ms: 1.01x faster                                                        |
| docutils                   | 2.87 sec                                                     | 2.88 sec: 1.00x slower                                                      |
| pickle_dict                | 32.5 us                                                      | 32.8 us: 1.01x slower                                                       |
| asyncio_websockets         | 387 ms                                                       | 390 ms: 1.01x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.01x slower                                                      |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 117 ms: 1.01x slower                                                        |
| sympy_expand               | 484 ms                                                       | 491 ms: 1.01x slower                                                        |
| fannkuch                   | 350 ms                                                       | 355 ms: 1.01x slower                                                        |
| regex_dna                  | 239 ms                                                       | 242 ms: 1.01x slower                                                        |
| unpickle                   | 14.8 us                                                      | 15.1 us: 1.02x slower                                                       |
| dulwich_log                | 65.4 ms                                                      | 66.6 ms: 1.02x slower                                                       |
| nbody                      | 88.0 ms                                                      | 89.9 ms: 1.02x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 58.8 ms: 1.02x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 4.76 us: 1.02x slower                                                       |
| pickle                     | 10.5 us                                                      | 10.8 us: 1.02x slower                                                       |
| float                      | 76.6 ms                                                      | 78.8 ms: 1.03x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.1 us: 1.03x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.95 ms: 1.04x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.35 ms: 1.04x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 218 us: 1.04x slower                                                        |
| xml_etree_parse            | 144 ms                                                       | 150 ms: 1.04x slower                                                        |
| json                       | 5.12 ms                                                      | 5.34 ms: 1.04x slower                                                       |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.23 ms: 1.04x slower                                                       |
| django_template            | 38.2 ms                                                      | 39.9 ms: 1.05x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.41 ms: 1.05x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 61.4 ms: 1.05x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 99.3 ns: 1.05x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 25.0 ms: 1.06x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.8 ms: 1.06x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 97.2 ms: 1.06x slower                                                       |
| pickle_list                | 4.43 us                                                      | 4.71 us: 1.06x slower                                                       |
| scimark_sor                | 109 ms                                                       | 118 ms: 1.08x slower                                                        |
| richards                   | 45.7 ms                                                      | 51.2 ms: 1.12x slower                                                       |
| richards_super             | 51.3 ms                                                      | 57.9 ms: 1.13x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 173 us: 1.14x slower                                                        |
| python_startup             | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                       |
| pyflate                    | 439 ms                                                       | 504 ms: 1.15x slower                                                        |
| telco                      | 6.96 ms                                                      | 8.19 ms: 1.18x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.54 sec: 1.18x slower                                                      |
| create_gc_cycles           | 1.59 ms                                                      | 2.03 ms: 1.28x slower                                                       |
| coverage                   | 66.7 ms                                                      | 85.7 ms: 1.29x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.81 ms: 1.38x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 1.33 sec: 279.16x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (3): scimark_fft, xml_etree_iterparse, xml_etree_generate
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.023x faster
# HPT report

- Reliability score: 85.78% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x