# Results vs. 3.12.0

- fork: brandtbucher
- ref: trace_through
- machine: linux-x86_64
- commit hash: b1a2c42
- commit date: 2024-09-06
- overall geometric mean: 1.084x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 278 ms: 1.01x slower                                                 |
| docutils       | 2.77 sec                                               | 3.00 sec: 1.08x slower                                               |
| tornado_http   | 103 ms                                                 | 95.7 ms: 1.07x faster                                                |
| Geometric mean | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.46x faster                                                 |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 402 ms: 1.44x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 401 ms: 1.43x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 542 ms: 1.34x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 889 ms: 1.33x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 562 ms: 1.29x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 926 ms: 1.25x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.3 ms: 1.21x faster                                                |
| nbody          | 97.0 ms                                                | 81.0 ms: 1.20x faster                                                |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                  | 1.13x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.47 ms: 1.04x faster                                                |
| regex_compile  | 148 ms                                                 | 145 ms: 1.02x faster                                                 |
| regex_v8       | 23.1 ms                                                | 24.4 ms: 1.06x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.19x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 76.5 ms: 1.17x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 54.0 ms: 1.14x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 145 ms: 1.10x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 98.5 ms: 1.08x faster                                                |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                                 |
| unpickle             | 15.9 us                                                | 15.3 us: 1.04x faster                                                |
| pickle_dict          | 35.5 us                                                | 34.5 us: 1.03x faster                                                |
| unpickle_list        | 5.29 us                                                | 5.16 us: 1.02x faster                                                |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                |
| json_loads           | 28.5 us                                                | 28.7 us: 1.01x slower                                                |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                                |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                         |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.85 ms: 1.21x faster                                                |
| django_template | 34.6 ms                                                | 36.6 ms: 1.06x slower                                                |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.4 us: 1.54x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.46x faster                                                 |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 402 ms: 1.44x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 401 ms: 1.43x faster                                                 |
| deepcopy                   | 371 us                                                 | 264 us: 1.40x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 542 ms: 1.34x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 889 ms: 1.33x faster                                                 |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 562 ms: 1.29x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.62 us: 1.28x faster                                                |
| async_tree_io              | 1.16 sec                                               | 926 ms: 1.25x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 66.7 ms: 1.23x faster                                                |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.22x faster                                                |
| mako                       | 11.9 ms                                                | 9.85 ms: 1.21x faster                                                |
| scimark_fft                | 382 ms                                                 | 316 ms: 1.21x faster                                                 |
| float                      | 84.7 ms                                                | 70.3 ms: 1.21x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 62.7 ms: 1.20x faster                                                |
| nbody                      | 97.0 ms                                                | 81.0 ms: 1.20x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.11 ms: 1.20x faster                                                |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.19x faster                                               |
| richards_super             | 51.5 ms                                                | 44.0 ms: 1.17x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 76.5 ms: 1.17x faster                                                |
| logging_format             | 7.23 us                                                | 6.22 us: 1.16x faster                                                |
| richards                   | 45.8 ms                                                | 39.8 ms: 1.15x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 54.0 ms: 1.14x faster                                                |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.14x faster                                                 |
| chaos                      | 67.0 ms                                                | 58.7 ms: 1.14x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.43 ms: 1.14x faster                                                |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.67 us: 1.14x faster                                                |
| fannkuch                   | 417 ms                                                 | 374 ms: 1.11x faster                                                 |
| scimark_sor                | 129 ms                                                 | 116 ms: 1.11x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 145 ms: 1.10x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 98.5 ms: 1.08x faster                                                |
| pprint_safe_repr           | 776 ms                                                 | 716 ms: 1.08x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                 |
| pyflate                    | 482 ms                                                 | 449 ms: 1.08x faster                                                 |
| tornado_http               | 103 ms                                                 | 95.7 ms: 1.07x faster                                                |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                                 |
| gc_traversal               | 3.79 ms                                                | 3.59 ms: 1.06x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                               |
| logging_silent             | 104 ns                                                 | 100.0 ns: 1.04x faster                                               |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.04x faster                                                 |
| sqlite_synth               | 2.83 us                                                | 2.72 us: 1.04x faster                                                |
| regex_effbot               | 3.61 ms                                                | 3.47 ms: 1.04x faster                                                |
| go                         | 139 ms                                                 | 134 ms: 1.04x faster                                                 |
| unpickle                   | 15.9 us                                                | 15.3 us: 1.04x faster                                                |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                 |
| pickle_dict                | 35.5 us                                                | 34.5 us: 1.03x faster                                                |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.03x faster                                                |
| regex_compile              | 148 ms                                                 | 145 ms: 1.02x faster                                                 |
| unpickle_list              | 5.29 us                                                | 5.16 us: 1.02x faster                                                |
| asyncio_tcp                | 491 ms                                                 | 485 ms: 1.01x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.67 ms: 1.01x faster                                                |
| bench_thread_pool          | 842 us                                                 | 834 us: 1.01x faster                                                 |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                |
| async_generators           | 463 ms                                                 | 460 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.01x slower                                                 |
| json_loads                 | 28.5 us                                                | 28.7 us: 1.01x slower                                                |
| json                       | 5.26 ms                                                | 5.30 ms: 1.01x slower                                                |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                                |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                               |
| 2to3                       | 274 ms                                                 | 278 ms: 1.01x slower                                                 |
| sympy_str                  | 300 ms                                                 | 304 ms: 1.01x slower                                                 |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.02x slower                                                 |
| dulwich_log                | 68.5 ms                                                | 70.7 ms: 1.03x slower                                                |
| mdp                        | 2.63 sec                                               | 2.72 sec: 1.03x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                |
| nqueens                    | 83.3 ms                                                | 86.1 ms: 1.03x slower                                                |
| sympy_sum                  | 169 ms                                                 | 175 ms: 1.04x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 24.4 ms: 1.06x slower                                                |
| django_template            | 34.6 ms                                                | 36.6 ms: 1.06x slower                                                |
| generators                 | 31.2 ms                                                | 33.0 ms: 1.06x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                 |
| sympy_expand               | 478 ms                                                 | 507 ms: 1.06x slower                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 58.4 ms: 1.06x slower                                                |
| sympy_integrate            | 21.4 ms                                                | 23.0 ms: 1.07x slower                                                |
| docutils                   | 2.77 sec                                               | 3.00 sec: 1.08x slower                                               |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                |
| telco                      | 7.10 ms                                                | 7.99 ms: 1.13x slower                                                |
| coverage                   | 72.7 ms                                                | 85.8 ms: 1.18x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                |
| hexiom                     | 6.41 ms                                                | 7.73 ms: 1.21x slower                                                |
| unpack_sequence            | 54.0 ns                                                | 139 ns: 2.57x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                         |

Benchmark hidden because not significant (4): regex_dna, bench_mp_pool, pickle_list, pycparser
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240906-3.14.0a0-b1a2c42-JIT/bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.084x faster
# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x