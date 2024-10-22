# Results vs. 3.12.0

- fork: brandtbucher
- ref: tracing_jumps
- machine: linux-x86_64
- commit hash: f1f5d13
- commit date: 2024-07-24
- overall geometric mean: 1.08x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 276 ms: 1.01x slower                                                 |
| docutils       | 2.77 sec                                               | 2.90 sec: 1.05x slower                                               |
| tornado_http   | 103 ms                                                 | 93.7 ms: 1.10x faster                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.50x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                                 |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 402 ms: 1.44x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 529 ms: 1.37x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 863 ms: 1.37x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 899 ms: 1.29x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.40x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.2 ms: 1.21x faster                                                |
| float          | 84.7 ms                                                | 70.6 ms: 1.20x faster                                                |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.14x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.11x faster                                                 |
| regex_effbot   | 3.61 ms                                                | 3.97 ms: 1.10x slower                                                |
| regex_dna      | 212 ms                                                 | 237 ms: 1.12x slower                                                 |
| regex_v8       | 23.1 ms                                                | 26.4 ms: 1.14x slower                                                |
| Geometric mean | (ref)                                                  | 1.06x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 79.3 ms: 1.12x faster                                                |
| pickle_pure_python   | 324 us                                                 | 294 us: 1.10x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.08x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 99.1 ms: 1.08x faster                                                |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                                 |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.01x faster                                                |
| json_loads           | 28.5 us                                                | 28.2 us: 1.01x faster                                                |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.20 ms: 1.04x slower                                                |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.68 ms: 1.23x faster                                                |
| django_template | 34.6 ms                                                | 36.2 ms: 1.05x slower                                                |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.50x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                                 |
| async_tree_none            | 472 ms                                                 | 325 ms: 1.45x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 402 ms: 1.44x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 28.6 us: 1.43x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 529 ms: 1.37x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 863 ms: 1.37x faster                                                 |
| deepcopy                   | 371 us                                                 | 273 us: 1.36x faster                                                 |
| comprehensions             | 21.8 us                                                | 16.1 us: 1.35x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 563 ms: 1.29x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 899 ms: 1.29x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 60.1 ms: 1.25x faster                                                |
| mako                       | 11.9 ms                                                | 9.68 ms: 1.23x faster                                                |
| scimark_fft                | 382 ms                                                 | 312 ms: 1.23x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.75 us: 1.22x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 67.4 ms: 1.21x faster                                                |
| nbody                      | 97.0 ms                                                | 80.2 ms: 1.21x faster                                                |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                               |
| float                      | 84.7 ms                                                | 70.6 ms: 1.20x faster                                                |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                |
| logging_format             | 7.23 us                                                | 6.14 us: 1.18x faster                                                |
| raytrace                   | 312 ms                                                 | 266 ms: 1.17x faster                                                 |
| chaos                      | 67.0 ms                                                | 57.7 ms: 1.16x faster                                                |
| logging_simple             | 6.46 us                                                | 5.64 us: 1.15x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.44 ms: 1.14x faster                                                |
| pyflate                    | 482 ms                                                 | 424 ms: 1.14x faster                                                 |
| richards                   | 45.8 ms                                                | 40.5 ms: 1.13x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 79.3 ms: 1.12x faster                                                |
| fannkuch                   | 417 ms                                                 | 373 ms: 1.12x faster                                                 |
| regex_compile              | 148 ms                                                 | 134 ms: 1.11x faster                                                 |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.10x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 294 us: 1.10x faster                                                 |
| richards_super             | 51.5 ms                                                | 46.8 ms: 1.10x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                |
| tornado_http               | 103 ms                                                 | 93.7 ms: 1.10x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.08x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 99.1 ms: 1.08x faster                                                |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 734 ms: 1.06x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.05x faster                                                |
| gc_traversal               | 3.79 ms                                                | 3.62 ms: 1.05x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.56 ms: 1.04x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                               |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                               |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.03x faster                                                |
| json                       | 5.26 ms                                                | 5.09 ms: 1.03x faster                                                |
| bench_thread_pool          | 842 us                                                 | 818 us: 1.03x faster                                                 |
| dask                       | 372 ms                                                 | 362 ms: 1.03x faster                                                 |
| coroutines                 | 23.2 ms                                                | 22.6 ms: 1.03x faster                                                |
| async_generators           | 463 ms                                                 | 454 ms: 1.02x faster                                                 |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.01x faster                                                |
| json_loads                 | 28.5 us                                                | 28.2 us: 1.01x faster                                                |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                               |
| sympy_str                  | 300 ms                                                 | 297 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                 |
| 2to3                       | 274 ms                                                 | 276 ms: 1.01x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                               |
| sqlglot_optimize           | 54.8 ms                                                | 55.8 ms: 1.02x slower                                                |
| dulwich_log                | 68.5 ms                                                | 69.9 ms: 1.02x slower                                                |
| asyncio_tcp                | 491 ms                                                 | 504 ms: 1.03x slower                                                 |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.03x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.20 ms: 1.04x slower                                                |
| sympy_integrate            | 21.4 ms                                                | 22.4 ms: 1.04x slower                                                |
| go                         | 139 ms                                                 | 146 ms: 1.05x slower                                                 |
| docutils                   | 2.77 sec                                               | 2.90 sec: 1.05x slower                                               |
| django_template            | 34.6 ms                                                | 36.2 ms: 1.05x slower                                                |
| generators                 | 31.2 ms                                                | 32.8 ms: 1.05x slower                                                |
| hexiom                     | 6.41 ms                                                | 6.74 ms: 1.05x slower                                                |
| scimark_lu                 | 118 ms                                                 | 124 ms: 1.05x slower                                                 |
| sympy_expand               | 478 ms                                                 | 504 ms: 1.06x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                                 |
| regex_effbot               | 3.61 ms                                                | 3.97 ms: 1.10x slower                                                |
| telco                      | 7.10 ms                                                | 7.84 ms: 1.10x slower                                                |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                |
| regex_dna                  | 212 ms                                                 | 237 ms: 1.12x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 26.4 ms: 1.14x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.20x slower                                                |
| coverage                   | 72.7 ms                                                | 91.5 ms: 1.26x slower                                                |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                         |

Benchmark hidden because not significant (4): sympy_sum, bench_mp_pool, nqueens, scimark_sor
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240724-3.14.0a0-f1f5d13-JIT/bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.06x